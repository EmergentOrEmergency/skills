---
name: narrative-architect
description: Develop, outline, draft, critique, and revise fiction while preserving authorial voice, continuity, point of view, and the distinction between narrative quality and commercial hypotheses.
metadata:
  language: "it"
  version: "1.2.0"
---

# Narrative Architect

## Purpose

Use this skill when the user wants to create or improve fiction: novel,
novella, short story, serial, screenplay-like narrative, or a narrative
concept. It covers the full pipeline from idea selection to final
revision.

This skill is a **diagnostic and creative system, not a formula**.
Frameworks are used to expose weaknesses, never to force every story
into identical beats.

## Core principles

1.  Story quality and commercial potential are related but different.
    Score them separately.
2.  Familiarity helps orientation; novelty creates interest. Seek
    **Familiar + Novel**.
3.  External plot should pressure the protagonist's internal conflict.
4.  Every important scene should change the state of the story.
5.  Preserve mystery and subtext. Do not explain what the reader can
    infer.
6.  Maintain a Story Bible and continuity ledger for long-form work.
7.  Critique and generation are separate modes. Do not silently rewrite
    when asked only to diagnose.
8.  Never promise success. Market scores are hypotheses, not guarantees.
9.  When current market validation is requested, use fresh external
    research rather than intuition alone.
10. Preserve the author's desired voice. Do not normalize everything
    into generic polished LLM prose.

# Workflow

Default pipeline:

`DISCOVER → EVALUATE → MARKET_VALIDATE (optional) → EVOLVE → PREMISE → BOOK_SPEC → ARCHITECT → CHARACTERS → POV_VOICE → OUTLINE → VISUAL_PLAN → SCENE_PLAN → WRITE → CRITIQUE → REWRITE → CONTINUITY_CHECK → FINAL_EDIT`

Do not force the user through every stage. Enter at the stage matching
their request.

# Modes

## 1. DISCOVER

Generate story territories, not merely random premises.

For each candidate identify: - genre / subgenre - target reader -
central fascination - emotional promise - protagonist type - conflict
engine - unusual constraint or inversion - possible thematic question -
why this story may be worth telling now

Prefer 5--10 meaningfully different candidates over superficial
variations.

## 2. EVALUATE

Evaluate a premise on two independent axes.

### Narrative Potential --- 100 points

-   High-concept clarity: 10
-   Hook / curiosity gap: 10
-   Conflict engine: 15
-   Character pressure and difficult choices: 15
-   Escalation capacity: 10
-   Emotional engine: 15
-   Thematic depth: 10
-   Distinctiveness: 10
-   Ending/payoff potential: 5

### Commercial Potential --- 100 points

-   Audience clarity: 10
-   Genre fit / reader expectations: 10
-   Familiar + Novel balance: 15
-   Pitchability in one sentence: 10
-   Title/cover/blurb potential: 10
-   Comparable-title fit: 10
-   Discoverability / word-of-mouth potential: 10
-   Series / IP / adaptation potential where relevant: 10
-   Author advantage: 10
-   Timing / market hypothesis: 5

Always explain the 3 strongest elements and 3 biggest risks. A numerical
score without diagnosis is insufficient.

Score interpretation: - 85--100: unusually promising; stress-test before
committing. - 70--84: strong foundation; improve weak dimensions. -
55--69: viable but currently generic, narrow, or structurally weak. -
\<55: do not discard automatically; mutate the premise before judging
again.

Scores are comparative heuristics, not probabilities of publication or
sales.

## 3. MARKET_VALIDATE

Use only when the user wants commercial validation, current trends,
positioning, or comparable titles.

Research current evidence when tools are available: - recent successful
comparable titles - genre/subgenre demand and saturation - reader
reviews and recurring praise/complaints - community discussions -
positioning, covers, blurbs, titles, formats - underserved combinations
or recurring reader desires

Distinguish: - **Evidence** --- observed market signals - **Inference**
--- interpretation of those signals - **Speculation** --- uncertain
prediction

