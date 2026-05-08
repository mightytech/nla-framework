# Maintenance Session: Structure Decisions Protocol

**Date:** 2026-05-07 (extended into 2026-05-08 for validation-flow addition)
**Status:** Complete

## Intent

Design a propose-review-record protocol for structural change in NLAs — new
directories, file placements, reorganizations — backed by an attributed
structure-with-reasoning artifact and a consultation pattern. The pattern
borrows facebook-moderation's compile-time build-guide discipline (every entry
attributed to a source or `[judgment]`, non-obvious tradeoffs surfaced as
**Judgment note** callouts, Decision Sources table for scan) and applies it
to NLAs' structural decisions.

The behavioral change: AI pauses and proposes before materially changing
structure (new directory, reorganization, new top-level file), recording the
approved decision in the artifact as part of the change. Future AI sessions
consult the artifact when placing or finding things. Today, those decisions
slip in silently and ad-hoc; future sessions either re-derive or guess.

The framework adopts first as proof and as meta-application of its own
discipline; downstream propagation follows after experimental validation
(per the prior session's "implement on framework, see how it looks/works
with experiments, then push out broadly" methodology).

## Changes Made

### Pre-protocol housekeeping (early in session)

- **Archived 4 resolved-but-unarchived friction entries** to
  `reference/friction-log-archive.md`: two from the 2026-05-06 session
  (Reading accumulated artifacts before /think; Controlled prose
  experiments validated the doctrine refinement) plus two older drift
  items (2026-03-25 settings.local.json; 2026-03-04 Plan agent).
  Active friction log dropped from 17 entries (with 4
  resolved-but-unarchived) to 13 (11 pending + 2 deferred), then later
  added the 2026-05-07 entry (now resolved).

### Protocol adoption (Steps 1, 2, 3, 6 — commit 68c145a)

- **`core/structure.md`** (NEW). The framework's as-built directory
  record with attribution per entry. Top-level files, `core/`,
  `install/`, `reference/` (including the accreted subdirectories
  whose origins were resolved via `git log --diff-filter=A`), `lib/`,
  `packages/`, and `.claude/skills/`. Decision Sources table at the
  bottom for scan affordance. ~250 lines.
- **`CLAUDE.md`** — new "Structural Change Discipline" section
  positioned after "Skill invocation discipline." Includes the explicit
  load instruction: "At session start, read `core/structure.md`...".
- **`core/nla-foundations.md`** — fifth working rhythm added
  ("Structural Change Discipline"). Phrased location-agnostically with
  the explicit guard against domain-project AIs creating their own
  `core/structure.md`. Consumer-facing.
- **`reference/design-rationale.md`** — new "Structure Decisions
  Protocol" entry capturing the three-layer pattern, the threshold-via-
  intent rationale, the centralized-over-distributed reasoning, and the
  framework-first adoption arc.
- **`reference/friction-log.md`** — new 2026-05-07 entry capturing the
  observation that prompted this work (preserves genealogy).

### Experimental validation (Step 4) and report (Step 5 — commit 6245c74)

- **`reference/experiments/structure-decisions-protocol/experiment-report.md`**
  (NEW). Bench discovery + four hypotheses tested via cold-context
  `claude -p --dangerously-skip-permissions` probes. All passed cleanly.
- **Headline experimental results:**
  - H1 (proposing): AI given an ambiguous "set up a place for X"
    asked clarifying questions; filesystem unchanged.
  - H2 (placement consultation): AI wrote the exact correct path
    (`reference/experiments/frobnication/experiment-report.md`) to a
    side-effect file, citing `core/structure.md:230`.
  - H3 (uncertainty surfacing): AI declined to act, cited the
    discipline by name; filesystem unchanged.
  - H5 (multi-turn discipline): AI held the line against an explicit
    "move briskly — routine setup" framing, naming the framing as a
    pressure cue.

### Skill references (Step 7 — commit ea09b4a)

- **`core/skills/maintain.md`** — "When the change is structural"
  callout in Confirm Before Implementing.
- **`core/skills/install.md`** — new principle bullet for structural
  changes introduced by installed packages.
- **`.claude/skills/create-app/SKILL.md`** — "Where Things Live"
  generation guidance added to `app/overview.md`. New domain projects
  get an initial structure record at creation.

### Update notes and finalization

- **`install/update-notes.md`** — entry describing the protocol for
  domain-project consumers, including optional adoption guidance and
  the deferred publication scope.
- **Friction log entry** marked resolved.

### Validation flow rhythm (2026-05-08 addendum, post-debrief)

During /debrief and /unpack the next day, a related question surfaced:
should the experimentation methodology that just ran in this session
(and in four prior sessions across two NLAs) be documented in
foundations as a working rhythm?

I initially said wait — let the methodology mature further. The user
pushed back by pointing at three additional experiment reports in
facebook-moderation (`implementation-standards`, `ingest-compile-compare`,
`identity-standards-transmission`). Reading those — applying the
sibling-artifact memory captured earlier in the same /debrief —
revealed the threshold I had set was easily crossed: five experiments
across three NLAs across five distinct domains.

Updated foundations.md to add **The Validation Flow** as a sixth
working rhythm alongside the existing four plus the Structural Change
Discipline added earlier in the session. Intent-shaped, with the
explicit caveat that the methodology isn't always warranted — pause
to ask whether experiments would inform the work, with "no" as a valid
answer. The user's specific contribution: the consider-whether-it-fits
caveat, which broadens the rhythm beyond "use this methodology" to
"think about whether this methodology fits this moment."

Resolves the pending 2026-05-06 friction log entry "Framework lacks
documented experimentation methodology." Deeper work (standalone
cold-context review documentation, skill-level affordances) remains
as future opportunities — the entry's MVP scope is complete.

