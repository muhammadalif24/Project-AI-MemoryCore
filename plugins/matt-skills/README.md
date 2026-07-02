# matt-skills Plugin
*Auto-triggered skill plugin for Matt — Alif's AI companion*

## Overview
This plugin provides auto-triggered skills that activate based on conversation context in Claude Code. Skills are plain markdown files — no build steps, no configuration.

## Structure
```
matt-skills/
├── .claude-plugin/
│   └── plugin.json          # Plugin identity
├── skills/                  # Auto-triggered behaviors
│   └── save-memory/
│       └── SKILL.md
├── commands/                # Slash commands (optional)
├── skill-format.md          # Template for creating new skills
└── README.md
```

## Adding New Skills
1. Create a folder: `skills/[skill-name]/`
2. Create `SKILL.md` inside with YAML frontmatter + protocol
3. Done — auto-discovered by Claude Code

## Active Skills
| Skill | Trigger | Purpose |
|---|---|---|
| save-memory | "save", "save memory", "update memory" | Preserve context to memory files |
| save-diary | "save diary", "write diary", "document session" | Write structured session diary entry |
| check-reminders | Session start, "remind me", "check reminders" | Manage persistent cross-session reminders |
| log-decision | "log decision", non-obvious choices detected | Append-only decision log with rationale |
| echo-recall | "do you remember", "recall", "when did we" | Search diary and narrate past sessions |

## How It Works

Skills are auto-discovered by Claude Code through the repo structure. No installation command needed — just reference them in CLAUDE.md and they're active:

```yaml
## Active Skills
The following skills are installed in `plugins/matt-skills/skills/`. Apply them automatically:
- **save-memory** → triggers on "save", "save memory", "update memory"
- **save-diary** → triggers on "save diary", "write diary", "document session"
- **check-reminders** → triggers at session start and on "remind me", "check reminders"
- **log-decision** → triggers on non-obvious decisions, "log decision", "why did we choose"
- **echo-recall** → triggers on "do you remember", "recall", "when did we", "check history"
```

**Works on**: Claude Code web + browser. No Windows CLI activation needed.
