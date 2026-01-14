#!/usr/bin/env python3
"""
Analyze battle animation scripts to find repeated command sequences.
Identifies sequences that could potentially be extracted to subroutines.
"""

import os
import sys
from pathlib import Path
from collections import defaultdict
from dataclasses import dataclass, field

# Add the project to path
sys.path.insert(0, str(Path(__file__).parent))

# Set up Django settings before importing randomizer modules
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'randomizer.settings')

from smrpgpatchbuilder.datatypes.battle_animation_scripts.commands.commands import (
    ReturnSubroutine,
    ReturnSpriteQueue,
    Jmp,
)
from smrpgpatchbuilder.datatypes.battle_animation_scripts.commands.types.classes import (
    UsableAnimationScriptCommand,
)


@dataclass
class SequenceOccurrence:
    """Tracks where a sequence occurs."""
    script_name: str
    start_index: int
    bank: str  # e.g., "0x35", "0x3A", "0x02"


@dataclass
class SequenceInfo:
    """Information about a repeated sequence."""
    commands: tuple  # tuple of command repr strings for hashing
    command_objects: list  # actual command objects from first occurrence
    total_bytes: int
    occurrences: list[SequenceOccurrence] = field(default_factory=list)
    ends_with_return: bool = False
    return_type: str = ""  # "ReturnSubroutine", "Jmp", "ReturnSpriteQueue", or ""

    @property
    def occurrence_count(self) -> int:
        return len(self.occurrences)

    @property
    def potential_savings(self) -> int:
        """Estimate bytes saved if extracted to subroutine.
        Each occurrence would be replaced with a JmpToSubroutine (3 bytes).
        Savings = (total_bytes * occurrences) - total_bytes - (3 * occurrences)
        """
        if self.occurrence_count < 2:
            return 0
        # Keep one copy as subroutine, replace others with calls
        return (self.total_bytes * (self.occurrence_count - 1)) - (3 * (self.occurrence_count - 1))


def get_command_signature(cmd: UsableAnimationScriptCommand) -> str:
    """Get a signature string for a command that can be used for comparison."""
    cmd_type = type(cmd).__name__

    try:
        # Render the command to get its actual bytes - this is the most accurate comparison
        rendered = cmd.render()
        return f"{cmd_type}:{rendered.hex()}"
    except Exception:
        # Fallback to repr if render fails
        return repr(cmd)


def find_sequences_in_script(
    commands: list[UsableAnimationScriptCommand],
    script_name: str,
    bank: str,
    min_bytes: int = 3,
    max_length: int = 20
) -> dict[tuple, SequenceInfo]:
    """Find all sequences of commands in a script."""
    sequences: dict[tuple, SequenceInfo] = {}

    for start_idx in range(len(commands)):
        current_bytes = 0
        current_sigs: list[str] = []
        current_cmds: list[UsableAnimationScriptCommand] = []

        for length in range(1, min(max_length + 1, len(commands) - start_idx + 1)):
            cmd = commands[start_idx + length - 1]
            sig = get_command_signature(cmd)
            current_sigs.append(sig)
            current_cmds.append(cmd)
            current_bytes += cmd.size

            # Only consider sequences with total size >= min_bytes
            if current_bytes >= min_bytes and length >= 2:
                seq_key = tuple(current_sigs)

                if seq_key not in sequences:
                    # Check if last command is a return-type command
                    last_cmd = current_cmds[-1]
                    ends_with_return = isinstance(last_cmd, (ReturnSubroutine, ReturnSpriteQueue, Jmp))
                    return_type = ""
                    if isinstance(last_cmd, ReturnSubroutine):
                        return_type = "ReturnSubroutine"
                    elif isinstance(last_cmd, ReturnSpriteQueue):
                        return_type = "ReturnSpriteQueue"
                    elif isinstance(last_cmd, Jmp):
                        return_type = "Jmp"

                    sequences[seq_key] = SequenceInfo(
                        commands=seq_key,
                        command_objects=list(current_cmds),
                        total_bytes=current_bytes,
                        ends_with_return=ends_with_return,
                        return_type=return_type
                    )

                sequences[seq_key].occurrences.append(
                    SequenceOccurrence(script_name, start_idx, bank)
                )

    return sequences


def merge_sequences(all_sequences: list[dict[tuple, SequenceInfo]]) -> dict[tuple, SequenceInfo]:
    """Merge sequences from multiple scripts."""
    merged: dict[tuple, SequenceInfo] = {}

    for script_sequences in all_sequences:
        for key, info in script_sequences.items():
            if key not in merged:
                merged[key] = SequenceInfo(
                    commands=info.commands,
                    command_objects=info.command_objects,
                    total_bytes=info.total_bytes,
                    ends_with_return=info.ends_with_return,
                    return_type=info.return_type
                )
            merged[key].occurrences.extend(info.occurrences)

    return merged


