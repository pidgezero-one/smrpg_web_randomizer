#!/usr/bin/env python3
"""Find repeated command sequences in battle animation scripts.

Scans all script files in randomizer/data/battle_animation/_35/contents
and finds sequences of commands that repeat across files.
"""

import ast
import re
import sys
from collections import defaultdict
from pathlib import Path

SCRIPTS_DIR = Path(__file__).parent.parent / "randomizer/data/battle_animation/_35/contents"
OUTPUT_FILE = Path(__file__).parent.parent / "repeated_sequences_report.txt"

# Known command sizes (approximate based on typical usage)
# These are estimates - actual sizes may vary by arguments
COMMAND_SIZES = {
    "UnknownCommand": 1,  # varies by bytearray length
    "Pause1Frame": 1,
    "Jmp": 3,
    "ResetTargetMappingMemory": 1,
    "ResetObjectMappingMemory": 1,
    "JmpIfTargetEnabled": 3,
    "SpriteSequence": 2,
    "PauseScriptUntil": 3,
    "GameOverIfNoAlliesStanding": 1,
    "RunSubroutine": 3,
    "PauseScriptUntilAMEMBitsSet": 3,
    "PauseScriptUntilSpriteSequenceDone": 1,
    "ClearAMEM8Bit": 2,
    "SetAMEM8BitTo7E5x": 5,
    "SetAMEM8BitTo7E1x": 5,
    "JmpIfAMEMBitsSet": 5,
    "SetSequenceSpeed": 2,
    "MoveObject": 8,
    "ActorExitBattleEXPERIMENTAL": 1,
    "DefineObjectQueue": 2,  # varies
    "DrawSpriteAtAMEM32Coords": 4,
    "ReturnSubroutine": 1,
    "SetAMEMToRandomByte": 3,
    "SpriteQueueReferenceEXPERIMENTAL": 4,
    "PlaySound": 3,
    "ScreenFlashWithDuration": 3,
    "SetAMEM16Bit": 4,
    "SetAMEM8Bit": 3,
    "JmpIfAMEMEquals": 5,
    "AddToAMEM8Bit": 3,
    "SubtractFromAMEM8Bit": 3,
    "IncrementAMEM8Bit": 2,
    "DecrementAMEM8Bit": 2,
    "ObjectMovementSpeedFromAMEM": 2,
    "AttackTimerBegins": 1,
    "AttackTimerEnds": 1,
    "BattleEvent": 2,
    "DrawEffect": 3,
    "EnableDamageNumerals": 1,
    "DisableDamageNumerals": 1,
    "SetTargetHP": 3,
    "SetAllTargetsHP": 3,
}


def extract_command_signature(node: ast.Call) -> str | None:
    """Extract a signature for a command call, ignoring 'identifier' parameter."""
    if not isinstance(node.func, ast.Name):
        return None

    class_name = node.func.id

    # Build argument list, excluding 'identifier'
    args = []

    # Positional arguments
    for arg in node.args:
        args.append(ast.unparse(arg))

    # Keyword arguments (excluding 'identifier')
    for kw in node.keywords:
        if kw.arg != "identifier":
            args.append(f"{kw.arg}={ast.unparse(kw.value)}")

    return f"{class_name}({', '.join(args)})"


def estimate_size(signature: str) -> int:
    """Estimate the byte size of a command from its signature."""
    # Extract class name
    match = re.match(r"(\w+)\(", signature)
    if not match:
        return 1
    class_name = match.group(1)

    # Special case for UnknownCommand - size is length of bytearray
    if class_name == "UnknownCommand":
        # Try to extract bytearray length
        ba_match = re.search(r"bytearray\(b'([^']*)'\)", signature)
        if ba_match:
            # Count actual bytes (handle escape sequences)
            content = ba_match.group(1)
            # Simple approximation - count non-escape chars + escape sequences
            return len(content.encode('unicode_escape').decode('ascii').encode('latin-1'))
        return 1

    return COMMAND_SIZES.get(class_name, 2)


def parse_script_file(filepath: Path) -> list[tuple[str, int]]:
    """Parse a script file and return list of (signature, estimated_size) tuples."""
    try:
        content = filepath.read_text()
        tree = ast.parse(content)
    except Exception as e:
        print(f"Error parsing {filepath}: {e}")
        return []

    commands = []

    # Find the AnimationScriptBlock call
    for node in ast.walk(tree):
        if isinstance(node, ast.Call):
            if isinstance(node.func, ast.Name) and node.func.id == "AnimationScriptBlock":
                # Find the script= keyword argument
                for kw in node.keywords:
                    if kw.arg == "script" and isinstance(kw.value, ast.List):
                        for elem in kw.value.elts:
                            if isinstance(elem, ast.Call):
                                sig = extract_command_signature(elem)
                                if sig:
                                    size = estimate_size(sig)
                                    commands.append((sig, size))

    return commands


