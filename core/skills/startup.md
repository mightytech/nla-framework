# NLA Runtime Initialization

You are the runtime for a Natural Language Application. Before doing any work, load foundational context by reading these documents **in order:**

1. **`../nla-framework/core/nla-foundations.md`** — What NLAs are, the hybrid model, key principles
2. **`app/overview.md`** — What this NLA does, how its pieces connect
3. **`app/shared/values.md`** — Commitments and priorities; shapes every decision across execution and maintenance
4. **`app/shared/common-patterns.md`** — Transformations and patterns all tasks share
5. **`app/shared/output-spec.md`** (if it exists) — Output format details
6. **`config.md`** (if it exists) — User preferences and configuration. If config.md routes to sub-configs for the current context, read those too.

## App-Specific Initialization

After loading foundational context, check if `app/startup.md` exists. If it does,
read and follow it. This is where the app defines additional startup steps —
scanning for active work, checking environment, presenting status — that vary
by domain.

If it doesn't exist, skip this step. Not every NLA needs app-specific initialization.

## Update Check (Optional)

If `config.md` contains a directive to check for updates at startup, read and follow
`../nla-framework/core/skills/check-updates.md` before presenting the loading
confirmation. Include the results in the startup summary so the user knows what's
available.

If no such directive exists, skip this step. Update checking at startup is off by
default — it requires network access and adds latency.

## After Loading

Confirm you've read the foundational documents. If config was loaded, note it
("Loaded user configuration"). If no config.md exists, that's fine — just note
"No user configuration found." Then await the user. They will either:

- Invoke a specific task skill
- Provide content or instructions that indicate which task to run
- Ask questions about the system (answer from `app/overview.md`)

If the user provides input without invoking a skill, consult `app/overview.md`
to identify the appropriate task.

## When to Re-Run This Skill

Run `/startup` again if:
- Your context has been compacted and you're unsure about project specifics
- You've been working for a long session and foundational context feels fuzzy
- You're switching between different tasks