Do not equate bestseller imitation with a good opportunity. Search for
unmet expectations and differentiating angles.

## 4. EVOLVE --- Idea Evolution Engine

If an idea is weak or the user asks for stronger variants: 1. Diagnose
the bottleneck. 2. Create mutations by changing one major variable at a
time. 3. Create several radical mutations by changing two or more
variables. 4. Re-score the strongest variants. 5. Hybridize compatible
strengths. 6. Return 2--3 finalists and explain the tradeoffs.

Mutation operators: - protagonist inversion - antagonist inversion -
setting displacement - time-period displacement - moral dilemma
injection - constraint amplification - stakes personalization - genre
collision - perspective change - hidden relationship - asymmetric
information - ticking clock - cost-of-power rule - expected trope
reversal - ending-first redesign - audience shift

Do not merely make the premise bigger. Often a more personal cost is
stronger than a larger catastrophe.

## 5. PREMISE

Before detailed outlining, establish: - one-sentence logline -
1-paragraph premise - genre/subgenre - target reader - emotional
promise - central dramatic question - protagonist want - protagonist
need - misbelief / wound when applicable - antagonist/opposing force -
stakes - thematic question (prefer a question before a slogan) - core
novelty - ending hypothesis

A theme should emerge through choices and consequences, not lectures.

## 6. ARCHITECT

Choose structure based on the story rather than habit.

Available diagnostic maps:

### Three Acts

-   Act I (\~25%): ordinary state, protagonist, disturbance/catalyst,
    commitment.
-   Act II (\~50%): pursuit, complications, rising stakes, midpoint
    reversal/redefinition.
-   Act III (\~25%): final convergence, climax, consequence/new
    equilibrium.

### Save the Cat --- functional beat map

Opening Image → Theme Stated → Set-Up → Catalyst → Debate → Break into
Two → B Story → Fun and Games → Midpoint → Bad Guys Close In → All Is
Lost → Dark Night of the Soul → Break into Three → Finale → Final Image.

Treat percentages as diagnostics, not laws. Beats may combine, move, or
be expressed subtly.

### Hero's Journey

Use primarily to inspect inner transformation: ordinary world → call →
refusal → mentor → threshold → tests/allies/enemies → ordeal → reward →
return → resurrection → elixir.

### Seven-Point Structure

Hook → Plot Turn 1 → Pinch 1 → Midpoint → Pinch 2 → Plot Turn 2 →
Resolution.

Recommended use: - commercial/high-pacing genre fiction: Save the Cat as
pacing diagnostic - transformation-centered story: Hero's Journey as
character diagnostic - lightweight planning: Seven Points - discovery
writing/pantser: diagnose retrospectively rather than over-outline

Hybrid use is allowed: e.g. Save the Cat for pacing + Hero's Journey for
internal arc.

## 7. CHARACTERS

For each major character maintain: - role/function - external want -
internal need - misbelief / wound - fear - contradiction -
leverage/power - secret - relationship to protagonist - voice markers -
knowledge at current story point - arc: positive / flat / negative /
mixed - irreversible choice

Character rule: attempts to achieve the **want** should progressively
expose the **need**.

Secondary characters should provide at least one useful function: ally,
obstacle, mirror, foil, temptation, witness, catalyst, thematic
counterargument. Merge redundant characters.

## 7A. POV_VOICE --- First-Person Character-Driven Engine

Use this module whenever the story is narrated in first person, or when
voice and subjective interpretation are central. First person is not
merely third person with "io": the narrator selects, interprets,
distorts, omits, and emotionally colors everything the reader receives.

### Dual-state model

Maintain two separate records: - **CHARACTER_TRUTH** --- what is
actually true about the protagonist, their wound, relationships,
situation, and thematic need. - **NARRATOR_BELIEF** --- what the
narrating self currently believes is true.

Never let the narrator automatically articulate CHARACTER_TRUTH. Growth
occurs partly through the changing gap between these states. The
narrator may be sincere yet wrong. Unreliability does not require
deliberate lying.

### First-person arc chain

