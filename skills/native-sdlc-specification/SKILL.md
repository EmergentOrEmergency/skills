---
name: native-sdlc-specification
description: Create requirements/spec.md from intent.md and optional repository context.
---

# Skill: Native SDLC specification

## Goal

Convert `requirements/intent.md` into an implementation-ready product specification.

Create or update:

- `requirements/spec.md`

## Inputs

Use:

- `requirements/intent.md`
- user clarifications
- existing `README.md`, `wiki/`, and `requirements/` files if present
- repository context that constrains the specification

## Required sections

`requirements/spec.md` must include:

```md
# Specification

## Purpose and stakeholders

## Scope

## Functional requirements

## Behavioral flows and state transitions

## Non-functional requirements

## External interfaces

## Data inputs and outputs

## Data validation and transformations

## Error handling and edge cases

## Configuration requirements

## Security, privacy, and compliance notes

## Success metrics

## Acceptance criteria

## Out of scope

## Requirement quality analysis

## Reference material used

## Open decisions
```

## Requirement format

Assign a stable identifier to every requirement:

- `FR-###` for functional requirements
- `NFR-###` for non-functional requirements
- `DR-###` for data requirements when they need independent traceability
- `AC-###` for acceptance criteria

Each requirement must record:

- identifier
- normative statement
- rationale or business value
- source or stakeholder
- priority: `MUST`, `SHOULD`, or `MAY`
- measurable acceptance or verification signal
- dependencies on other requirements when relevant

Avoid vague terms such as `fast`, `secure`, `user-friendly`, `scalable`, or `reliable` unless they are made measurable or explicitly listed as unresolved.

## Requirement quality analysis

Before presenting the specification for approval, inspect five dimensions:

1. **Purpose**: problem, stakeholders, value, success metrics
2. **Data**: sources, formats, volume, validation, transformations, destinations
3. **Behavior**: primary flow, alternative flows, state transitions, failure behavior
4. **Constraints**: integrations, compatibility, performance, security, compliance, dependencies
5. **Quality**: acceptance criteria, testability, observability, operational expectations

For each dimension, report:

- `clear`
- `needs-clarification`
- `not-applicable`, with a reason

Then explicitly list:

- ambiguities
- contradictions
- missing critical information
- assumptions requiring validation

Do not use a numerical clarity score as a substitute for analysis. The specification is not ready while a `MUST` requirement, external contract, security boundary, or acceptance criterion has a blocking ambiguity.

## Rules

- Make requirements testable where possible.
- Use `MUST`, `SHOULD`, and `MAY` intentionally.
- Keep open decisions explicit instead of silently choosing between valid alternatives.
- Do not over-specify implementation details that belong in architecture or planning.
- Do not generate code in this phase.
- If a requirement depends on missing information, mark it as an open decision.
- For every open decision, record why it matters, the affected requirement identifiers, and the decision needed.
- Keep architecture recommendations out of the specification unless they are user-mandated constraints. Technical recommendations belong in `architecture.md`.
- Check for conflicts between requirements instead of resolving them silently.

## Completion criteria

The specification phase is complete when:

- every requirement and acceptance criterion has a stable identifier
- purpose, data, behavior, constraints, and quality have been analyzed
- blocking ambiguities, contradictions, and gaps are resolved
- remaining assumptions and non-blocking decisions are explicit
- expected behavior, boundaries, and acceptance criteria are clear enough to design an architecture
- the user has approved the written specification
