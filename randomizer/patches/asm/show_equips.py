"""ShowEquips: relax the equipped-item bitmask check so the menu shows
which items are equipped on each character.

Replaces 3 bytes at ROM ``$03:3B6D`` — the mask byte changes from the
vanilla value to ``$1F`` and the trailing instruction becomes ``NOP``::

    AND #$1F   ; widen the mask
    NOP        ; eat the displaced byte
"""


def get_patch() -> dict[int, bytes]:
    return {0x033B6D: bytes([0x29, 0x1F, 0xEA])}
