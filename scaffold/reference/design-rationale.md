# Design Rationale

This document explains WHY this NLA system is built the way it is. It captures the reasoning, trade-offs, and principles that shaped the design.

**Audience:** Future maintainers (human or AI) who need to understand the decisions behind the system before modifying it.

**Purpose:** Prevent well-intentioned "improvements" that break things that work. Provide context that won't be obvious from the docs alone.

---

## Why an NLA?

Some problems are better solved by explaining what you want than by coding rules to get there. If the task requires judgment — "is this quote worth emphasizing?", "should there be a header here?", "does this sound right?" — an NLA lets you write the explanation once and have the LLM apply it with understanding.

Traditional code handles judgment calls through enumeration (listing every case). NLAs handle them through understanding (grasping intent and applying it). For tasks with numerous edge cases and "I know it when I see it" requirements, NLAs are more maintainable and more capable.

---

## Why This Structure

### The Two Channels

```
app/                    ← Operative channel (LLM reads and executes)
  overview.md
  shared/
  [task docs]

../nla-framework/core/  ← Framework (shared NLA foundations and skills)
  nla-foundations.md
  skills/

reference/              ← Non-executing channel (maintainers read)
  design-rationale.md
  friction-log.md
  system-status.md
  sessions/
```

**Why separate:** The operative channel (`app/`) contains instructions the LLM follows. The reference channel (`reference/`) contains information about the system. Mixing them risks metadata influencing LLM behavior — for example, a friction log entry discussing a weakness could cause the LLM to second-guess correct behavior.

### Why `app/` Not `docs/`

The files in `app/` are the application, not documentation about an application. The name reflects function: these files are read and executed by the LLM runtime. Calling them "docs" implies they describe something else — they don't, they ARE the thing.

### Framework and Domain

This project depends on the NLA Framework at `../nla-framework/`. The framework provides universal NLA infrastructure — foundations, skill logic, and the improvement pipeline. This project provides domain-specific content — voice, patterns, task docs, and output specs.

Framework skills use thin wrappers in `.claude/skills/` that delegate to logic files in the framework. This means `git pull` on the framework updates skill behavior across all projects that use it, without touching domain content.

If you need to customize a framework skill, replace the thin wrapper with a full skill file. This "eject" pattern means the framework is a convenience, not a lock-in.

---

## Key Design Decisions

### Friction Log Not Loaded at Startup

The friction log (`reference/friction-log.md`) is NOT loaded during content transformation. It's reference material — loaded only by `/maintain` when that skill is invoked.

**Why:** Dual-channel separation. Maintenance data (known gaps, correction patterns) shouldn't influence runtime behavior. Also, allowing friction to accumulate before acting reveals patterns that single entries miss.

### The Improvement Pipeline

The improvement loop uses two skills:

- **`/friction-log`** — Captures observations from any context: during formatting, maintenance, or casual conversation. Produces entries in the friction log.
- **`/maintain`** — Processes friction log entries into documentation changes. Editorial, architectural.

**Why separate:** Capturing observations and editing system docs are different tasks with different guardrails. Separating them enables batching (accumulate learnings, then implement in one thoughtful pass) and lets `/maintain` see patterns across multiple observations.

### Friction Log Skill and Archive

A dedicated `/friction-log` skill enables logging observations from any context. The friction log also has an archive (`friction-log-archive.md`) where resolved entries are moved to keep the active log lean.

**Why a skill:** The LLM needs the friction log's format, purpose, and usage patterns loaded to create consistent entries. A skill provides this context on demand plus discoverability through the skills table.

**Template portability:** The skill reads the entry format from `friction-log.md` rather than hardcoding it, so it adapts to any project's field conventions.

### Lists in Special Sections

Special sections (Resources, References, Call to Action) originally had no specific formatting guidance for multiple items. When a section contained several independent items — separate book recommendations, separate sources — consecutive paragraphs could blur together.

**The change:** Guidance to use bulleted lists when items are independent and scannable; paragraphs when the text is a single item or narrative.

**Why judgment, not a rule:** The guidance explains *why* lists help (scannability, item independence) rather than giving a mechanical threshold. This is a natural NLA judgment call — the LLM reads the content, understands whether items are parallel or narrative, and formats accordingly.

### Judgment Over Rules

The docs explain *why*, not just *what*. "Use blockquotes to emphasize powerful quotes — the reader should feel the weight" is more useful than "use blockquotes for text starting with a quotation mark." Purpose enables edge-case handling in ways that rules never can.

---

## Adding Decisions

When you make architectural changes (not just wording fixes), add an entry here documenting:
- What was decided
- Why (including what alternatives were considered)
- What it affects

This prevents future maintainers from re-introducing approaches that already failed or undoing decisions that had good reasons.

---

*This document is updated by the `/maintain` skill when architectural decisions are made.*
