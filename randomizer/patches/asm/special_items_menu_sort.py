"""Sort the Special Items (key items) list when its menu opens.

Unlike the item and equipment menus -- which MVN their whole 30-byte bag into
the $7E:2940 scratch list and then JSR $2630 to sort it -- the Special
Items menu builds $2940 by a *filter-copy* and never sorts::

    $C3:52EA  LDA #$FF : STA $2940 : MVN $7E,$7E   ; FF-fill $2940-$294F (16 bytes)
    $C3:5303  LDA #$0F                              ; read 15 key-item slots
    $C3:5307  LDA $7FF8A0,X   (repointed $7FF8F0)   ; a key item
    $C3:530D  BEQ +                                 ; skip $FF gaps
    $C3:530F  STA $2940,Y                           ; pack contiguously
    ...
    $C3:5318  JSR $53E7                             ; draw -- no sort

So key items appear in buffer (insertion) order. This patch inserts the same
$2630 sort the other two menus use, right before the draw.

Two things make it more than a one-line JSR $2630:

1. **Display-only, never commit.** $2940 is a *packed* copy here (gaps
   stripped, only 15 slots read), not a faithful image of the $7F:F8F0 key
   inventory. Committing a sorted $2940 back would corrupt the sparse
   buffer. We sort the scratch copy only; every reopen rebuilds and re-sorts.
   The draw at $C3:53E7 looks every entry up by its id (LDA ($64) ->
   JSR $7A07) and uses no position-indexed parallel array, so reordering
   $2940 alone cannot desync anything.

2. **The FF-fill must cover the whole sort domain.** $2630 sorts 30 bytes
   ($2940-$295D); the vanilla build only FF-fills 16 ($2940-$294F),
   leaving $2950-$295D holding stale bytes from the previous menu. Sorting
   would pull that low-valued garbage into the visible rows. We widen the fill
   from 15 to 29 MVN bytes so all 30 sort slots are real-or-$FF.

$2630 clobbers $60, which $C3:52E5 loaded with a routine pointer
($5D12) the menu still needs, so the helper saves and restores it. X is
16-bit at the hook (verified), and $2630 leaves the index width alone, so
PHX/PLX move the full pointer.

Always applied; no flag.
"""

_HELPER = 0xF0C0  # after equip_menu_sort's $F0B0-$F0B9

_SORT = 0x2630  # selection sort of $7E:2940, ascending
_DRAW = 0x53E7  # the Special Items list draw

# ROM offsets.
_FILL_COUNT = 0x0352F8  # operand of LDA #$000E at $C3:52F7 (MVN byte count)
_DRAW_HOOK = 0x035318  # the JSR $53E7 at $C3:5318

_VANILLA_FILL_COUNT = 0x0E  # fills $2940-$294F (16 bytes)
_FULL_FILL_COUNT = 0x1C  # fills $2940-$295D (30 bytes = the sort domain)
_VANILLA_DRAW_BYTES = bytes([0x20, 0xE7, 0x53])  # JSR $53E7


def _lo(addr: int) -> int:
    return addr & 0xFF


def _hi(addr: int) -> int:
    return (addr >> 8) & 0xFF


def get_patch() -> dict[int, bytes]:
    """Return the byte writes that make the Special Items menu sort on open."""
    return {
        # Widen the FF-fill so the full 30-byte sort domain is real-or-$FF.
        _FILL_COUNT: bytes([_FULL_FILL_COUNT]),

        # JSR $53E7 -> JSR helper (sort, then the original draw).
        _DRAW_HOOK: bytes([0x20, _lo(_HELPER), _hi(_HELPER)]),

        0x03F000 + (_HELPER - 0xF000): bytes([
            0xA6, 0x60,                    # LDX $60      ; save the $5D12 pointer
            0xDA,                          # PHX
            0x20, _lo(_SORT), _hi(_SORT),  # JSR $2630    ; sort $2940 ascending
            0xFA,                          # PLX
            0x86, 0x60,                    # STX $60      ; restore it
            0x20, _lo(_DRAW), _hi(_DRAW),  # JSR $53E7    ; original draw
            0x60,                          # RTS
        ]),
    }
