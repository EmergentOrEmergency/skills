---
name: jira-sdlc-tracking
description: Mirror approved Native SDLC workstreams into Jira sub-tasks through an available authenticated connector when the user requests external tracking.
---

# Jira SDLC Tracking

## Scope and prerequisites

Use only for explicitly requested Jira tracking of an approved plan. `requirements/plan.md` remains the source of truth; Jira records the workstream, requirement identifiers, acceptance summary, and plan reference.

Require the target Jira site and parent issue key, approved workstreams, and an authenticated connector or user-configured API client. Discover available tools and their schemas before use. This package includes no Jira server, fixed authentication scheme, API client, or credentials. Do not invent a local runner or claim a connector is installed.

If no integration is available, produce an execution-ready issue list and report tracking as not executed. Continue local implementation only if the user has not made external tracking mandatory.

## Resolve project capabilities

Read the parent issue and supported project metadata. Determine the actual sub-task issue type and required fields. Resolve the authenticated user and whether they are assignable; assign newly created items to that user by default unless the user requested a different assignment policy. Never reassign an existing parent implicitly.

Read available workflow transitions instead of hardcoding status names or transition IDs. Identify the intended in-progress, completed, and blocked states in this project. If no blocked state exists, use a supported flag/comment when authorized and leave the actual status accurately recorded.

Sprint assignment is optional and requires a user request. Resolve the relevant board and active sprint; ask for the missing choice if multiple candidates remain. Do not assume every Jira deployment permits adding sub-tasks directly to a sprint. Respect parent/sprint constraints and report unsupported operations.

## Create and reconcile

1. Read existing workstream-to-issue mappings from the plan. Reuse recorded issues.
2. Before creating a missing item, search or inspect the parent's sub-tasks for the stable workstream ID, including after an uncertain earlier response.
3. Create one sub-task per approved workstream with parent, summary, concise scope, requirement IDs, acceptance criteria, verification expectation, and plan reference. Use project fields validated by the connector.
4. Create a new parent only if explicitly requested with a project, summary, and appropriate issue type. Otherwise retain the supplied parent.
5. Record each confirmed issue key immediately in the plan. If recording fails, report the returned key so a retry cannot silently create duplicates.
6. Distinguish failed, confirmed, and unknown outcomes. After a timeout, reconcile with Jira before retrying a create action.

User authorization persists across the requested tracking workflow; do not ask again for every included create or transition. Confirm only materially different actions, targets, or assignment choices outside that scope.

## Lifecycle

- Move to the validated in-progress state immediately before work starts.
- Mark complete only after the workstream's checks, acceptance verification, and independent review pass.
- Record a concrete blocker and use the validated blocked-state mechanism when progress requires external input.
- Post meaningful checkpoints, not per-command chatter. Never duplicate the complete specification into every comment.

Report workstream IDs, issue keys/URLs, actual states, assignment/sprint results, and any tracking failures. Tracking failure is distinct from implementation failure. Do not include credentials, private configuration values, or sensitive command output in descriptions or comments.
