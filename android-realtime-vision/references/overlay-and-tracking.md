# Overlay and tracking

Covers: the coordinate transform from model space to screen space, the Compose overlay, temporal confirmation, and smoothing.

## Contents

- [The transform chain](#the-transform-chain)
- [Undoing the letterbox](#undoing-the-letterbox)
- [Undoing rotation and mirroring](#undoing-rotation-and-mirroring)
- [Mapping onto PreviewView](#mapping-onto-previewview)
- [Testing the transform](#testing-the-transform)
- [The Compose overlay](#the-compose-overlay)
- [Temporal confirmation](#temporal-confirmation)
- [Smoothing](#smoothing)

## The transform chain

A box travels through four coordinate spaces, and each step must be undone in reverse order:

```
sensor frame -> rotated upright frame -> letterboxed model input -> model output box
                                                                         |
screen pixels <- preview crop/scale <- un-rotate, un-mirror <- un-letterbox
```

Write it as an explicit composition of small functions, each independently testable. The alternative — a single fudge factor tuned until the boxes look right on the device at hand — passes on that device and fails on every phone with a different aspect ratio, which is a bug that reaches users because it cannot reproduce on the developer's desk.

The fastest way to find where the chain is wrong: draw the model's full input rectangle through the same transform. If that outline does not exactly cover the region the model is actually seeing, the error is upstream of the boxes and adjusting them is wasted effort.

## Undoing the letterbox

Normalized model output first becomes model-input pixels, then frame pixels using the scale and padding recorded during preprocessing ([inference.md](inference.md)):

```kotlin
fun modelToFrame(box: RectF, lb: Letterbox, inputW: Int, inputH: Int): RectF {
    // normalized -> model-input pixels
    val x0 = box.left * inputW; val y0 = box.top * inputH
    val x1 = box.right * inputW; val y1 = box.bottom * inputH
    // model-input pixels -> upright frame pixels
    return RectF(
        (x0 - lb.padX) / lb.scale, (y0 - lb.padY) / lb.scale,
        (x1 - lb.padX) / lb.scale, (y1 - lb.padY) / lb.scale,
    )
}
```

Skip the first step when the export emits pixel coordinates. Which one it is comes from the parity test, not from assumption — and once known, belongs in the manifest.

Remember that SSD post-processing emits `[ymin, xmin, ymax, xmax]`. Swapping y and x produces boxes that are plausibly sized and confidently wrong, and on a near-square input they can look almost right.

## Undoing rotation and mirroring

If the frame was rotated to upright before inference, frame coordinates are in the rotated space and must be rotated back into the sensor space the preview displays. For a 90° rotation of a `w × h` upright frame into `h × w` sensor space, a point `(x, y)` maps to `(y, w - x)`; 180° and 270° follow the same pattern. Derive them once, test them as a table, and never write them inline again.

Front-camera preview is mirrored, rear is not. Mirror horizontally in view space: `x' = viewWidth - x`. Drive this off `cameraInfo` rather than a hardcoded assumption about which camera is bound, since a camera-switch button will otherwise break it.

Boxes must stay normalized after mirroring — swap left and right rather than negating a width, or the rectangle ends up inverted and draws as nothing.

## Mapping onto PreviewView

`PreviewView` defaults to `FILL_CENTER`, which scales the frame to cover the view and crops the overflow. The overlay must apply the same crop, or boxes drift outward from the centre in proportion to the aspect mismatch:

```kotlin
val scale = max(viewW / frameW, viewH / frameH)        // FILL_CENTER
val dx = (viewW - frameW * scale) / 2f
val dy = (viewH - frameH * scale) / 2f
```

Use `min` instead for `FIT_CENTER`. During development `FIT_CENTER` is the friendlier choice, since the whole analyzed frame is visible and misalignment is obvious rather than hidden off-screen.

Request the same aspect ratio for preview and analysis. When they differ, the two use cases receive different crops of the sensor and the boxes cannot be made to line up by any transform applied after the fact — a genuinely confusing failure, because the maths looks correct.

CameraX also ships transform helpers under `androidx.camera.view.transform`. Their API has shifted across versions and parts have been experimental, so check what your version actually offers before depending on them; keep the explicit maths as the version your tests pin, since that is what you can unit-test off-device.

## Testing the transform

This is pure arithmetic and deserves table-driven unit tests: each rotation (0/90/180/270), each camera, portrait and landscape, and at least one deliberately mismatched aspect ratio.

The strongest assertion is a round trip — map a box forward through preprocessing and back through the overlay chain and require it to return to where it started, within a pixel. Round-trip tests catch sign errors and swapped axes that eyeballing a single case will not.

Anchor the suite with the four corners and the centre. Corner cases are literally corner cases here: a transform that is wrong only in a sign is still correct at the centre.

## The Compose overlay

Stack a `Canvas` over the `AndroidView` that hosts `PreviewView`, and draw in view pixels — the transform has already done the work:

```kotlin
Box(Modifier.fillMaxSize()) {
    AndroidView(factory = { previewView }, modifier = Modifier.fillMaxSize())
    Canvas(Modifier.fillMaxSize()) {
        detections.forEach { d ->
            drawRect(
                color = highlight,
                topLeft = Offset(d.rect.left, d.rect.top),
                size = Size(d.rect.width(), d.rect.height()),
                style = Stroke(width = 4.dp.toPx()),
            )
        }
    }
}
```

Publish detections through a `StateFlow` or `mutableStateOf` holding an immutable list, so recomposition touches the canvas and not the camera subtree — rebinding the camera on every frame is a spectacular but easily made mistake.

Make the indication readable against ground cover: a stroke with a contrasting halo survives a bright green background better than a thin single-colour line. Pair it with haptics or sound so the signal does not depend on colour vision or on the user watching the screen continuously, and expose confidence values only behind a diagnostics toggle — a number next to a box invites users to interpret a calibration they have no way to understand.

## Temporal confirmation

Per-frame output flickers, and flicker reads as unreliability. Match detections across frames and require persistence before telling the user anything.

Greedy IoU matching is sufficient at these object counts: for each new detection, find the existing track with the highest IoU above a threshold (0.3–0.5 works well) and update it; unmatched detections start new tracks; tracks that go unmatched for several frames expire. Promote a track to "confirmed" once it has been seen in K of the last N frames.

K and N encode a product decision. A tool meant to confirm a clover the user already spotted can demand 4 of 6 and stay quiet otherwise; a tool meant to find them unaided has to accept more false positives to keep recall, and should show candidates earlier at lower prominence. Pick deliberately, write down which error the app prefers, and keep the constants adjustable in diagnostic builds so the choice can be re-tested on real footage rather than re-argued.

Expire tracks on a timer as well as a frame count. A user who lowers the phone should not find a stale confirmation waiting when they raise it again.

## Smoothing

Inference runs slower than the display refreshes, so drawing only on new results looks stuttery. Smooth the track's box with an exponential moving average, and interpolate between updates so the overlay moves at display rate.

Keep the smoothing factor low enough that the box still follows real motion; over-smoothing produces a marker that visibly lags the object, which users read as the app having lost it. Around 0.6–0.8 toward the new measurement is a reasonable starting range, tuned on real handheld footage rather than on a phone resting on a desk.

Smoothing the box position is safe. Smoothing the confirmed/unconfirmed state is not — that is what the K-of-N rule above is for, and doing it twice just adds latency to the moment the user cares about.
