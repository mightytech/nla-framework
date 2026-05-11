# Maintenance Session: Prose-default + create-app mode-recognition; May process-improvements sweep

**Date:** 2026-05-11
**Status:** In Progress

## Intent

Resolve two related friction entries from the 2026-05-10/11 nla-archetypes
creation session, both about how the AI should hold the conversation in
design-sensitive moments.

- **2026-05-10 (AskUserQuestion overreach):** establish a framework-level
  prose-default principle that loads into every session's prompt. The
  prior session's lapse happened despite a user-private memory note;
  memory-only mitigation was insufficient. Move the guidance to a channel
  with more weight — CLAUDE.md, which loads at session start.
- **2026-05-11 (mode-recognition):** make `/create-app` recognize when
  the user is inviting collaborative refinement rather than structured
  extraction, so the most consequential design decisions (the Guernica
  value in nla-archetypes' case) emerge through collaborative
  articulation rather than mechanical Q&A.

The two entries pull in the same direction but address different layers:
tool-choice (5/10) vs. whole-mode-recognition (5/11). Both got addressed
in this session.

## Changes Made

- **Framework's own `CLAUDE.md`** — added a "Default to prose for design
  conversations" bullet to Grounding Principles. Covers framework
  sessions: `/create-app`, `/maintain`, `/think`, any conversation-heavy
  skill run from the framework. The bullet closes with a sentence
  connecting the principle to `core/nla-foundations.md` principle #2
  ("the LLM bridges human flexibility and computational rigidity") —
  naming the foundational truth that makes enum-for-design-questions a
  category error rather than a preference.

- **`install/CLAUDE-intent.md`** — added the same prose-default bullet
  to Execution Principles (alongside "the cardinal rule" and "flag
  uncertainty"). Propagates to every domain project's CLAUDE.md via
  `/create-app` (for new NLAs) and `/update` (for existing ones).

- **`.claude/skills/create-app/SKILL.md`** — two additions:
  - A "Between Phase A and Phase B: Recognize the mode" transition
    section that distinguishes extraction from collaborative refinement
    and names four signals for the latter (working prompt or sample
    artifact, length about *why*, explicit invitation of AI perspective,
    user-named-but-unresolved tensions).
  - A "User arrives with rich conceptual work" entry in Conversation
    Edge Cases, as a sibling to "User provides everything upfront."

- **`install/update-notes.md`** — entry for the `install/CLAUDE-intent.md`
  change, so existing NLAs running `/update` see why their CLAUDE.md is
  getting a new Execution Principle.

## Decisions Made

- **Awareness-level placement, not config-directive** — the user
  proposed a lateral option of making this a default config directive
  users could change. Rejected: config is for user-facing preferences
  (voice, output length), and AskUserQuestion behavior is a craft-level
  decision about how the AI uses its own tools. Making it configurable
  would dilute the principle ("configurable" reads as "negotiable") and
  put a micro-choice in front of the user that they shouldn't have to
  think about. The asymmetry is also load-bearing: when AskUserQuestion
  is right, prose still works; when prose is right, AskUserQuestion
  fails. Prose-as-default is safer in either case.

- **Universal NLA truth, not personal preference** — discussed whether
  this was a quirk of how this user works or a universal NLA principle.
  Landed on universal, with reasoning: the LLM's value proposition is
  handling nuance (foundations principle #2). Using enums for design
  questions surrenders that value — a category error in how the
  affordance is used. Also contradicts intent-over-rules (principle #4):
  enums *are* rules. Same logic applies to standard Claude Code use, not
  just NLA framework use — the surface area is just smaller there
  (operational questions dominate).

- **Bullet in Grounding Principles, not new Execution Principles
  section** — for framework CLAUDE.md, considered creating a parallel
  Execution Principles section to match consumer NLAs' structure. About
  3-4 bullets would migrate. Skipped: scope creep for the friction
  entries at hand. The structural symmetry isn't urgent, and the mix of
  posture/practice bullets already in Grounding Principles absorbs the
  new one cleanly. Captured the reorganization possibility implicitly in
  this session log — could surface as a friction entry if it feels worth
  it later.

- **Awareness-level only, no skill-level reinforcement in
  `core/skills/maintain.md` or `core/skills/think.md`** — the 2026-05-10
  friction entry's Notes argued for in-skill reminders at the
  lapse-prone moments. Deferred: the awareness-level placement loads
  into every session's prompt via CLAUDE.md, which is exactly the
  structural change the entry argued was needed (memory-only mitigation
  had failed). If recurrence shows up despite this, trigger-level
  reinforcements can be added then. Pre-emptive layering wasn't
  warranted. `core/skills/maintain.md` already has scoped guidance
  ("when using plan mode"); broadening it can wait for evidence.

- **5/11 entry resolved through skill-level work only, not parallel
  install/CLAUDE-intent.md addition** — collaborative refinement *is*
  prose by definition, so the broader prose-default principle from the
  5/10 work already covers the mode-recognition behavior at the
  awareness level. The skill-specific transition section + edge case
  covers the trigger level for `/create-app` specifically. No need for
  a separate "recognize the mode" principle in `install/CLAUDE-intent.md`
  — it would be a generalization the friction evidence doesn't support
  (the lapse was specific to `/create-app`'s extraction-shaped Phase B).

## What Didn't Work

- **Initial proposal missed the framework-side coverage entirely** —
  first draft only addressed `install/CLAUDE-intent.md` (consumer side).
  The user caught it: "but it has to be executed somewhere — downstream
  but also here in the framework (it's causing issues during maintenance
  sessions)." The framework's own CLAUDE.md is hand-written, not
  synthesized from `install/CLAUDE-intent.md`, so the intent-file
  channel alone covers only consumer NLAs. Revised proposal added
  framework's CLAUDE.md as a parallel placement. Useful reminder: when
  framework changes propagate via the intent files, the framework
  itself is a separate consumer that needs its own coverage if the
  guidance applies to framework sessions too. Worth a friction log entry
  if this conflation happens again.

## Friction Log Entries Processed

- **2026-05-11 — /create-app's structured Q&A misses the
  collaborative-refinement mode** — resolved. Skill-level placement in
  `.claude/skills/create-app/SKILL.md`. Archived.
- **2026-05-10 — AskUserQuestion overreach despite user-private memory
  note** — resolved. Awareness-level placement in framework `CLAUDE.md`
  + `install/CLAUDE-intent.md`. Update-notes entry. Archived.

---

## Second workstream: May process-improvements sweep

After the prose-default and mode-recognition work landed, picked up five
pending process-improvement friction entries from the 2026-05-04 through
2026-05-07 range. All small (sentence-to-paragraph additions), all
about how maintenance sessions function rather than what they produce.
Bundled into one continuing session because each individual change was
too small to justify a session of its own, and the entries were
thematically tight (maintenance workflow refinement).

### Intent (second workstream)

Close out the May process-improvement backlog while context was warm.
Each entry had a well-specified proposed fix in its own body; the
work was mostly placement + wording rather than design. The opportunity
cost of waiting (each entry remaining "I should do that small thing
someday") seemed higher than the cost of doing them now.

### Changes Made (second workstream)

- **`core/skills/maintain.md` Pre-flight Review** — added a
  "Cross-references" bullet to the existing checklist (Gaps,
  Unconsidered alternatives, etc.). Framed per the 2026-05-07 update
  note as "prefer landing referenced files together in one coherent
  commit; if changes must split, write the referenced file first."
  Single-commit atomicity is the easier path; ordered split is the
  fallback.

- **`core/skills/maintain.md` Confirm Before Implementing** — added a
  "When using Plan agents" paragraph next to the existing "When using
  plan mode" guidance. Plan agents are useful for surfacing concerns
  but conservatively calibrated on scope under cold context; the
  guidance treats scope-cut recommendations as one input, with the
  maintainer extracting the underlying concern and designing an
  explicit mitigation rather than following the cut.

- **`core/skills/maintain.md` Common Maintenance Tasks** — added a
  "Bulk Edits" task that names the three shapes (`Write` per file for
  substantial rewrites, single `Bash` pipeline for mechanical
  substitutions, `Edit` for surgical varying changes). Explains why
  parallel `Edit` batches don't actually parallelize for
  state-updating tools — the harness's state-update reminders end the
  turn between calls.

- **`core/skills/maintain.md` Session Start** — extended item 2 from
  friction-log-only to both friction and feedback logs ("both logs
  drift the same way when the resolving session doesn't archive
  immediately").

- **`core/skills/close.md` Step 2 (Check Documentation Mirrors)** —
  extended scope with a paragraph on resolved-but-unarchived log
  entries. Framed as the same family of drift as documentation
  mirrors, different surface. Extending Step 2's prose rather than
  adding a new numbered step (renumbering would have been more
  disruptive than the gap warranted).

- **`core/skills/think.md` Prior Art** — added a paragraph about
  reading sibling-project artifacts directly when borrowing patterns,
  not just descriptions of them. The texture of a borrowed shape only
  becomes real after reading the file.

The friction log archival used the new "Bulk Edits" guidance directly:
a Python script via `Bash` did the five-entry move (Status: pending →
Status: resolved + add Resolved line + reposition to archive), eating
its own dogfood. Worked cleanly; the script's structure shows the
shape this guidance recommends.

### Decisions Made (second workstream)

- **One bundled session, multiple commits** — chose to do the May
  sweep in the same session as the prose-default work rather than
  splitting into separate sessions. Reason: the entries were small
  enough that per-entry sessions would be overhead, and the user
  invited it ("anything else we should work on while we're going?").
  Commit shape kept "one change at a time" by grouping each
  friction-entry's resolution into its own commit; maintain.md sweep
  bundled three entries because they touch the same file in different
  sections.

- **Step 2 extension over new step in `/close`** — for the
  resolved-but-unarchived drift fix, considered adding a new numbered
  step ("Catch log-state drift") vs. extending Step 2 ("Check
  Documentation Mirrors"). Extension chosen: renumbering disrupts
  more than the gap warrants, and the two checks share a family
  (drift between manually-maintained state and authoritative state).
  The prose framing in Step 2 makes the broadening explicit.

- **Dual placement for the drift fix** — added the resolved-but-
  unarchived check to both `/close` (catch at session end) and
  `/maintain` Session Start (catch at next session start). The
  friction entry proposed `/close` as primary with `/maintain` as
  possible secondary. Did both because Session Start already had
  friction-log-only language that extending to feedback log was a
  one-word change. Light belt-and-suspenders for log-state drift.

- **Eating dogfood on Bulk Edits** — used the new "Bulk Edits"
  guidance to do the friction-log entry move itself. Five entries
  with the same Status-change pattern is exactly the case the
  guidance describes; running it via Python in `Bash` was both the
  efficient shape and a small live test of the recommendation.

### Friction Log Entries Processed (second workstream)

- **2026-05-07 — Borrowing patterns from sibling NLAs requires
  reading the actual artifact** — resolved. `core/skills/think.md`
  Prior Art. Archived.
- **2026-05-07 — Plan agent conservatism is a calibratable input,
  not a verdict** — resolved. `core/skills/maintain.md` Confirm
  Before Implementing. Archived.
- **2026-05-06 — Bulk Edit calls don't parallelize when system
  reminders fire between each** — resolved. `core/skills/maintain.md`
  Common Maintenance Tasks. Archived. (Note: companion Claude Code
  feature request not filed — out of scope for framework maintenance.)
- **2026-05-04 — Multi-file maintenance: cross-references demand
  the referenced file ship first** — resolved.
  `core/skills/maintain.md` Pre-flight Review. Archived.
- **2026-05-04 — Resolved-but-unarchived log entries drift across
  sessions** — resolved. `core/skills/close.md` Step 2 +
  `core/skills/maintain.md` Session Start. Archived.

---

## Debrief

[To be added at session close via `/debrief` or in `/close`.]

## State at Close

[To be finalized at session close.]
