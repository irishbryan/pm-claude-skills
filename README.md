```
╭────────────────────────────╮
│         pm-skills          │
╰────────────────────────────╯
```

Essential product management skills anyone can use. Get help making decisions, shaping products, writing status updates, summarizing meetings, and more.

## Skills

- `create-issue`: Turn a rough task into a well-shaped issue anyone can pick up and execute.
- `estimate-timeline`: Create a timeline estimate with a launch date and dated milestones.
- `triage-feedback`: Audit feedback from sources like Slack, meetings, docs, or support notes against an issue tracker.
- `make-decision`: Turn a fuzzy tradeoff into a concrete decision memo with a recommendation.
- `frame-problem`: Turn a vague request, complaint, or opportunity into a well-framed problem worth shaping or deferring.
- `shape-product-pitch`: Turn a rough product idea into a shaped pitch with scope, rationale, and constraints.
- `my-status`: Draft a concise personal status update from recent work.
- `team-status`: Summarize shipped work, in-flight work, and risks for a team.
- `meeting-digest`: Pull decisions, takeaways, and action items out of recent meetings.
- `slack-recap`: Catch up on Slack and focus on the threads that need attention.

Skills that reference tools like Slack, Linear, Granola, or Notion use them when connected. If a tool is unavailable, the skill should still work from pasted notes, exports, or summaries; creating or updating records requires the relevant tool connection and explicit approval.

## Quick Start

```bash
git clone <repo>
cd pm-skills
./script/setup
```

That’s it. `script/setup` asks for a few optional defaults, writes local context to `~/.config/pm-skills/config.yml`, and installs Claude Code and Codex skills as symlinks pointing back to this clone.

Use:

- Claude Code: `/pm-skills:my-status`
- Codex: `$pm-skills:my-status`

When new skills are added:

```bash
git pull
./script/setup
```

Personalization is optional. Skills use local context for defaults like name, team, role, product area, and timezone; they should not treat it as task evidence. Do not store secrets in `~/.config/pm-skills/config.yml`.

To remove installed artifacts later, run `./script/uninstall`.
