# Export to Plugin

You are converting this NLA project into a self-contained plugin for Claude Code and
Cowork. The NLA project is the development environment; the plugin is the distribution
artifact. Think of it as compiling source code into a binary.

**The core constraint:** Plugins cannot reference files outside their directory. Every
dependency — framework files, shared context, task docs — must be resolved and bundled
inside the plugin. No `../` paths survive.

**Note on context:** This skill is designed for domain NLA projects. It reads the
project's `.claude/skills/` directory as the complete manifest of what becomes the
plugin. The framework's own skills are infrastructure — they provide content when thin
wrappers reference them, but they don't independently contribute to the plugin.

---

## Required Reading

Before starting, read these to understand the NLA you're exporting:

1. **`CLAUDE.md`** — identity, grounding principles, skills table, modes
2. **`app/overview.md`** — what the NLA does, how pieces connect
3. **`app/config-spec.md`** — configuration options (if it exists)
4. **`../nla-framework/core/nla-foundations.md`** — for extracting behavioral principles

---

## Input

`$ARGUMENTS` optionally provides a plugin name. If not provided, derive from the
project's directory name.

**Output location:** `../[plugin-name]-plugin/`

If the directory exists, warn the user and confirm before overwriting. The export is
idempotent — re-running replaces everything.

---

## Processing Flow

### 1. Inventory the Project

Scan `.claude/skills/` and read every SKILL.md. For each skill, classify it:

| Category | How to identify | Ships? | Frontmatter adjustment |
|----------|----------------|--------|----------------------|
| **Domain** | Self-contained skill that performs the NLA's primary tasks. References `app/` docs. | Yes | Remove `disable-model-invocation` |
| **Dev tool** | Thin wrapper → framework dev skill (maintain, friction-log, validate) | Yes | Keep `disable-model-invocation: true` |
| **Utility** | preferences, setup, onboard — user-facing but operational | Yes | Keep `disable-model-invocation: true` |
| **Extension** | Installed by a package (penny post, etc.) — not a thin wrapper to framework, not a domain skill | If present | Preserve existing frontmatter |
| **Absorbed** | startup — its purpose is replaced by the foundation skill | No | N/A |
| **Framework-only** | install, update, export — framework development tools | No | N/A |

Also scan:
- `app/shared/` — list all shared context files
- `app/` — list all task docs
- `lib/` — check for helper code
- Any project-specific directories referenced by skills

Present the inventory to the user:

```
Plugin: [name]
Output: ../[name]-plugin/

Skills to export:
  Domain: [list] (auto-invocable by users)
  Dev tools: [list] (hidden, invocable on request)
  Utility: [list] (hidden, invocable on request)
  Extension: [list] (preserving current behavior)

Not exporting:
  Absorbed into foundation: startup
  Framework-only: install, update, export
  [any others with reason]

Shared context: [list of files from app/shared/]
Task docs: [list]
Helper code: [yes/no]

Proceed?
```

Get confirmation before continuing. The user may adjust classifications.

### 2. Generate plugin.json

Create `.claude-plugin/plugin.json`:

```json
{
  "name": "[plugin-name]",
  "description": "[one-line from CLAUDE.md's opening identity]",
  "version": "1.0.0"
}
```

Keep the description under 100 characters. Derive it from CLAUDE.md's first sentence
about what the NLA does.

### 3. Generate the Foundation Skill

Create `skills/foundation/SKILL.md`. This is the hardest step — it replaces CLAUDE.md
as the plugin's identity.

```yaml
---
name: foundation
description: "[NLA name] — core identity and principles. Always active."
user-invocable: false
---
```

Synthesize the body from five sources into one coherent document:

**Source 1 — NLA Identity** (from CLAUDE.md): The opening role description, grounding
principles, and execution rules. Strip framework-specific content (thin wrapper
references, `../nla-framework/` paths, `/maintain` mode details).

**Source 2 — Behavioral Principles** (from `nla-foundations.md`): Extract ONLY the
Key Principles section (sections 1-6). Do NOT include the "What is an NLA?" explainer,
"NLA Shapes," "How to Read This System," or the "Hybrid Model" explanation. Those are
developer education, not runtime guidance.

**Source 3 — System Overview** (from `app/overview.md`): What the NLA does, how the
pieces connect, the task table. Strip developer-oriented sections (improvement pipeline,
getting-started, document hierarchy).

**Source 4 — Configuration** (from `app/config-spec.md`, if it exists): What's
configurable, defaults, constraints. Reframe for plugin context.

**Source 5 — Available Skills**: A table of skills shipping in the plugin, with
descriptions. Gives the AI awareness of its capabilities.

**Critical:** This must be a synthesis, not a concatenation. Write it as one coherent
identity document in the NLA's own voice. The AI loading this skill should understand
who it is, what it does, how it approaches its work, and what capabilities it has.
Target 150-300 lines.

Also add an `export-metadata.md` supporting file in the foundation directory:

```markdown
# Export Metadata

- **Source project:** [absolute path]
- **Framework version:** [git commit hash of ../nla-framework/]
- **Export date:** [YYYY-MM-DD]
- **Project version:** [git commit hash, if available]
- **Feedback channel:** [repo URL, if available]
```

### 4. Process Each Shipping Skill

For each skill that ships (domain, dev, utility, extension):

