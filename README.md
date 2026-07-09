# pm-skills

> **tl;dr:** PM skills turn messy product context into clear decisions, issues, plans, and updates. Engineers have found them useful because they reduce back-and-forth and make product work easier to act on.

## Skills

| Skill | Helps with |
|---|---|
| `frame-problem` | Getting from a vague request to a clear problem, business value, and next step. Inspired by [Framing](https://www.ryansinger.co/framing/) |
| `shape-product-pitch` | Turning a framed problem and direction into a concise product pitch. Inspired by [Shape Up](https://basecamp.com/shapeup) |
| `create-okr` | Creating, sharpening, grading, and target-setting concise OKRs. Inspired by [What Matters](https://www.whatmatters.com/) |
| `create-strategy-canvas` | Creating a Blue Ocean Strategy-style strategy canvas with competitive factors, competitor evaluation, readable value charts, and ERRC moves. Inspired by [Strategy Canvas](https://www.blueoceanstrategy.com/tools/strategy-canvas/) |
| `create-issue` | Writing tracker-ready issues with context, done criteria, and scope |
| `estimate-timeline` | Creating launch estimates with milestones, risks, and scope tradeoffs |
| `make-decision` | Turning fuzzy tradeoffs into decision memos with recommendations |
| `my-status` | Drafting concise personal PM status updates |
| `team-status` | Summarizing shipped work, in-flight work, risks, and upcoming dates |
| `meeting-digest` | Pulling decisions, context, and action items out of meeting notes |
| `slack-recap` | Prioritizing missed Slack context into urgent items, actions, reviews, and FYIs |
| `triage-feedback` | Auditing feedback against tracked work and finding coverage gaps |

## Install

```bash
git clone <repo>
cd pm-skills
./script/setup
```

## Use

| Agent | Command |
|---|---|
| Claude Code | `/pm-skills:frame-problem` |
| Codex | `$pm-skills:frame-problem` |

## Notes

`script/setup` installs the skills and writes optional local context to `~/.config/pm-skills/config.yml`.

Local context gives defaults like name, team, role, product area, and timezone. It is not task evidence.

Some skills can use Slack, Linear, Granola, or Notion when connected. If tools are unavailable, paste notes, exports, or summaries instead. Creating or updating records requires explicit approval.

## Update

```bash
git pull
./script/setup
```

## Uninstall

```bash
./script/uninstall
```
