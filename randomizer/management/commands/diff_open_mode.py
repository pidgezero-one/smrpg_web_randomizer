"""Build-diff harness for the open_mode.json deprecation.

Proves a candidate ``asm/*.py`` module reproduces the open_mode.json entries
it is meant to replace (or that ``render()`` already covers a region we want
to drop), by assembling two full seed ROMs and comparing them byte-for-byte:

* **ROM A (current pipeline)** = vanilla + *all* open_mode.json + seed patch.
* **ROM B (future pipeline)**  = vanilla + open_mode.json *minus the entries
  owned by the module/drop-range* + seed patch + the module's ``get_patch()``.

The same ``world.get_patch()`` output is reused for both builds, so any
seed-RNG nondeterminism cancels out exactly — A and B can only differ where
open_mode/module bytes differ. Identical A and B (exit 0) means the swap is
byte-neutral and the JSON entries are safe to retire on the next regeneration.

Patch application order mirrors the live browser path
(``templates/randomizer/_rom_base.html`` fetches open_mode.json as the base,
then applies the per-seed patch over it): load vanilla -> apply open_mode ->
apply seed patch (overrides JSON) -> recompute SNES checksum at 0x7FDC. The
checksum is applied identically to A and B, so it never masks a real diff.

Usage::

    # Verify an ASM keeper module reproduces its open_mode entries:
    patchvenv/bin/python manage.py diff_open_mode \\
        --module randomizer.patches.asm.uncap_coins

    # Verify render() already covers a region (DROP_COVERED check):
    patchvenv/bin/python manage.py diff_open_mode --drop-range 0xE20000 0x29000
"""

import importlib
import json

from django.core.management.base import BaseCommand, CommandError

from randomizer.main import create
from randomizer.types.settings import Settings

OPEN_MODE_PATH = "randomizer/static/randomizer/patches/open_mode.json"
DEFAULT_ROM = "/mnt/d/smrpg.sfc"
DEFAULT_SEED = 20250520  # fixed, nonzero -> deterministic build


def _hexint(value: str) -> int:
    return int(value, 0)


def _load_open_mode() -> list[tuple[int, bytes]]:
    """open_mode.json -> ordered list of (start_offset, bytes)."""
    raw = json.load(open(OPEN_MODE_PATH))
    entries: list[tuple[int, bytes]] = []
    for ele in raw:
        key = list(ele)[0]
        entries.append((int(key), bytes(ele[key])))
    return entries


def _overlaps(a_start: int, a_end: int, b_start: int, b_end: int) -> bool:
    return a_start < b_end and b_start < a_end


def _apply_entries(rom: bytearray, entries: list[tuple[int, bytes]]) -> None:
    for start, data in entries:
        rom[start : start + len(data)] = data


def _apply_patch(rom: bytearray, patch) -> None:
    for addr in patch.addresses:
        data = bytes(patch.get_data(addr))
        rom[addr : addr + len(data)] = data


def _apply_dict(rom: bytearray, data: dict[int, bytes]) -> None:
    for addr, b in data.items():
        b = bytes(b)
        rom[addr : addr + len(b)] = b


def _fix_checksum(rom: bytearray) -> None:
    checksum = sum(rom) & 0xFFFF
    rom[0x7FDC] = (checksum ^ 0xFFFF) & 0xFF
    rom[0x7FDD] = (checksum ^ 0xFFFF) >> 8
    rom[0x7FDE] = checksum & 0xFF
    rom[0x7FDF] = checksum >> 8


def _diff_runs(a: bytearray, b: bytearray) -> list[tuple[int, int]]:
    """Return [(start, length)] runs where a and b differ."""
    runs: list[tuple[int, int]] = []
    n = min(len(a), len(b))
    i = 0
    while i < n:
        if a[i] != b[i]:
            j = i
            while j < n and a[j] != b[j]:
                j += 1
            runs.append((i, j - i))
            i = j
        else:
            i += 1
    if len(a) != len(b):
        runs.append((n, abs(len(a) - len(b))))
    return runs


