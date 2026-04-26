---
name: pm-skills:slack-recap
description: Prioritize Slack catch-up into urgent items, action needed, review threads, and FYIs after PTO, deep work, or missed messages.
---

# Purpose

Help a PM catch up on Slack by separating urgent items from useful background noise.

# When to use

- After travel or PTO
- After a day of deep work
- Before a weekly planning pass

# Inputs

- Optional time period
- Optional channels, people, or topics to prioritize
- Optional local config from `~/.config/pm-skills/config.yml` or `~/.pm-skills/config.yml`

# Instructions

- Treat local config as optional context. Use it to understand likely channels, role, and timezone if present.
- Default to the last 7 days unless the user specifies otherwise.
- Required tool: Slack.
- If Slack is unavailable, say: `Slack is not connected for pm-skills in this agent yet. Connect it, then rerun pm-skills:slack-recap.`
- Use multiple searches to gather high-signal messages:
  - mentions of the user
  - urgency keywords
  - messages from the user that now have replies or strong reaction activity
  - messages from configured stakeholders or key channels
- Deduplicate results before scoring them.
- Score messages into four sections: urgent, action needed, for review, and FYI.
- Never invent messages, people, permalinks, or timestamps.
- Keep the output scannable, prioritized, and Slack-ready.
- Follow `examples/output.md` as the canonical output template.
- Match its title format, section headings, numbered list style, and bold-first-sentence item pattern.
- All four sections must be present.
- Use numbered lists.
- Start each item with a bold, concrete first sentence on the same line as the supporting detail.
- Max 5 items per section.
- Keep the full answer to 300 words or less.
- Write `None found` for empty sections.

# Output

A prioritized Slack recap grouped into urgent items, action items, review items, and FYIs.

# Examples

Use `examples/output.md` as the formatting source of truth.
