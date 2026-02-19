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

## Addendum: Post-Session Learning Capture

After closing the session, a reflective review identified 7 meta-learnings about how NLAs
fail, how maintenance works, and how the framework should evolve. These were captured into
permanent homes: foundations (language note), validate-architecture (language breadth
category), maintain (three principle enrichments), design-rationale (lessons entry),
friction-log (pattern #4), and update-notes (entry for domain projects). See commits
464b618 (core files) and bd32ac6 (reference docs + update notes) for the full changes.

## Addendum: Remove /plan Skill

Following the learnings capture, analysis of the session revealed that the framework's `/plan`
skill was never invoked — its NLA design thinking concepts were used through `/maintain`, and
Claude Code's built-in plan mode handled implementation planning. Decision: remove `/plan` as
a standalone skill, fold its unique content (structure gradient, learning loop design) into
`/maintain`, and let Claude Code plan mode handle implementation planning.

This is the first framework skill removal, requiring enriched `/update` guidance for domain
projects. The config-spec "Plan first" option is reframed to reference planning mode generally
rather than the removed skill. Full plan in `.claude/plans/expressive-herding-lemon.md`.

Implemented in commits 497b1bf (fold + remove + update references) and 61f801c (update
mechanism + notes + rationale).

## Addendum: Post-Implementation Validation

Ran `/validate` with both structural check and architecture review as a post-implementation
verification and a test of the validate skill itself.

**Structural check:** Clean. Confirmed /plan removal left no dangling references. All skill
tables match, all thin wrapper targets resolve, all file references valid. Found 2 low-severity
items (update-notes-archive.md forward reference, README tree incomplete).

**Architecture review:** 18 findings (3 fix, 9 improve, 6 note). Recurring theme: documentation
artifacts that mirror filesystem state drifting after changes (README tree, core/skills README
table, structure-intent directory tree). Language breadth assessment confirmed clean — no
remaining transformation-specific language in shape-neutral contexts.

All 12 actionable findings fixed in commit 2504ace. Key changes: README directory tree now
reflects all 10 skills and reference contents, validate dispatcher uses relative paths,
core skills note they assume domain project context, skills-intent clarifies extension
package management, CLAUDE.md flags penny-post as optional.

## Final State

The framework is current. All Duet feedback processed, meta-learnings captured, /plan removed,
validation run, findings resolved. Open items for future sessions: voice/values splitting
(friction log), update-notes-archive.md (create when needed).
