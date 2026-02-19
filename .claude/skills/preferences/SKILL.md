---
name: preferences
description: Create or edit your preferences for how the NLA Framework tools behave — /create-app defaults, maintenance mode, verbosity, and more.
disable-model-invocation: true
---

# Framework Preferences

You are helping the user create or edit their personal configuration for the NLA Framework. Config lets users customize how the framework's tools behave without modifying the framework itself.

This is a conversation, not a form. The user expresses what they want naturally — you ask clarifying questions, then generate well-structured config files. Human provides intent, you provide structure.

---

## Required Reading

On invocation, read:

1. **`config-spec.md`** — What's configurable, defaults, constraints. This defines what knobs exist for framework behavior.
2. **`config.md`** (if it exists) — Current user configuration. Read to understand what's already set before proposing changes.
3. **All files in `config/`** (if the directory exists) — Current sub-configs.

---

## Two Modes

### Create Mode (no config.md exists)

The user has no configuration yet. Guide them through initial setup:

1. Briefly explain what config does: "Configuration lets you personalize how the framework tools work for you — things like how much `/create-app` asks before generating, how verbose explanations are, and maintenance mode behavior. Your preferences live in config files separate from the framework."

2. Based on `config-spec.md`, walk through the configurable areas. Don't present every option — highlight the most impactful ones and ask open-ended questions: "Do you want `/create-app` to ask where to save projects, or just use a default location?"

3. Accept whatever the user provides — freeform descriptions, specific values, or "just use the defaults." Shape their input into structured config.

4. Generate `config.md` (and `config/` sub-files if needed). Show the user what you've written before saving.

### Edit Mode (config.md exists)

The user already has configuration. Ask what they want to change:

1. Summarize current config briefly: "You have X active directives and Y contextual sub-configs."

2. Ask what they'd like to change. Accept anything from specific ("make /create-app skip the location question") to exploratory ("the tools feel too chatty").

3. Propose changes. Show the before and after. Get approval before writing.

---

## The Quarterback Pattern

`config.md` is the main config file — always loaded at session start. It has two jobs:

1. **Hold always-active directives** — preferences that apply in every context
2. **Route to sub-configs** — directives that say "when in context X, also read `config/X.md`"

When deciding where a directive belongs:

- **Always-active** (goes in `config.md`): preferences that apply everywhere — verbosity, explanation style, general workflow preferences
- **Contextual** (goes in a sub-config): preferences that only apply in specific modes — maintenance behavior, /create-app tweaks, friction log defaults

When in doubt, put it in `config.md`. Sub-configs are for when the user has enough context-specific preferences to warrant a separate file.

---

## Config File Format

Config files are Markdown — natural language, not YAML. A directive can be structured:

```markdown
Default project directory: ~/projects/
Verbosity: terse
```

Or behavioral:

```markdown
When generating files during /create-app, narrate what each file does rather than silently creating them.
```

Or conditional:

```markdown
When in maintenance mode, always enter planning mode before making changes.
```

The LLM reads these and applies judgment. Both forms are valid. Use whichever is clearest for the directive. Structured for values, behavioral for preferences, conditional for context-dependent rules.

---

## Conflict Detection

After any change to config files, perform a conflict check:

1. **Read all active config directives** — main config.md plus any sub-configs that would be active in the current context
2. **Read relevant framework docs** — `CLAUDE.md` grounding principles, skill files that config might affect
3. **Check for:**
   - **Conflicts between config directives** — two directives that contradict each other
   - **Conflicts between config and framework behavior** — a config preference that contradicts the framework's grounding principles or skill logic
   - **Ambiguities** — directives that could be interpreted multiple ways

4. **If issues found:** Flag them to the user with specific quotes from both sides. Ask how to resolve. Don't silently pick a winner.

5. **If clean:** Confirm: "No conflicts detected between your config and the framework docs."

### Precedence

When config and framework docs interact, precedence is governed by `config-spec.md`. The framework defines:

- If the spec says users can override a behavior, config takes precedence
- If the spec says users can only adjust within a range, config modifies within that boundary
- If the spec doesn't address it, flag the ambiguity rather than assuming

---

## Approval Gate

**Always show config changes to the user before writing.** Format the proposed config as a code block so they can see exactly what will be written. For edits, show what changed (before -> after).

Only write after confirmation.

---

## Scope

**You do:**
- Create config.md and config/ files from user preferences
- Edit existing config files based on user requests
- Run conflict detection after changes
- Explain what's configurable based on config-spec.md
- Shape freeform user input into well-structured config

**You don't:**
- Edit framework docs or skills (that's `/maintain`)
- Edit config-spec.md (that's `/maintain` — the framework developer controls what's configurable)
- Override constraints from config-spec.md (if the spec says "don't allow X", respect it)
- Write config without user approval

---

*Config is the user's space. They express preferences naturally; you structure them into files the framework can use. When in doubt, ask — don't assume.*
