"""Make the invaded Mushroom Kingdom doorway chest accessible.

Room 325 shares LevelMap 17 / solidity map 5 with room 17. The solidity
mod pointer table starts at 0x1D8DB0 (not 0x1D8DA6); room 325's
mod 0 data lives at 0x1D9823.

Overwrite that 8-byte slot with room 17's doorframe mod (a 2x2 block at
(10, 17) with tile 0xC2). The block size is unchanged.
"""


def get_patch() -> dict[int, bytes]:
    return {
        0x1D9823: bytearray([
            0x0A, 0x11, 0x11, 0xAA, 0xC2, 0xC2, 0xC2, 0xC2,
        ]),
    }
