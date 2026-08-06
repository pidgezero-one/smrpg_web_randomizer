"""Show free space in each script of the 0x3A battle animation bank."""

from django.core.management.base import BaseCommand

from randomizer.data.battle_animation._3A.export import bank
from smrpgpatchbuilder.datatypes.battle_animation_scripts.types import AnimationScriptBlock

def main():
    scripts = [s for s in bank.scripts if isinstance(s, AnimationScriptBlock)]

    print(f"0x3A Bank - Free space per script ({len(scripts)} scripts):")
    print("=" * 80)
    print(f"{'Address':<12} {'Expected':>10} {'Used':>10} {'Free':>10} {'%Free':>8}")
    print("-" * 80)

    total_expected = 0
    total_used = 0
    total_free = 0

    scripts_with_space = []

    for script in sorted(scripts, key=lambda s: s.expected_beginning):
        expected = script.expected_size
        used = script.get_rendered_size()
        free = expected - used
        pct_free = (free / expected * 100) if expected > 0 else 0

        total_expected += expected
        total_used += used
        total_free += free

        print(f"0x{script.expected_beginning:06X}  {expected:>10,}  {used:>10,}  {free:>10,}  {pct_free:>7.1f}%")

        if free > 0:
            scripts_with_space.append((script.expected_beginning, free))

    print("-" * 80)
    print(f"{'TOTAL':<12} {total_expected:>10,}  {total_used:>10,}  {total_free:>10,}  {(total_free/total_expected*100):>7.1f}%")

    # Show contiguous ranges that could be combined
    print("\n" + "=" * 80)
    print("Scripts with free space (sorted by free space, descending):")
    print("-" * 80)

    for addr, free in sorted(scripts_with_space, key=lambda x: -x[1]):
        print(f"0x{addr:06X}: {free:,} bytes free")

    # Calculate potential AnimationBank space if last scripts were consolidated
    print("\n" + "=" * 80)
    print("Contiguous unused space at end of bank:")
    print("-" * 80)

    # Find the last script end address
    last_script = max(scripts, key=lambda s: s.expected_beginning)
    last_end = last_script.expected_beginning + last_script.expected_size
    bank_end = 0x3B0000

    contiguous_at_end = bank_end - last_end
    print(f"Last script ends at: 0x{last_end:06X}")
    print(f"Bank ends at: 0x{bank_end:06X}")
    print(f"Contiguous space at end: {contiguous_at_end:,} bytes")


class Command(BaseCommand):
    help = 'Show free space in each script of the 0x3A battle animation bank.'

    def handle(self, *args, **options):
        main()
