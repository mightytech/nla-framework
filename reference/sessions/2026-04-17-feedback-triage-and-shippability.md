# Maintenance Session: Triage new feedback and implement shippability + tagged-release changes

**Date:** 2026-04-17
**Status:** Complete

## Intent

Triage two new GitHub Issues (#22 shippability distinction, #23 tagged-release
check + settings drift), then implement the three accepted items. All three came
from the first real field reports on the packages/submodules migration: penny-post
caught a scaling problem with update noise; process-helpers caught a silent tag
mismatch during their own migration plus a narrower permission-drift residual.

## Changes Made

- Triaged Issues #22 and #23; deposited three pending entries in feedback-log.md.
  Posted triage comments and closed both issues.
- **#22 Shippability convention — implemented.** Principle in
  `reference/design-rationale.md` (universally framed across project types),
  commit-time procedure in `core/skills/maintain.md` (affecting all domain
  projects via thin wrappers), package-specific pointer in
  `install/package-intent.md`, and an update-notes entry announcing the
  convention. Entry moved from feedback-log.md to feedback-log-archive.md.
- **#23 Item 1 (initial-add tag check) — implemented.** Added "Pin to a
  Tagged Release" subsection to `core/skills/install.md` with prompt wording
  mirrored from update.md's advance path. Added "For new intents that add a
  submodule" bullet to `core/skills/update.md` Phase 2 Apply Changes,
  cross-referencing install.md. Added step 1a to `.claude/skills/create-app/SKILL.md`
  for the framework-submodule tag check during project creation. Update-notes
  entry announces the change. Entry moved to archive.
- **#23 Item 2 (settings drift doc note) — implemented.** Added "Drift over
  time" paragraph to the `.claude/settings.local.json` description in
  `install/structure-intent.md` explaining Claude Code's auto-approve-and-record
  loop so maintainers recognize and don't misattribute the pattern. Heavier
  options (/close drift nudge, /validate baseline-diff mode) remain deferred.
  Update-notes entry written. Entry moved to archive.
- **#21 NLA writing standards — Phase 1 complete.** Created
  `reference/standards/` subfolder (anticipating future standards types per
  four 2026-04-16 friction entries). Landed `reference/standards/nla-writing.md`
  (adapted from facebook-moderation, ~420 lines after dropping the three
  facebook-moderation-specific meta-sections and generalizing examples /
  empirical citations). Added "Writing Standards" section to both
  `core/skills/maintain.md` (domain-project-facing) and the framework's own
  `.claude/skills/maintain/SKILL.md` (with path adjusted for each context).
  Update-notes entry written. Feedback log entry updated to show Phase 1 done,
  Phases 2–3 pending; not archived yet because the full multi-phase work isn't
  complete.

## Blast Radius

- #22 changes: `core/skills/maintain.md` (all domain projects), `install/package-intent.md`
  (packages), `reference/design-rationale.md` (maintainers).
- #23 Item 1 changes: `core/skills/install.md` and `core/skills/update.md` (all domain
  projects via thin wrappers); `.claude/skills/create-app/SKILL.md` (framework's own
  skill, affects new-project creation going forward).
- #23 Item 2 changes: `install/structure-intent.md` (read by /install and /update in
  all domain projects).
- #21 Phase 1 changes: `core/skills/maintain.md` (all domain projects) adds a pointer
  to the standards file; `.claude/skills/maintain/SKILL.md` (framework-internal)
  parallel pointer; `reference/standards/nla-writing.md` (framework-internal reference
  content; shipped inside the packaged submodule so domain projects can access via
  `packages/nla-framework/reference/standards/nla-writing.md`).

## Decisions Made

- **Shippability principle universal, not framework-specific** — decided during
  #22 implementation. Design-rationale framing generalized across project types;
  maintain.md procedure applies to all domain projects via thin wrappers.
- **Standards subfolder `reference/standards/` rather than flat
  `reference/nla-writing-standards.md`** — decided during #21 Phase 1 planning.
  Cost is low; four pending friction entries (Python standards, Fallingwater-style
  prose preamble, /maintain prose-vs-code mode, long-term nla-compiler re-compile)
  already anticipate multiple future standards types. Subfolder sets the
  organizational pattern before retroactive reorganization becomes costly.
- **Subfolder named `standards/`, not `implementation-standards/`** — the
  facebook-moderation naming distinguishes code-gen standards from other reference
  material. The framework is mostly prose; that distinction doesn't carry the
  same signal. `standards/` is cleaner.
- **Phased #21 delivery (Phase 1 this session; Phases 2–3 deferred)** — the
  original Issue #21 has four items (bring in, review, curate by findings,
  integrate). Review + curate + deeper integration are session-sized efforts of
  their own; attempting all four at once risked rushing. Phase 1 delivers a
  usable artifact + minimal pointer without pre-committing to findings.
- **Empirical citations in the standards file softened to qualitative** —
  specific facebook-moderation metrics (~97% agreement, 28+ compilations) replaced
  with qualitative claims in context. The quantitative citations don't strengthen
  the standards for framework readers who can't verify them; the qualitative
  findings carry the substance.
- **nla-foundations.md principle #2 phrasing flagged for Phase 2** — the standards'
  stronger reframe ("NLA documents are source code, not documentation") vs.
  foundations' current "The Documentation Is the Application" is a potential
  upgrade. Not touched in this session to avoid bundling foundations edits with
  the standards-introduction work. Noted in feedback log entry as Phase 2
  consideration.

## Decisions Made

