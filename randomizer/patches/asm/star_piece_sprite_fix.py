"""Fix the hardcoded sprite in ending star-piece sequence #8.

The credits cutscene at ``$C3:5516`` originally does
``LDX #$0184; STX $74`` to load sprite ``$0184`` (388). In v9 sprite 388
moved into the enemy-reserved range and now renders Poundette. Redirect
the load to sprite 725 (Geno Redemption), which is the intended visual.

Patches the 2-byte LDX immediate operand at ROM ``$03:5517``.

Also relocates the level-up "choose a bonus" screen sprites. Those seven
sprites were moved out of slots 225/227-232 into 829-835 (see
``sprite_names.py``, ``npcs.py``, ``packets.py`` and ``sprite_829``-``835.py``).
The level-up display lists in bank ``$C2`` still draw the old slot numbers as
hardcoded ``81`` sprite-draw command operands, so repoint each operand to its
new slot. Each offset below is a 16-bit little-endian sprite-ID word (the
``81 2X`` draw-command operand), located by ASM trace:
``$C2:DE94`` (level-up object builder) -> ``$C2:E574`` (object loader)
-> master table ``$C2:E654[9]`` = ``$C2:E703`` -> ``81`` draw commands.
"""

from randomizer.data.variables.sprite_names import (
    SPR0725_GENO_REDEMPTION,
    SPR0829_LEVEL_UP_BONUS_SELECTION_BOX,
    SPR0830_LIGHT_GREEN_PIPE_TOP_EDGE,
    SPR0831_LEVEL_UP_BONUS_TEXT,
    SPR0832_LEVEL_UP_BONUS_FLOWER,
    SPR0833_LEVEL_UP_BONUS_POW_POWER,
    SPR0834_LEVEL_UP_BONUS_STAR_MAGIC,
    SPR0835_LEVEL_UP_BONUS_HP,
)


def _le16(value: int) -> bytes:
    """Encode a sprite ID as a 2-byte little-endian word."""
    return bytes([value & 0xFF, (value >> 8) & 0xFF])


# ROM offset of each hardcoded level-up-bonus sprite-draw operand -> new sprite.
# Old slot at each offset (vanilla) is shown for reference.
_LEVELUP_BONUS_SPRITE_REFS: dict[int, int] = {
    0x02E900: SPR0829_LEVEL_UP_BONUS_SELECTION_BOX,   # was 225
    0x02E958: SPR0829_LEVEL_UP_BONUS_SELECTION_BOX,   # was 225
    0x02E7CB: SPR0830_LIGHT_GREEN_PIPE_TOP_EDGE,      # was 227
    0x02E763: SPR0831_LEVEL_UP_BONUS_TEXT,            # was 228
    0x02E775: SPR0832_LEVEL_UP_BONUS_FLOWER,          # was 229
    0x02E7DD: SPR0833_LEVEL_UP_BONUS_POW_POWER,       # was 230
    0x02E91B: SPR0833_LEVEL_UP_BONUS_POW_POWER,       # was 230
    0x02E80D: SPR0834_LEVEL_UP_BONUS_STAR_MAGIC,      # was 231
    0x02E930: SPR0834_LEVEL_UP_BONUS_STAR_MAGIC,      # was 231
    0x02E821: SPR0835_LEVEL_UP_BONUS_HP,              # was 232
    0x02E944: SPR0835_LEVEL_UP_BONUS_HP,              # was 232
}


def get_patch() -> dict[int, bytes]:
    patch: dict[int, bytes] = {
        0x035517: _le16(SPR0725_GENO_REDEMPTION),
    }
    for offset, sprite_id in _LEVELUP_BONUS_SPRITE_REFS.items():
        patch[offset] = _le16(sprite_id)
    return patch
