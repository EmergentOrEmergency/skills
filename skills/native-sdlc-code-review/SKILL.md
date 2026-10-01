---
name: native-sdlc-code-review
description: Review a Native SDLC workstream against approved artifacts, acceptance criteria, tests, and scope.
---

# Skill: Native SDLC code review

## Goal

Provide an independent, evidence-based review of an implementation workstream before it is accepted by the Native SDLC orchestrator.

## Reviewer inputs

Give the reviewer only the context needed to assess the change:

- target repository root
- approved `requirements/spec.md`, `requirements/architecture.md`, and `requirements/plan.md`
- workstream id, goal, allowed write scope, and acceptance criteria
- assigned requirement identifiers and their traceability rows
- diff or exact changed-file list
- tests and quality checks run
- verification evidence
- prior blocking findings when this is a remediation review

Do not pass unrelated session history or ask the reviewer to redesign the approved solution.

## Review order

1. Confirm the diff stays within the assigned scope.
2. Check compliance with the approved specification and architecture.
3. Check correctness, edge cases, failure behavior, and integration contracts.
4. Check whether tests cover the acceptance criteria and important failure modes.
5. Check the supplied quality and verification evidence.
6. Distinguish blocking defects from non-blocking improvements.
7. Confirm that implementation, tests, and verification evidence map to every assigned requirement identifier.
8. Return findings with concrete file and line references when available.

## Finding rules

- Report only actionable findings supported by repository evidence.
- Rank findings as `critical`, `high`, `medium`, or `low`.
- Treat correctness, data loss, security, contract violations, broken error handling, and unmet acceptance criteria as potentially blocking.
- Do not block on personal style preferences already handled by existing formatters or conventions.
- Do not propose unrelated refactors or speculative abstractions.
- Check whether a recommendation is actually required by current scope before raising it.
- If review context is insufficient, request the missing evidence rather than inventing a defect.

## Receiving review

The orchestrator and implementation worker must evaluate findings technically:

1. understand the finding
2. verify it against code and approved artifacts
3. accept, reject with evidence, or ask for clarification
4. implement accepted blocking findings before new work
5. rerun relevant checks and verification

Do not accept a finding merely because a reviewer stated it confidently. Do not dismiss a finding without evidence.

## Required output

- `workstreamId`
- `reviewedFiles`
- `specCompliance`
- `architectureCompliance`
- `scopeCompliance`
- `testCoverageAssessment`
- `verificationAssessment`
- `requirementCoverageAssessment`
- `blockingFindings`
- `nonBlockingFindings`
- `reviewStatus`: `passed`, `changes-required`, or `insufficient-evidence`
- `reviewEvidence`
