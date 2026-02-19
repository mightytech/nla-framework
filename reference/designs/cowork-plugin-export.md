# Design: Export NLA to Cowork Plugin

**Status:** Draft
**Date:** 2026-02-14
**Context:** Claude Cowork plugins are structurally almost identical to NLA framework projects — markdown skills, slash commands, file-based configuration. A converter from NLA → Cowork plugin would give NLAs a distribution channel with a built-in audience (all paid Claude subscribers).

---

## What Cowork Plugins Are

Cowork is Claude Code running in a sandboxed VM on the user's desktop, with folder access and a plugin system. Simon Willison described it as "regular Claude Code wrapped in a less intimidating default interface."

Plugins are entirely file-based — markdown and JSON, no code required:

```
plugin-name/
├── .claude-plugin/
│   └── plugin.json              # Manifest (metadata)
├── skills/                      # Agent skills (SKILL.md per skill)
│   └── skill-name/
│       ├── SKILL.md             # Required: frontmatter + instructions
│       └── [supporting files]   # Optional: templates, reference docs
├── commands/                    # Legacy simple slash commands (.md files)
├── agents/                      # Subagent definitions
├── hooks/
│   └── hooks.json               # Event handlers (pre/post tool use, session start, etc.)
├── .mcp.json                    # MCP server connections (external tools)
└── .lsp.json                    # Language server configs
```

### Key References

- Plugin creation docs: https://code.claude.com/docs/en/plugins
- Plugin reference/spec: https://code.claude.com/docs/en/plugins-reference
- Skill authoring: https://code.claude.com/docs/en/skills
- Example plugins: https://github.com/anthropics/knowledge-work-plugins
- Cowork announcement: https://claude.com/blog/cowork-research-preview
- Cowork plugins announcement: https://claude.com/blog/cowork-plugins

---

## Why This Matters

The NLA framework is a development methodology. Cowork plugins are a distribution format. The converter bridges them: develop with the framework's structure, learning loops, and maintenance tools — ship as a plugin anyone can install.

Without the converter, NLAs require: clone repo, understand framework, set up environment. With it: install plugin. The barrier drops from "understand a paradigm" to "try a tool."

---

## The Structural Mapping

### What Maps Directly

| NLA Framework | Cowork Plugin | Notes |
|--------------|---------------|-------|
| `.claude/skills/*/SKILL.md` | `skills/*/SKILL.md` | Same format, same YAML frontmatter |
| Skill names + descriptions | Skill names + descriptions | Identical |
| `lib/` | `lib/` or `scripts/` | Helper code, unchanged |
| Slash command invocation | Namespaced slash commands | `/compose` → `/plugin-name:compose` |
| `reference/` | Supporting files or omitted | Dev-time docs, not runtime |

### What Needs Transformation

#### 1. Flatten the Two-Hop Pattern

NLA skills are often thin wrappers that delegate to the framework:

```markdown
---
name: startup
description: Initialize the NLA runtime
---
Read and follow `../nla-framework/core/skills/startup.md`.
```

