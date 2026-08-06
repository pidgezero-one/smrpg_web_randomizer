"""Battle attack-attribute system edits (open-mode base).

Render-disjoint battle-engine ($C2) edits relocated from open_mode.json
(verified byte-identical via diff_open_mode).

- $C2:BDE9: in the spell/item attribute-descriptor builder ($C2:BDC2+),
  the status mask AND #$EF -> AND #$FF (the bank-$C2 trace comment reads
  "change to FF to include *confuse"). Preserves bit 4 ($10) so the
  confuse/fear ailment bit is no longer masked off and that status can apply.
- $C2:F96F / $C2:F988: the adjacent attack-attribute/element data table
  ($C2:F96F-F9A5, DATA) - one entry removed and its three little-endian
  pointers decremented by 1 to stay consistent with the shortened data.
"""


def get_patch() -> dict[int, bytes]:
    return {
        0x2BDE9: bytes([0xFF]),
        0x2F96F: bytes([0x8F, 0xF9, 0x94, 0xF9, 0x9B]),
        0x2F988: bytes([
            0x06, 0x01, 0x0F, 0x0C, 0x06, 0x11, 0x1A, 0x04, 0x0E, 0x0D, 0x04,
            0x02, 0x06, 0x06, 0x00, 0x06, 0x08, 0x0D, 0x1A, 0x06, 0x0B, 0x12,
            0x04, 0x0A, 0x18, 0x1A,
        ]),
    }
