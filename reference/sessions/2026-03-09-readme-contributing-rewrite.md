# Maintenance Session: README and CONTRIBUTING Rewrite

**Date:** 2026-03-09
**Status:** Complete

## Intent
Rewrite README.md and CONTRIBUTING.md to serve newcomers rather than existing users.
The README should be a landing page that makes the case for NLAs and motivates reading
the probe report — not a reference manual. The CONTRIBUTING should explain why NLA
contributions are observations, not pull requests. Both aligned with penny post's
README conventions.

## Changes Made
- **README.md rewritten** as a landing page. Leads with what NLAs are and why they
  matter, adds "Built With NLAs" section listing all seven applications plus
  whitepapers, drops reference-heavy sections (ejecting skills, adding domain skills,
  plugin export, key concepts) that existing users ask the AI about. Borrows penny
  post's patterns: two-path curious links, improvement loop, "ask the AI" help model.
- **CONTRIBUTING.md rewritten** using penny post's observation-over-PRs model.
  Explains why prose changes need reasoning not diffs, adds simulation via fork,
  appeal process, non-developer and multilingual contribution paths, blast radius
  awareness. Replaces the previous mechanical types-of-changes/testing guide.
- **Penny post letter sent** (Issue #10) noting two improvements penny post could
  adopt: the richer "What Is an NLA?" paragraph and the blast radius concept for
  CONTRIBUTING.

## Blast Radius
- README.md and CONTRIBUTING.md — framework documentation only, no downstream
  project impact

## Decisions Made
- **Audience is newcomers, not existing users** — existing users ask the AI for
  reference details. The README serves people arriving from the probe report or
  discovering the repo.
- **Probe report as motivational target** — the README should make people curious
  enough to read the report, not summarize it. Enough weight to intrigue, not satisfy.
- **Drop reference sections** — ejecting skills, adding domain skills, plugin export,
  key concepts all removed. These are "ask the AI" topics, not README material.
- **Align with penny post conventions** — borrow freely, note improvements for a
  letter rather than editing penny post directly.

## Debrief
1. **Penny post outpaced the framework's own presentation.** The downstream package
   had a better README and CONTRIBUTING than the origin project — simply because it
   was written more recently. Periodic comparison with packages is worth doing, not
   just the reverse.
2. **The /think phase was lightweight but essential.** A few exchanges identified the
   key insight: "existing users just ask the AI." That one sentence unlocked the
   whole rewrite by clarifying what to drop.
3. **The probe report as external context changed what was possible.** Reading it
   before drafting provided language and examples (spam filter, package manager in
   prose) that couldn't have come from the framework's own files. The README is
   better because it had a source of conviction beyond internal documentation.
4. **The letter wrote itself.** With observations already articulated during the
   /think session, the penny post letter was just packaging. The improvement loop
   working as designed.

## State at Close
**What's working:** README and CONTRIBUTING rewritten, committed, and aligned with
penny post conventions. Penny post letter sent (Issue #10).

**What's pending:** 3 friction log entries pending (startup auto-invocation, bare
project path, friction log git storage). 2 deferred (maintain thin wrapper, context
window awareness). 1 feedback item (export hybrid approach). Same as session start —
this session didn't touch any of them.

**Where to pick up:** The probe report link in both README and penny post currently
points to the framework repo — update when the report has its published URL.
