#!/usr/bin/env python3
"""Find DI####_EMPTY dialogs that ARE referenced outside their definition files."""

import re
from pathlib import Path
from collections import defaultdict

BASE = Path('/Users/stefkischak/code/smrpg_web_randomizer')

def get_empty_dialog_names():
    """Get all DI####_EMPTY names from dialog_names.py."""
    names_file = BASE / 'randomizer/data/variables/dialog_names.py'
    content = names_file.read_text()

    # Match DI####_EMPTY (with optional suffix like _EMPTY_2)
    matches = re.findall(r'^(DI\d{4}_EMPTY\w*)\s*=', content, re.MULTILINE)
    return set(matches)

def find_references():
    """Find all DI####_EMPTY references in the codebase."""
    references = defaultdict(list)

    excluded_files = {
        'dialog_names.py',
        'dialog_pointers.py',
    }

    # Walk through all Python files in randomizer
    for py_file in (BASE / 'randomizer').rglob('*.py'):
        if py_file.name in excluded_files:
            continue
        if '__pycache__' in str(py_file):
            continue

        try:
            content = py_file.read_text()
            lines = content.split('\n')
            rel_path = str(py_file.relative_to(BASE))

            for line_num, line in enumerate(lines, 1):
                # Find all DI####_EMPTY references
                found = re.findall(r'\b(DI\d{4}_EMPTY\w*)\b', line)
                for name in found:
                    references[name].append((rel_path, line_num, line.strip()[:80]))
        except Exception as e:
            print(f"Error reading {py_file}: {e}")

    return references

def main():
    print("Finding all DI####_EMPTY dialog names...")
    empty_names = get_empty_dialog_names()
    print(f"Found {len(empty_names)} EMPTY dialog names")

    print("\nScanning codebase for references...")
    references = find_references()

    # Filter to only EMPTY dialogs that are actually defined
    referenced_empty = {name: refs for name, refs in references.items() if name in empty_names}

    print(f"\n{'='*80}")
    print(f"EMPTY DIALOGS THAT ARE REFERENCED ({len(referenced_empty)} total):")
    print('='*80)

    for name in sorted(referenced_empty.keys()):
        refs = referenced_empty[name]
        print(f"\n{name} ({len(refs)} reference(s)):")
        for filepath, line_num, line_preview in refs:
            print(f"  {filepath}:{line_num}")
            print(f"    {line_preview}")

    print(f"\n{'='*80}")
    print(f"Total: {len(referenced_empty)} EMPTY dialogs are referenced in the codebase")

if __name__ == '__main__':
    main()
