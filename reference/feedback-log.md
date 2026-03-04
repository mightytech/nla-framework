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

### 2026-03-03 — Export hybrid approach: script for mechanical work, AI for judgment

**Source:** [Issue #9](https://github.com/mightytech/nla-framework/issues/9)
**Verdict:** Accept principle — implementation needs a `/think` design session
**Status:** pending

**What to do:**
Design and implement a `lib/export-plugin.sh` (or Python script) that handles the
mechanical phase of export (directory creation, thin wrapper resolution, path rewriting,
supporting file copying, frontmatter adjustment, plugin.json generation). The AI retains
inventory/classification (phase 1), foundation synthesis, edge case decisions, README
generation, and verification. Input to the script is a classification manifest (JSON)
produced by the AI through the phase 1 conversation.

Before implementing, run a `/think` session to work through: manifest format design,
edge case handling (ejected wrappers, extension naming, non-standard directories),
generalization across NLAs, and the contract between AI judgment and script execution.

**Why it was accepted:**
Duet's first export (18 skills, 54 files, three parallel agents) demonstrated that most
of the file generation work is deterministic — read file, apply path rewrites, copy
supporting files. A script applies these rules identically every time; parallel AI agents
independently interpreting the same instructions introduces consistency risk. The
phase 1/phase 2 distinction is sharp: judgment for classification and synthesis, script
for mechanical transformation.

---

---

*This log is populated by `/check-feedback` (or any external feedback tool) and consumed
by `/maintain`. Resolved entries are moved to `feedback-log-archive.md`.*
