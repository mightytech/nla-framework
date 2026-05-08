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

> **Superseded 2026-04-15.** The sibling directory convention and the "why not submodules" reasoning were overturned. See "Packages Directory with Git Submodules" below.

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

The framework has its own CLAUDE.md, `/maintain`, and `/friction-log` skills, plus a `reference/` directory. These are full skills (not thin wrappers) because the framework's working directory IS the framework — `../nla-framework/` paths would be self-referential.

**Why full skills instead of wrappers:** The logic files in `core/skills/` use `../nla-framework/core/` paths, designed for domain projects whose working directory is elsewhere. When the working directory is the framework itself, those paths break. Framework skills use project-relative paths (`core/...`, `reference/...`).

### Scaffold Directory (Historical)

The framework originally contained `scaffold/` — a complete working project template with a sample article formatter. It served two roles: manual fallback (copy and customize by hand) and structural reference for `/create-app`.

**Why it was removed:** The scaffold created a dual-maintenance problem. Intent files in `install/` and scaffold files described the same things separately. When the framework evolved, both had to be updated — and they'd drift apart. Making intent files the single source of truth eliminated this duplication. The scaffold's sample content (an article formatter) was extracted as a standalone example NLA repo, accessible via `/install-app`.

### Intent Files as Single Source of Truth

*Added 2026-02-18. Replaced the scaffold directory.*

The `install/` directory contains intent files that describe WHAT a well-formed NLA should have, not literal templates. `/create-app` reads these as its primary structural source; the creation conversation provides domain-specific content. `/install` and `/update` also read them.

**Why intent over templates:** Templates couple generation to a specific domain (the sample article formatter). Intent files are domain-agnostic — they describe sections, structures, and purposes. The AI synthesizes content that fits whatever domain the user described. This is the synthesis principle: same intent, different output for different NLAs.

**Three intent files cover three integration points:** `CLAUDE-intent.md` (runtime identity), `skills-intent.md` (skill wrappers with reference implementations), `structure-intent.md` (directory layout and reference file structures). Together they describe everything the framework provides. Domain-specific content (voice, patterns, task docs) has structural guidance inline in the `/create-app` skill itself, since it's the only consumer.

### /create-app: Conversational Project Creation

`/create-app` asks about the user's domain, voice, and tasks, then generates a tailored project. The first interaction with the framework is itself an NLA interaction — flexible interface on top (conversation), structure underneath (generated project).

**Why conversational:** The user describes what they want; the LLM generates files that fit. This is the structure gradient in action.

**Three generation categories:** (1) Mechanical files generated directly from intent files (skill wrappers, archives, .gitignore). (2) Structured framework files generated from intent + conversation (CLAUDE.md, reference files, config). (3) Domain-specific files generated from conversation only (voice, patterns, task docs), with structural guidance inline in the skill.

**Why framework-only:** Domain projects don't create other domain projects. `/create-app` lives in `.claude/skills/create-app/` (not in `core/skills/`) because it's framework infrastructure, not a universal skill that domain projects delegate to.

### Dual-Mode Framework CLAUDE.md

The framework's CLAUDE.md defaults to project creation (welcoming, directs to `/create-app`). `/maintain` activates maintenance mode. This mirrors the domain project pattern where the default mode is the primary task (content transformation) and `/maintain` switches to system editing.

**Why default to creation:** Most people arriving at the framework want to build something. A maintenance-focused landing page front-loads concepts (blast radius, session lifecycle) that new users don't need yet. Creation mode is welcoming; maintenance mode is available when needed.

**Why this mirrors domain projects:** Domain CLAUDE.md has a default mode (content transformation) and a maintenance mode. The framework CLAUDE.md has the same pattern — default mode (project creation) and maintenance mode. The consistency helps users who've seen one understand the other.

---

## Plugin Export: NLA as Source, Plugin as Artifact

*Added 2026-02-20. Supersedes the earlier "Cowork as a Target Environment" draft (which imagined routing tables and startup banners before the plugin system shipped).*

> **Substantially revised 2026-04-16.** The flattening model described below was
> necessary under the sibling-directory convention. The packages/submodules migration
> (2026-04-15) dissolved that constraint, and `${CLAUDE_PLUGIN_ROOT}` makes intra-plugin
> paths reliable. See "Plugin Export: View-Source Model" below for the current design.
> The *framing* in this section — NLA as source, plugin as artifact; dev tools always
> ship; foundation skill synthesis — still applies. The *mechanics* (flattening,
> per-skill bundling, transitive dependency resolution) have been superseded.

### The compile analogy

The NLA project is source code. The plugin is the compiled artifact. You develop with
the framework's full tooling — maintenance cycle, friction logs, validation, learning
loops. You distribute as a self-contained plugin that anyone can install in Claude Code
or Cowork. To improve the plugin, improve the NLA and re-export.

This separates building from using. The technical person builds the NLA. Anyone can use
the plugin — including non-technical users in Cowork who work with voice, tone, and
content daily but don't use a terminal.

### Why plugins, not a Cowork-specific conversion

The Cowork plugin system (shipped January 2026) uses the same format as Claude Code
plugins: markdown skills with YAML frontmatter, supporting files in skill directories,
a JSON manifest. One export produces a plugin that works in both environments. No need
for platform-specific conversions, routing tables, or skill mimicry — the plugin system
handles discovery natively.

### Why a converter, not dual-target /create-app

`/create-app` generates an NLA project — a development environment with friction logs,
maintenance tools, validation, and a learning loop. A plugin is the distribution artifact
that ships *from* that environment. Conflating them would mean either: (a) plugins carry
dev tools they don't need, or (b) NLA projects lack dev tools to keep plugins clean.
The converter keeps both optimized for their purpose.

(Dev tools DO ship in the plugin — see below — but as a deliberate design choice, not
an artifact of conflation.)

### The structural mapping

The mapping between NLA projects and plugins is nearly 1:1:

| NLA Project | Plugin | Notes |
|------------|--------|-------|
| `.claude/skills/*/SKILL.md` | `skills/*/SKILL.md` | Same format, same frontmatter |
| `app/shared/*` | Supporting files per skill | Bundled into each skill directory |
| `app/[task].md` | Supporting file in skill dir | Bundled into the skill that uses it |
| `CLAUDE.md` | `skills/foundation/SKILL.md` | Synthesized identity with `user-invocable: false` |
| `lib/` | `lib/` | Copied as-is |
| `reference/` | Not shipped | Development records, not runtime |

The main transformation is dependency resolution: flattening the two-hop thin wrapper
pattern (wrapper → framework file) into self-contained skills. Plugins cannot reference
files outside their directory (`../` paths fail after installation), so every dependency
must be bundled.

> **Superseded 2026-04-16.** The table and the "main transformation" description above
> are accurate only for the pre-view-source design. The current mapping preserves
> structure 1:1 (see "Plugin Export: View-Source Model" below for the current table).
> Dependency flattening is no longer needed because `packages/` ships inside the plugin
> and `${CLAUDE_PLUGIN_ROOT}` makes intra-plugin paths resolvable.

### The foundation skill

CLAUDE.md can't be auto-loaded in plugins. A `skills/foundation/SKILL.md` with
`user-invocable: false` is auto-loaded as background knowledge — functionally equivalent
to CLAUDE.md. It synthesizes:

- NLA identity and grounding principles (from CLAUDE.md)
- Behavioral principles (Key Principles 1-7 from nla-foundations.md — NOT the explainer)
- System overview (from app/overview.md)
- Configuration spec (from app/config-spec.md)
- Available skills table

This is a synthesis, not a concatenation. The foundation skill should read as one
coherent identity document in the NLA's own voice.

### Dev tools always ship

Every dev tool (maintain, friction-log, validate) ships in the plugin with
`disable-model-invocation: true`. This was a deliberate design choice driven by three
arguments (and the view-source model added in 2026-04-16 gives a fourth — when the
plugin's structure mirrors the NLA's structure, the dev tools aren't a bonus attached
to the plugin, they're part of what "view source" shows. Shipping them is no longer a
trade-off against plugin cleanliness; the plugin IS the source):

1. **Paradigm evangelism.** The NLA framework demonstrates a new paradigm. Showing the
   maintenance cycle, feedback loop, and validation system is part of the demonstration.
   Like View Source in browsers — it turns users into developers.

2. **Browser dev tools model.** Chrome ships developer tools to everyone. They're hidden
   until opened. `disable-model-invocation: true` means dev skills aren't loaded into
   context — zero runtime cost, present when needed.

3. **Early-stage necessity.** NLAs are new. Things won't always work right. The ability
   to debug and validate in the production environment is essential. Removing dev tools
   is like only putting black boxes on test aircraft.

The only skills excluded from plugins are `/install`, `/update`, and `/export` — framework
tools that are meaningless without the framework. `/startup` is absorbed into
the foundation skill (its purpose — loading context — happens automatically via
`user-invocable: false`).

### Domain skill frontmatter adjustment

