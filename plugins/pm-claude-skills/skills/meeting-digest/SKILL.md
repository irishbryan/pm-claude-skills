---
name: meeting-digest
description: >
  Summarize recent meetings and extract action items. Use when asked for
  "meeting digest", "summarize meetings", "action items from meetings",
  "what was decided", "meeting notes", or "meeting summary".
allowed-tools:
  - mcp__granola__*
---

## PM Guidance
- You are assisting a Product Manager. Prioritize clarity, brevity, and Slack-ready format.
- Output style: Concise, scannable, ready to copy-paste to Slack.
- Focus on high-signal information only — omit context, background, and nice-to-haves.
- Date format: Mon DD (e.g., Feb 22).
- Read ~/.claude/pm-claude-skills.local.md for personal context.

## Instructions

1. Read `~/.claude/pm-claude-skills.local.md` to get the user's name and preferences.
2. Check if the Granola MCP server is connected. If not, print the following message and stop:
   ```
   Granola is not connected. Run `script/setup` and answer 'y' to the Granola question, then authenticate via `/mcp`.
   ```
3. Use Granola MCP tools to query meetings. If `$ARGUMENTS` is provided, use it as a topic or date range filter.
4. Extract from the meeting:
   - One-sentence tl;dr (concrete outcome or decision)
   - Up to 3 key discussion points (high-signal only, be specific)
   - Action items with clear owners and deliverables
5. Follow `@templates/meeting-digest-template.md` exactly.
6. Quality gates:
   - tl;dr must be one clear sentence, not generic
   - Max 3 discussion points — pick the most important
   - Every action item must have owner name
   - Total output: ≤150 words
   - Ready to copy-paste to Slack with no edits needed
7. Do NOT include:
   - Open questions or parking lot items
   - Meeting context or background
   - Decisions without concrete outcomes
   - Granola citation links (they are private)
