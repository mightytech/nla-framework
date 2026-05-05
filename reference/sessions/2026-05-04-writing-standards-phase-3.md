# Maintenance Session: Writing Standards Phase 3

**Date:** 2026-05-04
**Status:** Complete

## Intent

Bring the NLA writing standards into active use through two complementary
integrations: author-time use during `/maintain` editing, and on-demand
retrospective review through a new `/validate standards` mode. Phase 1
(2026-04-17) brought the standards file into the framework with a
lightweight pointer in `/maintain`. Phase 2 (2026-04-18) ran two manual
review passes that empirically validated the standards' diagnostic value.
Phase 3 operationalizes that diagnostic value: author-time so docs land
right the first time, retrospective so existing docs (much of which
predate the standards) can be reviewed against them on demand and again
as the standards evolve.

## Approach

The /think exploration converged on a two-piece shape with an explicit
iteration posture:

**Author-time integration in `/maintain`:** Targeted-load — when editing
operative docs, identify the doc type, read section 2 (document
fundamentals) plus the matching 8.x subsection. Doc-type-aware loading
avoids burning context on every edit while keeping the high-leverage
standards in the room. Starting with targeted rather than always-load is
the lighter starting position; if the targeted approach keeps missing,
`/validate standards` catches the gaps and signals when to escalate.

**New `/validate standards` mode:** Retrospective review modeled on
Phase 2's flow. Scope-configurable — user picks docs and standards
subset. Defaults focus on 2.3 (produces what it contains) and 4.4
(cross-references with context), Phase 2's empirically most-diagnostic
standards. Output is a findings file in `reference/sessions/`, matching
`validate-architecture.md`'s pattern, then routed through `/validate`'s
existing disposition step (fix-now / defer to friction log / wont-fix).

## Decisions Made

- **Three modes collapsed to two.** Initial framing distinguished
  prospective (before drafting) / current (during drafting) /
  retrospective (after drafting). Conversation collapsed prospective and
  current to **author-time** — the value is standards in the room while
  writing, not a pre-edit reading ritual. Two modes that matter:
  author-time and retrospective. — Rationale: prospective awareness
  without operational use is hollow; current is what produces the value.

- **`/validate standards` over `/validate writing` or enhancing
  `/validate debug`.** Debug is reactive to a specific observed bug;
  standards review is proactive against the standards. Different
  diagnostic question. "Standards" is more accurate than "writing"
  (which suggests grammar/style). — Rationale: name should match the
  diagnostic question.

- **Targeted-load over always-load for /maintain.** When editing
  operative docs, read section 2 + the matching 8.x subsection rather
  than the full 738-line standards file. — Rationale: targeted is the
  lighter starting position; always-load is the conservative fallback if
  the targeted approach keeps missing. The /validate standards mode
  catches gaps and provides the escalation signal.

- **Default standards subset for /validate standards: 2.3 + 4.4.**
  Phase 2's empirical findings: 2.3 surfaced most behavioral gaps; 4.4
  is the most discrete, gremmable pattern. — Rationale: defaults should
  reflect what produced findings.

- **New mode is a sub-mode of /validate, not a top-level skill.**
  Follows the existing validate-* pattern (architecture, coherence,
  debug, scenario, structural). No separate framework wrapper needed. —
  Rationale: matches established structure; lower surface area.

## Changes Made

**Author-time integration in `/maintain`** (`core/skills/maintain.md`,
mirrored in `.claude/skills/maintain/SKILL.md` section listing). The
Writing Standards section was upgraded from a pointer to a procedure:
when editing operative docs, identify the doc type, read section 2 of
the standards plus the matching 8.x subsection, then draft. Doc-type →
standards mapping table covers skills, session logs, operative docs,
design docs, friction log entries, values docs, and specs. Mechanical
edits (typos, broken paths) skip the load.

**New `/validate standards` mode** (`core/skills/validate-standards.md`,
new). Retrospective review against the standards. Scope-configurable —
user picks docs and standards subset. Defaults to operative content
reviewed against 2.3 (produces what it contains) and 4.4
(cross-references with context), with a scoping-patterns table for
common alternative scopes. Findings file in `reference/sessions/`,
routed through `/validate`'s existing fix-now / defer / wont-fix
disposition step.

**Mode integration** (`core/skills/validate.md`,
`.claude/skills/validate/SKILL.md`, `core/skills/README.md`,
`install/skills-intent.md`, `CLAUDE.md`). Standards review added to
both mode menus, both routing tables, the skills README listing, the
skills-intent reference wrapper description, and the framework CLAUDE.md
skills table summary.

**Update notes** (`install/update-notes.md`). Two consumer-facing
entries — one for the new `/validate standards` mode, one for the
`/maintain` author-time integration. Per the 2026-04-18 friction-log
entry on tagging cadence, tags happen at session end (one tag for the
whole arc) rather than per commit.

**Feedback log archival** (`reference/feedback-log.md`,
`reference/feedback-log-archive.md`). Eight 2026-04-15 entries moved to
the archive — including #21 (writing standards), now resolved with all
three phases complete. The seven other entries had been resolved
2026-04-15 but were never archived; the active log was carrying their
weight unnecessarily.

