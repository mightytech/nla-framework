# Framework Feedback Log Archive

Resolved feedback log entries, moved here from `feedback-log.md` during `/maintain` sessions. This keeps the active feedback log lean while preserving history for pattern analysis.

**How entries get here:** When `/maintain` resolves a feedback log entry, it moves the complete entry (including the `**Resolved:**` line) from the active log to this archive.

**Searching:** Use grep to search this archive when looking for historical patterns.

---

## Entries

*Archived entries in reverse chronological order.*

### 2026-02-17 — Create `install/` directory for framework package management

**Source:** [Issue #1](https://github.com/mightytech/nla-framework/issues/1)
**Verdict:** Accept
**Status:** resolved
**Resolved:** 2026-02-17 — Created `install/` directory with four intent files: `install.md` (orchestrator), `CLAUDE-intent.md`, `skills-intent.md`, `structure-intent.md`. Modeled on penny post's install/ pattern.

**What to do:**
Create an `install/` directory with intent files (`CLAUDE-intent.md`, `skills-intent.md`,
`structure-intent.md`) that formalize what `/create-app` does implicitly. This is the
framework's counterpart to penny post's `install/` directory — the standard mechanism
for NLA packages to describe their integration points. Use penny post's
`../nla-penny-post/install/` as a reference for the pattern.

**Why it was accepted:**
Penny post already ships `install/` and NLAs need a standard way to consume it. The
framework is itself a "package" that gets installed into NLAs — `/create-app` is the
first install. Formalizing this into intent files enables a general `/install` and
`/update` pattern. Deferring would mean ad hoc solutions that cost as much as the
real thing.

---

### 2026-02-17 — Add feedback log as framework-level concept

**Source:** [Issue #2](https://github.com/mightytech/nla-framework/issues/2)
**Verdict:** Accept
**Status:** resolved
**Resolved:** 2026-02-17 — Added feedback log to `core/skills/maintain.md` (Required Reading, Processing Feedback Log Entries, broadened pipeline section), framework's own `/maintain` skill, scaffold (`reference/feedback-log.md`, `reference/feedback-log-archive.md`), and `/create-app` file lists. Also created framework's own `reference/feedback-log.md` and `reference/feedback-log-archive.md`.

**What to do:**
Add `reference/feedback-log.md` and `reference/feedback-log-archive.md` to the framework
and scaffold. Update `core/skills/maintain.md` to check the feedback log alongside the
friction log. Update the framework's own `/maintain` skill similarly.

**Why it was accepted:**
The friction log captures internal observations but there's no equivalent for external
feedback. After triage, accepted items have nowhere to land as actionable work for
`/maintain`. Penny post has a working implementation that proves the pattern. This is
the foundational piece that makes penny post (and future feedback tools) work end-to-end
with `/maintain`.

---

### 2026-02-17 — Add session-start checklist to `/maintain`

**Source:** [Issue #3](https://github.com/mightytech/nla-framework/issues/3), Items 1 and 3
**Verdict:** Accept (items 1 and 3 combined)
**Status:** resolved
**Resolved:** 2026-02-17 — Added Session Start section to `core/skills/maintain.md` and framework's own `/maintain` skill. Surfaces pending friction log and feedback log counts, reads most recent session log for continuity, presents summary before asking what to work on.

**What to do:**
Add a session-start step to `core/skills/maintain.md` that reads the friction log,
feedback log, and most recent session log, then presents a summary: "You have X friction
log entries and Y feedback items. Last session ended with [state]." This surfaces pending
work and provides session continuity without requiring `/startup`.

**Why it was accepted:**
Currently `/maintain` says "read the friction log" in Required Reading but doesn't
actively surface what's waiting. The session-close step already exists ("fill in State at
Close") but the complementary session-start step is missing. Together they form the
session continuity mechanism the framework needs.
