---
name: export
description: Export an NLA project as a plugin for Claude Code or Cowork. Converts the project into a self-contained plugin directory with all dependencies resolved.
disable-model-invocation: true
---
**Note:** This skill is designed for domain NLA projects. Run `/export` from a domain
project directory, not the framework. The export reads `app/`, `CLAUDE.md`, and
`.claude/skills/` — paths that exist in domain projects, not here.

Read and follow `core/skills/export.md`.
