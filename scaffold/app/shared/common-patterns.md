# Common Patterns

Transformations and patterns shared across all tasks. When multiple tasks need the same logic, it lives here.

---

## Text Cleanup

### Character Replacements

| From | To | Notes |
|------|----|-------|
| `--` | – (en-dash) | Double hyphen to en-dash |
| Straight quotes (`"` `'`) | Curly quotes (" " ' ') | Smart quotes throughout |
| Multiple consecutive blank lines | Single blank line | Clean up spacing |

### Formatting Artifacts

Remove common artifacts from raw content:
- Repeated divider lines (`---`, `===`, `***`)
- Trailing whitespace
- Redundant line breaks within paragraphs

---

## Links

### Converting URLs to Links

When you encounter a bare URL in raw content, convert it to a descriptive link.

**The rule:** Link text should tell the reader where they're going and why.

| URL Type | Link Text |
|----------|-----------|
| News article | Publication name (e.g., "the New York Times") |
| Organization website | Organization name |
| Book on a retailer | Retailer name (e.g., "Amazon", "Bookshop") |
| Blog post | Post title |
| Research paper | Brief description or paper title |

**Wrong:** "Click here" or "this link" or the bare URL
**Right:** Descriptive text that makes sense without the surrounding sentence

---

## Headers

### When to Add Headers

Add a header when:
- The topic genuinely shifts
- A long piece needs landmarks for scanning
- A new section begins (resources, references, etc.)

Don't add a header:
- Every few paragraphs on a schedule
- When the transition is already smooth
- For short pieces that flow naturally

### Header Level

- H2 for major sections
- H3 for subsections within an H2
- Don't skip levels (H2 → H4)

---

## Emphasis

### Blockquotes

Use blockquotes to visually emphasize powerful quotes. The reader should feel the weight of these words.

**Good candidates:**
- Quotes that capture the essence of the piece
- Emotionally resonant statements
- Key insights or turning points

**Not good candidates:**
- Informational quotes without emotional weight
- Quotes that primarily provide facts
- Anything already serving its purpose in flowing text

**Limit:** One or two blockquotes per article. More dilutes the impact.

**Attribution:** Goes outside the blockquote, not inside it. The blockquote contains only the quoted words.

### Bold and Italics

- **Bold** for terms being defined or key phrases on first use
- *Italics* for emphasis within sentences, titles of works
- Don't overuse either — if everything is emphasized, nothing is

---

## Special Sections

### Resources

A section collecting useful links, books, or tools for going deeper.

**Format:** Grouped logically (books, websites, tools), with brief descriptions.

**Recognize by:** Links to products, books, deep dives, or the subject's own projects and work.

### References / Learn More

A section collecting sources and further reading.

**Format:** List with descriptive link text.

**Recognize by:** Links to news articles, organizations, research — things that inform rather than things to buy or use.

### Call to Action

A section encouraging the reader to do something specific.

**Format:** Direct, actionable language. One clear ask, not a laundry list.

**Recognize by:** "You can...", "Join...", "Support...", petitions, volunteer opportunities.

### Lists vs. Paragraphs in Special Sections

Special sections often contain independent items — separate recommendations, separate sources, separate action steps. Think about how a reader will use each section:

- When items are independent and a reader would benefit from scanning them individually, use a bulleted list
- When the text is a single item or reads as a connected thought, a paragraph works fine

The goal is scannability. Readers come to these sections looking for something specific. Lists help them find it. But a Call to Action with one ask, or a References paragraph that tells a brief story before linking, shouldn't be forced into bullet form just because it could be.

---

## TK Notes

When uncertain about a decision, flag it with a TK note rather than guessing.

| Note | When to use |
|------|-------------|
| `TK [VERIFY]` | You made a judgment call that needs human review |
| `TK [QUESTION]` | You couldn't determine the right approach |
| `TK [MISSING]` | Content is needed (image, link, data) |
| `TK [SUGGESTION]` | You have an alternative to propose |

TK notes are temporary — they're resolved during human review, not left in published content.

---

*These patterns apply across all tasks. Task-specific patterns live in the task docs themselves.*
