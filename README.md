# AI Launchpad Marketplace

A curated collection of Claude Code plugins to unlock your personal workflow.

## 🚀 Quick Start

To use the plugins in this marketplace with Claude Code, you must first install the marketplace. You can then browse available plugins and install them directly from Claude Code.

### Installation

1. Run the command to add the ai-launchpad-marketplace to Claude Code.

```bash
/plugin marketplace add https://github.com/kenneth-liao/ai-launchpad-marketplace.git
```

You can then browse available plugins interactively by running `/plugin`.

## 📦 Available Plugins

**[NOTE]** Each plugin has its own set of requirements! Please refer to the plugin's README for more information.

### YouTube Content Strategist

A comprehensive plugin for researching, ideating, and planning YouTube videos with AI assistance.

**REQUIREMENTS:**
This plugin has 4 requirements! Please refer to the plugin's [README](./yt-content-strategist/README.md) for more information.

**Features:**
- Video topic research with competitive analysis
- Title generation with proven formulas
- Thumbnail concept creation and review
- Video planning and hook development
- YouTube Analytics integration via MCP server

**[View Plugin →](./yt-content-strategist)**

## 🛠️ Plugin Structure

Each plugin in this marketplace follows a consistent structure:

```
plugin-name/
├── .claude-plugin/
│   └── plugin.json          # Plugin metadata
├── README.md                 # Plugin documentation
├── skills/                   # Claude Code skills
├── agents/                   # Agent definitions (optional)
└── servers/                  # MCP servers (optional)
```

## 👤 Author

**Kenny Liao (The AI Launchpad)**
- YouTube: [@KennethLiao](https://www.youtube.com/@KennethLiao)
- GitHub: [@kenneth-liao](https://github.com/kenneth-liao)

## 🔗 Related Projects

- [AI Launchpad](https://github.com/kenneth-liao/ai-launchpad) - The main AI development framework
- [Thumbkit](https://github.com/kenneth-liao/thumbkit) - CLI tool for YouTube thumbnail generation

---

Made with ❤️ for the Claude Code community
