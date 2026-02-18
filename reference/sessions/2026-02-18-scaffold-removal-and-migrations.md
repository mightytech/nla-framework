# Maintenance Session: Scaffold Removal, Convention Updates, and Copydesk Migration

**Date:** 2026-02-18
**Status:** Complete

## Intent

Remove the scaffold directory, establish intent files as the single source of truth for project generation, update existing domain projects to current conventions, and migrate the original NLA (amg-ghost-tools) to a framework-based project.

## Changes Made

### Phase 1: Enriched Intent Files

Made intent files comprehensive enough that `/create-app` can generate every framework-provided file without reading scaffold.

- `install/CLAUDE-intent.md` — Added reference structure section listing 10 ordered sections a well-formed CLAUDE.md should have.
- `install/structure-intent.md` — Added reference file structures for all framework-provided files (design-rationale, friction-log, feedback-log, system-status, installed-packages, archives, README, config files) plus mechanical file templates (.gitignore, .gitkeep).
- `install/skills-intent.md` — Complete rewrite. Each of 8 skills now has full reference wrapper content. Added domain skill pattern section.
- `install/README.md` — New file documenting the intent pattern for humans.
- `install/install.md` — Updated `/create-app` relationship language.

### Phase 2: Refactored `/create-app`

Major rewrite of `.claude/skills/create-app/SKILL.md`. Replaced all scaffold references with intent file references. Three generation categories: mechanical (from intent files), structured (intent + conversation), and domain-specific (conversation only). Added inline structural guidance for domain files.

### Phase 3: Created `/install-app`

- `install/example-catalog.md` — Catalog of example NLA projects (email-rewriter, penny-post, duet).
- `.claude/skills/install-app/SKILL.md` — New skill that reads catalog, presents options, clones to sibling directory.

### Phase 4: Deleted Scaffold

- Removed `scaffold/` directory (28 files)
- Removed `.claude/skills/create-sample-app/`

### Phase 5: Cleaned Up References

Updated all skills (validate, maintain, plan, friction-log) to remove scaffold references and add intent file checks. Updated CLAUDE.md, README.md, design-rationale.md, CONTRIBUTING.md, config-spec.md, friction-log.md. Created `core/README.md` and `core/skills/README.md`.

### Convention Updates Across Domain Projects

Brought three existing NLAs to current framework conventions:

**Email Rewriter** (most gaps):
- Added skill wrappers: /validate, /preferences, /install, /update
- Added `disable-model-invocation: true` to /startup
- Created reference files: feedback-log, feedback-log-archive, installed-packages
- Created config infrastructure: config-spec.md, config.md, .gitignore
- Updated CLAUDE.md with Configuration section and expanded skills table

**Penny Post** (few gaps):
- Added skill wrappers: /install, /update
- Added `disable-model-invocation: true` to /startup
- Created reference files: feedback-log-archive, installed-packages
- Updated CLAUDE.md Framework Skills table

**Duet** (few gaps):
- Added skill wrappers: /install, /update
- Added `disable-model-invocation: true` to /startup (ejected startup, preserved custom content)
- Created reference files: feedback-log, feedback-log-archive, installed-packages
- Updated CLAUDE.md skills table

All three received enriched installed-packages.md entries and penny post letters documenting what changed.

### Copydesk Migration

Created `../copydesk/` as a framework-based successor to `../amg-ghost-tools/` (the original NLA that inspired the framework).

- Step 1: Generated framework skeleton via `/create-app` flow (CLAUDE.md, 11 skill wrappers, config infrastructure, reference files, README)
- Step 2: Migrated domain content from amg-ghost-tools (voice-and-values, common-patterns, output-spec, task docs, design rationale, friction logs, session logs, lib code, JS utility scripts)
- Task names updated: post-formatter → format, post-seeder → import, learning-feedback → learn
- Left migration prompts for steps 3 (reconciliation in copydesk) and 4 (review from amg-ghost-tools)

## Blast Radius

| Change | Affects |
|--------|---------|
| Intent file enrichment | Project generation (via `/create-app`) |
| `/create-app` rewrite | Project generation |
| `/install-app` creation | New user onboarding |
| Scaffold deletion | Nothing (scaffold was only used by `/create-app` and `/create-sample-app`) |
| Skill/reference updates | Framework documentation and validation |
| Domain project updates | email-rewriter, nla-penny-post, duet (committed separately from within each project) |
| Copydesk creation | New project, independent |

## Key Decisions

- **Intent files as single source of truth** — replaced dual-maintenance between scaffold and intent files. Scaffold deleted.
- **`/install-app` replaces `/create-sample-app`** — catalog-driven, points to real example repos instead of copying a built-in sample.
- **Convention updates done from framework side** — one-off bootstrapping since projects lacked `/update` skill. Now that all projects have it, future updates pull from within each project.
- **Penny post letters for notification** — used the feedback system to notify projects of changes made without their AI context. Submitted as GitHub Issues for penny-post and duet; deposited directly in feedback-log for email-rewriter (no GitHub repo).
- **Copydesk naming** — chose an evocative name over a descriptive one (learned from penny-post renaming experience). Copydesk = the editorial desk where content gets polished for publication.
- **Copydesk migration approach** — generate fresh skeleton + migrate content, rather than pure retrofit or pure recreation. Old app reviews new app as quality gate (step 4).

## State at Close

- Framework: all 5 phases complete, committed
- Email-rewriter, penny-post, duet: convention updates applied, uncommitted (to be committed from within each project)
- Copydesk: skeleton generated, content migrated, uncommitted. Steps 3 (reconciliation) and 4 (old app review) pending — migration prompts left in both projects
- amg-ghost-tools: MIGRATION-REVIEW.md added, uncommitted
