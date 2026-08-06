"""UncapCoins: lift the 999 cap on the current-coins counter to 9999, and
widen the X-menu coin display to 4 digits to match.

Reproduces the legacy open_mode.json coin-cap + coin-display edits so the
JSON entries can be retired. Always applied (the legacy base patch raised the
cap and widened the display unconditionally for every seed). All bytes match
the JSON entries EXCEPT storage site 4 (the Moleville minecart cash-out),
which the JSON never touched - so diff_open_mode reports that one clamp as
an intentional extra edit. Everything else is a pure relocation for
traceability.

This is the coin analogue of :mod:uncap_max_fp, which bundles the FP cap with
its display widening the same way.

STORAGE - coin clamp 999 -> 9999
--------------------------------
Vanilla clamps the current-coins value (WRAM $7F:F8AF, 2 bytes) to 999
($03E7) in every routine that adds coins. Each site has the shape::

    LDA $7FF8AF        ; current coins
    CLC / ADC <delta>  ; add the coins being awarded
    CMP #$03E7         ; >= 999 ?            <-- operand patched to #$270F
    BCC/BMI +3         ; if below the cap, keep the sum
    LDA #$03E7         ; else clamp to 999   <-- operand patched to #$270F
    STA $7FF8AF        ; store back

The 7-byte patched window spans the CMP operand through the LDA
operand, swapping both immediates to #$270F (9999). Confirmed against the
RAM map ($7F:F8AF = Current Coins; $7E:FA04 = coins gained from battle)
and a vanilla disassembly of /mnt/d/smrpg.sfc:

1. $C0:C443 (file 0x0C443) - overworld/event add-coins handler (delta
   = event amount in dp $70).  E7 03 90 03 A9 E7 03 -> 0F 27 90 03 A9 0F 27
2. $C2:9319 (file 0x29319) - battle-reward add (delta = 2 x $7E:FA04;
   BMI variant).  E7 03 30 03 A9 E7 03 -> 0F 27 30 03 A9 0F 27
3. $C3:3F03 (file 0x33F03) - X-menu add (delta = $0947; vanilla
   CMP #$03E8).  E8 03 90 03 A9 E7 03 -> 0F 27 90 03 A9 0F 27
4. $C3:AE73 (file 0x3AE74) - Moleville Mountain minecart cash-out
   (delta = $0A0B, the ride's collected-coin counter: STZ at start
   $C3:93BD, INC per pickup $C3:B432, LDA + clamp-add here).
   Vanilla CMP #$03E8 like the X-menu site:
   E8 03 90 03 A9 E7 03 -> 0F 27 90 03 A9 0F 27.  This site was NOT in
   the legacy open_mode.json clamp set, so vanilla/legacy both reset any
   >999 total down to 999 after the ride - a real bug, fixed here.

DISPLAY - X-menu coin field widened (one extra digit)
-----------------------------------------------------
With the cap at 9999 the X-menu coin counter needs a 4th digit. At each coin
render site the destination tilemap pointer (a 16-bit LDX #$43xx/#$44xx
stored to the converter cursor $62) shifts 2 bytes / 1 tile left, and the
digit converter JSR $78F8 swaps to the wider JSR $7902 (both are
PHP/SEP #$20/JSR $795D/... converter stubs that differ in digit count).
This mirrors :mod:uncap_max_fp's $78D2 -> $78EC widening. Sites
(raw file offsets; only the listed bytes change vs vanilla, the rest of each
window is rewritten identically to vanilla):

4. $C3:3AFC - LDX #$4318->#$4316 / STX $62 / JSR $78F8->$7902 /
   LDX #$4318->#$4316 (two coin groups).
5. $C3:3B0E - JSR $78F8 -> $7902 operand.
6. $C3:3F6E - LDX #$4318->#$4316 / STX $62 / JSR $78F8->$7902.
7. $C3:3FA1 - LDX #$4418 -> #$4416 operand low byte.
8. $C3:3FB0 - JSR $78F8 -> $7902 operand.
"""


def get_patch() -> dict[int, bytes]:
    return {
        # === Storage: coin clamp 999 -> 9999 ($7F:F8AF) ===
        # $C0:C443 - overworld/event add-coins clamp
        0x0C443: bytes([0x0F, 0x27, 0x90, 0x03, 0xA9, 0x0F, 0x27]),
        # $C2:9319 - battle-reward add-coins clamp (BMI variant)
        0x29319: bytes([0x0F, 0x27, 0x30, 0x03, 0xA9, 0x0F, 0x27]),
        # $C3:3F03 - X-menu add-coins clamp (vanilla CMP #$03E8)
        0x33F03: bytes([0x0F, 0x27, 0x90, 0x03, 0xA9, 0x0F, 0x27]),
        # $C3:AE73 - Moleville minecart cash-out clamp (vanilla CMP #$03E8);
        # not in legacy open_mode.json, so it reset >999 totals to 999.
        0x3AE74: bytes([0x0F, 0x27, 0x90, 0x03, 0xA9, 0x0F, 0x27]),

        # === Display: X-menu coin field widened by one digit ===
        # LDX #$4316 / STX $62 / JSR $7902 / LDX #$4316
        0x33AFC: bytes([0x16, 0x43, 0x86, 0x62, 0x20, 0x02, 0x79, 0xA2, 0x16]),
        # JSR $78F8 -> $7902
        0x33B0E: bytes([0x02, 0x79]),
        # LDX #$4316 / STX $62 / JSR $7902
        0x33F6E: bytes([0x16, 0x43, 0x86, 0x62, 0x20, 0x02, 0x79]),
        # LDX #$4418 -> #$4416 (low byte)
        0x33FA1: bytes([0x16]),
        # JSR $78F8 -> $7902
        0x33FB0: bytes([0x02, 0x79]),
    }
