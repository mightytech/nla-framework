# Export to Plugin

You are converting this NLA project into a plugin for Claude Code and Cowork. The
plugin mirrors your NLA's structure — a **view-source artifact**, not a compiled
binary. To improve the plugin, improve the NLA and re-export.

**Note on context:** This skill is designed for domain NLA projects. It reads the
project's `.claude/skills/` directory as the complete manifest of what becomes the
plugin. The framework's own skills are shipped through the bundled `packages/`
submodule, not as independent contributors.

## How this skill works

Your role is judgment. You classify the skills, synthesize the foundation identity
and the README, and choose plugin metadata. A Python script at
`packages/nla-framework/lib/export.py` handles the mechanical work: `git archive`,
submodule resolution, path rewrites, frontmatter adjustments, and post-export
verification.

The flow: you write a manifest JSON and three synthesized content files; the script
reads them and produces the plugin directory. You then parse the script's JSON
status report and present results.

---

## Required Reading

Before starting, read these to understand the NLA you're exporting:

1. **`CLAUDE.md`** — identity, grounding principles, skills table
2. **`app/overview.md`** — what the NLA does, how pieces connect (if present)
3. **`app/config-spec.md`** — configuration options (if it exists)
4. **`packages/nla-framework/core/nla-foundations.md`** — for extracting the Key
   Principles section into the foundation skill

---

## Input

`$ARGUMENTS` optionally provides a plugin name. If not provided, derive from the
project's directory name.

**Output location:** `../[plugin-name]-plugin/` by default, or a user-specified path.
If the directory exists, warn the user and confirm before overwriting.

---

## Processing Flow

### Phase 1 — Gather

**1a. Check Python 3 availability.** The script requires it. This is a point-of-use
requirement — Python 3 is not a framework-wide prereq.

```
python3 --version
```

If Python 3 is missing, stop and help the user install it:

- **macOS:** `brew install python3` or download from python.org
- **Ubuntu/Debian:** `sudo apt install python3`
- **Other Linux:** use the distribution's package manager
- **Windows:** download from python.org

Once installed, re-run `/export`.

**1b. Check the working tree.** The plugin ships committed state (`HEAD`), not
working state.

```
git status --porcelain
```

If there are uncommitted changes, tell the user: *"The plugin will ship your last
commit, not your working state. Changes to `[files]` won't be included. Commit them,
or proceed anyway?"* Proceed only with explicit confirmation.

**1c. Inventory the project:**

- Subdirectories under `.claude/skills/`
- Files in `app/` (overview, shared/, task docs)
- `lib/` contents, if any
- Top-level directories beyond the usual (`voices/`, `platforms/`, `templates/`,
  etc.) — these are preserved automatically
- Submodules listed in `.gitmodules`

### Phase 2 — Classify

Every skill in `.claude/skills/` goes into one of three buckets:

| Bucket | Description | Script behavior |
|--------|-------------|-----------------|
| `exclude` | Skills that are meaningless in a plugin | Directory removed |
| `domain` | Skills a plugin user invokes to do primary NLA tasks | `disable-model-invocation: true` stripped so plugin users can auto-invoke |
| `keep_as_is` | Dev tools (maintain, friction-log, validate), utility skills (preferences, setup), extension skills (penny post) | Frontmatter untouched |

**Default classifications:**

- `exclude`: `install`, `update`, `export`, `create-app`, `startup`
  (startup is absorbed into the foundation skill — its purpose is loading context,
  which happens automatically via `user-invocable: false`)
- `domain`: any skill whose SKILL.md delegates to `app/[task].md` (the primary-task
  pattern) — these are the skills end users invoke
- `keep_as_is`: everything else — dev tools, utilities, extensions

For non-obvious classifications, explain your reasoning so the user can evaluate the
judgment.

**Derive plugin metadata:**

