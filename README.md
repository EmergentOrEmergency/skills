# Skills

Reusable Codex and ChatGPT skills for fiction development, autonomous evidence-led book marketing, and on-device mobile computer vision.

## Included skills

| Skill | Purpose |
|---|---|
| [`narrative-architect`](./narrative-architect/) | Develop, outline, draft, critique, and revise fiction while preserving voice, point of view, and continuity. |
| [`fiction-discovery`](./fiction-discovery/) | Find readers for collections, linked series, serial narratives, and introspective first-person fiction through samples, publication routes, and reader-return experiments. |
| [`book-marketing-office`](./book-marketing-office/) | Orchestrate research, strategy, content, launch, paid growth, measurement, and iteration as an accountable book CMO. |
| [`market-intelligence`](./market-intelligence/) | Research readers, comparable titles, category dynamics, positioning, and discoverability. |
| [`audience-growth`](./audience-growth/) | Build an ethical, consent-aware reader audience across owned channels, communities, and partnerships. |
| [`content-social`](./content-social/) | Create channel-native content systems, editorial calendars, creative briefs, and scheduling payloads. |
| [`launch-sales`](./launch-sales/) | Plan launches, relaunches, storefront conversion, promotions, email sequences, and sales operations. |
| [`ads-growth`](./ads-growth/) | Design controlled paid-media experiments with budget caps, profitability thresholds, and approval gates. |
| [`analytics-cfo`](./analytics-cfo/) | Turn sales and marketing data into contribution profit, CAC, ROAS, attribution, and stop/scale decisions. |
| [`android-realtime-vision`](./android-realtime-vision/) | Build and debug real-time on-device computer vision on Android: CameraX, LiteRT/TFLite inference, and an aligned Compose bounding-box overlay. |

## Marketing office architecture

`book-marketing-office` coordinates seven focused marketing skills through a repeatable loop:

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

## Fiction discovery

`fiction-discovery` adds two complementary workflows:

- **Collections and series:** choose a representative entry story, distinguish independent stories from dependent installments, allocate full releases versus excerpts, research venues, and design a sustainable return-reading path.
- **Introspective first-person fiction:** identify concrete emotional conflict, select excerpts preserving voice and ambiguity, and prepare situation-led, voice-led, or audio-reading presentations.

The skill checks relevant publication commitments before public release, distinguishes observed reading from click/open proxies, and connects to the CMO, content, and audience skills. It also works standalone. Installing it does not publish stories.

Example requests:

```text
Use $fiction-discovery to choose an entry story for this Italian collection,
research publication routes, and prepare a four-week discovery pilot.

Use $fiction-discovery to promote this introspective first-person story:
select a faithful excerpt, draft two presentations, and prepare a reading brief.
```

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
