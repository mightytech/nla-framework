---
name: validate
description: Validate the NLA Framework's internal consistency, trace scenarios through docs, or debug unexpected behavior.
disable-model-invocation: true
---

# Framework Validation

You are validating the NLA Framework — checking that its internal references resolve, its skill registrations are consistent across all surfaces, and its documentation would produce intended behavior for both framework users and domain project users.

You are not editing the framework. You are inspecting it.

---

## Required Reading

Before validating, read:

1. **`CLAUDE.md`** — Framework skills table, key files
2. **`install/CLAUDE-intent.md`** — What a domain project's runtime identity should establish
3. **`install/skills-intent.md`** — What skill wrappers domain projects should have

Do not read every file upfront. Read specific files as validation requires them.

---

## Mode Selection

When invoked with clear intent, skip the menu and route directly to the appropriate mode. When invoked without clear intent, present these options:

> **"Are the framework's files wired up correctly?"**
> Structural check. Verifies file references, skill registrations, intent file consistency, and README accuracy. Fast and mechanical.

> **"Do the framework's docs tell a consistent story?"**
> Architecture review. Walks the full document chain checking for coherence issues. Thorough — reads most of the framework's docs. Writes findings to a file in `reference/sessions/`.

> **"Walk me through a scenario"**
> Scenario walkthrough. Describe a situation and I'll trace through the docs showing what would happen and where gaps exist. Supports both framework context (using `/create-app`, `/maintain`, etc.) and domain project context (using intent files to understand a well-formed project).

> **"Something's not working as expected"**
> Debug. Describe expected vs. actual behavior and I'll trace through docs to explain the divergence.

---

## Mode Routing

After selecting a mode, read and follow the corresponding core file, then apply the framework-specific addenda below.

| Mode | Core file |
|------|-----------|
| Structural check | `core/skills/validate-structural.md` |
| Architecture review | `core/skills/validate-architecture.md` |
| Scenario walkthrough | `core/skills/validate-scenario.md` |
| Debug | `core/skills/validate-debug.md` |

### Structural Addenda

After running the core structural checks, also check:

1. **Framework file references.** Read `CLAUDE.md` and `README.md`. For every file path mentioned, verify the file exists.
2. **Framework skill registration.** List all skills in `.claude/skills/`. Compare against the skills table in `CLAUDE.md`. Report mismatches.
3. **Core skill coverage.** For every file in `core/skills/`, check that a corresponding entry exists in `install/skills-intent.md`. Report missing entries.
4. **Intent file skill consistency.** For every skill in `install/skills-intent.md`, verify the target core skill file exists. Report broken references.
5. **Intent file completeness.** Verify `install/CLAUDE-intent.md`, `install/skills-intent.md`, and `install/structure-intent.md` all exist. Check that `install/example-catalog.md` exists.
6. **Config consistency.** Check that `config-spec.md` exists. If `config.md` exists, check routing targets.
7. **README directory listings.** Check that directory trees in `README.md` reflect actual contents.

**Blast radius tagging:** For each issue found, note:
- **Framework operation** — issues in `.claude/skills/`, `CLAUDE.md`, `config-spec.md`
- **All domain projects** — issues in `core/`
- **Project generation** — issues in `install/` intent files

### Scenario Addenda

The framework supports two trace contexts:
- **Framework context** (default): Trace scenarios where someone uses the framework itself — running `/create-app`, `/maintain`, etc.
- **Domain project context**: Trace scenarios as if operating inside a domain project — running domain tasks, `/startup`, etc. Use the intent files to understand what a well-formed domain project looks like.

Ask the user which context if ambiguous.

### Debug Addenda

When recommending fixes, note the blast radius of each suggested change (framework operation / all domain projects / project generation).

---

## Scope

**You do:**
- Check internal consistency across framework, core, and intent file layers
- Walk the document chain checking for coherence issues
- Trace through docs for hypothetical scenarios in either context
- Diagnose behavior divergence
- Read trace files when available
- Tag issues with blast radius

**You don't:**
- Edit any files (that is `/maintain`)
- Run actual tasks (you narrate what would happen)
- Fix issues you find (report them)
- Judge intent file content quality (check structure and consistency, not prose)

---

*Validation is read-only inspection. Find problems, tag their blast radius, point to fixes — then hand off to `/maintain` or `/friction-log`.*
