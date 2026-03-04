# Framework Feedback Log Archive

Resolved feedback log entries, moved here from `feedback-log.md` during `/maintain` sessions. This keeps the active feedback log lean while preserving history for pattern analysis.

**How entries get here:** When `/maintain` resolves a feedback log entry, it moves the complete entry (including the `**Resolved:**` line) from the active log to this archive.

**Searching:** Use grep to search this archive when looking for historical patterns.

---

## Entries

*Archived entries in reverse chronological order.*

### 2026-03-03 — Validation file-existence checks should prefer built-in tools over Bash

**Source:** [Issue #6](https://github.com/mightytech/nla-framework/issues/6), Item 1
**Verdict:** Accept
**Status:** resolved
**Resolved:** 2026-03-03 — Added "How to check" note to `core/skills/validate-structural.md`: prefer built-in file tools (Glob, Read) over Bash for existence checks on sibling directories to avoid permission prompts.

**What to do:**
Add a one-line note to the structural validation skill: "Use built-in file tools (Glob,
Read) rather than Bash for existence checks, especially for files in sibling directories,
to avoid unnecessary permission prompts."

**Why it was accepted:**
High confidence, reproduced across multiple validation runs in Creative Helpers. The
permission prompts are a recurring annoyance for a fundamentally read-only operation.

---

### 2026-03-03 — Strengthen install skill's post-install validation from suggestion to explicit step

**Source:** [Issue #6](https://github.com/mightytech/nla-framework/issues/6), Item 2
**Verdict:** Accept with adaptation
**Status:** resolved
**Resolved:** 2026-03-03 — Changed step 5 of `core/skills/install.md` from "Suggest running `/validate`" to "Run structural validation on the affected integration points" with rationale. Matches the pattern established in `/update` per Issue #5.

**What to do:**
In `core/skills/install.md`, change post-install validation from a suggestion to an
explicit step. Don't auto-run, but frame as standard rather than optional.

**Why it was accepted:**
During Creative Helpers' first package installation, post-install validation caught three
files out of sync. Framing validation as an explicit step closes the gap without adding
permission friction.

---

### 2026-03-03 — Note plugin format compatibility with Claude Code and Cowork in /export

**Source:** [Issue #8](https://github.com/mightytech/nla-framework/issues/8), Item 5
**Verdict:** Accept
**Status:** resolved
**Resolved:** 2026-03-03 — Added compatibility note to the opening section of `core/skills/export.md`: the plugin format works in both Claude Code and Cowork.

**What to do:**
Add a note to `core/skills/export.md` that the generated plugin format is compatible
with both Claude Code and Cowork.

**Why it was accepted:**
Confirmed via documentation during Duet's export. Users should know the plugin works in
both environments.

---

### 2026-03-03 — /validate should flag feedback infrastructure without penny post skills

**Source:** [Issue #11](https://github.com/mightytech/nla-framework/issues/11), Item 1
**Verdict:** Accept
**Status:** resolved
**Resolved:** 2026-03-03 — Added check 7 "Package consistency" to `core/skills/validate-structural.md`: flags when `reference/feedback-log.md` exists but no `/write-letter` skill is registered.

**What to do:**
Add a structural validation check for feedback infrastructure without corresponding
penny post skills.

**Why it was accepted:**
During Duet's session, the AI used feedback infrastructure incorrectly because the files
existed but the skills didn't. A low-cost structural check catches this gap.

---

### 2026-03-03 — Export inventory should surface classification rationale

**Source:** [Issue #11](https://github.com/mightytech/nla-framework/issues/11), Item 2
**Verdict:** Accept
**Status:** resolved
**Resolved:** 2026-03-03 — Added guidance to `core/skills/export.md` Step 1: "For skills where the classification isn't self-evident, explain your reasoning. The user should be able to evaluate the judgment, not just the result."

**What to do:**
Add guidance to export.md Step 1: explain reasoning for non-obvious classifications.

**Why it was accepted:**
During Duet's export, some classifications were arguably correct but the user couldn't
evaluate the judgment without explanation. The rationale is the last human-readable
checkpoint before execution.

---

### 2026-02-21 — Add reference-search step to /update for removals and renames

**Source:** [Issue #5](https://github.com/mightytech/nla-framework/issues/5), Item 1
**Verdict:** Accept
**Status:** resolved
**Resolved:** 2026-02-21 — Added "Search for stale references" substep to step 4 "For removed intents" in `core/skills/update.md`. Instructs the AI to grep the project for mentions of removed items beyond known integration points.

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
**Status:** resolved
**Resolved:** 2026-02-21 — Added "Check downstream targets" section to step 6 in `core/skills/update.md` listing README.md, CLAUDE.md, and app/overview.md as explicit post-update consistency checks.

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
**Status:** resolved
**Resolved:** 2026-02-21 — Renamed step 6 to "Summary and Verification", changed validate from a suggestion bullet to a bolded recommendation with rationale: "Updates often have downstream effects that intent-diff analysis doesn't catch — validation is the safety net."

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

### 2026-02-18 — Architecture review mode for /validate (adapted from /code-review proposal)

**Source:** [Issue #4](https://github.com/mightytech/nla-framework/issues/4)
**Verdict:** Adapt — implemented as Mode 4 of `/validate` rather than standalone `/code-review` skill
**Status:** resolved
**Resolved:** 2026-02-18 — Split `/validate` into dispatcher + mode files. Added architecture review as Mode 4 with nine analytical categories derived from Copydesk's review. Refactored framework's own validate to delegate to core mode files. Added session-close reminder in `/maintain` for structural changes.

**What to do:**
Add architecture review capability that walks the full document chain checking for
coherence issues after restructuring. Copydesk found 12 issues in six categories
(path resolution, cross-reference integrity, layer boundaries, consistency,
conditional completeness, generic/specific alignment) that existing `/validate`
modes don't catch.

**Why it was accepted:**
The categories are universal to any NLA with multiple doc files. Architecture review
complements existing modes the way code review complements testing in traditional
software — tests check behavior, reviews check structure. Implementing as a `/validate`
mode (not a standalone skill) preserves conceptual unity and avoids wrapper proliferation.

---

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
