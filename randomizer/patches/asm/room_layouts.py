"""Room area-layout records for rooms not handled by RoomCollection.render().

Each record is the 18-byte layout written at
``$1D:0040 + room_id * 18``. Byte layout matches LAZYSHELL-UPDATED's
``LevelLayer.cs``::

    0  map ID                                    (MAPS panel)
    1  message box                               (0xFE = NONE; non-zero = ((msg-1)<<1))
    2  mask left (bits 0-6) | lock-scrolling   (bit 7)
    3  mask top
    4  mask right
    5  mask bottom
    6  L2 -X shift
    7  L2 +Y shift
    8  L3 -X shift
    9  L3 +Y shift (bits 0-6) | infinite-scroll (bit 7)
    10 scroll-wrap bits (L1HZ, L1VT, culexA, L2HZ, L2VT, culexB, L3HZ, L3VT)
    11 scroll-sync bits (2 bits per L2HZ / L2VT / L3HZ / L3VT)
    12 L2 auto-scroll (dir bits 3-5, speed bits 0-2, bit 7)
    13 L3 auto-scroll
    14 priority set (bits 0-3) | rippling-water (bit 4)
    15 L3 animation effect
    16 effects-NPC                              (RoomCollection only writes when != 0)

``RoomCollection.render()`` does not touch these records, so they have to
be supplied directly.
"""


def get_patch() -> dict[int, bytes]:
    return {
        # Room 3 — map 107, priority set 10, mask L=40/T=48/R=63/B=63,
        # rippling pond water on L3.
        0x1D0076: bytes([
            0x6B, 0xFE, 0x28, 0x30, 0x3F, 0x3F, 0x00, 0x00,
            0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x0A, 0x05, 0x00,
        ]),
        # Room 4 — map 13, priority set 12, mask L=0/T=0/R=19/B=15,
        # no L3 animation.
        0x1D0088: bytes([
            0x0D, 0xFE, 0x00, 0x00, 0x13, 0x0F, 0x00, 0x00,
            0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x0C, 0x00, 0x00,
        ]),
        # Room 50 — map 79 (same as room 154), priority set 0,
        # mask R=63/B=63, talking organ pipes on L3.
        0x1D03C4: bytes([
            0x4F, 0xFE, 0x00, 0x00, 0x3F, 0x3F, 0x00, 0x00,
            0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x07, 0x00,
        ]),
        # Room 292 — clone of R496's layout (map 145, priority set 1,
        # effects-NPC 0x1B = UNKNOWN_1B). R292 is the
        # post-RunStarPieceSequence half of the R496 ending cutscene; map
        # data is shared with R496. Bytes are R496's vanilla 18-byte
        # record (read from $1D2320) written at R292's offset
        # ($1D14C8 = 0x1D0040 + 292*18). 18 bytes, not 17 — final byte
        # stays 0.
        0x1D14C8: bytes([
            0x91, 0xFE, 0x00, 0x00, 0x3F, 0x3F, 0x00, 0x00,
            0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x01, 0x00, 0x1B, 0x00,
        ]),
        # Room 293 — clone of R268's layout (map 132, mask R=63/B=63,
        # all other fields 0). Bytes are R268's vanilla 18-byte record
        # (read from $1D1318) written at R293's offset
        # ($1D14DA = 0x1D0040 + 293*18).
        0x1D14DA: bytes([
            0x84, 0xFE, 0x00, 0x00, 0x3F, 0x3F, 0x00, 0x00,
            0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
        ]),
    }