Plugins cannot reference files outside their directory (`../` paths don't work). The converter must **inline** the referenced framework file, producing a self-contained SKILL.md.

For domain skills that reference `app/` docs:

```markdown
Read and follow the instructions in **`app/compose.md`**.
```

The converter either inlines the doc content or copies it as a supporting file in the skill directory.

**Resolution algorithm:**
1. Read the SKILL.md
2. Find all file references (patterns: `Read and follow`, `Read`, path references)
3. For each reference, read the target file
4. If the target file itself has references (prerequisite chain), resolve those too
5. Produce a self-contained skill with all dependencies bundled

#### 2. CLAUDE.md → plugin.json + Foundation Skill

CLAUDE.md serves two roles in an NLA:
- **Metadata:** name, description, available skills, file layout
- **Runtime identity:** grounding principles, execution rules, constraints

Split into:
- `plugin.json` — metadata portion

```json
{
  "name": "duet",
  "version": "1.0.0",
  "description": "Collaborative music composition with SuperCollider",
  "author": { "name": "..." },
  "license": "MIT"
}
```

- `skills/foundation/SKILL.md` — runtime identity, with `user-invocable: false` so Claude loads it as background knowledge automatically

```yaml
---
name: foundation
description: Core principles and identity for this NLA. Always active.
user-invocable: false
---
[Grounding principles, execution rules, constraints from CLAUDE.md]
[Relevant portions of nla-foundations.md]
```

#### 3. Shared Context Distribution

`app/shared/` files (voice-and-values, common-patterns, output-spec) are read by all domain tasks. In a plugin, two approaches:

**Option A — Bundle per skill (recommended for v1):**
Each domain skill gets copies of the shared docs it needs as supporting files in its directory. Self-contained, no cross-skill dependencies. Duplicates content but guarantees each skill has everything it needs.

```
skills/compose/
├── SKILL.md
├── voice-and-values.md      # copied from app/shared/
├── common-patterns.md       # copied from app/shared/
└── output-spec-sc.md        # copied from app/shared/
```

**Option B — Shared context skill:**
A single `skills/shared-context/` skill with `user-invocable: false` that Claude auto-loads. Other skills reference it. Cleaner but relies on Claude reliably loading the shared skill before domain skills.

**Decision:** Start with Option A. Optimize to Option B if plugin size becomes a problem.

#### 4. Configuration System

NLA has `config.md` (user preferences) + `config-spec.md` (what's configurable). Cowork has **folder instructions** — persistent context per folder that the user can edit and Claude reads automatically.

The converter maps:
- `config-spec.md` → part of the `/preferences` skill (or foundation skill)
- `config.md` → written to folder instructions by `/preferences` skill
- Config reads at startup → Claude reads folder instructions automatically (no explicit step needed)

This is a behavioral change, not just structural. The `/preferences` skill needs to write folder instructions instead of a config file.

#### 5. nla-foundations.md

The philosophical foundation document. Options:
- **Inline into foundation skill** — full copy, always available
- **Extract behavioral principles only** — skip the "what are NLAs" explainer, keep only what affects runtime behavior
- **Weave into each skill** — each skill gets only the principles relevant to it

**Recommendation:** Extract behavioral principles into the foundation skill. The explanatory content is for developers, not for the runtime.

---

## What Gets Lost

### Framework Update Propagation
The two-hop pattern means `git pull` on the framework improves all NLAs. A flattened plugin is a **snapshot** — frozen at export time. To get framework improvements, re-export.

This is the fundamental tradeoff: development-time flexibility vs. distribution-time self-containment. It's the same tradeoff as compiling source code to a binary.

**Mitigation:** The converter is cheap to run. Re-export after framework updates. Version the plugin to track which framework version it was built from.

### Development-Time Tools
Friction log, maintain cycle, validate, session logs — these are the NLA development process. They don't ship in the plugin. The plugin is the *output* of that process.

A user installing the Duet plugin doesn't need `/maintain`. But the Duet developer does. The NLA project remains the development environment; the plugin is the release artifact.

### Reference Documentation
Design rationale, session archives — developer context, not user context. Could ship as plugin documentation (README) but aren't functional.

---

## What the Converter Does

### Input
An NLA framework project directory containing:
- `CLAUDE.md`
- `app/` (task docs, shared context, templates, config-spec)
- `.claude/skills/` (skill wrappers and domain skills)
- `lib/` (optional helper code)
- Framework path (default `../nla-framework/`)

### Output
A Cowork plugin directory containing:
- `.claude-plugin/plugin.json`
- `skills/` (self-contained, all dependencies resolved)
- `lib/` (copied)
- `.mcp.json` (if the NLA uses external tools)
- `README.md` (generated from overview + description)

### Algorithm

```
1. Read CLAUDE.md → extract metadata, runtime identity
2. Read app/overview.md → extract description
3. Read app/config-spec.md → extract configuration options

4. Generate plugin.json from metadata

5. Generate skills/foundation/SKILL.md from:
   - Runtime identity (from CLAUDE.md)
   - Behavioral principles (from nla-foundations.md)
   - Configuration spec (from config-spec.md)

6. For each skill in .claude/skills/:
   a. Read SKILL.md
   b. Classify: framework wrapper or domain skill
   c. If wrapper: resolve the framework file reference, inline content
   d. If domain skill: resolve app/ doc references
   e. For each resolved doc: follow its prerequisite chain
      (e.g., compose.md says "read voice-and-values.md first")
   f. Bundle all prerequisites as supporting files in the skill directory
   g. Rewrite SKILL.md to reference local supporting files instead of app/ paths
   h. Preserve frontmatter, adjust as needed

7. Filter out development-only skills:
   - /maintain → omit (development tool)
   - /friction-log → omit (development tool)
   - /validate → omit (development tool)
   - /preferences → keep (user-facing)

8. Copy lib/ → lib/

9. If the NLA has environment/tool dependencies:
   - Generate .mcp.json stub with notes on what servers are needed
   - Or generate hooks for tool checking

10. Generate README.md from app/overview.md + CLAUDE.md description

11. Write version metadata:
    - Framework version used
    - Export date
    - Source project path
```

### Where It Lives

A framework skill: `/export-plugin`. It works for any NLA built on the framework.

```
.claude/skills/export-plugin/SKILL.md
```

The logic is generic: read the project, flatten the hops, bundle the output. App-specific knowledge isn't needed — the converter reads the project structure and follows the conventions.

---

## Open Design Questions

### How much framework to inline?

- **Minimal:** Just skill logic, skip philosophy. Smaller but loses grounding.
- **Maximal:** Inline everything. Self-contained but each skill carries 200+ lines of context.
- **Smart:** Analyze which principles each skill depends on, include only those.

**Starting position:** Maximal for v1. Optimize when we see what's too large.

### How to handle the prerequisite chain?

Skills reference docs that reference other docs. The converter needs to follow this chain. Two approaches:

- **Eager:** Resolve everything, bundle everything. Simple, reliable, potentially large.
- **Lazy:** Only resolve first-level references. Risk: missing context at runtime.

**Starting position:** Eager. Let each skill be fully self-contained.

### What about plugins that need external tools?

Duet needs SuperCollider. A plugin can declare MCP servers in `.mcp.json`, but SC doesn't have an MCP server. Options:

- Ship a `/setup` skill that checks for dependencies (like Duet already has)
- Use hooks to check on session start
- Document requirements in README and accept the limitation

**Starting position:** Ship `/setup` as a plugin skill + document in README.

### Should the converter be idempotent?

Can you re-run it safely on the same output directory? Probably yes — overwrite everything, since the plugin is always a derived artifact from the NLA source.

### Plugin versioning strategy?

The plugin version should track the NLA project, not the framework. Suggested: use the NLA project's git tag or commit hash as the plugin version, with the framework version recorded in metadata.

---

## Duet as First Test Case

Duet → Cowork plugin would produce:

```
duet-plugin/
├── .claude-plugin/
│   └── plugin.json
├── skills/
│   ├── foundation/
│   │   └── SKILL.md              # Identity + principles + config spec
│   ├── compose/
│   │   ├── SKILL.md              # Composition workflow
│   │   ├── voice-and-values.md
│   │   ├── common-patterns.md
│   │   ├── output-spec-sc.md
│   │   └── context-template.md
│   ├── iterate/
│   │   ├── SKILL.md
│   │   ├── voice-and-values.md
│   │   ├── common-patterns.md
│   │   └── output-spec-sc.md
│   ├── critique/
│   │   ├── SKILL.md
│   │   ├── voice-and-values.md
│   │   └── output-spec-sc.md
│   ├── spark/
│   │   ├── SKILL.md
│   │   └── voice-and-values.md
│   ├── preferences/
│   │   └── SKILL.md
│   ├── setup/
│   │   └── SKILL.md
│   ├── snapshot/
│   │   └── SKILL.md
│   ├── shelve/
│   │   └── SKILL.md
│   ├── finish/
│   │   └── SKILL.md
│   └── resume/
│       └── SKILL.md
├── lib/
└── README.md
```

**Skills included:** compose, iterate, critique, spark, preferences, setup, snapshot, shelve, finish, resume
**Skills excluded:** startup (absorbed into foundation), maintain, friction-log, validate, plan (dev-only)

---

## Implementation Sequence

1. **Manual conversion of Duet** — do it by hand first to validate the mapping and discover edge cases
2. **Write the converter** as a framework skill (`/export-plugin`)
3. **Test the exported plugin** in Cowork — does it actually work?
4. **Iterate** — what broke? what's missing? what's unnecessary?
5. **Generalize** — ensure the converter works for any NLA, not just Duet

Step 1 before step 2. The manual conversion will surface problems the design doc didn't anticipate.

---

*This design emerged from analyzing the Cowork plugin architecture during a Duet maintenance session (2026-02-14). The structural similarity between NLA framework projects and Cowork plugins was unexpected — the mapping is close to 1:1, with the main complexity being dependency resolution (flattening the two-hop pattern).*
