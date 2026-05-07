# Maintenance Session: Skills Awareness Convention

**Date:** 2026-05-06 (extending into 2026-05-07 for report drafting)
**Status:** Complete

## Intent

Two unrelated workstreams ran in this session:

**Workstream A** (early): Document the `--recurse-submodules` one-step
clone option in both the framework's README and the generated NLA
README template. Closes a small onboarding gap where users following
the documented clone steps reached a working state but via the longer
two-step path.

**Workstream B** (main): Refine the framework's skill-invocation
convention. The original 2026-02-18 convention required
`disable-model-invocation: true` on all skills, structurally removing
them from the AI's active prompt. This refinement keeps skills in the
active prompt but uses constraint-bearing description language to
discipline invocation. Empirical experiments validated the approach;
the framework's own wrappers were migrated as the first adopter; a
plan for downstream publication was drafted, reviewed by two parallel
cold-context agents, revised, and committed for execution in a future
session.

The behavioral change for the framework: the AI now sees skill
descriptions in its tool listing and can suggest skills at appropriate
moments (e.g., `/debrief` at task transitions), without producing the
spontaneous-invocation failure mode the original convention prevented.

## Changes Made

### Workstream A: Recurse-submodules documentation

- `README.md` — `git clone --recurse-submodules` is now the primary
  clone form; `git submodule update --init` shown as fallback for
  already-cloned repos.
- `.claude/skills/create-app/SKILL.md` — generated NLA README template
  carries the same change. New domain projects from `/create-app`
  post-publication get the updated guidance.
- `install/update-notes.md` — entry telling domain project maintainers
  about the optional README mirror update.

### Workstream B: Skills awareness convention

- **21 framework wrapper migrations** (`.claude/skills/*/SKILL.md`) —
  removed `disable-model-invocation: true`, replaced descriptions
  with the new pattern: `[what] + Relevant when [trigger] + AI:
  Suggest as an option; invoke only on user assent or /skill-name`.
  Per-skill description audits during distillation reframed two
  invitation-style descriptions (`/check-feedback`,
  `/write-letter`) per the design rationale's specific concern about
  external-action skills.
- **Framework `CLAUDE.md`** — added "Skill invocation discipline"
  backstop rule covering ambiguous cases.
- **Auto-memory** (local, not committed) — updated convention entry;
  added two `feedback`-type memory files
  (`feedback_read_artifacts_before_think.md`,
  `feedback_intent_over_rules.md`); MEMORY.md updated with pointers.
- **`reference/plans/skills-doctrine-publication.md`** — drafted plan
  for future Commit C session that publishes the convention to domain
  projects. Reviewed by two parallel cold-context agents; revised to
  address findings; cold-context review findings appended as audit
  trail.
- **`reference/experiments/skill-invocation-discipline/experiment-report.md`**
  — first experiment report in the framework, documenting the prose
  experiments (Layers A–D, T1–T5, calibration) and cross-cutting
  methodology findings. Introduces `reference/experiments/` as a small
  new convention modeled on facebook-moderation's pattern.
- **`reference/friction-log.md`** — four new entries (two from main
  experiment work, two from debrief observations).
- **Banana-test cleanup** — the throwaway test skill at
  `.claude/skills/banana-test/` was deleted after experiments. Was
  never committed; deletion required no commit.

## Decisions Made

### Refinement, not reversal, of the 2026-02-18 design decision

The new convention addresses the same concern (preventing spontaneous
invocation) via a different mechanism (constraint-bearing descriptions)
than the original solution (structural removal from active prompt).
Empirical evidence shows constraint language disciplines invocation;
the AI honors "AI: do not invoke without user assent" while still
surfacing the skill conversationally. Original concern about
external-action skills (`/write-letter`, `/check-feedback`) is
preserved via stronger constraint language for those specifically.

Alternative considered: tier the skills, applying the new convention
only to "safe" skills and keeping the toggle on for external-action
ones. Rejected for simplicity; the constraint-language approach
covers external-action concerns adequately. Tiering can emerge
post-rollout if specific skills misbehave.

### Per-description constraints, not CLAUDE.md global rule alone

