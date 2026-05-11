# Framework Friction Log Archive

Resolved and closed friction log entries, moved here from `friction-log.md` during `/maintain` sessions. This keeps the active friction log lean while preserving history for pattern analysis.

**How entries get here:** When `/maintain` resolves a friction log entry, it moves the complete entry (including the `**Resolved:**` line) from the active log to this archive.

**Searching:** Use grep to search this archive when looking for historical patterns. The `/friction-log` skill searches here automatically before creating new entries.

---

## Entries

*Archived entries in reverse chronological order.*

### 2026-05-11 — /create-app's structured Q&A misses the collaborative-refinement mode

**Type:** core
**Severity:** minor
**Blast radius:** all projects (project generation)
**Status:** resolved
**Resolved:** 2026-05-11 — Added a "Between Phase A and Phase B: Recognize the mode" transition section to `.claude/skills/create-app/SKILL.md` that distinguishes extraction from collaborative refinement and names four signals for the latter (working prompt or sample artifact, length about *why*, explicit invitation of AI perspective, user-named-but-unresolved tensions). Added a "User arrives with rich conceptual work" entry to Conversation Edge Cases as a sibling to "User provides everything upfront." Skill-level placement only — `/create-app` lives only at `.claude/skills/create-app/SKILL.md` (framework-owned, no `core/skills/` analog and no consumer-ship surface). The parallel awareness-level work (prose-default principle) was handled by the 2026-05-10 entry rather than by adding a separate mode-recognition principle to `install/CLAUDE-intent.md` — collaborative refinement *is* prose by definition, so the broader prose-default principle covers the mode-recognition behavior at the awareness level; this entry's skill-specific work covers the trigger level.

**Observation:**
During /create-app for nla-archetypes (2026-05-10), the most consequential design
decision in the generated project did not emerge from any structured Phase A/B
question. The decision was the third value — "true like fiction, not like a
transcript," the Guernica anchor that resolves the productive tension with
the grounding value. It emerged because the user explicitly invited
collaboration twice:

1. At the project description (Phase A response): "I'm also interested in
   your thoughts, ideas, concerns or questions."
2. Mid-design, after I proposed two values: "Another candidate: true to life
   as in the way good fiction feels true... I'm not sure how to express that
   as a value exactly. Maybe you can help?"

