"""ASM patch: preserve invincibility turn timer when healing spells clear
ailments.

Bug
---

The ailment-clearing routine at $C2:C4E1 unconditionally writes
$00 to entity+$43 (the status turn timer). When invincible
(bit 7 of +$40) is still set after ailment clearing, the zeroed
timer causes invincibility to expire on the character's next turn.

Fix
---

After the ailment-clear logic runs (EOR/AND/STA at +$40), check if
bit 7 (invincible) is still set. If so, skip the timer clear to preserve
the remaining invincibility turns.

All code runs in 8-bit accumulator mode (M=1).

Layout
------

Original 6 bytes at ROM $02:C4E1::

    A9 00          LDA #$00
    9F 43 00 7E    STA $7E0043,X    ; unconditionally clear turn timer

Hook: ROM $02:C4E1 - replaces 6 bytes with JSR $FEA5 + 3 NOPs.
Patch: ROM $02:FEA5 (SA-1 $C2:FEA5) - small subroutine.
"""

# Hook at ROM $02C4E1: JSR $FEA5 + 3 NOPs.
_HOOK_OFFSET = 0x02C4E1
_HOOK_BYTES = bytes([0x20, 0xA5, 0xFE, 0xEA, 0xEA, 0xEA])

# Patch routine at ROM $02FEA5 (SA-1 $C2:FEA5), 8-bit accumulator mode.
_PATCH_OFFSET = 0x02FEA5
_PATCH_BYTES = bytes([
    0xBF, 0x40, 0x00, 0x7E,   # LDA $7E0040,X    read current status byte
    0x30, 0x07,               # BMI +7           bit 7 (invincible) set: skip clear
    # Not invincible: clear timer (vanilla behavior).
    0xA9, 0x00,               # LDA #$00
    0x9F, 0x43, 0x00, 0x7E,   # STA $7E0043,X    clear turn timer
    0x60,                     # RTS
    # Invincible: skip timer clear, return.
    0x60,                     # RTS
])


def get_patch() -> dict[int, bytes]:
    """Return the hook + patch bytes for the FixInvincibility flag."""
    return {
        _HOOK_OFFSET: _HOOK_BYTES,
        _PATCH_OFFSET: _PATCH_BYTES,
    }
