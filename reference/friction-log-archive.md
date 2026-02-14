# Framework Friction Log Archive

Resolved and closed friction log entries, moved here from `friction-log.md` during `/maintain` sessions. This keeps the active friction log lean while preserving history for pattern analysis.

**How entries get here:** When `/maintain` resolves a friction log entry, it moves the complete entry (including the `**Resolved:**` line) from the active log to this archive.

**Searching:** Use grep to search this archive when looking for historical patterns. The `/friction-log` skill searches here automatically before creating new entries.

---

## Entries

*Archived entries in reverse chronological order.*

### 2026-02-12 — AI maintainer executed changes without confirming strategy

**Type:** process
**Severity:** minor
**Blast radius:** maintainers
**Status:** resolved
**Resolved:** 2026-02-12 — Added assessment step to friction log processing in both `/maintain` skills (core and framework). Straightforward fixes proceed directly; entries requiring new functionality or design decisions get discussed first, with `/plan` if scope warrants it.

**Observation:**
During friction log processing, the AI maintainer treated entry #1 ("ask where to save project") the same as entry #3 ("remove scaffold path") — jumping straight to execution without discussing the approach. Entry #3 was a straightforward removal; entry #1 involved design decisions (when to ask, how to handle non-sibling paths, how much complexity to add). The result was over-engineered changes that had to be reverted.

The pattern: not all friction log entries are equal. Some are "remove X" (clear action, small blast radius). Others are "add Y" (design decisions, trade-offs, dependencies on other work). The AI should distinguish between these and propose before editing on anything that involves design.

**Proposed fix:**
Add guidance to the `/maintain` skill (or to the AI's own memory) that friction log entries requiring new functionality — as opposed to removing or simplifying existing functionality — should be discussed before implementation. The plan mode pattern worked well for entry #3; it should have been used for entry #1 as well, with more attention to the design questions before exiting the plan.

---

### 2026-02-12 — Framework could generate config files for new NLAs

**Type:** core
**Severity:** minor
**Blast radius:** new projects
**Status:** resolved
**Resolved:** 2026-02-12 — Implemented NLA configuration system. Created `core/skills/preferences.md` (framework skill logic), scaffold config files (`config-spec.md`, `config.md`, `config/`), thin wrapper, and integrated with `/startup`, scaffold `CLAUDE.md`, `overview.md`, `README.md`, `system-status.md`, and `/create-app`. Design rationale in `reference/design-rationale.md` under "Future Direction: NLA Configuration."

**Observation:**
NLA projects need a way for app users to modify behavior without modifying the application itself. Traditional config (YAML, JSON) is too rigid for an LLM runtime. Natural language config (Markdown) lets users express preferences from structured paths to behavioral directives — the LLM reads and applies them with judgment.

**Notes:**
Design rationale covers: three-actor model (framework devs, app devs, app users), quarterback pattern (light main config routes to sub-configs by context), three-layer git separation, generic `/preferences` framework skill + app-specific `config-spec.md`, conflict/ambiguity detection, integration with `/create-app`.

---

### 2026-02-11 — /create-app should ask where to save the project

**Type:** process
**Severity:** minor
**Blast radius:** new projects
**Status:** resolved

**Observation:**
`/create-app` defaults to creating the project in a sibling directory (`../project-name/`). The user is not asked where they want the project saved. The sibling convention is convenient but not technically required — the framework reference paths (`../nla-framework/`) just need to resolve correctly, and CLAUDE.md files in different projects shouldn't interact.

The user should be asked where to save the project. The sibling directory is a sensible default, but users may have different workspace layouts.

**Affected files:**
- `.claude/skills/create-app/SKILL.md` — Add location question to conversation flow, update path generation logic

**Proposed fix:**
Add a question to the `/create-app` conversation (Phase B or D) asking where to save the project. Default suggestion is `../project-name/`. If the user picks a different location, adjust the framework reference paths in thin wrappers and CLAUDE.md accordingly. Note the two constraints: (1) the framework path must resolve, and (2) CLAUDE.md files from different projects shouldn't be in the same directory tree where Claude Code might pick up both.

**Notes:**
Relates to "Path resolution" in Patterns to Watch. Non-sibling layouts are the main case where `../nla-framework/` breaks. If `/create-app` knows the actual location, it can generate correct paths from the start.

**Deferred 2026-02-12:** Asking about location is simple, but the framework path appears in ~17 places across 8 files in generated projects. Non-sibling support means changing all of them, and there's no single source of truth for the path after creation — moving the project later means manually updating all 17 references. A configuration variable (e.g. `framework_path`) would centralize this. Deferring until the config file design is resolved (see "Framework could generate config files for new NLAs" entry above), then tackling location as part of that.

**Resolved 2026-02-12:** Config system is now implemented. Investigated non-standard locations end-to-end. The config system makes the declaration layer easy (`Framework path:` in config.md), but `core/skills/*.md` files share hardcoded `../nla-framework/` paths across all domain projects. Making these location-agnostic requires either natural language path resolution (adds inference overhead to the common case), template variables (foreign to NLAs), or heavier wrappers. All degrade the default sibling experience to support a rare case. Decision: keep the sibling convention for MVP. Path resolution is a mechanical operation where you want reliability, not LLM flexibility. See `reference/design-rationale.md` "Sibling Directory Convention" for full rationale.

---

### 2026-02-11 — Scaffold path in /create-app conflates example app with side-by-side install

**Type:** process
**Severity:** minor
**Blast radius:** new projects
**Status:** resolved
**Resolved:** 2026-02-12 — Removed scaffold/from-scratch path choice from `/create-app`. Created `/create-sample-app` skill for installing the scaffold as a standalone example project.

**Observation:**
The `/create-app` skill presents a "scaffold path" that installs the sample format-article task alongside the user's custom task. The intent was to help users learn by example, but the scaffold app is better understood as a standalone example application — something you install once to see how a complete NLA works, not something you mix into a real project.

**Before:** `/create-app` offers "scaffold path" (includes sample formatter alongside custom task) vs "from-scratch path" (custom task only). The scaffold path is recommended for first-time users.

**After:** Two cleaner options: (1) A separate skill like `/create-sample-app` that installs the scaffold as a standalone example project, or (2) `/create-app` briefly mentions the scaffold can be installed separately as a reference, without emphasizing it. The scaffold-as-example is probably a one-time thing and shouldn't be a prominent fork in the create flow.

**Affected files:**
- `.claude/skills/create-app/SKILL.md` — Remove or de-emphasize scaffold path
- Possibly new skill: `.claude/skills/create-sample-app/SKILL.md`
- `scaffold/` — Already works as-is for standalone install

**Proposed fix:**
Remove the scaffold/from-scratch path decision from `/create-app`. Either create a `/create-sample-app` skill that installs the scaffold as a standalone example, or have `/create-app` mention in passing that the scaffold directory can be installed separately. The create flow should focus entirely on the user's custom project.

**Notes:**
The user who surfaced this already had a standalone scaffold project and chose "from scratch" immediately. The scaffold path may never have been the right default — a standalone example app is more useful than a hybrid project.
