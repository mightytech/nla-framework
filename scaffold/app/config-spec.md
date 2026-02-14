# Configuration Spec

This document defines what users of this NLA can configure. The `/preferences` skill reads this to guide the configuration conversation and enforce constraints.

---

## What's Configurable

Users can adjust how the formatter behaves without changing the core application docs. The main areas:

### Voice and Tone

The application has a defined voice in `voice-and-values.md`. Users can adjust the tone within that identity — for example, shifting formality level or warmth — but the core editorial values (accuracy, attribution, clarity) are not configurable.

**Default:** Use the voice as defined in `voice-and-values.md` without modification.

### Formatting Preferences

Users can adjust how aggressively the formatter adds structure:

- **Header frequency** — How readily to add section headers at topic shifts. Some users prefer more structure, others want a lighter touch.
- **Emphasis style** — How liberally to use blockquotes and bold for key points. Range from "minimal — only when truly impactful" to "generous — highlight most key insights."
- **Paragraph length** — Whether to break long paragraphs or preserve the author's original paragraph structure.

**Defaults:** Moderate headers (at clear topic shifts only), minimal emphasis (one or two per article), preserve original paragraph structure.

### TK Notes

Users can adjust how much uncertainty flagging they want:

- **Verbose** — Flag every judgment call, even minor ones
- **Standard** — Flag significant uncertainty and structural changes
- **Minimal** — Only flag things that could change meaning

**Default:** Standard.

### Output Length

Users can set preferences about output length relative to input — whether the formatter should tend toward concise output or preserve the full length of the original.

**Default:** Preserve original length; don't cut or pad.

### Special Sections

Users can configure which special sections (Resources, Learn More, Call to Action) the formatter should look for and create:

- Always include a specific section type
- Never include a specific section type
- Use default behavior (include when the content naturally supports it)

**Default:** Include when content supports it.

### Framework Path

If the NLA Framework is not at the standard sibling location (`../nla-framework/`), users can specify the actual path.

**Default:** `../nla-framework/`

### Tracing

Runtime tracing logs the LLM's decisions during work sessions — which documents it read, what directives it found, what it decided and why. Useful for debugging unexpected behavior, understanding how the application's docs interact, and verifying that voice, patterns, and task instructions are applied as intended.

**Trace level:**

- **Off** — No tracing. Default.
- **Standard** — Log major decisions: which docs read, what directives found, what was decided, and why.
- **Detailed** — Log everything including routine operations, alternatives considered, and directives that were read but didn't apply.
- **Custom** — User writes natural language describing exactly what to trace. Example: "Detailed for voice decisions, standard for formatting, off for file loading." The LLM interprets the description and applies judgment about what to log.

**Trace output:** `reference/sessions/trace-YYYY-MM-DD.md`. One file per day; if a trace file already exists for today, append with a session separator.

**Trace format:** Default format for trace entries. Users can override by creating `config/trace-format.md`. If that file exists, use its format instead.

Default trace entry format:

```
### [HH:MM] Decision Point

**Context:** [What was happening — which skill/task, what step]
**Read:** [Document path and section]
**Directive found:** [The relevant instruction, quoted or paraphrased]
**Decision:** [What was decided]
**Reasoning:** [Why — especially when judgment was applied]
```

For standard level, include only entries where a meaningful decision was made. For detailed level, include every document read and every directive evaluated.

**Observer effect:** Tracing changes behavior. The act of logging decisions consumes context window and may cause the LLM to reason more deliberately than it would untraced. At standard level this is minor. At detailed level it is significant. Traced sessions are not perfectly representative of untraced sessions.

**Performance:** Overhead scales with level. Standard is recommended for routine debugging. Use detailed for targeted sessions, not as always-on.

**Defaults:** Tracing off. Default format as above.

---

## Constraints

- Voice values (accuracy, attribution, clarity) are editorial standards, not preferences. Users cannot configure the system to skip attribution or be inaccurate.
- The Cardinal Rule (human can always compare and revert) is not configurable.
- TK notes can be adjusted in verbosity but cannot be disabled entirely — some uncertainty flagging must remain.

---

## Guidance for the Config Conversation

When users aren't sure what to configure, start with the most impactful settings: voice tone and formatting preferences. These have the most visible effect on output.

For first-time users, suggest trying the defaults first and coming back to `/preferences` after they've seen some output. Configuration is most useful when you know what you want to change.

---

*This spec is maintained by the app developer via `/maintain`. Users interact with config through `/preferences`.*
