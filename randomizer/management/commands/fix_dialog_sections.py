"""
Fix dialog section boundary violations.

The SNES game structures dialog pointers into sections. Each section's
pointers are relative to a boundary dialog. All dialogs in a section
must point to content at or after the boundary dialog's content.

This script fixes violations by:
1. Reordering dialog table content by the minimum pointer ID using each index
2. Making DUPLICATE dialogs share the boundary dialog's index in their section
"""

import re
from pathlib import Path

from django.conf import settings
from django.core.management.base import BaseCommand

BASE = Path(settings.BASE_DIR)
POINTERS_FILE = BASE / 'randomizer/data/dialogs/contents/dialog_pointers.py'

# Section definitions per bank
BANK_SECTIONS = {
    0x22: [(0x000, 0x1FF), (0x200, 0x3FF), (0x400, 0x5FF), (0x600, 0x7FF)],
    0x23: [(0x800, 0x9FF), (0xA00, 0xBFF)],
    0x24: [(0xC00, 0xDFF), (0xE00, 0xFFF)],
}


def is_duplicate(name: str) -> bool:
    """Check if a dialog is EMPTY or DUPLICATE."""
    return '_EMPTY' in name or '_DUPLICATE' in name


def parse_pointers_with_names() -> dict[int, tuple[str, int, int, int]]:
    """Parse dialog_pointers.py to get (name, bank, index, pos) for each pointer ID."""
    content = POINTERS_FILE.read_text()
    pattern = r'pointers\[(DI(\d{4})_\w+)\]\s*=\s*Dialog\(bank=(0x\d+),\s*index=(\d+),\s*pos=(\d+)\)'

    result = {}
    for match in re.finditer(pattern, content):
        name = match.group(1)
        ptr_id = int(match.group(2))
        bank = int(match.group(3), 16)
        index = int(match.group(4))
        pos = int(match.group(5))
        result[ptr_id] = (name, bank, index, pos)

    return result


def parse_dialog_table(bank: int) -> dict[int, str]:
    """Parse a dialog table file to get content at each index."""
    table_file = BASE / f'randomizer/data/dialogs/contents/dialog_table_0x{bank:02x}.py'
    content = table_file.read_text()
    pattern = r"dialog_data\[(\d+)\]\s*=\s*'''(.*?)'''"

    result = {}
    for match in re.finditer(pattern, content, re.DOTALL):
        index = int(match.group(1))
        dialog_content = match.group(2)
        result[index] = dialog_content

    return result


def get_section(bank: int, ptr_id: int) -> tuple[int, int, int]:
    """Get (section_num, section_start, section_end) for a pointer ID."""
    sections = BANK_SECTIONS.get(bank, [])
    for i, (start, end) in enumerate(sections):
        if start <= ptr_id <= end:
            return i, start, end
    return 0, 0, 0


