---
description: Summarize recent meetings and extract action items
argument-hint: [topic or date range]
---

Use the meeting-digest skill to summarize recent meetings and extract action items.

Filter: $ARGUMENTS (if provided, use as topic or date range filter).

**CRITICAL**: You MUST follow the template format exactly from `@pm-claude-skills/skills/meeting-digest/templates/meeting-digest-template.md`. Read the template file before generating output to ensure format consistency.

Load personal context from `~/.claude/pm-claude-skills.local.md` for the user's name and preferences.

If the Granola MCP server is not connected, print setup instructions instead.
