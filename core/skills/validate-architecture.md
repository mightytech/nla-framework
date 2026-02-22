# Architecture Review

Walk the full document chain checking for coherence issues. This is not a runtime check (that's structural validation or scenario walkthrough) — it's an architecture review for a system whose architecture is expressed in prose.

### When to Run

- After restructuring (file moves, splits, renames, new layers)
- After adding a new layer (new voice package, new platform, new shared doc)
- Periodically as the system grows
- When output quality degrades without obvious cause

---

## Process

### 1. Map the Document Chain

Identify the sequence of files the LLM reads from startup through task execution. This is the NLA's "call graph." Start from CLAUDE.md (or `/startup` if it exists), follow prerequisites, references, and delegation lines through to task completion. Note conditional branches (files loaded only in certain contexts).

### 2. Walk Each File

Read every file in the chain fully. For each file, check against the analytical categories below. Note issues with file path and specific location.

### 3. Analytical Categories

Not all categories apply to all NLAs. Before beginning, consider which matter most for this NLA's structure. These are a framework for analysis, not an exhaustive checklist.

**Path resolution** — Can the LLM find the files it's told to read? Check that file references include paths, not just names. After context compaction, the LLM can't resolve "Values" to a file — it needs `app/shared/values.md`.

**Cross-reference integrity** — Do references between docs point to the right places? Look for references to files that have moved, been renamed, or been split. A file that references "Ghost implementation details" by name in a layer that shouldn't know about Ghost has a cross-reference problem.

**Layer boundaries** — Is each concern in the right file? Platform rendering shouldn't live in voice pattern files. Voice conventions shouldn't live in CLAUDE.md. When restructuring splits files, content sometimes lands in the wrong layer.

**Consistency** — Is the same concept described the same way everywhere? Look for conventions (naming conventions, emoji patterns, formatting rules) defined in one place and described differently in another.

**Conditional completeness** — When something is optional, do all references handle the missing case? If prerequisites say "Voice Format Guide (if available)" but the processing step says "Use the voice format guide" without the conditional, there's a gap.

**Generic/specific alignment** — Do generic docs avoid hardcoding specific instances? After generalization, generic docs sometimes still reference specific voices, platforms, or configurations as if they were universal.

**Prerequisite sufficiency** — Are listed prerequisites enough for the LLM to execute? Check that prerequisite lists include everything the task actually needs. Missing prerequisites cause silent quality degradation — the LLM improvises instead of following documented guidance.

**Contradiction** — Do two documents give opposing instructions? Look for directives that conflict — one file says "always" while another says "only when." Contradictions are especially common after restructuring when content is split across files.

**Orphaned content** — Files or sections that nothing in the document chain references. After restructuring, some content may be left behind — still present in the directory but unreachable from the document chain. This is dead code.

**Values consistency** — Do task docs and behaviors align with the NLA's stated values (`app/shared/values.md`)? Check whether implicit priorities in task instructions, common patterns, or voice contradict explicit values — a task doc that optimizes for engagement when values.md says accuracy comes first, or a pattern that silently drops content when values.md commits to completeness. This is especially important after restructuring, when behavior may shift without values being reconsidered.

**Language breadth** — Do docs assume a specific NLA shape when they should be shape-neutral? Look for language that implicitly narrows the NLA's identity — words that assume transformation, deterministic output, or a specific workflow when the context should be universal. This is a distinctly NLA failure mode: constraints encoded in word choices rather than logic.

### 4. Write Findings Incrementally

Write findings to `reference/sessions/YYYY-MM-DD-architecture-review.md` as you go. Don't wait until the end — if the review is interrupted, partial findings are still valuable.

### 5. Classify Severity

- **Fix** — Will cause incorrect behavior or confusion. The LLM will make wrong decisions.
- **Improve** — Could cause confusion in edge cases. Worth fixing but not urgent.
- **Note** — Worth knowing but not worth changing now.

---

## Output

The deliverable is the findings file in `reference/sessions/`. Structure it as:

```markdown
# Architecture Review: [NLA Name]

**Date:** YYYY-MM-DD

## Document Chain
[Map of the chain — what loads what, in what order]

## Findings

### Fix
- [File]: [Issue] — [Category]

### Improve
- [File]: [Issue] — [Category]

### Note
- [File]: [Issue] — [Category]

## Summary
[X findings: N fix, N improve, N note. Overall assessment.]
```

This file is the handoff to `/maintain`. The reviewer identifies problems; the maintainer decides what to fix.
