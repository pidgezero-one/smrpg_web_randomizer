"""
Fix dialog pointer ordering violations.

Ensures that dialog indexes are monotonically non-decreasing within each bank.
DUPLICATE dialogs share the index of the most recent non-duplicate dialog.

Rearranges content in dialog_table files rather than duplicating.
Only duplicates when two non-duplicate dialogs share content but can't share an index.
"""
from randomizer.data.variables import dialog_names

import re
from pathlib import Path

from django.conf import settings
from django.core.management.base import BaseCommand

BASE = Path(settings.BASE_DIR)
POINTERS_FILE = BASE / 'randomizer/data/dialogs/contents/dialog_pointers.py'


def is_duplicate(name: str) -> bool:
    """Check if a dialog is EMPTY or DUPLICATE."""
    return '_EMPTY' in name or '_DUPLICATE' in name


def get_name_to_id_mapping() -> dict[str, int]:
    """Get mapping from variable name to actual ptr_id value."""
    mapping = {}
    for name in dir(dialog_names):
        if name.startswith('DI') and name[2:6].isdigit():
            mapping[name] = getattr(dialog_names, name)
    return mapping


def parse_pointers() -> list[tuple[int, str, int, int, int]]:
    """Parse dialog_pointers.py to get (ptr_id, name, bank, index, pos) for each pointer."""
    name_to_id = get_name_to_id_mapping()

    content = POINTERS_FILE.read_text()
    pattern = r'pointers\[(DI\d{4}_\w+)\]\s*=\s*Dialog\(bank=(0x\d+),\s*index=(\d+),\s*pos=(\d+)\)'

    result = []
    for match in re.finditer(pattern, content):
        name = match.group(1)
        ptr_id = name_to_id.get(name)
        if ptr_id is None:
            print(f"Warning: {name} not found in dialog_names")
            continue
        bank = int(match.group(2), 16)
        index = int(match.group(3))
        pos = int(match.group(4))
        result.append((ptr_id, name, bank, index, pos))

    return sorted(result, key=lambda x: x[0])


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


def fix_bank(bank: int, pointers: list[tuple[int, str, int, int, int]], dry_run: bool) -> list[str]:
    """Fix ordering violations for one bank. Returns list of manual fixes needed."""
    print(f"\nProcessing bank 0x{bank:02x}...")

    bank_pointers = [(p, n, b, i, pos) for p, n, b, i, pos in pointers if b == bank]
    table = parse_dialog_table(bank)

    if not table:
        print("  No dialog table found")
        return []

    manual_fixes_needed = []

    # Step 1: Collect non-duplicate dialogs in ptr_id order
    non_dup_dialogs = []
    for ptr_id, name, b, index, pos in bank_pointers:
        if not is_duplicate(name):
            non_dup_dialogs.append((ptr_id, name, index, pos))

    # Step 2: Build new table by processing dialogs in ptr_id order
    # Each non-duplicate dialog's content goes to the next available index

    # Track which original indexes we've already placed
    placed_indexes: dict[int, int] = {}  # original_index -> new_index
    per_dialog_index: dict[int, int] = {}  # ptr_id -> new_index (for duplications)
    new_table: dict[int, str] = {}
    next_new_index = 0

    # Also track duplications needed
    content_duplications = []

    for ptr_id, name, orig_index, pos in non_dup_dialogs:
        if orig_index in placed_indexes:
            # Content already placed - check if we can reuse it
            existing_new_index = placed_indexes[orig_index]
            if existing_new_index >= next_new_index:
                # Can reuse - it's still valid (>= our minimum)
                per_dialog_index[ptr_id] = existing_new_index
                # Update next_new_index to be after this
                next_new_index = existing_new_index + 1
            else:
                # Can't reuse - need to duplicate at a higher index
                dup_new_index = next_new_index
                new_table[dup_new_index] = table[orig_index]
                per_dialog_index[ptr_id] = dup_new_index
                content_duplications.append((orig_index, dup_new_index, name, ptr_id))
                next_new_index = dup_new_index + 1
        else:
            # First time seeing this content - place it
            new_index = next_new_index
            new_table[new_index] = table[orig_index]
            placed_indexes[orig_index] = new_index
            per_dialog_index[ptr_id] = new_index
            next_new_index = new_index + 1

    # Step 3: Calculate pointer updates
    pointer_updates: dict[int, int] = {}  # ptr_id -> new_index
    last_non_dup_new_index = -1

    for ptr_id, name, b, orig_index, pos in bank_pointers:
        if is_duplicate(name):
            # DUPLICATE: use same index as last non-duplicate
            if last_non_dup_new_index >= 0:
                pointer_updates[ptr_id] = last_non_dup_new_index
        else:
            # Non-duplicate: look up new index from per_dialog_index
            new_index = per_dialog_index.get(ptr_id, placed_indexes.get(orig_index, orig_index))

            if new_index != orig_index:
                pointer_updates[ptr_id] = new_index

            last_non_dup_new_index = new_index

    # Build manual fixes list
    for orig_index, dup_new_index, name, ptr_id in content_duplications:
        manual_fixes_needed.append(
            f"Bank 0x{bank:02x}: {name} (ptr {ptr_id}) shares content (orig index {orig_index}) "
            f"with earlier dialog but can't share index. Duplicated to index {dup_new_index}."
        )

    # Check if we actually have changes
    if not pointer_updates and not content_duplications:
        print("  No changes needed")
        return []

    print(f"  New table has {len(new_table)} entries")
    print(f"  {len(content_duplications)} content duplications")
    print(f"  {len(pointer_updates)} pointer updates")

    # Step 4: Apply changes
    if not dry_run:
        new_size = max(new_table.keys()) + 1 if new_table else 0
        lines = [f'dialog_data = [""]*{new_size}']
        for idx in sorted(new_table.keys()):
            lines.append(f"dialog_data[{idx}] = '''{new_table[idx]}'''")

        table_file = BASE / f'randomizer/data/dialogs/contents/dialog_table_0x{bank:02x}.py'
        table_file.write_text('\n'.join(lines) + '\n')

        if pointer_updates:
            content = POINTERS_FILE.read_text()

            for ptr_id, new_index in pointer_updates.items():
                orig = next((p for p in bank_pointers if p[0] == ptr_id), None)
                if not orig:
                    continue
                _, name, _, old_index, pos = orig

                pattern = rf'(pointers\[{name}\]\s*=\s*Dialog\(bank=0x{bank:02x},\s*index=){old_index}(,\s*pos={pos}\))'
                replacement = rf'\g<1>{new_index}\g<2>'
                new_content, count = re.subn(pattern, replacement, content)
                if count == 0:
                    print(f"  Warning: Failed to update {name} from index {old_index} to {new_index}")
                else:
                    content = new_content

            POINTERS_FILE.write_text(content)

    return manual_fixes_needed


