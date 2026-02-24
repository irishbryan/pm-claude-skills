---
name: team-status
description: >
  Generate a team-wide status report from Linear. Use when asked for "team
  status", "weekly update", "sprint summary", "what did the team ship",
  "leadership rollup", "standup summary", or "sprint review".
allowed-tools:
  - mcp__linear__*
  - mcp__granola__*
  - mcp__notion__*
---

## PM Guidance
- You are assisting a Product Manager. Prioritize clarity, data, and stakeholder communication.
- Output style: Succinct, scannable, Slack-ready. Avoid verbosity while providing enough context.
- Never create or modify Linear issues unless explicitly asked.
- Never fabricate Linear issue identifiers — only use real data from the API.
- Date format: Mon DD (e.g., Feb 22, target Mar 5).
- Include specific metrics when available: percentages, dates, user counts.
- NO Linear issue IDs in output - link project names instead.
- Read ~/.claude/pm-claude-skills.local.md for personal context (name, email, focus areas, and any additional config).

## Instructions

**TEMPLATE ENFORCEMENT**: You MUST read and follow `@templates/team-status-template.md` EXACTLY. The template defines four required sections: Shipped, In Progress, Blocked / At Risk, and Key Upcoming Dates. Do not deviate from this structure or add extra sections.

1. Read `~/.claude/pm-claude-skills.local.md` for user context. If teams are configured, use them to scope queries.
2. Query Linear MCP for team's work over requested period (default: last 7 days):
   - Completed issues → Shipped section
   - In-progress issues → In Progress section
   - Blocked or flagged items → Blocked / At Risk section
3. Query Granola for strategic context:
   - Specific metrics from experiments/launches
   - Key decisions and upcoming milestones
   - Current blockers with context
   - Use context but do NOT include Granola citation links (they are private)
4. Follow `@templates/team-status-template.md` exactly:
   - Use ONLY these four sections: ## Shipped, ## In Progress, ## Blocked / At Risk, ## Key Upcoming Dates
   - NO "Summary" or other extra sections - jump straight to Shipped
   - Use bullet points (-), NOT numbered lists
   - Format: **[Project Name](linear-url)**: {Description}
   - Project names are the links (bold + hyperlink), NOT issue IDs
   - Keep descriptions succinct but informative (avoid follow-up questions)
   - Include specific metrics when available
5. Group by project/workstream, prioritize most important items first
6. Quality gates:
   - Total output: ≤300 words (down from 500)
   - Format: Slack-ready, scannable
   - NO Linear issue IDs (e.g., CLO-28, SEAM-265)
   - Focus on outcomes with enough context to avoid follow-up questions
7. If `$ARGUMENTS` provided, override time period
