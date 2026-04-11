```
╭────────────────────────────╮
│         pm-skills          │
╰────────────────────────────╯
```

Essential product management skills anyone can use. Get help making decisions, shaping products, writing status updates, summarizing meetings, and more.

## Skills

- `create-issue`: Turn a rough task into a well-shaped issue anyone can pick up and execute.
- `estimate-timeline`: Create a timeline estimate with a launch date and dated milestones.
- `make-decision`: Turn a fuzzy tradeoff into a concrete decision memo with a recommendation.
- `shape-product-pitch`: Turn a rough product idea into a shaped pitch with scope, rationale, and constraints.
- `my-status`: Draft a concise personal status update from recent work.
- `team-status`: Summarize shipped work, in-flight work, and risks for a team.
- `meeting-digest`: Pull decisions, takeaways, and action items out of recent meetings.
- `slack-recap`: Catch up on Slack and focus on the threads that need attention.

## Quick Start

```bash
git clone <repo>
cd pm-skills
./script/setup
```

That’s it. `script/setup` asks for a few optional defaults, writes local config to `~/.config/pm-skills/config.yml`, and installs Claude Code and Codex skills as symlinks pointing back to this clone.

Use:

- Claude Code: `/pm-skills:my-status`
- Codex: `$pm-skills:my-status`

When new skills are added:

```bash
git pull
./script/setup
```

Personalization is optional. Skills should still work without local config. Do not store secrets in `~/.config/pm-skills/config.yml`.

To remove installed artifacts later, run `./script/uninstall`.
