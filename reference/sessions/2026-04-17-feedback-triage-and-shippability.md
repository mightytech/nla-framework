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

## Blast Radius

- #22 changes: `core/skills/maintain.md` (all domain projects), `install/package-intent.md`
  (packages), `reference/design-rationale.md` (maintainers).
- Additional changes: TBD as each lands.

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
