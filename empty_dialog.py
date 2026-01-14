#!/usr/bin/env python3
"""
Empty dialog(s) by ID and rename to DIXXXX_EMPTY.

Usage:
    python empty_dialog.py 803                    # Single dialog
    python empty_dialog.py DI0803_NO_ADVICE       # By name
    python empty_dialog.py 800-810                # Range (inclusive)
    python empty_dialog.py 800 801 802            # Multiple
    python empty_dialog.py 800-805 810 815-820   # Mixed
"""

import re
import sys
from pathlib import Path

BASE = Path('/Users/stefkischak/code/smrpg_web_randomizer')

def parse_dialog_ids(args: list[str]) -> list[int]:
    """Parse dialog IDs from arguments. Returns list of numbers."""
    result = []

    for arg in args:
        # Check if it's a range (e.g., 800-810)
        range_match = re.match(r'^(\d+)-(\d+)$', arg)
        if range_match:
            start = int(range_match.group(1))
            end = int(range_match.group(2))
            if start > end:
                start, end = end, start
            result.extend(range(start, end + 1))
            continue

        # Check if it's a named dialog (DI####_xxx)
        name_match = re.match(r'^DI(\d{4})_\w+$', arg)
        if name_match:
            result.append(int(name_match.group(1)))
            continue

        # Otherwise treat as number
        try:
            result.append(int(arg))
        except ValueError:
            print(f"Warning: Could not parse '{arg}' as a dialog ID, skipping")

    return sorted(set(result))  # Remove duplicates and sort

def get_current_dialog_name(num: int) -> str | None:
    """Look up the current name for a dialog number."""
    names_file = BASE / 'randomizer/data/variables/dialog_names.py'
    content = names_file.read_text()

    # Match DI####_xxx = num
    pattern = rf'^(DI{num:04d}_\w+)\s*=\s*{num}\s*$'
    match = re.search(pattern, content, re.MULTILINE)

    if match:
        return match.group(1)
    return None

def get_dialog_pointer_info(name: str) -> tuple[int, int] | None:
    """Get bank and index for a dialog name."""
    pointers_file = BASE / 'randomizer/data/dialogs/contents/dialog_pointers.py'
    content = pointers_file.read_text()

    pattern = rf'pointers\[{name}\]\s*=\s*Dialog\(bank=(0x\d+),\s*index=(\d+)'
    match = re.search(pattern, content)

    if match:
        bank = int(match.group(1), 16)
        index = int(match.group(2))
        return bank, index
    return None

def rename_in_file(filepath: Path, old_name: str, new_name: str) -> int:
    """Rename all occurrences of old_name to new_name in a file. Returns count."""
    try:
        content = filepath.read_text()
        # Use word boundary to avoid partial matches
        new_content, count = re.subn(rf'\b{old_name}\b', new_name, content)
        if count > 0:
            filepath.write_text(new_content)
        return count
    except Exception as e:
        print(f"  Error processing {filepath}: {e}")
        return 0

def empty_dialog_content(bank: int, index: int) -> bool:
    """Replace dialog content with [await]. Returns True if successful."""
    table_file = BASE / f'randomizer/data/dialogs/contents/dialog_table_0x{bank:02x}.py'

    if not table_file.exists():
        print(f"  Error: Dialog table file not found: {table_file}")
        return False

    content = table_file.read_text()

    # Match dialog_data[index] = '''...''' (multiline)
    pattern = rf"(dialog_data\[{index}\]\s*=\s*)'''.*?'''"
    replacement = rf"\g<1>'''[await]'''"

    new_content, count = re.subn(pattern, replacement, content, flags=re.DOTALL)

    if count > 0:
        table_file.write_text(new_content)
        return True
    else:
        print(f"  Warning: Could not find dialog_data[{index}] in {table_file}")
        return False

def process_dialog(num: int) -> tuple[bool, str]:
    """Process a single dialog. Returns (success, message)."""
    # Get current name
    current_name = get_current_dialog_name(num)
    if not current_name:
        return False, f"Could not find dialog #{num} in dialog_names.py"

    new_name = f"DI{num:04d}_EMPTY"

    # Check if already empty
    if current_name == new_name:
        return True, f"Already named {new_name}"

    # Get dialog pointer info
    pointer_info = get_dialog_pointer_info(current_name)
    if not pointer_info:
        return False, f"Could not find pointer info for {current_name}"

    bank, index = pointer_info

    # Rename in all Python files
    total_replacements = 0
    for py_file in (BASE / 'randomizer').rglob('*.py'):
        if '__pycache__' in str(py_file):
            continue
        count = rename_in_file(py_file, current_name, new_name)
        total_replacements += count

    # Empty dialog content
    if not empty_dialog_content(bank, index):
        return False, f"Failed to empty content for {current_name}"

    return True, f"{current_name} -> {new_name} ({total_replacements} replacements)"


def main():
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(1)

    dialog_ids = parse_dialog_ids(sys.argv[1:])

    if not dialog_ids:
        print("No valid dialog IDs provided.")
        sys.exit(1)

    print(f"Processing {len(dialog_ids)} dialog(s)...\n")

    success_count = 0
    fail_count = 0

    for num in dialog_ids:
        success, message = process_dialog(num)
        status = "✓" if success else "✗"
        print(f"  {status} #{num:04d}: {message}")

        if success:
            success_count += 1
        else:
            fail_count += 1

    print(f"\nDone! {success_count} succeeded, {fail_count} failed.")

if __name__ == '__main__':
    main()
