"""Battle-intro HDMA ordering fix - eliminate the neon-block glitch.

Symptom
-------
When a battle begins, background objects show neon-coloured blocks around
their edges for the whole intro; it clears the instant the player presses
a command button. Severity is monster-pack dependent. The same root cause
also corrupts the in-battle command/target selection dialog.

Root cause
----------
The battle screen is built by a chain of HDMA channels, enabled through
the HDMAEN shadow $00:0401 (the NMI copies it to $420C):

* ch1 -> $2121 CGADD, ch2 -> $2122 CGDATA  (per-scanline palette)
* ch4 -> $212C TM                              (per-scanline layer enable)
* ch6 -> windows / colour-math

$C1:1381 enables ch1,2,3 via LDA #$0E / TSB $01 at $C1:13EB.

In a clean battle the channels come up in the order ch4 -> ch6 -> ch1,2,3
(ch1,2,3 last, or not at all) and the intro renders correctly. In a
glitched battle $C1:1381 runs *first* - ch1,2,3 are enabled before
ch4/ch6. During that window the ch1+ch2 per-scanline palette HDMA runs
with not-yet-initialised data and bleeds bright garbage into CGRAM
palette 0 - the neon. Once ch4/ch6 come up the screen resolves, which is
why pressing a command "fixes" it. It is purely an ordering bug,
confirmed by comparing the $00:0401 write chain of a glitched battle
(00 -> 0e -> 1e -> ...) against a clean one (00 -> 10 -> ... -> 50).

Fix
---
Gate $C1:1381's ch1,2,3 enable on ch6 already being up, forcing the
clean ordering. $C1:13EB (vanilla A9 0E 04 01 = LDA #$0E / TSB
$01) is replaced with a JSL to a helper that performs the TSB $01
only when bit 6 (ch6) of $00:0401 is already set::

    helper @ $CF:FF00 :  LDA $01 / AND #$40 / BEQ +4 / LDA #$0E / TSB $01 / RTL

Clean battles are unaffected ($C1:1381 runs there with ch6 already
up). Glitched battles: the early $C1:1381 skips the enable -> no neon
window; ch1,2,3 are enabled by a later $C1:1381 once ch6 is up (or
stay off, which is a valid clean state). The direct-page $01 resolves
to $00:0401 because the battle/screen code runs with D = $0400,
and the accumulator is 8-bit at this point.

ROM sites
---------
* $0113EB (SNES $C1:13EB, 4 bytes) - hook, JSL $CF:FF00.
* $0FFF00 (SNES $CF:FF00, 11 bytes) - helper, in free space.
"""


# -----------------------------------------------------------------------
# Hook: $C1:13EB -- replace LDA #$0E / TSB $01 (A9 0E 04 01) with a JSL.
# -----------------------------------------------------------------------
HOOK_ROM_OFFSET = 0x0113EB
HOOK_BYTES = bytes([0x22, 0x00, 0xFF, 0xCF])  # JSL $CF:FF00

# -----------------------------------------------------------------------
# Helper @ $CF:FF00 (ROM $0FFF00) -- ch6-gated ch1,2,3 enable.
#   A5 01      LDA $01        ; $00:0401 (D=$0400), 8-bit A
#   29 40      AND #$40       ; isolate ch6 enable bit
#   F0 04      BEQ +4         ; ch6 not up -> skip the enable
#   A9 0E      LDA #$0E
#   04 01      TSB $01        ; enable HDMA ch1,2,3
#   6B         RTL
# -----------------------------------------------------------------------
HELPER_ROM_OFFSET = 0x0FFF00
HELPER_BYTES = bytes(
    [0xA5, 0x01, 0x29, 0x40, 0xF0, 0x04, 0xA9, 0x0E, 0x04, 0x01, 0x6B]
)


def get_patch() -> dict[int, bytes]:
    """Return {rom_offset: bytes} for the battle-intro HDMA fix."""
    return {
        HOOK_ROM_OFFSET: HOOK_BYTES,
        HELPER_ROM_OFFSET: HELPER_BYTES,
    }
