# Plan: Session-Bracketing Rhythm + Plan/Handoff Document Template

**Drafted:** 2026-05-19 (warm-context, drafted in the same session that
triaged Issues #24 and #25)
**Drafted for:** A future maintenance session
**Status:** Cold-context review complete (findings appended below);
ready for execution

---

## What this is

This plan implements the headline pending items from the
facebook-moderation feedback triage (2026-05-18):

1. **Session-bracketing as a new Working Rhythm** in `core/nla-foundations.md`
2. **Plan/handoff document template** — the four-section structure plus
   two structural patterns from Letter #25
3. **Plans-not-runbooks preventive note** — small adjacent guidance

The three items form one coherent execution unit because the rhythm names
*when* to draft a plan; the template names *what* a plan contains; the
preventive note keeps the framework's framing consistent (the cardinal
rule depends on it).

The plan does *not* cover the /close enhancement (detect plan-shaped
artifacts + offer simulation) or the memory-mining beat — both are
accept-with-/think items that need design sessions before they can be
specified at this level. They're separate feedback log entries; this plan
leaves them alone.

This is a plan, not a runbook. Each step expects human input. The AI
executing this plan should surface options at decision points and pause
for human direction rather than proceeding mechanically. The maintainer
is the active session-manager.

## What this adds to the framework

`core/nla-foundations.md` currently has seven Working Rhythms:

1. The Improvement Loop
2. The Design Flow
3. The Update Cycle
4. Session Structure
5. Structural Change Discipline
6. The Inquiry Flow (added 2026-05-14)
7. The Validation Flow

This plan adds an eighth rhythm (working name: *The Session-Bracketing
Discipline*, parallel to *Structural Change Discipline*) and a plan/handoff
document template that operationalizes what plan-shaped artifacts contain.

The exact name and placement are open at draft time — see Step 1.

## Why this exists

Facebook-moderation's letters (Issues #24 and #25, triaged 2026-05-18)
made the empirical case: across multiple substantive sessions producing
future work, a recurring workflow shape emerged that the existing rhythms
don't name. The shape:

> do-work → plan-while-hot → simulate-cold → cold-question-check → adjust
> → close-and-clear

It fires when sessions produce non-trivial future work; not in every
session and not within every Design Flow execution.

The rhythm and template are paired. The rhythm tells the AI *when* to
draft a plan; the template tells the AI *what* the plan contains.
Documenting them together avoids the gap where the rhythm names the beat
but the structural form is absent.

The feedback log entries to consult during execution:

- "Session-bracketing as a new Working Rhythm"
- "Plan/handoff document template"
- "Plans-not-runbooks preventive guidance"

All three reference Issues #24 and #25 for the originating context.

## Pre-requisites for execution

1. The three feedback log entries listed above are still pending — i.e.,
   no other session has resolved them.
2. Cold-context simulation review of *this plan* has happened, with
   findings appended below the "## Cold-context review" section.
3. Cold-context question review of *this plan* has happened (catches the
   conceptual-frame gaps the simulation can't catch because the simulating
   agent inherits the frame).
4. No other framework session has substantively modified
   `core/nla-foundations.md` Working Rhythms section since 2026-05-19 — if
   so, re-read the section before drafting Step 2's content.

**On pre-requisites 2-3:** These describe the same workflow as the
"To do at session close" section (below), viewed from the execution-side
rather than the drafting-side. The drafting session's close-and-clear
produced them; the execution session checks they're present before
proceeding. If you're executing this plan and pre-requisites 2-3 are
not satisfied (no "Cold-context review" section below), abort and run
the cold-context reviews first.

## Goals (and non-goals)

**Goals:**

- Add the session-bracketing rhythm to `core/nla-foundations.md` Working
  Rhythms
- Document the four-section plan/handoff template (substance,
  procedural-edge, judgment defaults, confidence band) plus the two
  structural patterns from Letter #25 (warm-context next-steps section,
  paired specific+generic checkpoint questions)
- Add a small preventive note that the framework prefers "plan" framing
  over "runbook" framing for multi-step workflows
- Write an update-notes entry for downstream propagation
- Archive the three resolved feedback log entries
- Post follow-up comments on Issues #24 and #25 naming what landed

**Non-goals:**

