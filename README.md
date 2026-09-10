# Skills

Reusable Codex and ChatGPT skills for fiction development and autonomous, evidence-led book marketing.

## Included skills

| Skill | Purpose |
|---|---|
| [`narrative-architect`](./narrative-architect/) | Develop, outline, draft, critique, and revise fiction while preserving voice, point of view, and continuity. |
| [`book-marketing-office`](./book-marketing-office/) | Orchestrate research, strategy, content, launch, paid growth, measurement, and iteration as an accountable book CMO. |
| [`market-intelligence`](./market-intelligence/) | Research readers, comparable titles, category dynamics, positioning, and discoverability. |
| [`audience-growth`](./audience-growth/) | Build an ethical, consent-aware reader audience across owned channels, communities, and partnerships. |
| [`content-social`](./content-social/) | Create channel-native content systems, editorial calendars, creative briefs, and scheduling payloads. |
| [`launch-sales`](./launch-sales/) | Plan launches, relaunches, storefront conversion, promotions, email sequences, and sales operations. |
| [`ads-growth`](./ads-growth/) | Design controlled paid-media experiments with budget caps, profitability thresholds, and approval gates. |
| [`analytics-cfo`](./analytics-cfo/) | Turn sales and marketing data into contribution profit, CAC, ROAS, attribution, and stop/scale decisions. |

## Marketing office architecture

`book-marketing-office` coordinates six focused marketing skills through a repeatable loop:

```text
baseline -> research -> strategy -> production -> distribution
         -> measurement -> experiment -> reallocation -> report
```

External actions are classified as `AUTO`, `AUTO_WITHIN_LIMITS`, or `APPROVAL_REQUIRED`. The skills prohibit fake reviews, undisclosed endorsements, impersonation, spam, fabricated scarcity, and misleading attribution.

The CMO skill also includes reusable references and standard-library Python utilities for:

- ROI, contribution profit, CAC, and ROAS calculations;
- first-, last-, linear-, and position-based attribution;
- import-ready content calendars;
- sales-window anomaly monitoring;
- experiment prioritization.

## Structure

Each skill follows the Agent Skills layout:

```text
skill-name/
├── SKILL.md
├── agents/
│   └── openai.yaml
├── references/    # when needed
└── scripts/       # when needed
```

## Installation

Copy the skill directories you want into your Codex skills directory, or package them in a plugin. Keep sibling marketing skills together when using `book-marketing-office`, because the orchestrator routes specialized work to them.

## Validation

Every included skill has been checked with the Codex `skill-creator` validator. The Python utilities require only the Python standard library and have been compiled and exercised with representative fixtures.

## Important operational note

Platform capabilities, APIs, account permissions, pricing, and policies change. The marketing skills require current verification before external execution and never treat a plan as authorization to publish, spend, send messages, or modify storefront data.
