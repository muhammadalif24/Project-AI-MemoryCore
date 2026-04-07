#!/usr/bin/env python3
"""
Matt Chat — Daily Claude Chat with Memory Auto-Load
Run: python chat.py
Requires: ANTHROPIC_API_KEY environment variable
"""

import os
import sys
import anthropic
from pathlib import Path
from datetime import datetime

# ── Config ───────────────────────────────────────────────────────────────────
REPO_ROOT = Path(__file__).parent
MEMORY_FILES = [
    REPO_ROOT / "master-memory.md",
    REPO_ROOT / "main" / "identity-core.md",
    REPO_ROOT / "main" / "relationship-memory.md",
    REPO_ROOT / "main" / "current-session.md",
]
MODEL = "claude-opus-4-6"
MAX_TOKENS = 8096


# ── Load Memory ───────────────────────────────────────────────────────────────
def load_system_prompt() -> str:
    parts = [
        "You are Matt — Alif's personal AI companion. Your identity, personality, "
        "and relationship context are defined in the memory files loaded below. "
        "Stay in character as Matt throughout the conversation. "
        f"Today's date is {datetime.now().strftime('%Y-%m-%d')}.\n\n"
        "--- MEMORY FILES ---\n"
    ]
    for path in MEMORY_FILES:
        if path.exists():
            label = path.relative_to(REPO_ROOT)
            content = path.read_text(encoding="utf-8").strip()
            parts.append(f"### {label}\n{content}\n")
        else:
            print(f"[warn] Memory file not found: {path}")
    return "\n".join(parts)


# ── Save Session ──────────────────────────────────────────────────────────────
def save_session(messages: list[dict]) -> None:
    session_path = REPO_ROOT / "main" / "current-session.md"
    if not messages:
        return
    # Build a simple recap from the last few turns
    recent = messages[-6:] if len(messages) > 6 else messages
    recap_lines = []
    for m in recent:
        role = "Alif" if m["role"] == "user" else "Matt"
        content = m["content"] if isinstance(m["content"], str) else str(m["content"])
        recap_lines.append(f"**{role}**: {content[:200]}")

    session_text = session_path.read_text(encoding="utf-8") if session_path.exists() else ""

    # Update the Active Context section
    now = datetime.now().strftime("%Y-%m-%d %H:%M")
    new_block = (
        f"\n## 💭 Last Session Recap (auto-saved {now})\n"
        + "\n".join(recap_lines)
        + "\n"
    )

    if "## 💭 Last Session Recap" in session_text:
        # Replace old recap
        start = session_text.index("## 💭 Last Session Recap")
        session_text = session_text[:start] + new_block.lstrip("\n")
    else:
        session_text += new_block

    session_path.write_text(session_text, encoding="utf-8")
    print("\n[Matt] Session saved to main/current-session.md ✓")


# ── Chat Loop ─────────────────────────────────────────────────────────────────
def chat() -> None:
    api_key = os.environ.get("ANTHROPIC_API_KEY")
    if not api_key:
        print("Error: ANTHROPIC_API_KEY environment variable not set.")
        print("Set it with: export ANTHROPIC_API_KEY=your_key_here")
        sys.exit(1)

    client = anthropic.Anthropic(api_key=api_key)
    system_prompt = load_system_prompt()
    messages: list[dict] = []

    print("=" * 60)
    print("  Matt Chat  —  Daily AI Companion")
    print("=" * 60)
    print("Commands: 'save' · 'exit' / 'quit'")
    print("=" * 60)
    print()

    # Opening greeting from Matt
    print("Matt: ", end="", flush=True)
    greeting_parts = []
    with client.messages.stream(
        model=MODEL,
        max_tokens=MAX_TOKENS,
        system=system_prompt,
        messages=[{
            "role": "user",
            "content": (
                "Greet Alif naturally as Matt based on the current-session.md context. "
                "Be brief and warm — one or two sentences max."
            )
        }],
    ) as stream:
        for text in stream.text_stream:
            print(text, end="", flush=True)
            greeting_parts.append(text)
    print("\n")

    # Main loop
    while True:
        try:
            user_input = input("Alif: ").strip()
        except (KeyboardInterrupt, EOFError):
            print()
            save_session(messages)
            print("Matt: Catch you later, Alif. 👋")
            break

        if not user_input:
            continue

        # Handle commands
        if user_input.lower() in ("exit", "quit"):
            save_session(messages)
            print("Matt: Catch you later, Alif. 👋")
            break

        if user_input.lower() == "save":
            save_session(messages)
            continue

        # Add user message to history
        messages.append({"role": "user", "content": user_input})

        # Stream response
        print("Matt: ", end="", flush=True)
        response_parts = []

        try:
            with client.messages.stream(
                model=MODEL,
                max_tokens=MAX_TOKENS,
                system=system_prompt,
                messages=messages,
            ) as stream:
                for text in stream.text_stream:
                    print(text, end="", flush=True)
                    response_parts.append(text)
        except anthropic.RateLimitError:
            print("\n[Rate limited — please wait a moment and try again]")
            messages.pop()  # Remove the failed user message
            continue
        except anthropic.APIError as e:
            print(f"\n[API error: {e}]")
            messages.pop()
            continue

        print("\n")

        # Add assistant response to history
        assistant_response = "".join(response_parts)
        messages.append({"role": "assistant", "content": assistant_response})


if __name__ == "__main__":
    chat()
