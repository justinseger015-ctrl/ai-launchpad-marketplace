# YouTube Content Strategist

This plugin contains a suite of skills and tools for researching, ideating, and planning YouTube videos. The skills are designed to work together to create a cohesive workflow for optimizing YouTube content performance.

## Requirements

1. **uv**: This plugin requires [uv](https://docs.astral.sh/uv/) to manage MCP servers. Installation instructions are [here](https://docs.astral.sh/uv/getting-started/installation/).
2. **YouTube Data API Key**: You need a YouTube Data API key to access the YouTube Analytics tools. You can create a key by following the instructions [here](https://developers.google.com/youtube/v3/getting-started).
3. **GEMINI API KEY**: You need a Gemini API key to use the NanoBanana image generation model. You can create a key by following the instructions [here](https://aistudio.google.com/app/api-keys).
4. **Thumbkit**: This plugin uses Thumbkit, a CLI tool for generating and editing high-performing YouTube thumbnails. Thumbkit is built on top of Gemini 2.5 Flash (NanoBanana) image generation model. 

You can install it as a global uv tool by running the following command:

```bash
uv tool install git+https://github.com/kenneth-liao/thumbkit.git
```

This makes thumbkit globally available on your system so you can run it from anywhere. To verify it's working, run `thubmkit` from the command line. You should see the help menu.

For detailed instructions, see [here](https://github.com/kenneth-liao/thumbkit).

## Getting Started

Once you have completed the requirements above, you are ready to install the plugin.

1. Create a new project folder or navigate to the folder where you want to use the plugin.
2. Create an `.env` file in the root of your project folder and add the following keys that you created above:

```bash
YOUTUBE_API_KEY=your_youtube_api_key
GEMINI_API_KEY=your_gemini_api_key
```

3. Open Claude Code in your project folder.
3. Run the command to add the ai-launchpad-marketplace

```bash
/plugin marketplace add https://gitlab.com/company/plugins.git
```

4. Install the plugin

```bash
/plugin install yt-content-strategist@ai-launchpad-marketplace
```

You can also do this interactively by running `/plugin`.

5. Restart Claude Code for the changes to take effect.

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