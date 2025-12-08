---
name: Workflows
description: Standard operating procedures learned from past sessions
update_policy: Update when workflow learned/changed - no permission needed
---

## YouTube Video Creation

1. Research with `youtube-research-video-topic` skill
2. Plan with `youtube-plan-new-video` skill
3. Generate thumbnails with thumbkit CLI
   - Headshots: `/Users/kennethliao/projects/youtube/assets/kenny_headshots/`
   - Command: `thumbkit generate --prompt "..." --ref <headshot> --out-dir <dir> --model pro`
   - Multiple --ref parameters supported (e.g., headshot + logo)
4. Episode files: `/Users/kennethliao/projects/youtube/episode_files/[N]_[topic]/`
   - Structure: `0_idea.md`, `1_research.md`, `2_plan.md`, `3_script.md`, `4_publish.md`
   - Subdirs: `thumbnails/`, `assets/`, `videos/`, `research/`

### Asset Locations

- Headshots: `/Users/kennethliao/projects/youtube/assets/kenny_headshots/`
- Logos: `/Users/kennethliao/projects/youtube/assets/icons_logos/`
- Templates: `/Users/kennethliao/projects/youtube/assets/thumbnail_templates/`

### Thumbnail Research

- Download competitor thumbnails using curl to analyze proven designs
- Analyze related, high-performing videos for patterns

## Code Research

- Use codebase-retrieval for finding code patterns
- Use git-commit-retrieval for understanding why changes were made

## Research & Analysis

- Use structured skill files for complex research (business-competitor-analysis, etc.)
- Create deliverable reports in project docs/ directories
- Reference deliverables in context, don't store full findings
