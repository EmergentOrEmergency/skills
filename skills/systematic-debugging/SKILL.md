---
name: systematic-debugging
description: Produce a structured failure analysis for repository-specific execution problems.
---

# Systematic debugging

Use this skill when a worker hits a failed pre-flight handoff, inspection, branch preparation, build, test, verification, or other repository-specific execution problem.

## Goal

Produce a structured failure analysis that helps the orchestrator decide whether the issue needs clarification, is blocked, or can be retried safely.

## Investigation workflow

Use these phases in order:

1. **Root-cause investigation**
   - reproduce the failure when safe
   - capture the exact failing phase, command, exit code, and concise output
   - trace inputs, state, configuration, and boundaries involved
   - distinguish the first causal failure from downstream symptoms
2. **Pattern analysis**
   - inspect nearby working examples, tests, conventions, and recent related changes
   - identify what differs between the working and failing paths
3. **Hypothesis and test**
   - state one falsifiable root-cause hypothesis
   - run the smallest safe diagnostic that can confirm or reject it
   - if rejected, record the evidence before forming the next hypothesis
4. **Remediation**
   - implement one root-cause fix at a time
   - rerun the original reproducer and relevant regression checks
   - do not combine unrelated speculative fixes

For failures spanning multiple components, collect evidence at component boundaries before deciding where the defect lives.

## Required output

- `phase`
- `command`
- `exitCode`
- `stdoutTail`
- `stderrTail`
- `rootCause`
- `hypothesesTested`
- `diagnosticEvidence`
- `nextAction`

## Rules

- Capture the failing phase explicitly: pre-flight, inspection, branch-prep, planning, implementation, quality-check, verification, or other execution phase.
- Note whether the failure happened before the clarification gate, before WIP, or during worker execution when that distinction matters.
- Summarize only the relevant output tail; do not flood the result with full logs.
- Separate symptom from root cause.
- Do not propose a fix before investigating the root cause and testing at least one concrete hypothesis.
- Do not make several speculative changes at once.
- Recommend one clear next action: retry, clarify, block, or manual follow-up.
- If the failure is caused by repository state, policy, permissions, or missing prerequisites, say that plainly.