def format_command_for_display(cmd: UsableAnimationScriptCommand) -> str:
    """Format a command for display in the report."""
    cmd_type = type(cmd).__name__

    # Try to get meaningful attributes
    attrs = []

    # Check for common attributes
    for attr in ['sprite_id', 'sound', 'amem', 'omem', 'value', 'sequence',
                 'destinations', 'palette_row', 'vram_address', 'x', 'y', 'z',
                 'origin', 'frames', 'channel', 'effect', 'target']:
        if hasattr(cmd, attr):
            val = getattr(cmd, attr)
            if val is not None:
                if isinstance(val, list) and len(val) > 3:
                    val = f"[{len(val)} items]"
                attrs.append(f"{attr}={val}")

    if attrs:
        return f"{cmd_type}({', '.join(attrs[:5])})"  # Limit to 5 attrs
    return f"{cmd_type}()"


@dataclass
class BankSequenceInfo:
    """Sequence info filtered to a specific bank."""
    seq_info: SequenceInfo
    bank: str
    bank_occurrences: list[SequenceOccurrence]

    @property
    def occurrence_count(self) -> int:
        return len(self.bank_occurrences)

    @property
    def potential_savings(self) -> int:
        """Estimate bytes saved if extracted to subroutine."""
        if self.occurrence_count < 2:
            return 0
        total_bytes = self.seq_info.total_bytes
        return (total_bytes * (self.occurrence_count - 1)) - (3 * (self.occurrence_count - 1))


def generate_report(sequences: dict[tuple, SequenceInfo], output_path: Path) -> None:
    """Generate the report file."""
    # Group occurrences by bank and filter to sequences with 2+ occurrences in same bank
    bank_sequences: list[BankSequenceInfo] = []

    for seq_info in sequences.values():
        # Group occurrences by bank
        by_bank: dict[str, list[SequenceOccurrence]] = {}
        for occ in seq_info.occurrences:
            if occ.bank not in by_bank:
                by_bank[occ.bank] = []
            by_bank[occ.bank].append(occ)

        # Only include if 2+ occurrences in the same bank
        for bank, occs in by_bank.items():
            if len(occs) >= 2:
                bank_sequences.append(BankSequenceInfo(
                    seq_info=seq_info,
                    bank=bank,
                    bank_occurrences=occs
                ))

    # Sort by potential savings (highest first), then by occurrence count
    sorted_sequences = sorted(
        bank_sequences,
        key=lambda x: (x.potential_savings, x.occurrence_count),
        reverse=True
    )

    with open(output_path, 'w') as f:
        f.write("REPEATED COMMAND SEQUENCES IN BATTLE ANIMATION SCRIPTS\n")
        f.write("=" * 70 + "\n\n")
        f.write(f"Total unique repeated sequences found: {len(sorted_sequences)}\n")
        f.write("Minimum sequence size: >= 3 bytes\n")
        f.write("Only showing sequences that repeat at least twice WITHIN THE SAME BANK\n\n")

        # Summary statistics
        total_potential_savings = sum(s.potential_savings for s in sorted_sequences)
        sequences_with_return = sum(1 for s in sorted_sequences if s.seq_info.ends_with_return)
        f.write(f"Total potential savings: ~{total_potential_savings} bytes\n")
        f.write(f"Sequences ending with return-type command: {sequences_with_return}\n")
        f.write("=" * 70 + "\n\n")

        # Separate sections for sequences with and without return commands
        f.write("=" * 70 + "\n")
        f.write("SECTION 1: SEQUENCES ENDING WITH RETURN-TYPE COMMANDS\n")
        f.write("(Best candidates for subroutine extraction)\n")
        f.write("=" * 70 + "\n\n")

        seq_num = 1
        return_sequences = [s for s in sorted_sequences if s.seq_info.ends_with_return]
        for bank_seq in return_sequences:
            seq_info = bank_seq.seq_info
            f.write(f"SEQUENCE #{seq_num}\n")
            f.write("-" * 40 + "\n")
            f.write(f"Bank: {bank_seq.bank}\n")
            f.write(f"Length: {len(seq_info.command_objects)} commands\n")
            f.write(f"Size: {seq_info.total_bytes} bytes\n")
            f.write(f"Occurrences in bank: {bank_seq.occurrence_count}\n")
            f.write(f"Potential savings: ~{bank_seq.potential_savings} bytes\n")
            f.write(f"Ends with: {seq_info.return_type}\n\n")

            f.write("Commands:\n")
            for i, cmd in enumerate(seq_info.command_objects, 1):
                f.write(f"  {i}. {format_command_for_display(cmd)}\n")
            f.write("\n")

            f.write("Locations:\n")
            for occ in bank_seq.bank_occurrences[:50]:  # Limit to first 50 locations
                f.write(f"  - {occ.script_name} at index {occ.start_index}\n")
            if len(bank_seq.bank_occurrences) > 50:
                f.write(f"  ... and {len(bank_seq.bank_occurrences) - 50} more locations\n")
            f.write("\n" + "=" * 70 + "\n\n")
            seq_num += 1

        f.write("=" * 70 + "\n")
        f.write("SECTION 2: OTHER REPEATED SEQUENCES\n")
        f.write("(May need additional return command if extracted)\n")
        f.write("=" * 70 + "\n\n")

        other_sequences = [s for s in sorted_sequences if not s.seq_info.ends_with_return]
        for bank_seq in other_sequences:
            seq_info = bank_seq.seq_info
            f.write(f"SEQUENCE #{seq_num}\n")
            f.write("-" * 40 + "\n")
            f.write(f"Bank: {bank_seq.bank}\n")
            f.write(f"Length: {len(seq_info.command_objects)} commands\n")
            f.write(f"Size: {seq_info.total_bytes} bytes\n")
            f.write(f"Occurrences in bank: {bank_seq.occurrence_count}\n")
            f.write(f"Potential savings: ~{bank_seq.potential_savings} bytes\n\n")

            f.write("Commands:\n")
            for i, cmd in enumerate(seq_info.command_objects, 1):
                f.write(f"  {i}. {format_command_for_display(cmd)}\n")
            f.write("\n")

            f.write("Locations:\n")
            for occ in bank_seq.bank_occurrences[:50]:
                f.write(f"  - {occ.script_name} at index {occ.start_index}\n")
            if len(bank_seq.bank_occurrences) > 50:
                f.write(f"  ... and {len(bank_seq.bank_occurrences) - 50} more locations\n")
            f.write("\n" + "=" * 70 + "\n\n")
            seq_num += 1