For a positive change arc, test this causal chain:
`WOUND/GHOST → MISBELIEF/LIE → WANT → CHOICES → CONSEQUENCES → MIDPOINT MOMENT OF TRUTH → RESISTANCE/EXPERIMENT → WANT-vs-NEED CHOICE → CLIMAX → NEW SELF`

The external plot must repeatedly make the old belief useful enough to
be tempting, but costly enough to become unsustainable. Avoid making
Want "bad" and Need "good" by definition; strong inner conflict often
pits two legitimate desires against each other.

### Midpoint as self-recognition

For character-driven first person, the midpoint should normally do more
than raise external stakes. Test whether it creates a **model-breaking
event**: - Before midpoint: the narrator can still explain events using
the Misbelief. - At midpoint: evidence/revelation makes that
interpretation inadequate. - After midpoint: the narrator may resist the
Truth, but cannot fully return to the old model. - The shift should
alter tactics in the external plot, not remain a private realization
only.

A midpoint can be a revelation, reversal, apparent victory/defeat,
mirror moment, or encounter that forces self-recognition. Do not require
explicit epiphany language.

### Voice Profile

Maintain for the narrator: - vocabulary/register - sentence length and
rhythm - education/profession/culture as relevant to perception - humor
and taboo subjects - favorite comparisons/metaphor domains - what they
notice first - what they habitually ignore - emotions they admit -
emotions they rename, rationalize, or deny - self-image - blind spots -
recurring verbal habits (use sparingly) - how they describe allies,
rivals, strangers, and themselves - narrative distance: immediate /
reflective / retrospective - reliability dimensions: factual,
interpretive, emotional, moral - temporal narrator: experiencing-I vs
narrating-I, if retrospective

**Voice rule:** voice is not only *how* the narrator speaks; it is also
*what enters their attention and what does not*. Select details through
the narrator's values, expertise, fears, desire, and current belief.

### Information discipline

In first person: - never reveal facts the narrator cannot perceive,
know, infer, remember, or plausibly reconstruct - distinguish
observation from inference - allow incorrect inference when
character-consistent - do not cheat twists by making the narrator
unnaturally avoid thinking about something they obviously know solely to
hide it from the reader - if using retrospective narration, define how
much the older narrating self knows and how much hindsight is allowed

### Interior narration

Do not convert first person into constant introspection. Internal
thought should create at least one of: interpretation, conflict,
misdirection, decision, emotional consequence, thematic pressure, or
voice pleasure. Compress repetitive processing.

Prefer **dramatic irony through self-deception**: let behavior and
concrete details permit the reader to infer something the narrator
cannot yet admit. Avoid explaining the discrepancy immediately
afterward.

### First-person voice drift check

Across chapters, compare samples for: - vocabulary drift -
sentence-rhythm drift - humor drift - unexplained changes in
self-awareness - narrator suddenly noticing things outside established
attention patterns - exposition that sounds like the author rather than
the character - every character's dialogue becoming infected by narrator
voice

Growth may change voice, but changes should be earned and traceable to
the arc.

## 8. OUTLINE

Create a sequence of story-changing events rather than a list of things
that happen.

For every chapter/sequence track: - POV - location/time - objective -
obstacle - conflict - new information - decision - cost - state change -
setup planted - payoff consumed - open question / forward pull

Check that escalation changes the nature of the problem, not only its
magnitude.

## 9. SCENE_PLAN --- Scene Engine

Before drafting an important scene, establish: 1. Entry state --- what
is true at the start? 2. POV desire --- what does the POV character want
right now? 3. Obstacle --- what prevents it? 4. Tactic --- what do they
try? 5. Escalation --- how does resistance intensify or mutate? 6.
Reveal/reversal --- what changes the reader's or character's model? 7.
Choice --- what decision exposes character? 8. Cost --- what is lost,
risked, compromised, or delayed? 9. Exit state --- what is now
different? 10. Forward pull --- why continue reading?

A scene should normally advance plot, character, relationship, theme, or
knowledge --- preferably more than one. A scene doing none is a
deletion/merge candidate.

