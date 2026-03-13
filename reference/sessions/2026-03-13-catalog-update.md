# Maintenance Session: Catalog Update — nla-claude-code and Complexity Rename

**Date:** 2026-03-13
**Status:** Complete

## Intent
Add nla-claude-code to the example catalog and revise complexity terminology to
better reflect application complexity rather than user experience difficulty.

## Changes Made
- **Added Claude Code Manager** to `install/example-catalog.md` — Moderate complexity,
  with GitHub repo link. Catalog now has six entries.
- **Renamed complexity scale** from Starter/Advanced to Low/Moderate — the old terms
  implied user difficulty rather than application complexity. The new scale also avoids
  overstating complexity relative to mature traditional software in these domains.
- **Reclassified Office Hours** from Moderate to Low — it's a conversational companion,
  not a multi-part system.
- **Reordered entries** by complexity (Low → Moderate) for readability.

## Blast Radius
- `install/example-catalog.md` — affects what `/install-app` offers

## Decisions Made
- Low/Moderate instead of Low/Moderate/High — nothing in the current catalog warrants
  "High" when compared to mature traditional apps in those domains. The scale can
  expand when something earns it.
- Dividing line: Low = single-purpose or stateless; Moderate = multiple moving parts
  (persistence, tool use, packages, cross-project workflows).

## Debrief
1. The complexity terminology discussion was valuable — "Starter" and "Advanced" were
   subtly misleading, framing examples as a learning progression rather than describing
   the applications themselves.
2. Calibrating against traditional software (Pro Tools, real ticketing systems) was the
   key insight that kept the scale honest.

## State at Close
**What's working:** Example catalog updated with six entries and clearer complexity scale.

**What's pending:** Same friction/feedback items as previous session — 3 pending
friction entries, 2 deferred, 1 feedback item. None touched this session.

**Where to pick up:** The `/think`-requiring items (startup auto-invocation, friction
log git storage, export hybrid approach) remain the next substantive work.
