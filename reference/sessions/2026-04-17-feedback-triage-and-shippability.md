# Maintenance Session: Triage new feedback and implement shippability + tagged-release changes

**Date:** 2026-04-17
**Status:** In Progress

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

[To be captured at session close.]

## State at Close

[To be captured at session close.]
