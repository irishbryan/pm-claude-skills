---
name: pm-skills:meeting-digest
description: Summarize recent meetings and extract decisions and action items.
---

# Purpose

Pull the highest-signal takeaways out of recent meetings so a PM can quickly share what matters.

# When to use

- After a staff meeting
- After a project sync
- After a roadmap or decision review

# Inputs

- Optional topic or date range
- Optional meeting title or project scope
- Optional local config from `~/.config/pm-skills/config.yml` or `~/.pm-skills/config.yml`

# Instructions

- Treat local config as optional context only.
- Required tool: Granola.
- If Granola is unavailable, say: `Granola is not connected for pm-skills in this agent yet. Connect it, then rerun pm-skills:meeting-digest.`
- Use the user input as a topic, date, or meeting filter when provided.
- Extract only the highest-signal details:
  - one concrete `tl;dr`
  - up to 3 discussion points
  - action items with clear owners
- Never invent attendees, decisions, or action items.
- Do not include Granola citation links.
- Keep the output brief, high-signal, and Slack-ready.
- Follow this output shape exactly:
  - `# {Meeting Title}`
  - `**tl;dr:** ...`
  - `**Key Discussion Points:**`
  - `**Action Items:**`
- Use numbered lists under both sections.
- Up to 3 discussion points. Action items must have clear owners.
- Start each list item with a bold, concrete first sentence on the same line as the supporting detail.
- Keep the full answer to 150 words or less.
- Do not add extra sections beyond these four elements.

# Output

A short meeting digest with a title, one `tl;dr`, a few discussion points, and clear action items.

# Examples

See `examples/output.md`.