## What Didn't Work

- **Initial "enhance /validate debug" suggestion.** Was offered as a
  quick side-quest but the user rejected it — debug is reactive to a
  specific observed problem, not standards-conformance review. Right
  pushback; revealed the diagnostic-question distinction.

- **Initial "three modes" framing (prospective / current /
  retrospective).** User reframed: prospective and current collapse
  to a single author-time mode — the value is standards in the room
  while writing, not pre-edit awareness as a separate beat. The
  collapsed framing made the work tighter.

## Friction Log Entries Processed

This session resolved the Phase 3 portion of feedback log entry
"2026-04-15 — Bring NLA writing standards into the framework"
(now archived).

Two new friction log entries were created during the debrief:
- 2026-05-04 — Multi-file maintenance: cross-references demand the
  referenced file ship first
- 2026-05-04 — Resolved-but-unarchived log entries drift across sessions

Both pending; both have proposed fixes; neither was implemented this
session.

## Debrief

**What worked.**

- The /think reframings landed where they were supposed to. Collapsing
  "prospective + current" into "author-time" came from the user's
  pushback and tightened the design — a genuine reframing, not just
  renaming. The debug-vs-standards-review distinction also came from
  user pushback, and was right.

- Targeted-load over always-load was the right call. The user's
  framing — "if it misses, /validate standards catches it, and we can
  escalate later" — turned the design choice into an iteration plan.
  Lighter now, conservative fallback known.

- Per the user's reminder, loading section 2 + 8.1 + 8.3 of the
  standards before drafting `validate-standards.md` and the maintain.md
  edits was concretely useful. The "posture before procedure" guidance
  from 8.1 shaped the validate-standards.md opening; 8.3's
  "self-contained, design rationale stays out" kept the file focused on
  *what to do* rather than *why we built it this way*. The standards
  earned their place during their own integration.

**What was unclear.**

- Reading order under iteration. The plan initially had maintain.md
  before validate-standards.md, but maintain.md's diagnostic-use
  section references `/validate standards` — so the file order had to
  flip mid-implementation to keep each commit internally consistent.
  Worth flagging for future multi-file maintenance work: when files
  cross-reference, write the referenced file first.

**What surprised.**

- The archival backlog (seven 2026-04-15 entries unmoved for ~3 weeks)
  was visible at session start and became a small task at session end.
  Worth noting that the maintain Common Tasks step "Archive resolved
  entries" is easy to skip during the session it's earned in — and
  drift accumulates silently. Possible future friction-log entry: a
  /close prompt that asks "any resolved-but-unarchived entries?" when
  the active log has them.

## State at Close

### Context for next time

- Phase 3 of feedback entry #21 is complete. The writing standards now
  have author-time use in /maintain (targeted-load) and retrospective
  use in `/validate standards`. The active feedback log is empty;
  all eight previously-pending entries are archived. GitHub Issue #21
  is closed with a Phase 3 summary comment.

- The `/validate standards` mode hasn't yet been exercised in anger.
  Next time the framework's docs are reviewed against the standards
  (e.g., when the standards file evolves, or when a doc feels off),
  it'll get its first real test.

- Per the 2026-04-18 friction-log entry on tagging cadence, this
  session ended with one tag (`v0.0.6`) for the whole arc of work —
  not per-commit tags. Five commits landed: new mode, /maintain
  author-time, archive cleanup, session log finalization, debrief
  friction entries. All pushed to origin/main.

### Decisions awaiting implementation

- **Pending friction log entries** — ten remain (eight unchanged from
  2026-04-18, plus two new from this session's debrief). Most natural
  pairings:
  - 2026-05-04 cross-reference ordering + 2026-05-04 archival drift
    (this session's debrief entries): both quick edits to
    `core/skills/maintain.md` Pre-flight and `core/skills/close.md`
    Loose Ends respectively. Could pair into a single short session.
  - 2026-04-18 shippability convention refinement: quick edit to
    `core/skills/maintain.md` Shippability section + mirror in
    `install/package-intent.md`.
  - 2026-04-16 cluster (Python implementation standards, Fallingwater
    preamble, /maintain prose-vs-code, re-compile export.py): pairs
    thematically; best after nla-compiler package becomes available.
  - Older entries (2026-03-08 /startup flag, 2026-02-23 bare project
    path, 2026-02-23 friction-logs gitignored, 2026-02-22 context
    awareness): unchanged.

- **Packages migration propagation** (penny-post, process-helpers,
  domain projects) — still pending from 2026-04-15.

### Where to pick up

**Immediate candidates:**
- **Test-drive `/validate standards`.** Run the new mode against a
  recent doc that hasn't been reviewed (e.g., `validate-standards.md`
  itself, or the new author-time `/maintain` section) — first-use
  feedback shapes whether defaults need adjustment.
- **Shippability convention refinement (2026-04-18 friction entry).**
  Quick, fits any session.

**Watch:**
- Whether the targeted-load in `/maintain` actually triggers reliably
  during operative-doc edits. If the AI keeps not loading the
  standards (because the trigger language is too soft, or the doc-type
  detection is fuzzy), that's the escalation signal — switch to
  always-load, or sharpen the procedure language.
