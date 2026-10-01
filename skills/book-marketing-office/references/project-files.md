# Project files

Read this reference when creating or resuming durable marketing operations. Store these files in the user's book project, not inside the installed skill.

Create only the artifacts the project needs. Prefer updating existing canonical files to creating duplicates.

## `BOOK_MARKETING_BRIEF.md`

Canonical author-approved facts and boundaries:

- book, edition, ASIN/ISBN and territories;
- genre, reader, promise, positioning, comparables;
- publication stage, formats, prices and royalty assumptions;
- author voice, approved claims, spoiler boundary, prohibited topics;
- storefronts, landing pages, owned channels and connected tools;
- budget ceiling and autonomy/approval envelope;
- business objective, time horizon and success definition.

## `MARKETING_STATE.md`

Compact current state, updated after each meaningful cycle:

- timestamp and data freshness;
- current funnel bottleneck;
- active campaigns/content/launch dependencies;
- committed, spent and remaining budget;
- active experiments and next decision dates;
- confirmed results and unresolved anomalies;
- next autonomous actions and pending approvals.

Do not turn this into a diary. Move history to ledgers.

## `EXPERIMENT_LEDGER.csv`

Recommended columns:

```text
experiment_id,status,hypothesis,segment,channel,intervention,control,primary_metric,guardrail_metrics,start_date,end_date,budget,minimum_evidence,stop_rule,scale_rule,result,uncertainty,decision,next_action
```

Use stable experiment IDs in content, links, campaigns, and reports.

## `CONTENT_CALENDAR.csv`

Recommended columns:

```text
content_id,datetime,timezone,channel,pillar,objective,audience,hook,body_or_script,creative_brief,cta,destination,utm,experiment_id,approval_state,external_status,external_id
```

Keep `approval_state` separate from `external_status`. A draft, approved item, scheduled item, and published item are different states.

## `METRICS_LEDGER.csv`

Recommended columns:

```text
period_start,period_end,source,extracted_at,timezone,currency,book_id,channel,campaign_id,experiment_id,impressions,clicks,eligible_visits,signups,orders,units,refunds,kenp,attributed_revenue,royalties,spend,variable_cost,attribution_model,notes
```

Do not coerce unavailable fields to zero. Leave them blank and record the limitation.

## `CONTACT_LEDGER.csv`

Use only when outreach exists:

```text
contact_id,organization,contact_name,fit_basis,source,consent_or_legitimate_basis,last_contact,status,opt_out,notes
```

Never store more personal data than the workflow needs. Honor opt-outs across future batches.
