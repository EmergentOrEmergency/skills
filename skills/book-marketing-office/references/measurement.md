# Measurement and decision rules

Read this reference when defining a KPI plan, reconciling reports, ranking experiments, or reallocating budget.

## Metric hierarchy

Use the deepest reliably measured outcome available:

1. incremental contribution profit;
2. attributable net revenue or royalties;
3. net sales / new readers;
4. conversion rate and CAC;
5. ROAS;
6. qualified clicks, visits, samples, or signups;
7. engagement and reach as diagnostics.

Never substitute a shallower metric without stating the measurement gap.

## Definitions

- `net_units = units_sold - refunded_units`
- `contribution_profit = attributable_net_revenue - variable_product_cost - ad_spend - variable_campaign_cost`
- `ROAS = attributable_revenue / ad_spend`
- `CAC = acquisition_spend / new_attributable_customers`
- `CTR = clicks / impressions`
- `conversion_rate = conversions / eligible_visits_or_clicks`
- `incremental_profit = observed_profit - estimated_counterfactual_profit`

State whether revenue means gross customer spend, estimated royalty, accrued royalty, or cash received. For Kindle Unlimited, keep KENP and estimated/final royalty separate.

## Attribution hierarchy

Prefer, in order:

1. randomized holdout or credible geo/time experiment;
2. deterministic purchase or coupon/referral linkage;
3. first-party journey linkage with consent;
4. last/first/linear/position-based attribution;
5. platform-reported attribution;
6. correlation or temporal association.

Use multiple models as a sensitivity range when no causal method exists. Deduplicate conversions before adding channels; if deduplication is impossible, report channel views separately.

## Decision quality

Predeclare the primary metric, minimum evidence, loss budget, test duration, and stop/scale rule. Also check practical significance: a statistically or directionally positive result can still be too small to matter.

Treat results as inconclusive when sample size is tiny, data is delayed, tracking changed mid-test, campaigns overlap materially, the comparison periods differ in seasonality, or the metric definition drifted.

Hard stop rules may protect cash, policy, privacy, or reputation and can fire before minimum evidence. Soft underperformance should normally wait for the agreed evidence threshold.

## Reporting delay

Record extraction time and source-specific freshness. Do not compare a near-real-time ad cost to incomplete print sales as if both were final. Reopen decisions when late refunds, royalties, or conversions materially change the economics.
