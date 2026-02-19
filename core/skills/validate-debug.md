# Debug

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