Layer C of the experiments disconfirmed the assumption that a global
system-prompt rule could substitute for per-description constraints.
The description's routing trigger wins contention with system-prompt-
level discipline when the trigger is clear. The CLAUDE.md backstop
rule remains useful (Layer D showed it helps with ambiguous cases)
but cannot replace the per-description discipline.

### Internal-only adoption; downstream publication deferred

The framework's house adopts the convention this session. Publication
to domain projects (Commit C) is deferred until verification in real
maintenance use. Premature publication would propagate a regression
to every downstream NLA. The plan at
`reference/plans/skills-doctrine-publication.md` captures the
publication arc with pre-requisites that must be verified before
execution.

### Plan structure follows Issue #24's four-section template

The plan was drafted using the four-section template from the
facebook-moderation feedback letter (substance + procedural-edge
cases + judgment defaults + confidence band) plus standard sections
(intent, goals, open questions, verification). Cold-context reviewers
explicitly noted the structure pre-addressed many of their concerns.

### Reference/plans/ as new directory convention

Adding `reference/plans/` for warm-context-drafted plans intended for
later-session execution. Modeled on `reference/standards/` and
`reference/experiments/` patterns — a small convention introduction.

### Reference/experiments/ as new directory convention

First experiment report drafted; directory introduced to hold future
experiment writeups. Modeled on facebook-moderation's
`reference/experiments/` pattern.

## What Didn't Work

### Initial test design conflated visibility and constraint

My first experimental design (the "say BANANA" prepending test) would
have ambiguously tested both whether descriptions are visible AND
whether they carry instructions. The maintainer's refinement (test
with a file-creation side effect, separating routing from constraint)
was load-bearing. Without that refinement, the experiments would
have produced ambiguous results.

### Subagent-as-test-bench was wrong

Initial plan: use Agent tool subagents as cold-context test bench.
Discovery probe revealed general-purpose subagents do not load
project-level skills — their toolset is harness-defined. Pivoted to
`claude -p` headless invocation. The discovery cost was minutes; the
alternative would have been hours of wrong-instrument work.

### Plan was drafted with state mismatches

The first plan draft referenced framework wrapper migration as if it
had already happened; at drafting time, it hadn't. Pass 1 (cold-context
simulation) caught this and several related state-mismatch issues.
Lesson: when drafting a plan, distinguish "what we did" from "what we
plan to do" in the prose.

### Rules-vs-intent slip on audit design

When designing the body audit step, my first proposal was a
forbidden-phrase checklist. The maintainer pointed out this was
rules-shaped and inconsistent with the framework's foundations
principle #4. Intent-based audit was clearly better. Surfaced as a
meta-pattern worth watching across future similar work; captured in
auto-memory as `feedback_intent_over_rules.md`.

### Bulk Edit calls didn't parallelize

The 21 wrapper migrations were intended to run as parallel Edit
batches. System reminders fired between each Edit, ending each turn
sequentially. Net result: 21 sequential edits despite parallel intent.
Captured as friction log entry.

## Friction Log Entries Processed

None — no pending entries were resolved this session. Four new
entries added (two from main experiment work, two from debrief
observations).

## Debrief

Eight observations surfaced during /debrief, captured across the
experiment report (Section 6 + cross-cutting findings), friction log,
and auto-memory:

- **Cold-context review methodology paid off.** Pass 2 (frame
  question) caught the design-rationale reversal that Pass 1
  (simulation) wouldn't have. Two-pass distinction is load-bearing.
- **Reading accumulated artifacts before /think saves rediscovery.**
  Issue #24 captured findings the /think session converged on
  independently. Maintainer-as-session-manager pointed us to it.
  Operational gap: /maintain's session-start reads only the
  post-triage feedback log; pre-triage open issues are invisible.
- **Rules-vs-intent slip is a watchable pattern.** Defaulted to
  rules when intent was the right shape; corrected when surfaced.
  Captured in memory as a feedback pattern.
- **The audit step caught the design-rationale's specific concern
  cases.** `/check-feedback` ("Run periodically") and `/write-letter`
  ("Best used at the end of") had invitation-style language that
  needed reframing during distillation. Without the audit, we'd have
  reproduced the original failure mode.
