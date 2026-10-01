---
name: native-sdlc-architecture
description: Create requirements/architecture.md from spec.md and available project context.
---

# Skill: Native SDLC architecture

## Goal

Translate the approved intent and specification into a practical architecture for a new project, service, or capability.

Create or update:

- `requirements/architecture.md`

## Inputs

Use:

- `requirements/intent.md`
- `requirements/spec.md`
- user clarifications
- existing README, wiki, requirements, templates, and repository conventions if present

## Required sections

`requirements/architecture.md` must include:

```md
# Architecture

## Overview

## Components and responsibilities

## Requirements allocation

## Runtime flow

## Data flow

## External integrations

## Configuration model

## Security and operational considerations

## Observability

## Deployment considerations

## Alternatives considered

## Architecture decisions

## Reference material used

## Open architecture questions
```

## Rules

- Prefer simple architecture that satisfies the specification.
- Under `Requirements allocation`, map every `MUST` requirement and acceptance criterion to the responsible component, interface, or architecture decision.
- Record cross-cutting `NFR-*` ownership explicitly when multiple components contribute to it.
- Do not leave a requirement unallocated. Return to specification clarification when no credible component or boundary can own it.
- Reuse approved project templates and repository conventions when applicable.
- Make integration boundaries explicit.
- Include operational concerns that affect implementation: configuration, logging, health, retries, failure modes, and deployment shape.
- Record alternatives considered when there is a meaningful tradeoff.
- Do not generate code in this phase.

## Completion criteria

The architecture phase is complete when the implementation planner can identify components, touch points, dependencies, and verification needs without guessing and the user has approved the written architecture.
