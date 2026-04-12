"""Interactive CLI chat (bonus for 1.1) with short-term memory.

This script provides a small terminal chat interface connected to a model
deployment in Azure AI Foundry. It keeps a bounded in-memory conversation
history so the assistant can use recent context without growing indefinitely.

Environment variables (.env):
    FOUNDRY_ENDPOINT
    FOUNDRY_API_KEY
    MODEL_DEPLOYMENT

Usage:
    python 01-ai-foundry-basics/cli_chat_tool.py

Commands:
    /exit     Quit the chat
    /reset    Clear short-term memory
    /history  Print current in-memory conversation
"""

from __future__ import annotations

import os
from collections import deque
from typing import Deque

from dotenv import load_dotenv
from openai import OpenAI


DEFAULT_MEMORY_TURNS = 4
SYSTEM_PROMPT = (
    "You are a helpful and concise assistant. Keep answers practical and short "
    "unless the user asks for detail."
)


def _build_client() -> tuple[OpenAI, str]:
    """Build and return an OpenAI client configured for Foundry project endpoints.

    Returns:
        tuple[OpenAI, str]:
            - OpenAI client configured with `.../openai/v1` base URL
            - Deployment name from MODEL_DEPLOYMENT

    Raises:
        ValueError: If any required environment variable is missing.
    """
    load_dotenv(override=True)

    endpoint = os.getenv("FOUNDRY_ENDPOINT", "").strip()
    api_key = os.getenv("FOUNDRY_API_KEY", "").strip()
    deployment = os.getenv("MODEL_DEPLOYMENT", "").strip()

    missing = [
        name
        for name, value in [
            ("FOUNDRY_ENDPOINT", endpoint),
            ("FOUNDRY_API_KEY", api_key),
            ("MODEL_DEPLOYMENT", deployment),
        ]
        if not value
    ]

    if missing:
        raise ValueError(
            "Missing required environment variables: "
            + ", ".join(missing)
            + ". Fill them in .env and try again."
        )

    base_url = endpoint.rstrip("/") + "/openai/v1"
    client = OpenAI(base_url=base_url, api_key=api_key)
    return client, deployment


def _format_history(history: Deque[dict[str, str]]) -> str:
    """Convert the in-memory chat history into a readable multiline string."""
    if not history:
        return "(history is empty)"

    lines: list[str] = []
    for idx, message in enumerate(history, start=1):
        role = message["role"].upper()
        content = message["content"]
        lines.append(f"{idx:02d}. {role}: {content}")
    return "\n".join(lines)


def run_cli_chat(memory_turns: int = 4) -> None:
    """Run an interactive terminal chat with bounded short-term memory.

    Args:
        memory_turns: Number of user+assistant turn pairs kept in memory.
    """
    client, deployment = _build_client()

    # Each turn has 2 messages (user + assistant).
    max_messages = max(2, memory_turns * 2)
    history: Deque[dict[str, str]] = deque(maxlen=max_messages)

    print("Interactive CLI Chat")
    print(f"Deployment: {deployment}")
    print(f"Short-term memory window: {memory_turns} turns")
    print("Type /exit to quit, /reset to clear memory, /history to inspect memory.\n")

    while True:
        try:
            user_text = input("You: ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\nExiting chat.")
            break

        if not user_text:
            continue

        if user_text.lower() in {"/exit", "exit", "quit"}:
            print("Exiting chat.")
            break

        if user_text.lower() == "/reset":
            history.clear()
            print("Memory cleared.")
            continue

        if user_text.lower() == "/history":
            print(_format_history(history))
            continue

        # Build message list from fixed system instruction + short-term memory.
        messages = [{"role": "system", "content": SYSTEM_PROMPT}, *history]
        messages.append({"role": "user", "content": user_text})

        try:
            response = client.chat.completions.create(
                model=deployment,
                messages=messages,
                temperature=0.3,
                max_tokens=300,
            )
            assistant_text = response.choices[0].message.content or ""
        except Exception as exc:
            print(f"Assistant: [error] {type(exc).__name__}: {exc}")
            continue

        print(f"Assistant: {assistant_text}")

        # Persist current exchange in bounded memory for the next turns.
        history.append({"role": "user", "content": user_text})
        history.append({"role": "assistant", "content": assistant_text})


if __name__ == "__main__":
    run_cli_chat(memory_turns=DEFAULT_MEMORY_TURNS)
