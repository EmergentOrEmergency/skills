# Skills

Reusable skills and agent instructions for fiction development, book marketing, on-device mobile computer vision, and project development through a Native SDLC workflow.

## Included skills

| Skill | Purpose |
|---|---|
| [`narrative-architect`](./skills/narrative-architect/) | Develop, outline, draft, critique, and revise fiction while preserving voice, point of view, and continuity. |
| [`fiction-discovery`](./skills/fiction-discovery/) | Find readers for collections, linked series, serial narratives, and introspective first-person fiction through samples, publication routes, and reader-return experiments. |
| [`book-marketing-office`](./skills/book-marketing-office/) | Orchestrate research, strategy, content, launch, paid growth, measurement, and iteration as an accountable book CMO. |
| [`market-intelligence`](./skills/market-intelligence/) | Research readers, comparable titles, category dynamics, positioning, and discoverability. |
| [`audience-growth`](./skills/audience-growth/) | Build an ethical, consent-aware reader audience across owned channels, communities, and partnerships. |
| [`content-social`](./skills/content-social/) | Create channel-native content systems, editorial calendars, creative briefs, and scheduling payloads. |
| [`launch-sales`](./skills/launch-sales/) | Plan launches, relaunches, storefront conversion, promotions, email sequences, and sales operations. |
| [`ads-growth`](./skills/ads-growth/) | Design controlled paid-media experiments with budget caps, profitability thresholds, and approval gates. |
| [`analytics-cfo`](./skills/analytics-cfo/) | Turn sales and marketing data into contribution profit, CAC, ROAS, attribution, and stop/scale decisions. |
| [`android-realtime-vision`](./skills/android-realtime-vision/) | Build and debug real-time on-device computer vision on Android: CameraX, LiteRT/TFLite inference, and an aligned Compose bounding-box overlay. |

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

Copy the directories you want from skills/ into your configured skill search location, or package them in a plugin. Keep sibling marketing skills together when using `book-marketing-office`, because the orchestrator routes specialized work to them.

## Validation

Every included skill has been checked with the Codex `skill-creator` validator. The Python utilities require only the Python standard library and have been compiled and exercised with representative fixtures.

## Important operational note

Platform capabilities, APIs, account permissions, pricing, and policies change. The marketing skills require current verification before external execution and never treat a plan as authorization to publish, spend, send messages, or modify storefront data.

## Imported development agents

The package includes two callable Copilot profiles and one internal worker contract:

| File | Role |
|---|---|
| [automation-wiki-generator.agent.md](./agents/automation-wiki-generator.agent.md) | Builds or refreshes a concise local wiki; writes only under the target project's `wiki/`. |
| [native-sdlc-orchestrator.agent.md](./agents/native-sdlc-orchestrator.agent.md) | Coordinates intent, specification, architecture, implementation planning, delegated execution, review, and requirement verification. |
| [native-sdlc-code-worker.md](./agents/native-sdlc-code-worker.md) | Defines the bounded workstream input/output contract used by the orchestrator; it is not a standalone callable profile. |

The agent definitions retain the `.agent.md` Copilot format. Merely cloning this repository does not register them as Codex custom agents. Codex can read and follow the Markdown instructions when you explicitly supply the path. In that mode, the current task acts as the orchestrator and uses the delegation tools actually available in its host.

The imported workflow has been generalized: no fixed company namespace, internal server, user-profile installation, bundled service template, or pinned model is required. Existing scoped user authorization is carried forward.

### Related skills

| Skill | Purpose |
|---|---|
| [native-sdlc-brainstorm](./skills/native-sdlc-brainstorm/) | Classify the delivery path and turn the idea into `intent.md`. |
| [native-sdlc-specification](./skills/native-sdlc-specification/) | Define testable requirements, acceptance criteria, and stable identifiers. |
| [native-sdlc-architecture](./skills/native-sdlc-architecture/) | Allocate requirements to components and record architecture decisions. |
| [native-sdlc-planning](./skills/native-sdlc-planning/) | Plan bounded workstreams, dependencies, tests, and requirement coverage. |
| [native-sdlc-code-generation](./skills/native-sdlc-code-generation/) | Implement the approved plan within the assigned scope. |
| [native-sdlc-code-review](./skills/native-sdlc-code-review/) | Independently review scope, correctness, contracts, and evidence. |
| [template-bootstrap](./skills/template-bootstrap/) | Bootstrap from an approved local template or verified framework scaffolder. |
| [verification-before-completion](./skills/verification-before-completion/) | Verify the requested outcome and map claims to observed evidence. |
| [systematic-debugging](./skills/systematic-debugging/) | Investigate failures through falsifiable hypotheses and focused diagnostics. |
| [jira-sdlc-tracking](./skills/jira-sdlc-tracking/) | Optionally mirror workstreams through an available authenticated Jira connector. |

Application templates and private integration clients are not bundled. Bootstrap accepts user/project-provided templates or a verified scaffolder. Jira tracking is disabled unless requested and requires an available connector or configured API client; without one, it produces an issue preparation package and reports that tracking was not executed.

### Try the orchestrator in Codex

Open the **target project** as your Codex workspace, then send this prompt, replacing the checkout path and idea as appropriate:

```text
Read and follow C:/src/Skills/agents/native-sdlc-orchestrator.agent.md.
The bundle root is C:/src/Skills; resolve its related skills from
C:/src/Skills/skills/ and its worker contract from C:/src/Skills/agents/.

The target project is the current workspace, not the Skills repository.
Start with context discovery and brainstorming for this idea:
[Describe the product, its users, and the intended outcome.]

Create the requirements artifacts in the target project.
Use Italian for our conversation. Keep Jira tracking disabled.
Follow the staged review workflow; do not generate application code
before the implementation plan is approved.
```

The Markdown tool list belongs to the Copilot profile. In Codex, use the host's actual tools and disclose unavailable capabilities; do not simulate a callable `read_agent` or other tool that is absent. For automatically discoverable Codex custom agents, a separate native TOML configuration would be required; this import does not install or activate one.

Keep the complete checkout accessible. Agent instructions resolve `<bundle-root>` to that checkout, while generated `requirements/`, `wiki/`, and application files belong to the target project.

### Package layout and migration

```text
agents/
  automation-wiki-generator.agent.md
  native-sdlc-orchestrator.agent.md
  native-sdlc-code-worker.md
skills/
  <skill-name>/SKILL.md
  <skill-name>/agents/openai.yaml
  <skill-name>/references/       # when used
  <skill-name>/scripts/          # when used
```

Existing skills now live beneath `skills/`; their workflows are preserved. The Android skill's description received a YAML syntax correction. Update GitHub installation paths from `<skill-name>` to `skills/<skill-name>`; relative references inside each skill retain their layout. Copying only an orchestrator profile is insufficient for the full workflow: also supply its worker contract and related skills.

The development workflow preserves the source package's acknowledgment that staged planning, review, debugging, and verification practices were informed in part by the MIT-licensed [obra/superpowers](https://github.com/obra/superpowers) project. No application templates from the source package are included.