- `plugin_name` — from user input or project directory name
- `plugin_description` — one line from CLAUDE.md's opening identity, under 100 chars
- `plugin_version` — default `1.0.0` (or ask)
- `framework_commit` — `git -C packages/nla-framework rev-parse --short HEAD`
- `project_commit` — `git rev-parse --short HEAD`
- `export_date` — today's date (YYYY-MM-DD)
- `feedback_channel` — the NLA's upstream repo URL, if known

**Present the plan to the user:**

```
Plugin: [name]
Version: [version]
Output: [absolute path]

Submodules to include:
  [framework + any extension packages]

Skills:
  Exclude: [list]
  Domain (auto-invocable in plugin): [list]
  Keep as-is (dev/utility/extension): [list]

Warnings:
  [working tree status, non-standard dirs, submodule drift, etc.]

Proceed?
```

Get explicit approval before continuing.

### Phase 3 — Synthesize

Create a staging directory (e.g., `/tmp/nla-export-[plugin-name]-staging/`) and
write three files there.

**3a. Foundation SKILL.md** — the plugin's identity, auto-loaded at runtime because
CLAUDE.md isn't auto-loaded in plugins.

```yaml
---
name: foundation
description: "[NLA name] — core identity and principles. Always active."
user-invocable: false
---
```

Synthesize the body from five sources into one coherent document:

- **NLA Identity** (from CLAUDE.md): opening role description, grounding principles,
  execution rules. Strip framework-specific content (thin wrapper references,
  maintenance mode, framework paths, `/install`/`/update` instructions).
- **Behavioral Principles** (from `nla-foundations.md`): the Key Principles section
  only. Do NOT include the "What is an NLA?" explainer, "NLA Shapes," "How to Read
  This System," or the "Hybrid Model" sections — those are developer education, not
  runtime guidance.
- **System Overview** (from `app/overview.md`): what the NLA does, how pieces
  connect, the task list. Strip developer-oriented sections (improvement pipeline,
  getting-started, document hierarchy).
- **Configuration** (from `app/config-spec.md`, if present): what's configurable,
  defaults, constraints. Reframe for plugin context.
- **Available Skills**: a table of skills shipping in the plugin (domain +
  `keep_as_is`), with descriptions.

**Critical:** This is a synthesis, not a concatenation. Write it as one coherent
identity document in the NLA's voice. Target 150–300 lines.

**3b. export-metadata.md** — traceability:

```markdown
# Export Metadata

- **Source project:** [absolute path]
- **Framework version:** [git short hash]
- **Project version:** [git short hash]
- **Export date:** [YYYY-MM-DD]
- **Feedback channel:** [repo URL, if known]
```

**3c. README.md** — user-facing introduction to the plugin:

- What this plugin does (one paragraph)
- Available skills (table with name and description — domain first, then
  dev/utility labeled as such)
- Setup requirements (e.g., "Requires SuperCollider installed")
- Configuration (`"Use /[plugin-name]:preferences to customize"`)
- Feedback channel (from metadata)

Write for someone discovering the plugin, not for a developer maintaining the NLA.

### Phase 4 — Execute

**4a. Write the manifest** to the staging directory:

```json
{
  "plugin_name": "[name]",
  "plugin_description": "[description]",
  "plugin_version": "[version]",
  "source_project_path": "[absolute path to this project]",
  "output_dir": "[absolute path to plugin output]",
  "framework_submodule_path": "packages/nla-framework",
  "additional_submodule_paths": ["[other submodules, if any]"],
  "skills": {
    "exclude": [...],
    "domain": [...],
    "keep_as_is": [...]
  },
  "synthesized": {
    "foundation_skill_md": "[staging path]/foundation-SKILL.md",
    "foundation_export_metadata": "[staging path]/export-metadata.md",
    "readme": "[staging path]/README.md"
  },
  "export_metadata": {
    "framework_commit": "[hash]",
    "project_commit": "[hash]",
    "export_date": "[date]",
    "feedback_channel": "[url]"
  }
}
```