Domain skills lose `disable-model-invocation: true` in the plugin. In the NLA project,
the flag prevents spontaneous invocation (CLAUDE.md's skills table provides awareness).
In a plugin, non-technical users say "help me format this" — they don't know about
`/pluginname:format-article`. Removing the flag lets Claude auto-match user intent to
available skills.

Dev and utility skills keep the flag. The foundation skill uses `user-invocable: false`
(always loaded, never explicitly invoked).

### The export is NLA-scoped

The export reads the NLA project's `.claude/skills/` directory as the complete manifest.
The framework's own skills are invisible — it's infrastructure. If penny post is installed
in the NLA, its skills ship. If not, they don't. The export doesn't check for specific
extensions or inspect installed-packages.md. It walks the skill directory and bundles
what's there.

### What gets lost

- **Framework update propagation.** The plugin is a snapshot, frozen at export time.
  `git pull` on the framework doesn't reach it. To get improvements, re-export.
- **The two-hop pattern.** Thin wrappers are resolved and inlined. The indirection that
  enables framework updates is flattened for self-containment.
- **Reference documentation.** Design rationale, session archives, friction log archives
  are development context, not shipped.

### What gets gained

- **Zero-setup distribution.** Install the plugin, start using it. No framework clone,
  no sibling directory setup, no git.
- **Non-technical user access.** Cowork users who would never use Claude Code can use
  NLA capabilities through plugins.
- **The learning loop persists.** Friction-log and maintain ship in the plugin, enabling
  local observation and tweaking. If penny post is installed, write-letter enables
  upstream feedback to the NLA developer.

### LLM self-aware diagnostics

A capability unique to the paradigm: when an NLA plugin user hits friction, the LLM can
explain its own behavior — which instructions it read, what judgment it applied, and what
documentation change might fix it. "I suggested 4/4 time because common-patterns.md
step 3 says [exact quote]. The user appears experienced. Consider rewording to: [proposed
change]." This is a diagnostic with a proposed documentation patch, not just a bug report.

Risks: confabulation (the LLM might construct plausible but inaccurate explanations —
mitigation: include exact quotes, not paraphrases), context window decay (early decisions
may be compressed — mitigation: capture feedback close to the moment), and incomplete
proposals (the LLM has limited context about all cases a doc serves — mitigation: the
Cardinal Rule, the human decides).

This capability lives in the friction-log and write-letter skills, not as a separate
tool. It's a quality characteristic of NLA feedback, not a feature to build.

### Open questions

- **Plugin size.** Bundling shared context per skill creates duplication. At what point
  does this become a practical problem? Worth monitoring but not optimizing prematurely.
- **Plugin versioning.** Should the plugin version track the NLA project's git tags?
  The framework version? Both?
- **Cowork folder instructions.** How do folder instructions interact with the
  foundation skill? Both provide background context. Need to test.

---

## Plugin Export: View-Source Model

*Added 2026-04-16. Supersedes the mechanics (not the framing) of "Plugin Export: NLA
as Source, Plugin as Artifact" above. Origin: friction log entry 2026-04-16 ("/export
may not need to flatten thin wrappers anymore") and feedback item #9 ("Export hybrid
approach: script for mechanical work, AI for judgment"), resolved jointly.*

### What changed

The earlier design flattened thin wrappers and bundled shared context into per-skill
directories. This was necessary when the framework was a sibling directory —
`../nla-framework/` paths couldn't survive in a plugin, so every dependency had to be
inlined. The 2026-04-15 packages/submodules migration changed that: dependencies now
live inside the project at `packages/`, and `${CLAUDE_PLUGIN_ROOT}` makes those paths
resolvable from any installed location (Claude Code and Cowork both substitute the
variable before the LLM reads the skill).

### The new model

Export now produces a **view-source plugin**: the plugin mirrors the NLA's structure
almost 1:1. `.claude/skills/` becomes `skills/`. `app/`, `lib/`, and `packages/` are
preserved. Thin wrappers stay thin — their `packages/nla-framework/...` references
get prefixed with `${CLAUDE_PLUGIN_ROOT}/`, and the wrapped file ships alongside.

Only three things change structurally:
1. `.claude/skills/` is renamed to `skills/` (plugin convention)
2. `CLAUDE.md` becomes `skills/foundation/SKILL.md` (plugins don't auto-load CLAUDE.md)
3. Framework-only skills (`/install`, `/update`, `/export`, `/create-app`) are removed
   and `/startup` is absorbed into foundation — meaningless or redundant in a plugin

Everything else is a path rewrite (adding `${CLAUDE_PLUGIN_ROOT}/` prefixes) and a
frontmatter tweak (removing `disable-model-invocation: true` from domain skills so
non-technical users can auto-invoke them).

### The structural mapping (current)

| NLA Project | Plugin | Notes |
|------------|--------|-------|
| `.claude/skills/*/SKILL.md` | `skills/*/SKILL.md` | Renamed; no flattening; `packages/...` and `app/...` paths prefixed with `${CLAUDE_PLUGIN_ROOT}/` |
| `app/` | `app/` | Preserved at original paths; referenced via `${CLAUDE_PLUGIN_ROOT}/app/...` |
| `packages/` (submodules) | `packages/` (inlined) | Submodule contents archived and embedded; no runtime cloning needed |
| `CLAUDE.md` | `skills/foundation/SKILL.md` | Synthesized identity with `user-invocable: false` |
| `lib/` | `lib/` | Preserved; referenced via `${CLAUDE_PLUGIN_ROOT}/lib/` |
| Non-standard dirs (`voices/`, `platforms/`, etc.) | Preserved | Path rewrites auto-detect top-level dirs and prefix references |
| `reference/` | Not shipped | Development records. Either gitignored in the NLA or marked `export-ignore` in `.gitattributes`. |
| `config.md`, `config/` | Not shipped | Gitignored; plugin user's preferences aren't the developer's |

### Why this is better

- **Inspectable.** A technical user browsing the plugin sees the real NLA structure,
  not a dependency-resolved artifact. Thin wrappers are visible; the files they delegate
  to are visible. Tracing a skill through its wrapper to the framework implementation
  works the same way it does in the NLA itself.
- **Faithful.** Duplication is eliminated. No per-skill copies of `voice.md` or
  `common-patterns.md`. The plugin is closer to what you'd get by cloning the NLA repo.
- **Simpler mechanics.** No transitive dependency resolution. The script rewrites paths
  and does frontmatter surgery; it doesn't need to walk wrapper chains.
- **Local tweaks work.** A plugin user who wants to adjust a shared file (voice, values)
  can edit it once. Under flattening, they would have had to hunt down copies across
  skill directories. This isn't a designed workflow — heavy customization happens by
  editing the NLA and re-exporting — but it's a friendly side-effect.

### Non-technical users are still the primary audience

The shift doesn't change who the plugin is for. Non-technical Cowork users install and
use; they don't open files. What changed is how the plugin treats technical users who
DO look: it shows them the source, not a compiled binary.

### Mechanism: hybrid AI + Python script

Mechanical transforms (`git archive`, submodule resolution via per-submodule archives
piped through tarfile, path rewrites, frontmatter surgery, directory rename,
`plugin.json` generation) are handled by a Python 3 script at `lib/export.py`. Judgment
work (skill classification, foundation synthesis, README writing, verification) stays
with the AI.

The flow: the AI inventories and classifies, writes a manifest JSON, synthesizes the
foundation skill and README and export-metadata, invokes the script, and parses the
status report. The script is stdlib-only (no pip, no venv) and exits non-zero with
structured diagnostics on failure.

Python 3 is a point-of-use requirement — `/export` checks availability at invocation
and offers install guidance if missing. Not a framework-wide prereq.

### What gets lost (unchanged from prior design)

- **Framework update propagation.** The plugin is a snapshot, frozen at export time.
  Changes to the framework or to the NLA don't reach an installed plugin. To update,
  re-export.
- **Reference documentation.** Design rationale, session archives, friction log
  archives are development context and don't ship.

### What gets gained (new)

- **Plugin as inspection medium.** A second "view-source-like" role the prior design
  couldn't support. Someone installing your plugin can learn from its structure as
  well as use its capabilities.
- **Per-skill duplication eliminated.** Shared context lives once.
- **Ejected skills and annotated wrappers need zero special handling.** They ship
  intact. Path rewriting treats them the same as any other skill file.
- **Gitignore drives exclusions for free.** `git archive` honors `.gitignore` and
  `.gitattributes export-ignore` natively. The NLA's own declarations about what's
  private become the export filter — no parallel "don't ship these" list.

### Open questions

- **Plugin size.** Still worth monitoring. View-source inherently ships more than
  strictly necessary (dev tools, framework logic, possibly multiple submodules), but
  duplication of shared context is gone and the net effect is likely smaller plugins
  than the flattening design produced.
- **Permissions in Cowork.** A plugin that reads from its own `packages/` subdirectory
  shouldn't hit cross-directory prompts. Worth confirming on first real export.
- **Foundation skill's "five sources" under view source.** The synthesis may be able to
  be lighter now that `packages/` is visible in the plugin — the foundation doesn't
  need to fully replace `nla-foundations.md`, since that file is shipped. Deferred
  until we see real exports; current design keeps the full five-source synthesis for
  continuity.

---

## The Wrapper Spectrum

*Added 2026-02-20. Emerged from the plugin export design discussion.*

### Four states of a skill wrapper

The thin wrapper pattern enables more than just delegation. A skill wrapper can exist in
four states, each with different update characteristics:

**1. Thin wrapper** — Full delegation to framework. Updates flow automatically via
`git pull`. This is the default state after `/create-app` or `/install`.

```yaml
---
name: startup
---
Read and follow `../nla-framework/core/skills/startup.md`.
```

**2. Annotated wrapper** — Delegates to framework but adds project-specific context.
Framework updates flow for the delegated part; annotations persist.

```yaml
---
name: startup
---
Read and follow `../nla-framework/core/skills/startup.md`.

After standard startup, also check `app/deployment-checklist.md`.
```

**3. Ejected (customized) skill** — Full custom implementation. The wrapper is replaced
with a complete skill file. The NLA takes ownership of the skill logic.

**4. Redirected wrapper** — Points at a different implementation, typically provided by
an extension package. Penny post does this: its installer replaces the write-letter
wrapper with penny post's own version.

### Ejection is not forking

In traditional software, ejecting from a framework means forking — no more updates. In
an NLA, `/update` communicates *intent*, not diffs. When the framework changes a skill's
purpose, the LLM can propose how that intent applies to a customized implementation:

"Your startup already loads voice context and checks for SuperCollider. The framework
now recommends also loading extension context. Here's where that would fit in your
custom implementation, and here's why."

This is the judgment layer doing something deterministic systems cannot: understanding
both sides of a customization boundary and proposing a merge that respects both.

Under the view-source export model (added 2026-04-16), all four wrapper states — thin,
annotated, ejected, redirected — survive export without special handling. Each wrapper
ships intact; the framework file it delegates to ships alongside at
`${CLAUDE_PLUGIN_ROOT}/packages/nla-framework/core/skills/...`. This reinforces the
wrapper pattern's value: the same file that enables `git pull` updates in development
also enables view-source transparency in the plugin.

### Risks of intent-based updates to ejected skills

- **Misunderstanding customization.** A subtle guardrail added for a reason the LLM
  doesn't recognize might be weakened by a merge proposal.
- **Misinterpreting intent.** The framework's new intent might be applied too broadly
  or too narrowly in the custom context.
- **Compounding drift.** Multiple intent-merges over time, each slightly different from
  both the framework's original and the user's customization, create a skill nobody fully
  understands.

The Cardinal Rule applies: the human reviews and approves every merge. But the risks are
worth documenting so that `/update` can flag them when proposing changes to ejected skills.

### The override pattern

Any framework skill can be overridden by redirecting the wrapper to a different
implementation. This is the NLA equivalent of dependency injection — same interface
(the user still says `/write-letter`), different implementation (penny post's GitHub
delivery instead of the base local-file delivery), decided at install time.

No new machinery is needed. The thin wrapper pattern already supports this. The wrapper
just points somewhere else.

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

- **Config and Cowork.** The plugin export model (see "Plugin Export" above) changes the config picture. Cowork users aren't running git, so the "gitignored from app repo" model doesn't apply the same way. Config might live in Cowork's designated folder alongside the project. Need to test how Cowork handles user-specific files.
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

NLA debugging is fundamentally different from traditional debugging. There are no syntax errors, no stack traces, no line numbers. Bugs are behavioral — an ambiguous directive in values.md that the LLM interprets differently than intended, or a conflict between two docs that surfaces only with certain inputs.

`/validate` provides four modes:

1. **Structural validation** — mechanical checks (file references resolve, skill tables consistent). The NLA equivalent of a linter.
2. **Architecture review** — walk the full document chain checking for coherence issues (path resolution, cross-reference integrity, layer boundaries, consistency). The NLA equivalent of a code review.
3. **Scenario walkthrough** — trace through docs for a hypothetical scenario, narrating each decision. The NLA equivalent of a debugger's step-through.
4. **Debug mode** — given expected vs. actual behavior, trace through docs to explain the divergence. The NLA equivalent of a stack trace.

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

> **Superseded 2026-04-15.** Cross-directory permission friction, lack of version pinning, and project non-self-containment made the sibling convention impractical. See "Packages Directory with Git Submodules" below.

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

- **Mode switches** (`/maintain`) change the AI's operating context. Always user-initiated.
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

This applies to all skills in all projects — framework and extensions. It is documented in `install/skills-intent.md` so that `/create-app` and package installers set the flag consistently.

---

## Package Installation: Two Skills, Not One

*Added 2026-02-18.*

### Why `/install` and `/update` are separate

Installation (adding something new) and updating (bringing existing things current) have different risk profiles, different entry points, and different processing flows.

**`/install` is additive.** It reads a package manifest, finds what's missing, and synthesizes new content. The NLA before installation is the baseline — nothing gets modified, only added. The user's main concern is "does this belong in my project?"

**`/update` is transformative.** It modifies content that was previously synthesized. The NLA after a previous install is the baseline — the user needs to understand what's changing in something they already have. The user's main concern is "will this break what I've built on top?"

Different risk profiles warrant different skills, different confirmations, and different log entries.

### The synthesis principle

Intent files describe *what should exist*, not literal text to paste. The installing AI reads the intent and synthesizes it into the NLA — matching voice, structure, and conventions. A formal NLA and a casual NLA should both get the same capability, expressed differently.

This is the same principle as `/create-app`: the framework describes structure, the AI generates content that fits the domain. The intent files are the `/create-app` equivalent for individual capabilities rather than whole projects.

### The install log as source of truth

`reference/installed-packages.md` records what packages are installed, when, in what state, and what was done. This serves three purposes:

1. **`/update` needs it** to detect changes — it compares the logged state against current package state
2. **Humans need it** to understand what came from where — especially when debugging or customizing
3. **History is preserved** — update records are appended, never replacing install records, so the full story is traceable

### Relationship to `/create-app`

`/create-app` bootstraps a new NLA from scratch. `/install` adds capabilities to an existing NLA. They share the synthesis principle (read intent, generate content that fits) but solve different problems:

- `/create-app` has a conversation, asks about domain and voice, generates everything
- `/install` reads a manifest, applies specific intents, logs what was done

`/create-app` generates the initial install log with the framework as the first entry. After that, `/install` and `/update` maintain it.

### Blast radius

Both skills live in `core/skills/` — they affect all domain projects. The thin wrappers follow the standard pattern documented in `install/skills-intent.md`.

---

## Validate Dispatcher + Mode Files

*Added 2026-02-18. Origin: Copydesk Issue #4 (proposal for `/code-review` skill).*

### Why a dispatcher, not separate skills

Copydesk proposed a standalone `/code-review` skill for architecture review. We implemented it as a mode of `/validate` instead, because:

1. **Conceptual unity.** All four modes answer "is my NLA working correctly?" — structural checks, architecture review, scenario walkthroughs, and debug are different lenses on the same question.
2. **Shared setup.** All modes need the same required reading (CLAUDE.md, app/overview.md) and the same scope constraints (read-only, suggest fixes, don't edit).
3. **Wrapper simplicity.** Domain projects have one thin wrapper pointing to one dispatcher. Four separate skills would mean four wrappers in every project.

### Why the dispatcher + mode file split

With four modes, the monolithic `validate.md` grew too large. Splitting into a dispatcher (menu + routing) and mode files (one per mode) keeps each file focused:

- **Dispatcher** (~55 lines): opening, required reading, mode selection menu, routing table, scope constraints
- **Mode files** (~30-60 lines each): self-contained logic for one mode

The dispatcher owns the shared context. Mode files own the analytical logic. This matches the pattern of a traditional router dispatching to handlers.

### Why the hybrid menu

The mode selection menu maps user concerns to system approaches:
- "Are my files wired up correctly?" → Structural check
- "Do my docs tell a consistent story?" → Architecture review
- "Walk me through a scenario" → Scenario walkthrough
- "Something's not working as expected" → Debug

Users think in terms of problems, not modes. The menu translates. When invoked with clear intent, the menu is skipped — the LLM routes directly.

### Architecture review origin

Copydesk ran a manual architecture review after a 6-phase restructuring and found 12 coherence issues that `/validate`'s existing modes didn't catch. The issues fell into categories (path resolution, cross-reference integrity, layer boundaries, consistency, conditional completeness, generic/specific alignment) that are universal to any NLA with multiple doc files. We added prerequisite sufficiency, contradiction, and orphaned content as additional categories.

The architecture review mode is read-only — it produces a findings file that `/maintain` acts on. This respects the separation between analysis and editing.

### Framework validate refactoring

The framework's own `.claude/skills/validate/SKILL.md` was a 140-line monolith that duplicated and extended each core mode. Refactored to delegate to core mode files with framework-specific addenda (blast radius tagging, intent file checks, dual-context scenario tracing). This eliminates dual maintenance — mode logic lives in one place (`core/skills/validate-*.md`), framework extensions live in the wrapper.

### Blast radius

- Mode files (`core/skills/validate-*.md`): all domain projects
- Core dispatcher (`core/skills/validate.md`): all domain projects
- Framework wrapper (`.claude/skills/validate/SKILL.md`): framework only

---

## Update Notes: A Changelog for NLA Packages

*Designed and implemented 2026-02-19.*

### The problem

When the framework changes intent files or core files, domain projects need to update.
`/update` detects changes by diffing git commits and reading current intent files. This
works for mechanical changes — the intent file says what should exist, the project has
something different, the delta is clear.

But some changes carry context that the intent diff alone doesn't convey:
- "We broadened the Cardinal Rule because the old version was transformation-specific"
- "Startup now has an extension point — if you ejected, you can un-eject"
- "NLA Shapes was added to foundations — consider which shape your project is"

These are things the framework maintainer knows at change time that would help the
updating AI make better proposals. Without them, `/update` either misses the nuance
or the project maintainer has to figure it out themselves.

### The design: update notes as changelog

A changelog-style file in `install/` where the framework maintainer writes notes when
making changes that affect domain projects. Each entry provides context that `/update`
reads alongside intent diffs when proposing changes.

**File:** `install/update-notes.md`

**Entry format:**

```markdown
### YYYY-MM-DD — [Brief title]

**Affects:** [which intent files or core files changed]
**Commit:** [optional — a hash for precise anchoring, if convenient]

[Narrative guidance — written for both human readers and the AI running /update.
Not migration steps to execute, but context for judgment. What changed, why,
and what it might mean for different kinds of projects.]
```

**Example entry:**

```markdown
### 2026-02-19 — Cardinal Rule broadened, NLA Shapes added

**Commit:** 25e9c00
**Affects:** core/nla-foundations.md, install/CLAUDE-intent.md, install/skills-intent.md

The Cardinal Rule changed from "the human must always be able to compare changes
against the original and easily revert" to "the human decides." The old framing was
transformation-specific — it assumed an original to compare against. The new framing
is universal across stateless, persistent, and creative NLAs.

Projects with custom Cardinal Rule language in their CLAUDE.md: check whether your
framing is already aligned with the broader principle. If so, no change needed.

NLA Shapes (stateless, persistent, tool-using) was added to nla-foundations.md. This
is loaded by all projects automatically. Consider whether your overview.md reflects
which shape your NLA is.

TK note references were removed throughout — "flag uncertainty" replaces "use TK notes."
Projects using TK conventions in their own docs can keep them (they're domain choices),
but framework-generated references should use the general language.
```

### How /update uses notes

`/update` already knows the project's last-known commit hash from the install log. When
it detects changes:

1. Read `install/update-notes.md` (and the archive if the hash is old enough)
2. Filter to entries between the project's last-known commit and current HEAD
3. Use matching notes as additional context when proposing changes — not as instructions
   to execute, but as maintainer guidance that informs judgment

Notes can cover both intent-file changes (which `/update` acts on directly) and core-file
changes (which propagate automatically via `git pull`). For core-file changes, `/update`
surfaces the note as context — "foundations changed, consider whether your overview
reflects it" — without proposing edits. This gives the project maintainer a complete
picture of what's new, not just what `/update` can mechanically apply.

When there are no notes for a change range, `/update` proceeds as usual. Notes are a
bonus, not a requirement.

The AI exercises judgment about each note's applicability to the specific project. Two
projects updating from the same commit may get different proposals because they're
different projects — different shapes, different customizations, different ejections.
This is non-determinism as a feature: the same update notes, interpreted in context,
produce recommendations tailored to each project.

This is fundamentally different from traditional package updates, where applying a patch
produces uniform results. A traditional update system facing divergent projects either
overwrites everything (dangerous) or refuses to update (useless). The judgment layer
is what makes context-sensitive updates possible — something that was never on the table
with deterministic systems.

The safety model isn't determinism — it's the Cardinal Rule. Every proposed change is
inspectable and rejectable. The human decides.

### How notes are created

During `/maintain` sessions, after changes to intent files or core files that affect
domain projects, the maintainer writes an update note. The maintain skill prompts for
this: "This change affects domain projects. Want to add an update note?"

Notes are written in the moment, when the maintainer has full context about what changed
and why. They're written for a dual audience: humans scanning a changelog, and an AI
that will use the notes as context for update proposals.

Not every change needs a note. Typo fixes, formatting changes, and mechanical
corrections where the intent diff speaks for itself don't need notes. Notes are for
changes where the *so what for your project* isn't obvious from the diff alone.

### Lifecycle and archival

Notes accumulate chronologically, newest first. They don't expire per-project because
different projects may be at different framework versions.

When the file gets long, old entries move to `install/update-notes-archive.md`. The
maintain skill handles this — same pattern as friction log archival. `/update` checks
the archive when a project's last-known commit is old enough that relevant notes might
have been archived. A brief note in the main file: "For notes older than [date], see
the archive."

No prescribed rotation schedule. Maintainers archive when it feels right. The AI can
check the archive when needed. Flexibility over rules.

### What notes are NOT

- **Not migration scripts.** They don't prescribe exact steps. They provide context
  that the AI uses with judgment.
- **Not required.** An update without notes works fine when the intent diff is clear.
- **Not authoritative over intent files.** If a note and an intent file disagree, the
  intent file wins. Notes are context from a moment in time; intent files are the
  current source of truth.

### Alternatives considered

**Bake migration intelligence into /update's general logic.** Rejected — it's
over-engineering for cases that are individually rare. Update notes handle the general
case without adding complexity to the skill itself.

**Use git commit messages as the context source.** Commit messages are brief and
already exist, but they're written for the framework maintainer, not for domain
projects. Update notes are specifically the domain-project-facing view of a change.

**Per-commit note files (like database migrations).** Too granular. A single maintenance
session might produce multiple commits but one coherent set of changes worth one note.
Changelog entries at the session level match how changes are actually made.

**Penny post letters instead of update notes.** Letters are project-to-project
communication about specific situations. Update notes are broadcast guidance for all
projects. Different audiences, different purposes. A change might warrant both — a
note for `/update` and a letter to a specific project that needs extra attention.

### Blast radius

- `install/update-notes.md` (new file): project generation, `/update` behavior
- `core/skills/update.md`: all domain projects (adding note-reading step)
- `core/skills/maintain.md` or `.claude/skills/maintain/SKILL.md`: maintainers (prompting for notes)

### Implementation path

1. Create `install/update-notes.md` with format guidance and seed it with entries for
   recent changes (today's foundations work, the startup extension point)
2. Add a step to `/update` processing flow: after detecting changes, read update notes
   for the relevant range
3. Add a prompt to `/maintain`: after intent file changes, ask about update notes
4. Add archive guidance

---

## Output Spec as Optional Shared Context

*Designed and implemented 2026-02-19.*

### The observation

The framework treats `app/shared/output-spec.md` as a default part of every NLA —
startup loads it, validate checks for it, `/create-app` always generates it. This
originates from the framework's roots in Copydesk (an article formatter) where output
format specification is central.

But NLAs are broader than transformation. A classification NLA's "output" is a label
and a confidence score — a line in the task doc, not a file. A conversational NLA has
no discrete output at all. A creative NLA's output spec is tool-specific (Duet renamed
theirs to `output-spec-sc.md`).

### The decision

Make `output-spec.md` conditional — present when useful, not assumed to always exist.
The file works exactly as before when present; it's just no longer mandatory.

The principle: `output-spec.md` is shared context, like `values.md`, `voice.md`, and
`common-patterns.md`. It prevents duplication when multiple tasks share output format
concerns. When there's one task, or output is simple, the guidance belongs in the task
doc and the file is skipped.

### Changes required

Eight references across five files, all expressing the same idea:

| File | Line | Change |
|------|------|--------|
| `core/skills/startup.md` | 9 | Add "(if it exists)" — same pattern as config.md |
| `core/skills/validate-structural.md` | 13 | Only flag if referenced but missing, not if absent entirely |
| `core/skills/maintain.md` | 91 | Add "(if it exists)" to downstream effects table |
| `core/skills/maintain.md` | 212-218 | Condition the "Updating the Output Spec" section |
| `.claude/skills/create-app/SKILL.md` | 156 | Mark as conditional in Category 3 table |
| `.claude/skills/create-app/SKILL.md` | 185-189 | Note it's for complex/shared output; simple output goes in task doc |
| `.claude/skills/create-app/SKILL.md` | 205 | Add "(if needed)" in generation order |
| `install/structure-intent.md` | 20 | Mark as optional in directory tree |
| `.claude/skills/create-app/SKILL.md` | 195 | Task doc prerequisites — make output spec conditional |
| `install/skills-intent.md` | ~181 | Domain skill pattern — make output spec prerequisite conditional |

### /create-app heuristic

The conversation flow already asks about output format (information target #5). The
change is that the answer doesn't always become a file:

- Multiple tasks sharing output format → create output-spec.md
- One task with complex output → AI uses judgment
- Simple output or conversational NLA → guidance goes in task doc, skip the file

### Blast radius

- `core/skills/startup.md`, `validate-structural.md`, `maintain.md`: all domain projects
- `.claude/skills/create-app/SKILL.md`: project generation
- `install/structure-intent.md`: project generation, `/install`, `/update`

Existing projects with output-spec.md are unaffected — the file still works. Projects
without one stop being flagged as incomplete.

### Why this matters beyond output-spec

This is part of a broader pattern: the framework was designed around a transformation
NLA and some of its defaults assume that shape. Making output-spec.md conditional is
one step toward a framework that fits all NLA shapes equally well, without removing
anything that works for transformation NLAs.

---

## Lessons from First Cross-NLA Feedback Session

*Added 2026-02-19. Origin: Duet's 11-item feedback letter processed in session `reference/sessions/2026-02-19-duet-feedback-and-update-notes.md`.*

### What happened

Duet (a persistent, creative, tool-using NLA) sent an 11-item feedback letter exposing transformation-NLA assumptions throughout the framework. Processing it produced three evolution principles:

1. **Broadening over adding.** Most fixes removed constraints rather than added features. The Cardinal Rule changed from transformation-specific ("compare against the original") to universal ("the human decides"). NLA Shapes replaced assumptions with explicit categories. Output-spec became optional. The pattern: when the LLM behaves too narrowly, loosen the language rather than adding more rules.

2. **The feedback-to-resolution pipeline works.** Penny post letter → triage → item-by-item processing → session log → close is a repeatable workflow. The 11-item letter processed cleanly in one session with full traceability.

3. **Proportional resolution.** Not every gap needs a full implementation. Item 8 (deeper `/create-app` questions) got a light touch — one line in the conversation groupings — because the root cause (framework not recognizing NLA shapes) was addressed in foundations. Match the fix to the gap.

### What this means for the framework

The framework was built around Copydesk (an article formatter — stateless, transformation-focused). Duet was the first non-transformation NLA to provide systematic feedback. The session confirmed that NLA-general language is achievable without losing transformation-NLA utility — broadening the Cardinal Rule didn't weaken it for Copydesk, it just stopped excluding Duet.

This is evidence for the design principle: when in doubt, broaden rather than specialize. The LLM applies judgment regardless; narrow language just constrains which judgment it applies.

### Blast radius

Reference only — this entry captures lessons, not operative changes. The operative changes (foundations, validate, maintain) are recorded in their respective files and the session log.

---

## Removing the /plan Skill

*Added 2026-02-19. Origin: Observation during the Duet feedback session that /plan was never invoked.*

### What was decided

Remove `/plan` as a standalone skill. Fold its unique design thinking concepts (structure
gradient, learning loop design) into `/maintain`'s Principle 2. Let Claude Code's built-in
plan mode handle implementation planning.

### Why

During the Duet feedback session — a full-day maintenance session with significant design
work — the `/plan` skill was never invoked. Its NLA design thinking concepts (blast radius,
downstream effects, structure gradient) were used constantly, but through `/maintain`'s
existing principles. Claude Code's plan mode handled implementation planning and was
described by the user as "really, really helpful." The two tools complemented each other
naturally without the framework's `/plan` skill being involved.

The `/plan` skill's unique content was: structure gradient (where does the human need
flexibility / where does the LLM add structure / where does code handle things) and
learning loop design (how will we know this works). Everything else was already in
`/maintain`. Folding these two concepts into Principle 2 preserves the behavior while
eliminating a redundant entry point.

### Alternatives considered

1. **Rename to /design** — eliminates name collision with Claude Code plan mode, clearer
   purpose. Rejected because the behavior was already delivered by maintain + plan mode;
   a rename doesn't address the redundancy.
2. **Keep but clarify** — add documentation distinguishing it from Claude Code plan mode.
   Rejected because a skill that exists but never gets used is worse than no skill.
3. **Merge into /maintain** (chosen) — fold unique content, remove the skill. Cleanest
   option with the least surface area.

### Blast radius

- All domain projects: orphaned `/plan` wrapper needs manual removal
- Install/skills-intent: `/plan` section removed, affects project generation
- Core/maintain: enriched with folded content, affects all projects using /maintain
- First framework skill removal — enriched `/update`'s removed-intents guidance

---

## Collaborative Design Exploration (/think)

*Added 2026-02-21. Origin: friction log entry "Need a 'thinking it through' mode for
design exploration" (2026-02-20), observed during the plugin export design session.*

### What was decided

Create a lightweight skill (`/think`) that establishes space for collaborative design
exploration — the what/why phase before planning (how) and implementation. The skill
is deliberately short (~90 lines) because the AI is already good at collaborative
thinking when it knows that's its job. The value is in signaling, posture, and
transition — not procedure.

### Why a skill, not general guidance

General context in CLAUDE.md or foundations competes with everything else the AI
attends to. A skill — even non-invokable — creates a discrete moment: the AI
recognizes "this needs exploration" and suggests it, or the human invokes it directly.
When loaded, the skill's posture guidance actively shapes the conversation.

Evidence from penny post: the AI knows write-letter exists and suggests it at the
right moment. But the quality of the letter comes from loading the skill file. Without
it, the AI writes a letter, but a worse one. The same applies to thinking — without
the skill, the AI can explore collaboratively but drifts toward action because nothing
is actively saying "stay in this space."

### Why lightweight

The plugin export design session (2026-02-20) demonstrated that the best design
thinking happened through open-ended conversation, not structured decision-making.
The AI's corrections came from the human pushing back on framing. A heavy, procedural
skill would formalize what works precisely because it's informal.

The skill provides: posture nudges (bring expertise, be transparent, resist premature
convergence), a named practice for keeping conversations open ("Thoughts? Concerns?
Ideas? Questions?"), and a transition checkpoint for moving to planning. That's it.

### The four-phase flow

The skill completes a four-phase workflow that emerged from practice:

1. **Think** (`/think`) — explore what to build and why
2. **Plan** (Claude Code plan mode) — design how to implement
3. **Implement** (`/maintain` or direct editing) — make the changes
4. **Debrief** (`/debrief`) — reflect on the process

Not every task needs all four phases. Mechanical fixes skip to implementation. Clear
requirements skip to planning. The phases exist so the AI knows when to suggest each
one and the human knows what's available.

### Relationship to /plan (removed 2026-02-19)

`/plan` was removed because it overlapped with both `/maintain` and Claude Code plan
mode. Its unique content (structure gradient, learning loop design) was folded into
`/maintain`'s Principle 2. `/think` fills a different gap — not the overlap `/plan`
occupied, but the space before it. `/plan` tried to be both design thinking and
implementation planning. `/think` is purely the former; Claude Code plan mode is
purely the latter.

### The self-referential design session

The `/think` skill was designed using the process it describes. The session began with
open-ended exploration ("what's the gap?"), evolved through reframings ("the posture
is more important than the process," "less code, better results"), and transitioned
naturally to planning when shared understanding was sufficient. The conversation itself
became evidence for what the skill should enable.

### Alternatives considered

1. **Guidance in maintain.md only** — just expand Principle 2. Rejected because general
   context doesn't get prioritized when it matters most. The AI needs an active signal
   to enter thinking posture.

2. **Guidance in nla-foundations.md** — add a section on design thinking. Rejected
   because foundations is conceptual (what NLAs are), not procedural (how to work with
   them). Design thinking is a practice, not a concept.

3. **A heavy, procedural skill** — required reading, structured phases, artifact
   production. Rejected because the evidence (plugin export session, this session) shows
   that the best thinking happens through informal conversation. Formalizing it would
   kill it.

### Blast radius

- `core/skills/think.md`: all domain projects (new skill available via thin wrapper)
- `core/skills/maintain.md`: all domain projects (brief reference to thinking phase
  added to Principle 2)
- `install/skills-intent.md`: project generation (new projects get /think wrapper)

---

## Post-Work Reflection (/debrief)

*Added 2026-02-21. Origin: friction log entry "Post-session reflection as a skill"
(2026-02-21), evidence from penny post's post-update reflection producing 11-item
feedback letter with 3 accepted items.*

### What was decided

Create a lightweight skill (`/debrief`) for collaborative reflection after substantive
work. The skill completes the four-phase flow established by `/think`: think (what/why)
→ plan (how) → implement → debrief (reflect). Like `/think`, it's deliberately short
(~100 lines) because the AI is already good at reflection when it knows that's its job.

### Why lightweight

The evidence is the penny post session: a single open-ended question ("think about what
we just went through") produced an 11-item feedback letter. No procedure, no template.
The AI was present for everything — it has the context. What it needs is permission and
posture, not instructions.

But debrief is differently shaped than think. Think is open-ended exploration — it can
go anywhere. Debrief has direction: look back, surface observations, refine
collaboratively, then suggest where observations should land. More directional, but
the observations themselves are freeform.

### Three design decisions

**1. Transition-sensitive triggers.** The AI suggests debrief when it senses a context
shift between tasks or projects — not wired into other skills' closing steps. This
avoids maintaining "suggest /debrief" in every skill that might warrant reflection, and
lets the AI judge when reflection would be valuable. A batch of related tasks gets one
suggestion at the end; three unrelated tasks get three.

The prompt is low-cost: "Sounds like we've wrapped up this task — want to debrief?"
The user can say no or ignore it.

**2. Judgment-based handoff.** The skill produces refined observations. Those need to
land somewhere — /friction-log (self-directed) or /write-letter (upstream feedback).
But the routing is judgment, not mechanism. The AI suggests the natural next step based
on what emerged: "Three of these are about our own docs — want me to log them? The one
about the framework's update flow would make a good letter." The skill doesn't own the
capture step — it makes clear that observations should land somewhere and trusts the AI
to know the destinations.

**3. Two dimensions of reflection.** Process (ambiguities, inefficiencies, missing
steps) and human experience (did the session feel right? too many confirmations?
signs of fatigue?). The second dimension is uniquely available to the AI as
participant-observer — it can surface things the human might not consciously articulate.

### The "Thoughts? Concerns? Ideas? Questions?" correction

During the design session for this skill, a misunderstanding of the named practice
from `/think` was identified. "Thoughts? Concerns? Ideas? Questions?" was being used
as a conversation closer directed at the human ("your turn"). The intended pattern is
the opposite: it's an invitation for the AI to share ITS thoughts, concerns, ideas,
and questions in response to what the human just said. The human's response IS the
prompt; the AI treats it as if the human had asked for its perspective.

This affects `/think`'s "Keep the conversation open" bullet, which currently reads as
"ask the human" — the misinterpretation. Logged in the friction log for resolution.

### Alternatives considered

1. **Wire into other skills' closing steps.** Add "suggest /debrief" to maintain's
   session close, update's completion, etc. Rejected because it creates maintenance
   burden (every skill needs to know about debrief) and presumes which work is
   "substantive enough." The AI can judge transitions better than a checklist.

2. **Heavier procedural skill.** Required reading, structured output format, routing
   tables. Rejected for the same reason /think is light — the evidence shows the best
   reflection comes from informal conversation, not procedure.

3. **Fold into /maintain's session close.** Just add a reflection step to the session
   lifecycle. Rejected because debrief applies beyond maintenance — after updates,
   exports, create-app runs, domain task execution. It's a general capability, not a
   maintenance-specific step.

### Blast radius

- `core/skills/debrief.md`: all domain projects (new skill available via thin wrapper)
- `install/skills-intent.md`: project generation (new projects get /debrief wrapper)

---

## Conversation Structure as Facilitation Technique (/unpack)

*Added 2026-02-21. Origin: friction log entry "Conversation structure skill: slow
your roll" (2026-02-21), observed during the /debrief design session where chunked
discussion was highly effective.*

### What was decided

Create a lightweight skill (`/unpack`) that structures complex conversations by
identifying bundled threads and working through them sequentially. The skill layers
on top of whatever's already active — it's a facilitation technique, not a mode
switch.

### Why a skill, not a behavior in foundations

Two reasons, both grounded in observed behavior:

1. **Context decay.** As conversation context grows, principles in foundations get
   fuzzed out — specific behaviors fade. A skill gets re-read when invoked, putting
   guidance at the top of the context pile. This is the same dynamic that makes
   `/think` and `/debrief` more effective as skills than as general guidance.

2. **User preference, not universal imposition.** The chunked pattern is one way of
   working. Others might prefer everything at once, or questions written to a file
   for annotation. A skill keeps the technique available without imposing it on every
   NLA user.

### A new category: facilitation techniques

The existing skills fall into two categories: **phase skills** (/think, /debrief,
/maintain) that define what stage of work you're in, and **action skills** (/validate,
/export, /friction-log) that perform a specific operation. `/unpack` is neither — it's
a **technique skill** that structures how a conversation proceeds regardless of what
phase or action is active.

This is potentially the first of a category. Facilitation techniques (brainstorming,
card sorting, naming exercises) are process interventions that work regardless of
subject matter — the same shape as `/unpack`. The framework doesn't need to design
the category yet; let the pattern emerge from practice. But the precedent is worth
noting: technique skills layer on active context rather than replacing it.

### Composability: skills can layer

Nothing in the framework prevents two skills from being active simultaneously.
Skills are markdown files the AI reads and follows. `/think` establishes a posture;
`/unpack` establishes a conversational structure. These compose naturally — the AI
follows both. This was already happening informally (the AI follows session log
conventions while in `/maintain`), but `/unpack` makes it explicit.

### Naming

`/unpack` was chosen over several alternatives explored in the /think session:

- `/chunk` — clear about method, but sounds like breaking content into pieces rather
  than managing conversation flow
- `/structure` — too broad; everything in the framework is about structure
- `/untangle` — implies the conversation is messy, which isn't always the case
- `/slow-down` — sounds like criticism rather than methodology
- `/focus` — implies narrowing to one thing; this is about all the things, sequentially

`/unpack` captures the action: take something bundled, lay out the pieces, work
through them. "Let's unpack this" is natural conversational language.

### Adaptive state tracking

The skill tracks progress visibly but adapts format to scale. A few items get names
("naming done, scope still to go"). Many items get counts ("5 resolved, 3 to go").
This follows the framework principle: structured underneath, flexible on top.

### Alternatives considered

1. **General guidance in nla-foundations.md.** Rejected — principles fuzz out as
   context grows, and this imposes one collaboration style on all users.

2. **Part of /think.** Rejected — /think worked this way in the debrief session
   because the friction log had pre-decomposed the problem. In open-ended
   exploration, forcing "identify your starter questions" too early is premature
   structure.

3. **Session log enhancement.** Rejected — the value is in real-time conversation
   management, not post-hoc recording. The session log is a side effect.

### Blast radius

- `core/skills/unpack.md`: all domain projects (new skill available via thin wrapper)
- `install/skills-intent.md`: project generation (new projects get /unpack wrapper)

---

## Values and Voice Separation

*Added 2026-02-22. Origin: friction log entry "Voice and values may need splitting;
values as transparent ethics" (2026-02-19), designed in /think session
(reference/sessions/2026-02-22-voice-values-design.md).*

### What was decided

Split `app/shared/voice-and-values.md` into two files: `values.md` (loaded at startup
as infrastructure) and `voice.md` (task-level shared context). Add "Values Are Visible"
as a new principle (#3) in nla-foundations.md.

### Why

Voice and values have different lifecycles and different scopes:
- **Voice** varies by context — the same NLA could use different tones for different
  audiences. It shapes content production.
- **Values** are stable across all contexts — you don't have different ethics for
  different audiences. They shape every decision, including maintenance proposals.

Bundling them hid this distinction. The split makes values infrastructure (always
present, loaded at startup) and voice task-level (loaded when producing content).

### Values as infrastructure

Loading values at startup enables "soft contradiction flagging" across the entire
lifecycle — the AI can surface tensions between a maintenance proposal and the NLA's
stated values ("This would prioritize X over Y — your values doc says Y comes first.
Are you sure?"). This awareness was impossible when values were only loaded as task
prerequisites.

Values range from stylistic preferences ("keep it concise") to legal requirements
(HIPAA compliance, accessibility). The mechanism is the same; the stakes differ.

### Values transparency as a principle

Traditional code embeds the same value choices (what gets prioritized, what gets
filtered, who gets served) but hides them in logic. NLAs state them in prose:
readable, debatable, modifiable. There is no neutral default — silence defers to
model defaults. Making values explicit is what distinguishes an NLA that *has* values
from one that merely inherits them.

This is the third Key Principle in nla-foundations.md, sitting between "Judgment Over
Rules" and "The Cardinal Rule." The flow: explain why (#2) → your docs embed values
whether you intend to or not (#3) → the human decides (#4).

### Multiple voices

One or more voice files in `app/shared/`, self-contained, referenced by task docs.
This is a supported pattern, not an engineered feature — no routing tables, no voice
registry. Task docs reference the voice file they need. Values remain singular: one
set per NLA.

### Create-app approach

Light touch: one tradeoffs-oriented question during conversation, seeds `values.md`
with a sentence or two. The maintenance cycle refines. This follows the pattern of
starting minimal and iterating — the same principle as common-patterns.md.

### Backward compatibility

No fallback for the old `voice-and-values.md` filename. Migration is via update notes
and `/update`. The affected population is small (three domain projects); the clean
break avoids dual-file ambiguity.

### Alternatives considered

1. **Keep the combined file.** Rejected because the loading distinction (values at
   startup vs. voice at task level) requires separate files. A combined file either
   loads everything at startup (wasting context on voice during maintenance) or loads
   nothing at startup (losing values awareness during maintenance).

2. **Values in CLAUDE.md.** Rejected because values are domain content that evolves
   through the maintenance cycle. CLAUDE.md is infrastructure that changes rarely.

3. **Values in nla-foundations.md.** Rejected because foundations is framework-level
   (shared across all projects). Values are project-specific.

4. **Graceful fallback for old filename.** Rejected — adds backward-compatibility
   complexity to startup for a rare case. Update notes + `/update` handle migration.

### Blast radius

- `core/nla-foundations.md`: all projects (new principle, renumbering)
- `core/skills/startup.md`, `maintain.md`, `validate-*.md`, `preferences.md`,
  `export.md`, `friction-log.md`: all projects (reference updates, new behavior)
- `install/` intent files: project generation and `/update`
- `.claude/skills/create-app/SKILL.md`: project creation

---

## Moving Process Helpers to a Package (/unpack)

*Added 2026-02-22. Origin: voice/values debrief observation that /unpack represents
a different category of skill, followed by a /think session exploring core vs. package.*

### What was decided

Move `/unpack` from `core/skills/` to a standalone NLA package (`nla-process-helpers`).
Phase skills (/think, /debrief) remain in core. The process helpers package is the
second NLA extension after penny post.

### Why

The /think session identified a key distinction:

**Phase skills define *when* in the work lifecycle.** /think (before planning), /debrief
(after work) — these are universal. Every NLA does work. Every NLA has a lifecycle.

**Process helpers define *how* within conversations.** /unpack (sequential
thread-by-thread) is one approach to managing complex conversations. Others are
equally valid: document-for-inline-annotation, everything-at-once-and-steer,
structured Q&A. How you manage conversations is a preference, not infrastructure.

The reframing that clinched it: "unpack is useful across sessions — but it's also the
way *I* like to work. I can imagine other people preferring different ways." When a
skill reflects a personal working style, it belongs in an installable package where
users opt in.

An analogy: phase skills are "what meeting are we in?" (standup, retrospective). Process
helpers are "what facilitation technique are we using?" (round-robin, parking lot, dot
voting). You always need meetings. You choose your facilitation style.

### The update path

Domain projects with `/unpack` wrappers pointing to `../nla-framework/core/skills/unpack.md`
need to either:
1. Install the process helpers package and redirect the wrapper to
   `../nla-process-helpers/app/unpack.md`
2. Remove the wrapper if they don't use /unpack

This is the redirected wrapper pattern (state 4 in the wrapper spectrum) — the same
mechanism penny post uses with `/write-letter`.

### Selective installation (future direction)

When the package has multiple techniques, users should be able to choose which ones to
install. This would be a general `/install` enhancement, not specific to process helpers.
Not implemented yet — with one technique, there's nothing to select.

### Blast radius

- `core/skills/unpack.md`: deleted (was: all domain projects)
- `install/skills-intent.md`: /unpack section removed (affects project generation)
- `CLAUDE.md`: /unpack removed from skills table, process-helpers added to key files
- Domain projects with /unpack wrappers: need redirect or removal via `/update`

---

## Context Determines Competence

*Added 2026-02-22. Origin: /think session designing /check-updates and /update
enhancement for cross-package update management.*

### The principle

The AI's ability to make good judgment calls is bounded by the project context it
has loaded. When operating as Duet's maintainer, the AI has Duet's voice, values,
structure, and conventions. It can synthesize framework intents into Duet because
it understands Duet. It cannot resolve a merge conflict in penny post's files
because it doesn't have penny post's development context — it doesn't know what
changes were intentional, what's in progress, or what the maintainer's reasoning was.

**Mechanical operations can cross context boundaries.** A fast-forward merge, a
file copy, a git fetch — these don't require judgment. Moving a pointer forward
is safe regardless of what context is loaded.

**Judgment operations cannot.** Synthesizing intent files into an NLA, resolving
merge conflicts, proposing documentation changes — these require understanding the
project being modified. The AI should only attempt them when it has that project's
context loaded.

### Why this matters

This principle emerged from designing the update pipeline. An NLA can have multiple
upstream dependencies (framework, penny post, process helpers). Updating them involves
operations at different levels:

1. Fetching remote changes to a package's local clone (git operation, mechanical)
2. Applying a package's intent changes to the NLA (synthesis, requires NLA context)
3. Resolving conflicts in a package's own files (judgment, requires package context)

Operation 1 is safe from any context. Operation 2 requires the NLA's context.
Operation 3 requires the package's context. The update skill can handle 1 and 2
(it runs in the NLA's context). It should refuse 3 and direct the user to work
in the package's context.

### The fast-forward boundary

The specific mechanism that makes this concrete: git fast-forward merges.

A fast-forward means the local branch is strictly behind the remote — no local
changes, no divergence, no judgment needed. The AI can safely perform this from
any context because it's pointer movement, not content resolution.

A non-fast-forward means histories have diverged. Someone made local changes that
need to be reconciled with remote changes. This is a judgment call that requires
understanding both sides — which means being in that project's context.

The rule: **fast-forward = mechanical = safe across contexts. Non-fast-forward =
judgment = requires the right context.**

### Broader applicability

This principle isn't limited to git operations. It applies whenever the AI operates
across project boundaries:

- **Plugin export** reads NLA files from the NLA's context — safe, because it's
  reading, not modifying the source
- **Penny post letters** describe observations from one context to another — the
  receiving project's maintainer applies judgment in their own context
- **Package installation** clones and reads a package, then synthesizes into the
  NLA — the judgment happens on the NLA side, where context is loaded

The pattern: gather information across boundaries freely, but apply judgment only
where you have context.

### Risks

- **False confidence in mechanical operations.** A fast-forward is safe at the git
  level, but the fetched changes might have implications the AI doesn't understand
  without context. Mitigation: fast-forward only updates the package's files — the
  NLA synthesis step (where implications are assessed) still happens in the NLA's
  context with full judgment.

- **Context boundaries aren't always obvious.** An NLA might have deeply customized
  a package's files (ejected wrappers, local patches). The AI might not recognize
  that a "mechanical" operation is actually touching something that needs judgment.
  Mitigation: the rollback branch makes any operation reversible.

---

## Update Pipeline: /check-updates and /update Enhancement

*Added 2026-02-22. Origin: /think session exploring how users check for updates
across the NLA and all packages.*

### What was decided

Create `/check-updates` as a read-only scan skill. Enhance `/update` to handle the
full update lifecycle: pull remotes (fast-forward only), then apply intent changes.
Add a rollback branch for safety.

### Why /check-updates is separate from /update

The same pattern as `/validate` vs `/maintain`: one skill analyzes (read-only, safe,
low-cost), another acts (transformative, requires approval, has blast radius).
`/check-updates` tells you where you stand. `/update` acts on it.

This separation matters because checking is safe to run anytime — at startup, mid-session,
just to see. Acting requires commitment: rollback branches, proposals, approvals. Bundling
them would make the check feel heavyweight and discourage casual use.

### Why the rollback branch covers the whole session

One branch, created before any operations, covers everything: remote pulls, intent
applications, downstream fixes. Alternatives considered:

- **Per-package branches** — more granular rollback. Rejected: too many branches, and
  the operations are conceptually one update session.
- **No rollback (rely on git reflog)** — simpler. Rejected: reflog requires git expertise,
  and the Cardinal Rule says make reversal easy.

### The two-phase flow

Phase 1 (pull remotes) is mechanical — no judgment, no synthesis. Phase 2 (apply intents)
is judgment — requires the NLA's context. Separating them makes the "Context Determines
Competence" principle operative: all mechanical work happens first, all judgment work
happens after, each in the appropriate mode.

### Scope disambiguation

When multiple things need updating and the user doesn't specify, `/update` asks rather
than assuming "all." This follows the Cardinal Rule — the user decides what gets updated.
When only one thing needs updating, it proceeds (after confirming). The principle:
reduce friction for the common case, add a question for the ambiguous case.

### Blast radius

- `core/skills/update.md`: all domain projects (major revision)
- `core/skills/check-updates.md`: new skill, all projects via thin wrapper
- `core/skills/startup.md`: all projects (config-gated, off by default)
- `install/skills-intent.md`: project generation
- `config-spec.md`: framework config

---

## Package-Framework Dependency Direction

*Added 2026-02-23. Origin: designing the friction log communication path for
non-maintainer users.*

### The principle

Packages own capabilities. The framework owns awareness and timing. The AI
bridges them. No coupling needed.

This is the `requests` library pattern: `requests` knows how to make HTTP calls
but doesn't decide when your app should make one. Similarly, penny post's
`/write-letter` knows how to compile friction entries into a letter — that's a
capability. The framework's startup skill knows when to surface "you have pending
friction entries" — that's awareness. Neither references the other directly. The
AI sees both and connects them naturally: "you can use `/write-letter` for that."

### What this means in practice

**Framework code never names a package.** Startup says "share with your
maintainer," not "use `/write-letter`." If the skill is available, the AI
mentions it. If not, it suggests sharing the file directly. The graceful
fallback is built into the intent-level language, not coded as an if/else.

**Packages can assume framework infrastructure.** Penny post depends on the
framework, so it can assume every NLA has a friction log. It doesn't need to
check — `reference/friction-log.md` is framework infrastructure. The package
builds capabilities on top of guaranteed foundations.

**The AI is the integration layer.** Traditional packages need explicit
integration points — hooks, events, adapters. In an NLA, the AI reads the
skills table, understands what's available, and suggests the right tool for the
moment. No wiring needed. This is the LLM doing what LLMs do: understanding
context and making connections.

### Why not package intent files

We considered having penny post's intent files tell domain projects to add
startup nudges. But domain projects don't customize startup based on which
packages are installed — they delegate to the framework's startup skill via
thin wrappers. The framework change propagates automatically. Package intent
files describe what the package adds to the project (skills, docs), not how
the framework should behave.

### Blast radius

Reference only — this is a principle, not an operative change. The operative
changes (startup awareness, friction-log session awareness) are recorded in
the session log.

---

## Permission Management Model

*Added 2026-03-04.*

### The problem

Claude Code prompts for permission on every external directory access. NLAs
routinely read from sibling directories — the framework (`../nla-framework/`),
packages (`../nla-penny-post/`), and domain data directories (`../duet-music/`).
A project with many thin wrapper skills triggers prompts on nearly every skill
invocation. The accumulated ad-hoc approvals produce messy settings files —
garbled entries, duplicates, overly specific patterns (50-80 entries per project).

### What was decided

Permissions are declared in package intent files and generated into project
settings files by existing skills. No new skill — three existing integration
points handle the lifecycle:

- **`/create-app`** — generates initial `.claude/settings.local.json` at project
  creation, with framework reads and broad bash patterns pre-approved
- **`/install` + `/update`** — proposes permission entries when packages declare
  needs in their manifests, appends to the settings file
- **`/validate`** — checks declared needs against actual settings, reports gaps

### Tiered placement

| What | Where | Why |
|------|-------|-----|
| Framework reads | Project-level `settings.local.json`, absolute path resolved at generation | Every NLA needs this; user-wide documented as optimization for multi-project users |
| Package reads | Project-level `settings.local.json`, relative paths | Per-project; varies by NLA |
| Domain data dirs | Project-level `settings.local.json`, relative paths | Per-project; unique to each NLA. Not yet handled by skills — declared in project config, added manually. Candidate for future `/create-app` integration. |
| Common bash (`git:*`, `ls:*`, `test:*`) | Project-level `settings.local.json` | Pre-empts the most common prompt noise |
| Write operations | Manual approval | Safety — writes have consequences |

### Why settings.local.json, not settings.json

`settings.local.json` is gitignored by Claude Code by default. Permissions
contain absolute paths (for the framework entry) and are machine-specific.
Checked-in `settings.json` is documented as a team option when all developers
share the same directory layout — but the default protects against accidentally
committing machine-specific paths or making permission decisions for others.

### Why not a new skill

Permission management is a property of packages, not a standalone workflow.
It fits naturally into the existing package lifecycle: packages declare needs,
install/update processes them, validation catches drift. A `/permissions` skill
would be invoked rarely and in contexts where one of the three existing skills
is already active.

### The declaration format

Each package's `install.md` manifest includes a "Permissions" section with a
table of Claude Code permission patterns, purpose descriptions, and
required/optional classification. Same format everywhere — framework, packages,
standalone NLAs. The installing skill reads the table and proposes corresponding
entries in the NLA's `settings.local.json`.

### Migration path

Existing projects adopt through `/update`: the framework update introduces
permission declarations in its own manifest, `/update` detects the new section,
and proposes generating `settings.local.json`. Existing packages add permission
sections to their manifests — the framework's update notes communicate this to
package maintainers. Domain projects pull package updates and get permission
proposals alongside other intent changes. Each layer learns about permissions
through `/update` from the layer above.

### Blast radius

- `install/` — New sections in `install.md`, `structure-intent.md`, `package-intent.md`
- `core/skills/` — Changes to install.md, update.md, validate-structural.md,
  startup.md
- `.claude/skills/create-app/` — Settings file generation
- All existing projects — via update notes; migration is optional (projects work
  without it, they just see more permission prompts)
- All existing packages — should add permission declarations to their manifests

> **Superseded 2026-04-15.** The packages/submodules model eliminates cross-directory reads entirely, making Read permission management unnecessary. Bash patterns (`git:*`, `ls:*`, `test:*`) remain relevant. See "Packages Directory with Git Submodules" below.

---

## Packages Directory with Git Submodules

*Added 2026-04-15. Supersedes Sibling Directory Convention, the "why not submodules" reasoning in Dual-Source Architecture, and the cross-directory Read portion of the Permission Management Model.*

### What was decided

Replace the sibling directory convention (`../nla-framework/`, `../nla-package/`) with a `packages/` directory using git submodules inside each NLA project. Every NLA — including the framework itself — keeps its dependencies in `packages/` as shallow-cloned submodules with HTTPS URLs. Dependencies are flat (not nested): `git submodule update --init` (without `--recursive`) clones only direct dependencies.

### Why the original reasoning was overturned

The sibling directory convention was chosen because "submodules add tooling friction (init, update, sync)." Three things changed:

1. **Cross-directory permission friction proved persistent.** Claude Code prompts on every read outside the project directory. The Permission Management Model (2026-03-04) attempted to solve this with settings.local.json entries. Testing across 5 projects (Issues #15, #16) showed that pattern matching was unreliable (absolute paths didn't match relative reads) and the settings files accumulated junk rather than systematic entries. The packages/ model eliminates the problem entirely — all reads are within-project.

2. **Ambient updates were a hidden danger.** `git pull` on a shared sibling directory changed behavior in every project simultaneously. One project's update could silently break another. Submodule version pinning means each project runs exactly the version it was tested with.

3. **Tooling friction is manageable.** `/update` abstracts submodule commands — users never run `git submodule` directly. `/create-app` sets up submodules during project creation. The friction that remained was less than the friction it replaced.

### Flat dependencies, not nested

Each NLA lists its direct dependencies as submodules. There is no transitive dependency resolution. If package A needs package B, the consuming NLA adds both as direct dependencies — they're siblings in `packages/`.

`git submodule update --init` (not `--recursive`) is the convention. `--recursive` would descend into dependencies' own `packages/` directories, creating wasteful nesting. Each project's `packages/` is relevant only when that project is the active working directory.

### Circular dependencies work

The framework depends on penny post (for `/check-feedback`, `/write-letter`). Penny post depends on the framework (thin wrappers delegate to framework core skills). In traditional software, this circular dependency creates build-order and version-resolution problems. In NLAs, it's harmless — there's no build step, no dependency resolver. Each project pins a specific version of the other. The LLM reads files from paths; the files exist at those paths. No compilation order, no resolution algorithm needed.

This is a consequence of the NLA model: when "code" is prose and the "runtime" is an LLM reading files, the constraints that make circular dependencies dangerous in traditional software don't apply.

### Update model: ambient to explicit

Previously, `git pull` on the framework updated all projects sharing that sibling. Now updates are per-project and explicit:

1. `/check-updates` compares the submodule's pinned commit against the remote HEAD
2. `/update` fetches, advances the submodule pointer (fast-forward only), stages it, then applies intent changes
3. The pointer advance + intent changes commit together atomically in the NLA's git history

Rollback is trivial — revert the commit that advanced the pointer. No collateral damage to other projects.

This aligns with the Cardinal Rule: the human decides when each project updates, and each update is independently reversible.

### Permission model retirement

With all dependencies inside `packages/`, cross-directory Read permissions are unnecessary. The Permission Management Model's Read-related machinery is retired:

- Removed: `Read(../nla-framework/**)` declarations in package manifests
- Removed: `/create-app` generating Read entries in settings.local.json
- Removed: `/install` and `/update` proposing Read permission entries
- Removed: `/validate` checking Read permission consistency
- Removed: `/startup` warning about missing settings.local.json

Retained: Bash patterns (`Bash(git:*)`, `Bash(ls:*)`, `Bash(test:*)`) for shell command approvals. These aren't about directory access — they're convenience patterns for routine CLI operations.

### Blast radius

- `install/` intent files: all path references, permission declarations
- `core/skills/`: all path references, permission-related sections in install, update, validate, startup
- `.claude/skills/create-app/`: generation flow (git init, submodule add), settings simplification
- `CLAUDE.md`: Key Files table
- All domain projects: migration via `/update` (required, no transition period)

---

## Shippability: Consumer-Facing vs. Internal Content

*Added 2026-04-17. Origin: Issue #22 from the penny-post maintainer, during
the packages/ migration roll-out.*

### The distinction

Every NLA's files divide into two buckets:

- **Consumer-facing** — content a downstream consumer's runtime reads. For the
  framework, that's `core/` (what thin wrappers delegate to) and
  consumer-facing `install/*.md` (what `/install` and `/update` read). For
  packages, it's the `app/` content consumers synthesize via `/install` plus
  `install/*.md`. For domain projects exported as plugins, it's `app/`,
  `.claude/skills/`, and `CLAUDE.md` (which becomes the foundation skill).
- **Internal** — content only maintainers read. Across project types: the
  project's own `reference/` (design rationale, friction log, session logs,
  install log) and, for framework and packages, their own `CLAUDE.md` (the
  runtime identity for self-maintenance, not read by consumers).

The rule for telling them apart: *who reads this file?* If it's something a
consumer's runtime reads during installation, update, or execution, it's
consumer-facing. If only maintainers ever open it, it's internal.

### Why the distinction matters

Without it, routine internal work surfaces to consumers as noise. A commit
that updates a framework session log, or fixes a typo in a package's design
rationale, causes every downstream NLA running `/update` to see "there are
new commits to review" — even though nothing has changed that would affect
those NLAs. As the ecosystem grows (more packages, more domain projects), the
signal-to-noise ratio in update prompts degrades. Consumers learn to skim or
ignore updates, which defeats the point of the update channel.

The analogous problem for domain projects is plugin re-exports. If tags
signal "there's a new version worth re-exporting," then tagging for every
reference-file change dilutes the signal.

### The rule

- **Commits touching consumer-facing content** → add an update-notes entry (if
  the project ships update notes). Tag fires at push, not at commit — see "The
  *when*: tag at push, not at commit" below.
- **Commits touching only internal content** → skip the note. Consumers see the
  submodule pointer advance but have nothing to review.

This scales naturally. Nothing new is required — tags are already the stable
choice, untagged HEAD is already the bleeding edge, and absence of an
update-notes entry already means nothing to surface. The convention is which
of those existing affordances to use when.

### The *when*: tag at push, not at commit

*Refined 2026-05-08. Origin: friction log entry 2026-04-18, "Shippability
convention reads as per-commit tagging; session-end is better."*

The original rule conflated two questions: *what counts as tag-worthy*
(consumer-facing content) and *when the tag actually goes on* (per commit).
The literal reading — tag every consumer-facing commit — produced
version-number inflation. A maintenance session with three consumer-facing
commits would jump v0.0.4 → v0.0.5 → v0.0.6 → v0.0.7 in a single arc of work,
none of the intermediate tags marking a meaningful release point.

The refined rule: tags attach at *push*, not at commit. Typically that means
session end — `/close` reviews the commits accumulated since the last tag and
tags HEAD before pushing if any of them touched consumer-facing content. One
session of consumer-facing work produces one tag.

Why push as the trigger? Tags are for consumers. An unpushed tag is noise —
it sits on a local commit that nobody downstream can see. If a session ends
without a push (work left local for review tomorrow), no tag fires; the next
push tags whatever has accumulated. This keeps the tag stream as
consumer-meaningful release markers rather than per-commit noise.

Update-notes entries continue to land per-commit. They're a running changelog
at commit granularity; the tag is the release marker that batches them.

### The edge case: cross-references in consumer-facing files

Sometimes an internal change necessitates edits to consumer-facing content —
for example, if `install/skills-intent.md` recommends penny-post as an
optional extension and the recommendation text needs updating. Those edits
count as consumer-facing because they change what consumers read, regardless
of why the change was needed. Shippability is about who reads the file, not
the nature of the motivating change.

### Two decisions: at commit, and at push

In practice this is two quick judgments:

**At commit time** — does this commit touch `core/`, consumer-facing
`install/*.md` (framework/package), or `app/` / `.claude/skills/` / `CLAUDE.md`
(domain project)? Yes → write an update-notes entry (if the project uses them).
No → skip the note.

**At push time** — review the commits since the last tag. If any touched
consumer-facing content, tag HEAD before pushing. If none did, push without
tagging. (See "The *when*: tag at push, not at commit" above.)

When a commit touches both consumer-facing and internal content, the presence
of consumer-facing content drives the commit-time decision: write the note.

### Blast radius

- `core/skills/maintain.md` — Shippability section (all domain projects).
- `core/skills/close.md` — operates the tag-at-push rule at session end.
- `install/package-intent.md` — package-specific pointer (packages).
- Design principle for all NLA maintenance going forward.

---

## Aspirational Engineering

*Added 2026-04-15. Origin: feedback triage discussion about human flourishing, lateral
thinking in /think, and the facebook-moderation compiler's observation about artistry.*

### The principle

Include aspirational goals in NLA documents — identity, values, skill postures — because
the aspiration itself produces better behavior even when the goal isn't fully achieved.
The aspiration creates a gradient: the AI moves toward the goal, and the movement is
valuable even if the destination isn't reached.

### Why it works

Every sentence in an NLA's identity documents gives the AI a behavioral nudge. These
nudges can be realistic ("flag uncertainty") or aspirational ("the person should finish
each session understanding more and making better judgments"). Both are operative. The
realistic nudge produces compliance. The aspirational nudge produces a gradient — the AI
aims higher and lands somewhere better than it would have without the aspiration.

The mechanism is the same as the intent-over-rules principle: the AI that understands
the *purpose* handles situations the instructions didn't anticipate. An aspirational
purpose extends this further — it shapes behavior across the entire space of possible
interactions, not just the ones the document addresses explicitly.

### Evidence from practice

Three independent observations:

1. **Artistry in compilation.** The facebook-moderation compiler was given three quality
   tiers: operable, understanding, artistry ("finding the form the spec was reaching
   toward"). Builds achieved the first two. Artistry didn't manifest, but the compiler
   identified specific missed opportunities and what it would need. The aspiration
   created a gradient that produced understanding as a side effect.

2. **Lateral thinking in /think.** The AI won't generate genuinely lateral ideas
   (like the packages/submodules leap that came from the human). But aspiring to lateral
   thinking — "question the frame," "bring unexpected connections" — produces better
   frame-questioning and more exploratory conversation as a side effect.

3. **Human flourishing in foundations.** The paragraph about flourishing gives the AI
   concrete behavioral nudges: explain reasoning rather than just producing output, make
   checkpoints informative rather than perfunctory, share diagnoses rather than just
   fixes, resist "I can handle this, you don't need to understand it." Each sentence
   is aspirational. Each nudges behavior in a measurable direction.

### Connection to AI identity

An NLA's identity IS its documentation. CLAUDE.md, values, foundations — they
collectively define who the AI is in this context. The identity-description pattern
(principle #4) says "describe who you are, not what you're not." Aspirational
engineering extends this: describe who you're *becoming*, not just who you are now.

The AI that reads "this framework is designed for human flourishing" behaves differently
from one that reads "this framework produces good output" — even if it can't fully
achieve flourishing. The difference is the gradient. And the gradient compounds: each
session where the AI aims for flourishing produces a slightly more engaged, more
explanatory, more human-developing interaction. Over many sessions, the gap between
aspirational and non-aspirational identity is substantial.

### What this is NOT

- **Not wishful thinking.** Each aspiration must be operationally specific enough to
  produce behavioral nudges. "Be good" is wishful. "The person should finish each
  session understanding more" is aspirational but operative — it tells the AI to
  explain its reasoning, share its thinking, make the human's engagement productive.
- **Not a substitute for concrete guidance.** Aspirational goals complement procedures
  and principles; they don't replace them. "Aim for artistry" without writing standards
  produces vague output. Writing standards plus "aim for artistry" produces craft.
- **Not always appropriate.** A pure formatting rule ("use ISO 8601 dates") doesn't
  benefit from aspiration. Aspirational engineering applies to identity, values, posture,
  and judgment-bearing instructions — the spaces where the AI's disposition matters.

### Blast radius

- `core/nla-foundations.md`: principle #1 (human flourishing), principle #4 (intent
  over rules / identity descriptions). All projects.
- `core/skills/think.md`: aspirational posture bullets. All projects.
- Design principle for all NLA document writing going forward.

---

## Structure Decisions Protocol

*Added 2026-05-07. Origin: friction log entry "Ad-hoc structural decisions
lack process and record" + /think conversation 2026-05-07.*

### The problem

NLAs lacked a process for modifying directory structures and placing
files. When AI determined "we need X," it tended to create `x/` ad hoc,
silently. Two failure modes stacked: no checkpoint with the human (the
structural decision slipped in unannounced), and no record for future
sessions (the next AI re-derived or guessed where things lived).

The framework itself was the case-in-point: `reference/feedback/`,
`reference/specs/`, `reference/designs/` had accumulated since 2026-02
without appearing in `install/structure-intent.md`. The framework
prescribed structure for new NLAs but had no protocol for evolving it.

### The three-layer pattern

The protocol borrows from facebook-moderation's compile-time
`build-guide.md` (in their `/compile` skill — every entry attributed to a
source or `[compiler]` judgment, **Judgment note** callouts for
non-obvious tradeoffs, Decision Sources table for scan affordance). Three
layers:

1. **Behavioral rule.** When AI is about to materially change project
   structure (new directory, reorganization, new top-level file), pause
   and propose. Recording is part of the change, not separate hygiene.
2. **Recording artifact.** Short attributed map of the as-built
   structure. Each entry: path → purpose → why this location → what put
   it there. Decision Sources table at the bottom.
3. **Consultation pattern.** Future AI sessions consult the artifact
   first when placing or finding things. The artifact must be in active
   context, which means the project's CLAUDE.md (or equivalent) must
   instruct reading it at session start.

### Threshold via intent, not rules

The threshold for "is this structural enough to fire the protocol?" is a
judgment call. The discipline describes the tension (over-gating annoys;
under-gating misses the cases that matter), names attribution as the
safety net, and lets the AI judge. This applies foundations principle #4
(intent over rules) to a question about its own design — a wrong judgment
is visible (the artifact records what the AI decided), and the human can
redirect.

### Centralized over distributed

A single short artifact loaded at startup. Distributed per-directory
READMEs would require lazy-load discovery the AI can't easily do without
an index, and they accumulate drift on different timelines from each
other. Centralized + always-loaded gives drift a chance to be
self-evident: an existing-but-undocumented directory or a
described-but-missing entry both surface as flags rather than going
silent.

### Where the artifact lives

Project-type dependent because framework and domain projects have
different runtime patterns:

- **Framework:** new file `core/structure.md`. The framework lacks
  `app/overview.md` by design (it isn't a domain project), and
  `core/structure.md` sits alongside the existing `core/README.md`. The
  framework's CLAUDE.md instructs reading it at session start.
- **Domain projects (deferred):** extension to `app/overview.md` (a
  "Where Things Live" section), since `app/overview.md` is already
  startup-loaded for domain projects via `/startup`.

The *content shape* is identical; the *file location* differs. Same
logic as the existing `core/` vs. `app/` split.

### Framework-first adoption with experimental validation

The framework adopts the protocol first, in this session. Domain-project
propagation is deferred — to be drafted as a publication plan after the
framework's experiments validate the pattern. This mirrors the prior
session's skill-invocation discipline pattern (Commit C deferred for
verification in real maintenance use).

The validation is empirical: cold-context experiments using the
methodology established in
`reference/experiments/skill-invocation-discipline/experiment-report.md`.
Specifically: `claude -p --dangerously-skip-permissions` headless
agents, binary filesystem signals, synthetic vocabulary to avoid
framework-prior contamination, hypotheses tested as discrete probes.
The full experiment report lives at
`reference/experiments/structure-decisions-protocol/experiment-report.md`.

### Blast radius

- **Consumer-facing:** `core/nla-foundations.md` (mention of the
  discipline as a working rhythm), `core/structure.md` (new file),
  eventually `core/skills/maintain.md`/`install.md`/`create-app/SKILL.md`
  if Step 7's wiring lands. Domain projects on next `/update` will see
  the foundations mention; the location-agnostic phrasing prevents them
  from creating `core/structure.md` themselves (that's the framework's
  own analog).
- **Framework-internal:** `CLAUDE.md` (new "Structural Change
  Discipline" section), `reference/experiments/structure-decisions-protocol/`
  (experiment report).
- **Deferred:** `install/CLAUDE-intent.md`, `install/structure-intent.md`,
  `install/update-notes.md` updates that propagate the pattern to
  domain projects.

### Why not just better written `install/structure-intent.md`?

That file *prescribes* structure for new NLAs but doesn't carry as-built
attribution. Two different jobs: the prescriptive intent (what new NLAs
should have) is forward-looking; the as-built record (what this specific
NLA actually has, and why) is backward-looking. They could coexist in
one file, but separating them keeps each one easier to maintain — the
intent file changes when the framework's prescription changes; the
structure record changes when the project's actual structure changes.
Different change frequencies, different audiences (framework
maintainers vs. domain-project maintainers).

---

## Principles as Design Tools

*Added 2026-05-07. Origin: Structure Decisions Protocol session debrief
(2026-05-07).*

### What was decided

Treat the framework's principles as operational design tools, not just
descriptive statements about the system. When designing new framework
discipline — rules, protocols, conventions, patterns — the principles
themselves should be load-bearing inputs to the design, explicitly
applied, not just generally aspirational.

### Where this surfaced

The Structure Decisions Protocol's threshold question — when should the
discipline fire? — was answered by applying foundations principle #4
(intent over rules). The protocol describes the tension between
over-gating and under-gating, names attribution as the safety net, and
lets AI judge. This is principle #4 designing the threshold for
*applying* principle #4 to structural change.

The self-referential pattern is what made the design clean. A
rules-shaped threshold ("fire on directories, not files inside
well-defined areas") would have been brittle and wrong at the margins.
The intent-shaped threshold turned out to work cleanly in experiments —
exactly as principle #4 predicts.

The same self-application shows up in other framework design choices
when looked at with this lens: principle #6 (the human decides) directly
designed the propose-review-record cadence; principle #5 (values are
visible) shapes the attribution discipline (decisions are *visible*
through citations and Decision Sources tables); principle #3 (NLA
documents are source code) explains why "fix the doc, not the code" is
the framework's standard maintenance move.

### Generalizable

When designing future framework discipline, ask: which principles are
load-bearing here? Apply them as design tools, not just background
philosophy:

- Principle #2 (NLA documents are source code) → design for prose-readability
  and edit-friendliness, not just executability.
- Principle #4 (intent over rules) → describe spaces, not boundaries; let
  judgment fill the gap that rules can't enumerate.
- Principle #5 (values are visible) → make tradeoffs and attributions
  explicit in prose.
- Principle #6 (the human decides) → propose-and-confirm workflows for
  consequential decisions.
- Principle #1 (imperfection is assumed) → design improvement loops, not
  perfection paths.

This makes the principles operational. They're not just "what we
believe"; they're "how we design new things."

### Caveats

Principles aren't always the right design tool. Pure consistency
conventions (date formats, file naming, commit message shape) benefit
from rules, not intent. Principle #4 itself notes this explicitly:
*"Rules have their place. Use rules for pure preferences where
consistency is the only goal."*

The design-tool judgment is "is this a judgment question or a
consistency question?" Judgment questions reach for intent-shaped
principles; consistency questions reach for rules. Conflating them
produces brittle rules where principles would generalize, or vague
principles where rules would suffice.

### Blast radius

Maintainers — this informs how new framework discipline gets designed.
Domain projects don't need to know about this directly; they receive
the products of well-designed discipline. The pattern is most useful at
the *design* moment, before convergence to a specific shape.

### Related

- Structure Decisions Protocol entry above (2026-05-07) — the case
  study where this pattern was first surfaced.
- `core/nla-foundations.md` "Key Principles" — the list of principles
  that serve as design tools.

---

## Adding Decisions

When you make architectural changes to the framework, add an entry here documenting:
- What was decided
- Why (including what alternatives were considered)
- Blast radius (core = all projects, install = project generation, reference = maintainers)

---

*This document is updated by the `/maintain` skill when architectural decisions are made.*
