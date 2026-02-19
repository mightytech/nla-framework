# Scenario Walkthrough

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
