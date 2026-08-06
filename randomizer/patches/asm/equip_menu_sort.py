"""Sort the equipment list when the Equip menu opens.

The item menu opens by loading its bag, sorting it, and committing the result::

    $C3:291B  JSR $72E6   ; load items    $7F:F882 -> $7E:2940
    $C3:291E  JSR $2630   ; sort ascending, in place
    $C3:2921  JSR $72FD   ; commit        $7E:2940 -> $7F:F882

The equip menu's open path does only the load::

    $C3:19ED  JSR $7316   ; load equipment $7F:F864 -> $7E:2940
    $C3:19F0  LDA #$05 / STA $94 ...

$7316 has four callers and $C3:19ED is the only one not followed by a
sort, so the equipment bag is ordered only as a side effect of *adding* to it --
which is why it appears to "sort only after you equip something".

The fix redirects that one load into a load-sort-commit helper, mirroring the
item menu exactly. $C3:2630 needs no setup: it initialises $62, $70,
$72, $7E, $60 and $7C before reading any of them. Its only
preconditions -- $2940 populated, 16-bit X, DBR $7E -- already hold at
$C3:19ED, and $732D preserves DBR via PHB/PLB.

The commit is deliberate, not incidental: it makes the new order persist in
$7F:F864 rather than only in the $7E:2940 scratch list, which is what
the item menu does.

Note $C3:2630 also strips and re-appends the Waste Basket sentinel
(#$A0), but only if the list already contains one. Equipment never does, so
sorting the equip list cannot conjure a basket into it.

Always applied; no flag.
"""

# Free space: $C3:F0B0. The $C3:F000-F3FF page is $FF in vanilla;
# unsellable_items owns $F000-$F0A7.
_HELPER = 0xF0B0

# Vanilla routines.
_LOAD_EQUIPMENT = 0x7316  # MVN $7F:F864 -> $7E:2940
_SORT = 0x2630  # selection sort of $7E:2940, ascending
_STORE_EQUIPMENT = 0x732D  # MVN $7E:2940 -> $7F:F864

# The equip-menu open path's JSR $7316, which we redirect.
_OPEN_HOOK = 0x0319ED
_VANILLA_OPEN_BYTES = bytes([0x20, 0x16, 0x73])  # JSR $7316


def _lo(addr: int) -> int:
    return addr & 0xFF


def _hi(addr: int) -> int:
    return (addr >> 8) & 0xFF


def get_patch() -> dict[int, bytes]:
    """Return the byte writes that make the Equip menu sort on open."""
    return {
        0x03F000 + (_HELPER - 0xF000): bytes([
            0x20, _lo(_LOAD_EQUIPMENT), _hi(_LOAD_EQUIPMENT),    # JSR $7316
            0x20, _lo(_SORT), _hi(_SORT),                        # JSR $2630
            0x20, _lo(_STORE_EQUIPMENT), _hi(_STORE_EQUIPMENT),  # JSR $732D
            0x60,                                                # RTS
        ]),

        # JSR $7316 -> JSR helper. Operand-and-opcode, 3 for 3, no padding.
        _OPEN_HOOK: bytes([0x20, _lo(_HELPER), _hi(_HELPER)]),
    }
