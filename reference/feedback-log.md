# Framework Feedback Log

Accepted items from external feedback, waiting for implementation. Each entry captures
what was accepted, why, and where to find the full context.

The feedback log is the sibling of the friction log:
- **Friction log** — things *you* noticed while working
- **Feedback log** — things *others* noticed that you agreed with

Both feed into `/maintain`. Both are queues of actionable items.

---

## How to Use This Log

**When items are added:**
- After triaging feedback (via `/check-feedback` or any intake mechanism), accepted
  items are deposited here with their verdict rationale and a reference to the source.

**When items are resolved:**
- During `/maintain` sessions, the maintainer reviews pending items and implements them.
  Resolved entries are moved to `feedback-log-archive.md`.

**At session start:**
- `/maintain` checks this log alongside the friction log to surface what's waiting.

---

## Entry Format

```markdown
### [DATE] — [Brief description of the accepted item]

**Source:** [Link to GitHub Issue or intake item]
**Verdict:** [Accept / Adapt — and the reasoning]
**Status:** pending | in-progress | resolved

**What to do:**
[Concrete description of the change needed]

**Why it was accepted:**
[The rationale from triage — why this matters, what it improves]

**Resolved:** [DATE] — [brief description of what was changed and where]
```

Not every entry needs all fields. The essentials are: Source, What to do, Why it was
accepted, Status.

---

## Entries

*Entries are added chronologically, newest first.*

### 2026-02-21 — Add reference-search step to /update for removals and renames

**Source:** [Issue #5](https://github.com/mightytech/nla-framework/issues/5), Item 1
**Verdict:** Accept
**Status:** pending

**What to do:**
Add a substep to `/update` step 4 for removals and renames: after identifying removed
or renamed items, grep the project for remaining references and clean them up. Currently
the update skill focuses on known integration points (CLAUDE.md, skills, structure) but
removals have tendrils throughout the project (overview.md, system-status.md, README.md).

**Why it was accepted:**
First real `/update` run (penny post) demonstrated the gap — `/plan` removal left stale
references in three files beyond the integration points the skill knows about. A
systematic search is low-cost and catches what intent-driven updates miss.

---

### 2026-02-21 — Add README.md as explicit downstream check in /update

**Source:** [Issue #5](https://github.com/mightytech/nla-framework/issues/5), Item 2
**Verdict:** Accept
**Status:** pending

**What to do:**
Add README.md to the downstream effects check in the update skill, at minimum after
structural changes to skills or reference files. README contains a hand-maintained
directory tree that mirrors project structure — any structural change causes drift.

**Why it was accepted:**
README drift was caught by post-update validation, not by the update itself. README
is a predictable downstream target (like CLAUDE.md and overview.md) that should be
checked systematically rather than relying on validation as a safety net.

---

### 2026-02-21 — Strengthen validate-after-update from suggestion to recommendation

**Source:** [Issue #5](https://github.com/mightytech/nla-framework/issues/5), Item 3
**Verdict:** Accept
**Status:** pending

**What to do:**
Strengthen step 6 of the update skill from "suggest running `/validate`" to recommend
it as a standard final step. Something like: "Run `/validate` structural check to verify
consistency. Updates often have downstream effects that the intent-diff approach doesn't
catch."

**Why it was accepted:**
Post-update validation caught 4 issues the update itself missed (stale README tree,
missing entries in system-status.md, unarchived log entries, missing file in overview.md
hierarchy). The evidence is strong that validation after update is essential, not optional.

---

*This log is populated by `/check-feedback` (or any external feedback tool) and consumed
by `/maintain`. Resolved entries are moved to `feedback-log-archive.md`.*