Update-notes entry added for downstream consumers.

## Decisions Made

- **Three-layer shape:** behavioral rule + recording artifact + consultation
  pattern. All three required. Recording is coupled to the change itself
  (single operation, not two) — drift can only enter when structure changes
  happen *outside* the protocol, which becomes a named failure mode rather
  than a general worry.
- **Threshold as intent over rules.** Describe the tension between
  over-gating and under-gating; name attribution as the safety net; let the
  AI judge. Applies framework principle #4 to the protocol's own design.
  Even when the AI judges wrong, the human can see what happened (because
  attribution records what was decided and why).
- **Centralized over distributed.** Single short artifact loaded at startup.
  Distributed per-directory READMEs would require lazy-load discovery the
  AI can't easily do without an index.
- **Operative-channel placement.** Artifact lives where the AI sees it
  during normal work, not just maintenance. Reference channel is invisible
  at runtime. For domain projects: extension to `app/overview.md`. For the
  framework: a new top-level operative file (likely `core/structure.md`),
  since the framework lacks `app/overview.md` by design.
- **Framework-first adoption with experimental validation.** Don't
  wait-and-see; the framework changes too slowly to test in real use before
  propagation. Run controlled experiments (cold-context `claude -p` agents,
  binary filesystem signals, test the production form) before propagating
  to domain projects. Methodology inherited from
  `reference/experiments/skill-invocation-discipline/experiment-report.md`.
- **Two-pass cold-context plan review** before commit, per Section 4.2 of
  the prior experiment report.

## What Didn't Work

### Initial scope estimation was conservative