Do not require a cliffhanger every chapter. Vary endings: revelation,
decision, threat, emotional turn, unanswered question, new goal,
unsettling image, reversal.

### First-person dual-layer scene card

For first-person character-driven stories, silently track two
simultaneous arcs:

**EXTERNAL SCENE** - immediate goal - obstacle/conflict - tactic -
outcome/disaster or altered state

**INTERNAL SCENE** - expectation entering the scene - narrator's
interpretation of events - emotional/physical reaction - Misbelief
reinforced, challenged, or complicated - new information - dilemma -
decision/new goal

**VOICE/INFORMATION** - what the narrator notices - what the narrator
misses - what the reader may infer beyond the narrator - what the
narrator refuses to admit or mislabels - subtext

Use the classic Scene/Sequel causal chain as a diagnostic:
`Goal → Conflict → Outcome/Disaster → Reaction → Dilemma → Decision`.
The Decision should naturally create or modify the next Goal. Elements
may be compressed, implied, interrupted, or distributed across chapter
boundaries; do not mechanically force six visible blocks into every
scene.

## 10. WRITE

When drafting prose: - enter scenes as late as practical - establish POV
quickly - create an implicit question early - favor concrete detail over
generic description - use sensory anchors selectively - keep knowledge
inside POV limits - use deep POV where stylistically appropriate; reduce
filter phrases such as "vide", "sentì", "pensò" when they add distance -
dramatize key moments in scene; summarize connective tissue when
useful - compress real conversation into purposeful dialogue - make
character voices distinguishable - prefer subtext to explicit emotional
explanation - interrupt dialogue with meaningful action/behavior, not
random gestures - filter technical exposition through character goals
and conflict - alternate tension and recovery

"Show, don't tell" is not absolute. Tell when compression, clarity,
pacing, or narrative voice benefits from it; show when the reader should
experience the moment.

### Additional first-person drafting rules

-   Filter description through desire and attention; do not provide
    neutral camera coverage unless the voice calls for it.
-   Let diction, syntax, omissions, judgments, and metaphor reveal
    character without constant self-description.
-   Keep a productive gap between what happened, what the narrator
    thinks happened, and what the reader suspects happened.
-   In retrospective first person, manage two potential voices: the self
    who experienced events and the self telling them later. Define
    whether hindsight comments are rare, frequent, ironic, regretful, or
    absent.
-   Do not make the narrator implausibly self-diagnostic. A character
    can display a Need long before they can name it.
-   After consequential action, give enough Reaction/Dilemma for the
    choice that follows to feel psychologically caused; compress it when
    pacing demands.

## 11. FORESHADOWING & PAYOFF LEDGER

Maintain entries: - ID - setup - first appearance - intended
interpretation - hidden true meaning - reinforcement(s) - payoff -
payoff location - status: planted / reinforced / paid / abandoned

A twist should ideally be surprising on first read and
plausible/inevitable in retrospect.

Red herrings must serve story/character and should not rely on cheating
the POV.

## 12. CONTINUITY / STORY BIBLE

For long projects maintain canonical records for: - character facts and
physical details - relationships - timeline/date/age - locations - world
rules - technology/magic rules - injuries/resources/inventory where
relevant - secrets - who knows what and when - promises, setups, clues,
unresolved questions - terminology/spelling - chronology of major events

Before writing a continuation, consult the Bible and the latest scene
state. New prose must not silently override canon. If a contradiction is
desirable, flag it for author approval.

## 13. CRITIQUE

Critique in layers, largest problems first: 1. premise / promise 2.
structure and pacing 3. character arcs and motivation 4. causality and
stakes 5. scene function 6. POV and information control 7.
dialogue/subtext 8. prose/style 9. continuity 10. copyediting

Do not spend time polishing sentences in a scene likely to be deleted.

For each problem return: - symptom - why it hurts the story - severity:
critical / major / moderate / minor - likely cause - recommended
intervention - optional example, clearly marked as an example

## 14. PACING CHECK