- /close skill enhancement (separate /think session — accept-with-/think)
- Memory-mining beat (separate /think session — accept-with-/think)
- Editing other Working Rhythms beyond what's needed to integrate the
  new one (no current evidence other rhythms need restructuring)
- Domain-project propagation (handled separately by domain projects via
  `/update`)

## Substance — the steps

The content of items from Letters #24 and #25 is inlined in the steps
below. Letter references (e.g., "per Letter #24 item 1") are for
traceability and historical attribution, not execution prerequisites.
The letters are at Issues #24 and #25 (closed) if execution-time
judgment surfaces a question about *whether* these are the right items
rather than *how* to implement them.

### Step 1: Resolve the framing question

The session-bracketing rhythm has an open framing question that must be
resolved before drafting the prose. Four options:

**Option 0: Amend existing rhythms; no new rhythm.** The Design Flow,
Session Structure, or both gain inline notes or examples that name the
session-bracketing shape without granting it rhythm status. Rationale:
the existing rhythms may already cover this implicitly; what's missing
might be naming, not a new construct. Cost: the substeps (plan-while-hot
→ simulate-cold → cold-question-check → adjust → close-and-clear) lose
their own shape; they'd live as descriptions inside an existing rhythm
rather than as a rhythm in their own right.

**Option A: Extend The Design Flow.** Current rhythm reads "Think → plan
→ implement → debrief." Extend to "Think → plan → implement → debrief →
plan next session (if it produced future work)." Adds one step to the
existing rhythm; folds session-bracketing inside Design Flow as a single
beat.

**Option B: New standalone rhythm.** Add session-bracketing as the 8th
Working Rhythm, distinct from Design Flow. Letter #24's framing.

**Option C: Hybrid — short note in Design Flow + standalone rhythm.**
Design Flow's "debrief" gets a sentence: "if the session produced future
work for a later session, see The Session-Bracketing Discipline." The
detailed rhythm lives standalone.

**Author's lean:** Option C. Three reasons for C over A or B:

1. The substeps (plan-while-hot → simulate-cold → cold-question-check →
   adjust → close-and-clear) are substantial enough to warrant their own
   rhythm shape. Folding them into Design Flow as a single beat (Option
   A) loses the substeps.
2. The trigger condition (session created future work) is distinct from
   Design Flow's trigger (any task). Many Design Flow runs don't produce
   future work; bracketing doesn't apply to those.
3. The hybrid acknowledges that someone reading Design Flow benefits
   from knowing the bracketing rhythm exists. Pure Option B leaves them
   to discover it from the Working Rhythms list alone.

**On Option 0:** This is the genuine alternative to a new rhythm. The
case for it: the pattern may already be implicit in Session Structure
(startup → work → close) and could be elaborated there with an inline
section about session-end discipline when future work is produced. The
case against: the substeps' substantiality is real and warrants
visibility above the prose level. Fresh-context AI should evaluate
whether the existing rhythms genuinely cover this implicitly — if so,
Option 0 is right; if not, C or B.

**For execution-session AI:** confirm or revise this lean. If you (fresh
context) think Option 0 or Option A is right, argue it — the downstream
maintainer's initial framing was A; my warm-context lean may be
over-rotating to substep-preservation. Don't defer to my lean.

### Step 2: Draft the session-bracketing rhythm prose

In `core/nla-foundations.md`, add the new rhythm to Working Rhythms.

**Placement in list:** Author's lean is after "Session Structure" (which
describes startup/work/close) and before "Structural Change Discipline"
— grouping the two "discipline" rhythms together, with the session-shape
rhythm immediately preceding. Confirm at execution time.

**Naming:** Working name *The Session-Bracketing Discipline* (parallels
*Structural Change Discipline* in shape and naming). Open to revision.

**Content the rhythm must cover:**

- Cycle shape in arrow notation: `do-work → plan-while-hot →
  simulate-cold → cold-question-check → adjust → close-and-clear`
