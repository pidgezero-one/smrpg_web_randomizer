"""Reserve dialogue-font codes 0x7B-0x7E for the punctuation item names encode.

Item names are stored in the *menu* charset, which parks four punctuation marks at
codes ASCII cannot reach -- ASCII 0x2D and 0x27 are the consumable / weapon icon
prefixes, and byte 0 of every name is that prefix::

    0x7B = '!'   0x7C = '#'   0x7D = '-'   0x7E = "'"

The menu font and the description font both draw those glyphs. The *dialogue* font
does not -- vanilla leaves codes 0x7B-0x7F blank, width 0. That is a latent vanilla
bug, because item names are also drawn with the dialogue font: by the battle spoils
box ("Item / <name>") and by the ``[0x70A7]`` dialog substitution. Vanilla never
trips it -- no vanilla enemy drops a hyphenated or apostrophe'd item, so "Yoshi-Ade"
/ "B'tub Ring" / "Lamb's Lure" never reach those code paths.

The randomizer trips it. It shuffles drops, so Yoshi-Ade *can* be an enemy drop; and
it fills dialogue codes 0x7B-0x85 (via ``static_data.bin``) with the Psychopath
element/status symbols. Codes 0x7B-0x7E carried the weakness / resistance / ice /
fire symbols -- exactly the four an item name needs. A Yoshi-Ade drop rendered
"Yoshi<snowflake>Ade": the hyphen hit the ice symbol.

Both readings of those codes are load-bearing, so one has to move. The item-name
codes are fixed by the game (menu font + ``Item.render()``); the Psychopath codes are
the randomizer's own choice. So this module:

* repaints 0x7B-0x7E with the punctuation glyphs the dialogue font already carries
  elsewhere (0x21 ``!``, 0x93 ``#``, 0x2D ``-``, 0x27 ``'``), and
* repaints the four displaced symbols at 0x88-0x8B, which vanilla leaves blank and
  nothing else claims.

``psychopath_symbols.RELOCATED`` drives both halves, and
``randomizer/types/enemy.py`` emits the new codes, so the font and the text cannot
drift apart. ``static_data.py`` excludes 0x7B-0x7E: its stale symbol bytes sit at
*higher* offsets and would otherwise win the address-ordered apply.
"""

from randomizer.data.variables.psychopath_symbols import RELOCATED

# Dialogue font: glyph index = character code - 0x20. Graphics are 0x30 bytes each
# (two 8x12 halves, 2bpp planar); widths are one byte each.
_GFX_BASE = 0x37C000
_WIDTH_BASE = 0x249280
_GLYPH_SIZE = 0x30

# Only the codes static_data.bin also writes need excluding from it; the relocation
# targets (0x88-0x8B) are vanilla blanks the blob does not carry.
GFX_RANGE = (
    _GFX_BASE + (min(RELOCATED) - 0x20) * _GLYPH_SIZE,
    _GFX_BASE + (max(RELOCATED) + 1 - 0x20) * _GLYPH_SIZE,
)
WIDTH_RANGE = (
    _WIDTH_BASE + min(RELOCATED) - 0x20,
    _WIDTH_BASE + max(RELOCATED) + 1 - 0x20,
)

# character code -> (width, 0x30 bytes of 2bpp graphics)

# Punctuation, painted into the codes item names encode.
_PUNCTUATION: dict[int, tuple[int, bytes]] = {
    # '!' -- copy of dialogue code 0x21
    0x7B: (0x06, bytes.fromhex(
        "00001800102030002000200000002050"
        "70006000000000000000000000000000"
        "00000000000000000000000000000000"
    )),
    # '#' -- copy of dialogue code 0x93
    0x7C: (0x09, bytes.fromhex(
        "0000120012007f0024002400fe004800"
        "48004800000000000000000000000000"
        "00000000000000000000000000000000"
    )),
    # '-' -- copy of dialogue code 0x2D
    0x7D: (0x05, bytes.fromhex(
        "00000000000000000000f00000000000"
        "00000000000000000000000000000000"
        "00000000000000000000000000000000"
    )),
    # "'" -- copy of dialogue code 0x27
    0x7E: (0x04, bytes.fromhex(
        "20002040402040000000000000000000"
        "00000000000000000000000000000000"
        "00000000000000000000000000000000"
    )),
}

# The Psychopath symbols those codes used to hold, moved out of the way.
_SYMBOLS: dict[int, tuple[int, bytes]] = {
    # weakness symbol -- was dialogue code 0x7B
    0x88: (0x0D, bytes.fromhex(
        "000038007c00ee00c600c6000e001c00"
        "38007000fe00fe000000000000000000"
        "00000000000088005000200050008800"
    )),
    # resistance symbol -- was dialogue code 0x7C
    0x89: (0x0D, bytes.fromhex(
        "000038007c00ee00c600c600c600c600"
        "c600ee007c0038000000000000000000"
        "00000000000088005000200050008800"
    )),
    # ice symbol -- was dialogue code 0x7D
    0x8A: (0x0D, bytes.fromhex(
        "000088006700520027008a007f008a00"
        "27005200670088000000880030005000"
        "20008800f00088002000500030008800"
    )),
    # fire symbol -- was dialogue code 0x7E
    0x8B: (0x0E, bytes.fromhex(
        "88448864e8060f008340826dce31fa01"
        "6310601838071f00040844984c90cc00"
        "ec006000244834081c6038406080e000"
    )),
}


def get_patch() -> dict[int, bytes]:
    patch: dict[int, bytes] = {}
    for code, (width, graphics) in {**_PUNCTUATION, **_SYMBOLS}.items():
        index = code - 0x20
        patch[_GFX_BASE + index * _GLYPH_SIZE] = graphics
        patch[_WIDTH_BASE + index] = bytes([width])
    return patch
