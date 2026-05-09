"""Force room 174 (sea shore w/ sunken ship) to use the Sea Enclave battlefield.

The level→battlefield path goes LevelMap.battlefield_byte → "Battlefield Sets
by Area" table at ``$39BA44`` (64 sets x 4 bytes). For BattlePackNPC
collisions the engine indexes one of slots 1-3 of the set, never slot 0.
Room 174's vanilla LevelMap (25) points to area 9 = ``[22 26 26 26]``, so
slot 0 is Sea Enclave (BF34) but the BLOOBER pack collision returns Sea
(BF38) from slot 1+.

Editing area 9 directly would also affect every other room pointed at it.
LevelMap 25 itself is shared with room 219 (the intro shore). To isolate
the change to room 174, the patch carves a fresh area-table slot, copies
LevelMap 25 into a free LevelMap slot pointing at it, and repoints room
174 alone at the duplicate.

Three writes, all into otherwise-unreferenced bytes:

* ``$39BA84`` (4 bytes) - area-table slot 16 was leftover Bowser's Keep
  (``07 07 07 07``) and unreferenced by any LevelMap. Set to
  ``22 22 22 22`` so every selector slot resolves to BF34 Sea Enclave.
* ``$1D247C`` (15 bytes) - LevelMap 4 was unreferenced junk. Overwritten
  with a byte-for-byte copy of LevelMap 25, except byte 14 (battlefield)
  is ``0x10`` (= area 16) instead of ``0x09`` (= area 9).
* ``$1D0C7C`` (1 byte) - level 174's LevelMap pointer (byte 0 of its
  18-byte struct at ``$1D0040 + 174*18``) flipped from ``0x19`` to
  ``0x04``. Room 219 still reads ``0x19`` and behaves as before.

After the patch any battle started in room 174 - BattlePackNPC collisions
or anything else routed through the area table - resolves to BF34
Sea Enclave.
"""


_LEVELMAP_25_BYTES = bytes([
    0x6A, 0x35, 0x4B, 0x53, 0x54, 0x1F, 0xA0, 0x3C,
    0x3D, 0x3C, 0x1B, 0x07, 0x07, 0x4B, 0x09,
])
_NEW_LEVELMAP_BYTES = _LEVELMAP_25_BYTES[:14] + bytes([0x10])


def get_patch() -> dict[int, bytes]:
    return {
        0x39BA84: bytes([0x22, 0x22, 0x22, 0x22]),
        0x1D247C: _NEW_LEVELMAP_BYTES,
        0x1D0C7C: bytes([0x04]),
    }