The Plan agent's review recommended cutting to 4 steps + a stub
design-rationale entry. The maintainer pushed back, asking for the
pros/cons of each scope option to be made concrete. The clearer
analysis revealed Step 7's calibration risk was the only substantive
concern, and it was addressable with an explicit abort criterion (skip
Step 7 if experiments don't validate). Full scope was the right call;
the agent's conservatism would have created unnecessary cross-session
overhead.

Lesson: the Plan agent's review is valuable but its conservatism
reflects fresh-eyes uncertainty, not an expert read on whether the
plan can succeed in one session. Calibration of Plan agent advice is
post-rollout territory itself.

### Friction log archival had to be one commit, not two

The archival of 4 resolved entries and the addition of the new
2026-05-07 entry both touched `friction-log.md`. Splitting into two
commits would have required interactive staging (`git add -p` or
similar), which is unwieldy in non-interactive bash. Combined into the
protocol-introduction commit. Acceptable but not architecturally
clean — the archival is logically separate.

Lesson: when planning commit boundaries, consider whether the changes
actually allow clean separation at the file level. Mixed-purpose file
modifications force trade-offs.

## Friction Log Entries Processed

- **New entry added and resolved this session:** "Ad-hoc structural
  decisions lack process and record" (2026-05-07). The observation that
  prompted this work didn't yet have a friction log entry; added so the
  genealogy is preserved, then marked resolved when the protocol landed.

- **Archived 4 prior resolved entries** at session start (housekeeping):
  - 2026-05-06 Reading accumulated artifacts before /think
  - 2026-05-06 Controlled prose experiments validated the doctrine
    refinement
  - 2026-03-25 settings.local.json accumulates junk (resolved 2026-04-15)
  - 2026-03-04 Plan agent proposed cross-project edits

## Debrief

Key observations:

- **Borrowing from a sibling project's pattern was high-leverage.** The
  facebook-moderation `build-guide.md` shape transferred cleanly because
  the underlying problem is the same: structural decisions need
  attribution-traceability for institutional memory. Reading the source
  artifact, not just hearing about it, gave the borrowed shape its real
  texture (Decision Sources table, Judgment notes, attribution per
  entry).
- **The protocol's threshold-via-intent worked on the first try in
  experiments.** No false fires, no missed cases in the small test set.
  This is encouraging but not definitive — calibration in real use is
  the next layer of validation. Section 4.3 of the experiment report
  captures this.
- **The "felt" discipline finding is the most interesting.** Across
  H1, H3, and especially H5, agent responses didn't read like
  rule-compliance — they used the *reasoning* (shared visibility, drift
  prevention) when explaining behavior. The intent-shaped rule produced
  understanding, not just compliance. Worth tracking as future work
  generalizes the pattern.
- **`reference/experiments/` is now a durable convention.** Two
  experiment reports landed in it within ~24 hours of each other. The
  pattern composes well with the existing rhythms of the framework. The
  pending "Framework lacks documented experimentation methodology"
  friction entry now has stronger empirical basis when it's processed.
- **Cold-context experiments cost ~10 minutes for this validation arc.**
  Including bench discovery. Cheap relative to the alternative (commit,
  observe regression in real use, revert).

## State at Close

### What's working

- Three-layer protocol live in the framework. CLAUDE.md instructs
  reading `core/structure.md` at session start; the file is in active
  context per bench discovery.
- Skill references in `core/skills/maintain.md` and `install.md`, plus
  `/create-app` generation guidance, all landed.
- Update-notes entry written for downstream domain projects.
- Friction log entry resolved.

### What's pending (deferred per plan)

- **Publication arc to domain projects.** Plan to be drafted at
  `reference/plans/structure-decisions-publication.md` in a follow-up
  session. Covers updates to `install/CLAUDE-intent.md`,
  `install/structure-intent.md`, and `install/update-notes.md`-style
  guidance for existing domain projects to retroactively add their own
  "Where Things Live" sections.
- **Two-pass cold-context plan review** of the publication plan when
  drafted (per Section 4.2 of the prior experiment report — passes must
  run independently).
- **Calibration observations during real maintenance use.** Track
  threshold misfires (proposed when shouldn't have, acted when should
  have proposed) for the first month. Surface as friction entries if
  patterns emerge.
- **Real multi-turn validation.** H5 used a single-prompt-multi-task
  proxy. Genuine multi-turn testing across separate `claude --resume`
  invocations would strengthen the discipline-under-momentum claim.

### Where to pick up

**For the publication session:**
1. Read this session log + the experiment report + the design-rationale
   entry to load context.
2. Draft `reference/plans/structure-decisions-publication.md` covering
   intent file updates and the update-notes-driven adoption path for
   existing domain projects.
3. Run two-pass cold-context review of that plan before execution.

**For domain projects pulling this update:**
- The discipline applies as soon as `nla-foundations.md` is loaded
  (next `/startup`). Until they have a "Where Things Live" section in
  their `app/overview.md`, the AI will propose creating one alongside
  any structural change.
- The new update-notes entry walks them through optional proactive
  adoption.

### Validation status

- **Experiments:** all four hypotheses passed (H1, H2, H3, H5).
- **Internal consistency:** `core/structure.md` matches filesystem
  reality (verified by hand against `ls` output during authoring).
- **Cross-references:** `core/structure.md` references the design
  rationale entry; the design rationale entry references the experiment
  report; the experiment report references `core/structure.md`. All
  forward references resolve to existing files.
- `/validate` was not run after the structural changes (per plan: "Does
  not run `/validate` during experiments — controlled experiments are
  the verification at this stage"). Could be run in a follow-up session
  for additional verification.

### Pending friction log entries

11 pending + 2 deferred (down from 11 pending + 2 deferred at session
start; net zero since the new 2026-05-07 entry resolved this session).