The Phase B grouping suggestions ("voice + audience," "values/tradeoffs as a
single lightweight question," etc.) frame the AI's job as *extracting* domain
requirements via structured Q&A. That framing fits a user providing
requirements from scratch. It underperforms when the user arrives with rich
conceptual work — a working prompt, a developed framing, half-formed
intuitions — and the AI's job is *translation into NLA structure* rather
than extraction.

In the translation case, the high-value mode is collaborative refinement:
the AI proposes shape, names the gaps, asks for pushback, helps articulate
what the user can feel but hasn't named. That's what happened on the
Guernica value. It wouldn't have happened if I'd followed Phase B
mechanically through its question groupings.

**Confirmed reason:**
Phase A is genuinely open-ended ("What are you building? Accept anything from
a one-liner to a full paragraph.") and accepted the user's rich prompt
cleanly. But Phase B's structure assumes the next move is to fill remaining
fields via targeted Q&A, not to enter a collaborative-refinement mode. The
existing "user provides everything upfront → skip to Phase C" edge case
covers the *requirements-already-given* case, but not the
*conceptual-work-rich-but-design-choices-unresolved* case. In that
intermediate state, neither Q&A nor skip-to-summary is right; collaborative
refinement is.

**Affected files:**
- `core/skills/create-app.md` — Phase A → Phase B transition; the
  Conversation Edge Cases section ("User provides everything upfront") could
  grow a sibling entry for "User arrives with rich conceptual work."
- Possibly `install/CLAUDE-intent.md` or `core/nla-foundations.md` — the
  collaborative-vs-extractive mode-recognition is a general AI posture that
  applies beyond create-app. /maintain has analogous moments
  (refining-a-doc vs. extracting-new-doc-requirements).

**Proposed fix:**
Two complementary moves:

1. In `core/skills/create-app.md`, after Phase A and before Phase B, add a
   mode-recognition step:

   > Before targeted follow-ups, recognize what mode the user is inviting.
   > If their Phase A response is mostly *requirements* (what tasks, what
   > audience, what voice), proceed to Phase B as written — extraction is
   > the right mode. If their response carries rich conceptual work
   > (a working prompt, a developed framing, half-formed intuitions) and
   > invites your perspective explicitly or implicitly, shift to
   > collaborative refinement: propose shape, name gaps, invite pushback,
   > help articulate what the user can feel but hasn't named. Phase B's
   > structured questions still apply for genuinely missing fields, but
   > the conversation should lead with refinement, not extraction.

2. Add a Conversation Edge Cases entry — "User arrives with rich conceptual
   work" — describing the pattern and pointing to the mode-recognition
   guidance.

**Notes:**
- Related to archived entry 2026-02-21 "Reflection after execution produces
  high-quality feedback" (resolved by creating /debrief). Same shape — open
  invitation to reflection/collaboration produces high-value output that
  structured Q&A doesn't — but at a different moment. That entry was about
  reflection *after* execution; this one is about collaboration *during*
  design. /debrief carved out the post-execution slot; this would carve out
  the mid-design slot inside /create-app.
- Distinct from the 2026-05-10 AskUserQuestion entry — that's about
  tool-choice (enum vs. prose) at any conversational moment. This is about
  whole-mode-recognition: when to enter collaborative refinement vs.
  structured extraction. Both pull in the same direction but address
  different layers of the problem.
- The framework addenda apply: this is a `core/skills/` change with reach
  to every domain project's generation, since /create-app is the entry
  point for every new NLA.
- Possible test of the fix: re-read the nla-archetypes transcript and
  check whether the mode-recognition step would have fired correctly on
  the Phase A response (a working extraction prompt + explicit invitation
  to AI thoughts). Should be a clean yes.

---

### 2026-05-10 — AskUserQuestion overreach despite user-private memory note

**Type:** core
**Severity:** minor
**Blast radius:** all projects
**Status:** resolved
**Resolved:** 2026-05-11 — Added a "Default to prose for design conversations" bullet to both `install/CLAUDE-intent.md` Execution Principles (consumer-facing — propagates to every NLA's CLAUDE.md via `/create-app` and `/update`) and the framework's own `CLAUDE.md` Grounding Principles (covers `/create-app`, `/maintain`, `/think`, and other conversation-heavy skills run from the framework). Update-notes entry added under `install/update-notes.md`. The two placements use the same operational language; the framework version adds one closing sentence connecting the principle to `core/nla-foundations.md` principle #2 ("the LLM bridges human flexibility and computational rigidity") — naming the foundational truth that makes enum-for-design-questions a category error, not a personal preference. Skill-level reinforcement in `core/skills/maintain.md` and `core/skills/think.md` was deliberately deferred: if recurrence shows up despite the awareness-level placements, trigger-level reminders can be added then. Pre-emptive layering wasn't warranted; awareness-level placement loads into every session's prompt via CLAUDE.md, which is the structural change the friction entry argued was needed (memory-only mitigation had been insufficient).

**Observation:**
During `/create-app` for nla-archetypes (this session), I invoked Claude Code's
`AskUserQuestion` tool twice for design questions that were "yes-but"/"yes-and"
shaped — questions where the user's likely response was a layered refinement
("yes, but with this addition"), not a discrete pick among mutually exclusive
options. Both invocations were rejected by the user, who reminded me that
prose would be the right format. The user flagged the pattern explicitly:
"You're an AI not a python interpreter so you can (and should) handle more
nuance than can be given by an enum."

Specifically:
- First invocation: three questions (output voice, source format, output
  destination) — each was "could be either" or "depends" shaped.
- Second invocation: similar three-question pattern after the user had
  already clarified the Guernica value and AI-optimized voice direction.

I had a memory note (`feedback_prose_over_enum_for_decisions.md`) from prior
sessions saying exactly this pattern was wrong. The note did not prevent
the lapse — the structured affordance of AskUserQuestion appears strong
enough that user-private memory isn't sufficient mitigation.

**Confirmed reason:**
[Per user] AskUserQuestion fits genuinely discrete clarifications but is
wrong for "yes, but"/"yes, and" shaped decisions. When a question is
layered (refinement, addition, partial agreement), prose lets the user
respond in the shape of the actual decision; enum forces them into a
shape that pre-judges it. Memory notes alone don't prevent the lapse —
the tool's affordance is attractive, and the memory note isn't loaded
into the system prompt the way framework CLAUDE.md or core skill
guidance would be.

**Affected files:**
- `install/CLAUDE-intent.md` — could add framework-level guidance about
  defaulting to prose for design questions; this propagates to every NLA's
  CLAUDE.md via /create-app and /update.
- `core/skills/create-app.md` — Phase B and Phase C currently assume prose
  conversation but don't say so explicitly enough to overcome
  AskUserQuestion's pull. Adding an explicit "default to prose for
  follow-ups; AskUserQuestion only for genuinely discrete clarifications"
  in those sections would fire at the lapse-prone moment.
- Possibly `core/skills/maintain.md`, `core/skills/think.md` — anywhere a
  skill invites multi-turn design conversation could carry the same default.

**Proposed fix:**
Add framework-level guidance, probably in `install/CLAUDE-intent.md`
("Execution Principles" or similar), along these lines:

> When asking the user a follow-up question, default to prose. Tools that
> force enum-style choices (Claude Code's `AskUserQuestion`, similar
> affordances) are appropriate only for genuinely discrete clarifications
> with mutually exclusive answers — never for layered design decisions
> where the user's likely answer is "yes, but" or "yes, and."

Complementary: `core/skills/create-app.md` (and conversation-heavy skills
generally) could state the default explicitly in their Conversation Flow
sections — the lapse-prone moments are where the guidance needs to fire.

**Notes:**
- Related-but-distinct from archived entry 2026-02-21 "Plan mode kept
  pushing toward decisions (AskUserQuestion with multiple choice options),"
  resolved by creating `/think`. That entry addressed plan-mode/design-
  exploration specifically. This one is broader: AskUserQuestion overreach
  across general conversational skills, not just plan mode. The /think
  refuge alone doesn't address the default-tool-choice problem in skills
  like /create-app and /maintain.
- The lapse happened despite the user's existing memory note — evidence
  that memory-only mitigation is insufficient for tool-default behaviors.
  This argues for moving the guidance into framework docs that every
  session loads.
- Affects all projects because the AskUserQuestion pull is a property of
  Claude Code itself, present in every NLA's runtime. Per the framework
  addenda: this is a `core/` (and `install/`) change with all-domain-
  project reach.
- This also relates to the active "Patterns to Watch" item #4 — language
  breadth, when defaults assume one shape (here: enum-shaped questions)
  when the situation needs another.

---

### 2026-04-18 — Shippability convention reads as per-commit tagging; session-end is better

**Type:** process
**Severity:** minor
**Blast radius:** all projects
**Status:** resolved
**Resolved:** 2026-05-08 — Refined the Shippability section in `core/skills/maintain.md` to separate *what counts as consumer-facing* (the classification, unchanged) from *when the tag goes on* (push moment, typically session end). `core/skills/close.md` was restructured at the same time and now operates the rule: step 5 reviews commits since the last tag and tags HEAD before pushing if any touched consumer-facing content. A session shipping three consumer-facing commits gets one tag. The `reference/design-rationale.md` Shippability entry carries the refinement record. `install/package-intent.md` was not touched in this pass — the package-specific pointer remains aligned with the framework rule because it inherits maintain.md's Shippability section conceptually rather than restating it.

**Observation:**
During the 2026-04-18 writing-standards session, I tagged the first
consumer-facing commit (the `/maintain` broadening work) as v0.0.5 mid-session,
with more consumer-facing work planned for the same session. The user pushed
back: jumping 0.0.4 → 0.0.5 → 0.0.6 → 0.0.7 in a single session inflates
version numbers without making each tag more meaningful. Downstream consumers
would rather see "v0.0.5 = one session of writing-standards-related work"
than three incrementally-numbered tags of the same arc of work.

The `core/skills/maintain.md` Shippability section as currently written —
"If yes → tag the commit (if the project uses tagged releases)" — reads as
per-commit tagging. The operative rule works correctly (consumer-facing
content gets tagged); the *timing* doesn't distinguish "tag each commit" from
"tag a meaningful release." Per-commit tagging was the literal
interpretation; session-end (or "explicit release moment") tagging is what
the downstream consumer actually benefits from.

**Confirmed reason:**
User's framing: "It just seems weird to potentially jump up from 0.0.4 to
0.0.7 in this session alone (if we go to 0.0.6 after pass 1 and 0.0.7 after
pass 2)." The version number should track meaningful release cadence, not
commit cadence. A session is a natural unit: one arc of work, one set of
changes a consumer should review together, one tag.

Related: the 2026-04-17 session's debrief already carried a gentle tension
about tagging choice ("reassess after a few more sessions if the pattern
recurs"). This is the recurrence.

**Affected files:**
- `core/skills/maintain.md` (Shippability at Commit Time section)
- `install/package-intent.md` (package-specific pointer, per 2026-04-17 session)

**Proposed fix:**
Refine the Shippability guidance to separate the *what-to-include-in-tag*
question (consumer-facing content) from the *when-to-tag* question. Rough
direction:
- The commit-time decision stays: "does this commit touch consumer-facing
  content?" determines whether the work belongs in the next release.
- The tagging-time decision is separate: tag at meaningful release moments
  (typically session end, or when a consumer-facing arc of work is
  complete), not per-commit. Update-notes entries can still land per-commit
  — they're a running changelog, not a release marker.
- Update-notes per consumer-facing commit still makes sense (changelog
  granularity); it's the tag that should be release-grained.

Scope for a future `/maintain` to work through — this friction log entry
captures the observation; convention refinement happens when processed.

**Notes:**
- Mid-session local v0.0.5 tag was deleted (it wasn't pushed). The
  2026-04-18 session will tag at end, once, for all its consumer-facing
  work.
- Worth checking how the per-commit vs. release-moment distinction interacts
  with `/update`'s tag-check behavior (install.md "Pin to a Tagged Release"
  and update.md's fast-forward tag offer) — the tag-check pattern assumes
  tags mark stable release points. Batched session-end tagging matches that
  assumption better than per-commit tagging does.

---

### 2026-05-06 — Framework lacks documented experimentation methodology

**Type:** core
**Severity:** minor
**Blast radius:** all projects
**Status:** resolved
**Resolved:** 2026-05-08 — Validation flow added as a sixth working rhythm in `core/nla-foundations.md`, with the "consider whether experiments fit this work" caveat per intent-over-rules framing. Methodology vocabulary lists in the rhythm (bench discovery, two-pass cold-context review, synthetic vocabulary, citation as safety net, pressure-resistance probes) name the patterns; full detail lives in the per-experiment reports under `reference/experiments/`. Entry's MVP scope (#1: validation flow as a rhythm) implemented. Open future work: a more detailed standalone cold-context review documentation (#2) and skill-level affordances for facilitating experiments (#3) — the entry explicitly authorized incremental resolution. Threshold for adding the rhythm was crossed when five experiments across three NLAs (framework's two + facebook-moderation's three: implementation-standards, ingest-compile-compare, identity-standards-transmission) demonstrated the methodology generalizes across domains.

**Observation:**
The NLA Framework documents four working rhythms in
`core/nla-foundations.md`: the improvement loop, the design flow, the
update cycle, and session structure. None of these cover empirical
validation of prose-as-code claims between hypothesis and commit.

This session's prose experiments
(`reference/experiments/skill-invocation-discipline/experiment-report.md`)
ran ad-hoc. They worked. But the methodology isn't documented and
isn't discoverable for future work. The next time someone considers
a doctrine change, convention shift, or any prose-as-code change with
downstream impact, they'd have to either (a) reinvent the methodology,
(b) find this experiment report and copy the pattern, or (c) skip the
empirical step and rely on reasoning alone.

**Before:** Prose-as-code changes go directly from /think to plan to
commit. Empirical validation between hypothesis and commit is ad-hoc
when it happens at all. Cold-context review (the related but distinct
practice of reviewing artifacts before commit) is similarly undocumented.

**After:** A documented "validation flow" — possibly as a fifth working
rhythm — describes when and how to test prose-as-code claims
empirically. Cold-context review (two-pass: simulation + frame question)
is similarly documented. Both compose with existing rhythms (improvement
loop, design flow) without replacing them.

**Confirmed reason:**
The framework's current rhythms reflect what was true when they were
documented. The prose-experiment pattern is newer (this session is
where it surfaced as a generalizable pattern, though Issue #24 from
facebook-moderation introduced related methodology). The framework
hasn't yet absorbed it.

**Affected files (proposed):**
- `core/nla-foundations.md` Working Rhythms section
- Potentially a new core skill (e.g., `core/skills/run-experiment.md`)
  or fold guidance into existing skills (`/think`, `/maintain`)
- `reference/design-rationale.md` for the rationale entry

**Proposed fix:**
Sized appropriately, probably a /think session followed by maintain
work in a separate session. Specific shape to explore:

1. **Validation flow** as a fifth working rhythm in foundations.
   Tentative wording: "Hypothesize → design experiment → test in cold
   context → measure → iterate or commit. Used when prose changes
   have downstream impact and reasoning alone is uncertain."

2. **Cold-context review pattern** documented separately. Two-pass
   distinction (simulation + frame question) is load-bearing per
   Section 4.2 of the experiment report.

3. **Skill or sub-skill** for facilitating experiments? Could be
   `/run-experiment`, or could be folded into `/think` as a phase. The
   shape depends on how often the pattern fires; this is the design
   judgment to settle in /think.

Don't decide all three at once. The minimum viable change is documenting
the patterns (in foundations + design rationale) so future maintainers
can find them. Skill-level affordances are optional add-ons.

**Notes:**
- This is the meta-version of the previous entry. The previous entry
  documents that the experiments paid off; this entry asks whether to
  elevate the methodology to framework-level guidance.
- Related to Issue #24 (recommendations B and F about handoff template
  and session-bracketing rhythm); consider triaging together.
- Worth checking facebook-moderation's `reference/experiments/` pattern
  for prior art on directory structure and report format. Our first
  experiment report (`reference/experiments/skill-invocation-discipline/`)
  borrows that pattern.
- Tag for cross-reference: the rules-vs-intent slip flagged in the
  experiment report's Section 6 is itself a meta-pattern about
  defaulting to rules where intent is appropriate. Worth watching
  during framework methodology work specifically.

---

### 2026-05-07 — Ad-hoc structural decisions lack process and record

**Type:** process
**Severity:** minor
**Blast radius:** all projects
**Status:** resolved
**Resolved:** 2026-05-07 — Three-layer structure decisions protocol adopted in the framework: behavioral rule in `CLAUDE.md`, recording artifact at `core/structure.md`, consultation pattern via the read-at-session-start instruction. Working rhythm added to `core/nla-foundations.md` (consumer-facing). Skill references wired into `core/skills/maintain.md` and `install.md`; `/create-app` updated to populate the structure record for new domain projects. Experimental validation at `reference/experiments/structure-decisions-protocol/experiment-report.md` (H1, H2, H3, H5 all passed). Domain-project propagation (intent file updates, update-notes for existing projects) deferred to a follow-up publication session.

**Observation:**
NLAs don't have a good process for modifying their directory structures
and placing files within them. When the AI determines "we need X," it
tends to create `x/` ad hoc — picking a location, making the directory,
moving on. Two failure modes stack:

1. **No checkpoint with the human.** The structural decision slips in
   unannounced. The human doesn't get a chance to redirect or approve.
2. **No record for future sessions.** The next AI has no idea why `x/`
   exists, where related things should go, or whether the placement was
   thought through. Future sessions either re-derive or guess.

The cumulative effect is haphazard accumulation. The framework prescribes
a default structure via `install/structure-intent.md`, but once an NLA
exists, deviations and additions land without the propose-review-record
discipline that other framework operations already carry (`/install`
proposes permissions, `/think` proposes design, `/create-app` proposes
initial structure). Structural change is the gap.

**Before:** AI creates new directories silently when a task implies they
are needed. The reasoning lives nowhere; future sessions must re-derive
or guess where things go.

**After:** AI proposes structural changes for human review (Phase-1-to-
Phase-2 style), records the approved decision in an attributed structure
document with reasoning, and consults that document on future placement
decisions.

**Affected files (proposed):**
- New: structure-with-attribution doc (location TBD per framework-first
  plan — likely `core/structure.md` for the framework, extension to
  `app/overview.md` for domain projects)
- `CLAUDE.md` (the behavioral rule)
- Possibly `core/nla-foundations.md` (the protocol pattern as principle
  or working rhythm)
- `core/skills/maintain.md`, `core/skills/install.md`,
  `.claude/skills/create-app/SKILL.md` (skills whose work creates
  structural decisions)

**Proposed fix:**
Three-layer pattern — behavioral rule + attributed artifact + consultation
discipline. Borrowed shape from facebook-moderation's compile-time
build-guide. Framework-first adoption, validated by controlled experiments
(per the methodology in `reference/experiments/skill-invocation-discipline/
experiment-report.md`), then propagated.

**Notes:**
- Surfaced during a /think discussion 2026-05-07 after the maintainer
  read facebook-moderation's `app/compile.md` and the build-guide it
  produced (`lib/ingest-build-o/build-guide.md`).
- Connects to the 2026-03-04 archived entry (Plan agent making cross-
  project edits without checkpoint) — same family of "structural
  decisions slip in without review," different scope.
- Connects to the pending "Framework lacks documented experimentation
  methodology" entry — this work applies that methodology before
  formalizing it. Useful evidence either way.

---

### 2026-05-06 — Reading accumulated artifacts before /think saves rediscovery

**Type:** process
**Severity:** positive
**Blast radius:** maintainers (immediate); all projects (the pattern generalizes to any NLA)
**Status:** resolved
**Resolved:** 2026-05-06 — Pattern surfaced and applied during this session; documented for future use.

**Observation:**
This session ran /think on the skill-invocation doctrine question and
converged on several findings independently — only to discover that
GitHub Issue #24 (a feedback letter from facebook-moderation) had
captured most of those findings and several more. Reading the issue
*after* /think meant the plan needed substantive rework to incorporate
findings that were already documented.

The maintainer was the one who pointed at the issue (knowing it
existed), so the cost was bounded. But the pattern generalizes: when
considering substantive work on a topic where prior thinking might
exist, *read accumulated artifacts first*. /think extends and stress-
tests existing thinking; it shouldn't reinvent it.

**Generalizable:** Yes. Applies to any maintenance work where prior
artifacts (feedback log, friction log, design rationale, related
GitHub issues) might capture relevant thinking. Cost: a few minutes
of reading. Value: variable but can be large (the letter saved us
from a plan missing three sections).

**Operational gap noticed:** The /maintain session-start prompt reads
the *post-triage* feedback log. Open GitHub Issues that haven't been
triaged yet are invisible at session start. Issue #24 was filed
2026-05-05 (one day before this session) and hadn't been triaged —
so it was on GitHub but not in the feedback log. Two possible fixes:
(a) maintainer remembers to run `/check-feedback` discovery
(no triage) at session start when substantive work is on deck; or
(b) /maintain's session-start adds a quick `gh issue list` check
alongside the feedback log read. The second feels procedurally
right but lives outside this entry's scope.

**Affected files:**
- `core/skills/maintain.md` (potentially — Session Start)
- Possibly the Working Rhythms section in `core/nla-foundations.md`

**Proposed fix:**
Two adjacent fixes:
1. Update /maintain's Session Start to scan open GitHub issues, not
   just the feedback log. Lightweight check (`gh issue list --state
   open --limit 20`); maintainer decides whether to triage now or
   defer.
2. Document the broader principle in foundations: before /think on
   substantive work, scan accumulated artifacts for prior thinking.
   Potentially fold into the "improvement loop" working rhythm or
   a new "validation flow" rhythm (see related entry on
   experimentation methodology).

**Notes:**
- Related to "Framework lacks documented experimentation methodology"
  entry below (the meta-question about formalizing methodology).
- Maintainer's framing: "I sent the feedback letter myself, and I
  knew we were missing key parts of the plan, which is why I wanted
  you to read the full letter." So the maintainer was operating as
  an informed session-manager (Issue #24 item 8); the cost would be
  higher in sessions without that human-in-the-loop awareness.

---

### 2026-05-06 — Controlled prose experiments validated the skill-invocation doctrine refinement

**Type:** process
**Severity:** positive
**Blast radius:** maintainers (immediate); all projects (methodology generalizes)
**Status:** resolved
**Resolved:** 2026-05-06 — Experiments ran (Layers A-D + T1-T5 + calibration); framework wrappers migrated to new convention; full writeup at `reference/experiments/skill-invocation-discipline/experiment-report.md`. Plan for downstream publication at `reference/plans/skills-doctrine-publication.md`.

**Observation:**
A controlled prose-experiment methodology produced empirical findings
that reasoning alone wouldn't have surfaced. The experiments tested
whether constraint-bearing skill description language disciplines AI
invocation behavior — a question where the framework had a documented
prior decision (`disable-model-invocation: true` on all skills) and
proposed reversing required evidence proportional to the original
concern.

The shape that worked: hypothesize → isolate variable → cold-context
agent → binary signal (filesystem state) → iterate or commit. Each
test cycle was ~30 seconds + analysis. Total experimental cost across
all layers and calibrations: ~30-45 minutes. One finding (Layer C)
disconfirmed an assumption we'd otherwise have shipped.

The methodology pattern is the more durable contribution. Future
prose-as-code work in the framework — doctrine changes, convention
shifts, skill template revisions — could benefit from the same shape.
See report Section 4 ("Cross-Cutting Findings") for the methodology
findings beyond the immediate doctrine question.

**Generalizable:** Yes. The pattern is "controlled experiments on
prose-as-code." Applies whenever a prose change has downstream impact
and reasoning alone leaves uncertainty. The experiments worked in this
domain (skill descriptions); they should generalize to others (CLAUDE.md
prescriptive language, intent file conventions, skill template shapes,
etc.).

**Notes:**
- The cold-context review methodology (two-pass: simulation + frame
  question) is a related but distinct contribution surfaced by this
  work. Issue #24 introduced it; our experiments validated its value
  in a different domain. Worth surfacing in the same writeup but
  conceptually separate from the prose-experiment methodology.
- See companion friction-log entry: "Framework lacks documented
  experimentation methodology" (the meta-question of whether to
  elevate this pattern to framework-level guidance).
- The experiment report itself (~600 lines) is the durable artifact;
  this friction log entry is the pointer.
- Mistakes worth flagging (full list in report Section 6): the initial
  test design conflated visibility and constraint; we almost shipped
  pilot-skill testing instead of production-form testing; a
  rules-vs-intent slip on audit design needed correction. The user-as-
  session-manager pattern (Issue #24 item 8) was load-bearing
  throughout.

---

### 2026-03-25 — settings.local.json accumulates junk instead of systematic permission entries

**Type:** process
**Severity:** major
**Blast radius:** all projects
**Status:** resolved
**Resolved:** 2026-04-15 — Architectural change: the packages/ submodule model eliminates cross-directory reads entirely, making Read permission entries and settings.local.json generation for them unnecessary. The symlink investigation is also closed — symlinks are ruled out (test data from Issues #15, #16 confirmed they add friction rather than removing it).

**Observation:**
The permission management model (designed 2026-03-04) envisioned clean, systematic
entries like `Read(../nla-framework/**)` generated by `/create-app`, `/install`, and
`/update`. In practice, the framework's own `settings.local.json` contains a junk
drawer of individually approved commands — entire commit messages, shell loop fragments,
broken entries — accumulated from one-off approvals over time. No systematic Read
permission entries for sibling directories exist.

The user reports "tons of permissions messages" despite having updated their NLAs. The
generation lifecycle (create → install → update → validate) either never ran for
existing projects, or the generated entries don't match what Claude Code actually checks.

**Before:** Permission model designed but not delivering friction relief in practice.
**After:** Clean permission entries that actually eliminate cross-directory prompts.

**Related discovery:**
Symlinks within the project directory bypass Claude Code's permission checks entirely.
A symlink at `dependencies/nla-penny-post` → `../nla-penny-post/` allows reads through
the logical path with no permission prompt. Tested 2026-03-25 from the framework project.
Test letters sent to 5 domain projects to gather broader data.

**Open questions:**
- Is the generation logic in `/create-app` and `/update` actually producing the entries?
- Does Claude Code's permission pattern matching support `Read(../nla-framework/**)`?
- Would symlinks be a more reliable solution than settings-based permissions?
- Why did direct reads to sibling directories also work without prompts from the
  framework project? (Permission mode specific? Accumulated one-off approvals?)

**Affected files:**
- `install/install.md` — permission declarations
- `.claude/skills/create-app/SKILL.md` — settings generation
- `core/skills/install.md`, `core/skills/update.md` — permission proposal logic

**Proposed fix:**
Awaiting test results from domain projects (Issues filed 2026-03-25). Once data is in,
either fix the settings generation pipeline or pivot to a symlink-based architecture.

---

### 2026-03-04 — Plan agent proposed cross-project edits that contradicted /think design

**Type:** process
**Severity:** minor
**Blast radius:** maintainers
**Status:** resolved
**Resolved:** 2026-03-04 — Reverted package edits, logged pattern.

**Observation:**
During implementation of the permission management model, the Plan agent proposed
directly editing sibling package manifests (penny-post, process-helpers). This
contradicted the design from the /think session, which explicitly established that
packages learn about permission declarations through `/update` from the framework —
not through direct cross-project edits by the framework maintainer.

The changes were implemented before the human caught the contradiction.

**Root cause:**
Two contributing factors:

1. **Plan agent lacked design context.** The Plan agent received a summary of
   decisions but not the reasoning behind the migration flow design. It optimized
   for completeness ("these packages need permissions sections") rather than
   honoring the principle that each project adopts changes through its own update
   channel.

2. **Review gap between /think and plan.** When reviewing the Plan agent's output,
   the AI checked for mechanical correctness (right files, right format) but didn't
   verify each step against the /think design principles. The contradiction was
   between a design-level decision (migration flows through /update) and an
   implementation step (directly edit packages) — a category mismatch that
   mechanical review doesn't catch.

**Generalizable pattern:**
When a /think session establishes *how changes flow between projects*, the
implementation plan must respect those flow decisions. Direct cross-project edits
bypass the update channel that was designed precisely for this purpose. This is
also a "Context Determines Competence" issue — changes to a package's manifests
are judgment operations that should happen in that package's own maintenance
context.

**Proposed fix:**
When writing implementation plans after a /think session, explicitly check each
proposed cross-project edit against the /think design: "Does this change belong
in the current project's context, or should it flow through /update?" Add this
as a pre-flight check item in the maintain skill.

---

### 2026-03-03 — Framework maintain skill can't use thin wrapper pattern

**Type:** core
**Severity:** minor
**Blast radius:** all projects
**Status:** resolved
**Resolved:** 2026-04-18 — Broadened `core/skills/maintain.md` so it works in both domain-project and framework/package contexts (conditional path phrasing for foundations and overview, project-type-agnostic "What You Can Edit" table, "Check for Downstream Effects" principle renamed to "Name the Blast Radius" as a universal principle with domain-project specifics preserved inside). Shrank `.claude/skills/maintain/SKILL.md` to the `/validate` wrapper pattern — framework-specific opening + required reading, delegation to core for methodology, plus framework-specific addenda (editable targets, Blast Radius taxonomy, framework-specific Common Tasks: Updating Core Skill Logic / Updating Intent Files / Updating Core Files). Sync burden eliminated — subsequent universal edits (like the Writing Standards pointer added 2026-04-17) only need to land once in core. See session log `2026-04-18-writing-standards-phase-2.md`.

**Observation:**
The framework's own `.claude/skills/maintain/SKILL.md` is a full custom version
rather than a thin wrapper to `core/skills/maintain.md`. The core file assumes domain
project context — hardcoded paths like `app/overview.md`, `app/shared/values.md`,
`reference/system-status.md`. The framework doesn't have these, so it maintains a
parallel version with adjusted targets.

This creates a sync burden: structural changes to the session log format, common tasks,
or session lifecycle steps need to be applied to both files. The framework is an NLA
itself — it should be able to use its own patterns.

**Root cause:** The core maintain skill is written in "code style" (prescriptive paths)
rather than "NLA style" (described intent). "Read `app/overview.md`" could be "read
your project's overview document." The AI resolves the right path in any context.

**Possible approaches:**
- Broaden language in `core/skills/maintain.md` until the framework can thin-wrap it
- Rename/move core files to match the `app/` convention the skill assumes
- Some combination

**Re-prioritized 2026-04-17:** Status bumped from deferred to pending after the
2026-04-17 session added to the dual-maintenance surface (Writing Standards
section dual-applied to both files). The user flagged that the sync burden is
getting more annoying and estimated the broadening fix at 5–10 minutes. Next
session candidate — pairs naturally with #21 Phase 2 work or can be done
independently.

---

### 2026-04-16 — /export may not need to flatten thin wrappers anymore

**Type:** core
**Severity:** minor
**Blast radius:** project generation
**Status:** resolved
**Resolved:** 2026-04-16 — Rewrote /export as a view-source plugin generator with a hybrid AI + Python script architecture. Plugins now mirror the NLA's structure (no flattening); paths get ${CLAUDE_PLUGIN_ROOT}/ prefixes so intra-plugin references resolve reliably. See session log `2026-04-16-export-simplification.md` and design-rationale "Plugin Export: View-Source Model". Resolved jointly with feedback #9.

**Observation:**
The export skill flattens the two-hop thin wrapper pattern (wrapper → framework file)
into self-contained skills because "plugins cannot reference files outside their
directory." This was correct under the sibling-directory model: thin wrappers pointed
to `../nla-framework/`, which wouldn't exist in the plugin's installed location.

With the packages/submodules model (2026-04-15), dependencies are inside the project.
A plugin bundled with its own `packages/` directory could plausibly contain internal
thin wrappers that resolve within the plugin:

```
my-plugin/
├── skills/
│   └── startup/SKILL.md   ← "Read packages/nla-framework/core/skills/startup.md"
└── packages/
    └── nla-framework/      ← bundled as part of the plugin
```

If Claude Code's plugin loader treats the plugin directory as the working context for
skills, internal thin wrappers work and no flattening is needed.

**Resolution notes:** The hypothesis was mostly right. Plain relative paths in SKILL.md don't resolve reliably (Claude Code issues #17741, #11011), but `${CLAUDE_PLUGIN_ROOT}`-prefixed paths do. The redesign uses the prefix and preserves structure. The reframing that settled it: "view source" replaced "compile" as the guiding metaphor — the plugin is the NLA in an inspectable form, not a compiled artifact.

**Affected files:**
- `core/skills/export.md` — rewritten
- `lib/export.py` — new script
- `reference/design-rationale.md` — new "Plugin Export: View-Source Model" section; prior entry marked superseded

**Notes:**
Raised during debrief of 2026-04-15 session. Surfaced by the question "why can't
plugins use the thin wrapper pattern?" — the assumption was correct in the sibling
era, may not be correct now.

---

### 2026-03-03 — Context-aware help/guide skill

**Type:** core
**Severity:** minor
**Blast radius:** all projects
**Status:** resolved
**Resolved:** 2026-03-05 — Added Working Rhythms section to nla-foundations.md, created /guide mode-as-skill, broadened overview.md pattern to include user workflows, added nudges to startup/maintain/create-app.

**Observation:**
The framework workflow (startup → maintain → think/plan → validate → debrief → close)
is implicit. Individual skills know what they do but not where they sit in the larger
flow. A new user finishes `/create-app` and has no guidance on what to do next.

A context-aware help/guide skill could: understand where the user is in the workflow,
explain the system as they encounter it, serve as a tour guide for recent framework
changes after `/update`, and adapt to the user's interest level. This is interactive
onboarding, not static documentation.

**Open questions:**
- Does it read session state? Know what skills you've used?
- Is it a mode or a skill you invoke?
- How does it relate to `/startup`?
- Does it replace documentation or complement it?
- The "tour guide for recent changes" angle connects to `/update` — walk through
  what changed and why it matters for your project.

**Proposed fix:**
Design session (`/think`) to work through the concept. This is a new feature, not a
tweak to existing skills.

**Notes:**
Surfaced during debrief. The user has internalized the workflow rhythm but recognized
other users won't. The AI's ability to gauge interest and respond to questions makes
this a natural fit for an NLA skill rather than a static doc.

---

### 2026-03-03 — Session close skill

**Type:** core
**Severity:** minor
**Blast radius:** all projects
**Status:** resolved
**Resolved:** 2026-03-04 — Created `/close` core skill (`core/skills/close.md`). Shape-neutral session closer that creates or finalizes session logs, checks loose ends, summarizes state. Registered across framework (wrapper, intent, create-app, CLAUDE.md, README).

**Observation:**
There's no `/close` or `/end` skill to wrap up a session. The maintain skill has
session-close *steps* (finalize log, check README, suggest validation) but they're
buried in the skill doc rather than being an invocable action. From a UX perspective,
an explicit session-close skill signals "we're done" and handles the checklist:
commit, finalize session log (including debrief section), "here's where to pick up
next time."

---

### 2026-03-03 — Skills should suggest next steps

**Type:** core
**Severity:** minor
**Blast radius:** all projects
**Status:** resolved
**Resolved:** 2026-03-04 — Added light next-step suggestions to `debrief.md` (→ /close), `validate.md` (→ /debrief, /close), `export.md` (→ validation, /close), `maintain.md` (session close → /close). `/install` already suggested /validate, left unchanged.

**Observation:**
Skills have natural successors that aren't surfaced: `/validate` → `/debrief` or fix
findings, `/debrief` → session close, `/install` → `/validate`, `/maintain` (after
resolving items) → `/validate`. Users who know the workflow follow it naturally; new
users don't know what comes next.

---

### 2026-03-03 — Add debrief section to session log format

**Type:** process
**Severity:** minor
**Blast radius:** all projects
**Status:** resolved
**Resolved:** 2026-03-03 — Added Debrief section to session log template in `core/skills/maintain.md` and framework's own maintain skill. Added debrief population as first session-close step. Updated `core/skills/debrief.md` to note conclusions land in session log.

**Observation:**
"What went well and why" has no natural home. The friction log captures what went
wrong. Session logs capture what happened. But positive observations and process
reflections disappear when the session ends. The debrief's value is the
participant-observer perspective — the AI experienced the instructions and the
interaction. That perspective is worth preserving.

---

### 2026-03-03 — Validation findings should propose dispositions, not just report

**Type:** process
**Severity:** minor
**Blast radius:** all projects
**Status:** resolved
**Resolved:** 2026-03-03 — Added "After Presenting Findings" section to `core/skills/validate.md` with disposition flow: fix now, defer (friction log), or ignore (friction log as wont-fix). AI recommends based on context advantage, effort, dependencies, and batching potential.

**Observation:**
Validation surfaces findings but doesn't prompt action. Findings get noted in session
logs, carried forward, and rediscovered by the next validation run — sometimes across
multiple sessions. The `/check-updates` gap was noted three times before being fixed.
Root cause: findings live in session logs (history) rather than the friction log (queue).

---

### 2026-02-22 — "Adding a New Skill" checklist not surfaced during skill creation

**Type:** process
**Severity:** minor
**Blast radius:** maintainers
**Status:** resolved
**Resolved:** 2026-03-03 — Added "Adding a New Skill" section to `core/skills/maintain.md` Common Maintenance Tasks, referencing the checklist in `core/skills/README.md`.

**Observation:**
When adding `/check-updates` as a new core skill, three of seven steps in the
`core/skills/README.md` "Adding a New Skill" checklist were missed: creating the
framework's own wrapper, updating the What's Here table, and updating the README
directory tree. `/validate` caught all three post-implementation.

The checklist exists and is correct — it just wasn't consulted during implementation.
The maintain skill's "Updating Core Skill Logic" section and the plan file both
focused on the core logic and intent files, not the mechanical registration steps.

**Affected files:**
- `core/skills/maintain.md`

---

### 2026-02-22 — Package creation relies on pattern-matching against existing packages

**Type:** intent
**Severity:** minor
**Blast radius:** maintainers / package creators
**Status:** resolved
**Resolved:** 2026-02-22 — Created `install/package-intent.md` describing package conventions as a diff from domain project intent files. Lightweight approach: start from structure-intent.md and CLAUDE-intent.md, apply documented differences.

**Observation:**
When creating the process helpers package (the second NLA extension), every file was
pattern-matched against penny post's structure — CLAUDE.md, app/overview.md, install
manifest, reference files, skill wrappers. This worked well (the package was created
quickly and cleanly), but the conventions live implicitly in penny post's files, not
explicitly anywhere.

If penny post didn't exist, creating a package would mean guessing at conventions:
what goes in install/, how the CLAUDE.md differs from a domain project's, how skill
wrappers work for package skills vs. framework skills, what reference files to include.
The intent files (CLAUDE-intent.md, skills-intent.md, structure-intent.md) describe
what a *domain project* needs, but there's no equivalent for what a *package* needs.

**Notes:**
Resolved with a "diff from baseline" approach — package-intent.md describes only what
differs from domain project conventions, inheriting the rest from structure-intent.md
and CLAUDE-intent.md. Verified by creating and inspecting a throwaway test package.

---

### 2026-02-22 — Process helpers package creation went smoothly end-to-end

**Type:** process
**Severity:** positive
**Blast radius:** maintainers
**Status:** resolved
**Resolved:** 2026-02-22 — Archived as baseline. No action needed; positive observation recording the first complete four-phase flow (think → plan → implement → debrief) for package creation.

**Observation:**
The full workflow for creating the process helpers package — /think (4 exchanges to
reach the key insight), plan mode (mechanical after thinking), implementation (28 files
created in one pass), structural validate (zero issues) — worked cleanly. This is the
first time the four-phase flow (think → plan → implement → debrief) was used for a
complete package creation.

Notable positives:
- /think produced the design insight ("preference, not infrastructure") quickly
- Penny post conventions transferred cleanly to a second package (see related entry)
- The structural validate confirmed the /unpack removal was thorough
- Session pacing was good throughout — no confirmation fatigue

**Notes:**
Worth preserving as a baseline. If future package creation hits friction, this session
provides a comparison point for what smooth looks like.

---

### 2026-02-22 — "Adding a New Skill" checklist missing framework wrapper step

**Type:** documentation
**Severity:** minor
**Blast radius:** framework maintainers
**Status:** resolved
**Resolved:** 2026-02-22 — Added step 2: create `.claude/skills/[name]/SKILL.md` wrapper with project-relative paths

**Observation:**
The "Adding a New Skill" checklist in `core/skills/README.md` has 6 steps but doesn't
include creating a `.claude/skills/[name]/SKILL.md` wrapper in the framework itself.
When adding a new framework skill (as was done for think, debrief, unpack, export),
this step is essential — without the wrapper, the skill isn't discoverable by Claude Code.

**Affected files:**
- `core/skills/README.md`

---

### 2026-02-22 — Framework install/update wrappers use wrong path prefix

**Type:** core
**Severity:** minor
**Blast radius:** framework maintainers
**Status:** resolved
**Resolved:** 2026-02-22 — Changed `../nla-framework/core/skills/` → `core/skills/` in both wrappers

**Observation:**
The framework's own `.claude/skills/install/SKILL.md` and `.claude/skills/update/SKILL.md`
use `../nla-framework/core/skills/` paths — the domain-project convention. Since the
framework's working directory IS `nla-framework/`, these should use project-relative
paths (`core/skills/install.md`, `core/skills/update.md`), matching the pattern used
by the debrief, export, think, and unpack wrappers.

`core/skills/README.md` explicitly states: "The framework's own skills in `.claude/skills/`
use project-relative paths instead." These two wrappers violate that convention.

**Affected files:**
- `.claude/skills/install/SKILL.md`
- `.claude/skills/update/SKILL.md`

---

### 2026-02-22 — Session logs fall behind commits

**Type:** process
**Severity:** minor
**Blast radius:** maintainers
**Status:** resolved
**Resolved:** 2026-02-22 — Added commit-point log sync guidance to both the framework
maintain wrapper (`.claude/skills/maintain/SKILL.md`) and core maintain skill
(`core/skills/maintain.md`).

**Observation:**
Architecture review findings #11 and #14 were fixed in code but the session log
still listed them as unresolved. The fixes were committed — the session log just
wasn't updated to reflect them. This means the session log's "State at Close"
becomes unreliable as a record of what was actually resolved.

**The pattern:**
Fixes happen, a commit goes out, but the session log entry that tracks the work
doesn't get updated before the commit. The next session reads "State at Close"
and sees stale information about what's pending.

**Notes:**
The friction is minor per occurrence but compounds — each stale entry costs
a future session time to investigate whether it's actually pending or already
done. The fix is proportional: one line of guidance, not a new mechanism.

---

### 2026-02-22 — Voice and values may need splitting; values as transparent ethics

**Type:** core
**Severity:** major
**Blast radius:** all projects
**Status:** resolved
**Resolved:** 2026-02-22 — Split `voice-and-values.md` into `values.md` (startup
infrastructure) and `voice.md` (task-level shared context). Added "Values Are Visible"
principle (#3) to nla-foundations.md. Updated all core skills, intent files, and
create-app. See session `reference/sessions/2026-02-22-voice-values-design.md`.

**Observation:**
Voice (tone, personality, style) and values (ethics, priorities, non-negotiables) are
conceptually different things bundled into one file. Voice might vary by context — the
same NLA could use different tones for different platforms or audiences. Values should
be stable across all contexts. The split makes values infrastructure (loaded at startup)
and voice task-level shared context. A new "Values Are Visible" principle was added to
nla-foundations.md. Values range from stylistic preferences to legal requirements.

---

### 2026-02-20 — Need a way to export NLAs for use in Claude Cowork

**Type:** core
**Severity:** major
**Blast radius:** all projects
**Status:** resolved
**Resolved:** 2026-02-20 — Created `/export` skill (`core/skills/export.md`) that converts
NLA projects into self-contained plugins for Claude Code and Cowork. Added to
`install/skills-intent.md`, `CLAUDE.md`, and `README.md`. Updated design rationale with
plugin export section and wrapper spectrum patterns. See session log
`reference/sessions/2026-02-20-plugin-export-design.md` for full design discussion.

**Observation:**
There's no path for taking an NLA built with this framework and exporting it for use
in Claude Cowork. Users who build NLAs today are locked to Claude Code as the runtime.
Cowork reaches non-technical users who work with voice, tone, and content daily but
don't use a terminal.

---

### 2026-02-21 — Conversation structure skill: "slow your roll, let's chunk this"

**Type:** core
**Severity:** major
**Blast radius:** all projects
**Status:** resolved
**Resolved:** 2026-02-21 — Created `/unpack` skill (`core/skills/unpack.md`) as a
lightweight facilitation technique for structuring complex conversations. Added to
`install/skills-intent.md`, `CLAUDE.md`, and `README.md`. Design rationale entry
covers the facilitation technique category, composability, and naming. See session
log `reference/sessions/2026-02-21-unpack-skill.md`.

**Observation:**
During the /debrief design session, the AI presented four design questions and worked
through them one at a time. The user noted this chunked pattern was highly effective.
The discussion evolved from "formalize the pattern" to "this is a distinct skill" — a
facilitation technique that layers on top of active context rather than replacing it.

---

### 2026-02-21 — "Thoughts? Concerns? Ideas? Questions?" is an AI invitation, not a human prompt

**Type:** core
**Severity:** major
**Blast radius:** all projects
**Status:** resolved
**Resolved:** 2026-02-21 — Rewrote the "Keep the conversation open" bullet in
`core/skills/think.md`. Old language ("End substantive responses with an invitation")
read as "ask the human." New language explicitly says: when the human responds, treat
it as an invitation to share YOUR thoughts, concerns, ideas, and questions.

**Observation:**
During the debrief skill design session, the AI used "Thoughts? Concerns? Ideas?
Questions?" as a conversation closer directed at the human — "your turn to respond."
The intended pattern (established in /think) is the opposite: it's an invitation for
the AI to share ITS own thoughts, concerns, ideas, and questions in response to what
the human just said. The human's response IS the prompt; the AI treats it as if the
human had asked "do you have thoughts, concerns, ideas, or questions about this?"

**Before:** AI ends with "Thoughts? Concerns? Ideas? Questions?" as a volley back to
the human — functionally equivalent to "what do you think?"

**After:** AI receives human input and responds with its own perspective — concerns it
sees, ideas it wants to float, questions it has. The named practice is about the AI's
posture (bring expertise, engage substantively), not turn-taking.

**Affected files:**
- `core/skills/think.md` — the "Keep the conversation open" bullet

---

### 2026-02-21 — Post-session reflection as a skill (debrief / retrospective)

**Type:** process
**Severity:** major
**Blast radius:** all projects
**Status:** resolved
**Resolved:** 2026-02-21 — Created `/debrief` skill (`core/skills/debrief.md`) as a
lightweight reflection tool. Added to `install/skills-intent.md`, `CLAUDE.md`, and
`README.md`. Design rationale entry covers transition-sensitive triggers, judgment-based
handoff, and two-dimension reflection model.

**Observation:**
After running `/update` on penny post, the user asked the AI to reflect on the process:
"Think about what we just went through. Was there anything that could be improved?" That
open-ended reflection produced an 11-item feedback letter (Issue #5) — 3 items triaged
today, all accepted. The reflection wasn't prompted by a skill or a step in the update
flow. It was an informal question that happened to produce high-quality, actionable
feedback.

This suggests a general-purpose "debrief" skill that runs after major work: updates,
maintenance sessions, app execution (create-app, Duet composition, Copydesk formatting).
The AI reflects on what just happened while context is fresh.

**Two dimensions of reflection:**

1. **Process:** Ambiguities in instructions, inefficiencies in the flow, missing steps,
   places where the AI had to guess or improvise. What worked, what didn't, what could
   be streamlined.

2. **Human experience:** How did the human seem during the process? Content, confused,
   frustrated, excited? Did they hesitate before approving something? Did they shorten
   their responses (possible fatigue or impatience)? Were there too many confirmation
   steps? These are observations the human might not consciously articulate but the AI
   can surface from its position as participant-observer.

**The collaborative refinement step is essential.** The AI surfaces 3-5 prioritized
observations. The human pushes back on some, develops others, adds their own. Together
they produce feedback that feeds into the friction log (self-directed) or a penny post
letter (directed at a package or the framework).

**Evidence:** Issue #5 on this repo — penny post's post-update reflection produced 3
accepted items about downstream reference cleanup and validation strengthening in the
update skill. The process worked; it just isn't formalized.

**Discussion notes (from initial conversation):**

- **The LLM's unique position.** It was present for the entire interaction, read the
  same instructions, made judgment calls, and observed reactions. This connects to the
  "LLM self-aware diagnostics" insight from the export session — the AI can trace its
  own reasoning chain AND reflect on the human's experience.

- **Missing step in the learning loop.** Do work → reflect → capture → act. Steps 3-4
  exist (friction-log, write-letter, maintain). Step 2 is currently informal.

- **Bookend with "thinking it through."** That friction log entry is about reflection
  BEFORE implementation (design thinking). This is about reflection AFTER execution.
  Same meta-concern: the framework supports doing work well but has less support for
  thinking about work.

- **Timing is critical.** Must happen while context is fresh — before conversation
  compression loses the details that make reflection valuable.

- **Naming.** "Post-mortem" implies failure. `/debrief` or `/reflect` fits better — this
  is about learning from the full experience, including what went well.

- **Scope control.** Risk of producing a wall of observations after a long session.
  Prioritize — 3-5 observations ranked by impact, with the human choosing which to
  develop.

- **Dual destination.** Output may be letter-ready (aimed at a package or framework) or
  self-directed (friction-log material about the project's own docs). The skill needs
  to handle both.

**Affected files:**
- New skill in `core/skills/` (blast radius: all domain projects)
- `install/skills-intent.md` — new skill wrapper
- Potentially `core/skills/maintain.md` — session close could prompt for debrief

---

### 2026-02-20 — Need a "thinking it through" mode for design exploration

**Type:** process
**Severity:** major
**Blast radius:** all projects
**Status:** resolved
**Resolved:** 2026-02-21 — Created `/think` skill (`core/skills/think.md`) as a lightweight
collaborative design exploration mode. Added to install/skills-intent.md, CLAUDE.md, README.md.
Updated maintain.md Principle 2 with thinking phase reference. See session log
`reference/sessions/2026-02-21-think-skill.md` and design rationale entry.

**Observation:**
There's a gap between "exploring what and why" and "planning how to implement." Claude
Code's plan mode is implementation-oriented — it wants to produce steps and exit with an
actionable plan. `/maintain` is execution-oriented — it wants to edit files. The old
`/plan` skill was removed because it overlapped with both. But the *thinking space* —
collaborative exploration of what to build and why — doesn't have a dedicated home.

During the plugin export design session, we needed to:
- Walk through key decisions and their rationale
- Challenge assumptions (e.g., "should dev tools ship in plugins?")
- Explore paradigm-level questions (what does a feedback loop look like when distributed?)
- Capture evolving understanding without committing to implementation

Plan mode kept pushing toward decisions (AskUserQuestion with multiple choice options)
and action (ExitPlanMode). The actual design thinking happened by working around the
mode, not within it.

This isn't just a framework gap — it's a gap in how NLAs are designed. The "what and
why" phase is where the most important decisions happen. It deserves its own support,
separate from implementation planning.

**Notes:**
Related to the /plan removal (2026-02-19). /plan was removed because it overlapped with
maintain + plan mode. But what it offered — and what's now missing — is a space for
design thinking that isn't rushing toward implementation. The fix might not be a new
skill. It might be guidance in maintain or foundations about how to hold a design
conversation. Or it might be something else entirely. Needs its own thinking session.

---

### 2026-02-19 — README directory tree falls out of sync on every file change

**Type:** process
**Severity:** minor
**Blast radius:** maintainers
**Status:** resolved
**Resolved:** 2026-02-19 — Added "Check documentation mirrors" step to session close in both core/skills/maintain.md and framework wrapper. Triggers on file creation, moves, or deletions.

**Observation:**
The README's directory tree is a manual mirror of the filesystem. Every time a file is
added, moved, or deleted, the tree may need updating — but because the README isn't in
any functional chain (not read by skills, not loaded at startup, not an intent file),
there's no natural trigger to check it. The maintainer's mental model of "what needs
updating" is driven by functional blast radius, and the README is outside that model.

This keeps showing up in `/validate` structural checks. The system catches it reliably,
but after the fact — creating a recurring low-severity finding in every validation pass
that involves file changes.

**Notes:**
The deeper pattern: documentation artifacts that mirror filesystem state will always
drift unless there's a trigger in the workflow that creates the drift. This applies
to README trees, but could also apply to any manually-maintained index or listing.

---

### 2026-02-19 — Pre-flight design review caught gaps before implementation

**Type:** process
**Severity:** positive
**Blast radius:** maintainers
**Status:** resolved
**Resolved:** 2026-02-19 — Strengthened Principle 2 in maintain skill with a named "Pre-flight review" sub-section. Added specific checklist (gaps, unconsidered alternatives, unintended consequences, cost/benefit, scope, maintenance burden) drawn from what pre-flight has actually caught across sessions. Both core/skills/maintain.md and framework wrapper updated.

**Observation:**
After drafting the update notes design in design-rationale.md, we did a critical re-read
before implementation — checking for gaps, viability, appropriateness to the framework,
and extraneous content. It caught two real gaps (multi-commit sessions, core vs. intent
file distinction in notes) that would have surfaced during implementation at higher cost.

This is a distinct activity from the existing `/validate` modes: those check what exists
(coherence of the document chain, scenario traces, debug). This checks what's proposed
(is a design complete and viable before building it). Worth repeating for future designs.

**Notes:**
Not yet clear where this belongs — could be a `/validate` mode, a `/maintain` best
practice, or a standalone pattern. Watch for recurrence before deciding.

---

### 2026-02-14 — Duet maintenance session: 9 framework-level learnings

**Type:** core
**Severity:** major
**Blast radius:** all projects
**Status:** resolved — 2026-02-19. All 11 items processed in session `reference/sessions/2026-02-19-duet-feedback-and-update-notes.md`. Items 1-7, 9-11 implemented across foundations, startup, validate, maintain, create-app, and intent files. Item 8 addressed with light-touch NLA shape prompt in create-app (may revisit if insufficient). Update notes system designed and implemented for propagating changes to domain projects.

---

### 2026-02-11 — /create-app generates everything upfront; large apps may benefit from skeleton + /maintain

**Type:** process
**Severity:** minor
**Blast radius:** new projects
**Status:** resolved
**Resolved:** 2026-02-18 — Added `/maintain` as development cycle guidance in post-creation steps; added complex project edge case (4+ tasks → generate skeleton + one starter task, defer the rest to `/maintain`).

**Observation:**
`/create-app` currently generates all files with full content — voice, patterns, task docs, output spec, reference files. This works well for small, focused apps (1-2 tasks). For larger apps with many tasks or complex domain logic, generating everything in one pass may produce shallow content that needs immediate rework.

A better pattern for larger apps: `/create-app` generates the skeleton structure (directories, thin wrappers, minimal shared context, one starter task), then instructs the user to run `/maintain` sessions to flesh out the domain content iteratively.

Additionally, even for small apps, users should be told that running `/maintain` is a natural next step after creation — to refine voice, add patterns based on early usage, and iterate on the task doc after seeing real output.

**Affected files:**
- `.claude/skills/create-app/SKILL.md` — Add guidance for large apps; always mention `/maintain` in post-creation steps

**Proposed fix:**
Two changes: (1) For complex projects (many tasks, unclear domain), `/create-app` should generate a working skeleton with one task and instruct the user to flesh out additional tasks via `/maintain`. (2) Post-creation instructions should always mention that `/maintain` is how the app improves — not just for fixing problems, but for iterating on initial content.

**Notes:**
This connects to the framework's core philosophy: iterate through documentation. `/create-app` gets you started; `/maintain` is the development cycle. Making this explicit in the post-creation message reinforces the right mental model.

---

### 2026-02-12 — AI maintainer executed changes without confirming strategy

**Type:** process
**Severity:** minor
**Blast radius:** maintainers
**Status:** resolved
**Resolved:** 2026-02-12 — Added assessment step to friction log processing in both `/maintain` skills (core and framework). Straightforward fixes proceed directly; entries requiring new functionality or design decisions get discussed first, with `/plan` if scope warrants it.

**Observation:**
During friction log processing, the AI maintainer treated entry #1 ("ask where to save project") the same as entry #3 ("remove scaffold path") — jumping straight to execution without discussing the approach. Entry #3 was a straightforward removal; entry #1 involved design decisions (when to ask, how to handle non-sibling paths, how much complexity to add). The result was over-engineered changes that had to be reverted.

The pattern: not all friction log entries are equal. Some are "remove X" (clear action, small blast radius). Others are "add Y" (design decisions, trade-offs, dependencies on other work). The AI should distinguish between these and propose before editing on anything that involves design.

**Proposed fix:**
Add guidance to the `/maintain` skill (or to the AI's own memory) that friction log entries requiring new functionality — as opposed to removing or simplifying existing functionality — should be discussed before implementation. The plan mode pattern worked well for entry #3; it should have been used for entry #1 as well, with more attention to the design questions before exiting the plan.

---

### 2026-02-12 — Framework could generate config files for new NLAs

**Type:** core
**Severity:** minor
**Blast radius:** new projects
**Status:** resolved
**Resolved:** 2026-02-12 — Implemented NLA configuration system. Created `core/skills/preferences.md` (framework skill logic), scaffold config files (`config-spec.md`, `config.md`, `config/`), thin wrapper, and integrated with `/startup`, scaffold `CLAUDE.md`, `overview.md`, `README.md`, `system-status.md`, and `/create-app`. Design rationale in `reference/design-rationale.md` under "Future Direction: NLA Configuration."

**Observation:**
NLA projects need a way for app users to modify behavior without modifying the application itself. Traditional config (YAML, JSON) is too rigid for an LLM runtime. Natural language config (Markdown) lets users express preferences from structured paths to behavioral directives — the LLM reads and applies them with judgment.

**Notes:**
Design rationale covers: three-actor model (framework devs, app devs, app users), quarterback pattern (light main config routes to sub-configs by context), three-layer git separation, generic `/preferences` framework skill + app-specific `config-spec.md`, conflict/ambiguity detection, integration with `/create-app`.

---

### 2026-02-11 — /create-app should ask where to save the project

**Type:** process
**Severity:** minor
**Blast radius:** new projects
**Status:** resolved

**Observation:**
`/create-app` defaults to creating the project in a sibling directory (`../project-name/`). The user is not asked where they want the project saved. The sibling convention is convenient but not technically required — the framework reference paths (`../nla-framework/`) just need to resolve correctly, and CLAUDE.md files in different projects shouldn't interact.

The user should be asked where to save the project. The sibling directory is a sensible default, but users may have different workspace layouts.

**Affected files:**
- `.claude/skills/create-app/SKILL.md` — Add location question to conversation flow, update path generation logic

**Proposed fix:**
Add a question to the `/create-app` conversation (Phase B or D) asking where to save the project. Default suggestion is `../project-name/`. If the user picks a different location, adjust the framework reference paths in thin wrappers and CLAUDE.md accordingly. Note the two constraints: (1) the framework path must resolve, and (2) CLAUDE.md files from different projects shouldn't be in the same directory tree where Claude Code might pick up both.

**Notes:**
Relates to "Path resolution" in Patterns to Watch. Non-sibling layouts are the main case where `../nla-framework/` breaks. If `/create-app` knows the actual location, it can generate correct paths from the start.

**Deferred 2026-02-12:** Asking about location is simple, but the framework path appears in ~17 places across 8 files in generated projects. Non-sibling support means changing all of them, and there's no single source of truth for the path after creation — moving the project later means manually updating all 17 references. A configuration variable (e.g. `framework_path`) would centralize this. Deferring until the config file design is resolved (see "Framework could generate config files for new NLAs" entry above), then tackling location as part of that.

**Resolved 2026-02-12:** Config system is now implemented. Investigated non-standard locations end-to-end. The config system makes the declaration layer easy (`Framework path:` in config.md), but `core/skills/*.md` files share hardcoded `../nla-framework/` paths across all domain projects. Making these location-agnostic requires either natural language path resolution (adds inference overhead to the common case), template variables (foreign to NLAs), or heavier wrappers. All degrade the default sibling experience to support a rare case. Decision: keep the sibling convention for MVP. Path resolution is a mechanical operation where you want reliability, not LLM flexibility. See `reference/design-rationale.md` "Sibling Directory Convention" for full rationale.

---

### 2026-02-11 — Scaffold path in /create-app conflates example app with side-by-side install

**Type:** process
**Severity:** minor
**Blast radius:** new projects
**Status:** resolved
**Resolved:** 2026-02-12 — Removed scaffold/from-scratch path choice from `/create-app`. Created `/create-sample-app` skill for installing the scaffold as a standalone example project.

**Observation:**
The `/create-app` skill presents a "scaffold path" that installs the sample format-article task alongside the user's custom task. The intent was to help users learn by example, but the scaffold app is better understood as a standalone example application — something you install once to see how a complete NLA works, not something you mix into a real project.

**Before:** `/create-app` offers "scaffold path" (includes sample formatter alongside custom task) vs "from-scratch path" (custom task only). The scaffold path is recommended for first-time users.

**After:** Two cleaner options: (1) A separate skill like `/create-sample-app` that installs the scaffold as a standalone example project, or (2) `/create-app` briefly mentions the scaffold can be installed separately as a reference, without emphasizing it. The scaffold-as-example is probably a one-time thing and shouldn't be a prominent fork in the create flow.

**Affected files:**
- `.claude/skills/create-app/SKILL.md` — Remove or de-emphasize scaffold path
- Possibly new skill: `.claude/skills/create-sample-app/SKILL.md`
- `scaffold/` — Already works as-is for standalone install

**Proposed fix:**
Remove the scaffold/from-scratch path decision from `/create-app`. Either create a `/create-sample-app` skill that installs the scaffold as a standalone example, or have `/create-app` mention in passing that the scaffold directory can be installed separately. The create flow should focus entirely on the user's custom project.

**Notes:**
The user who surfaced this already had a standalone scaffold project and chose "from scratch" immediately. The scaffold path may never have been the right default — a standalone example app is more useful than a hybrid project.
