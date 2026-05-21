"""Force a menu item always-available (open-mode base).

``$C3:15B7``: ``BNE`` -> ``BRA``. The menu code scans a 4-byte BW-RAM
presence/availability bitfield at ``$40:30E3`` (``LDA $4030E3,X`` / ``BNE`` /
loop x4) and branches to the "present/found" path on any nonzero entry. Forcing
that branch unconditional makes the menu item always treated as available (the
all-zero fallthrough path becomes dead). Render-disjoint engine code relocated
from open_mode.json (verified byte-identical via ``diff_open_mode``).
"""


def get_patch() -> dict[int, bytes]:
    return {
        0x315B7: bytes([0x80]),
    }