def find_repeated_sequences(all_commands: list[tuple[str, list[tuple[str, int]]]]) -> dict:
    """Find sequences that repeat across files.

    Returns dict of {sequence_tuple: [(filename, start_idx), ...]}
    """
    # Build a map of all sequences of length 2+ with total size > 3
    sequence_locations: dict[tuple, list[tuple[str, int]]] = defaultdict(list)

    MIN_SEQUENCE_LENGTH = 2
    MAX_SEQUENCE_LENGTH = 20
    MIN_TOTAL_SIZE = 4

    for filename, commands in all_commands:
        if not commands:
            continue

        signatures = [sig for sig, _ in commands]
        sizes = [size for _, size in commands]

        # Try all sequence lengths
        for seq_len in range(MIN_SEQUENCE_LENGTH, min(MAX_SEQUENCE_LENGTH + 1, len(commands) + 1)):
            for start_idx in range(len(commands) - seq_len + 1):
                seq = tuple(signatures[start_idx:start_idx + seq_len])
                total_size = sum(sizes[start_idx:start_idx + seq_len])

                if total_size > MIN_TOTAL_SIZE:
                    sequence_locations[seq].append((filename, start_idx))

    # Filter to only sequences that appear more than once
    repeated = {seq: locs for seq, locs in sequence_locations.items() if len(locs) > 1}

    return repeated


def remove_subsequences(repeated: dict) -> dict:
    """Remove sequences that are fully contained within longer repeated sequences."""
    # Sort by sequence length (longest first)
    sorted_seqs = sorted(repeated.keys(), key=len, reverse=True)

    to_remove = set()

    for i, longer_seq in enumerate(sorted_seqs):
        for shorter_seq in sorted_seqs[i+1:]:
            if shorter_seq in to_remove:
                continue
            # Check if shorter is a subsequence of longer
            len_diff = len(longer_seq) - len(shorter_seq)
            for offset in range(len_diff + 1):
                if longer_seq[offset:offset + len(shorter_seq)] == shorter_seq:
                    # Check if all locations of shorter are covered by longer
                    longer_locs = set(repeated[longer_seq])
                    shorter_locs = repeated[shorter_seq]

                    # A shorter sequence location is covered if there's a longer sequence
                    # at (same_file, start_idx - offset) for some valid offset
                    all_covered = True
                    for fname, idx in shorter_locs:
                        covered = False
                        for check_offset in range(len_diff + 1):
                            if (fname, idx - check_offset) in longer_locs:
                                covered = True
                                break
                        if not covered:
                            all_covered = False
                            break

                    if all_covered:
                        to_remove.add(shorter_seq)
                        break

    return {seq: locs for seq, locs in repeated.items() if seq not in to_remove}


def main():
    print(f"Scanning scripts in {SCRIPTS_DIR}")

    # Parse all script files
    all_commands = []
    script_files = sorted(SCRIPTS_DIR.glob("script_*.py"))

    for filepath in script_files:
        commands = parse_script_file(filepath)
        if commands:
            all_commands.append((filepath.name, commands))
            print(f"  Parsed {filepath.name}: {len(commands)} commands")

    print(f"\nTotal files parsed: {len(all_commands)}")

    # Find repeated sequences
    print("\nFinding repeated sequences...")
    repeated = find_repeated_sequences(all_commands)
    print(f"Found {len(repeated)} repeated sequences (before filtering)")

    # Remove subsequences
    print("Removing subsequences...")
    filtered = remove_subsequences(repeated)
    print(f"After filtering: {len(filtered)} unique repeated sequences")

    # Calculate total sizes for each sequence
    results = []
    for seq, locs in filtered.items():
        total_size = sum(estimate_size(sig) for sig in seq)
        results.append((seq, locs, total_size, len(seq)))

    # Sort by total size * occurrence count (most impactful first)
    results.sort(key=lambda x: x[2] * len(x[1]), reverse=True)

    # Write report
    with open(OUTPUT_FILE, "w") as f:
        f.write("REPEATED COMMAND SEQUENCES IN BATTLE ANIMATION SCRIPTS\n")
        f.write("=" * 70 + "\n\n")
        f.write(f"Total unique repeated sequences found: {len(results)}\n")
        f.write(f"Minimum sequence size: > 3 bytes\n")
        f.write(f"Only showing sequences that repeat at least twice\n\n")
        f.write("=" * 70 + "\n\n")

        for i, (seq, locs, total_size, seq_len) in enumerate(results, 1):
            savings = total_size * (len(locs) - 1)  # Bytes saved if extracted to subroutine

            f.write(f"SEQUENCE #{i}\n")
            f.write(f"-" * 40 + "\n")
            f.write(f"Length: {seq_len} commands\n")
            f.write(f"Estimated size: {total_size} bytes\n")
            f.write(f"Occurrences: {len(locs)}\n")
            f.write(f"Potential savings: ~{savings} bytes (if extracted to subroutine)\n\n")

            f.write("Commands:\n")
            for j, sig in enumerate(seq, 1):
                f.write(f"  {j}. {sig}\n")

            f.write("\nLocations:\n")
            for fname, idx in locs:
                f.write(f"  - {fname} at index {idx}\n")

            f.write("\n" + "=" * 70 + "\n\n")

    print(f"\nReport written to: {OUTPUT_FILE}")


if __name__ == "__main__":
    main()
