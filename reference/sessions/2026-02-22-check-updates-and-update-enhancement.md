# Maintenance Session: /check-updates and /update Enhancement

**Date:** 2026-02-22
**Status:** Complete

## Intent
Give NLA users a way to see what updates are available across their NLA and all installed
packages, and make `/update` handle the full lifecycle — pulling remotes, applying intent
changes, and creating rollback branches for safety.

## Changes Made
- Enhanced `core/skills/update.md` with two-phase flow: Phase 0 (safety checks + rollback
  branch), Phase 1 (pull remotes, fast-forward only), Phase 2 (apply intent changes —
  the existing flow). Added scope disambiguation, edge cases, and the context-competence
  principle.
- Created `core/skills/check-updates.md` — read-only three-tier scan (remote→local,
  local→installed, NLA remote) with actionable recommendations
- Registered `/check-updates` in `install/skills-intent.md` and `CLAUDE.md` skills table
- Updated `/update` description in `install/skills-intent.md` to reflect broader scope
- Added optional update check to `core/skills/startup.md` (config-gated, off by default)
- Added "Update Checking" section to `config-spec.md`
- Clarified git URL source recording in `core/skills/install.md` install log format
- Added update note to `install/update-notes.md`
- Added design rationale entry for the update pipeline design
- Added "Context Determines Competence" principle to design rationale (during /think session)
- Post-validate fixes: created `.claude/skills/check-updates/SKILL.md` wrapper, updated
  `.claude/skills/update/SKILL.md` description, added check-updates to `core/skills/README.md`
  table and `README.md` directory tree

## Blast Radius
- `core/skills/update.md`, `check-updates.md`, `startup.md`: all domain projects
- `install/skills-intent.md`: project generation and `/install`/`/update`
- `config-spec.md`: framework configuration
- `CLAUDE.md`: framework only
- Startup behavior change is config-gated (off by default) — no project is affected
  unless the user explicitly enables it

## State at Close
All changes committed. /check-updates skill is live, /update is enhanced with
two-phase flow and rollback. Startup integration is config-gated. Validation
passed after fixing three structural findings (missing wrapper, stale description,
missing README entries). No pending work.
