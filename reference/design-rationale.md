# Framework Design Rationale

This document explains WHY the NLA Framework is built the way it is. It captures the reasoning, trade-offs, and principles that shaped the design.

**Audience:** Framework maintainers (human or AI) who need to understand the decisions before modifying them.

**Purpose:** Prevent well-intentioned "improvements" that break things that work across every domain project.

---

## Foundational Decisions

### Dual-Source Architecture

Domain projects reference the framework as a sibling directory (`../nla-framework/`). The framework is a separate git repo. `git pull` updates the framework independently.

**Why not a package/dependency manager:** NLA "code" is Markdown files. Package managers add complexity that doesn't match the medium. A sibling directory is simple, visible, and the LLM can read both repos naturally.

**Why not git submodules:** Submodules add tooling friction (init, update, sync). A sibling directory with thin wrappers is simpler and matches how LLMs already work — reading files from paths.

### `core/` for Framework Executable Docs

The framework's operative files live in `core/`, not `app/`. Domain projects use `app/` for their application. The different name signals the different role: `core/` is infrastructure read by all projects, `app/` is domain-specific content.

### `reference/` Stays As-Is

Both the framework and domain projects use `reference/` for maintenance records. Familiar to developers. The NLA twist (non-executing channel, operative during maintenance) is worth a sentence in docs, not a rename.

### Thin Wrapper Skills

Claude Code requires skills in `.claude/skills/` within the project. Framework skills use thin wrappers in domain projects that delegate to logic files in the framework's `core/skills/`.

**Why wrappers:** Claude Code discovers skills by scanning `.claude/skills/`. It can't scan a sibling directory. Wrappers give Claude Code what it needs (frontmatter, discoverability) while the actual logic lives in the framework (updatable via `git pull`).

**Eject pattern:** Any wrapper can be replaced with a full skill file for customization. The wrapper is a convenience, not a lock-in.

### /learning-feedback Excluded from Framework

The friction log + maintain cycle is the universal learning loop. `/learning-feedback` (structured correction analysis with before/after examples) is a domain extension for content-transformation NLAs, not universal infrastructure.

**Why not include it:** Not every NLA transforms content. A data-processing NLA, a classification NLA, or a planning NLA might not have "corrections" in the editorial sense. The framework provides the general pipeline; domains extend it.

### Framework Self-Maintenance

The framework has its own CLAUDE.md, `/maintain`, `/friction-log`, and `/plan` skills, plus a `reference/` directory. These are full skills (not thin wrappers) because the framework's working directory IS the framework — `../nla-framework/` paths would be self-referential.

**Why full skills instead of wrappers:** The logic files in `core/skills/` use `../nla-framework/core/` paths, designed for domain projects whose working directory is elsewhere. When the working directory is the framework itself, those paths break. Framework skills use project-relative paths (`core/...`, `reference/...`).

### Scaffold Directory

The framework contains `scaffold/` — a complete working project template with a sample article formatter. It serves two roles: manual fallback (copy and customize by hand) and structural reference for `/create-app`.

**Sample content, not markers:** Scaffold files have working sample content so someone can test immediately. "Replace me" markers would be metadata that influences LLM behavior.

### /create-app: Conversational Project Creation

`/create-app` asks about the user's domain, voice, and tasks, then generates a tailored project. The first interaction with the framework is itself an NLA interaction — flexible interface on top (conversation), structure underneath (generated project).

**Why conversational, not just copy:** The scaffold requires manual customization of 6+ files. That's an implementation burden the LLM can absorb. The user describes what they want; the LLM generates files that fit. This is the structure gradient in action.

**Why read scaffold at generation time:** The skill instructs the LLM to read each scaffold file as a structural reference immediately before generating its counterpart. This keeps generated projects in sync with scaffold updates — when the scaffold improves, `/create-app` picks up the changes without skill edits.

**Why framework-only:** Domain projects don't create other domain projects. `/create-app` lives in `.claude/skills/create-app/` (not in `core/skills/`) because it's framework infrastructure, not a universal skill that domain projects delegate to.

**Scaffold still exists because:** Some users prefer to see exactly what they're getting before customizing. Manual copy is transparent and requires no conversation. `/create-app` is the recommended path; scaffold is the fallback.

