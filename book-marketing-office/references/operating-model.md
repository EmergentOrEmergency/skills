# Operating model

Read this reference when starting a campaign cycle, resolving conflicts between specialists, or deciding whether an action may run autonomously.

## Routing contract

| Need | Owner | Required handoff |
|---|---|---|
| Market, comps, reader evidence, positioning | `market-intelligence` | Evidence pack, confidence, positioning hypotheses |
| Owned audience, community, partners, outreach | `audience-growth` | Segment, consent basis, batch, approval state |
| Editorial system, channel copy, scheduling | `content-social` | Content IDs, experiment IDs, exact payloads |
| Launch, storefront, promotion, email | `launch-sales` | Critical path, dependencies, approval queue |
| Paid media | `ads-growth` | Budget envelope, stop/scale rules, payloads |
| Reconciliation and decisions | `analytics-cfo` | Metric definitions, freshness, uncertainty, decision |

The CMO owns the single prioritized backlog and resolves local optimization conflicts. A specialist may recommend an action but must not expand its authorization.

## Cadence

Use the lightest cadence justified by volume and spend:

- Continuous: record confirmations, failures, spend-limit breaches, reputation or policy risks.
- Daily during a launch or paid test: check delivery and hard guardrails; avoid strategy changes from ordinary noise.
- Weekly: reconcile data, diagnose the funnel bottleneck, close or continue experiments, and reprioritize.
- Monthly: assess contribution profit, audience quality, channel roles, positioning evidence, and whether the operating thesis still holds.

## Action envelope

An `AUTO_WITHIN_LIMITS` envelope is valid only when it states:

- accounts and channels;
- allowed action types;
- start and expiry;
- per-action, daily, and total spend limits where relevant;
- content/claim boundaries;
- stop conditions;
- reporting cadence;
- actions that always escalate.

Missing or ambiguous fields narrow the envelope; they never broaden it. External tool capability and authorization are separate checks.

## Stop and escalate

Stop the affected action and preserve evidence when any of these occurs: hard budget breach, credential or privacy risk, policy warning, unexpected account, incorrect destination, materially false claim, hostile or legally sensitive interaction, data corruption, unexplained conversion anomaly, or uncertainty about an irreversible change.

Do not stop the whole program for an isolated low-risk failure. Record the incident, use a safe fallback, and continue unaffected work.

## Approval packet

Make approval easy to evaluate. Include:

1. proposed action and business reason;
2. exact account, audience, copy/creative, link, timing, and spend;
3. expected outcome and uncertainty;
4. stop/rollback plan;
5. deadline and consequence of no decision.

Approval applies only to the described packet unless the user explicitly grants a reusable envelope.
