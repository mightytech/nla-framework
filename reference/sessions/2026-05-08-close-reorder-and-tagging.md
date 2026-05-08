# Maintenance Session: /close Reorder and Tagging Refinement

**Date:** 2026-05-08
**Status:** In Progress

## Intent

Restructure the `/close` skill so its steps run in dependency order — validation,
mirrors, and debrief produce content that needs to land in the session log, so the
log is finalized later, not first. Then refine the Shippability convention to
separate *what counts as tag-worthy* (consumer-facing content, unchanged) from
*when the tag goes on* (push moment — typically session end via `/close`, not
per-commit). One session of consumer-facing work produces one tag.

This resolves friction log entry 2026-04-18 (per-commit tagging inflates version
numbers without making each tag more meaningful).

## Changes Made

- **`core/skills/close.md`** — restructured the body to a 5-step order:
  validation → mirrors → debrief → session log → commit + tag + push. The
  former "Loose Ends" container dissolves; its contents are now first-class
  steps in dependency order. Step 5 includes tag-decision logic
  (review consumer-facing commits since the last tag; tag HEAD if any).
  Tag fires only at push, not at session end without push.

- **`core/skills/maintain.md`** — refined the Shippability section to split
  *what counts as consumer-facing* (the classification, unchanged) from
  *when the tag goes on* (now: at push moment, typically session end).
  Update-notes entries continue to land per-commit; tags batch.

- **`reference/design-rationale.md`** — added a 2026-05-08 refinement note to
  the existing Shippability entry recording the per-commit → per-push shift.

- **`reference/friction-log.md` / archive** — resolved and archived the
  2026-04-18 entry.

- **`install/update-notes.md`** — added a 2026-05-08 entry alerting
  downstream projects to the new `/close` order and the changed tag cadence.

## Decisions Made

- **Tag at push, full stop.** If a session ends without push, no tag fires
  during that session — the next push (whenever it happens) tags whatever
  consumer-facing work has accumulated. Rationale: tags are for consumers,
  so unpublished tags are noise.

- **Validation stays conditional in step 1.** It runs only when structural
  changes warrant it. Reflexive validation runs would dilute the signal.

- **Step 5 commit shape is judgment, not procedure.** A single coherent
  "session close" commit is fine when the close work is small; separate
  commits when the close-work changes are substantial enough to merit
  independent review. The skill doesn't dictate.

- **Cross-referenced files land together.** The 2026-05-04 friction entry's
  update note prefers single-commit atomicity for cross-references over
  ordering discipline. `close.md` and `maintain.md` reference each other
  through the Shippability rule, so they ship in one commit alongside the
  design-rationale, friction log, and update-notes changes.

## Friction Log Entries Processed

- 2026-04-18 "Shippability convention reads as per-commit tagging;
  session-end is better" — resolved, archived. The convention now
  separates what-is-tag-worthy from when-the-tag-goes-on.

## Notes on the Implementation

- **Cross-reference path in `close.md` step 5.** Initial draft used
  `packages/nla-framework/core/skills/maintain.md` directly. That path
  only resolves from a domain-project perspective. Fixed to give both
  paths (domain project vs. framework's own /close), matching the
  pattern used in maintain.md's foundations reference.
- **`/install` and `/update` tag-check compatibility.** Verified the
  tag-check flows in those skills (Pin to a Tagged Release; fast-forward
  tag offer) benefit from fewer, more meaningful tags. Per-push tagging
  improves that path rather than breaking it.
- **Section heading kept.** maintain.md's "Shippability at Commit Time"
  section retains its header even though the *when* sub-section now
  discusses push-time. Rationale: the consumer-facing classification
  still anchors at commit time (it drives update-notes entries), and
  changing the header would create churn in cross-references.

## Debrief

(To be filled at close.)

## State at Close

(To be filled at close.)
