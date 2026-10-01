---
name: verification-before-completion
description: Verify the requested outcome and collect evidence before reporting success.
---

# Verification before completion

Use this skill before reporting success for a repository or issue result.

## Goal

Verify the requested outcome, not only the mechanics of the change.

## Required output

- `qualityChecksRun`
- `qcStatus`
- `verificationSteps`
- `expectedOutcome`
- `actualOutcome`
- `verificationStatus`
- `verificationEvidence`
- `verificationNotPossibleReason`

## Rules

- Existing repository checks are necessary but not sufficient.
- Use fresh evidence from the current implementation state. Do not rely only on an earlier run, a worker's confidence, or expected behavior.
- Distinguish "the checks ran" from "the requested behavior is verified".
- Keep quality control and verification as separate gates; do not collapse them into one step.
- Prefer evidence tied to the requested task: expected output, before/after behavior, changed contract, or observable artifact.
- If verification is impossible in the current environment, say so explicitly and explain what is missing.
- Do not report a result as complete when verification is missing, inconclusive, or contradicted by the evidence.
- Avoid unsupported completion language such as `should work`, `probably fixed`, `seems correct`, or `done` without naming the evidence.
- Match every completion claim to evidence: build claims need a successful build result, test claims need test output, behavior claims need an observed outcome, and acceptance claims need each relevant criterion checked.
- For spec-driven work, map evidence to every assigned requirement and acceptance-criterion identifier.
- Treat an uncovered or unverified `MUST` requirement or acceptance criterion as incomplete, not passed.
