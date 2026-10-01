# Project setup

Covers: dependencies, the Gradle settings this stack needs, permissions, module layout, and release-build concerns.

Versions in this file are illustrative. Resolve the current one from the official documentation or the project's version catalog, and always prefer a version already used elsewhere in the project over anything suggested here.

## Contents

- [Dependencies](#dependencies)
- [Asset compression](#asset-compression)
- [Permissions](#permissions)
- [Module layout](#module-layout)
- [Release builds](#release-builds)
- [Model delivery](#model-delivery)

## Dependencies

Four groups: CameraX, the inference runtime, Compose, and test support.

```kotlin
// CameraX — camera2 is the implementation, lifecycle binds use cases,
// view provides PreviewView. Keep all CameraX artifacts on one version.
implementation("androidx.camera:camera-core:$cameraX")
implementation("androidx.camera:camera-camera2:$cameraX")
implementation("androidx.camera:camera-lifecycle:$cameraX")
implementation("androidx.camera:camera-view:$cameraX")

// Inference — LiteRT is the current name of the TensorFlow Lite runtime.
implementation("com.google.ai.edge.litert:litert:$litert")
implementation("com.google.ai.edge.litert:litert-gpu:$litert")   // only if a GPU path is actually used
```

Older projects will have `org.tensorflow:tensorflow-lite` instead. The APIs are close enough that examples transfer, but do not mix the two artifacts in one build — duplicate native symbols produce link-time failures whose messages point nowhere useful.

Recent CameraX versions also ship a Compose-native artifact. Check whether your version offers one before writing an `AndroidView` wrapper by hand; if it is still alpha or absent, the `AndroidView` route described in [overlay-and-tracking.md](overlay-and-tracking.md) is fine and stable.

`minSdk` is bounded by CameraX (API 21) in principle, but a GPU delegate wants OpenGL ES 3.1 and quantized models want a CPU worth accelerating on. A baseline around API 26 avoids a long tail of devices that will not run the app acceptably anyway.

## Asset compression

```kotlin
android {
    androidResources {
        noCompress += "tflite"
    }
}
```

Without this the model is stored compressed in the APK, `assets.openFd()` throws, and the app crashes on first inference with an exception that says nothing about compression. Older AGP versions spell it `aaptOptions { noCompress "tflite" }`.

This is the single most common first-run failure on this stack, and it only appears once real loading code runs — long after project setup feels finished.

## Permissions

```xml
<uses-permission android:name="android.permission.CAMERA" />
<uses-feature android:name="android.hardware.camera.any" android:required="true" />
```

Request `CAMERA` at runtime with the Activity Result APIs. Design three states rather than two: not yet asked, granted, and permanently denied — the last one cannot be re-prompted and needs a path into system settings, or the app becomes a dead screen for anyone who tapped "don't allow" once.

Explain the reason before the system dialog when the connection is not obvious, and keep the explanation honest about what happens to frames. For an offline detector that claim is a feature; state it plainly and do not add analytics that contradict it.

Declare no `INTERNET` permission at all if the app genuinely works offline. It is the most credible possible statement that frames stay on the device, and it makes accidental regressions fail at build time.

## Module layout

Keep the pure logic free of Android framework types, so it is unit-testable on the JVM without a device:

```
app/
├── camera/      CameraX binding, analyzer, executor lifecycle
├── detect/      interpreter, preprocessing, decoders, NMS       <- pure, JVM-testable
├── geometry/    letterbox, rotation, preview mapping            <- pure, JVM-testable
├── track/       matching, K-of-N confirmation, smoothing        <- pure, JVM-testable
├── ui/          Compose screens, overlay, diagnostics
└── model/       manifest parsing and validation
```

Three of those packages contain the logic that actually breaks, and all three are ordinary deterministic code. Keeping them free of `ImageProxy`, `Context`, and `Bitmap` is what makes the test strategy in `SKILL.md` cheap enough to actually run.

Put the model artifact and its manifest in `assets/`, and parse the manifest rather than hardcoding its values — see the contract discipline in `SKILL.md`.

## Release builds

Test inference in a release build before believing it works. R8 strips aggressively, and the failure mode is a crash or silent fallback that never appears in debug.

Runtime artifacts generally ship consumer ProGuard rules, so start without custom rules and add keeps only for what actually breaks. Native-backed classes reached reflectively and delegate implementations are the usual suspects. Verify the delegate is still applied in release rather than silently falling back to CPU — log the active path.

Keep the default ABI set. Restricting to `arm64-v8a` shrinks the build and quietly excludes 32-bit devices, which are disproportionately the low-end phones where latency matters most. Use an app bundle and let Play split per device instead.

Check the size contribution of the native runtime and the model together. A detector plus runtime can dominate a small app's download, and that is worth knowing before it is a launch-day surprise.

## Model delivery

Bundle the model in `assets/` for an offline-first app. It is the simplest thing that works, and it makes the offline claim structural rather than aspirational.

Consider Play asset delivery only when the model is genuinely large, and keep a bundled fallback so a fresh install works with no network. An offline tool that needs a download before its first use is not an offline tool.

If models are ever updated out of band, version them with the semantics the model contract defines, verify the hash before use, and keep the previous artifact until the new one has run successfully once. A model swap that downgrades recall is the failure nobody notices in time.
