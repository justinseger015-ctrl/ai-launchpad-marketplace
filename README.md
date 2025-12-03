# AI Launchpad Marketplace

The AI Launchpad marketplace is a curated collection of Claude Code plugins to unlock your personal workflows.

## 🚀 Quick Start

You must first add the marketplace to your Claude Code, then you can choose what plugins to install. 

Marketplaces and plugins are installed globally, in your user-level Claude Code (`~/.claude`). This just means that any plugins you install will be available in all projects: anywhere on your system that you start Claude Code.

### Requirements

This marketplace requires [uv](https://docs.astral.sh/uv/) to manage MCP servers and CLI tools. Complete the installation instructions [here](https://docs.astral.sh/uv/getting-started/installation/) before proceeding!

**[NOTE]** Individual plugins may have additional requirements! Please refer to the plugin's README for more information.

### Installation

1. Start Claude Code anywhere.

```bash
claude
```

2. Add the AI Launchpad marketplace to Claude Code.

```bash
/plugin marketplace add https://github.com/kenneth-liao/ai-launchpad-marketplace.git
```

You can now browse available plugins interactively by running `/plugin`.

## 📦 Available Plugins

**[NOTE]** Individual plugins may have additional requirements! Please refer to the plugin's README for more information.

### Personal Assistant

Turn Claude Code into your personal assistant with this plugin.

**REQUIREMENTS:**
No additional requirements.

**Features:**
- Personalized context system
- Memory management
- Task tracking
- Notification sounds

**[View Plugin →](./personal-assistant)**

### YouTube Content Strategist

A comprehensive plugin for researching, ideating, and planning YouTube videos with AI assistance.

**REQUIREMENTS:**
This plugin has 2 requirements! Please refer to the plugin's [README](./yt-content-strategist/README.md) for more information.

**Features:**
- Video topic research with competitive analysis
- Title generation with proven formulas
- Thumbnail concept creation and review
- Video planning and hook development
- YouTube Analytics integration via MCP server

**[View Plugin →](./yt-content-strategist)**

---

## 👤 Author

**Kenny Liao (The AI Launchpad)**
- YouTube: [@KennethLiao](https://www.youtube.com/@KennethLiao)
- GitHub: [@kenneth-liao](https://github.com/kenneth-liao)

## 🔗 Related Projects

- [AI Launchpad](https://github.com/kenneth-liao/ai-launchpad) - The main AI development framework
- [Thumbkit](https://github.com/kenneth-liao/thumbkit) - CLI tool for YouTube thumbnail generation

---

Made with ❤️ for the Claude Code community
