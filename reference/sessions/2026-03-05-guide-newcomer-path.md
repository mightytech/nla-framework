# Maintenance Session: Guide Newcomer Path

**Date:** 2026-03-05
**Status:** Complete

## Intent
Make `/guide` work as a first-touch experience for users who know nothing about NLAs.
The framework wrapper was written for maintainers only — the most important audience
(brand-new users) had no structured orientation path.

## Changes Made

### Framework guide wrapper — two-audience detection (blast radius: framework only)
- Updated `.claude/skills/guide/SKILL.md` to handle two audiences:
  - **Newcomers:** NLA concepts → framework purpose → what to do next (/create-app, /install-app)
  - **Maintainers:** architecture, skill catalog, working rhythms, pending items
- The core skill (`core/skills/guide.md`) was unchanged — domain projects unaffected.

### CLAUDE.md Default Mode — suggest /guide (blast radius: framework only)
- Default Mode section now suggests `/guide` for users wanting to understand before building.
- "If the user asks about the framework" guidance updated to match (caught by validation).

## Blast Radius
- Framework only. No core skill or intent file changes.

## Decisions Made
- **Wrapper, not core** — The newcomer path is framework-specific (no `app/overview.md`,
  different "what you can do from here"). Domain projects don't need this; their guide
  already has project context to work with.
- **Two audiences in one wrapper** — Rather than separate skills or modes, the wrapper
  gives the AI context for both audiences and relies on the core skill's "adapt to
  familiarity" posture to select the right one.

## What Didn't Work
- (nothing — small, contained change)

## Debrief
1. **User questions are the best gap-finders.** "Can I run /guide before /create-app?"
   is a question structural validation can't ask. Testing skills by imagining real user
   journeys surfaces gaps that consistency checks miss.
2. **Validation caught documentation drift.** The "If the user asks about the framework"
   line in CLAUDE.md was stale after updating Default Mode. Manual mirrors fall behind —
   the structural validator is good at catching these.
3. **Light sessions don't need full ceremony.** Two files, three edits, one validation
   pass. The discuss → implement → validate flow was the right weight.
4. **Audience detection in wrappers may generalize.** Startup could benefit from
   newcomer vs. returning-user detection. Worth watching, not acting on yet.
5. **Testing the newcomer path requires a fresh session.** Running /guide inside /maintain
   shapes the response toward maintainer context. True newcomer testing needs no prior
   conversation.

## State at Close
**What's working:** /guide now handles both newcomers and maintainers from the framework.
CLAUDE.md consistently points to /guide for orientation.

**What's pending (friction log — 4 items):**
- /create-app bare project path (minor, project generation)
- Should friction logs be gitignored? (needs /think)
- Framework maintain thin wrapper pattern (deferred)
- Context window awareness for session log nudges (deferred)

**What's pending (feedback log — 1 item):**
- Export hybrid approach: script for mechanical work, AI for judgment (needs /think)
