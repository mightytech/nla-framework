---
name: format-article
description: Format raw content into a polished article following voice and style guidelines
disable-model-invocation: true
---

# Format Article

You are formatting content. Your job is to transform raw, unformatted content into a polished article.

## Execute

Read and follow the instructions in **`app/format-article.md`**. That document is your primary source of truth for this task.

It will direct you to read prerequisite docs (voice/values, common patterns, output spec) if you haven't already. Follow that prerequisite chain.

## Input

If invoked with arguments, `$ARGUMENTS` contains the raw content to format.

Otherwise, the user will provide content in conversation.

## Key Guardrails

These apply throughout formatting — they're non-negotiable:

- **The Cardinal Rule:** The human must always be able to compare your changes against the original and easily revert.
- **Flag uncertainty:** Use TK notes (`TK [VERIFY]`, `TK [QUESTION]`, `TK [MISSING]`, `TK [SUGGESTION]`) for any judgment call that might need adjustment.
- **Less is more.** Let the writing breathe. Don't over-format.

## What NOT to Do

- Don't write code to solve content problems — use editorial judgment
- Don't skip the documentation — read it every time, it may have been updated
- Don't make silent changes — flag restructuring with TK notes
- Don't over-format — not every paragraph needs a header, not every quote needs emphasis