**a. Resolve references.** Read the SKILL.md and find all file references:
- `Read and follow ../nla-framework/core/skills/[name].md` (thin wrapper pattern)
- `Read and follow app/[name].md` (domain skill pattern)
- `app/shared/[name].md`, `shared/[name].md` (shared context)
- Any other path references in backticks

**b. Follow the prerequisite chain.** Read each referenced file. If it references
other files (e.g., a task doc that lists shared context as prerequisites), follow
those too. Resolve transitively until all dependencies are found.

**c. Bundle supporting files.** Copy each resolved file into the skill's directory
as a supporting file. Flatten the directory structure — `app/shared/voice-and-values.md`
becomes just `voice-and-values.md` in the skill directory.

**d. Rewrite paths.** In the SKILL.md and all copied files:
- Replace `../nla-framework/core/nla-foundations.md` references → remove (principles
  are in the foundation skill, which is always loaded)
- Replace `app/[name].md` → `[name].md` (now a local supporting file)
- Replace `app/shared/[name].md` or `shared/[name].md` → `[name].md`
- Replace `lib/` paths → `${CLAUDE_PLUGIN_ROOT}/lib/` if lib ships
- Remove any remaining `../` references

**e. Adjust frontmatter** per the classification table in step 1.

**Example transformation:**

Before (thin wrapper in NLA):
```yaml
---
name: maintain
description: Edit the NLA system
disable-model-invocation: true
---
Read and follow `../nla-framework/core/skills/maintain.md`.
```

After (self-contained in plugin):
```yaml
---
name: maintain
description: Edit the NLA system
disable-model-invocation: true
---
[Full content of core/skills/maintain.md, with all paths rewritten
to reference local supporting files]
```

Before (domain skill in NLA):
```yaml
---
name: compose
description: Start a new composition
disable-model-invocation: true
---
# Compose
...
Read and follow `app/compose.md`.
```

After (domain skill in plugin):
```yaml
---
name: compose
description: Start a new composition
---
# Compose
...
Read and follow `compose.md` (in this skill's directory).
```

With supporting files:
```
skills/compose/
├── SKILL.md
├── compose.md              (from app/compose.md)
├── voice-and-values.md     (from app/shared/)
├── common-patterns.md      (from app/shared/)
└── [other prerequisites]
```

### 5. Copy Supporting Assets

- **`lib/`** — copy contents to `lib/` at plugin root if non-empty
- **Project-specific directories** — if skills reference files outside `app/` and
  `lib/` (e.g., `voices/`, `platforms/`, `templates/`), bundle the referenced files
  as supporting files in the skill that references them
- For config-dependent references (e.g., `voices/{active-voice}/`), resolve using
  the currently configured value. Note this in export metadata: "Exported with
  voice: [name]"

### 6. Generate README.md

Write a user-facing README at the plugin root. Synthesize from the NLA's identity
and overview:

- What this plugin does (one paragraph)
- Available skills (table with name and description — domain skills first, then
  utility, then dev tools labeled as such)
- Setup requirements (e.g., "Requires SuperCollider installed")
- Configuration ("Use `/[plugin-name]:preferences` to customize behavior")
- Where to send feedback (if feedback channel is in export metadata)

Write for someone discovering the plugin, not for a developer maintaining the NLA.

### 7. Final Verification

Before reporting success, check:

1. **No escaped paths.** Search all generated files for `../` — should find zero.
2. **No broken references.** Every file referenced in a SKILL.md exists in that
   skill's directory.
3. **Valid manifest.** `plugin.json` is valid JSON with at least a `name` field.
4. **Foundation size.** Foundation SKILL.md is under 500 lines (plugin best practice).
5. **Completeness.** Every skill from the approved inventory is present.

Report results to the user. If issues are found, fix them before confirming.

---

## Edge Cases

- **Ejected skills** — If a thin wrapper was replaced with a full custom skill,
  treat it as self-contained. Read it, resolve its references, bundle everything.
- **Annotated wrappers** — If a wrapper delegates to the framework but adds
  project-specific notes, resolve the framework reference AND keep the annotations.
  The result should be a self-contained skill with the annotations preserved.
- **Non-standard directories** — Projects may have custom directories (voices/,
  platforms/, templates/). Read skill references to discover what's needed. Bundle
  referenced files per skill.
- **Cross-skill duplication** — Multiple skills referencing the same shared file
  each get their own copy. Duplication is acceptable for small markdown files.
- **Missing references** — If a referenced file doesn't exist, warn the user and
  note it in the output. Don't silently skip.
- **Large skills** — If a resolved skill exceeds 500 lines, note it as a warning
  but proceed. The limit is guidance, not a hard constraint.
- **No overview.md** — Generate the foundation skill from CLAUDE.md and config-spec
  alone. Note the gap.

---

## Principles

- **Propose before generating.** The inventory step gets approval before any files
  are created. The user controls what ships.
- **Self-containment over everything.** Every skill must work without any external
  references. When in doubt, bundle more, not less.
- **Synthesize, don't concatenate.** The foundation skill is a coherent document,
  not four pasted sections. Match the NLA's voice.
- **Preserve intent.** Domain skills should behave the same in the plugin as in
  the NLA project. The conversion changes structure, not behavior.
- **Transparency.** Export metadata records exactly what was exported, from where,
  and when. The plugin should be traceable to its source.

---

*This skill converts an NLA project into a plugin. The NLA project remains the
development environment. To improve the plugin, improve the NLA and re-export.*
