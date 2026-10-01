---
name: native-sdlc-brainstorm
description: Create requirements/intent.md from a new project idea and optional repository context.
---

# Skill: Native SDLC brainstorm

## Goal

Turn an early idea into a clear intent document for a new project, service, or major capability.

Create or update:

- `requirements/intent.md`

## Inputs

Use:

- the user's idea
- any user-provided constraints
- existing `README.md` or `readme.md` if present
- existing `wiki/*.md` if present
- existing `requirements/*.md` if present
- obvious repository context such as templates, solution files, manifests, pipelines, and configuration

README and wiki are optional. If they do not exist, continue from the idea and ask only for missing decisions that materially affect the SDLC direction.

## Delivery-path classification

Before asking the first question, classify the request and tell the user which path applies:

- `spike`: the goal is to answer a feasibility question; any code is disposable and is not an implementation
- `bounded`: a small change to an existing, understood flow with limited touch points
- `architectural`: a new project, service, subsystem, public interface, or change that materially affects component boundaries

A new project is always `architectural`, even when the first version appears small.

When uncertain, choose the more rigorous path. If hidden complexity appears later, upgrade the path and stop at the next approval gate. Never silently downgrade the process to skip an artifact or approval.

The Native SDLC artifact flow is primarily for the `architectural` path. For `spike` or `bounded` work, record the classification and recommended next workflow in `intent.md`; do not pretend that approval of the initial idea approves production implementation.

## Interactive workflow

Use this order:

1. Explore available project context before proposing a solution.
2. Summarize the intended outcome, target users or systems, constraints, and success signal.
3. Separate user-confirmed facts from assumptions.
4. Ask one focused clarification question at a time. Prefer a small set of concrete choices when appropriate.
5. Propose two or three viable approaches with trade-offs and a recommendation.
6. Remove speculative features and unnecessary scope.
7. Present the recommended intent in small, reviewable sections.
8. Incorporate corrections before writing the final artifact.
9. Create or update `requirements/intent.md`.
10. Ask the user to approve the written intent before specification begins.

Do not ask questions already answered by the user or available context.

## Required sections

`requirements/intent.md` must include:

```md
# Intent

## Delivery path

## Idea summary

## Problem statement

## Target users or systems

## Desired outcomes

## Non-goals

## Known constraints

## Assumptions

## Approaches considered

## Recommended direction

## Success signals

## Reference material used

## Open questions

## Approval status
```

## Rules

- Keep the document concise and decision-oriented.
- Distinguish user-stated facts from assumptions.
- Do not invent business rules, integration contracts, compliance requirements, or deployment constraints.
- If the project starts from an empty folder, say that no local reference material was found.
- If existing documentation conflicts with the user idea, record the conflict under `Open questions`.
- Use stable headings so the specification phase can consume the document.
- Do not create code, scaffold a project, install product dependencies, or invoke an implementation worker in this phase.
- Approval applies only to the artifact presented. Approval of the idea does not approve a specification, architecture, plan, or implementation that does not yet exist.
- If the user requests changes, revise and re-present the affected intent sections before continuing.

## Completion criteria

The brainstorm phase is complete only when:

- the delivery path is explicit
- `requirements/intent.md` makes the intended product or capability understandable
- material assumptions and open questions are visible
- the approaches and recommendation are recorded
- the user has approved the written intent for transition to specification
