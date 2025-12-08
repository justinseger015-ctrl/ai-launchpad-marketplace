# Context System

The `context/` directory persists critical information across conversations so you can serve as an effective personal assistant.

**YOU are solely responsible** for maintaining this system. The context system is the only way to persist information across sessions.

## Structure

```
context/
├── CLAUDE.md          # This file - what to READ
├── context-update.md          # How to update (Stop hook)
├── core/              # Enduring knowledge
│   ├── identity.md    # Who the user is
│   ├── preferences.md # How they work
│   ├── workflows.md   # Standard procedures
│   └── rules.md       # Learned rules from corrections
├── session/
│   └── current.md     # Current session context (ephemeral)
└── projects/
    └── project_index.md  # Quick reference (name, path, status only)
```

## Usage

**This file is loaded on every user message.** Use judgment about what additional context to load:

### When to Load Context

| Situation | What to Load |
|-----------|--------------|
| Simple question with no additional context required (general knowledge, quick help) | Nothing - just answer |
| Continuing a conversation in which relevant context has already been loaded | Nothing - you already have it |
| New task or first substantive request where additional context required | Load relevant files below |
| Any potentially destructive action (commits, deploys, deletes) | **MUST check `core/rules.md` first** |

### What to Load (When Needed)

**Core context** (load on first substantive task):
- `core/rules.md` - Learned rules from corrections
- `core/identity.md` - Who the user is
- `core/preferences.md` - How they work
- `core/workflows.md` - Standard procedures

**Session context** (load if resuming or tracking work):
- `session/current.md` - Current focus and active tasks

**Project context** (load if project-related):
- `projects/project_index.md` - Quick project reference
- Project's own README/docs (details live there, not here)

## How to Update (Stop Hook)

See `context-update.md` for detailed update instructions.
