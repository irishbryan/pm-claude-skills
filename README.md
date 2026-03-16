# pm-skills

Essential PM skills for Claude Code and Codex.

- Generate the updates PMs write all the time: team status, personal status, meeting digests, and Slack recaps.
- Use the same skills across tools instead of rebuilding prompts for each agent.
- Get started quickly with one setup script.

<p align="center">
  <img width="1000" alt="PM Tools Overview" src="https://github.com/user-attachments/assets/d6cfc988-1056-4a23-962a-90e5c31852a0" />
</p>

## Quick Start

1. `script/setup`
2. Connect Linear, Granola, Slack, etc. if needed
3. Run `/pm-skills:my-status` in Claude Code or `$pm-skills my-status` in Codex

## Skills

- `pm-skills:team-status` for shipped, in-progress, and risk updates
- `pm-skills:my-status` for personal progress, next steps, and risks
- `pm-skills:meeting-digest` for decisions and action items from meetings
- `pm-skills:slack-recap` for important Slack follow-ups
- `pm-skills:shape-product-pitch` for shaping product pitches using Shape Up methodology

## Works Across Tools

- Claude Code setup places symlinks in `~/.claude`
- Codex installs under `~/.codex/skills/pm-skills`
- Only `pm-skills`-namespaced files and symlinks are created

## Useful Commands

- Refresh just your profile: `script/setup --profile-only`
- Remove installed wrappers: `script/uninstall`
