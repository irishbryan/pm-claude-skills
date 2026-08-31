---
name: pm-skills:team-status
description: Draft a team status update with shipped work, in-flight work, risks, blockers, upcoming dates, and leadership-ready summary.
---

# Purpose

Help a PM produce a concise team-wide status update that is useful for leadership, partner teams, and weekly team communication.

# When to use

- Weekly team updates
- Sprint reviews
- Leadership rollups
- Cross-functional status reviews

# Inputs

- Optional time period
- Optional team scope
- Optional audience or level of detail
- Optional source material, such as pasted issues, project updates, meeting notes, or team summaries
- Local context from `~/.config/pm-skills/config.yml` or `~/.pm-skills/config.yml` when available

# Instructions

- Use local context only for defaults like role, team, company, product area, and timezone. Do not treat it as work evidence.
- Default to the last 7 days unless the user specifies otherwise.
- Preferred tool: Linear. Optional tools: Granola and Notion.
- Use connected tools when available; otherwise ask the user to paste or summarize team work.
- Use Granola and Notion only when available to add useful context such as milestones, risks, decisions, or metrics.
- Use the configured team when present. If no team is configured, infer the most relevant scope from the available work.
- Never create or modify issues unless the user explicitly asks.
- Never invent issue IDs, project names, dates, counts, or metrics.
- Keep the output concise, scannable, and ready to paste into Slack.
- Use `examples/output.md` as the canonical output shape.
- Keep the title unnumbered. Immediately after it, write one clear, concise, concrete line in the form `**tl;dr:** ...` with the most important progress, near-term focus, and material risk.
- Treat the `tl;dr` as the unnumbered lead, not a section. Follow it with sequential numbered section headings: `Shipped`, `In Progress`, `Blocked or At Risk`, and `Upcoming Dates`.
- Use hierarchically numbered subheadings only when a genuine nested structure is needed. Do not use bold or italic labels as substitute section headings.
- Use the example sections in that order only.
- Use a short paragraph when a section contains one coherent point. When a section needs multiple distinct points, use a numbered list to make the update easier to scan.
- Apply bolding per numbered list. If every item in a list is one sentence, do not bold any item. If any item has two or more sentences, bold exactly the first sentence of every item in that list and keep all later sentences normal. Never mix bolded and unbolded first sentences within the same list; a bold sentence is content, not a substitute section heading.
- Link project names when possible.
- Keep the full answer to 300 words or less.
- Do not include Linear issue IDs in the output.

# Output

A team update that highlights delivered work, active work, risks, and near-term dates in a format that can be pasted directly into Slack or a status doc.