**4b. Invoke the script:**

```
python3 packages/nla-framework/lib/export.py --manifest [staging]/manifest.json
```

Optional flags: `--verbose` (log every path rewrite), `--dry-run` (do everything
except the final move), `--force` (allow dirty tree or overwrite existing output).

**4c. Parse the JSON status on stdout.** The script emits:

```json
{
  "status": "ok",
  "plugin_name": "[name]",
  "output": "[absolute path]",
  "excluded_skills": [...],
  "domain_skills_touched": [...],
  "path_substitutions": <number>,
  "warnings": [...]
}
```

On non-zero exit, read stderr and relay the error. Common failures:

- **Exit 2** — dirty working tree (commit first, or re-invoke with `--force`)
- **Exit 3** — output directory exists (confirm with user, re-invoke with `--force`)
- **Exit 5** — submodule not initialized (run `git submodule update --init`, re-try)
- **Exit 6** — synthesized file missing (check the staging paths in the manifest)
- **Exit 7** — verification found a leaked path (a bug — surface the affected file)

For the full list of transforms the script performs, see the docstring at the top
of `packages/nla-framework/lib/export.py`.

### Phase 5 — Verify and Clean Up

Report structural success:

- Skills shipped (count, names)
- Path substitutions made (from the status report)
- Any warnings
- Output path

**Optional runtime validation.** Offer to verify the plugin loads:

```
env -u CLAUDECODE claude -p "List all available skills." \
  --plugin-dir [output-path] --max-turns 2
```

The `env -u CLAUDECODE` prevents conflicts when launching Claude from inside an
existing session. `--max-turns 2` prevents runaway turns.

**Clean up** the staging directory once the user confirms the output looks right.

---

## Edge Cases

The view-source export model handles most edge cases automatically — the script
preserves structure rather than transforming it:

- **Ejected skills** ship as-is. Internal references get path-rewritten by the
  script like any other file.
- **Annotated wrappers** ship intact. Annotations persist alongside the delegated
  framework file.
- **Non-standard directories** (`voices/`, `platforms/`, `templates/`) are
  preserved by `git archive`. The script auto-detects top-level dirs and rewrites
  references to them.
- **Missing `app/config-spec.md`** — skip the Configuration section of foundation
  synthesis.
- **No `app/overview.md`** — synthesize foundation from CLAUDE.md and the skills
  table alone. Note the gap in export-metadata.
- **Extension skills** (penny post, process helpers) — classify as `keep_as_is`.
  Their submodule must be listed in `additional_submodule_paths`.
- **Submodule HEAD differs from the superproject pointer** — script warns. User
  decides whether to `git submodule update` and re-export.
- **`reference/` directory** — exclude from the plugin via `.gitattributes
  export-ignore` in the NLA. `git archive` honors it for free.

---

## Principles

- **Propose before generating.** Classification and manifest get approval before the
  script runs. The user controls what ships.
- **Structure-preserving.** The plugin mirrors the NLA. Same layout, same file
  names; paths get a `${CLAUDE_PLUGIN_ROOT}/` prefix so they resolve from any
  installed location.
- **Synthesize, don't concatenate.** The foundation skill is a coherent document in
  the NLA's voice — not four pasted sections.
- **Commits only.** The plugin ships `HEAD`. If there are uncommitted changes, the
  user commits or explicitly confirms proceed-with-warning.
- **Judgment and mechanics are separate.** The AI classifies and synthesizes; the
  script transforms and verifies. Each does what it does best.

---

## After Export

Suggest verifying the plugin loads (runtime validation above) if you haven't already.
If the session is wrapping up, `/debrief` can surface observations about the export
process, and `/close` finalizes the session record.

---

*This skill orchestrates plugin export. The script does the mechanical work; the AI
does the judgment work. To improve the plugin, improve the NLA and re-export.*
