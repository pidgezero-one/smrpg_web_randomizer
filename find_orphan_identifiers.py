#!/usr/bin/env python3
"""
Script to find orphan identifiers in battle animation scripts.

Finds all identifier="..." strings that are NOT referenced in any destinations list.
"""

import re
import os
from pathlib import Path
from collections import defaultdict

# Directories to scan
DIRECTORIES = [
    "randomizer/data/battle_animation/02/contents",
    "randomizer/data/battle_animation/35/contents",
    "randomizer/data/battle_animation/3A/contents",
]

def extract_identifiers(content: str) -> list[tuple[str, int]]:
    """Extract all identifier="..." values with line numbers."""
    identifiers = []
    for i, line in enumerate(content.split('\n'), 1):
        # Match identifier="..."
        matches = re.findall(r'identifier\s*=\s*["\']([^"\']+)["\']', line)
        for match in matches:
            identifiers.append((match, i))
    return identifiers

def is_valid_identifier(s: str) -> bool:
    """Check if a string looks like a valid destination identifier.

    Real identifiers in this codebase contain underscores (e.g., command_0x3A6000).
    Single letters or short strings without underscores are likely from other arrays.
    """
    if not re.match(r'^[a-zA-Z_][a-zA-Z0-9_]*$', s):
        return False
    # Must contain an underscore (all real identifiers have underscores)
    return '_' in s

def extract_destinations(content: str) -> set[str]:
    """Extract all destination references from the content."""
    destinations = set()

    # Match explicit destinations=["...", "..."]
    dest_pattern = r'destinations\s*=\s*\[([^\]]+)\]'
    for match in re.finditer(dest_pattern, content):
        # Extract strings from the list
        strings = re.findall(r'["\']([^"\']+)["\']', match.group(1))
        for s in strings:
            if is_valid_identifier(s):
                destinations.add(s)

    # Match implicit destinations - string arrays that are arguments to commands
    # These are typically the last (or only) list argument in commands like:
    # Jmp(["..."]), RunSubroutine(["..."]), DefineObjectQueue(["..."], identifier="...")
    # JmpIf...(value, ["..."])

    # Pattern to find string arrays in function calls
    # We look for patterns like: CommandName(... ["string1", "string2"] ...)
    array_pattern = r'\[([^\[\]]*?["\'][^"\']+["\'][^\[\]]*?)\]'
    for match in re.finditer(array_pattern, content):
        inner = match.group(1)
        # Only consider arrays that contain strings (not numbers, etc.)
        strings = re.findall(r'["\']([^"\']+)["\']', inner)
        for s in strings:
            if is_valid_identifier(s):
                destinations.add(s)

    return destinations

def main():
    # Collect all identifiers and destinations
    all_identifiers: dict[str, list[tuple[str, int]]] = defaultdict(list)  # identifier -> [(file, line)]
    all_destinations: set[str] = set()

    for directory in DIRECTORIES:
        dir_path = Path(directory)
        if not dir_path.exists():
            print(f"Warning: Directory not found: {directory}")
            continue

        for file_path in dir_path.glob("*.py"):
            if file_path.name == "__init__.py":
                continue

            content = file_path.read_text()

            # Extract identifiers
            for identifier, line_num in extract_identifiers(content):
                all_identifiers[identifier].append((str(file_path), line_num))

            # Extract destinations
            destinations = extract_destinations(content)
            all_destinations.update(destinations)

    # Find orphan identifiers (identifiers not in any destinations)
    orphan_identifiers = set(all_identifiers.keys()) - all_destinations

    # Sort and display results
    print(f"Total unique identifiers: {len(all_identifiers)}")
    print(f"Total unique destination references: {len(all_destinations)}")
    print(f"Orphan identifiers (not referenced by any destinations): {len(orphan_identifiers)}")
    print()

    if orphan_identifiers:
        print("=" * 80)
        print("ORPHAN IDENTIFIERS (identifier not in any destinations):")
        print("=" * 80)
        for identifier in sorted(orphan_identifiers):
            locations = all_identifiers[identifier]
            for file_path, line_num in locations:
                print(f"  {identifier}")
                print(f"    -> {file_path}:{line_num}")
        print()

    # Also show identifiers that ARE referenced (for verification)
    referenced = set(all_identifiers.keys()) & all_destinations
    print(f"\nReferenced identifiers (for verification): {len(referenced)}")

    # Show destinations that don't have a matching identifier (potential dangling references)
    dangling_destinations = all_destinations - set(all_identifiers.keys())
    # Filter to only valid-looking identifiers
    dangling_destinations = {d for d in dangling_destinations if is_valid_identifier(d)}
    if dangling_destinations:
        print()
        print("=" * 80)
        print("DANGLING DESTINATIONS (destinations pointing to non-existent identifiers):")
        print("=" * 80)
        for dest in sorted(dangling_destinations):
            print(f"  {dest}")

if __name__ == "__main__":
    main()