def fix_bank(bank: int, pointers: dict[int, tuple[str, int, int, int]], dry_run: bool) -> int:
    """Fix section violations for one bank. Returns number of changes."""
    print(f"\nProcessing bank 0x{bank:02x}...")

    table = parse_dialog_table(bank)
    if not table:
        print("  No dialog table found")
        return 0

    sections = BANK_SECTIONS.get(bank, [])

    # Step 1: Find the minimum pointer ID for each content index (for ordering)
    index_min_ptr: dict[int, int] = {}
    for ptr_id, (name, b, idx, pos) in pointers.items():
        if b != bank:
            continue
        if idx not in index_min_ptr:
            index_min_ptr[idx] = ptr_id
        else:
            index_min_ptr[idx] = min(index_min_ptr[idx], ptr_id)

    # Step 2: Reorder content by minimum pointer ID
    # Include any unreferenced indexes at the end
    referenced_indexes = sorted(index_min_ptr.keys(), key=lambda i: index_min_ptr[i])
    unreferenced_indexes = sorted(set(table.keys()) - set(index_min_ptr.keys()))
    sorted_indexes = referenced_indexes + unreferenced_indexes
    old_to_new: dict[int, int] = {old: new for new, old in enumerate(sorted_indexes)}

    # Step 3: For each section, find boundary index and fix violations
    pointer_updates: dict[int, int] = {}  # ptr_id -> new_index
    content_to_duplicate: list[tuple[int, int]] = []  # (old_idx, new_idx_for_duplicate)

    next_new_idx = len(sorted_indexes)  # For duplicated content

    for section_num, (section_start, section_end) in enumerate(sections):
        # Find boundary dialog's content index
        boundary_entry = pointers.get(section_start)
        if not boundary_entry or boundary_entry[1] != bank:
            continue

        boundary_old_idx = boundary_entry[2]
        boundary_new_idx = old_to_new.get(boundary_old_idx, boundary_old_idx)

        # Find all dialogs in this section that would violate the constraint
        for ptr_id in range(section_start, section_end + 1):
            entry = pointers.get(ptr_id)
            if not entry or entry[1] != bank:
                continue

            name, _, old_idx, pos = entry
            new_idx = old_to_new.get(old_idx, old_idx)

            if new_idx < boundary_new_idx:
                if is_duplicate(name):
                    # Make this DUPLICATE point to the boundary's index
                    pointer_updates[ptr_id] = boundary_new_idx
                else:
                    # Non-duplicate needs content duplicated for this section
                    # Check if we already planned to duplicate this content for this section
                    existing_dup = next(
                        (dup_idx for dup_old, dup_idx in content_to_duplicate
                         if dup_old == old_idx and dup_idx >= boundary_new_idx),
                        None
                    )
                    if existing_dup is not None:
                        pointer_updates[ptr_id] = existing_dup
                    else:
                        # Need to create a duplicate
                        content_to_duplicate.append((old_idx, next_new_idx))
                        pointer_updates[ptr_id] = next_new_idx
                        print(f"  Duplicating content at index {old_idx} for section {section_num} "
                              f"(dialog {name})")
                        next_new_idx += 1

    # Step 4: Apply changes
    changes = 0

    needs_table_update = any(old != new for old, new in old_to_new.items()) or content_to_duplicate
    if needs_table_update:
        new_table = {old_to_new[old]: content for old, content in table.items()}

        for old_idx, dup_new_idx in content_to_duplicate:
            new_table[dup_new_idx] = table[old_idx]

        new_size = max(new_table.keys()) + 1 if new_table else 0

        lines = [f'dialog_data = [""]*{new_size}']
        for idx in sorted(new_table.keys()):
            lines.append(f"dialog_data[{idx}] = '''{new_table[idx]}'''")

        if not dry_run:
            table_file = BASE / f'randomizer/data/dialogs/contents/dialog_table_0x{bank:02x}.py'
            table_file.write_text('\n'.join(lines) + '\n')

        changes += sum(1 for old, new in old_to_new.items() if old != new)
        print(f"  Reordered {changes} table entries")

    content = POINTERS_FILE.read_text()
    ptr_changes = 0

    for ptr_id, (name, b, old_idx, pos) in pointers.items():
        if b != bank:
            continue

        if ptr_id in pointer_updates:
            new_idx = pointer_updates[ptr_id]
        else:
            new_idx = old_to_new.get(old_idx, old_idx)

        if new_idx != old_idx:
            pattern = rf'(pointers\[{name}\]\s*=\s*Dialog\(bank=0x{bank:02x},\s*index=){old_idx}(,\s*pos={pos}\))'
            replacement = rf'\g<1>{new_idx}\g<2>'
            new_content, count = re.subn(pattern, replacement, content)
            if count > 0:
                content = new_content
                ptr_changes += 1

    if ptr_changes > 0:
        if not dry_run:
            POINTERS_FILE.write_text(content)
        print(f"  Updated {ptr_changes} pointers")

    return changes + ptr_changes


def main(dry_run: bool):
    if dry_run:
        print("DRY RUN - No changes will be made. Use --apply to make changes.")

    print("Parsing dialog pointers...")
    pointers = parse_pointers_with_names()
    print(f"Found {len(pointers)} pointers")

    total_changes = 0
    for bank in [0x22, 0x23, 0x24]:
        total_changes += fix_bank(bank, pointers, dry_run)

    if total_changes > 0:
        print(f"\nTotal: {total_changes} changes")
        if dry_run:
            print("Run with --apply to make changes.")
    else:
        print("\nNo changes needed.")


class Command(BaseCommand):
    help = "Fix dialog section boundary violations."

    def add_arguments(self, parser):
        parser.add_argument("--apply", action="store_true",
                            help="Actually make changes (default is a dry run preview)")

    def handle(self, *args, **options):
        main(dry_run=not options["apply"])
