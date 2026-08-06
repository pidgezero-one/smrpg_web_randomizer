"""
Compress dialog tables by removing unused [await] entries.

This script:
1. Finds all [await] entries only used by EMPTY/DUPLICATE dialogs
2. Points those dialogs to a shared [await] index (renaming EMPTY -> DUPLICATE)
3. Removes the unused [await] entries from dialog tables
4. Shifts all subsequent indexes down
5. Updates all pointers accordingly

Usage:
    manage.py compress_dialogs          # Dry run (show what would change)
    manage.py compress_dialogs --apply  # Actually make changes
"""

import re
from pathlib import Path
from collections import defaultdict

from django.conf import settings
from django.core.management.base import BaseCommand

BASE = Path(settings.BASE_DIR)
POINTERS_FILE = BASE / 'randomizer/data/dialogs/contents/dialog_pointers.py'
NAMES_FILE = BASE / 'randomizer/data/variables/dialog_names.py'


def is_empty_or_duplicate(name: str) -> bool:
    """Check if a dialog name indicates it's EMPTY or DUPLICATE."""
    return '_EMPTY' in name or '_DUPLICATE' in name


def parse_pointers() -> dict[str, tuple[int, int, int]]:
    """Parse dialog_pointers.py to get (bank, index, pos) for each dialog name."""
    content = POINTERS_FILE.read_text()

    # Match pointers[DI####_xxx] = Dialog(bank=0x##, index=###, pos=###)
    pattern = r'pointers\[(DI\d{4}_\w+)\]\s*=\s*Dialog\(bank=(0x\d+),\s*index=(\d+),\s*pos=(\d+)\)'

    result = {}
    for match in re.finditer(pattern, content):
        name = match.group(1)
        bank = int(match.group(2), 16)
        index = int(match.group(3))
        pos = int(match.group(4))
        result[name] = (bank, index, pos)

    return result


def build_index_to_dialogs(pointers: dict[str, tuple[int, int, int]]) -> dict[tuple[int, int], list[str]]:
    """Build mapping of (bank, index) -> list of dialog names."""
    result = defaultdict(list)
    for name, (bank, index, pos) in pointers.items():
        result[(bank, index)].append(name)
    return result


def parse_dialog_table(bank: int) -> dict[int, str]:
    """Parse a dialog table file to get content at each index."""
    table_file = BASE / f'randomizer/data/dialogs/contents/dialog_table_0x{bank:02x}.py'
    if not table_file.exists():
        return {}

    content = table_file.read_text()

    # Match dialog_data[index] = '''...''' (multiline)
    pattern = r"dialog_data\[(\d+)\]\s*=\s*'''(.*?)'''"

    result = {}
    for match in re.finditer(pattern, content, re.DOTALL):
        index = int(match.group(1))
        dialog_content = match.group(2)
        result[index] = dialog_content

    return result


def is_await_content(content: str) -> bool:
    """Check if content is just [await] (with optional whitespace)."""
    return content.strip() == '[await]'


def find_removable_indexes(
    bank: int,
    dialog_table: dict[int, str],
    index_to_dialogs: dict[tuple[int, int], list[str]]
) -> list[int]:
    """Find indexes that can be removed (only [await] used by EMPTY/DUPLICATE)."""
    removable = []

    for index, content in dialog_table.items():
        if not is_await_content(content):
            continue

        dialogs = index_to_dialogs.get((bank, index), [])
        if not dialogs:
            # No dialogs point here, can remove
            removable.append(index)
            continue

        # If ALL dialogs are EMPTY or DUPLICATE, this index can be removed
        if all(is_empty_or_duplicate(name) for name in dialogs):
            removable.append(index)

    return sorted(removable)


def find_shared_await_index(
    bank: int,
    dialog_table: dict[int, str],
    index_to_dialogs: dict[tuple[int, int], list[str]],
    removable_indexes: list[int]
) -> int | None:
    """Find an [await] index to use as the shared target (one that will remain)."""
    # First, look for an [await] used by at least one non-EMPTY/DUPLICATE dialog
    for index, content in sorted(dialog_table.items()):
        if not is_await_content(content):
            continue
        if index in removable_indexes:
            continue

        dialogs = index_to_dialogs.get((bank, index), [])
        if any(not is_empty_or_duplicate(name) for name in dialogs):
            return index

    # If no such index exists, keep the first removable one as shared
    if removable_indexes:
        return removable_indexes[0]

    return None


