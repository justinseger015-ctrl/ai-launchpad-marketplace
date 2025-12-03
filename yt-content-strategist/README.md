# YouTube Content Strategist

This plugin contains a suite of skills, agents, and tools for researching, ideating, and planning YouTube videos. The skills are designed to work together to create a cohesive workflow for optimizing YouTube content performance.

## Requirements

**[NOTE]** You must already have uv installed and the AI Launchpad marketplace added, see [main README](../README.md) if you haven't already.

1. **YouTube Data API Key**: You need a YouTube Data API key to access the YouTube Analytics tools. Instructions [here](https://developers.google.com/youtube/v3/getting-started).
2. **GEMINI API KEY**: You need a Gemini API key to use the NanoBanana image generation model. Instructions [here](https://aistudio.google.com/app/api-keys).

### Thumbkit

This plugin also uses Thumbkit, a CLI tool for generating and editing YouTube thumbnails with the Gemini 2.5 Flash (NanoBanana) image generation model.

The `yt-content-strategist` plugin will automatically install Thumbkit for you if it's missing. To learn more about Thumbkit or install manually yourself, see [here](https://github.com/kenneth-liao/thumbkit).

## Getting Started

Once you have completed the requirements above, you are ready to install the plugin.

1. Navigate to your user level .claude directory.

```bash
cd ~/.claude
```

2. Create an `.env` file in `~/.claude` and add the following keys that you created above:

```bash
YOUTUBE_API_KEY=your_youtube_api_key
GEMINI_API_KEY=your_gemini_api_key
```

3. Navigate to any project directory and start Claude Code.

```bash
claude
```

3. Install the plugin

```bash
/plugin install yt-content-strategist@ai-launchpad-marketplace
```

You can also do this interactively by running `/plugin`.

4. Restart Claude Code for the changes to take effect.

You should now be able to run the skills and tools in this plugin. You can use the `/plugin` command to see the installed plugin and its skills, or run `/context` to see the new MCP tools that have been installed by the plugin.

## Plugin Structure

```
yt-content-strategist/
├── .claude-plugin/
│   └── plugin.json          # Plugin metadata
├── README.md                 # Plugin documentation
├── skills/                   # Claude Code skills
│   ├── youtube-plan-new-video
│   └── youtube-research-video-topic
│   └── youtube-thumbnail
│   └── youtube-title
│   └── youtube-video-hook
├── agents/                   # Agent definitions
│   ├── youtube-researcher
│   └── thumbnail-reviewer
└── servers/                  # MCP servers
    └── py-mcp-youtube-toolbox
```