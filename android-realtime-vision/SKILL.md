---
name: android-realtime-vision
description: Build and debug real-time on-device computer vision on Android — CameraX preview plus ImageAnalysis, LiteRT/TFLite inference, and a Compose bounding-box overlay. Use this whenever the work involves a live camera feed driving a model on the phone: wiring the analyzer, converting frames, decoding detector output, mapping boxes onto the preview, choosing delegates, or chasing symptoms like boxes offset or mirrored, detections that work on a saved photo but not live, growing frame latency, or results that differ from the Python reference. Also use it when planning such an app, even if the request only mentions "camera app", "object detection on phone", "TFLite model in an app", or "find X with the camera".
---

# Real-time vision on Android

A live detector is three pipelines that must agree: camera frames, model inference, and screen coordinates. Most failures are not model failures — they are a silent disagreement between these three. This skill exists because those disagreements produce plausible-looking output (boxes appear, just in the wrong place; detections fire, just not the same ones the Python model found), so they survive casual testing and get diagnosed late.

Work in this order. Each stage is verifiable on its own, which is what makes the next one debuggable.

## 1. Pin the model contract before writing camera code

Load the model's properties from a metadata file shipped beside it, never from the filename or from constants typed into Kotlin. Input size, dtype, colour order, normalization, class list, decoder identity, recommended confidence/IoU thresholds, and the artifact hash all belong in that manifest. When the model is retrained, only the artifact and its manifest change.

This matters more than it looks: the most expensive bug class in this domain is an app that silently keeps using yesterday's assumptions after the model changed. Validate the artifact's SHA-256 against the manifest on first load and fail loudly on mismatch — a wrong-but-running model is worse than a crash, because it degrades recall in a way nobody attributes to the swap.

If the project already defines such a contract (for example a `MODEL_CONTRACT.md` in the training repository), treat that document as authoritative and mirror it exactly rather than inventing a parallel schema.

## 2. Stand up the frame pipeline, and prove it in isolation

Read [references/camera-pipeline.md](references/camera-pipeline.md) for the CameraX wiring: backpressure, the `close()` contract, output format, rotation, and threading.

Before any model is involved, verify the analyzer alone: log the resolution, rotation degrees, and format of arriving frames, and confirm the callback rate stays stable while the preview runs. An analyzer that leaks `ImageProxy` instances or accumulates a queue shows up here as a frame rate that decays over seconds — trivially visible now, deeply confusing later once inference is in the loop and appears to be the cause.

## 3. Bind the decoder to a golden-image parity test

Read [references/inference.md](references/inference.md) for interpreter setup, quantization handling, delegates, and the common output layouts.

Detector output layouts are genuinely ambiguous — box ordering (`[ymin,xmin,ymax,xmax]` versus `xywh`), normalized versus pixel units, whether class indices are offset by a background class, and whether NMS is embedded in the graph all vary between exports of the same architecture. Do not settle these by reasoning about them. Take one image, run it through the training repository's reference implementation, record the expected boxes and scores, ship that image as a test asset, and assert the Android decoder reproduces those numbers within a small tolerance.

This test is the backbone of the whole app. It converts every later question — "did the GPU delegate change the results?", "did the new export break us?", "is the app wrong or is the model wrong?" — from an argument into a check that takes seconds.

## 4. Map model space to screen space explicitly

Read [references/overlay-and-tracking.md](references/overlay-and-tracking.md) for the transform chain and the Compose overlay.

Boxes come out of the model in the coordinate space of the letterboxed, rotated, possibly mirrored tensor that was fed to it. They must be drawn in the coordinate space of a `PreviewView` that is itself cropping the sensor output to fill its own aspect ratio.

Check first whether `CameraController` is an option: an analyzer that reports `COORDINATE_SYSTEM_VIEW_REFERENCED` receives the sensor-to-view matrix from CameraX through `updateTransform`, which removes most of this problem at the source. When it is not — a directly bound `ImageAnalysis` is not integrated with the preview — compose each step deliberately: undo letterbox, apply rotation, apply front-camera mirroring, apply preview crop and scale. Either way, never tune offsets until it looks right on one phone; hand-tuned constants pass on the device you tested and fail on every other aspect ratio.

The cheap diagnostic: draw the model's input rectangle as an outline on the overlay. If that outline does not sit exactly over the region the model actually sees, the transform is wrong and no amount of box-level adjustment will fix it.

## 5. Separate detection rate from display rate

A raw per-frame detector flickers, and flicker reads as "broken" to users even when recall is good. Track detections across frames, require confirmation over a short window before promoting a hit to the user, and interpolate the drawn box between inferences so the overlay stays smooth at display rate while inference runs slower. The tracking and confirmation rules live in [references/overlay-and-tracking.md](references/overlay-and-tracking.md).

Choose the confirmation threshold from the product's error preference, and say which one you chose. A tool that confirms something the user already suspects can afford to be strict; a tool that must find things unaided cannot.

## Project setup

Read [references/project-setup.md](references/project-setup.md) when creating the module or adding dependencies: Gradle configuration, the asset-compression setting that breaks memory-mapped models, permissions, and the ProGuard and ABI concerns.

Dependency versions in that file drift. Check the current version against the official documentation or the project's version catalog before pinning one, and prefer whatever the project already uses over anything suggested here.

## Measuring and reporting performance

Report end-to-end latency from frame arrival to overlay update, not `interpreter.run()` in isolation — preprocessing and conversion are often the larger half, and optimizing the wrong half is the usual outcome of measuring only inference.

Report p50 and p95 rather than an average; the tail is what users perceive as stutter. Measure over a sustained run of at least a couple of minutes, because thermal throttling on a phone held in the sun is the realistic operating condition for an outdoor scanning app and can halve throughput well after a short benchmark has finished.

State the device, Android version, resolution, delegate, and thread count alongside any number. A latency figure without that context cannot be compared against anything.

## Testing

Unit-test the pure functions — preprocessing, output decoding, NMS, the coordinate transform, and temporal filtering — since they are ordinary deterministic code and need no device. The coordinate transform in particular deserves table-driven tests across rotations, aspect ratios, and both cameras, because that is precisely where per-device failures hide.

Keep the golden-image parity test running in CI. Add instrumentation tests for permission flows and lifecycle transitions (background, rotate, screen off), which is where camera resources get leaked.

Test on real hardware across at least a low-end and a high-end device, both orientations, and both the CPU and any delegate path in use.

## Privacy and accessibility

Camera frames stay on device unless the user has explicitly consented to something else, per-instance and with a preview of what is being sent. An offline-by-default vision app should not acquire analytics that undermine that claim.

Feedback must not depend on colour alone — pair the visual indication with haptics or sound, and label controls for screen readers. Users scanning the ground in bright sunlight are effectively low-vision users too.