def load_scripts_from_bank(bank_module, bank_name: str) -> list[tuple[str, str, list]]:
    """Load all scripts from a bank module.

    Returns list of (script_name, bank_name, commands) tuples.
    """
    scripts = []
    seen_addresses: set[int] = set()

    if hasattr(bank_module, 'scripts') and bank_module.scripts:
        for script in bank_module.scripts:
            if hasattr(script, 'contents'):
                # Get script name from expected_beginning if available
                if hasattr(script, 'expected_beginning'):
                    addr = script.expected_beginning
                    # Skip duplicates (same script referenced multiple times)
                    if addr in seen_addresses:
                        continue
                    seen_addresses.add(addr)
                    name = f"script_0x{addr:06X}.py"
                else:
                    name = f"script_{id(script)}"
                scripts.append((name, bank_name, list(script.contents)))
    return scripts


def main():
    print("Loading battle animation data...")

    # Import the battle animation banks through the proper package system
    from randomizer.data.battle_animation._35.export import bank as bank_35
    from randomizer.data.battle_animation._3A.export import bank as bank_3A
    from randomizer.data.battle_animation._02.export import bank as bank_02

    all_scripts: list[tuple[str, str, list]] = []

    print("Loading bank 0x35...")
    all_scripts.extend(load_scripts_from_bank(bank_35, "0x35"))

    print("Loading bank 0x3A...")
    all_scripts.extend(load_scripts_from_bank(bank_3A, "0x3A"))

    print("Loading bank 0x02...")
    all_scripts.extend(load_scripts_from_bank(bank_02, "0x02"))

    print(f"Loaded {len(all_scripts)} scripts")

    # Analyze each script
    all_sequences: list[dict[tuple, SequenceInfo]] = []

    for i, (script_name, bank_name, commands) in enumerate(all_scripts):
        if (i + 1) % 10 == 0:
            print(f"Processing {i + 1}/{len(all_scripts)}...")

        if commands:
            sequences = find_sequences_in_script(
                commands,
                script_name,
                bank_name,
                min_bytes=3,
                max_length=15
            )
            all_sequences.append(sequences)

    print("Merging sequences...")
    merged = merge_sequences(all_sequences)

    print(f"Found {len(merged)} unique sequences")
    repeated = sum(1 for v in merged.values() if v.occurrence_count >= 2)
    print(f"Of which {repeated} repeat at least twice")

    output_path = Path(__file__).parent / "repeated_sequences_report.txt"
    print(f"Generating report at {output_path}...")
    generate_report(merged, output_path)

    print("Done!")


if __name__ == "__main__":
    main()