Inspect: - time to catalyst - time to protagonist commitment - distance
between meaningful reversals - midpoint strength - length of reaction
without new pressure - repeated scene functions - exposition clusters -
consecutive high-intensity scenes without recovery - chapters ending
after all tension has resolved - late-book acceleration or rushed climax

Do not optimize for constant speed. Rhythm requires contrast.

## 15. ANTI-LLM PROSE CHECK

Actively detect and reduce common machine-writing signatures when they
conflict with the chosen voice: - every sentence polished to the same
smooth cadence - excessive parallel triples and rhetorical symmetry -
generic metaphors and atmospheric filler - repeated body-language
clichés - explaining an emotion after already showing it - explaining
the meaning of a line of dialogue immediately afterward - all characters
using the same vocabulary/rhythm - excessive therapeutic
self-awareness - characters behaving too rationally for the situation -
constant "not X, but Y" constructions - repetitive micro-cliffhangers -
fake profundity / moralizing conclusions - excessive
adjectives/adverbs - unnecessary recap of information the reader already
knows - overuse of ominous narrator hints such as "he could not know
that..." - perfectly explicit motivations where ambiguity would be
stronger - generic sensory lists added mechanically

Correction rule: do not replace one detectable formula with another.
Preserve intentional quirks, roughness, dialect, humor, silence, and
asymmetry.

## 16. REWRITE

When rewriting: 1. identify the requested objective 2. preserve canon
and necessary information 3. preserve or deliberately modify voice as
requested 4. solve the highest-level problem first 5. avoid introducing
new facts without need 6. compare before/after function, not merely
elegance

If multiple solutions are plausible, explain the tradeoff or provide
genuinely distinct variants.

## 17. FINAL_EDIT

Perform passes in this order: 1. structural integrity 2. character arc
integrity 3. scene necessity 4. continuity / setup-payoff 5. POV and
information 6. dialogue 7. prose rhythm and repetition 8.
factual/technical consistency 9. copyedit and formatting

# Book Architecture, Citations, and Visual Direction

## BOOK_SPEC --- Physical and Editorial Architecture

Before detailed outlining, define a provisional book specification.
Treat all numeric targets as planning ranges, not laws.

Track: - genre / subgenre - target audience - publication strategy:
print / ebook / serial / hybrid - target word count and acceptable
range - target chapter count - expected chapter-length rhythm - POV and
tense - part structure, if any - front matter - back matter - visible
notes policy - bibliography / source-note policy - real-world claims
policy - illustration strategy - print constraints: black-and-white /
color / trim assumptions when known

### Length logic

Do not choose length from a universal rule. Infer a provisional range
from genre, audience, comparable titles, format, and story complexity.
When market validation is requested, verify current comparable-title
expectations with fresh sources.

Use length diagnostically: - map major structural turns to approximate
manuscript position - warn when a major beat is materially displaced
without an intentional reason - detect underdeveloped acts, rushed
endings, bloated middles, and repeated scene functions - vary chapter
length intentionally rather than forcing a fixed average - never pad
prose merely to reach a target

### Front matter / back matter

Consider only what the project needs: - title page - copyright page -
dedication - epigraph - contents - author's note - acknowledgments -
appendices - endnotes - bibliography / sources - image credits

For pure fiction, default to minimal scholarly apparatus. For
historical, documentary, scientific, technical, or hybrid narrative,
maintain stronger source traceability.

## RESEARCH_LEDGER --- Facts, Notes, and Quotations

When the story uses real-world facts, maintain an internal ledger: -
claim/fact ID - claim as used - source - source location - verification
status - chapter/scene - whether visible citation is required -
uncertainty/conflict notes - last verification date when time-sensitive

Do not fabricate citations, quotations, page numbers, authors, dates, or
source details.

### Quotation policy

For every non-original quotation track: - exact text - attributed
speaker/author - original source if discoverable - verification status -
intended use: epigraph / dialogue quote / body / note - rights status:
public domain / permission / needs rights review / unknown

Attribution is not the same as permission. Flag uncertain copyright or
permissions questions for publication-stage review. Prefer paraphrase
when exact wording is unnecessary.

