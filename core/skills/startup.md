# NLA Runtime Initialization

You are the runtime for a Natural Language Application. Before doing any work, load foundational context by reading these documents **in order:**

1. **`../nla-framework/core/nla-foundations.md`** — What NLAs are, the hybrid model, key principles
2. **`app/overview.md`** — What this NLA does, how its pieces connect
3. **`app/shared/voice-and-values.md`** — The editorial identity; shapes every decision
4. **`app/shared/common-patterns.md`** — Transformations and patterns all tasks share
5. **`app/shared/output-spec.md`** — Output format details
6. **`config.md`** (if it exists) — User preferences and configuration. If config.md routes to sub-configs for the current context, read those too.

## After Loading

Confirm you've read the foundational documents. If config was loaded, note it ("Loaded user configuration"). If no config.md exists, that's fine — just note "No user configuration found." Then await task identification. The user will either:

- Invoke a specific skill (e.g., `/format-article`)
- Provide content or instructions that indicate which task to run
- Ask questions about the system (answer from the overview)

If the user provides content without invoking a skill, identify the task:

| User provides | Skill to suggest |
|---------------|-----------------|
| Raw content to format | `/format-article` |
| Questions about the system | Answer from `app/overview.md` |

## When to Re-Run This Skill

Run `/startup` again if:
- Your context has been compacted and you're unsure about project specifics
- You've been working for a long session and foundational context feels fuzzy
- You're switching between different tasks
