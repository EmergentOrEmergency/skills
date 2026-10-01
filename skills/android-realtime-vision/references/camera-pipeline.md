# Camera pipeline

Covers: binding CameraX, the analyzer contract, frame formats and conversion, rotation, threading, and torch. Read alongside [inference.md](inference.md), which consumes the buffer this file produces.

## Contents

- [Binding preview and analysis](#binding-preview-and-analysis)
- [The analyzer contract](#the-analyzer-contract)
- [Frame format and conversion](#frame-format-and-conversion)
- [Rotation](#rotation)
- [Threading](#threading)
- [Resolution](#resolution)
- [Torch, focus, and lifecycle](#torch-focus-and-lifecycle)
- [Symptoms and causes](#symptoms-and-causes)

## Binding preview and analysis

Bind both use cases in a single `bindToLifecycle` call. Binding them separately, or rebinding on every recomposition, causes visible restarts of the camera stream.

```kotlin
val provider = ProcessCameraProvider.getInstance(context).await()

val preview = Preview.Builder().build().apply {
    surfaceProvider = previewView.surfaceProvider
}

val analysis = ImageAnalysis.Builder()
    .setBackpressureStrategy(ImageAnalysis.STRATEGY_KEEP_ONLY_LATEST)
    .setOutputImageFormat(ImageAnalysis.OUTPUT_IMAGE_FORMAT_RGBA_8888)
    .build()
    .apply { setAnalyzer(analysisExecutor, detectorAnalyzer) }

provider.unbindAll()
val camera = provider.bindToLifecycle(
    lifecycleOwner, CameraSelector.DEFAULT_BACK_CAMERA, preview, analysis,
)
```

`STRATEGY_KEEP_ONLY_LATEST` is the important line. The default, `STRATEGY_BLOCK_PRODUCER`, queues frames, so when inference is slower than the camera the app shows an overlay describing a scene from several seconds ago while latency grows without bound. Dropping stale frames is the correct behaviour for a live scanner: the user cares about what the phone is pointed at now.

In Compose, hold the provider and the executor in state that outlives recomposition (`remember` plus a `DisposableEffect` that shuts the executor down), and put `PreviewView` in an `AndroidView`.

## The analyzer contract

```kotlin
override fun analyze(image: ImageProxy) {
    try {
        val rotation = image.imageInfo.rotationDegrees
        // preprocess -> infer -> publish results
    } finally {
        image.close()
    }
}
```

Every path out of `analyze` must close the `ImageProxy`, including exceptional ones — hence the `finally`. The analyzer owns a small fixed pool of image buffers, so a single leaked frame permanently reduces the pool and a few leaks stop delivery altogether. The symptom is a preview that keeps running while detections silently stop, which reliably gets misdiagnosed as a model problem.

Do the work synchronously inside `analyze`, on the analyzer's own executor. If you hand the frame to a coroutine and return, you either close the image too early (garbage input) or too late (leak). When inference must be asynchronous, copy what you need into your own buffer first, then close.

## Frame format and conversion

`OUTPUT_IMAGE_FORMAT_RGBA_8888` asks CameraX to do the YUV conversion, which is both less code and usually faster than doing it yourself.

The trap is row padding. The plane's `rowStride` is frequently larger than `width * pixelStride`, so copying the buffer wholesale gives a skewed image — recognisable as a picture that shears diagonally. Copy row by row:

```kotlin
val plane = image.planes[0]
val rowStride = plane.rowStride          // bytes per row, may exceed width * 4
val pixelStride = plane.pixelStride      // 4 for RGBA_8888
```

`ImageProxy.toBitmap()` (camera-core 1.3 and later) handles this correctly and is a reasonable default. It allocates, so for a sustained loop either reuse a destination `Bitmap` or keep your own row-wise copy into a pre-allocated buffer. Allocating a full-resolution bitmap per frame is the single most common source of GC-driven stutter in this kind of app.

If you take `OUTPUT_IMAGE_FORMAT_YUV_420_888` instead, note that RenderScript is gone from modern Android; the U and V planes may be interleaved with `pixelStride == 2`, and code copied from old NV21 examples usually assumes otherwise. Prefer letting CameraX convert unless profiling says the conversion is your bottleneck.

Watch the channel order end to end. CameraX gives RGBA; most models want RGB, and OpenCV-derived reference code often assumes BGR. A channel swap does not crash — it produces a model that "sort of works" with degraded accuracy, which is far harder to notice than a failure. The golden-image parity test in [inference.md](inference.md) is what catches this.

## Rotation

`image.imageInfo.rotationDegrees` is the rotation needed to make the frame upright relative to the target rotation. Sensors are typically mounted landscape, so a phone held upright commonly reports 90.

Feed the model an upright image, because that is how the training data was oriented; a model fed sideways frames loses accuracy in a way that looks like a bad model. Then remember that the boxes come back in that rotated space and must be un-rotated on the way to the screen — see [overlay-and-tracking.md](overlay-and-tracking.md).

Keep `analysis.targetRotation` updated when the activity handles rotation itself rather than being recreated; otherwise the reported degrees go stale after a device rotation.

## Threading

Use one dedicated single-thread executor for analysis:

```kotlin
val analysisExecutor = Executors.newSingleThreadExecutor()
```

A single thread is not a limitation here. LiteRT `Interpreter` instances are not thread-safe, and a delegate must be used on the thread that created it, so a single analysis thread owning a single interpreter is both the simplest and the correct arrangement. Parallelism belongs inside the interpreter (`setNumThreads`), not outside it.

Never block the main thread on inference, and shut the executor down when the camera is released.

## Resolution

Analysis resolution is a latency knob, distinct from preview resolution. Requesting frames much larger than the model input wastes time on a downscale that produces no accuracy.

Use `ResolutionSelector` on current CameraX versions (`setTargetResolution` is deprecated). Treat any resolution as a request, not a guarantee — the device picks the closest supported size, so always read the actual dimensions from the arriving `ImageProxy` rather than assuming you got what you asked for.

## Torch, focus, and lifecycle

Torch comes from the bound camera: `camera.cameraControl.enableTorch(true)`. Check `camera.cameraInfo.hasFlashUnit()` first and observe `torchState` for the UI, so the button reflects reality rather than intent.

For close-range scanning, consider a tap-to-focus affordance via `FocusMeteringAction`; continuous autofocus hunts on low-contrast ground cover and the user usually knows where they want focus.

Binding to a `LifecycleOwner` means CameraX releases the camera on stop and reacquires on start. Verify it actually happens — background, rotate, and screen-off transitions are where camera resources leak, and those paths deserve an instrumentation test.

## Symptoms and causes

| Symptom | Likely cause |
| --- | --- |
| Detections stop, preview keeps running | leaked `ImageProxy` (missing `close()` on some path) |
| Overlay lags further behind over time | `STRATEGY_BLOCK_PRODUCER`, or work queued off-analyzer |
| Image shears diagonally | ignored `rowStride` padding |
| Colours look wrong / accuracy quietly poor | RGB vs BGR channel order |
| Accuracy drops only in portrait | frame not rotated upright before inference |
| Periodic stutter, sawtooth memory | per-frame bitmap or buffer allocation |
