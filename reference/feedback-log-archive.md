# Framework Feedback Log Archive

Resolved feedback log entries, moved here from `feedback-log.md` during `/maintain` sessions. This keeps the active feedback log lean while preserving history for pattern analysis.

**How entries get here:** When `/maintain` resolves a feedback log entry, it moves the complete entry (including the `**Resolved:**` line) from the active log to this archive.

**Searching:** Use grep to search this archive when looking for historical patterns.

---

## Entries

*Archived entries in reverse chronological order.*

### 2026-04-17 — Document settings.local.json drift pattern in structure-intent

**Source:** [Issue #23](https://github.com/mightytech/nla-framework/issues/23) item 2
**Verdict:** Adapt — take only the lightweight doc note; defer the heavier options
**Status:** resolved
**Resolved:** 2026-04-17 — Added "Drift over time" note to the `.claude/settings.local.json` description in `install/structure-intent.md`. Wrote update-notes entry so existing projects know the pattern has been documented. Heavier options (/close or /maintain drift nudge, /validate baseline-diff mode) remain deferred — revisit if drift accumulates meaningfully across more projects or a third data point arrives.

**What to do:**
Add a short note in `install/structure-intent.md` (alongside or near the
`.claude/settings.local.json` guidance) describing the drift pattern: Claude Code
auto-approves-and-records new Bash patterns when a maintainer runs a tool the project
hasn't pre-declared (e.g., `python3 -m json.tool`). These entries accumulate silently
over time even in a fully-migrated packages/ project. This isn't framework behavior
and isn't a bug — but maintainers should know to recognize it and periodically prune
if the file grows, rather than mistake it for a framework-introduced problem.

Deferred from this item (not implementing now): a `/close` or `/maintain` drift nudge
comparing actual settings against a declared baseline, and a `/validate` mode doing
the same check. Both require more design work (what's the authoritative baseline?
what's the diff strategy?) and solve a problem that's now narrow after the packages/
migration closed out the big accumulation vectors (#6, #7, #12). Revisit if drift
actually accumulates meaningfully across a few projects, or if a third data point
comes in.

**Why it was accepted:**
The submitter explicitly flagged no strong recommendation and moderate confidence on
best mitigation. The positive signal — packages/ migration closed out the primary
permission-drift concerns — means this residual is genuinely narrow. A doc note meets
the submitter's primary ask (help maintainers recognize and not misattribute the
pattern) with minimal surface area. Heavier interventions can wait for more evidence.

---

### 2026-04-17 — /install and /update initial-add path should check for tagged releases

**Source:** [Issue #23](https://github.com/mightytech/nla-framework/issues/23) item 1
**Verdict:** Accept
**Status:** resolved
**Resolved:** 2026-04-17 — Added "Pin to a Tagged Release" subsection to core/skills/install.md, with prompt wording mirrored from update.md's advance path. Added "For new intents that add a submodule" bullet to core/skills/update.md Phase 2 Apply Changes, cross-referencing install.md. Added step 1a to .claude/skills/create-app/SKILL.md for the framework-submodule tag check during project creation. Wrote update-notes entry announcing the change.

**What to do:**
The advance path in `core/skills/update.md` already checks for tagged releases between
current and HEAD and offers the user a choice between the tagged release (stable) and
HEAD (bleeding edge). Extend that same check to the initial-add path:

1. In `core/skills/install.md`, after `git submodule add`, run
   `git -C packages/[name] tag --sort=-creatordate | head -1`. If a tag exists and
   points at a commit other than current HEAD, offer the same stable/HEAD choice the
   advance path offers. Mirror `update.md:65`'s prompt wording for consistency.
2. In `core/skills/update.md`, apply the same check when a migration introduces new
   submodules (the initial-add flow inside `/update`, not only the advance flow).
3. Check `.claude/skills/create-app/` — if it runs `git submodule add` for framework
   during project creation, the same check should apply there too, so new projects
   pin at the framework's tagged release rather than HEAD.

**Why it was accepted:**
The principle (tagged release = stable default) is already in the framework; only the
initial-add path didn't inherit it. High confidence: this was caught during the
process-helpers maintainer's actual packages/ migration. Penny-post's HEAD was one
commit past v0.0.1 (a session-log update, not behavioral), so the project ended up
silently pinned at `main` rather than at the tagged release. Caught during pre-push
review — otherwise the mismatch would have drifted undetected. Small, well-scoped
change; same UX pattern applied to more entry points.

---

### 2026-04-17 — Shippability distinction for framework changes: consumer-facing vs. framework-internal

**Source:** [Issue #22](https://github.com/mightytech/nla-framework/issues/22)
**Verdict:** Accept
**Status:** resolved
**Resolved:** 2026-04-17 — Added "Shippability: Consumer-Facing vs. Internal Content" section to reference/design-rationale.md (principle, universally framed). Added "Shippability at Commit Time" section to core/skills/maintain.md (commit-time procedure, all domain projects). Added "Shippability" section to install/package-intent.md (package-specific pointer). Wrote update-notes entry announcing the convention.

**What to do:**
Codify the shippability convention. Commits touching consumer-facing content (`core/`,
consumer-facing `install/*.md`) get a tag and an `install/update-notes.md` entry.
Commits touching only framework-internal content (framework's own `CLAUDE.md`, its
own `reference/`, its own `reference/installed-packages.md`) skip both — consumers
never read those files. Landing points:

1. Add a "Shippability" section to `reference/design-rationale.md` that defines the
   distinction and explains the reasoning (consumer sees what `/update` reads: `core/`
   and consumer-facing `install/`; everything else is invisible).
2. Add a short note in the framework's own `/maintain` guidance (`.claude/skills/maintain/SKILL.md`
   and/or `core/skills/maintain.md`'s tagging/update-notes coverage) referencing the
   convention so future maintainers apply it.
3. Propagate to packages via `install/package-intent.md` so package authors (penny-post,
   process-helpers, future packages) inherit the same rule.

Start with prose convention (lightest touch); add more structure (severity field, etc.)
only if prose alone proves insufficient.

**Why it was accepted:**
The distinction isn't invented — it mirrors what `/update` already does. Without
codifying it, routine cross-reference maintenance (updating descriptions of where
packages live, internal session logs, framework's own CLAUDE.md) surfaces as "there's
an update to review" prompts in every downstream NLA. The signal-to-noise ratio in
`/update` degrades as the ecosystem grows. The framework's own next natural commit —
updating its own references from `../nla-penny-post/` to `packages/nla-penny-post/` —
is the first immediate test case: under this convention, it lands un-tagged with no
update-note, which is correct.

**Scope adjustment during implementation:** Initial proposal framed the convention as framework/package-specific. During the implementation discussion, the user pointed out the principle applies universally — domain projects have the same split (reference/ internal; app/, skills/, CLAUDE.md consumer-facing via plugin export). Final landing: design-rationale framed universally, maintain.md procedure affecting all domain projects, package-intent.md as a package-specific application of the general rule.

---

### 2026-03-03 — Export hybrid approach: script for mechanical work, AI for judgment

**Source:** [Issue #9](https://github.com/mightytech/nla-framework/issues/9)
**Verdict:** Accept principle — implementation needs a `/think` design session
**Status:** resolved
**Resolved:** 2026-04-16 — Implemented jointly with the /export view-source redesign. `lib/export.py` handles mechanical transforms (git archive, submodule resolution, path rewrites, frontmatter surgery, plugin.json generation, verification); AI handles inventory, classification, foundation synthesis, README, and final verification. Manifest JSON is the handoff format. Python 3, stdlib only. Self-test and integration test cover the script. See session log `2026-04-16-export-simplification.md` and design-rationale "Plugin Export: View-Source Model".

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
**Status:** resolved
**Resolved:** 2026-03-04 — Added permission management model: declarations in package manifests, `/create-app` generates settings files, `/install`+`/update` propose entries, `/validate` checks consistency, `/startup` notes missing settings. Design rationale, update notes, and package manifest updates included.

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

**Design deviation:** The /think session placed all permissions at project scope
(`settings.local.json`) rather than user-wide for framework reads. User-wide
(`~/.claude/settings.json`) is documented as an optional optimization for
multi-project setups. See design-rationale.md "Permission Management Model" for
the rationale.

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
