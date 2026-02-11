---
name: friction-log
description: Log observations, issues, or positive findings to the framework's friction log
disable-model-invocation: true
---

# Framework Friction Log Entry

You are capturing an observation to the framework's friction log — the framework's learning journal. You are not editing the framework. You are recording something worth remembering.

This skill can be invoked from any context during framework maintenance.

---

## Required Reading

On invocation, read these sections from **`reference/friction-log.md`**:

1. **"How to Use This Log"** — Entry types, severity levels, when to add entries
2. **The entry format/template section** — Field definitions and structure
3. **"Patterns to Watch"** — Recurring themes the framework is monitoring

**Do not** read the full entries list. You need the format and the patterns, not the history.

---

## Before Drafting

Search for related history. Grep `reference/friction-log.md` and `reference/friction-log-archive.md` for terms related to the observation. Note connections in your draft's Notes field.

---

## Adaptive Conversation

The human may give you a detailed paragraph or a quick note. Adapt.

### When the user provides enough context

Draft the entry immediately. Show it for approval.

### When context is incomplete

Ask targeted questions about what's genuinely missing. The most important thing is a clear observation.

### The principle

The human provides flexibility; you provide structure underneath.

---

## Entry Creation

### Format

Follow the entry template defined in `reference/friction-log.md`. Read the format from the file.

Key rules:
- New entries always start with **Status: pending**
- Entry headings use `###` (H3 level)
- Heading format: `### YYYY-MM-DD — [Brief descriptive title]`
- Write to the **Entries** section, newest first

### Blast radius note

When logging observations about `core/` changes, note in the entry that these affect all domain projects. When logging about `scaffold/`, note they only affect new projects.

### Approval gate

**Always show the complete drafted entry to the user before writing it to the file.**

### What you produce

You produce entries from observations about the framework — issues with skill logic, scaffold gaps, documentation clarity, patterns across domain projects. If the user provides before/after examples and confirmed reasons, include those details.

---

## Scope

**You do:**
- Create friction log entries about the framework
- Search for related history
- Suggest connections to Patterns to Watch

**You don't:**
- Edit framework documentation (that's `/maintain`)
- Resolve or archive entries (that's `/maintain`)
- Make system changes based on the observation

Your job ends when the entry is written. `/maintain` will process it later.

---

*When in doubt: log it. A pending entry with a clear observation is always better than an unrecorded insight.*
