"""Expand key item inventory size.

The randomizer increases the key-item inventory capacity beyond vanilla.
That requires updating both the inventory-size byte at three menu sites
($0C305, $0C37F, $0C3B5) and the base-pointer triplets the
menu and load/save code use to address the inventory in WRAM.

The new pointer base is $7FF8F0 (3 bytes: F0 F8 7F); the new size
is 0x1E (30 slots).
"""

_INVENTORY_SIZE = 0x1E

# Three pointer-triplet sites. $0C302 / $0C37C / $0C3B2 are the
# menu-side pointer LSB+MSB pair (no bank byte); $2BC80 /
# $2BC95 / $2BCA1 / $2BCB6 and $35308 are full long
# pointers (LSB MSB BANK).
_PTR_LSBMSB_BYTES = bytes([0xF0, 0xF8])           # SNES low+high bytes of $7FF8F0
_PTR_LONG_BYTES = bytes([0xF0, 0xF8, 0x7F])       # full long pointer


def get_patch() -> dict[int, bytes]:
    """Return the byte writes that expand the key-item inventory."""
    return {
        # Inventory size byte at three sites.
        0xC305: bytes([_INVENTORY_SIZE]),
        0xC37F: bytes([_INVENTORY_SIZE]),
        # TODO might need to be larger than 0x20, recount key items
        0xC3B5: bytes([_INVENTORY_SIZE]),

        # Menu-side 2-byte pointer (LSB, MSB only - bank is implicit).
        0xC302: _PTR_LSBMSB_BYTES,
        0xC37C: _PTR_LSBMSB_BYTES,
        0xC3B2: _PTR_LSBMSB_BYTES,

        # Long pointers (LSB, MSB, bank).
        0x2BC80: _PTR_LONG_BYTES,
        0x2BC95: _PTR_LONG_BYTES,
        0x2BCA1: _PTR_LONG_BYTES,
        0x2BCB6: _PTR_LONG_BYTES,
        0x35308: _PTR_LONG_BYTES,
    }
