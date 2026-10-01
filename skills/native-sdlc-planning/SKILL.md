---
name: native-sdlc-planning
description: Create requirements/plan.md with implementation phases, tasks, tests, risks, and approval checklist.
---

# Skill: Native SDLC planning

## Goal

Create an actionable implementation plan from the SDLC intent, specification, and architecture.

Create or update:

- `requirements/plan.md`

## Inputs

Use:

- `requirements/intent.md`
- `requirements/spec.md`
- `requirements/architecture.md`
- user clarifications
- repository or template context if present

## Required sections

`requirements/plan.md` must include:

```md
# Implementation Plan

## Goal

## Preconditions

## Dependency graph

## Implementation phases

## Task breakdown

## Interfaces and contracts

## Expected file and folder changes

## Testing strategy

## Review focus

## Requirements traceability matrix

## Checkpoints

## Verification plan

## Risks and mitigations

## Dependencies

## Rollback or recovery notes

## Definition of done

## External tracking

## Approval checklist

## Reference material used

## Open planning questions
```

## Rules

- Before replacing an existing `requirements/plan.md`, determine whether it belongs to the same initiative:
  - same initiative: update it in place and preserve useful completed decisions
  - different initiative with incomplete tasks: stop and ask where the new plan should live; do not overwrite active planning state
- Keep tasks concrete and ordered.
- Split work into the smallest independently verifiable tasks that have a coherent test or validation cycle.
- Prefer vertical feature slices that produce observable behavior across the necessary layers over horizontal tasks such as building all storage, then all APIs, then all consumers.
- Build and record a dependency graph before ordering tasks. Define shared contracts and foundations before parallel work that consumes them.
- Order high-risk or uncertain tasks early enough to fail fast without destabilizing unrelated work.
- For every task, record:
  - task id and short outcome-oriented title
  - requirement identifiers covered
  - description and observable outcome
  - dependencies
  - expected write scope and likely files
  - consumed and produced interfaces
  - no more than three primary acceptance criteria; split the task if more are needed
  - test-first step when applicable
  - validation command or manual verification when known
  - estimated scope: `XS`, `S`, `M`, or `L`
- Treat `L` as a warning that the task should normally be decomposed. A task is too large when it spans independent subsystems, cannot complete in one focused worker session, has unclear acceptance criteria, or uses `and` to combine separate outcomes.
- Separate bootstrapping, production implementation, tests, documentation, and validation.
- Identify whether a approved project template should be used.
- Include the smallest meaningful validation commands when they are known.
- Under `Review focus`, list likely failure modes, edge cases, or integration mistakes and map each one to a test, inspection, or verification step.
- Under `Requirements traceability matrix`, include one row for every `FR-*`, `NFR-*`, `DR-*`, and `AC-*` identifier with:
  - architecture component or decision
  - implementation task or workstream
  - planned test or inspection
  - planned verification evidence
  - coverage status: `covered`, `deferred`, or `uncovered`
- Make workstream dependencies and overlapping file ownership explicit so the orchestrator can safely choose parallel or sequential execution.
- Prefer parallel workstreams across separate repositories. For workstreams in the same repository, account for shared manifests, generated outputs, build artifacts, and commands in addition to source-file ownership.
- Identify tasks that require explicit approval because they are destructive, security-sensitive, or create external side effects.
- Include a final integration task covering the combined behavior of all workstreams.
- Add checkpoints after coherent groups of tasks, not merely at the end. Each checkpoint must state the checks, integrated behavior, and requirement coverage expected at that point.
- Ensure every task and checkpoint leaves the repository in a buildable or explicitly documented transitional state.
- Under `Definition of done`, state the common quality, documentation, review, security, and verification conditions every task must satisfy in addition to task-specific acceptance criteria.
- Under `External tracking`, keep Jira disabled by default. When the user opts in after plan approval, record the parent issue, whether current-sprint assignment is requested, whether default authenticated-user assignment is overridden, and the Jira key returned for each workstream. Do not duplicate the task specification in Jira.
- Perform a final plan completeness audit before asking for implementation approval:
  - every `MUST` requirement and every acceptance criterion must be `covered`
  - every `SHOULD` or `MAY` item marked `deferred` must include a rationale and explicit approval expectation
  - no workstream may reference an unknown requirement
  - tests and verification must cover normal flow, failure behavior, and relevant non-functional requirements
- Do not claim that the plan satisfies a requirement. The plan proves intended coverage; actual satisfaction is checked after implementation.
- Do not generate code in this phase.
- End with an approval checklist that the user can accept before implementation starts.

## Completion criteria

The planning phase is complete when the traceability matrix has no uncovered `MUST` requirements or acceptance criteria, code generation can proceed without making unapproved product, architecture, or scope decisions, and the user has explicitly approved implementation from the written plan.