def verify_bank(bank: int, pointers: list[tuple[int, str, int, int, int]]) -> list[str]:
    """Verify that a bank has no ordering violations."""
    bank_pointers = [(p, n, b, i, pos) for p, n, b, i, pos in pointers if b == bank]

    violations = []
    last_non_dup_index = -1

    for ptr_id, name, b, index, pos in bank_pointers:
        if is_duplicate(name):
            if index != last_non_dup_index and last_non_dup_index >= 0:
                violations.append(f"{name} (ptr {ptr_id}): DUPLICATE at index {index}, should be {last_non_dup_index}")
        else:
            if index < last_non_dup_index:
                violations.append(f"{name} (ptr {ptr_id}): index {index} < previous non-dup index {last_non_dup_index}")
            last_non_dup_index = index

    return violations


def main(dry_run: bool, verify_only: bool):
    if verify_only:
        print("VERIFY MODE - Checking for violations...")
        pointers = parse_pointers()
        for bank in [0x22, 0x23, 0x24]:
            violations = verify_bank(bank, pointers)
            if violations:
                print(f"\nBank 0x{bank:02x}: {len(violations)} violations")
                for v in violations[:20]:
                    print(f"  {v}")
                if len(violations) > 20:
                    print(f"  ... and {len(violations) - 20} more")
            else:
                print(f"\nBank 0x{bank:02x}: No violations")
        return

    if dry_run:
        print("DRY RUN - No changes will be made. Use --apply to make changes.")

    print("Parsing dialog pointers...")
    pointers = parse_pointers()
    print(f"Found {len(pointers)} pointers")

    all_manual_fixes = []
    for bank in [0x22, 0x23, 0x24]:
        manual_fixes = fix_bank(bank, pointers, dry_run)
        all_manual_fixes.extend(manual_fixes)

    if all_manual_fixes:
        print("\n=== CONTENT DUPLICATIONS ===")
        for fix in all_manual_fixes:
            print(f"  {fix}")

    if dry_run:
        print("\nRun with --apply to make changes.")
    else:
        # Verify after applying
        print("\n=== VERIFICATION ===")
        pointers = parse_pointers()  # Re-parse after changes
        for bank in [0x22, 0x23, 0x24]:
            violations = verify_bank(bank, pointers)
            if violations:
                print(f"Bank 0x{bank:02x}: {len(violations)} violations remaining!")
                for v in violations[:5]:
                    print(f"  {v}")
            else:
                print(f"Bank 0x{bank:02x}: OK")


class Command(BaseCommand):
    help = "Fix dialog pointer ordering violations."

    def add_arguments(self, parser):
        parser.add_argument("--apply", action="store_true",
                            help="Actually make changes (default is a dry run preview)")
        parser.add_argument("--verify", action="store_true",
                            help="Only report ordering violations; make no changes")

    def handle(self, *args, **options):
        main(dry_run=not options["apply"], verify_only=options["verify"])
