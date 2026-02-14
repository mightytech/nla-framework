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
2. **`scaffold/CLAUDE.md`** — Domain project skills table
3. **`scaffold/app/overview.md`** — Domain project skill tables and document hierarchy

Do not read every file upfront. Read specific files as validation requires them.

---

## Modes

`/validate` operates in three modes. If invoked with no arguments, run structural validation. If invoked with a scenario description, run scenario walkthrough. If the user describes expected-vs-actual behavior, run debug mode. If ambiguous, ask.

### Mode 1: Structural Validation

Check that the framework's internal references are consistent. The framework has more reference surfaces than a domain project — check them all.

**What to check:**

1. **Framework file references.** Read `CLAUDE.md` and `README.md`. For every file path mentioned, verify the file exists. Report broken references.

2. **Framework skill registration.** List all skills in `.claude/skills/`. Compare against the skills table in `CLAUDE.md`. Report any mismatches (skill directory exists but not in table, or table entry with no skill directory).

3. **Scaffold skill registration.** List all skills in `scaffold/.claude/skills/`. Compare against skills tables in `scaffold/CLAUDE.md`, `scaffold/app/overview.md`, and `scaffold/reference/system-status.md`. Report any mismatches across these three surfaces.

4. **Core-to-scaffold alignment.** For every file in `core/skills/`, check that a corresponding thin wrapper exists in `scaffold/.claude/skills/`. For every thin wrapper in scaffold, check that it targets an existing core skill file. Report gaps in either direction.

5. **Thin wrapper paths.** For every thin wrapper in `scaffold/.claude/skills/`, verify the target path (e.g., `../nla-framework/core/skills/maintain.md`) resolves to an existing file within the framework. Report broken wrapper paths.

6. **Scaffold file references.** Read `scaffold/CLAUDE.md`, `scaffold/app/overview.md`, `scaffold/README.md`. Check that referenced files exist within `scaffold/`. Report broken references.

7. **Document hierarchy.** If `scaffold/app/overview.md` has a document hierarchy or index, check that listed files exist and existing `scaffold/app/` files are listed. Report gaps.

8. **Config consistency.** Check that `config-spec.md` exists at framework root. Check that `scaffold/app/config-spec.md` exists. If `config.md` exists, check that routing rules point to existing files in `config/`. Report issues.

9. **README directory listings.** Check that directory trees in `README.md` and `scaffold/README.md` reflect the actual directory contents. Report stale listings.

**Blast radius tagging:** For each issue found, note:
- **Framework operation** — issues in `.claude/skills/`, `CLAUDE.md`, `config-spec.md`
- **All domain projects** — issues in `core/`
- **New projects only** — issues in `scaffold/`

**Output format:**

```
## Validation Results

### Issues Found
- [Category] (blast radius: [framework | all projects | new projects]): [Specific issue]

### All Clear
- [Category]: [What was checked and passed]
```

Suggest fixes but do not make them — that is `/maintain`'s job.

### Mode 2: Scenario Walkthrough

Trace through documentation step by step for a hypothetical scenario. The framework supports two contexts:

- **Framework context** (default): Trace a scenario where someone uses the framework itself — running `/create-app`, `/maintain`, etc.
- **Domain project context**: Trace a scenario as if operating inside the scaffold project — running `/format-article`, `/startup`, etc.

Ask the user which context if ambiguous.

**Process:**

1. **Parse the scenario.** Identify which skill and context this maps to.

2. **Trace the doc chain.** Starting from the relevant CLAUDE.md, walk through every document the LLM would read. For each document:
   - Name the document and the relevant section
   - Quote or paraphrase the directive that applies
   - State what decision it leads to
   - Note when judgment is being applied (vs. following explicit instruction)

3. **Identify gaps.** Note:
   - Points where no doc covers what to do
   - Ambiguous directives that could go multiple ways
   - Conflicting directives between documents
   - Judgment calls that feel under-specified

4. **Summarize.** Provide the complete decision chain, any issues found, and suggestions for doc improvements.

This traces one plausible path through the docs. Actual behavior may vary at judgment points — non-determinism is by design.

### Mode 3: Debug

The user describes what they expected the framework to do and what it actually did. Trace through the docs to explain the divergence.

**Process:**

1. **Understand the gap.** Ask clarifying questions if needed: What was the input? What did you expect? What actually happened? Which skill was running?

2. **Trace through docs.** Trace the path that would lead to the actual behavior. Identify the specific document and directive that caused the divergence.

3. **Check for trace files.** If tracing was enabled, ask if a trace file exists in `reference/sessions/`. If so, read it for the actual decision chain.

4. **Diagnose.** Identify the root cause:
   - **Missing guidance** — No doc covers this case
   - **Ambiguous directive** — Could be read multiple ways
   - **Conflicting directives** — Two docs disagree
   - **Correct behavior, wrong expectation** — Docs are right; expectation didn't match
   - **Non-determinism** — Docs allow judgment; different runs produce different results

5. **Recommend a fix.** Point to the specific document and section. Note the blast radius of any suggested change. Do not make the change.

---

## Scope

**You do:**
- Check internal consistency across framework, core, and scaffold layers
- Trace through docs for hypothetical scenarios in either context
- Diagnose behavior divergence
- Read trace files when available
- Tag issues with blast radius

**You don't:**
- Edit any files (that is `/maintain`)
- Run actual tasks (you narrate what would happen)
- Fix issues you find (report them)
- Judge scaffold content quality (scaffold is intentionally sample content — check structure, not prose)

---

*Validation is read-only inspection. Find problems, tag their blast radius, point to fixes — then hand off to `/maintain` or `/friction-log`.*
