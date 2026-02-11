# Format Article

Transform raw, unformatted content into a polished, well-structured article.

---

## Purpose

The Format Article task takes raw content — rough drafts, pasted text, informal writing — and applies editorial standards to produce a publication-ready piece:
- Adds structure (headers, sections)
- Converts URLs to descriptive links
- Cleans up formatting artifacts
- Identifies special sections (resources, calls to action)
- Adds emphasis where warranted
- Flags uncertainty with TK notes

## Input

- Raw content: unformatted text, often pasted from another source

## Output

- Formatted article following the output spec and voice guidelines
- TK notes for any uncertain decisions

---

## Prerequisites

**Before running this task, read:**

1. **[NLA Foundations](../nla-framework/core/nla-foundations.md)** — Understand what you're doing
2. **[Voice and Values](shared/voice-and-values.md)** — The editorial identity
3. **[Common Patterns](shared/common-patterns.md)** — Transformations you'll apply
4. **[Output Spec](shared/output-spec.md)** — Output format details

---

## Processing Steps

### Step 1: Read and Understand

Read the entire raw content before making any changes. Understand:
- What is this about?
- Who is the audience?
- What's the narrative arc?
- What's the author's intent?

Don't start formatting until you understand the whole piece.

### Step 2: Clean Up

Apply cleanup patterns from common-patterns.md:
- Fix character issues (dashes, quotes, spacing)
- Remove formatting artifacts
- Normalize line breaks

### Step 3: Structure

Add structure based on the content's natural flow:
- Identify topic shifts and add headers
- Break up wall-of-text paragraphs where natural breaks exist
- Don't add structure where the text flows naturally

**Remember:** Headers mark genuine shifts. If you're unsure whether a header is needed, it probably isn't.

### Step 4: Links

Convert bare URLs to descriptive links:
- Follow the link text patterns in common-patterns.md
- If you can't determine good link text, use `TK [VERIFY]: link text` and provide your best guess

### Step 5: Emphasis

Identify quotes or passages worthy of blockquote emphasis:
- Maximum 1-2 per article
- Choose the most powerful, not all that qualify
- Attribution goes outside the blockquote

### Step 6: Special Sections

Identify and format special sections if present:
- Resources (books, tools, projects)
- Learn More / References (sources, further reading)
- Call to Action (things the reader can do)

Not every article has these. Don't force them.

When a section has multiple independent items, a bulleted list helps readers scan. When it's a single item or narrative text, a paragraph is fine.

### Step 7: Review

Before finalizing:
- Read the formatted version as a reader would
- Check that the voice matches the guidelines
- Verify no meaning was changed
- Ensure TK notes flag anything uncertain
- Confirm the output follows the output spec

---

## Judgment Calls

This task is full of judgment calls. That's the point — an LLM can make these where traditional code can't.

**When uncertain:** Flag it with a TK note. The human can always adjust. A flagged judgment call is better than a silent wrong choice.

**When the content is ambiguous:** Present options. "I structured it as [X], but it could also work as [Y] — TK [SUGGESTION]."

**When the raw content is already good:** Don't over-format. Sometimes raw content just needs cleanup and links, not a full restructure. Less is more.

---

*The goal is not perfection — it's a great starting point that the human can quickly review and publish.*