## VISUAL_PLAN --- Visual Narrative Director

Images are editorial objects, not automatic decoration. First ask what
each image does for the reader.

Possible functions: - NARRATIVE --- advances or changes story
understanding - EXPLANATORY --- makes a complex idea easier to
understand - EVIDENCE --- shows a document, artifact, data point, or
source relevant to a factual claim - ORIENTATION --- map, timeline,
family tree, spatial diagram - ATMOSPHERE --- creates a deliberate
emotional or aesthetic transition - DIEGETIC --- exists inside the story
world: message, diary page, photograph, interface, newspaper clipping -
DECORATIVE --- aesthetic only

Default rule: if removing an image loses nothing meaningful, remove it
unless decoration is an explicit design goal.

### Image quantity

Never impose a universal image count.

Choose density from: - genre and reader expectations - age group - print
vs ebook - color vs monochrome economics - whether visuals carry
evidence or explanation - comparable titles - pacing and interruption
cost

Default tendencies: - adult prose fiction: sparse or no interior images
unless conceptually justified - speculative/historical fiction:
selective maps, artifacts, diagrams, or diegetic visuals when useful -
illustrated/younger-reader formats: visual cadence is part of the format
and must be planned accordingly - nonfiction/technical/hybrid narrative:
include visuals whenever they materially improve comprehension,
evidence, orientation, or retention

When current commercial positioning matters, validate visual density
against relevant recent comparable books rather than relying on these
tendencies alone.

### Visual Bible

Before generating multiple images, define: - visual identity - medium /
rendering approach - realism level - line/shape language - contrast and
lighting - texture - composition tendencies - recurring motifs -
representation of people - representation of technology/world elements -
period/era cues - typography inside images - aspect-ratio families -
caption style - color philosophy, including grayscale compatibility when
relevant - MUST rules - MUST NOT rules

Keep the visual system coherent across the project. Do not allow
chapter-to-chapter style drift unless the change is narratively
intentional.

### Visual Ledger

For each planned visual record: - ID - chapter / scene / placement -
function - narrative or explanatory purpose - information revealed -
first-view interpretation - post-reveal interpretation, if applicable -
spoiler risk - Visual Bible style ID - caption required? - alt text
required? - source: generated / commissioned / licensed / public domain
/ author-owned - rights / permission status - print constraints -
status: proposed / approved / generated / final

### Images as storytelling

A visual may: - foreshadow a later revelation - contradict an unreliable
narrator through observable detail - recur with changed meaning - reveal
spatial relationships more elegantly than exposition - function as an
in-world artifact - provide evidence in documentary/hybrid narrative

Do not let an image accidentally reveal information the text
intentionally withholds. Run a spoiler check against the knowledge state
of the reader at its placement.

### First-person visual rule

For first-person fiction, decide explicitly whether a visual
represents: 1. what objectively exists in the story world, 2. what the
narrator perceives/remembers, 3. an artifact the narrator can access, or
4. editorial information supplied directly to the reader.

This distinction matters when the narrator is unreliable. A
contradiction between text and image may be powerful, but it must be
intentional and fair.

### Production hygiene

Before final publication, verify as applicable: - sufficient effective
resolution for target reproduction size - legibility of labels and
typography at actual page size - grayscale behavior when printing
monochrome - margins / bleed / safe area with the chosen publishing
workflow - ebook reflow and small-screen readability - captions and
figure numbering - alt text / accessibility - image credits - licenses,
releases, and permissions - consistency between captions, text
references, and final figure order

Do not invent technical print specifications when the publishing
platform, trim size, or printer is unknown. Request or verify the actual
production requirements.

### Image-generation prompts

When the user wants generated visuals, derive prompts from the Visual
Bible plus the visual's ledger entry. Preserve: - subject continuity -
era/world rules - character identity - camera/composition intent -
narrative function - spoiler boundary - established visual language

Do not let prompt embellishment introduce new canon.

## VISUAL_REVIEW

Review the complete visual program after the outline and again before
final layout.

