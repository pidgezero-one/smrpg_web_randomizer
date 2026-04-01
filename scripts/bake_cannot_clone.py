"""Bake cannot_clone from NPC definitions into room object constructors.

For every NPC object in every room file, resolves the NPC-level cannot_clone
value and sets it explicitly at the room object level. This ensures room
objects always have an explicit True/False, never None.

Usage:
    python scripts/bake_cannot_clone.py [--dry-run]
"""

import sys
import os
import re
import importlib
import glob

# Add project root to path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Set up Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'smrpg_web_randomizer.settings')
import django
django.setup()

from smrpgpatchbuilder.datatypes.levels.classes import Clone


def get_npc_cannot_clone_values(room_module):
    """Get the cannot_clone value for each NPC in a room from NPC definitions."""
    room = room_module.room
    if room is None:
        return []
    results = []  # list of (obj_index, npc_name, cannot_clone_value, is_clone, already_set)

    for i, obj in enumerate(room.objects):
        is_clone = isinstance(obj, Clone)
        npc = obj._npc

        # Check if room-level override is already set
        already_set = obj.cannot_clone is not None

        # Get the NPC-level default
        npc_cannot_clone = npc.cannot_clone

        results.append((i, npc_cannot_clone, is_clone, already_set))

    return results


def add_cannot_clone_to_file(filepath, results):
    """Add cannot_clone= to NPC constructors in a room file."""
    with open(filepath, 'r') as f:
        content = f.read()
        lines = content.split('\n')

    # Track which NPC objects we've found (by index comment pattern)
    changes = 0

    for obj_idx, cannot_clone_val, is_clone, already_set in results:
        if already_set:
            continue  # Skip if already explicitly set

        # Find the NPC constructor for this object index
        # Pattern: "BattlePackNPC( # N" or "RegularNPC( # N" or "ChestNPC( # N"
        # or "BattlePackClone( # N" or "RegularClone( # N" or "ChestClone( # N"
        # or "EffectsNpc( # N"
        comment_pattern = f"# {obj_idx}\n"
        # Also try without newline for end-of-line comments
        comment_pattern2 = f"# {obj_idx}$"

        # Find the line with the object index comment
        obj_line_idx = None
        for li, line in enumerate(lines):
            # Match "( # N" at the end of a line
            if re.search(rf'\(\s*#\s*{obj_idx}\s*$', line):
                obj_line_idx = li
                break

        if obj_line_idx is None:
            # Some objects might not have index comments
            continue

        # Find the closing paren of this constructor
        # Walk forward from obj_line_idx to find the matching closing )
        # We need to find the line that ends with ")," or ")" that closes this constructor
        paren_depth = 0
        close_line_idx = None
        for li in range(obj_line_idx, len(lines)):
            line = lines[li]
            paren_depth += line.count('(') - line.count(')')
            if paren_depth <= 0:
                close_line_idx = li
                break

        if close_line_idx is None:
            continue

        # Check if cannot_clone already appears between obj_line_idx and close_line_idx
        has_cannot_clone = False
        for li in range(obj_line_idx, close_line_idx + 1):
            if 'cannot_clone' in lines[li]:
                has_cannot_clone = True
                break

        if has_cannot_clone:
            continue

        # Insert cannot_clone before the closing paren
        close_line = lines[close_line_idx]
        # Determine indentation from the previous parameter line
        prev_line = lines[close_line_idx - 1] if close_line_idx > 0 else ""
        indent_match = re.match(r'^(\s+)', prev_line)
        indent = indent_match.group(1) if indent_match else '            '

        # Check if the closing line is just ")" or has the last param + ")"
        stripped = close_line.strip()
        val_str = str(cannot_clone_val)

        if stripped.endswith('),') or stripped == '),' or stripped == ')':
            # Closing paren is on its own line or end of last param
            # Check if last param is on close line
            if stripped in (')', '),'):
                # Closing paren on its own line - add cannot_clone before it
                new_line = f"{indent}cannot_clone={val_str},"
                # Remove trailing comma from previous line if it doesn't have one
                # Actually, the previous line should already have a trailing comma
                lines.insert(close_line_idx, new_line)
            else:
                # Last param and closing paren on same line like "byte7_upper2=3),"
                # Add comma to end of current last param, add new line, keep closing paren
                # Actually, need to split the closing paren
                paren_match = re.match(r'^(\s+)(.*?)(\),?\s*)$', close_line)
                if paren_match:
                    line_indent = paren_match.group(1)
                    last_param = paren_match.group(2)
                    closing = paren_match.group(3)
                    # Add comma to last param if not already there
                    if not last_param.rstrip().endswith(','):
                        last_param = last_param.rstrip() + ','
                    lines[close_line_idx] = f"{line_indent}{last_param}"
                    lines.insert(close_line_idx + 1, f"{indent}cannot_clone={val_str}{closing}")
                else:
                    # Fallback: just add before closing
                    lines[close_line_idx] = close_line.replace(')', f'cannot_clone={val_str})')
        else:
            continue  # Can't figure out format, skip

        changes += 1

    if changes > 0:
        with open(filepath, 'w') as f:
            f.write('\n'.join(lines))

    return changes


def main():
    dry_run = '--dry-run' in sys.argv

    room_files = sorted(glob.glob('randomizer/data/rooms/room_*.py'))
    total_changes = 0
    files_changed = 0

    for filepath in room_files:
        # Import the room module
        module_name = filepath.replace('/', '.').replace('.py', '')
        try:
            module = importlib.import_module(module_name)
        except Exception as e:
            print(f"ERROR importing {filepath}: {e}")
            continue

        results = get_npc_cannot_clone_values(module)

        if dry_run:
            needs_changes = sum(1 for _, _, _, already_set in results if not already_set)
            if needs_changes > 0:
                print(f"{filepath}: {needs_changes} NPCs need cannot_clone")
                for obj_idx, val, is_clone, already_set in results:
                    if not already_set:
                        kind = "Clone" if is_clone else "NPC"
                        print(f"  obj {obj_idx} ({kind}): cannot_clone={val}")
            total_changes += needs_changes
        else:
            changes = add_cannot_clone_to_file(filepath, results)
            if changes > 0:
                print(f"{filepath}: {changes} NPCs updated")
                files_changed += 1
            total_changes += changes

    if dry_run:
        print(f"\nDry run: {total_changes} NPCs across {len(room_files)} files need cannot_clone")
    else:
        print(f"\nDone: {total_changes} NPCs updated across {files_changed} files")


if __name__ == '__main__':
    main()
