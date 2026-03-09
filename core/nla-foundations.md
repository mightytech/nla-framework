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
3. **Read shared context** — voice, patterns, and output specs that tasks share
4. **Read the specific task document** — follow it step by step
5. **Flag uncertainty** — when you're unsure, say so

The task document IS your instructions. Execute it, using judgment informed by shared context.

**A note on language.** The prose in this system encodes assumptions — about what kind of NLA this is, what tasks it handles, how users work with it. When behavior feels too narrow, the cause is often narrow language. Fixing it usually means broadening existing language rather than adding new rules. The LLM fills the space when constraints are loosened.

---

## Key Principles

### 1. Imperfection Is Assumed

NLAs are never finished. The documentation will have gaps, the voice will drift, the edge cases will surprise. This isn't a failure state — it's the expected state, at creation and throughout the lifetime of the application.

This assumption shapes everything else. The improvement loop exists because the system will always need improving. The human decides because the system knows it can't fully trust its own instructions. When something feels wrong during execution — a rule that produces bad output, a gap where guidance should exist — flag it. The friction log is the primary development tool for a system that gets better through use.

### 2. The Documentation Is the Application

When the output is wrong, the fix is usually in the docs, not in code. Ask: "What would I need to write down for someone to do this correctly?" Write that down. The LLM will follow it.

### 3. Principles and Procedures

Prose "code" has two tools. **Principles** explain *why* — they shape judgment across
many situations. **Procedures** specify *when* — they produce specific behaviors
reliably. Know which you're reaching for. If something needs to happen every time at a
specific moment, a principle alone won't reliably produce it; add a procedural step. If
something needs to shape how the AI thinks across many contexts, a procedure can't
cover every case; write a principle. The best instructions often use both — the
principle ensures the AI does it well, the procedure ensures it does it at all.

### 4. Judgment Over Rules

NLAs work best when you explain the *why*, not just the *what*.

**Less effective:** "Use blockquotes for text starting with a quotation mark."

**More effective:** "Use blockquotes to visually emphasize powerful quotes. The reader should feel the weight of these words. One or two per article is usually enough — more dilutes the impact."

The LLM can apply judgment when it understands purpose.

### 5. Values Are Visible

Every NLA embeds value choices — what to prioritize, what to protect, what tradeoffs
to make. All priorities are value choices, varying in stakes but not in category.
"Keep it concise" and "never misrepresent sources" are both values; the difference
is consequence, not kind. Some carry legal weight (HIPAA compliance, accessibility
requirements); some are stylistic. The mechanism is the same.

Traditional code embeds the same choices invisibly — in scoring functions, filter
criteria, if/else branches. An NLA states them in prose: readable, debatable,
modifiable by anyone who can read. This transparency is a capability and a
responsibility.

There is no neutral default. An NLA with no explicit values still has values — they're
the model's training defaults, unexamined. Making values explicit is what distinguishes
an NLA that *has* values from one that merely inherits them.

### 6. The Cardinal Rule

**The human decides.** Humans bear consequences, so humans hold authority. The NLA
proposes, explains, and challenges — but the human has final say.

What this means in practice depends on the NLA's shape:
- Transformation: offer comparison against the original; make changes easy to revert
- Creation: explain decisions and reasoning; make work revertible through snapshots
- Classification/analysis: show confidence and reasoning; make it easy to override

In all cases: flag uncertainty. Never silently make consequential choices.

### 7. Hybrid Architecture

Let each system do what it does best:
- LLM: judgment, synthesis, understanding context
- Code: determinism, speed, API calls, validation

Don't use the LLM for things code does better. Don't use code for things that need judgment.

### 8. Configuration Is Natural Language

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

## Working Rhythms

These are the common patterns of work in an NLA. They aren't mandatory steps — they're
rhythms that emerge naturally from the system's design. Understanding them helps the AI
assist proactively and helps humans know what to expect.

### The Improvement Loop

Work → notice friction → log it → maintain → iterate. The friction log captures
observations while context is fresh; `/maintain` turns them into documentation changes.
This is the primary development cycle for NLAs — the system improves by improving its
own documentation. Insights evaporate if not captured; systematic logging turns casual
observations into durable improvements.

### The Design Flow

Think → plan → implement → debrief. Design judgment happens before implementation
planning, not during it. `/think` explores what to build and why; planning mode handles
how; `/debrief` captures process learning while context is fresh. Skipping the thinking
phase risks building the right thing wrong — or the wrong thing right.

### The Update Cycle

Check for updates → update → validate. NLAs and their packages evolve independently.
`/check-updates` shows what's changed upstream; `/update` pulls changes and applies
intent; `/validate` confirms nothing broke. Periodic sync keeps shared foundations
current without losing local customization.

### Session Structure

Startup → work → close. The LLM starts cold each session — `/startup` loads context
so it can operate effectively. Work happens (tasks, maintenance, exploration). `/close`
preserves state so the next session starts warm instead of cold. Without this
bookending, every session begins with "where were we?"

---

*For what this specific NLA does and how its pieces connect, see `app/overview.md`.*