- **Shippability principle belongs universally, not just framework-specific.**
  Initial framing positioned the convention as framework/package-only (because
  the noise problem was flagged by projects with live `/update`-consumers).
  User pushed back: the underlying distinction between consumer-facing and
  internal content applies to every NLA — domain projects export as plugins,
  and the same split (reference/ excluded, app/skills/CLAUDE.md shipped) holds.
  Revised placement: principle in design-rationale framed universally;
  procedure in `core/skills/maintain.md` (all domain projects); package-specific
  pointer in `install/package-intent.md` as an application of the general rule.

## What Didn't Work

- (Nothing yet.)

## Friction Log Entries Processed

- (This session is processing feedback log items, not friction log items.)

## Feedback Log Entries Processed

- #22 (shippability) — in-progress
- #23 item 1 (initial-add tag check) — pending, this session
- #23 item 2 (settings drift doc note) — pending, this session

## Debrief

Three observations from this session (no explicit `/debrief` conversation; AI-selected):

- **Recursive application of the shippability convention on its own
  implementation worked cleanly.** I codified the rule, then applied it to
  every subsequent commit of the session. The "touches both buckets → treat
  as consumer-facing" clause kept coming up in practice — the writing
  standards commit mixed internal (`reference/standards/` new directory)
  and consumer-facing (`core/skills/maintain.md` pointer, `install/update-notes.md`
  entry) changes, and the rule produced the right classification without
  needing to re-reason. Shipping a convention that applies to its own
  implementation turns out to be a good stress test.

- **User pushback on framing twice produced broader-and-better outcomes.**
  My initial framings were too narrow in both cases: shippability as
  framework/package-specific (→ corrected to universal across project types),
  standards as a flat file in reference/ (→ corrected to a subfolder
  anticipating future standards types). Pattern worth noting: when the
  user's instinct is "this seems too narrow," they're usually right. The
  friction log had signals I hadn't weighted properly (four 2026-04-16
  entries anticipating multiple standards types) — the subfolder decision
  was there in the data; I just didn't connect it until pushback forced
  the re-read. Worth being more suspicious of my own "start small" reflex.

- **Phased delivery for #21 preserved multi-session coherence.** The
  in-place feedback-log entry update (Phase 1 complete / Phases 2–3
  pending, with explicit scope for each) is more informative than either
  "archive it, open a new entry for Phase 2" or "leave the whole thing
  pending without status." Future sessions picking up Phase 2 will read
  the entry and know exactly what's done, what's left, and where to start.
  The convention in the close skill about "context vs. decisions awaiting
  implementation" applied at the feedback-log level too.

## State at Close

### Context for next time

- **Framework at v0.0.4** after this session's push + tag. Four commits
  since v0.0.3, all consumer-facing. Tag applied to the writing-standards
  commit (cd27c25) per strict shippability (session-log finalization commit
  rides above without a tag).
- **Writing standards available at `reference/standards/nla-writing.md`** —
  420+ lines, 33 standards, 9 sections, adapted from facebook-moderation.
  `reference/standards/` subfolder ready for future standards types.
- **`/maintain` (both core skill and framework's own wrapper) now includes a
  Writing Standards section** pointing at the file. Lightweight pointer, not
  full integration — that's Phase 3.
- **Shippability convention live.** Every commit decision since it landed has
  applied it. Framework's next natural cross-reference cleanup commits
  (updating `../nla-penny-post/` → `packages/nla-penny-post/` in
  framework-internal files) are now cleanly classifiable.
- **Three friction entries confirmed still-pending:** the four 2026-04-16
  entries (Python standards, Fallingwater-style prose preamble, /maintain
  prose-vs-code mode distinction, long-term re-compile-export.py experiment)
  all pair thematically with #21 Phase 2. Best addressed together or in
  sequence.

### Decisions awaiting implementation

- **#21 Phase 2: two-pass review of framework docs against writing standards.**
  Scope planned this session. Pass 1 (behavioral gaps, standards 2.3 / 2.4 /
  8.3) on ~10-12 high-risk operative docs: `core/nla-foundations.md`,
  `CLAUDE.md`, `core/skills/{maintain,startup,validate,validate-*,export,update,install,close}.md`,
  one sample posture-focused skill (probably `think.md`), possibly
  `.claude/skills/create-app/SKILL.md`. Pass 2 (craft refinements, 4.2 / 4.4 /
  3.5) broader — all core skills + intent files. User prefers a single-session
  sweep so learnings carry forward; checklist structure drafted but not
  materialized.
- **#21 Phase 3: deeper integration.** `/validate` mode using standards
  diagnostically; richer `/maintain` writing guidance beyond the pointer.
  Best done after Phase 2 so the review tells us which standards pull the
  most weight.
- **Potential `nla-foundations.md` principle #2 reframe.** The writing
  standards' "NLA documents are source code, not documentation" framing is
  stronger than foundations' current "The Documentation Is the Application."
  Flagged in the #21 feedback entry as a Phase 2 consideration. Small,
  focused edit; could land in the same session as the Pass 1 review or
  separately.
- **2026-04-16 friction entries** (Python standards, Fallingwater-style
  prose preamble, /maintain prose-vs-code mode, re-compile-export.py
  experiment) — pair with Phase 2 work thematically. Best addressed after
  Phase 2 has produced concrete findings.
- **Propagate packages migration** (penny-post, process-helpers, then domain
  projects) — still pending from the 2026-04-15 session; unchanged.
- **Close permission-test issues** (process-helpers#1, claude-code#1, duet#2)
  — still pending from 2026-04-15; unaffected by this session.

### Where to pick up

**Immediate:** Phase 2 of #21. The user's preference is a single-session
sweep for context coherence. Fresh context will help — the review is
judgment-bearing work that benefits from standards-file fluency.

**Medium:** Phase 3 of #21 once Phase 2 findings clarify which integration
surfaces to prioritize.

**Long:** The four 2026-04-16 friction entries, in whatever sequence makes
sense after Phase 2 produces findings.
