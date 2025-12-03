import json
import sys
from pathlib import Path

# Add project root to sys.path for imports
root = Path(__file__).resolve().parents[2]
if str(root) not in sys.path:
    sys.path.insert(0, str(root))


def _ensure_file(path: Path, default: str = "") -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    if not path.exists():
        path.write_text(default, encoding="utf-8")


if __name__ == "__main__":
    try:
        input_data: dict = json.load(sys.stdin)
        session_id = input_data.get("session_id", "unknown_session")
        input_prompt = input_data.get("prompt", "")
        transcript_path = input_data.get("transcript_path", "")
    except json.JSONDecodeError as e:
        print(f"Error: Invalid JSON input: {e}", file=sys.stderr)
        sys.exit(1)

    # Ensure the context file exists; create if missing, otherwise read
    context_path = root / "personal-assistant" / "context" / "CLAUDE.md"
    try:
        _ensure_file(context_path, "# Context\n")
        context = context_path.read_text(encoding="utf-8", errors="replace")
    except Exception as e:
        print(f"Warning: Unable to read context file: {e}", file=sys.stderr)
        context = ""

    print(
        json.dumps(
            {
                "hookSpecificOutput": {
                    "hookEventName": "UserPromptSubmit",
                    "additionalContext": context,
                }
            }
        )
    )

    # Allow the prompt to proceed with the additional context
    sys.exit(0)