def compute_index_shift(removable_indexes: list[int], old_index: int, shared_index: int) -> int:
    """Compute the new index after shifting, accounting for removed indexes."""
    if old_index in removable_indexes and old_index != shared_index:
        # shared_index shifts too, so resolve where it lands rather than using it raw
        shift = sum(1 for ri in removable_indexes if ri < shared_index and ri != shared_index)
        return shared_index - shift

    # Normal case: shift down by count of removed indexes below this one
    removed_kept_as_shared = shared_index if shared_index in removable_indexes else None
    shift = sum(1 for ri in removable_indexes if ri < old_index and ri != removed_kept_as_shared)
    return old_index - shift


def update_pointers_file(
    bank: int,
    removable_indexes: list[int],
    shared_index: int,
    dry_run: bool = True
) -> list[str]:
    """Update dialog_pointers.py for the given bank. Returns list of changes."""
    content = POINTERS_FILE.read_text()
    changes = []

    # Keep shared_index (remove from removable if present)
    actual_removable = [i for i in removable_indexes if i != shared_index]

    # Pattern to match pointer lines for this bank
    pattern = rf'(pointers\[(DI\d{{4}}_\w+)\]\s*=\s*Dialog\(bank=0x{bank:02x},\s*index=)(\d+)(,\s*pos=\d+\))'

    def replace_pointer(match):
        prefix = match.group(1)
        name = match.group(2)
        old_index = int(match.group(3))
        suffix = match.group(4)

        if old_index in actual_removable:
            new_index = compute_index_shift(actual_removable, shared_index, shared_index)
            new_name = name

            if '_EMPTY' in name and not '_EMPTY_' in name:
                # Simple _EMPTY suffix
                new_name = name.replace('_EMPTY', '_DUPLICATE')
            elif '_EMPTY_' in name:
                # Has extra suffix like _EMPTY_2
                new_name = name.replace('_EMPTY_', '_DUPLICATE_')

            if new_name != name:
                changes.append(f"Rename {name} -> {new_name}")

            changes.append(f"  {name}: index {old_index} -> {new_index} (shared)")
            return f"pointers[{new_name}] = Dialog(bank=0x{bank:02x}, index={new_index}{suffix}"

        new_index = compute_index_shift(actual_removable, old_index, shared_index)

        if new_index != old_index:
            changes.append(f"  {name}: index {old_index} -> {new_index}")

        return f"{prefix}{new_index}{suffix}"

    new_content = re.sub(pattern, replace_pointer, content)

    if not dry_run and new_content != content:
        POINTERS_FILE.write_text(new_content)

    return changes


def rename_in_all_files(renames: dict[str, str], dry_run: bool = True) -> int:
    """Rename EMPTY -> DUPLICATE in all Python files. Returns files modified."""
    if not renames:
        return 0

    # Build a single regex pattern for efficiency
    pattern = re.compile(r'\b(' + '|'.join(re.escape(old) for old in renames.keys()) + r')\b')

    def replace_match(match):
        return renames[match.group(1)]

    files_modified = 0
    for py_file in (BASE / 'randomizer').rglob('*.py'):
        if '__pycache__' in str(py_file):
            continue

        try:
            content = py_file.read_text()
            new_content = pattern.sub(replace_match, content)

            if new_content != content:
                files_modified += 1
                if not dry_run:
                    py_file.write_text(new_content)
        except Exception as e:
            print(f"  Error processing {py_file}: {e}")

    return files_modified


def update_dialog_table(
    bank: int,
    removable_indexes: list[int],
    shared_index: int,
    dry_run: bool = True
) -> int:
    """Update dialog table to remove entries and reindex. Returns count removed."""
    table_file = BASE / f'randomizer/data/dialogs/contents/dialog_table_0x{bank:02x}.py'
    content = table_file.read_text()

    # Keep shared_index, remove the rest
    actual_removable = set(i for i in removable_indexes if i != shared_index)
    if not actual_removable:
        return 0

    # Parse all entries with their full text (including newlines in content)
    pattern = r"dialog_data\[(\d+)\]\s*=\s*'''(.*?)'''"

    entries = []
    for match in re.finditer(pattern, content, re.DOTALL):
        old_index = int(match.group(1))
        dialog_content = match.group(2)

        if old_index in actual_removable:
            continue

        shift = sum(1 for ri in actual_removable if ri < old_index)
        new_index = old_index - shift

        entries.append((new_index, dialog_content))

    # Use new compressed size (max index + 1)
    new_size = max(idx for idx, _ in entries) + 1 if entries else 0
    lines = [f'dialog_data = [""]*{new_size}']
    for new_index, dialog_content in sorted(entries):
        lines.append(f"dialog_data[{new_index}] = '''{dialog_content}'''")

    new_content = '\n'.join(lines) + '\n'

    if not dry_run:
        table_file.write_text(new_content)

    return len(actual_removable)


