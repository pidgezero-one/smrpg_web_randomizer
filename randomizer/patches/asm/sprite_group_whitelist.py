"""Restore the Green Yoshi entry in the engine sprite-group whitelist.

The overworld engine keeps a hardcoded whitelist of "base" sprite IDs as
an inline ``CMP``/``BEQ`` chain at ``$00:9BAA``. When a room loads a sprite
whose ID is on the list, the engine builds a run of *additional sprites*
in VRAM for it (extra pose / jump / riding banks); action-script
``SetSpriteSequence``'s ``sprite_offset`` then indexes into that run.

Vanilla whitelists sprite ``$31`` (49 = Green Yoshi) — the Yoster Isle
Yoshi-riding minigame in room 34 depends on it. :mod:`non_mario_character`
also needs the alternate-protagonist base (sprite 31) whitelisted, and
originally got it by *overwriting* the Green Yoshi entry
(``CMP #$31`` -> ``CMP #$1F``). That silently broke Yoshi-riding on every
non-Mario seed (jump -> garbage VRAM read -> softlock / black screen).

The inline chain has no spare slot for a 7th entry, so this patch
relocates the comparison + dispatch logic. ``$9BAA`` becomes a
``JMP $9BAD`` into a rewritten routine that fits in the 54 bytes the old
chain vacated (``$9BAA-$9BDF``) and recognizes every vanilla entry *plus*
sprite 31. The ``$9BE0`` build loop and ``$9BED`` RTS are untouched.

Always applied — the routine is a strict superset of vanilla behavior.
This patch fully owns ``$9BAA-$9BDF``; :mod:`non_mario_character` must NOT
also write ``$9BBF`` / ``$9BC1`` (those bytes are now inside this routine).
"""

from randomizer.data.variables.sprite_names import (
    SPR0031_ALT_PROTAGONIST_1,
    SPR0049_GREEN_YOSHI,
)


def get_patch() -> dict[int, bytes]:
    """Return the relocated sprite-group whitelist routine.

    54 bytes overwriting ``$9BAA-$9BDF``. Branch displacements are
    position-fixed for this exact layout — do not reorder or resize.
    """
    return {
        0x009BAA: bytes([
            0x4C, 0xAD, 0x9B,                              # 9BAA  JMP  $9BAD
            0xA5, 0x70,                                    # 9BAD  LDA  $70
            0xF0, 0x1E,                                    # 9BAF  BEQ  $9BCF  ; 0  -> count 6 (Mario block)
            0xC9, SPR0031_ALT_PROTAGONIST_1, 0xF0, 0x1A,   # 9BB1  CMP #31 / BEQ $9BCF  ; alt protagonist -> count 6
            0xC9, 0x07, 0xF0, 0x12,                        # 9BB5  CMP #$07 / BEQ $9BCB ; -> count 5
            0xC9, 0x0D, 0xF0, 0x0E,                        # 9BB9  CMP #$0D / BEQ $9BCB
            0xC9, 0x13, 0xF0, 0x0A,                        # 9BBD  CMP #$13 / BEQ $9BCB
            0xC9, 0x19, 0xF0, 0x06,                        # 9BC1  CMP #$19 / BEQ $9BCB
            0xC9, SPR0049_GREEN_YOSHI, 0xF0, 0x0A,         # 9BC5  CMP #49 / BEQ $9BD3  ; Green Yoshi
            0x80, 0x22,                                    # 9BC9  BRA  $9BED  ; no match -> RTS
            0xA9, 0x05, 0x80, 0x11,                        # 9BCB  LDA #$05 / BRA $9BE0  (count 5)
            0xA9, 0x06, 0x80, 0x0D,                        # 9BCF  LDA #$06 / BRA $9BE0  (count 6)
            0xA9, 0x32, 0x85, 0x70,                        # 9BD3  LDA #$32 / STA $70   (Green Yoshi: base -> 50)
            0xA9, 0x02, 0x80, 0x05,                        # 9BD7  LDA #$02 / BRA $9BE0  (count 2)
            0xEA, 0xEA, 0xEA, 0xEA, 0xEA,                  # 9BDB  padding (unused)
        ]),
    }
