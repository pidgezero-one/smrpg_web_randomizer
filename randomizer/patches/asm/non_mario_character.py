"""Patches that activate when the protagonist (overworld and/or starter)
is not Mario.

Three independent sites:

* **World map character sprite** (``$3E:90AA``) — picks one of four
  precomputed byte arrays based on which non-Mario ally walks the
  overworld. Used regardless of whether a starter override is in play.

* **File-select character graphic** — when the *starter* (not the
  overworld walker) isn't Mario, eight small writes around
  ``$3:4757-$3:5016`` swap the title-screen / file-select character
  graphic to the alternate protagonist sprite.

* **Overworld walker engine hooks** — when the *overworld walker* isn't
  Mario, two sites:

    - ``$0:9B86`` sets the default sprite base. (Recognition of that
      base by the engine sprite-group whitelist is handled by the
      always-on :mod:`sprite_group_whitelist` patch — this module no
      longer touches the whitelist.)
    - ``$0:94AF`` rewrites the clone-protagonist setup so it copies
      the alternate sprite base instead of zeroing the byte
      (which would force Mario).

* **File select names** — always written, but lives here because it's
  the same character-display group. Each name is 7 bytes, padded with
  ``\\x00``, written at ``$3E:F528 + i*7``.
"""

from typing import Sequence

from randomizer.data.sprites.overworld_map import (
    BOWSER_OVERWORLD,
    GENO_OVERWORLD,
    MALLOW_OVERWORLD,
    TOADSTOOL_OVERWORLD,
)
from randomizer.data.variables.sprite_names import SPR0031_ALT_PROTAGONIST_1


_OVERWORLD_BY_INDEX: dict[int, bytes] = {
    1: TOADSTOOL_OVERWORLD,
    2: BOWSER_OVERWORLD,
    3: GENO_OVERWORLD,
    4: MALLOW_OVERWORLD,
}

# File-select character graphic write sites and their per-site offsets
# from the alternate protagonist sprite base. Mirrors the original
# inline list in gameworld.py.
_STARTER_GRAPHIC_SITES: list[tuple[int, int]] = [
    (0x34757, 1),
    (0x3489A, 2),
    (0x34EE7, 1),
    (0x340AA, 0),
    (0x3501E, 2),
    (0x34D9A, 2),
    (0x3500E, 2),
    (0x35016, 3),
]


def get_patch(
    starter_index: int,
    overworld_index: int,
    file_select_names: Sequence[str],
) -> dict[int, bytes]:
    """Build all character-display patches.

    Args:
        starter_index: Ally index of the run's *starter*. 0 = Mario;
            anything else triggers the file-select graphic swap.
        overworld_index: Ally index of the *overworld walker*. 0 = Mario;
            anything else triggers the world-map sprite + the engine
            hooks.
        file_select_names: List of file-select names to write, one per
            slot.
    """
    out: dict[int, bytes] = {}

    # World map sprite (only when the overworld walker isn't Mario).
    if overworld_index in _OVERWORLD_BY_INDEX:
        out[0x3E90AA] = _OVERWORLD_BY_INDEX[overworld_index]

    # File-select character graphic (driven by the *starter*).
    if starter_index != 0:
        for addr, offset in _STARTER_GRAPHIC_SITES:
            out[addr] = bytes([SPR0031_ALT_PROTAGONIST_1 + offset])

    # Overworld walker engine hooks (driven by the *overworld walker*).
    if overworld_index != 0:
        out[0x9B86] = bytes([SPR0031_ALT_PROTAGONIST_1])

        # Sprite 31 (the alternate-protagonist base) is recognized by the
        # engine sprite-group whitelist via the always-on
        # `sprite_group_whitelist` patch, which fully owns $9BAA-$9BDF.
        # This module must NOT write into that range — it previously
        # cannibalized the Green Yoshi entry there ($9BBF/$9BC1), which
        # broke room 34 Yoshi-riding on every non-Mario seed.

        # Fix clone-protagonist handler at $94AF: set sprite base to
        # protagonist's base instead of hardcoding 0 (Mario).
        # Original: STZ $70; STZ $71; STZ $7F; STZ $1F (8 bytes).
        # New:      LDA #base; STA $70; STZ $71; STZ $1F (8 bytes).
        # $7F is unused by downstream subroutines; $1F is read at $94EE.
        # Note: $F5C0 is a SOUND dispatch routine (not sprite
        # processing). $17BE and $1A56 pass sound command type $00 to
        # play water SFX — do NOT patch those bytes.
        out[0x94AF] = bytes([
            0xA9, SPR0031_ALT_PROTAGONIST_1,  # LDA #$1F
            0x85, 0x70,                        # STA $70
            0x64, 0x71,                        # STZ $71
            0x64, 0x1F,                        # STZ $1F
        ])

        # Clone-protagonist VRAM build-slot. Vanilla $C0:8B6F (`LDA #$04`,
        # operand byte at ROM $8B70) hardcodes the clone-protagonist's slot
        # to 4 — `$70 = $4000 + $19*$40`, so the clone builds at $40:4100.
        # That fits a 4-slot sprite (Mario), but Bowser is a 6-slot sprite
        # (slots 0-5 = $40:4000-$417F), so the clone at slot 4 builds on top
        # of the real protagonist and corrupts every room-load fade-in
        # (self-heals on first movement, which rebuilds only the real one).
        # Move the clone to slot 6 ($40:4180, the free gap above Bowser).
        # Bowser-only: a smaller protagonist genuinely wants slot 4.
        if overworld_index == 2:  # Bowser
            out[0x8B70] = bytes([0x06])

    # File-select names — always written.
    for i, name in enumerate(file_select_names):
        addr = 0x3EF528 + (i * 7)
        out[addr] = name.encode().ljust(7, b"\x00")

    return out