class Command(BaseCommand):
    help = "Diff-verify an open_mode.json ASM-keeper module or a DROP_COVERED region."

    def add_arguments(self, parser):
        parser.add_argument("--rom", default=DEFAULT_ROM, help="Vanilla ROM path")
        parser.add_argument("--seed", type=int, default=DEFAULT_SEED)
        parser.add_argument(
            "--flags",
            default="",
            help="Flag string for set_from_flag_string(). Empty = defaults "
            "(fine for always-on modules; pass the gating flag otherwise).",
        )
        parser.add_argument(
            "--module",
            default=None,
            help="Dotted path of an asm module exposing get_patch() to verify.",
        )
        parser.add_argument(
            "--module-kwargs",
            default=None,
            help="JSON dict of kwargs passed to the module's get_patch().",
        )
        parser.add_argument(
            "--drop-range",
            nargs=2,
            action="append",
            metavar=("START", "LEN"),
            type=_hexint,
            default=None,
            help="Drop open_mode entries overlapping [START, START+LEN) "
            "with NO replacement (DROP_COVERED render check). Repeatable.",
        )

    def handle(self, *args, **options):
        if not options["module"] and not options["drop_range"]:
            raise CommandError("Pass --module and/or --drop-range.")

        # ---- Resolve the module's patch + write ranges -------------------
        override: dict[int, bytes] = {}
        owned_ranges: list[tuple[int, int]] = []
        if options["module"]:
            mod = importlib.import_module(options["module"])
            kwargs = json.loads(options["module_kwargs"]) if options["module_kwargs"] else {}
            override = {int(k): bytes(v) for k, v in mod.get_patch(**kwargs).items()}
            owned_ranges = [(o, o + len(b)) for o, b in override.items()]
            self.stdout.write(f"Module {options['module']} writes {len(override)} offset(s):")
            for o in sorted(override):
                self.stdout.write(f"  0x{o:06X}  {len(override[o])}B  {override[o].hex(' ')}")

        if options["drop_range"]:
            for start, length in options["drop_range"]:
                owned_ranges.append((start, start + length))
                self.stdout.write(f"Drop-range: 0x{start:06X}..0x{start + length:06X} (no replacement)")

        # ---- Build the seed once (live path: create() -> get_patch()) ----
        s = Settings()
        s.set_from_flag_string(options["flags"])
        self.stdout.write(f"Building world (seed={options['seed']}, flags={options['flags']!r})...")
        world = create(options["seed"], s)
        seed_patch = world.get_patch()

        open_mode = _load_open_mode()

        # ---- Partition open_mode into kept vs dropped --------------------
        kept: list[tuple[int, bytes]] = []
        dropped: list[tuple[int, bytes]] = []
        for start, data in open_mode:
            entry_end = start + len(data)
            if any(_overlaps(start, entry_end, rs, re) for rs, re in owned_ranges):
                dropped.append((start, data))
            else:
                kept.append((start, data))

        self.stdout.write(
            f"open_mode entries: {len(open_mode)} total, {len(dropped)} dropped, {len(kept)} kept"
        )
        for start, data in dropped:
            covered = all(
                any(rs <= off < re for rs, re in owned_ranges)
                for off in range(start, start + len(data))
            )
            flag = "" if covered else "  *** NOT fully covered by replacement ***"
            self.stdout.write(f"  dropped 0x{start:06X} {len(data)}B  {data.hex(' ')}{flag}")

        # ---- Assemble ROM A (current) and ROM B (future) -----------------
        base = bytearray(open(options["rom"], "rb").read())

        rom_a = bytearray(base)
        _apply_entries(rom_a, open_mode)
        _apply_patch(rom_a, seed_patch)
        _fix_checksum(rom_a)

        rom_b = bytearray(base)
        _apply_entries(rom_b, kept)
        _apply_patch(rom_b, seed_patch)
        _apply_dict(rom_b, override)
        _fix_checksum(rom_b)

        # ---- Diff --------------------------------------------------------
        runs = _diff_runs(rom_a, rom_b)
        if not runs:
            self.stdout.write(self.style.SUCCESS(
                "IDENTICAL — ROM A == ROM B. The swap is byte-neutral; "
                "JSON entries are safe to retire."
            ))
            return

        total = sum(length for _, length in runs)
        self.stdout.write(self.style.ERROR(
            f"DIFFER — {len(runs)} run(s), {total} byte(s) differ between A and B:"
        ))
        for start, length in runs[:40]:
            a_bytes = bytes(rom_a[start : start + min(length, 16)]).hex(" ")
            b_bytes = bytes(rom_b[start : start + min(length, 16)]).hex(" ")
            self.stdout.write(f"  0x{start:06X} +{length}: A={a_bytes}  B={b_bytes}")
        if len(runs) > 40:
            self.stdout.write(f"  ... and {len(runs) - 40} more run(s)")
        raise CommandError("ROM A != ROM B (see runs above).")
