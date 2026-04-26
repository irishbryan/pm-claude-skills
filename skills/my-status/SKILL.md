---
name: pm-skills:my-status
description: Draft a personal PM status update for weekly updates, 1:1 prep, leadership notes, progress, next steps, risks, and asks.
---

# Purpose

Turn recent PM work into a short update that emphasizes outcomes, next steps, and asks.

# When to use

- Weekly updates
- 1:1 prep
- Leadership or stakeholder rollups

# Inputs

- Optional time period
- Optional audience or format preference
- Optional focus areas that matter most this week
- Optional local config from `~/.config/pm-skills/config.yml` or `~/.pm-skills/config.yml`

# Instructions

- Treat local config as optional context. Use it to understand role, team, company, and timezone, but do not block if it is missing.
- Default to the last 7 days unless the user asks for a different period.
- Required tool: Linear. Optional tool: Granola.
- If Linear is unavailable, say: `Linear is not connected for pm-skills in this agent yet. Connect it, then rerun pm-skills:my-status.`
- Use Granola only to add strategic context such as decisions, blockers, or milestones.
- Cast a wide net for PM work: assigned issues, created issues, project work, coordination work, and follow-through.
- Never create or modify issues unless the user explicitly asks.
- Never invent issue IDs, project names, dates, or metrics.
- Keep the output Slack-ready and concrete.
- Follow `examples/output.md` as the canonical output template.
- Match its title format, section headings, numbered list style, and bold-first-sentence item pattern.
- Use the example sections in that order only.
- Use numbered lists.
- Start each item with a bold, concrete first sentence on the same line as the supporting detail.
- Keep the full answer to 250 words or less.
- Focus on outcomes and impact, not issue IDs.
- If a section has no useful data, write `None this period`.

# Output

A short personal update with progress, next steps, and asks that is easy to paste into Slack or a doc.

# Examples

Use `examples/output.md` as the formatting source of truth.