Check: - every visual has a reason to exist - no repetitive
illustrations with the same function - visual density supports rather
than interrupts pacing - style is coherent - maps/diagrams agree with
canon - captions do not over-explain - images do not spoil later
reveals - generated visuals do not silently contradict character/world
facts - rights status is known for every non-original asset - the book
still works when an image cannot render in a given format

# Success diagnostics

Ask or verify: - Is the central conflict clear early enough for this
genre? - Is the protagonist pushed into consequential trouble quickly
enough? - Do attempts to solve problems create new costs or
complications? - Is there a meaningful midpoint/redefinition? - Does the
low point make the climax feel earned? - Does the climax resolve the
central dramatic question through consequential choice/action? - Does
the ending pay the emotional promise? - Does the theme emerge from
consequences? - Are major voices distinguishable? - Are setups paid off
or intentionally left open? - Can the premise be pitched clearly? - Is
the project differentiated from its likely comparables? - Is the planned
length appropriate to the story, audience, and format rather than padded
to a target? - Are factual claims and quotations traceable when the
project requires sourcing? - Does every planned visual have a clear
function, coherent style, safe placement, and known rights status?

# Output conventions

For development work, prefer concise structured outputs over long
lectures.

When evaluating an idea, default to: - Logline - Narrative Potential
/100 - Commercial Potential /100 - Strongest assets - Biggest risks -
Best mutations - Recommended next step

When writing a scene, do not expose the internal checklist unless the
user asks. Use it silently and output the scene.

When critiquing, do not rewrite the entire text unless requested.

# Safety against formulaic fiction

Framework compliance is never the goal. If breaking a rule creates a
stronger intended effect, identify the tradeoff and allow the exception.
Originality, emotional truth, coherence, and reader experience outrank
beat-sheet conformity.

# Source basis

This skill was developed from the user's September 2026 craft guide,
which synthesizes public narrative-craft approaches including Three-Act
Structure, Save the Cat, Hero's Journey, Seven-Point Structure,
character want/need/misbelief, dialogue/subtext, hooks, deep POV,
tension, foreshadowing/payoff, worldbuilding, drafting, and layered
revision. The skill expands that material into an agent-oriented
workflow, adding idea discovery/evaluation, commercial-vs-narrative
scoring, market validation, idea evolution, scene-state tracking, Story
Bible/continuity, payoff ledgers, pacing diagnostics, and anti-LLM prose
checks.

# Research extensions added in v1.1

The first-person/character-driven module also incorporates operational
principles synthesized from public craft material on Dwight Swain-style
Scene/Sequel and K.M. Weiland's treatments of scene causality,
Want/Need, Lie/Truth, and the Midpoint as a Moment of Truth. These are
used as diagnostics, not mandatory formulas.

Key research-derived rules: - Scene/Sequel provides a causal chain: Goal
→ Conflict → Outcome/Disaster → Reaction → Dilemma → Decision; the
decision feeds the next goal. - Reaction and dilemma are not filler:
they are high-value locations for character development, theme, and
believable decision-making. - Want/Need and Lie/Truth should be nuanced
rather than simplistic good-vs-bad binaries. - In a positive arc, the
Midpoint can function as a Moment of Truth: the protagonist glimpses a
more accurate model but need not immediately abandon the old Lie. -
Later structural pressure should force a consequential choice between
incompatible versions of Want/Need or Lie/Truth, making the climax an
expression of character rather than merely plot mechanics.

# Recommended project files

For substantial projects, maintain these companion artifacts as
needed: - `STORY_BIBLE.md` - `BOOK_SPEC.md` - `VOICE_PROFILE.md` -
`CHARACTER_ARC_LEDGER.md` - `SCENE_CARD.md` or
`FIRST_PERSON_SCENE_CARD.md` - `FORESHADOWING_LEDGER.md` -
`RESEARCH_LEDGER.md` - `VISUAL_BIBLE.md` - `VISUAL_PLAN.md`

These files are working memory for the writing system. Keep them
concise, canonical, and updated after approved story changes.
