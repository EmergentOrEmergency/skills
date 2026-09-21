# Inference

Covers: loading the model, preprocessing and letterboxing, quantization, running the interpreter, decoding the output tensors, NMS, delegates, and the parity test that holds it all together.

## Contents

- [Loading the model](#loading-the-model)
- [Preprocessing and letterboxing](#preprocessing-and-letterboxing)
- [Quantization](#quantization)
- [Running the interpreter](#running-the-interpreter)
- [Discovering the output layout](#discovering-the-output-layout)
- [Common decoders](#common-decoders)
- [Non-maximum suppression](#non-maximum-suppression)
- [Delegates](#delegates)
- [The golden-image parity test](#the-golden-image-parity-test)

## Loading the model

Memory-map the model from assets rather than reading it into a byte array. A mapped file is shared, not copied, which matters for a multi-megabyte detector on a low-memory device.

```kotlin
private fun loadMapped(context: Context, assetPath: String): MappedByteBuffer {
    context.assets.openFd(assetPath).use { fd ->
        FileInputStream(fd.fileDescriptor).use { input ->
            return input.channel.map(
                FileChannel.MapMode.READ_ONLY, fd.startOffset, fd.declaredLength,
            )
        }
    }
}
```

`openFd` throws for a compressed asset, so the build must exclude `.tflite` from asset compression — see [project-setup.md](project-setup.md). That exception is the classic first-run crash on this stack, and its message does not mention compression.

Load the model's metadata manifest in the same step and validate it. Compare the artifact's SHA-256 against the manifest, and compare the manifest's declared input shape and dtype against `interpreter.getInputTensor(0)`. Two sources of truth that agree are worth the few lines; when they disagree, you want to know at startup rather than through degraded recall in the field.

## Preprocessing and letterboxing

Resize to the model's input size while preserving aspect ratio, padding the remainder with a constant colour. Stretching instead distorts the objects away from what the model saw in training, and costs accuracy in a way that is hard to attribute later.

Record the scale factor and the pad offsets. They are the inverse transform that turns model-space boxes back into frame-space boxes, and [overlay-and-tracking.md](overlay-and-tracking.md) depends on them.

```kotlin
data class Letterbox(val scale: Float, val padX: Float, val padY: Float)

fun letterboxFor(srcW: Int, srcH: Int, dstW: Int, dstH: Int): Letterbox {
    val scale = minOf(dstW.toFloat() / srcW, dstH.toFloat() / srcH)
    return Letterbox(scale, (dstW - srcW * scale) / 2f, (dstH - srcH * scale) / 2f)
}
```

Use the pad colour the training pipeline used when it is documented (Ultralytics pads with grey `114`); it is a small effect, but a free one.

Allocate the input `ByteBuffer` once and reuse it. It must be `allocateDirect` with `order(ByteOrder.nativeOrder())`, and rewound before every run — a buffer left at its end position produces a `BufferOverflowException` or, worse, a silently stale inference.

## Quantization

This is where hand-written preprocessing most often goes wrong, because the wrong version still runs.

**When the input tensor is `uint8`**, write raw pixel bytes in `0..255`. Do not normalize. The tensor's `scale` and `zeroPoint` describe how the graph interprets those bytes internally — they are not an instruction to the app. A manifest reading `scale: 0.0078125, zeroPoint: 128` means the graph treats the byte as `(b - 128) / 128`; applying that yourself and casting back to a byte destroys the signal.

**When the input tensor is `float32`**, apply exactly the normalization the training pipeline used — commonly `x / 255.0`, sometimes mean/std per channel. Take it from the manifest, not from a guess.

Read the truth from the model rather than trusting documentation:

```kotlin
val input = interpreter.getInputTensor(0)
val params = input.quantizationParams()   // scale, zeroPoint
val dtype = input.dataType()              // UINT8 / FLOAT32
```

Quantized outputs need dequantizing on the way out: `real = scale * (quantized - zeroPoint)`. A confidence score that clusters oddly around small integers, or a "0.5 threshold" that lets everything through, usually means an output was read raw.

## Running the interpreter

```kotlin
val options = Interpreter.Options().apply { numThreads = 4 }
val interpreter = Interpreter(modelBuffer, options)
```

Four threads is a reasonable starting point on a modern phone; more is often slower, since the big cores are the ones that matter and contention costs more than it buys. Benchmark on real hardware instead of assuming.

The interpreter is not thread-safe. Create it on the analysis thread, use it only there, and `close()` it with the camera. For multiple outputs use `runForMultipleInputsOutputs`, with the output map pre-allocated and reused across frames.

## Discovering the output layout

Log this once, on the first run, in a debug build:

```kotlin
for (i in 0 until interpreter.outputTensorCount) {
    val t = interpreter.getOutputTensor(i)
    Log.d("Model", "out[$i] ${t.name()} shape=${t.shape().contentToString()} dtype=${t.dataType()}")
}
```

Shapes disambiguate most of the question quickly: four outputs with a trailing `[1]` is an SSD graph with embedded post-processing; a single `[1, 84, 8400]`-shaped tensor is a raw YOLO head that still needs decoding and NMS. What shapes cannot tell you — box ordering, normalized versus pixel units, class index offsets — is settled by the parity test below, not by inference from the architecture name.

## Common decoders

**`TFLite_Detection_PostProcess`** (TF Object Detection API SSD exports) emits four tensors, conventionally in this order: boxes `[1, N, 4]`, class indices `[1, N]`, scores `[1, N]`, and detection count `[1]`. Boxes are normalized `[ymin, xmin, ymax, xmax]` — y first, which is the opposite of nearly every other API you will touch that day. NMS is already applied inside the graph, so applying it again is a waste.

The class index needs care. Some exports index into a label file that starts with a `background` entry, others index the real classes directly with background excluded. Off-by-one here maps every detection to the wrong class name while confidences look perfectly healthy. Resolve it with a test image containing a known class rather than by reading the label file.

**Ultralytics YOLO exports** emit a single tensor, typically `[1, 4 + numClasses, numAnchors]` — note that the anchor axis is last, so a naive row-major read gives nonsense. Transpose to per-anchor rows, then each row is `cx, cy, w, h` followed by per-class scores, with no separate objectness in v8 and later. Convert centre form to corners, filter by score, then run NMS yourself. Whether the coordinates are normalized or in input-pixel units varies by exporter version: check the actual value range on a real inference, and record the answer in the manifest so nobody has to check twice.

## Non-maximum suppression

Sort candidates by score, take the highest, drop every remaining box whose IoU with it exceeds the threshold, repeat. Run it per class unless the classes are mutually exclusive by construction.

Two knobs worth exposing in diagnostic builds: the score threshold (recall versus false positives) and the IoU threshold (how aggressively overlapping boxes merge). For a scanner that hunts small objects in dense clutter, a too-high IoU threshold produces stacked duplicate boxes on one target, while a too-low one deletes genuinely adjacent targets.

Cap the candidate count before NMS. A degenerate frame can produce thousands of low-score boxes and the quadratic pass will visibly stall the pipeline.

## Delegates

Default to CPU and treat every accelerator as an optimization that must prove itself.

```kotlin
val compatibility = CompatibilityList()
val options = Interpreter.Options().apply {
    if (compatibility.isDelegateSupportedOnThisDevice) {
        addDelegate(GpuDelegate(compatibility.bestOptionsForThisDevice))
    } else {
        numThreads = 4
    }
}
```

Three constraints follow. The delegate must be created and used on the same thread as the interpreter, and closed after it. GPU inference is usually fp16, so results differ slightly from CPU — run the parity test on the delegate path with a tolerance rather than assuming equivalence. And a delegate that fails to apply falls back to CPU silently, so log which path is actually live or you will attribute CPU latency to the GPU.

NNAPI is deprecated as of Android 15; do not build new work on it. The Play Services runtime (`play-services-tflite-java`) is worth considering when binary size matters, at the cost of a runtime initialization step and a dependency on Play Services being present.

Whether a delegate helps at all depends on the model. Quantized integer models often run better on CPU with XNNPACK than on a GPU that has to convert; measure both before choosing.

## The golden-image parity test

Ship a small image in `androidTest` assets together with the expected detections produced by the training repository's reference implementation.

```kotlin
@Test fun decoderMatchesReference() {
    val detections = detector.detect(loadAsset("golden/clover_01.jpg"))
    assertEquals(expected.size, detections.size)
    detections.zip(expected).forEach { (got, want) ->
        assertEquals(want.label, got.label)
        assertEquals(want.score, got.score, 0.02f)
        assertBoxNear(want.box, got.box, tolerancePx = 2f)
    }
}
```

This single test pins the whole preprocessing and decoding chain: channel order, normalization, letterbox maths, box convention, class mapping, and threshold semantics. Every one of those can be wrong in a way that still yields boxes on screen, which is exactly why reasoning about them is unreliable and a fixture is not.

Regenerate the expected values whenever the model changes, from the reference implementation, and treat a diff as a question about the export rather than something to paper over by loosening the tolerance.
