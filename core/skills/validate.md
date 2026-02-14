# System Validation

You are validating this NLA system — checking that its pieces are consistent, its document references resolve, and its instructions would produce the intended behavior. You are not transforming content and you are not editing the system. You are inspecting it.

---

## Required Reading

Before validating, read:

1. **`CLAUDE.md`** — Skills table, key files, runtime identity
2. **`app/overview.md`** — How pieces connect, skill tables, document hierarchy

Do not read every app file upfront. Read specific files as validation requires them.

---

## Modes

`/validate` operates in three modes. If invoked with no arguments, run structural validation. If invoked with a scenario description, run scenario walkthrough. If the user describes expected-vs-actual behavior, run debug mode. If ambiguous, ask.

### Mode 1: Structural Validation

Check that the system's internal references are consistent. This is a mechanical check — verify that things point where they claim to point.

**What to check:**

1. **File references.** Read CLAUDE.md, app/overview.md, all task docs in `app/`, and all skill files in `.claude/skills/`. For every file path mentioned, verify the file exists. Report any broken references with the source file and the missing target.

2. **Skill table consistency.** Compare the skills tables in CLAUDE.md and app/overview.md. They should list the same skills. Check `reference/system-status.md` too if it has a skills table. Report any mismatches (skill in one table but not another).

3. **Thin wrapper targets.** For every skill in `.claude/skills/` that delegates to the framework (contains a `Read and follow` line pointing to `../nla-framework/`), verify the target file exists. Report any broken wrappers.

4. **Task doc references.** For each task doc in `app/`, check that referenced shared docs (`app/shared/voice-and-values.md`, `app/shared/common-patterns.md`, `app/shared/output-spec.md`) exist. Report missing shared docs.

5. **Document hierarchy.** If `app/overview.md` has a document hierarchy or index section, check that every file listed exists and every existing `app/` file is listed. Report gaps in either direction.

6. **Config consistency.** If `config.md` exists, check that any sub-configs it routes to (files in `config/`) exist. If `app/config-spec.md` exists, check that CLAUDE.md references it. Report issues.

**Output format:**

```
## Validation Results

### Issues Found
- [Category]: [Specific issue — source file, missing target, or mismatch details]

### All Clear
- [Category]: [What was checked and passed]
```

If everything passes, say so clearly. If issues are found, suggest fixes but do not make them — that is `/maintain`'s job.

### Mode 2: Scenario Walkthrough

Trace through the system's documentation step by step for a hypothetical scenario. This is a dry run — narrate what the LLM would read and decide without actually performing the task.

**Process:**

1. **Parse the scenario.** The user describes a situation: "A user pastes a 2000-word blog post with no headers and asks to format it." Identify which task and skill this maps to.

2. **Trace the doc chain.** Starting from CLAUDE.md, walk through every document the LLM would read to handle this scenario. For each document:
   - Name the document and the relevant section
   - Quote or paraphrase the directive that applies
   - State what decision it leads to
   - Note when judgment is being applied (vs. following explicit instruction)

3. **Identify gaps.** As you trace, note:
   - Points where no doc covers what to do
   - Ambiguous directives that could go multiple ways
   - Conflicting directives between documents
   - Judgment calls that feel under-specified

4. **Summarize.** Provide:
   - The complete decision chain (which docs, in what order, leading to what result)
   - Any gaps, ambiguities, or conflicts found
   - Suggestions for doc improvements (if any)

This traces one plausible path through the docs. Actual behavior may vary at judgment points — non-determinism is by design.

### Mode 3: Debug

The user tells you what they expected the system to do and what it actually did. Your job is to trace through the docs and explain why the actual behavior diverged.

**Process:**

1. **Understand the gap.** Ask clarifying questions if needed: What was the input? What did you expect? What actually happened? Which skill was running?

2. **Trace through docs.** Like scenario walkthrough, but focused: trace the path that would lead to the actual behavior. Identify the specific document and directive that caused the divergence.

3. **Check for trace files.** If tracing was enabled during the session, ask the user if a trace file exists in `reference/sessions/`. If it does, read it — it contains the actual decision chain, which is more reliable than reconstructing from docs alone.

4. **Diagnose.** Identify the root cause:
   - **Missing guidance** — No doc covers this case. The LLM improvised.
   - **Ambiguous directive** — The doc could be read multiple ways. The LLM read it differently than intended.
   - **Conflicting directives** — Two docs say different things. The LLM followed one over the other.
   - **Correct behavior, wrong expectation** — The docs are right; the user's expectation didn't match the documented behavior.
   - **Non-determinism** — The docs allow judgment; different runs may produce different results. This is by design.

5. **Recommend a fix.** Point to the specific document and section that needs editing. Describe what the change would be. Do not make the change — that is `/maintain`'s job.

Debug mode is significantly more powerful when trace files exist. If the user reports unexpected behavior and tracing was off, suggest enabling standard tracing (`/preferences`) to capture the decision chain next time.

---

## Scope

**You do:**
- Check internal consistency of the project's documentation structure
- Trace through docs for hypothetical scenarios
- Diagnose behavior divergence from expected outcomes
- Read trace files when available
- Suggest documentation fixes

**You don't:**
- Edit any files (that is `/maintain`)
- Run actual tasks (you narrate what would happen)
- Fix issues you find (report them; the user decides what to act on)
- Generate friction log entries (the user can invoke `/friction-log` for issues worth tracking)

---

*Validation is read-only inspection. Find problems, explain them, point to fixes — then hand off to `/maintain` or `/friction-log`.*
