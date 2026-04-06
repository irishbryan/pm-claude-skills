Essential product management skills anyone can use. Get help making decisions, shaping products, writing status updates, summarizing meetings, and more.

## Skills

| Skill | Problem it solves |
|---|---|
| `estimate-timeline` | Helps create a timeline estimate with a launch date and dated milestones. |
| `make-decision` | Turns a fuzzy tradeoff into a concrete decision memo with a recommendation. |
| `shape-product-pitch` | Turns a rough product idea into a clearer pitch with scope, rationale, and constraints. |
| `my-status` | Turns recent work into a concise personal update you can paste into Slack, docs, or leadership updates. |
| `team-status` | Summarizes what a team shipped, what is in flight, and where risks or blockers are building. |
| `meeting-digest` | Pulls the signal out of recent meetings and turns it into decisions, takeaways, and action items. |
| `slack-recap` | Helps you catch up on Slack and focus on the threads that actually need attention. |

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
