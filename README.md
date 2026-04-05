# PM Skills for your AI tools

Opinionated product management skills for Claude Code and Codex.

## Why PM Skills

- Reuse the same PM skills across Claude Code and Codex
- Avoid rebuilding prompts for routine PM work
- Get from setup to a usable output quickly

## Quick Start

1. Run `script/setup`
2. Connect the tools you use if needed, such as Linear, Granola, or Slack
3. Run `/pm-skills:my-status` in Claude Code or `$pm-skills my-status` in Codex

## Included Skills

- `my-status`: draft your weekly update or 1:1 prep from current work
- `team-status`: summarize shipped, in-progress, and risk items for a team
- `meeting-digest`: pull decisions and action items from meetings
- `slack-recap`: catch up on important Slack threads that need attention
- `shape-product-pitch`: turn a rough idea into a Shape Up style pitch
- `make-decision`: interview the PM and draft a decision doc with a traffic-light comparison table

<p align="center">
  <img width="1000" alt="PM Tools Overview" src="https://github.com/user-attachments/assets/d6cfc988-1056-4a23-962a-90e5c31852a0" />
</p>

## Tool Support

- Claude Code installs command wrappers under `~/.claude/commands`
- Codex installs skills under `~/.codex/skills/pm-skills`
- Only `pm-skills`-namespaced files and symlinks are managed

## Useful Commands

- Refresh just your profile: `script/setup --profile-only`
- Remove installed wrappers: `script/uninstall`

Upgrading from an older install? Run `script/setup` and it will offer to clean up legacy configuration if needed.
