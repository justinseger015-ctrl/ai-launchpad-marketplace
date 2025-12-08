#!/usr/bin/env python3
"""
Stop hook to trigger memory updates after each Claude response.
Blocks Claude from stopping until it updates the memory/context systems.
"""

import json
import sys
from pathlib import Path


def get_hook_root() -> Path:
    """
    Get the root directory for the hook's context system.
    Uses the hook file's location to find the sibling 'context' folder.
    """
    hook_dir = Path(__file__).resolve().parent  # hooks/
    hook_root = hook_dir.parent  # personal-assistant/ (or whatever it's named)
    return hook_root


def get_context_update_instructions(hook_root: Path) -> str:
    """Generate context update instructions with correct paths."""
    context_dir = hook_root / "context"

    return f"""Before finishing, update the context system:

If you haven't already, read `{context_dir}/context-update.md` to understand the requirements for a context update.

If a context update is necessary, complete the update according to the instructions in `{context_dir}/context-update.md`.

After completing the context update or if no update is necessary, you may finish your response."""


def main() -> None:
    # Read hook input from stdin
    try:
        hook_input = json.load(sys.stdin)
    except json.JSONDecodeError as e:
        print(f"Error: Invalid JSON input: {e}", file=sys.stderr)
        sys.exit(1)

    # Check if Claude is already continuing due to this hook
    stop_hook_active = hook_input.get("stop_hook_active", False)

    if stop_hook_active:
        # Let Claude stop - context update already happened this turn
        sys.exit(0)

    # Block Claude and instruct it to update context
    hook_root = get_hook_root()
    output = {
        "decision": "block",
        "reason": get_context_update_instructions(hook_root)
    }
    print(json.dumps(output))
    sys.exit(0)


if __name__ == "__main__":
    main()

