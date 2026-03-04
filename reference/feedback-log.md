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

### 2026-03-03 — Permission model: NLAs need a way to whitelist external directory access

**Source:** [Issue #7](https://github.com/mightytech/nla-framework/issues/7)
**Verdict:** Accept principle — implementation needs a `/think` design session
**Status:** pending

**What to do:**
Design and implement the framework's role in permission management:
1. Document the permission conversation pattern (how NLAs walk users through permissions)
2. `/startup` or `/setup` guides users through permission setup at first run
3. `/install` proposes read permissions for package directories when installing
4. Tiered model: framework reads at user-wide scope, NLA-specific dirs at project scope,
   writes stay manual

Before implementing, run a `/think` session to determine where each piece lives in the
framework, how it affects existing projects, and the right integration points with
Claude Code's settings hierarchy.

**Why it was accepted:**
Two sources report the same friction from different angles. Creative Helpers (#6 item 1)
hit permission prompts during structural validation of sibling directories. Duet (#7)
hit them across every skill invocation — 11 thin wrappers each triggering prompts for
framework reads. The proposed tiered model maps to Claude Code's existing settings
hierarchy (user-wide, project, local). The principles (contextual, specific, read/write
distinction, rare operations manual, conversational) are well-reasoned.

---

### 2026-03-03 — Add runtime validation step to /export

**Source:** [Issue #8](https://github.com/mightytech/nla-framework/issues/8), Items 1-3
**Verdict:** Accept (items 1-3 combined into one enhancement)
**Status:** resolved
**Resolved:** 2026-03-04 — Added optional step 8 (Runtime Validation) to `core/skills/export.md` with env var workaround, two-step validation approach, and guidance on what runtime catches that structural checks can't.

**What to do:**
Add an optional step 8 to `core/skills/export.md` for runtime validation. After
structural verification (step 7), offer to load the plugin into a real Claude session
to confirm it actually works. Include:
- The env var workaround: `env -u CLAUDECODE claude -p "..." --plugin-dir ./path --max-turns 2`
- Prompt guidance: use simple prompts, consider two-step validation (confirm loading,
  then check skill registration)
- Note that `--max-turns` is essential to prevent runaway turns
- Frame as optional — structural checks are the baseline, runtime is the bonus

**Why it was accepted:**
Duet's export produced 54 files across 18 skills. Structural checks (step 7) verified
files look right but can't confirm the plugin loads. Runtime testing confirmed all 18
skills loaded, frontmatter behaved correctly, and user-invocable flags worked — things
structural checks can't verify. The env var workaround and prompt guidance are practical
findings that should be documented where they're needed.

---

---

*This log is populated by `/check-feedback` (or any external feedback tool) and consumed
by `/maintain`. Resolved entries are moved to `feedback-log-archive.md`.*
