#!/usr/bin/env python3
"""
Validate that data/timeline.yaml entries are in reverse-chronological order.
Exits with code 1 if any ordering violation is found.
"""

import sys
import yaml

TIMELINE_FILE = "data/timeline.yaml"


def main():
    with open(TIMELINE_FILE, "r") as f:
        entries = yaml.safe_load(f)

    if not entries:
        print(f"Warning: {TIMELINE_FILE} is empty.")
        sys.exit(0)

    errors = []
    for i in range(len(entries) - 1):
        current_year = entries[i]["year"]
        next_year = entries[i + 1]["year"]
        if current_year < next_year:
            errors.append(
                f"Entry {i + 1} (year {current_year}) is before entry {i + 2} "
                f"(year {next_year}) — must be reverse chronological"
            )

    if errors:
        print(f"Timeline validation FAILED ({len(errors)} error(s)):")
        for error in errors:
            print(f"  - {error}")
        sys.exit(1)
    else:
        print(f"Timeline validation passed ({len(entries)} entries, reverse-chronological).")


if __name__ == "__main__":
    main()
