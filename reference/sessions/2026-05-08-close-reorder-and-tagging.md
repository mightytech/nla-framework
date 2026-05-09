# Maintenance Session: /close Reorder and Tagging Refinement

**Date:** 2026-05-08
**Status:** Complete

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

Held during this session's `/close` (no separate /debrief earlier). The
maintainer reviewed four observations and judged them worth keeping in the
session log but not worth promoting to friction log entries.

- **Single-commit cross-reference resolution held up again.** The 2026-05-04
  friction entry's update note proposed single-commit atomicity as the
  preferred path for cross-referenced files; the 2026-05-07 structure
  decisions session was the first confirmation, and this session is the
  second. `close.md` ↔ `maintain.md` ↔ design-rationale ↔ archive ↔
  update-notes all landed in commit 4252be5 with no interim broken
  references. The pattern is durable enough now that the original 2026-05-04
  entry's "write referenced files first" fallback is rarely the natural path
  — single-commit is.

- **Dogfooding `/close` in the same session worked as intended.** The new
  step order shipped at commit 4252be5, then ran immediately. Step 1 (skip
  validate — content-only session) and step 2 (mirrors clean — no new
  skills/intent files) fired correctly. Step 3 (debrief before session log
  finalization) is the dependency the reorder was designed for. Notable that
  the dogfood suggestion came from the maintainer ("should we try out the
  new /close?"), not the AI — the user pulled the change into immediate use
  rather than deferring to a future session.

- **Two-hop path issue caught during author-time re-read, not from
  maintainer.** Step 5's tag-decision section initially wrote
  `packages/nla-framework/core/skills/maintain.md` directly, which only
  resolves from a domain-project perspective. The catch happened during the
  post-edit coherence re-read by recalling the maintain.md foundations-
  reference pattern (which gives both paths). Recurring concern (friction
  log "Patterns to Watch" #2). The catch was right and at the right time;
  the question this raises is whether author-time review of core skills
  could include a more reliable check for dual-context paths than
  pattern-recall. Not promoted to its own friction entry — the system
  worked.

- **Summarizing the current skill before proposing a change was useful
  priming.** The maintainer's first ask was a summary of `/close`'s current
  steps in order; that made the proposed restructure concrete rather than
  abstract, with the contrast visible side-by-side. Worth noting as a small
  technique: when proposing a structural change to an existing skill, the
  "summarize current behavior first" move tends to make both sides crisper.

- **Annotated-tag gotcha caught after first push.** The first attempt to
  push v0.0.8 used `git tag v0.0.8` (lightweight), which `git push
  --follow-tags` skipped silently. Caught only because I verified the tag
  on remote. Recreated as annotated (`git tag -a`) and pushed explicitly.
  The maintainer suggested fixing `close.md` immediately — adding an
  annotated-tag instruction to step 5's tag-decision section — and
  retagging v0.0.8 to the doc-fix commit (no consumers had pulled yet).
  Done in commit (this commit), retagged. The catch and fix in the same
  session is the dogfood validating itself a second time: the new design
  surfaced the gap, and the gap got closed before it could trip anyone
  else.

## State at Close

### What's working

- `/close` runs in the new dependency order (validate → mirrors → debrief
  → log → commit + tag + push). First dogfood run completed as designed.
- Shippability rule splits *what counts as consumer-facing* (commit-time)
  from *when the tag goes on* (push-time). This session's commit (4252be5)
  is consumer-facing; tag fires when this `/close` reaches step 5 push.
- Friction log: 11 pending + 2 deferred (down from 12 + 2 at session
  start). 2026-04-18 resolved and archived.

### Context for next time

- The new `/close` order is live framework-wide. Domain projects pulling
  via `/update` will see the change after they advance their submodule
  pointer past commit 4252be5. The update-notes entry walks them through
  the practical implications (especially the changed tag cadence).
- Tag cadence is now per-push. Multi-commit sessions produce one tag at
  push, not one per consumer-facing commit. Sessions that end without a
  push produce no tag.

### Decisions awaiting implementation

None from this session — all proposed changes shipped in commit 4252be5.

### Where to pick up

- **Cluster A (maintain.md polish bundle)** remains the tempting next
  target: 2026-05-07 (Plan agent calibration), 2026-05-06 (bulk Edit
  parallelism), 2026-05-04 (cross-reference ordering — now partially
  evidenced by this session's single-commit atomicity), 2026-05-04
  (resolved-but-unarchived check at /close). Each is small; together they
  could be one focused session.
- **Deferred publication arc** for the structure decisions protocol
  (`reference/plans/structure-decisions-publication.md` to draft) still
  sits, independent of the friction queue.
