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
- Optional source material, such as pasted threads, message exports, or channel summaries
- Local context from `~/.config/pm-skills/config.yml` or `~/.pm-skills/config.yml` when available

# Instructions

- Use local context only for defaults like role, team, product area, and timezone. Do not treat it as message evidence.
- Default to the last 7 days unless the user specifies otherwise.
- Preferred tool: Slack.
- Use Slack when connected; otherwise ask the user to paste or export the relevant messages.
- Use multiple searches to gather high-signal messages:
  - mentions of the user
  - urgency keywords
  - messages from the user that now have replies or strong reaction activity
  - messages from configured stakeholders or key channels
- Deduplicate results before scoring them.
- Score messages into four sections: urgent, action needed, for review, and FYI.
- Never invent messages, people, permalinks, or timestamps.
- Keep the output scannable, prioritized, and Slack-ready.
- Use `examples/output.md` as the canonical output shape.
- Keep the title unnumbered. Immediately after it, write one clear, concise, concrete line in the form `**tl;dr:** ...` with the most urgent action and useful message counts, or state that nothing actionable was found.
- Treat the `tl;dr` as the unnumbered lead, not a section. Follow it with supported sections from `Urgent`, `Action Needed`, `For Review`, and `FYI` as sequential numbered headings.
- Include only sections with useful items.
- Renumber the remaining sections sequentially when a category is omitted.
- Use hierarchically numbered subheadings only when a genuine nested structure is needed. Do not use bold or italic labels as substitute section headings.
- Use a short paragraph when a section contains one coherent point. When a section needs multiple distinct points, use a numbered list to make the recap easier to scan.
- Apply bolding per numbered list. If every item in a list is one sentence, do not bold any item. If any item has two or more sentences, bold exactly the first sentence of every item in that list and keep all later sentences normal. Never mix bolded and unbolded first sentences within the same list; a bold sentence is content, not a substitute section heading.
- Max 5 items per section.
- Keep the full answer to 300 words or less.
- If nothing actionable is found, say so briefly instead of adding empty sections.

# Output

A prioritized Slack recap grouped by the useful sections found: urgent items, action items, review items, and FYIs.
