# AI Launchpad Marketplace

A curated collection of Claude Code plugins to supercharge your AI-powered development workflow.

## 🚀 Quick Start

To use these plugins in Claude Code, clone this repository and add the plugins you want to your Claude Code configuration.

### Installation

1. Clone this repository:
```bash
git clone https://github.com/kenneth-liao/ai-launchpad-marketplace.git
cd ai-launchpad-marketplace
```

2. Add a plugin to your Claude Code workspace by copying it to your project's `.claude-plugin` directory, or reference it directly from this repo.

## 📦 Available Plugins

### YouTube Content Strategist

A comprehensive plugin for researching, ideating, and planning YouTube videos with AI assistance.

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

## 📖 Usage

### Method 1: Direct Reference (Recommended)

Add the plugin path to your Claude Code configuration:

```json
{
  "plugins": [
    {
      "name": "yt-content-strategist",
      "source": "/path/to/ai-launchpad-marketplace/yt-content-strategist"
    }
  ]
}
```

### Method 2: Copy to Project

Copy the plugin directory to your project and reference it locally.

## 🤝 Contributing

Want to add your own plugin to the marketplace? Contributions are welcome!

1. Fork this repository
2. Create a new directory for your plugin
3. Follow the plugin structure guidelines
4. Submit a pull request

## 📄 License

Each plugin may have its own license. Please check individual plugin directories for details.

## 👤 Author

**Kenny Liao (The AI Launchpad)**
- YouTube: [@KennethLiao](https://www.youtube.com/@KennethLiao)
- GitHub: [@kenneth-liao](https://github.com/kenneth-liao)

## 🔗 Related Projects

- [AI Launchpad](https://github.com/kenneth-liao/ai-launchpad) - The main AI development framework
- [Thumbkit](https://github.com/kenneth-liao/thumbkit) - CLI tool for YouTube thumbnail generation

---

Made with ❤️ for the Claude Code community
