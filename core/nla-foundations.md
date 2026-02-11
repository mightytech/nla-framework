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

---

## How to Read This System

When executing an NLA task:

1. **Read this document first** — understand what NLAs are and how they work
2. **Read the overview** (`overview.md`) — understand what this specific NLA does
3. **Read shared context** — voice, patterns, and output specs that all tasks use
4. **Read the specific task document** — follow it step by step
5. **Flag uncertainty** — use TK notes when you're unsure

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

**The human must always be able to compare changes against the original and easily revert.**

This means:
- Obvious additions (headers, callouts) don't need comment — the original had none
- Text restructuring must offer options, including "keep original"
- TK notes flag uncertainty
- Never silently change meaning

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

---

*For what this specific NLA does and how its pieces connect, see [overview.md](overview.md).*