### Dual-Mode Framework CLAUDE.md

The framework's CLAUDE.md defaults to project creation (welcoming, directs to `/create-app`). `/maintain` activates maintenance mode. This mirrors the domain project pattern where the default mode is the primary task (content transformation) and `/maintain` switches to system editing.

**Why default to creation:** Most people arriving at the framework want to build something. A maintenance-focused landing page front-loads concepts (blast radius, session lifecycle) that new users don't need yet. Creation mode is welcoming; maintenance mode is available when needed.

**Why this mirrors domain projects:** Domain CLAUDE.md has a default mode (content transformation) and a maintenance mode. The framework CLAUDE.md has the same pattern — default mode (project creation) and maintenance mode. The consistency helps users who've seen one understand the other.

---

## Future Direction: Cowork as a Target Environment

NLAs built on this framework currently require Claude Code. Cowork (Anthropic's desktop agent, launched January 2026) could dramatically expand the audience. Cowork has local file access and can read/write to a designated folder — the core NLA architecture (`app/`, `reference/`, friction log) works unchanged. The difference is skill discovery and project setup.

### The key insight

The framework (Claude Code) is a *builder* tool. The generated project could be a *user* tool on either platform. `/create-app` always runs from Claude Code, but the project it generates could target Cowork or Claude Code. This separates building from using — the technical person builds the NLA, and non-technical people can use it in Cowork.

This is the difference between "neat geeky idea" and "idea that resonates with many types of people." Content teams, editors, marketers — people who work with voice and tone daily — are natural NLA users. They don't use a terminal.

### Skill mimicry in Cowork

Claude Code discovers skills by scanning `.claude/skills/`. Cowork doesn't have this. But skills are just named entry points with instructions. A routing table in the project's instruction file replaces Claude Code's skill scanner:

```markdown
## Available Commands

When the user asks for any of these, read the corresponding file and follow it:

| User says | Read this |
|-----------|-----------|
| "startup" or "load context" | skills/startup.md |
| "format this" or "format article" | skills/format-article.md |
| "maintain" or "edit the system" | skills/maintain.md |
```

This is actually more natural than `/command` syntax — the LLM fuzzy-matches intent instead of requiring exact invocation. "Fix up this article" matches format-article without the user knowing the skill name.

### Discoverability

Claude Code has `/` autocomplete. Cowork has nothing — the user needs to know what to ask for. Three layers of discoverability:

1. **Startup banner.** On new conversation, the LLM lists what it can do: "I can help with: Format article, Friction log, Maintain. Just tell me what you'd like to do, or paste some content."
2. **Help keyword.** "What can you do?" prints available commands with descriptions.
3. **Context-aware hints.** After completing a task, suggest the natural next step: "If something felt off, you can say 'log that' to capture it." Teaches the workflow through use.

All three live in the instruction files — no special infrastructure, just better prose. The startup banner and help keyword would also benefit Claude Code projects.

### Generation differences by target

| Aspect | Claude Code target | Cowork target |
|---|---|---|
| Skills | `.claude/skills/` with YAML frontmatter | `skills/` plain markdown + routing table |
| Framework link | Thin wrappers → `../nla-framework/` | Self-contained (full skill files inlined) |
| Updates | `git pull` the framework | Re-run `/create-app` or manual |
| Instructions | `CLAUDE.md` | Cowork instruction file (TBD — need to test exact mechanism) |
| Discoverability | `/` autocomplete | Startup banner + help keyword + hints |
| `app/`, `reference/` | Same | Same |

The Cowork version is self-contained because Cowork users aren't running `git pull`. Trade-off: no automatic framework updates, but zero-setup simplicity.

### Implementation path

1. Validate Claude Code `/create-app` first (current work)
2. Manually test a simple Cowork project — learn the instruction model, verify file reading works as expected
3. Build `/convert` (or `/deploy`) — a framework skill that takes an existing Claude Code NLA project and generates a Cowork-ready version: ejects thin wrappers into full skill files, adds routing table, adds discoverability (startup banner, help, hints), removes `.claude/skills/`. This is cleaner than complicating `/create-app` with dual-target generation — build for Claude Code first, convert when ready for Cowork.
4. If `/create-app` eventually needs a Cowork target, it can call `/convert` internally rather than duplicating the logic

### Open questions

- What is Cowork's exact mechanism for persistent project instructions? This determines where the routing table and grounding principles live.
- Does Cowork support plugins/MCP that could provide skill-like discoverability?
- How does Cowork handle the 1M context window across sessions — does it reload project files each time, or is there session continuity?

---

## NLA Configuration

*Implemented 2026-02-12. Originally designed as a future direction, now live in both the framework and domain projects.*

Traditional applications use config files (YAML, JSON, .env) to let users modify behavior without modifying the application itself. These files are rigid: structured syntax, limited to predefined keys, unforgiving of errors. NLAs can do something fundamentally different.

### The core insight

In an NLA, the runtime is an LLM. An LLM can read natural language. So config files can be natural language — Markdown, not YAML. This means config can express things traditional config never could:

**Structured** (like traditional config):
```markdown
The framework is located at ../nla-framework/
```

**Behavioral** (only possible with an LLM runtime):
```markdown
When in maintenance mode, always propose changes before editing — never edit directly.
```

**Contextual** (impossible in traditional config):
```markdown
On Wednesdays, talk like a pirate.
```

The LLM reads these directives and applies judgment, the same way it reads voice docs or task docs. Config becomes another natural language input — not a rigid contract between human and machine, but a flexible expression of preferences that the LLM interprets.

### Three-actor model

The framework serves three (sometimes overlapping) groups, each with different relationships to configuration:

**Framework developers** maintain `nla-framework/`. They define the universal config skill logic and the config conversation patterns. They don't set config values — they build the infrastructure that makes config work.

**App developers** build domain NLAs. They decide what's configurable in their app, set defaults, and define constraints. Their choices are captured in a config spec (`app/config-spec.md`) that governs what the config skill offers to users. Examples of developer-set constraints:
- "Always ask about base path and default to ../nla-framework/"
- "Allow users to customize any behavior — this is an LLM, they can change anything"
- "Only allow configuration of output format and voice tone"
- "Make sure user configurations are ethical"

**App users** run the NLA and set preferences via `/preferences`. They don't edit app docs or skill files — they express preferences in config, and the LLM applies them. Their config is personal: gitignored from the app repo, untouched by `git pull`.

This creates a clean three-layer separation:

```
nla-framework/       ← git pull updates infrastructure
my-app/              ← git pull updates the application
my-app/config/       ← user preferences, never touched by either pull
```

The same pattern as `.env` files in traditional apps, but with the full expressiveness of natural language.

### The quarterback pattern

Config must be always-loaded (like CLAUDE.md) because it can affect any aspect of the application's behavior. But a large config file wastes context space. Solution: a light main config that acts as a quarterback.

`config.md` (always loaded) has two jobs:
1. Hold simple, universal directives that always apply
2. Route to sub-configs based on context

```markdown
## Always Active
The framework is located at ../nla-framework/
Never generate output longer than 2000 words.

## Contextual
When in maintenance mode, also read config/maintenance.md.
When running format-article, also read config/formatting-preferences.md.
On Wednesdays, also read config/wednesdays.md.
```

The LLM reads the main config, evaluates the current context (what mode am I in? what skill is running? what day is it?), and loads relevant sub-configs. Sub-configs can overlap — Wednesday + maintenance mode loads both `config/wednesdays.md` and `config/maintenance.md`.

This is the same pattern as CLAUDE.md pointing to skills: a light routing layer that loads detail on demand.

### Config file structure in a domain project

```
my-app/
├── config.md                  # Quarterback — always loaded, routes to sub-configs
├── config/                    # Sub-configs — loaded by context
│   ├── maintenance.md
│   ├── formatting-preferences.md
│   └── wednesdays.md
├── app/
│   ├── config-spec.md         # App developer's config specification
│   └── ...                    # (rest of app unchanged)
└── .gitignore                 # Includes config.md and config/
```

`config.md` and `config/` are gitignored — they belong to the user, not the app. `app/config-spec.md` is committed — it's part of the application, defining what's configurable.

### The config skill: `/preferences`

A framework skill (thin wrapper pattern) that creates config if missing, edits if present. The conversation flow:

1. Read `app/config-spec.md` to understand what's configurable, with what defaults, under what constraints
2. If no config exists, generate initial `config.md` and `config/` from the spec defaults
3. If config exists, read it, then ask the user what they want to change
4. After any change, read through all active config directives and check for:
   - **Conflicts between config directives** — two sub-configs that contradict each other
   - **Conflicts between config and app docs** — a config preference that contradicts voice, patterns, or task instructions
   - **Ambiguities** — directives that could be interpreted multiple ways
5. Flag issues and ask for clarification before saving

The conflict detection is a capability unique to NLA config. A YAML parser can catch duplicate keys. An LLM can catch "these two natural language directives contradict each other" or "this config preference conflicts with your voice doc." This is one of the strongest arguments for natural language config over traditional config.

### Config precedence

When config directives interact with app docs (voice, patterns, tasks), the system needs clear precedence rules. Two models:

- **Config overrides app** — "The app says professional tone, but my config says casual. Config wins." This gives users maximum control but could break the app developer's intent.
- **App authoritative, config suggestive** — "The app's voice doc is authoritative. Config preferences are applied when they don't conflict." This protects the developer's design but limits user flexibility.

The right answer depends on what the app developer specified in `config-spec.md`. A developer who says "allow them to change any behavior" is opting into config-overrides-app. A developer who says "only allow configuration of output format" is opting into a constrained model. The config spec governs precedence — not a framework-wide rule.

### Integration with `/create-app`

During project creation, `/create-app` asks the app developer about configuration:
- What behaviors should users be able to configure?
- What are sensible defaults?
- What constraints should apply? (Ethics requirements, behavioral boundaries, etc.)
- How flexible should the config system be? (Specific knobs only? Or "change anything"?)

The developer doesn't need to be an expert prompt engineer. They express intent naturally — "I want users to be able to tweak the tone" — and the LLM asks clarifying questions ("Should they be able to override the voice entirely, or just adjust formality?"), then produces a well-structured config-spec that the config skill can work with reliably. Human provides intent, AI provides structure — the same principle as everywhere else in the framework. This applies equally to `/preferences` when app users express their preferences.

These answers become `app/config-spec.md`. `/create-app` also generates:
- A starter `config.md` with defaults from the spec
- The `config/` directory
- `.gitignore` entries for config files
- The `/preferences` thin wrapper skill

The config spec can also be edited later via `/maintain` — if the developer realizes they want to add configurable behaviors, they update `config-spec.md` without touching the skill.

### Why natural language, not YAML

**Expressiveness.** "When in maintenance mode, always propose changes before editing" is a behavioral directive that has no YAML equivalent. Traditional config is limited to what the code checks for. NLA config is limited only by what the LLM can understand and apply — which is essentially anything expressible in language.

**Forgiveness.** A missing comma in YAML breaks the parser. A slightly awkward sentence in Markdown config still communicates intent. The LLM handles ambiguity; the conflict detection step catches genuine problems.

**Discoverability.** Users can read their own config and understand it. No key-value lookup, no schema reference needed. The config explains itself.

**Consistency.** In a system where documentation is the application, config should be documentation too. YAML config in an NLA would be an odd break from the "everything is natural language" philosophy.

**The structured end still works.** `framework_base_path: ../nla-framework/` is valid Markdown. Config doesn't need to avoid structure — it just doesn't require it. The spectrum from structured to behavioral is a feature, not a compromise.

### What this enables

Beyond the obvious (user preferences, operator customization), natural language config enables patterns that traditional config can't:

- **Conditional behaviors** — "When processing urgent tickets, skip the formatting review step"
- **Role-based config** — "I'm a senior editor; don't flag style issues, I'll handle those"
- **Workflow modification** — "After every format-article run, automatically log friction"
- **Tone tuning** — "A little less formal than the default voice, but keep it professional"
- **Learning preferences** — "I prefer detailed explanations over terse responses when something goes wrong"

Each of these would require custom code in a traditional app. In an NLA, they're just sentences the LLM reads and applies.

### Open questions

- **Config and Cowork.** The Cowork target (see above) changes the config picture. Cowork users aren't running git, so the "gitignored from app repo" model doesn't apply the same way. Config might live in Cowork's designated folder alongside the project. Need to test how Cowork handles user-specific files.
- **Config migration.** When the app developer updates `config-spec.md` (adds new configurable behaviors, changes defaults), existing user configs may need updating. Should `/preferences` detect spec changes and offer to migrate? Or is this a manual "re-run /preferences" step?
- **Config sharing.** Can users export/import config? "Here's my config for the article formatter, try it." This would be natural (it's just Markdown files) but may have implications for the conflict detection step.

### Config-spec as committed default (no dist file)

When a config directive routes to a sub-config file (e.g., `config/trace-format.md`) that the user hasn't customized, the system needs a default. Traditional code uses a "dist" file pattern — `trace-format.dist.md` (committed) alongside `trace-format.md` (gitignored). This adds parallel files to keep in sync.

**The NLA approach:** The config-spec IS the committed default. `app/config-spec.md` defines what's configurable AND provides default values. If a sub-config file doesn't exist, the LLM falls back to the default described in config-spec. When `/preferences` generates config, it reads defaults from the spec and generates self-contained directives.

This eliminates dist files entirely. One committed source of truth (config-spec), one user-editable space (config/), no parallel files.

---

## Runtime Tracing

*Added 2026-02-12. Tracing is a config behavior, not a skill.*

### Why config, not a skill

Tracing could have been a skill (`/trace on`, `/trace off`). We made it a config behavior instead because:

1. **Tracing is persistent.** A skill invocation is session-scoped. Config persists across sessions. A user who wants standard tracing shouldn't have to remember to run `/trace on` every session.
2. **Tracing has levels.** off/standard/detailed/custom maps naturally to a config directive. A skill would need arguments that duplicate what config already does.
3. **Config is already loaded at startup.** The LLM reads `config.md` before doing any work. Trace directives are active from the first operation, which is exactly when you want them.

### Custom trace levels: an NLA demonstration

The custom trace level is worth highlighting. In traditional logging, you build a framework with predefined levels, category filters, and configuration API. If someone wants "detailed for voice decisions, standard for formatting, off for file loading," they write code.

In an NLA, the user writes that sentence in `config.md` and the LLM does it. No code, no logging framework, no filter API. The same mechanism handles any trace directive expressible in natural language. This is one of the clearest demonstrations of the NLA principle: the LLM interprets intent, so the configuration space is infinite without adding code.

### Observer effect

Tracing changes the system being observed. An LLM narrating its decisions may reason more deliberately than one working silently. We document this in config-spec rather than trying to eliminate it — it's inherent to introspective systems and is analogous to the observer effect in any instrumented system. Users should know that traced sessions are not perfectly representative of untraced sessions.

---

## System Validation (/validate)

*Added 2026-02-12.*

### Why a dedicated skill

NLA debugging is fundamentally different from traditional debugging. There are no syntax errors, no stack traces, no line numbers. Bugs are behavioral — an ambiguous directive in voice-and-values.md that the LLM interprets differently than intended, or a conflict between two docs that surfaces only with certain inputs.

`/validate` provides three tools for this:

1. **Structural validation** — mechanical checks (file references resolve, skill tables consistent). The NLA equivalent of a linter.
2. **Scenario walkthrough** — trace through docs for a hypothetical scenario, narrating each decision. The NLA equivalent of a debugger's step-through.
3. **Debug mode** — given expected vs. actual behavior, trace through docs to explain the divergence. The NLA equivalent of a stack trace.

### Why read-only with handoff

`/validate` finds problems but doesn't fix them. Fixes go through `/maintain` (for doc edits) or `/friction-log` (for capturing observations). This separation exists because:

- **Different guardrails.** Validation is read-only and risk-free. Maintenance has blast-radius concerns and requires proposals.
- **Different decisions.** Finding an issue is mechanical. Deciding how to fix it requires judgment and human approval.
- **Clean handoff.** `/validate` says "this doc has a conflict on line 23." The user decides: fix it now (`/maintain`), log it for later (`/friction-log`), or ignore it.

### Tracing + validate complement

Runtime tracing captures what DID happen during real work. `/validate` analyzes what SHOULD happen based on docs. Debug mode bridges them — it can read trace files to see the actual decision chain, making diagnosis dramatically more reliable than reconstruction from docs alone. This creates a natural incentive: enable standard tracing when debugging, so `/validate` has real data to work with.

---

## Sibling Directory Convention

*Affirmed 2026-02-12. Considered and rejected alternatives.*

### Why we kept the sibling convention

We considered supporting non-standard project locations (projects not at `../project-name/` relative to the framework). The config system made this conceptually easier — `config.md` stores `Framework path:`, providing a declared source of truth.

However, the implementation revealed a tension: `core/skills/*.md` files are shared across all domain projects but contain hardcoded `../nla-framework/` paths. These paths resolve from the domain project's working directory. Making them location-agnostic required either:

1. **Natural language references** ("the framework's `core/nla-foundations.md`") — adds inference overhead to the default case, and path resolution is a mechanical operation where you want reliability, not flexibility.
2. **Template variables** (`{framework-path}/core/...`) — traditional code approach, foreign to the NLA model.
3. **Wrapper-based resolution** — push framework paths into thin wrappers, making them less thin.

All three degraded the common case (sibling projects work perfectly today) to support a rare case (non-sibling layouts). This is a case where traditional code is genuinely easier than an NLA — path substitution is mechanical and deterministic, exactly the kind of thing code handles well and LLMs add unnecessary flexibility to.

**Decision:** Keep the sibling convention for the MVP. The getting-started experience is zero-friction (clone and go), there's no NLA ecosystem requiring a vendor/packages pattern, and the alternatives all involve tradeoffs that aren't justified by current demand.

---

## Skill Invocation: disable-model-invocation on All Skills

*Added 2026-02-18. Discovered during first penny post install.*

### The two effects of the flag

Claude Code's `disable-model-invocation: true` in skill frontmatter has two effects:

1. **Prevents programmatic invocation.** The AI cannot call the skill via the Skill tool — it errors. The AI can still read the skill file with the Read tool and follow it manually.
2. **Removes the skill from the AI's active prompt.** Without the flag, Claude Code adds the skill's description to a system reminder listing "available skills." This reminder actively influences the AI's behavior — it treats listed skills as part of its current toolkit and may spontaneously invoke them.

Effect #2 is more important than #1. The active prompt shapes how the AI reasons about what to do next. A description like "Run periodically" or "Best used at the end of maintenance sessions" reads as an invitation to act without being asked.

### Why all NLA skills should have it

Every NLA skill — framework skills, extension skills (penny post), and domain-specific skills — should set `disable-model-invocation: true`. The reasoning:

- **Mode switches** (`/maintain`, `/plan`) change the AI's operating context. Always user-initiated.
- **Expensive operations** (`/startup`, `/validate`) load many files. The user should opt into the context cost.
- **Observation skills** (`/friction-log`) could cause the AI to interrupt primary work to log things.
- **External actions** (`/write-letter`, `/check-feedback`) post to GitHub Issues or other external services. Spontaneous external actions are especially problematic.

The AI already knows about every skill from CLAUDE.md's skills table. When the user asks for one ("check if there's new feedback"), the AI reads the skill file and follows it. The flag prevents the *active prompt* from nudging the AI toward spontaneous invocation — it keeps the user in control of when skills activate.

### What was tried

We initially removed the flag from penny post's `/check-feedback` and `/write-letter` wrappers, reasoning that they're "action skills" the user explicitly requests (unlike mode switches). This was wrong for two reasons:

1. The skill descriptions ("run periodically," "best used at end of sessions") invite spontaneous invocation.
2. `/write-letter` posts GitHub Issues on other projects — spontaneous external action with real consequences.

The workaround (AI reads the file manually when asked) has minor UX friction but works correctly. The cost is low; the risk of spontaneous invocation is not.

### Blast radius

This applies to all skills in all projects — framework, scaffold, and extensions. It should be documented in the install intent files so that `/create-app` and package installers set the flag consistently.

---

## Adding Decisions

When you make architectural changes to the framework, add an entry here documenting:
- What was decided
- Why (including what alternatives were considered)
- Blast radius (core = all projects, scaffold = new projects, reference = maintainers)

---

*This document is updated by the `/maintain` skill when architectural decisions are made.*
