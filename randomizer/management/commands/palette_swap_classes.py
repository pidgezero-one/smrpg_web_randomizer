"""Generate randomizer/data/sprites/palette_swap_classes.py.

Two sprites belong to the same palette-swap class when their definitions are
byte-identical once palette_offset is stripped. Such sprites share tile data
outright, so they can share one VRAM clone buffer -- a buffer holds exactly one
sprite_id, and that is the constraint forcing extra NPCs into dedicated VRAM.

Sprites with no graphics, or with palette SPAL000_NOTHING, are excluded. They are
placeholder records (the protagonist-remap slots, the ally slots) whose files are
identical to each other for reasons that have nothing to do with recolouring.

Run: patchvenv/bin/python manage.py palette_swap_classes
"""
import collections
import hashlib
import pathlib
import re

from django.core.management.base import BaseCommand

SPRITE_DIR = pathlib.Path("randomizer/data/sprites/objects")
OUTPUT = pathlib.Path("randomizer/data/sprites/palette_swap_classes.py")

_OFFSET = re.compile(r"palette_offset=(\d+)")
_PALETTE = re.compile(r"palette_id=(\w+)")
_TILE = re.compile(r"\bTile\(")
_MOLD = re.compile(r"\bMold\(")


def _scan() -> dict[int, tuple[str, int]]:
    """sprite_id -> (hash of definition without palette_offset, palette_offset)."""
    found: dict[int, tuple[str, int]] = {}
    for path in SPRITE_DIR.glob("sprite_*.py"):
        match = re.search(r"sprite_(\d+)", path.name)
        if match is None:
            continue
        text = path.read_text()
        offset = _OFFSET.search(text)
        palette = _PALETTE.search(text)
        if offset is None or palette is None:
            continue
        if palette.group(1) == "SPAL000_NOTHING":
            continue
        if not _TILE.search(text) or not _MOLD.search(text):
            continue
        body = "\n".join(
            line
            for line in text.splitlines()
            if "palette_offset=" not in line and not line.startswith("#")
        )
        found[int(match.group(1))] = (
            hashlib.sha1(body.encode()).hexdigest(),
            int(offset.group(1)),
        )
    return found


def build_tables() -> tuple[dict[int, int], dict[int, tuple[int, int]]]:
    """Return (PURE, SHIFTED). Canonical member of a class is its lowest id."""
    scanned = _scan()
    groups: dict[str, list[int]] = collections.defaultdict(list)
    for sprite_id, (digest, _) in scanned.items():
        groups[digest].append(sprite_id)

    pure: dict[int, int] = {}
    shifted: dict[int, tuple[int, int]] = {}
    for members in groups.values():
        if len(members) < 2:
            continue
        # Canonical must be the member with the LOWEST palette_offset, not the
        # lowest sprite id. palette_offset is a property of the SPRITE, so every
        # object merged onto the canonical inherits the canonical's offset as its
        # baseline, and A_IncPaletteRowBy can only increment. A canonical sitting
        # above another member would need a negative bump, which cannot be
        # expressed -- that object would render in the canonical's colour instead.
        # Ties break on sprite id so the result stays deterministic.
        members.sort(key=lambda sprite_id: (scanned[sprite_id][1], sprite_id))
        canonical = members[0]
        canonical_offset = scanned[canonical][1]
        for sprite_id in members[1:]:
            offset = scanned[sprite_id][1]
            if offset == canonical_offset:
                pure[sprite_id] = canonical
            else:
                shifted[sprite_id] = (canonical, offset)
    return dict(sorted(pure.items())), dict(sorted(shifted.items()))


HEADER = '''"""Palette-swap equivalence classes. GENERATED -- do not edit by hand.

Regenerate with: patchvenv/bin/python manage.py palette_swap_classes
Drift is caught by .claude/tests/test_palette_swap_classes.py

PURE:    sprite_id -> canonical_sprite_id
         Same palette_offset. Merging is a sprite-id override and nothing else.
SHIFTED: sprite_id -> (canonical_sprite_id, pack_offset)
         Merging additionally needs palette residency plus an A_IncPaletteRowBy
         bump.
"""
'''


class Command(BaseCommand):
    help = "Generate the palette-swap equivalence class table."

    def handle(self, *args, **options):
        pure, shifted = build_tables()
        lines = [HEADER, "", "PURE: dict[int, int] = {"]
        for sprite_id, canonical in pure.items():
            lines.append(f"    {sprite_id}: {canonical},")
        lines.append("}")
        lines.append("")
        lines.append("SHIFTED: dict[int, tuple[int, int]] = {")
        for sprite_id, (canonical, offset) in shifted.items():
            lines.append(f"    {sprite_id}: ({canonical}, {offset}),")
        lines.append("}")
        lines.append("")
        OUTPUT.write_text("\n".join(lines))
        self.stdout.write(
            f"wrote {OUTPUT}: {len(pure)} pure, {len(shifted)} shifted"
        )
