#!/usr/bin/env python3
"""Find unreferenced dialogs that have actual content (not just [await] or [end])
and whose content is not shared with any referenced dialog."""

import re
from pathlib import Path
from collections import defaultdict

BASE = Path('/Users/stefkischak/code/smrpg_web_randomizer')

def get_all_dialog_names():
    """Get all DI####_xxx names from dialog_names.py."""
    names_file = BASE / 'randomizer/data/variables/dialog_names.py'
    content = names_file.read_text()
    matches = re.findall(r'^(DI\d{4}_\w+)\s*=', content, re.MULTILINE)
    return set(matches)

def find_all_references():
    """Find all DI####_xxx references in the codebase."""
    references = set()

    excluded_files = {
        'dialog_names.py',
        'dialog_pointers.py',
    }

    for py_file in (BASE / 'randomizer').rglob('*.py'):
        if py_file.name in excluded_files:
            continue
        if '__pycache__' in str(py_file):
            continue

        try:
            content = py_file.read_text()
            found = re.findall(r'\b(DI\d{4}_\w+)\b', content)
            references.update(found)
        except Exception as e:
            print(f"Error reading {py_file}: {e}")

    return references

def get_dialog_pointers():
    """Parse dialog_pointers.py to get bank and index for each dialog."""
    pointers_file = BASE / 'randomizer/data/dialogs/contents/dialog_pointers.py'
    content = pointers_file.read_text()

    # Match pointers[DI####_xxx] = Dialog(bank=0x##, index=###, ...)
    pattern = r'pointers\[(DI\d{4}_\w+)\]\s*=\s*Dialog\(bank=(0x\d+),\s*index=(\d+)'
    matches = re.findall(pattern, content)

    result = {}
    for name, bank_str, index_str in matches:
        bank = int(bank_str, 16)
        index = int(index_str)
        result[name] = (bank, index)

    return result

def load_dialog_tables():
    """Load all dialog table content."""
    tables = {}
    for bank in [0x22, 0x23, 0x24]:
        table_file = BASE / f'randomizer/data/dialogs/contents/dialog_table_0x{bank:02x}.py'
        if table_file.exists():
            content = table_file.read_text()
            tables[bank] = content
    return tables

def get_dialog_content(tables, bank, index):
    """Extract dialog content for a given bank and index."""
    if bank not in tables:
        return None

    content = tables[bank]

    # Match dialog_data[index] = '''...''' (multiline)
    pattern = rf"dialog_data\[{index}\]\s*=\s*'''(.*?)'''"
    match = re.search(pattern, content, re.DOTALL)

    if match:
        return match.group(1)
    return None

def is_empty_content(content):
    """Check if content is effectively empty (just [await], [end], whitespace)."""
    if content is None:
        return True

    # Remove whitespace
    stripped = content.strip()

    # Check for empty or just control codes
    empty_patterns = [
        '',
        '[await]',
        '[end]',
        '[await][end]',
        '[end][await]',
    ]

    return stripped in empty_patterns

def main():
    print("Finding all dialog names...")
    all_names = get_all_dialog_names()
    print(f"Found {len(all_names)} dialog names")

    print("Finding references...")
    references = find_all_references()
    print(f"Found {len(references)} referenced dialog names")

    print("Loading dialog pointers...")
    pointers = get_dialog_pointers()
    print(f"Found {len(pointers)} dialog pointers")

    print("Loading dialog tables...")
    tables = load_dialog_tables()

    # Build content -> dialog names mapping and find content used by referenced dialogs
    print("Building content mapping...")
    content_to_dialogs = defaultdict(list)
    referenced_contents = set()

    for name in all_names:
        if name not in pointers:
            continue
        bank, index = pointers[name]
        content = get_dialog_content(tables, bank, index)
        if content is not None:
            content_to_dialogs[content].append(name)
            if name in references:
                referenced_contents.add(content)

    print(f"Found {len(referenced_contents)} unique contents used by referenced dialogs")

    # Find unreferenced dialogs
    unreferenced = all_names - references

    print(f"\nChecking content of {len(unreferenced)} unreferenced dialogs...")

    unreferenced_with_unique_content = []

    for name in sorted(unreferenced):
        if name not in pointers:
            continue

        bank, index = pointers[name]
        content = get_dialog_content(tables, bank, index)

        if is_empty_content(content):
            continue

        # Skip if this content is also used by a referenced dialog
        if content in referenced_contents:
            continue

        # Has actual content that isn't shared with any referenced dialog
        preview = content.replace('\n', ' ')[:60] if content else ""
        unreferenced_with_unique_content.append((name, bank, index, preview))

    print(f"\n{'='*80}")
    print(f"UNREFERENCED DIALOGS WITH UNIQUE CONTENT ({len(unreferenced_with_unique_content)} total):")
    print("(Excludes empty dialogs and dialogs whose content is shared with a referenced dialog)")
    print('='*80)

    for name, bank, index, preview in unreferenced_with_unique_content:
        print(f"\n{name} (bank 0x{bank:02x}, index {index}):")
        print(f"  {preview}...")

    print(f"\n{'='*80}")
    print(f"Total: {len(unreferenced_with_unique_content)} unreferenced dialogs with unique content")

if __name__ == '__main__':
    main()