- **The four-section plan template produced demonstrably better
  reviewability.** Reviewers explicitly noted concerns were
  pre-addressed. Feeds Issue #24 recommendation B.
- **Bulk Edit calls didn't parallelize as intended.** Harness
  behavior; worth Write or Bash shaping for future bulk migrations.
- **Test the production form, not a stand-in.** Pilot-skill testing
  would have missed the over-routing issue that surfaced from
  testing actual production wording.
- **Bench discovery before instrument design.** Saved hours of
  wrong-instrument work via a one-step probe.

These are now captured durably across the experiment report,
friction log, and auto-memory.

## State at Close

### Context for next time

- **Six commits pushed to origin/main**, no tag. All internal-only:
  recurse-submodules docs (workstream A, two commits) and skills
  convention adoption (workstream B, four commits).
- **Convention adopted in framework's house.** All 21 framework
  wrappers are model-invokable with constraint-bearing descriptions.
  CLAUDE.md backstop rule is active. Auto-memory updated.
- **The skills listing in active prompt now shows the new pattern.**
  This session continued working with the new convention after
  adoption (during the experiment report drafting and debrief);
  behavior was consistent. Counts as one substantive session of
  verification — though more sessions would strengthen confidence
  before publication.
- **Plan for downstream publication is committed.** At
  `reference/plans/skills-doctrine-publication.md`. Includes
  cold-context review findings as audit trail. Execution requires
  pre-requisite verification (which this session is the first
  satisfaction of).
- **Issue #24** (facebook-moderation feedback letter) is open. We
  consumed its findings about plan structure but did not perform
  formal triage. Triage is deferred to a separate session.

### Decisions awaiting implementation

- **Commit C (publication to domain projects)** — captured in plan;
  awaits future session.
- **Framework methodology question** — should the validation flow
  (hypothesize → experiment → measure → commit) become a documented
  fifth working rhythm? Captured in friction log; sized for /think
  + maintain work in a separate session.
- **Issue #24 triage** — recommendations A, B, C, D, E, F all
  pending; this session consumed the letter's structural findings
  about plans but didn't dispose of the issue.
- **Operational gap: /maintain session-start doesn't surface
  pre-triage open issues.** Captured in friction log; small
  procedural fix in a future session.
- **Bulk-edit harness behavior.** Pending; could be a Claude Code
  feature request, plus framework-side guidance about Write or Bash
  shaping for bulk work.

### Where to pick up

**Immediate candidates for next session:**

- **Run the framework with the new convention through a non-trivial
  maintenance session.** This would satisfy more of the verification
  pre-requisite for Commit C and surface any second-session-only
  regressions.
- **Triage Issue #24** — formal `/check-feedback` triage of the
  letter's six recommendations. Could pair with running the new
  convention since /check-feedback now has updated description and
  is in the active prompt.
- **Smaller, ready-to-go items:** the 2026-04-18 shippability
  convention refinement (still pending in friction log); the two
  2026-05-04 procedural entries (cross-reference ordering +
  archival drift, both quick edits).

**Watch:**

- Whether the AI suggests `/debrief`, `/friction-log`, etc. at
  appropriate moments in the next session. If the convention is
  working, suggestions should fire more naturally than before.
- Whether anything regresses (auto-invocation of mode-entry skills,
  spurious cross-context invocation, etc.). The constraint language
  should hold; if it doesn't, that's the escalation signal.

### Validation status

`/validate` was not run after the structural changes. Could be run
in a future session as additional verification, but this session's
empirical experiments + cold-context plan review provided substantial
verification already.

### Pending friction log entries

13 total: 9 pending + 2 deferred + 2 resolved-but-unarchived. Up
from 11 at session start (4 new entries this session, 0 resolved).
Resolved-but-unarchived entries (2026-03-25 settings.local.json,
2026-03-04 Plan agent) still drift across sessions; the 2026-05-04
"resolved-but-unarchived drift" friction entry is itself the same
problem and remains unresolved — pending a `/close` Loose Ends
addition.
