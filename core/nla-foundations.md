# NLA Foundations

This document explains what natural language applications are and the principles that make them work. It's the conceptual foundation for everything else in this system. Read it first.

---

## What is an NLA?

### The Concept

A Natural Language Application (NLA) is software where the runtime is an LLM and the "code" is written in natural language.

**Traditional application:**
```
Code (Python, JavaScript) → Executed by interpreter/compiler → Output
```

**Natural Language Application:**
```
Documentation (Markdown) → Executed by LLM → Output
```

This isn't metaphor. The documentation literally IS the application. When you want to change behavior, you edit the docs. When you want to add features, you write more docs. The LLM reads the docs and does what they say.

### Why NLAs?

Some problems are hard to solve with traditional code:

| Problem | Traditional Code | NLA |
|---------|------------------|-----|
| "Is this paragraph a quote?" | Regex patterns, heuristics, edge cases | LLM reads it and knows |
| "Should there be a header here?" | Rules about word count, topic detection | LLM feels the narrative shift |
| "What's good link text for this URL?" | Domain mapping tables, fallbacks | LLM understands context |

These are judgment calls. Traditional code handles them through enumeration — listing every case. NLAs handle them through understanding — grasping intent and applying it.

**NLAs excel when:**
- The task requires judgment and synthesis
- Edge cases are numerous and hard to enumerate
- "I know it when I see it" describes the requirement
- The rules are easier to explain than to code

**Traditional code excels when:**
- Determinism is required (calculations, transactions)
- Speed is critical (millions of operations per second)
- The logic is well-defined and finite
- Auditability requires exact reproducibility

### The Hybrid Model

NLAs don't replace traditional code — they complement it. A well-designed system uses both:

**LLM handles:**
- Formatting decisions (is this a blockquote?)
- Pattern recognition (is this a Resources section?)
- Tone and voice (does this sound right?)
- Judgment calls (should I add a header here?)

**Traditional code handles:**
- API calls (reading from and writing to services)
- File I/O (reading CSVs, writing JSON)
- Triggers (detecting events, webhooks, scheduling)
- Validation (is the output valid structured data?)

The traditional code is plumbing. The NLA is the intelligence.

### NLA Shapes

NLAs aren't all the same shape:

**Stateless** — Input in, output out, done. An article formatter, a ticket classifier,
a code reviewer. No state persists between sessions.

**Persistent** — Work evolves across sessions. A composition tool, a writing assistant,
a design system. Persistent NLAs need some form of state management: where work lives,
how sessions pick up where they left off, how work moves through stages. The specific
mechanisms vary — the need doesn't.

The key challenge is session continuity. The LLM starts cold each session. Persistent
NLAs need curated state files that capture decisions, reasoning, and open questions —
not transcripts, but distillations of *why*. The framework's own session logs
(`reference/sessions/`) follow this pattern for maintenance work.

**Tool-using** — Some NLAs drive external tools: compilers, APIs, interpreters. The LLM
handles judgment and intent; external tools handle execution. When the NLA generates
runnable artifacts, the LLM can execute them directly — errors become conversation, not
stack traces.

Most NLAs are a mix. The shape informs which patterns apply.

---

## How to Read This System

When executing an NLA task:

1. **Read this document first** — understand what NLAs are and how they work
2. **Read the overview** (`overview.md`) — understand what this specific NLA does
3. **Read shared context** — voice, patterns, and output specs that all tasks use
4. **Read the specific task document** — follow it step by step
5. **Flag uncertainty** — when you're unsure, say so

The task document IS your instructions. Execute it, using judgment informed by shared context.

---

## Key Principles

### 1. The Documentation Is the Application

When the output is wrong, the fix is usually in the docs, not in code. Ask: "What would I need to write down for someone to do this correctly?" Write that down. The LLM will follow it.

### 2. Judgment Over Rules

NLAs work best when you explain the *why*, not just the *what*.

**Less effective:** "Use blockquotes for text starting with a quotation mark."

**More effective:** "Use blockquotes to visually emphasize powerful quotes. The reader should feel the weight of these words. One or two per article is usually enough — more dilutes the impact."

The LLM can apply judgment when it understands purpose.

### 3. The Cardinal Rule

**The human decides.** Humans bear consequences, so humans hold authority. The NLA
proposes, explains, and challenges — but the human has final say.

What this means in practice depends on the NLA's shape:
- Transformation: offer comparison against the original; make changes easy to revert
- Creation: explain decisions and reasoning; make work revertible through snapshots
- Classification/analysis: show confidence and reasoning; make it easy to override

In all cases: flag uncertainty. Never silently make consequential choices.

### 4. Hybrid Architecture

Let each system do what it does best:
- LLM: judgment, synthesis, understanding context
- Code: determinism, speed, API calls, validation

Don't use the LLM for things code does better. Don't use code for things that need judgment.

### 5. Iterate Through Documentation

The system improves by improving documentation:
1. Run the NLA
2. Review output
3. Identify gaps or mistakes
4. Update documentation
5. Run again

This is the development cycle for NLAs. The friction log and maintenance cycle formalize it.

### 6. Configuration Is Natural Language

Traditional config is structured: enums, booleans, key-value pairs. NLA config is
prose — interpreted by the LLM with the same judgment it applies to everything else.

This means config can express nuance that traditional config cannot:
- "Option A, but with this modification..."
- "Detailed explanations for voice decisions, brief for formatting"
- "Creative partner, but shift into educator mode when I'm struggling"

Enum options are convenient defaults — they make common choices easy. But natural
language is the real interface. Users can modify any setting with prose, and the LLM
synthesizes intent from the combination. No plugin architecture needed — the LLM's
ability to interpret nuanced instructions IS the extension mechanism.

---

*For what this specific NLA does and how its pieces connect, see [overview.md](overview.md).*
