# Standards Review

Read each in-scope document against the NLA writing standards. Find places
where the doc doesn't meet a standard, name the standard, suggest the fix.
This mode asks a specific diagnostic question — *does this doc match the
rubric?* — distinct from coherence (within-doc consistency) and
architecture (between-doc consistency).

The standards file is at `reference/standards/nla-writing.md`. In a domain
project, it's at `packages/nla-framework/reference/standards/nla-writing.md`.

### When to Run

- After the standards file evolves — re-check existing docs against the new bar
- When a doc feels off but passes structural and coherence checks
- Periodic quality sweep, especially over docs that predate the standards
- Before promoting a doc that hasn't been reviewed against the standards

---

## Process

### 1. Scope the Review

Decide which docs and which standards to read against. A focused pass
finds more than a broad one — empirically, the most diagnostic standards
(2.3 and 4.4) produce more findings per unit of attention than a full-pass
review.

If the user invokes this mode without specifying scope, offer the default
and let them adjust:

> **Default scope:** operative content (`core/` in framework, `app/` and
> `.claude/skills/` in domain projects), reviewed against standards 2.3
> (produces what it contains) and 4.4 (cross-references with context).
> These are the standards Phase 2 of feedback log entry #21 found most
> diagnostically productive. Want this default, or scope differently?

Common scoping patterns:

| Question being asked | Docs | Standards |
|----------------------|------|-----------|
| "Are operative docs producing what they should?" (default) | Operative content | 2.3, 4.4 |
| "Is this specific skill written well?" | One skill file | Section 2 + 8.1 |
| "Do session logs follow the format?" | `reference/sessions/` | 8.2 |
| "Did the latest standards change invalidate current docs?" | Whatever the changed standard touches | The changed standards |
| "Full quality sweep" | Everything in scope | All applicable standards |

### 2. Read Each Document Against the Standards

For each in-scope doc, read it fully. For each standard in the chosen
subset, ask: does this doc meet the standard? If not, where exactly, and
what would the fix look like?

Cite the specific standard. Standards-grounded feedback is more useful
than generic feedback:

- Generic: "This skill is unclear about when to apply judgment."
- Standards-grounded: "*Standard 2.3 violation:* the skill says 'apply
  judgment here' without describing what judgment looks like in this
  context. The LLM won't fill the gap from general knowledge — needs an
  example or boundary case."

### 3. Write Findings Incrementally

Append findings to `reference/sessions/YYYY-MM-DD-standards-review.md`
as you go, file by file. If the review is interrupted, partial findings
remain valuable.

### 4. Classify Severity

- **Fix** — The doc will mislead the LLM into wrong behavior.
- **Improve** — The doc could mislead in edge cases. Worth fixing but not urgent.
- **Note** — Minor craft issue worth recording but not changing now.

### 5. Track Standards Without Findings

When a standard in the chosen subset produces no findings across the
in-scope docs, record it as validated. This matters for understanding
which standards earn active diagnostic status — the framework's posture
is that standards earn their place by producing findings, not by
editorial preference.

---

## Output

The findings file:

```markdown
# Standards Review: [Scope description]

**Date:** YYYY-MM-DD
**Scope:** [Docs reviewed]
**Standards applied:** [Subset reviewed]

## Findings

### Fix
- `[file]:[section]` — [Issue, citing standard X.Y]

### Improve
- `[file]:[section]` — [Issue, citing standard X.Y]

### Note
- `[file]:[section]` — [Issue, citing standard X.Y]

## Standards Without Findings
- [Standard X.Y]: validated across [scope], no current gaps

## Summary
[N findings: M fix, K improve, J note. Overall assessment.]
```

After presenting findings, route them through `/validate`'s common
disposition step — fix-now / defer to friction log / wont-fix per
finding.

---

*Standards review asks a different question than the other validation
modes: not "are the pieces consistent with each other?" (architecture) or
"does each doc work as a unit?" (coherence) but "does each doc meet the
rubric?" The rubric is the standards file. The mode is most valuable when
the standards file changes — which it will, as the framework learns.*
