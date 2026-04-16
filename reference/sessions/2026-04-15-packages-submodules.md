# Maintenance Session: Packages Directory with Git Submodules

**Date:** 2026-04-15
**Status:** Complete

## Intent
Replace the sibling directory convention (`../nla-framework/`, `../nla-package/`) with a
`packages/` directory using git submodules within each NLA project. This solves the
cross-directory permission friction, adds version pinning, makes projects self-contained,
and simplifies the new user experience.

## /think Session Summary

### Origin
During /check-feedback triage of permission test results (#15, #16), a lateral idea
emerged: rather than fixing the permission pattern matching (relative vs. absolute paths),
eliminate cross-directory reads entirely by putting dependencies inside the project.

### Threads Explored (via /unpack)

1. **Permission resolution** — Solved. All reads within-project, no prompts.
2. **CLAUDE.md isolation** — Safe. Subdirectory CLAUDE.md files don't auto-load.
3. **Development workflow** — Non-issue. Develop in source repos, consume via submodules.
   Enforces Context Determines Competence.
4. **Framework's own packages** — Self-consistent. Framework eats its own dog food.
   Circular dependencies work (no build step, no resolution needed).
5. **Update model** — Strictly better. Ambient → explicit. Version pinning, atomic
   commits, trivial rollback. `/update` owns all submodule commands.
6. **New user experience** — Improved. Self-contained projects.
   `git submodule update --init` gives a complete working copy.
7. **Path migration** — Mechanical. `../nla-framework/` → `packages/nla-framework/`
   everywhere. Framework migrates first. Required (no transition period — single user).
8. **Permission model obsolescence** — Retire cross-directory permission machinery.
   Keep design rationale with supersession note.

### Key Insights

**Circular dependencies work in NLAs.** The framework depends on penny post; penny post
depends on the framework. In traditional software, this is a build-order problem. In NLAs,
there's no build step — the LLM reads files from paths. Each project pins its own version
of the other. No resolver needed. (Fits the "absurd things that work" pattern.)

**Flat, not nested dependencies.** `git submodule update --init` (without `--recursive`)
clones only direct dependencies. No transitive dependency resolution. If package A needs
package B, the consuming NLA lists both as direct dependencies — they're siblings in
`packages/`.

**The ambient update model was a hidden danger.** `git pull` on a shared sibling changed
behavior in every project simultaneously. Version pinning means each project runs exactly
what it was tested with. The apparent convenience was actually a liability.

## Decisions Made

- **Directory name:** `packages/`
- **Mechanism:** git submodules
- **Clone depth:** shallow (dependencies don't need full history)
- **URL format:** HTTPS in `.gitmodules` (portable)
- **Init convention:** `git submodule update --init` (not `--recursive`)
- **Migration:** required, no transition period
- **Framework migrates first** as test case
- **Permission management model** for cross-directory reads: retired
- **External data directories** (e.g., Duet's `../duet-music/`): project-specific, not a framework decision
- **Tag-aware updates:** `/check-updates` reports available tagged releases; `/update` offers advancing to a tag vs. HEAD
- **Tagged as v0.0.1** — first packages/submodules release

## Changes Made
- **Git submodules added** — `packages/nla-penny-post/` and `packages/nla-process-helpers/` as shallow submodules
- **Framework skill wrappers** — all 6 package-delegating wrappers updated to `packages/` paths
- **CLAUDE.md** — Key Files table updated
- **Core skills** — all `../nla-framework/` paths updated to `packages/nla-framework/`; permission machinery retired from startup, validate-structural, install, update, check-updates
- **Intent files** — all 5 intent files updated (skills-intent, CLAUDE-intent, structure-intent, install.md, package-intent); permission declarations simplified to Bash patterns only
- **Create-app skill** — generation flow now includes git init + submodule add; settings simplified; narration updated
- **Install-app skill** — added submodule init step
- **Design rationale** — supersession notes on 3 existing entries; new "Packages Directory with Git Submodules" entry
- **README.md** — getting started, thin wrappers, directory trees, upgrading all updated
- **Update notes** — new entry with migration steps for domain projects
- **Friction log** — "settings.local.json accumulates junk" resolved
- **Installed-packages.md** — all package paths updated
- **Tag-aware updates** — check-updates reports tagged releases; update offers tag vs. HEAD choice
- **Tagged v0.0.1** and pushed to remote
- **Feedback triage** — all 10 open issues triaged, commented, closed. 8 accepted (including 2 adapted), 4 deferred, 1 declined. Feedback log entries created for all accepted items.
- **Foundations enriched** — principle #4 rewritten as "Intent Over Rules" with identity-description pattern; principle #2 enriched with diagnostic insight; principle #6 (Cardinal Rule) rewritten with three-beat structure (consequences, perspective, capability); improvement loop gains diagnostic beat
- **/think posture strengthened** — "question the frame" and "bring unexpected connections" added
- **/close convention** — State at Close now distinguishes context from actionable decisions
- **Friction log guidance** — "Confirmed reason" field strengthened with diagnostic emphasis
- **Session-checkpoint promoted** — new core skill from facebook-moderation, with timing insight
- **Tagged v0.0.2** — feedback triage and foundations enrichment

## Blast Radius
- `install/` intent files: project generation convention changes
- `core/skills/`: path references in update, check-updates, install, startup
- `.claude/skills/`: framework wrapper paths, create-app generation logic
- `CLAUDE.md`: Key Files table
- `reference/design-rationale.md`: new entry, supersession of sibling convention and permission model
- All domain projects: migration via `/update`

## What Didn't Work
- (Nothing — the /think session proceeded cleanly from premise checks through implications)

## Friction Log Entries Processed
- "settings.local.json accumulates junk" — resolved by architectural change (no more
  cross-directory reads), not by fixing the generation pipeline

## Debrief
- The /think → /unpack combination worked well for the architecture change — 8 threads, resolved sequentially, clear go/no-go gating on premise checks before investing in downstream threads.
- The "lateral idea during triage" pattern: checking feedback surfaced data (permission test results) that prompted a design question bigger than the feedback itself. The framework correctly paused triage to explore the design question.
- The circular dependency insight is worth capturing beyond the design rationale — it's an "absurd thing that works" that demonstrates the NLA paradigm.
- Plan agent was effective for the migration scope — the implementation was largely mechanical once the design was settled. No cross-project edit issues this time (lesson learned from 2026-03-04).
- /unpack for the feedback triage was the right call — 16 items across 6 issues, each getting individual attention, with the human pushing back on verdicts that were too conservative (principle #4 strength, human flourishing, session-checkpoint as alternative to session splitting). Item-by-item triage produced better verdicts than batch assessment would have.
- The session-checkpoint skill was tested live during the triage and worked — re-reading foundations before reasoning about where accepted items would land was genuinely useful. The timing insight from the compiler (checkpoint before reasoning, not after finishing) was validated firsthand.
- The human flourishing discussion produced the richest design work of the triage. The three-beat Cardinal Rule (consequences, perspective, capability) and the "limitations are an asset" framing emerged from collaborative exploration, not from the feedback item alone. The item proposed a concept; the conversation produced a design.
- The "aspirational gradient" insight applies broadly: the AI won't achieve true lateral thinking, but aspiring to it produces better frame-questioning as a side effect. Same pattern as "artistry produces understanding."
- **The /think → triage → implement pipeline compressed well.** A design question emerged mid-triage, got a full /think session, got planned and implemented, then triage resumed — all in one session. The framework's skills composed naturally: /think for design, /unpack for triage structure, /session-checkpoint for context refresh, /close for wrap-up. This session demonstrated the skills working together rather than in isolation.
- **The human's lateral contributions were the highest-value moments.** The packages/submodules idea, the session-checkpoint file, the "limitations are your contribution" frame, the human flourishing concept, "aspirational engineering." Each came from the human bringing a perspective the AI wasn't reaching for — exactly what the enriched Cardinal Rule now describes. The session is evidence for its own principles.
- **Scope grew organically but stayed coherent.** Started as /check-feedback, expanded to an architecture change, expanded to foundations enrichment, added a new skill, added a design principle. Each expansion was the human's choice and built on what came before. Session log and checkpoints kept it trackable.
- **"Aspirational engineering" emerged from conversation, not feedback.** The feedback item (#18.3) proposed "human flourishing." The conversation turned it into an operative principle with evidence and mechanism. Then the naming — "aspirational engineering" — crystallized a pattern that had been appearing across multiple items (lateral thinking, artistry, flourishing). The most important design work in this session happened in conversation, not in any skill or plan.

## State at Close

### Context for next time
- v0.0.2 tagged and pushed. Framework is current.
- The facebook-moderation project has been an exceptionally productive feedback source — 6 letters, 16 items, empirically grounded. The compilation workflow is producing transferable insights.
- The packages/submodules model is live in the framework but not yet propagated to any other projects.

### Decisions awaiting implementation
- **Propagate packages migration** — penny-post and process-helpers first (they're packages others consume), then domain projects. Each in their own session.
- **Close unanswered permission test issues** (process-helpers#1, claude-code#1, duet#2) — during each project's migration session.
- **Bring NLA writing standards into framework** — copy from facebook-moderation, review framework docs against them, integrate with /validate and /maintain. Detailed steps in feedback log.
- **Export hybrid approach** — pre-existing pending item, needs /think session.

### Where to pick up
Migrate penny-post and process-helpers to packages/submodules model (in their own sessions). Then domain projects. Writing standards is the next framework-side work after migrations are done.
