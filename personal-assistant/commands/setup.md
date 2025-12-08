---
description: Set up the personal assistant plugin. Run this once after installing the plugin.
---

# Personal Assistant Setup

Set up the personal assistant plugin with context system and default Claude Code settings.

## Step 1: Set Default Settings

Update Claude's settings to use the personal assistant output style, display the output style in the status line, and enable the personal-assistant plugin.

You **MUST** first read the current settings:

```bash
cat ~/.claude/settings.json
```

Then update the following fields. If the file doesn't exist or is empty, create it with this content (you **MUST** preserve other settings):

```json
{
  "outputStyle": "personal-assistant:Personal Assistant",
  "statusLine": {
    "type": "command",
    "command": "cat | jq -r '.output_style.name'"
  },
  "enabledPlugins": {
    "personal-assistant@ai-launchpad": true
  },
}
```

If the file exists, merge the fields above into the existing settings.

<REQUIRED>
You **MUST** preserve other settings in the `settings.json` file. Only update/add the fields specified above.
</REQUIRED>

## Step 2: Initialize Context System

### ⚠️ First, check if context already exists

```bash
ls ~/.claude/.context/
```

- **If the directory exists**: Context is already set up. Do NOT overwrite it or you'll lose saved context. **CRITICAL: Do NOT proceed with the copy if the directory already exists!**
- **If the directory doesn't exist**: Proceed with setup below.

### Fresh Install (only if directory doesn't exist)

Copy the template directory to `~/.claude/.context/`:

```bash
cp -r ~/.claude/plugins/marketplaces/ai-launchpad/personal-assistant/context-template/ ~/.claude/.context/
```

### Verify Setup

```bash
ls ~/.claude/.context/
```

You should see: `CLAUDE.md`, `context-update.md`, `core/`, `session/`, `projects/`

## What Gets Created

```
~/.claude/.context/
├── CLAUDE.md              # Main instructions (loaded on every message)
├── context-update.md      # Update instructions (Stop hook)
├── core/                  # Your enduring context
│   ├── identity.md        # Who you are
│   ├── preferences.md     # How you work
│   ├── workflows.md       # Your standard procedures
│   └── rules.md           # Learned rules from corrections
├── session/
│   └── current.md         # Current session context
└── projects/
    └── project_index.md   # Your project index
```

## Why External Storage?

Your context is stored **outside** the plugin directory so that:
- Plugin updates don't overwrite your personalized context
- Your context persists across plugin reinstalls
- You own your data

## After Setup

Once initialized:
- Context is loaded on every user message
- Context updates are prompted after each response

<REQUIRED>
The output style is not active until the user restarts Claude Code. Prompt the user to restart Claude Code now to activate the output style. Otherwise, if they decide to continue, the context system will work correctly but the output style will not be active.
</REQUIRED>