def process_bank(
    bank: int,
    pointers: dict[str, tuple[int, int, int]],
    dry_run: bool = True
) -> tuple[int, dict[str, str]]:
    """Process a single bank. Returns (count_removed, renames_dict)."""
    print(f"\n{'='*60}")
    print(f"Processing bank 0x{bank:02x}")
    print('='*60)

    dialog_table = parse_dialog_table(bank)
    if not dialog_table:
        print(f"  No dialog table found for bank 0x{bank:02x}")
        return 0, {}

    index_to_dialogs = build_index_to_dialogs(pointers)

    # Find [await] entries only used by EMPTY/DUPLICATE
    removable_indexes = find_removable_indexes(bank, dialog_table, index_to_dialogs)

    if not removable_indexes:
        print(f"  No removable [await] entries found")
        return 0, {}

    print(f"  Found {len(removable_indexes)} removable [await] indexes: {removable_indexes[:20]}{'...' if len(removable_indexes) > 20 else ''}")

    shared_index = find_shared_await_index(bank, dialog_table, index_to_dialogs, removable_indexes)

    if shared_index is None:
        print(f"  No shared [await] index available")
        return 0, {}

    print(f"  Shared [await] index: {shared_index}")

    # Calculate actual removals (excluding shared)
    actual_removable = [i for i in removable_indexes if i != shared_index]
    print(f"  Will remove {len(actual_removable)} entries")

    # Collect renames - include dialogs at shared index too (they'll share with others)
    renames = {}
    indexes_to_rename = list(actual_removable)
    if shared_index in removable_indexes:
        indexes_to_rename.append(shared_index)

    for idx in indexes_to_rename:
        dialogs = index_to_dialogs.get((bank, idx), [])
        for name in dialogs:
            if '_EMPTY' in name:
                if not '_EMPTY_' in name:
                    new_name = name.replace('_EMPTY', '_DUPLICATE')
                else:
                    new_name = name.replace('_EMPTY_', '_DUPLICATE_')
                renames[name] = new_name

    print(f"\n  Pointer changes:")
    changes = update_pointers_file(bank, removable_indexes, shared_index, dry_run)
    for change in changes[:30]:
        print(f"    {change}")
    if len(changes) > 30:
        print(f"    ... and {len(changes) - 30} more changes")

    removed = update_dialog_table(bank, removable_indexes, shared_index, dry_run)
    print(f"\n  {'Would remove' if dry_run else 'Removed'} {removed} dialog entries from table")

    return removed, renames


def main(dry_run: bool):
    if dry_run:
        print("DRY RUN - No changes will be made. Use --apply to make changes.")
    else:
        print("APPLYING CHANGES")

    print("\nParsing dialog pointers...")
    pointers = parse_pointers()
    print(f"  Found {len(pointers)} dialog pointers")

    all_renames = {}
    total_removed = 0

    for bank in [0x22, 0x23, 0x24]:
        removed, renames = process_bank(bank, pointers, dry_run)
        total_removed += removed
        all_renames.update(renames)

    # Rename EMPTY -> DUPLICATE in all Python files
    if all_renames:
        print(f"\n{'='*60}")
        print(f"Dialog name renames ({len(all_renames)} total)")
        print('='*60)
        for old, new in list(all_renames.items())[:20]:
            print(f"  {old} -> {new}")
        if len(all_renames) > 20:
            print(f"  ... and {len(all_renames) - 20} more")

        rename_count = rename_in_all_files(all_renames, dry_run)
        print(f"  {'Would modify' if dry_run else 'Modified'} {rename_count} files")

    print(f"\n{'='*60}")
    print("SUMMARY")
    print('='*60)
    print(f"  Total dialog entries {'to remove' if dry_run else 'removed'}: {total_removed}")
    print(f"  Total renames: {len(all_renames)}")

    if dry_run:
        print("\nRun with --apply to make changes.")


class Command(BaseCommand):
    help = "Compress dialog tables by removing unused [await] entries."

    def add_arguments(self, parser):
        parser.add_argument("--apply", action="store_true",
                            help="Actually make changes (default is a dry run preview)")

    def handle(self, *args, **options):
        main(dry_run=not options["apply"])
