---
name: pm-skills:triage-feedback
description: Audit product feedback from sources like Slack, meetings, docs, or support notes against trackers like Linear, and highlight coverage gaps.
---

# Purpose

Help a PM find product feedback from a specific source, check whether it is tracked, and close gaps without manually cross-referencing tools.

# When to use

- Before sprint planning to catch untracked feedback
- During goalie, support, or on-call handoff
- After an incident to verify follow-ups are filed
- Auditing a product area, customer, launch, or feedback theme

# Inputs

- Required: feedback source location, such as Slack channels, meeting notes, docs, support notes, or another connected source
- Required: topic, product area, customer, keyword, or audit goal
- Optional: tracker or planning system, such as Linear
- Optional: tracker team or project
- Optional: time period, defaulting to the last 7 days
- Optional: local config from `~/.config/pm-skills/config.yml` or `~/.pm-skills/config.yml`

# Instructions

- Treat local config as optional context. Use it to understand likely role, team, product area, and timezone if present.
- If the user does not specify where to search, ask for the feedback source before searching.
- Do not broadly search every connected source unless the user explicitly asks for a broad audit.
- Use the connected tool that matches the requested source and tracker.
- Slack and Linear are common examples, not requirements.
- If the requested source tool is unavailable, say which source is not connected and ask the user to connect it or choose another source.
- If the user asks for tracking coverage but does not name a tracker, infer from local config or connected issue-tracking tools. If still unclear, ask which tracker to check.
- If the requested tracker is unavailable, still produce the source inventory and mark tracking status as `Not checked`.
- Default to the last 7 days unless the user specifies otherwise.
- Search the source with exact terms, semantic variants, and related wording.
- Deduplicate findings by durable container, such as Slack thread, meeting note, doc page, support case, or similar record.
- Classify each finding as `Bug`, `Request`, or `Feedback`.
- Extract a concise summary, source or reporter, date, source link, and any tracker issue IDs already mentioned.
- Cross-reference directly mentioned issue IDs first. Otherwise search the selected tracker using key terms from the finding.
- Mark tracking status as `Tracked`, `Needs review`, `Untracked`, or `Not checked`.
- Use `Needs review` when there is a plausible tracker match but the relationship is not clear enough to call tracked.
- Urgency is a best guess using signals like severity words, customer impact, repeated reports, thread activity, incident language, stakeholder role, and tagged owner groups.
- Use urgency levels: `High`, `Medium`, and `Low`.
- Never invent messages, people, dates, links, tracker statuses, or issue IDs.
- Follow `examples/output.md` as the canonical output template.
- Keep the output concise: title, `tl;dr`, findings table, and issue-creation prompt.
- Use `Issue` as the tracker column heading.
- Link issue IDs, PR numbers, or tracker record numbers when URLs are available. Use plain text only when the tool returns an identifier without a URL.
- Limit the table to 15 rows, sorted by urgency first and newest date second.
- If more findings exist, mention the overflow count in the `tl;dr`.
- Include `Not checked` in the `tl;dr` only when one or more rows were not checked against a tracker.
- If there are no untracked items, replace the issue-creation prompt with a brief note that no new issues are needed.
- After presenting the report, offer to create issues for untracked items.
- Create issues only after the user selects row numbers or says `all`.
- If tracker, team, or project is unknown, ask before creating issues.
- When creating issues, use the source link, source or reporter, date, type, and relevant context in the description.
- Apply labels only when confidence is high. Default to `bug` only for clear bug rows when that label exists.
- Confirm each created issue with its ID and URL.

# Output

A concise feedback triage report with a `tl;dr`, a compact findings table, and an option to create missing tracker issues.

# Examples

Use `examples/output.md` as the formatting source of truth.