- One-line meaning for each substep (per Letter #24 item 1):
  - **Plan-while-hot** — capture future-session work while current-session
    context is still warm. The author has implicit assumptions, recently
    touched file shapes, and conversational decisions in working memory.
  - **Simulate-cold** — spawn a fresh-context *reviewer* agent (distinct
    from the eventual executor) to read the plan and report what they'd
    execute, where they'd improvise, what's ambiguous. Catches
    author-implicit execution gaps.
  - **Cold-question-check** — diagnostic questions about the plan's
    conceptual frame, asked by a fresh-context reviewer (same or
    different agent from the simulator). Catches concept-layer
    conflations the simulation can't catch (because the simulating agent
    inherits the conceptual frame from the plan).
  - **Adjust** — apply clear-improvement patches to the plan based on
    reviewer findings, with verify-each-claim discipline. Reviewer output
    is candidates, not authority — per The Inquiry Flow. (Distinguish:
    the cold-context *executor* who eventually runs the plan in a future
    session is a different role from the cold-context *reviewers*; their
    work happens after close-and-clear, not as part of it.)
  - **Close-and-clear** — finalize session log, mark plan ready, commit,
    end session.
- The two cold-context check mechanisms catch different gap-classes
  (item 2): simulation catches what an executor would stumble on;
  question catches what an executor wouldn't notice was wrong because the
  conflation is internally consistent.
