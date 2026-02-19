# Maintenance Session: Duet Feedback Processing + Update Notes Design

**Date:** 2026-02-19
**Status:** Complete

## Intent

Process the 11-item feedback letter from Duet's first major maintenance session
(friction log entry 2026-02-14). Broaden the framework beyond its transformation-NLA
origins to support persistent, creative, and tool-using NLAs equally well.

## Changes Made

### Friction log 2b — /create-app post-creation guidance (commit 4fd5c5f)
- Added `/maintain` as development cycle guidance in post-creation steps
- Added complex project edge case (4+ tasks → skeleton + defer to `/maintain`)

### nla-foundations.md broadening (commit 25e9c00)
- **NLA Shapes** section: stateless, persistent, tool-using (items 1, 2, 3, 5, 7)
- **Cardinal Rule** broadened: "the human decides" replacing transformation-specific framing (item 11a)
- **Principle 6**: Configuration Is Natural Language (item 10)
- TK note references removed throughout, downstream alignment in intent files, README, maintain skill

### Update notes design + implementation (commits 26f6fd0, 58a7dc9)
- Designed `install/update-notes.md` — changelog for domain projects read by `/update`
- Key insight: non-determinism as feature; same notes, different proposals per project
- Implemented: file created with seed entry, `/update` reads notes as context, `/maintain` prompts for notes
- Commit hash made optional — date + Affects field do the real work

### Startup extensibility (commit 0d6b1b2)
- `app/startup.md` extension point — app-specific initialization without ejecting (item 4)
- Scaffold `/format-article` references removed (item 11b)
- Intent file descriptions updated, update note written

### Validate for non-deterministic NLAs (commit b5b0569)
- Process-focused validation guidance added to scenario walkthrough mode (item 11d)

### Output-spec.md conditional (commit ccc310f)
- Made optional throughout: startup, validate, maintain, create-app, intent files (item 6)
- Design rationale entry written
- Update note written

### Friction log entries added
- Pre-flight design review pattern (positive — caught gaps before implementation)
- README directory tree drift (process — recurring low-severity issue)
- Voice and values splitting + values as transparent ethics (major — deferred to future session)

## Blast Radius
- **All domain projects:** foundations changes, startup extensibility, validate guidance, output-spec conditionality, maintain skill updates
- **Project generation:** create-app changes, intent file updates, output-spec conditionality
- **Maintainers only:** design rationale entries, friction log entries, session log

## Items Remaining from Duet Letter
- **Item 8** (`/create-app` deeper questions): Addressed with light touch — added NLA shape
  as a conversation grouping in Phase B follow-ups. The AI explores persistence and tool
  use when the user's description is ambiguous. Full question flow deferred unless this
  proves insufficient.

## Decisions Made This Session
- Cardinal Rule reframed as "the human decides" — universal, not transformation-specific
- Update notes as context for judgment, not instructions to execute
- Commit hash optional in update notes — LLMs adapt when fields are missing
- Output-spec.md conditional, not mandatory — framework fits all NLA shapes
- Voice/values splitting deferred — bigger design, needs its own session

## State at Close
All 11 Duet feedback items resolved. The framework now supports stateless, persistent,
and tool-using NLAs with broadened foundations, extensible startup, conditional output-spec,
non-deterministic validation guidance, and an update notes system for propagating changes.

Three friction log entries added during the session: pre-flight design review (positive
pattern), README directory tree drift (recurring), voice/values splitting (deferred to
future session). The voice/values item is the most significant open question — it touches
on NLAs as vehicles for transparent, debatable ethics.
