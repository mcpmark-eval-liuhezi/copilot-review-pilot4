#!/usr/bin/env python3
"""Example demo script for the Copilot code review pilot."""


def greet(name: str) -> str:
    """Return a friendly greeting for the given name."""
    if not name:
        raise ValueError("name must not be empty")
    return f"Hello, {name}! Welcome to the Copilot review pilot."


def main() -> None:
    print(greet("HeziLiu"))


if __name__ == "__main__":
    main()
