---
name: pm-skills:team-status
description: Summarize shipped work, in-flight work, and risks for a team.
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
- Optional local config from `~/.config/pm-skills/config.yml` or `~/.pm-skills/config.yml`

# Instructions

- Treat local config as optional context. Use the role, team, company, and timezone if present.
- Default to the last 7 days unless the user specifies otherwise.
- Required tool: Linear. Optional tools: Granola and Notion.
- If Linear is unavailable, say: `Linear is not connected for pm-skills in this agent yet. Connect it, then rerun pm-skills:team-status.`
- Use Granola and Notion only to add useful context such as milestones, risks, decisions, or metrics.
- Use the configured team when present. If no team is configured, infer the most relevant scope from the available work.
- Never create or modify issues unless the user explicitly asks.
- Never invent issue IDs, project names, dates, counts, or metrics.
- Keep the output concise, scannable, and ready to paste into Slack.
- Follow `examples/output.md` as the canonical output template.
- Match its title format, section headings, numbered list style, and bold-first-sentence item pattern.
- Use the example sections in that order only.
- Use numbered lists.
- Start each item with a bold, concrete first sentence on the same line as the supporting detail.
- Link project names when possible.
- Keep the full answer to 300 words or less.
- Do not include Linear issue IDs in the output.

# Output

A team update that highlights delivered work, active work, risks, and near-term dates in a format that can be pasted directly into Slack or a status doc.

# Examples

Use `examples/output.md` as the formatting source of truth.