- "Someone drives the bracketing" note (item 8): the default is human as
  session-manager; AI surfaces options ("is this the right moment for
  X?"), executes decisions, and captures context for handoff. AI-led
  bracketing isn't precluded — it may be appropriate in long-running
  autonomous contexts — but it's a genuine open design question, not a
  settled framework stance. The default holds in absence of explicit
  choice; AI-led mode warrants explicit signaling when invoked.
- When the rhythm fires: when a session has produced (or is about to
  produce) a non-trivial plan for future-session execution AND there's
  enough author-context worth capturing in the plan. Doesn't fire for
  quick fixes, single-step tasks, conversation-only sessions, or trivial
  follow-ups.
- Plans-not-runbooks preventive note (item 4 of letter): the rhythm
  produces *plans*, not *runbooks*. Plans invite collaboration at decision
  points; runbooks prime script-execution mode. The cardinal rule
  (foundations principle #6) depends on the framing carrying its semantic
  weight.
- Cross-reference to The Inquiry Flow (the simulation and question
  substeps are Inquiry Flow applications — asking the AI about its
  experience with the plan, treating the answer as hypothesis, verifying).
- Cross-reference to The Validation Flow (cold-context experiment is the
  empirical endpoint for hypotheses the rhythm generates).

**Style consistency:** match the existing seven rhythms' length and shape
— most are 5-9 sentences in 1-2 paragraphs. This rhythm may run slightly
longer because of the substeps; aim for two paragraphs total. If it pushes
to three, that's acceptable.

### Step 3: Document the handoff template

(Naming clarification: the template is specifically for *handoffs* —
plan-shaped artifacts that cross an agent boundary, typically from a
drafting session's warm context to a future session's cold context.
Plans that don't cross such a boundary — e.g., a continuation plan
where the same author resumes — may carry only a subset of the six
elements. The four-section structure is handoff scaffolding answering
"what does the cold executor need from the warm drafter?"; the
warm-context next-steps section is plan-shape that fits either case.
Precise naming in the template doc itself should distinguish.)

Three location options:

**Option A: Standalone doc** at `core/plan-handoff-template.md`. Needs
structure record update (`core/structure.md`). New file in core/ means
consumer-facing → high blast radius but clear separation.

**Option B: Section inside `core/skills/close.md`** under a "When the
session produced future work" subsection. No structure record change.
Less discoverable from the rhythm's perspective; but `/close` is the
natural locus when the template gets used.

**Option C: Subsection inside the new rhythm** in
`core/nla-foundations.md`. Denser. Avoids cross-file reference. Trade-off:
foundations.md grows; rhythm becomes 4-5 paragraphs instead of 2.

**Author's lean:** Option A (standalone). Reason: the template is
referenced from multiple places (the rhythm itself, /close eventually,
possibly /maintain). A standalone doc avoids duplication and gives it room
to grow as patterns accumulate. The structure record update is a small
cost.

**Template content (per Letter #24 item 3 + Letter #25 items 1, 2, +
Letter #24 item 5):**

- **Title + Intent** (item 5 — intent at every layer). What the plan does
  and why it matters.
- **Substance section** — what to do. Steps, decisions, references. The
  bulk of the document.
- **Procedural-edge cases section** — what to do when source deviates
  from the plan. Items the warm drafter wouldn't anticipate because they
  weren't executing.
- **Judgment defaults section** — where to lean when rule space is open.
  Items where the right answer depends on context the cold executor
  doesn't have; the warm drafter pre-decides them.
- **Confidence band section** — where the cold executor should expect to
  push back at the next collaborative step. Where the drafter is
  uncertain; what would change the answer.
- **Warm-context next-steps section** (Letter #25 item 1) — near the
  phase-close beat, explicit section asking "what other work benefits
  from the warm context this session produced?" Three sub-parts:
  - Specific candidates (next-phase plans, spec/standards drafts,
    friction log entries, memory updates)
  - Generic open-question ("anything else?")
  - Calibration (lean: capture-shaped work warm; defer execution-shaped
    to fresh session)
- **Block-end checkpoints** (Letter #25 item 2) — at each major block's
  end, pair specific questions (tied to that block's decisions) with at
  least one generic open-question (for unstructured surfacing).

The template doesn't enforce. It scaffolds the drafter's thinking.
Sections can be dropped when the work doesn't warrant them — a small
plan doesn't need a confidence band; a fully mechanical plan doesn't
need judgment defaults. The intent is to make the drafter ask each
question from warm context (cheap) what the cold executor would
otherwise improvise (lossy).

### Step 4: Verify the plans-not-runbooks preventive note landed

This step is a verification beat, not a separate addition. The preventive
note's content was included in Step 2's content list and should have been
incorporated when the rhythm prose was drafted. Verify the drafted prose
includes a sentence (or equivalent) naming that the rhythm produces
plans, not runbooks — runbooks structurally suppress human input
(primes script-execution mode); the cardinal rule depends on the framing
carrying its semantic weight.

Audit finding from triage (2026-05-18): no "runbook" framing exists in
framework skills already. So the note is preventive, not corrective.

### Step 5: Add update-notes entry

For consumers (downstream NLAs). `install/update-notes.md`, newest first.

Should cover:

- New Working Rhythm — session-bracketing — and what it operationalizes
- Pointer to the plan/handoff template (wherever it landed in Step 3)
- Preventive note: framework prefers "plan" framing for multi-step work
- Practical effect on consumer NLAs: AIs in domain sessions will more
  often suggest drafting a plan when a session produced future work, and
  the plan's expected shape is the four-section template plus the two
  structural patterns.

Cross-reference (not duplicate) the 2026-05-14 update-notes entry on
Inquiry Flow — the session-bracketing rhythm uses Inquiry Flow during its
cold-context check substeps.

### Step 6: Archive the three resolved feedback log entries

Move from `reference/feedback-log.md` to
`reference/feedback-log-archive.md` with `**Resolved:**` lines describing
what landed.

### Step 7: Post follow-up comments on Issues #24 and #25

Tell submitters what landed. Two comments — one each on the issues.
Reference the foundations changes, the template doc location, and the
update-notes entry.

### Step 8: Commit + tag (if pushing) + push

Consumer-facing commit (touches `core/`, `install/`). Per shippability
rule, tag attaches at push. Bump `VERSION` before tagging.

Single commit if all three items land cleanly together. Two commits if
the template doc is substantial enough to merit its own commit (judgment
call at execution time).

## Block-end checkpoints

### After Step 1 (framing resolved)

- **Specific:** Did the framing land as Option A, B, or C? If B or C, is
  the placement-in-list decision made (where in Working Rhythms)?
- **Generic:** Anything else surfaced during framing that should land in
  the plan before continuing — naming, cross-references, or scope
  adjustment?

### After Step 2 (rhythm drafted)

- **Specific:** Does the rhythm prose cover all the content elements
  listed (cycle shape, substep meanings, two cold-context check
  mechanisms, "someone drives" note, when-it-fires, plans-not-runbooks
  note, cross-references)? Does it match the style of the existing seven
  rhythms?
- **Generic:** Anything about the rhythm's shape that needs flagging —
  overlap with existing rhythms, internal contradictions, ambiguity for
  cold readers?

### After Step 3 (template documented)

- **Specific:** Does the template cover all six elements (four sections
  + two structural patterns + intent layer)? Is the template-doc
  location decided and consistent with Step 1's framing?
- **Generic:** Anything about the template's shape that needs flagging —
  overlap with /close's existing content, internal contradictions,
  ambiguity that would confuse cold readers?

### After Step 5 (update-notes drafted)

- **Specific:** Does the update-notes entry name what consumers need to
  do (typically nothing — foundations changes propagate at submodule
  advance)? Does it cross-reference rather than duplicate the 2026-05-14
  entry?
- **Generic:** Anything else worth telling consumers — connections to
  prior update-notes, optional adoption steps, things they might want to
  add to their own session-end disciplines?

### After Step 8 (committed and pushed)

- **Specific:** Tag attached? VERSION bumped? Push successful? Issues #24
  and #25 follow-up comments posted?
- **Generic:** Anything about the commit shape, message, or tag scope
  that should be improved next time?

## Procedural edge-cases

### What if the framing question can't be resolved cleanly?

Default to Option C (hybrid). The hybrid preserves the standalone rhythm
(which has the substep detail) and the Design Flow integration (which
lets readers of Design Flow discover bracketing). Both downsides are
small; Option C absorbs them.

If even Option C feels wrong, abort and trigger a /think session before
continuing. The framing question is design judgment, not execution.

### What if the rhythm prose grows beyond 2 paragraphs?

Three is acceptable. Four means the rhythm is carrying template-level
content that should move to the standalone template doc instead.

### What if the template-doc location decision diverges from the rhythm placement?

Template can live in `core/` even if the rhythm is in
`core/nla-foundations.md`. They reference each other; they don't need to
be co-located.

### What if other Working Rhythms need editing to integrate cleanly?

Expected: Design Flow gets a one-sentence reference (Option C). Session
Structure may benefit from a similar reference. Don't restructure the
other rhythms beyond cross-references unless integration testing surfaces
a real conflict.

### What if the update-notes entry overlaps with the 2026-05-14 entry on Inquiry Flow?

Cross-reference rather than duplicate. The 2026-05-14 entry established
The Inquiry Flow as a foundation; this entry adds the workflow rhythm
that operationalizes plan-shaped work, which uses Inquiry Flow during
its cold-context check substeps.

### What if `core/structure.md` needs updating beyond the template-doc entry?

If Option A (standalone template doc): add a `core/plan-handoff-template.md`
entry. If Option B or C: probably no structure record change needed
(template lives inside existing files). Confirm at execution.

### What if mid-implementation the maintainer wants to add /close enhancement work?

Defer to the /think session that was triaged for that work. The /close
enhancement touches the most-frequently-run framework skill and shouldn't
be folded into this scope opportunistically — that's exactly the kind of
unbounded scope creep the four-section template's confidence band is
meant to surface.

### What if `gh` CLI auth fails when posting Issue #24/#25 comments?

Note it and continue. The feedback-log archival and the foundations
changes are the important artifacts. The follow-up comments can be
posted later or by the maintainer manually.

## Judgment defaults

### Rhythm vs. Design Flow extension

Lean: Option C (hybrid). If unclear at execution time, default to C.
Reverting from C to A or B is cheaper than reverting from A or B to C.

### Template doc location

Lean: standalone doc at `core/plan-handoff-template.md`. If the structure
record update or new-file overhead feels heavy in the execution moment,
fall back to Option C (inside the rhythm).

### Plans-not-runbooks placement

Lean: inline sentence in the rhythm. Small, contextual.

### Placement in Working Rhythms list

Lean: after Session Structure, before Structural Change Discipline.

### Update-notes verbosity

Lean: moderate. Include a "what this means for your project" section
(matches the 2026-05-14 entry's pattern). Foundations changes don't
require project-side action but the new rhythm changes how AIs in domain
sessions handle session-end work.

### When to trigger /think instead of proceeding

If during drafting any of the following surfaces:

- The rhythm prose pulls in concepts not yet defined in foundations
- The template structure feels like it conflicts with `/close`'s existing
  shape (Validate → Check Documentation Mirrors → Debrief → Finalize
  Session Log → Commit/Tag/Push)
- The framing question keeps shifting under iteration
- Two or more of the substeps' meanings feel underspecified for cold
  readers
- A real conflict surfaces between this rhythm and an existing rhythm

### Commit shape

Lean: one commit covering all three items + update-notes + structure
record update (if any) + feedback log archival + session log. Two commits
if the template doc is substantial enough to merit isolation (200+ lines).

### Tag and version

Consumer-facing → tag at push, bump VERSION. Tag scope covers any unpushed
commits since the last tag.

## Confidence band

Where the cold executor should expect to push back at the next
collaborative step.

### Framing question (Option A / B / C)

I'm 60% on Option C. The case for B (pure standalone) is strong — Letter
#24's recommendation F frames it that way. The case for A (Design Flow
extension) is also defensible — the downstream maintainer's initial
framing. Don't treat my lean as authoritative; the framing is genuinely
open and benefits from fresh eyes.

### Template location

I'm 55% on standalone doc. Templates inside skills also work (the
existing `skills-doctrine-publication.md` plan demonstrates how a
substantial doc can live elsewhere). Either Option A or Option C is
defensible.

### Three-item bundling

I'm 75% the three-item bundle is right size for one session. Could be
split (rhythm + preventive note in one session; template separately) if
the session feels long. The preventive note is small enough that it
should always ride along with the rhythm.

### Placement in Working Rhythms list

I'm 50% on "after Session Structure, before Structural Change
Discipline." Other reasonable placements: at the end (after Validation
Flow, as the capstone) or right after Design Flow (since it extends
thinking-about-future-work). Fresh eyes should see the right placement
faster than I can in warm context.

### Rhythm name

I'm 45% on "The Session-Bracketing Discipline." It parallels Structural
Change Discipline, which is helpful — but it's also long. Alternatives:
"The Bracketing Rhythm," "Session-Bracketing," "The Handoff Rhythm"
(though Handoff is also the template's name). Worth a fresh read.

### What the cold-context simulation will catch

I'm 40% the simulation will catch the framing question's full weight.
The framing question is conceptual rather than executional, so it may be
more of a cold-context-question target than a cold-context-simulation
target. If both substeps are available at execution time, run both.

### Whether the rhythm needs an inline example

I'm 50% on adding a one-sentence example after the substeps (e.g., "This
session bracketing produced [plan.md] in [location]"). Examples ground
rhythms; they also lengthen them. Letter #25's Item 5 argues for intent
at every layer — examples may be intent-shaped scaffolding. Leave to
execution-time judgment.

## Warm-context next-steps

Per Letter #25 item 1, before closing this session, ask: what other work
benefits from the warm context this session produced?

### Specific candidates

- **None on principle #2 / Inquiry Flow work.** Complete and committed
  (commits a57d225 + 9461931 from this session).
- **None on /close enhancement.** Waiting on /think. No warm context to
  capture beyond what's already in the feedback log entry.
- **None on memory-mining beat.** Same.
- **Plan for the session-bracketing rhythm + template work** — this
  document.
- **Update `install/structure-intent.md` to mention accreted `reference/`
  subdirectories** — flagged in `core/structure.md` lines 161-163 as
  deferred to a publication plan. Adjacent to but distinct from this
  plan; not in scope.

### Generic open-question

Anything else that benefits from warm context this session's work didn't
capture? The session covered:

- Principle #2 recalibration (design + implementation)
- The Inquiry Flow rhythm (design + implementation)
- Three workstreams of feedback triage (eight items + six recommendations
  across two letters)
- The Inquiry Flow agent-self-report anchor refinement
- This plan

Nothing else surfaces. The session is at a natural end.

### Calibration

Lean: do plan-shaped and capture-shaped work warm; defer execution-shaped
work to fresh session. This plan honors that — capturing the
rhythm + template work for fresh execution rather than rushing it in
heavily loaded context.

---

## To do at session close

1. **Cold-context simulation review** of this plan — spawn fresh-context
   agent, prompt: "Read this plan and report what you'd execute, where
   you'd improvise, what's ambiguous." Findings get appended below as
   "Cold-context review: simulation findings."
2. **Cold-context question review** — same fresh-context agent (or
   separate), prompt: diagnostic questions about the plan's conceptual
   frame, particularly the framing question in Step 1. Findings appended
   as "Cold-context review: question findings."
3. **Maintainer triage** of cold-context findings — apply
   clear-improvement patches with verify-each-claim discipline. Cold
   output is candidates, not authority.
4. **Mark plan ready** for execution — update Status field at the top.

---

## Cold-context review

Run 2026-05-19 by two parallel fresh-context agents (`general-purpose`
subagent type), one for simulation (executability), one for question
(conceptual frame). Methodology per Letter #24 item 2 — different
mechanisms catch different gap-classes.

### Simulation findings (executability)

Self-containment positive — the agent did not need to open referenced
files to evaluate executability. Findings clustered around:

- **Improvisation decisions** normal at execution time: style anchoring
  against existing rhythms, rhythm naming alternatives, template
  granularity, update-notes verbosity, commit shape.
- **Ambiguities** worth resolving: Pre-req #3 reading twice with To-do
  #1-2; Step 4 redundancy with Step 2's content list; "plan ready"
  marker semantics; Step 6 archival format; Step 1 framing-question
  current-state confusion (A vs. C).

### Question findings (conceptual frame)

External context required at the rationale level (not for execution).
Findings:

- **Conflations:** Plan vs. Handoff treated as one artifact; "cold-context"
  used for two distinct roles (review-mechanism vs. executor);
  "plan-shaped" vs. "plan-shaped-with-handoff-scaffolding" not separated.
- **Pre-judged framings:** Existence of a new rhythm pre-judged (Option
  0 — amend existing — wasn't surfaced); six template elements
  pre-judged as the right set; "someone drives" defaulting to human
  rather than acknowledged as open.
- **Unsupported leans:** Standalone template doc rationale relies on
  speculative future referents; placement justification mildly circular
  (the "two discipline rhythms" grouping rests on the new rhythm's
  working name including "Discipline," which was the author's choice);
  rhythm length capped at 2 paragraphs without engaging that the content
  list is materially longer than peers'.
- **Implicit context dependencies:** Letter content referenced by
  number; cardinal rule, verify-each-claim, shippability rule referenced
  without inline quote. (Note: simulation agent reported letter content
  *is* sufficiently inlined for execution; question agent flagged it for
  rationale-level engagement.)

### Patches applied (2026-05-19)

Per The Inquiry Flow's Adjust step: clear-improvement patches with
verify-each-claim discipline. Reviewer output was treated as candidates,
not authority — each finding verified against the plan before patching.

- **A. Plan vs. Handoff distinction** — Step 3 retitled "Document the
  handoff template" with a naming clarification: the template is
  specifically for handoffs (cross-agent transfer); plans that don't
  cross such a boundary may carry a subset.
- **B. "Cold-context" role disambiguation** — Step 2's substeps now
  distinguish review-mechanism reviewer (pre-execution diagnostic) from
  executor (post-handoff implementer). Adjust's "candidates, not
  authority" rule applies to reviewer output.
- **C. Option 0 added to Step 1** — amend existing rhythms (no new
  rhythm) as a real option, with explicit author's-lean engagement.
- **D. Letter content inlining clarified** — note at top of Substance
  section that letter references are for traceability, not execution
  prerequisites.
- **E. Pre-req / To-do reconciliation** — explicit note that
  pre-requisites 2-3 describe the drafting session's close-and-clear
  output, viewed from the execution side.
- **F. Step 4 clarification** — retitled and reframed as an explicit
  verification beat; the note content itself was already included in
  Step 2's content list.
- **H. "Someone drives" framing** — acknowledged AI-led bracketing as a
  genuine open question, not a settled default.

### Patches not applied (low-value relative to plan length)

- **I (template-doc rationale honesty)** — already acknowledged in
  Confidence band at 55%; no additional surfacing warranted.
- **J (length acknowledgment)** — covered by the "What if the rhythm
  prose grows beyond 2 paragraphs" edge case.
- **G (status field semantics)** — answerable at execution time.
- **K (shippability rule pointer)** — pointer exists in
  `core/skills/maintain.md` "Shippability at Commit Time"; cold executor
  finds it via the maintain skill discipline.
- **Placement-circularity finding** — true but small; acknowledged
  here so the execution-time AI can weigh placement freshly.
- **Six template elements as the right set** — this is a question the
  template doc itself should engage when it's drafted (Step 3); the
  plan doesn't need to pre-resolve it.

### Status

Plan is ready for execution. Status field updated.
