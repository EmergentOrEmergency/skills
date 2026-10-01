---
name: native-sdlc-code-generation
description: Generate or bootstrap code only after Native SDLC artifacts are present and approved.
---

# Skill: Native SDLC code generation

## Goal

Implement the approved Native SDLC plan with minimal, traceable changes.

Use this skill only after:

- `requirements/intent.md` exists
- `requirements/spec.md` exists
- `requirements/architecture.md` exists
- `requirements/plan.md` exists
- the user has explicitly approved moving to implementation

## Inputs

Use:

- the approved SDLC artifacts under `requirements/`
- the user's approval and any approval constraints
- existing repository conventions
- approved templates when the plan calls for a new C# or Python microservice
- the orchestrator-assigned workstream, target repository, allowed write scope, acceptance criteria, and dependency results

## Rules

- Follow `requirements/plan.md` as the implementation contract.
- Do not expand scope beyond the approved plan without asking.
- Use the local `template-bootstrap` skill when bootstrapping from approved project templates.
- Use test-driven development for observable behavior when a suitable test harness exists:
  1. write the smallest test that expresses the assigned acceptance criterion
  2. run it and observe the expected failure (`RED`)
  3. implement the smallest production change that can satisfy it
  4. run the test and observe it pass (`GREEN`)
  5. refactor without changing behavior and rerun the relevant tests
- Do not write production behavior before its failing test unless the work is scaffolding, generated code, documentation, declarative configuration, a migration that cannot be exercised locally, or the repository has no viable test harness. Record the exception and alternative verification.
- A test that passes before the implementation change is not evidence of a valid RED step; confirm that it fails for the expected reason.
- Keep changes surgical and traceable to the plan.
- Preserve type safety and existing conventions.
- Do not commit secrets or generated credentials.
- Update SDLC artifacts only when implementation reveals a material correction.
- If the plan is incomplete or conflicts with repository reality, stop and ask for clarification before coding.
- When invoked by the Native SDLC orchestrator, work only within the assigned workstream and allowed write scope.
- Do not assume that independent workers may edit shared files. Return a scope conflict to the orchestrator instead.
- Update directly related README or wiki documentation for material behavior, configuration, deployment, or operational changes.

## Validation

Run the smallest existing validation that covers the generated change.

Report:

- workstream id and files changed
- TDD status, RED evidence, GREEN evidence, or the documented exception
- commands run
- quality check result
- verification steps
- expected outcome
- actual outcome
- evidence
- anything not verified and why
- scope compliance and any deviation

## Completion criteria

The code generation phase is complete when the approved implementation has been created or bootstrapped, relevant checks have run or a clear reason is recorded, and the result is mapped back to the approved SDLC artifacts.
