# Venues, publication boundaries, and records

Read before recommending destinations, preparing editorial submissions, or executing releases.

## Match route to objective

| Route | Useful role | Evidence to collect |
|---|---|---|
| Author site/newsletter | Stable reading destination and ongoing relationship | Delivery capabilities, discovery source, language fit, signup path, analytics |
| Fiction community/serial platform | Discovery and recurring installments | Recent comparables, active target-language readers, genre fit, link rules, cadence expectations |
| Magazine/journal | Editorial placement and relevant readership | Open window, language/length fit, publication and AI policies, rights requested, fees/payment, submission route |
| Audio publication/reading event | Discovery through spoken voice | Format/length, performer/recording rights, process, audience, transcript/link options |

Search in the intended language. Do not recommend an English-language venue for Italian fiction without verifying acceptance of that language or an authorized translation.

For each candidate, record official URL, check date, audience/genre evidence, supported format, requirements, submission/publication route, and uncertainty. If the authoritative page is inaccessible, mark terms unverified and exclude the venue from immediate execution. Hosting capability alone does not establish audience fit.

## Resolve the specific release boundary

Before releasing full text or excerpts, inspect applicable commitments:

- Prior publication history and whether the target journal accepts reprints or treats online access as prior publication.
- Existing licenses/exclusivity covering this work, language, medium, territory, or period.
- Rules for simultaneous submissions, multiple pieces, AI-assisted/generated work, and withdrawal after acceptance elsewhere.
- Whether the story belongs to a KDP Select edition; verify current terms and permitted excerpts instead of assuming exemption.
- Permissions for translations, illustrations, quotations, or third-party audio in this release.

Record `CONFIRMED`, `UNRESOLVED`, or `CONFLICT`, with evidence for the specific use. Public hosting does not imply unrestricted reuse; removing a post does not establish that the work is unpublished again. Do not invent a universally safe excerpt percentage or make unsupported contract assurances.

If one route conflicts with a commitment, continue a safe alternative or prepare a draft. Escalate the concrete conflict before publication. Do not add rights investigations to an ordinary blurb request without a release decision.

## Capability and execution

Inspect tools and accounts. API documentation does not establish session access. If execution is unavailable, deliver the complete manual package: text/payload, title, author credit, required cover note/synopsis, metadata, destination, timing, and known conditions.

Match the final version/destination to the user's instructions. Authorization persists; do not re-request approval for the same scoped action. Story publication, editorial submission, fee payment, and contractual changes must each be covered by the request or prior authorization.

## Release ledger

For multi-story projects maintain one table in `FICTION_RELEASE_LEDGER.md`:

```text
story_id | title | source_version/location | format/dependencies | editorial_allocation | excerpt_location/cuts | spoiler_boundary | rights_status/evidence | venue | submission_or_release_date/timezone | authorization_reference | execution_state | external_id/url | next_read/CTA | experiment_id
```

Keep editorial allocation, rights status, and execution state separate. States include `DRAFT`, `SUBMITTED`, `ACCEPTED`, `REJECTED`, `SCHEDULED`, `PUBLISHED`, and `WITHDRAWN`. Record dated events per venue rather than overwriting submission history. Inspect uncertain outcomes before retrying.

## Verified starting points, not fixed recommendations

Checked 2026-09-10; re-check current official terms/capabilities at use time:

- [Substack: publishing a new post](https://support.substack.com/hc/en-us/articles/360037831771-How-do-I-publish-a-new-post-on-Substack) documents web publication and optional email/app delivery. This supports a possible reading destination, not guaranteed discovery or audience fit.
- [KDP Select](https://kdp.amazon.com/en_US/select) states that enrolled digital books are exclusive to KDP during enrollment, including restrictions on website/blog distribution. Inspect applicable terms and the proposed work/excerpt before parallel publication.
