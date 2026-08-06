"""Dialogue-font character codes for the Psychopath symbol glyphs.

Psychopath messages are battle dialogs, so they are drawn with the **dialogue**
font (0x37C000, glyph index = code - 0x20). The randomizer adds its own symbol
glyphs to that font -- element/status icons -- in slots vanilla leaves blank.

Four of those slots were a trap. Item names are stored in the *menu* charset,
which puts punctuation at 0x7B-0x7E (! # - '), because ASCII
0x2D/0x27 are the item icon prefixes. Item names are *also* drawn with the
dialogue font -- battle spoils box ("Item / <name>") and [0x70A7] substitution
-- so a hyphenated item drop rendered its hyphen as whatever glyph sat at
0x7D. That was the ice snowflake: "Yoshi-Ade" came out "Yoshi<snowflake>Ade".

The item-name codes are fixed by the game (menu font + Item.render()); the
symbol codes are ours to choose. So the symbols move, and 0x7B-0x7E are
reserved for the punctuation item names need. See
randomizer.patches.asm.dialog_font_item_punctuation, which paints both.

These symbols are a randomizer invention: every code below is a slot the *vanilla*
dialogue font leaves blank. So the randomizer owns them end to end -- the codes
here, the glyphs in randomizer.patches.asm.dialog_font_item_punctuation, and
the text in randomizer/types/enemy.py. smrpgpatchbuilder's BATTLE_CHAR_MAP
is vanilla-only and deliberately does not name them (it used to, pointing at the
pre-relocation codes; removed in 7.1.1).

The extension point is encode_battle_text's ord() fallback: anything not in
BATTLE_CHAR_MAP passes through as its ordinal (valid 32-156), so these are
emitted as raw chr(). The caller owns trimming trailing EMPTY padding --
build_psychopath_text does that; the encoder no longer does.
"""

# Relocated out of 0x7B-0x7E, which item names need for '!' '#' '-' "'".
WEAKNESS = 0x88  # was 0x7B ('{' in BATTLE_CHAR_MAP)
RESISTANCE = 0x89  # was 0x7C ('|' in BATTLE_CHAR_MAP)
ICE = 0x8A  # was 0x7D ('~ice~')
FIRE = 0x8B  # was 0x7E ('~fire~')

# Unchanged: item names never reach these codes. (0x7F is an item *prefix* byte,
# but the name-drawing routine skips byte 0, so it never renders as a glyph.)
THUNDER = 0x7F
SLEEP = 0x80
FEAR = 0x81
MUTE = 0x82
POISON = 0x83
OHKO = 0x84
JUMP = 0x85
EMPTY = 0x8D  # invisible placeholder, trimmed off the end by the encoder

# old dialogue-font code -> new one. Consumed by dialog_font_item_punctuation to
# repaint the glyphs, so the font and this table cannot drift apart.
RELOCATED: dict[int, int] = {
    0x7B: WEAKNESS,
    0x7C: RESISTANCE,
    0x7D: ICE,
    0x7E: FIRE,
}
