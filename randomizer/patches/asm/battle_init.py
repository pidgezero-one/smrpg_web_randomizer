"""Battle init: copy overworld party count to battle party size.

Replaces the linear zero-fill block at $C2:A2BD (vanilla = 8
individual STA $7EE0xx instructions, 39 bytes) with a tight zero-fill
loop followed by an explicit copy of the overworld party count
($00:303F) into the battle party-size byte ($00:0926).

Patches a single contiguous 39-byte block at ROM $02:A2BD (SNES
$C2:A2BD) - the new code is 31 bytes plus 8 NOP bytes of padding so
the routine fits in the same footprint. Trailing fall-through to vanilla
code at $C2:A2E4 is unchanged.
"""

_ROUTINE_OFFSET = 0x02A2BD
_ROUTINE_BYTES = bytes([
    0xA9, 0x00, 0x00,        # LDA #$0000
    0x8D, 0x24, 0x07,        # STA $0724
    0xA2, 0x00, 0x00,        # LDX #$0000
    0x9F, 0x00, 0xE0, 0x7E,  # STA $7EE000,x   (loop body)
    0xE8,                    # INX
    0xE8,                    # INX
    0xE0, 0x10, 0x00,        # CPX #$0010
    0x90, 0xF5,              # BCC loop
    0xE2, 0x20,              # SEP #$20
    0xAD, 0x3F, 0x30,        # LDA $303F      (overworld party count)
    0x8D, 0x26, 0x09,        # STA $0926      (battle party size)
    0xC2, 0x20,              # REP #$20
    0x60,                    # RTS
    0xEA, 0xEA, 0xEA, 0xEA,  # NOP padding
    0xEA, 0xEA, 0xEA, 0xEA,
])


def get_patch() -> dict[int, bytes]:
    return {_ROUTINE_OFFSET: _ROUTINE_BYTES}
