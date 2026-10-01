---
name: template-bootstrap
description: Bootstrap an approved project from a user-selected local template or verified framework scaffolder, adapting names and references without importing organization-specific configuration.
---

# Template Bootstrap

## Goal and inputs

Create the project skeleton specified by the approved plan. Establish language/framework, destination, desired project/package/namespace names, template source, source placeholder names, and expected validation. Read the target repository's conventions before choosing a scaffold.

This package does not bundle application templates. Use a template already provided by the user or target project. If none exists, select an official framework scaffolder or a minimal skeleton consistent with the approved architecture. Verify tool availability and current scaffolder options before execution; explain any material template choice that remains unresolved. A missing optional template does not require reinstalling this package.

## Bootstrap workflow

1. Resolve the source and destination to absolute paths. Confirm that the destination belongs to the assigned write scope, differs from the source, and is not nested inside the source tree being copied.
2. Inspect the source before copying. Identify its license, placeholders, framework/runtime versions, build commands, external integrations, and required configuration. Do not carry over credentials, private endpoints, organization-specific registries, binaries, caches, Git history, IDE state, or generated artifacts.
3. Inspect the destination. Use a new directory or merge only the files required by the plan. Preserve existing files; resolve collisions before replacing user work. Do not mirror or recursively delete an existing destination.
4. Copy the inspected template or run the verified scaffolder. Record the template path/version or scaffolder command and version.
5. Rename only the known placeholders, using a concrete old-to-new mapping. Check file names, source references, tests, build configuration, and runtime paths together. Avoid blind replacement of generic words or unrelated dependency names.
6. Run the smallest relevant restore/build/test/startup check available. Report missing tools or unavailable integrations separately from scaffold correctness.

## Language-specific checks

For C#: update solution/project references, namespaces, assembly names, test references, Docker entrypoints, and CI paths when present. Keep the selected framework version consistent across projects.

For Python: choose a valid import package name independently of the distribution/project display name. Update imports, packaging metadata, module entrypoints, test discovery, Docker paths, and CI paths when present. Do not assume a dotted C# namespace is a valid Python directory layout.

Do not add a corporate service framework, deployment pipeline, database, or integration merely because a source template contained it. Preserve only the dependencies required by the approved architecture.

## Result

Return source/provenance, target path, files copied/generated, rename mapping, configuration requiring user values, validation command results, and remaining gaps. Describe scaffolding as scaffolding; working application behavior still needs implementation and verification.
