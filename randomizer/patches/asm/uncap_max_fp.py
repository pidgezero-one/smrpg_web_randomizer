"""UncapMaxFP: lift the 99 cap on max FP so it can grow up to 255.

Multiple sites participate:

1. Two ``Add7000ToMaxFP`` handlers — overworld at ``$C0:C4CC`` and battle
   at ``$C2:C14F`` — replace the 99-cap with a 255-cap. ``BCS`` catches
   8-bit ADC overflow so a wrap cannot regress max FP.

2. The X-menu per-character "Flowers" line ($C3:1621-$C3:163E) widens
   from 2-digit to 3-digit by switching its converter
   ``$C3:78D2 -> $C3:78EC`` and shifting its destination LDX 2 tiles
   left ($4630 -> $462C). New layout: cur h/t/o at $462C/$462E/$4630,
   slash at $4632, max h/t/o at $4634/$4636/$4638.

3. The X-menu party-total "Flowers" line at $C3:35FF: cur and max also
   use the 2-digit converter at $C3:78D2 (call sites at $C3:3605 and
   $C3:3615), with the field starting at tilemap slot $44B2. The inner
   routine has no separate LDX for the slash or max — both ride on $62,
   which each subroutine advances (2-digit converter += 4, slash writer
   += 2, 3-digit converter += 6). Switching both converters to 3-digit
   widens the field, so we shift the LDX start 4 tiles left
   ($44B2 -> $44AA) to bring the digits inside the menu box.

   New layout: cur h/t/o at $44AA/$44AC/$44AE, slash at $44B0, max
   h/t/o at $44B2/$44B4/$44B6. Writes hit the BG2 tilemap mirror; the
   "Flowers" label sits on a different BG layer so left-shifting past
   the visual label boundary does not corrupt it.

4. The X-menu item-submenu Flowers display ($C3:2CC0) — third call site
   that targets the same shared inner subroutine ($C3:35FF), so the JSR
   target swaps above already make this site emit 3-digit. Shift the
   LDX dest pointer 2 tiles left ($4694 -> $4690) so max-ones lands at
   vanilla $469C (touching the box's right border, with no gap). A
   4-tile shift over-corrected; a 2-tile shift only clips the 's' when
   cur < 100 (the leading blank lands on it) but keeps the digits flush
   right.

5. The battle spell-menu FP header (bank $C1) widens to 3 digits.
   Vanilla renderer at $C1:62F6-$C1:630F (26 bytes) writes 2-digit
   cur/max via JSR $C1:6378 ("F P _ _ _ _ TT/TT"). The 11-tile window
   $7020-$7034 is shared with the spell list (which begins at $7040,
   only 6 bytes past $7034) and with the per-spell FP cost renderer
   (which writes $7024/$7026 each frame).

   This implementation reuses the battle HP 3-digit converter at
   $C1:5D6A (which writes 3 tiles via $7000+Y with leading-zero
   suppression and $2400 attribute prefix) via a 6-byte trampoline at
   $C1:9564 that masks A's high byte first ($FA0C/$FA0D are 1-byte
   values; m16 LDA reads the adjacent byte as garbage in the high
   half). The renderer is rewritten in-place at $C1:62F6 in exactly 26
   bytes, ending without RTS to preserve the fall-through to the F-tile
   animator at $C1:6310.

   New layout in the existing 11-tile $7020-$7034 window::

       $7020 F | $7022 P | $7024-$7026 spell cost (untouched)
       $7028-$702C cur FP (3 digits) | $702E '/' (static)
       $7030-$7034 max FP (3 digits)

   Highest write is $7034 — vanilla parity, no DMA changes. The
   per-spell FP cost renderer at $C1:635B is NOT modified because spell
   costs are capped at 99 in the spell stat table even under
   UncapMaxFP.

Known limitations
-----------------

(Accepted tradeoffs vs alternative implementations that produced worse
artifacts.)

1. ``STZ $8C`` clobbers the dialog-text tilemap cursor used by
   ``$C1:25D2`` / ``$C1:2610``. The "Hold Y for ..." battle-start
   dialog renders with truncated text and an unexpected right-edge
   tile pattern.

2. A small fragment of the A-button HUD sprite occasionally appears in
   the wrong place during action selection (likely a downstream effect
   of the $8C clobber on HUD sprite-table state).

Two earlier attempts to fix these (relocating the renderer with
``$8C`` save/restore, and writing a custom converter using only $80/$86
with save/restore) introduced more visible accumulating tile and
sprite artifacts during menu transitions and spell casting. Without
bsnes runtime tracing we can't pinpoint the exact mechanism, so the
in-place trampoline approach is the best static-analysis option for
now. Followup: instrument with bsnes to trace what reads
$8C / $86 / $80 at the moment of artifact appearance.
"""


def get_patch() -> dict[int, bytes]:
    return {
        # Add7000ToMaxFP handler ($C0:C4CC): replace 99-cap with 255-cap.
        # BCS catches 8-bit ADC overflow so a wrap cannot regress max FP.
        0xC4CC: bytes([0xB0, 0x02, 0x80, 0x02, 0xA9, 0xFF]),
        # Battle bump-max-FP handler ($C2:C14F): same fix, identical bytes.
        0x2C14F: bytes([0xB0, 0x02, 0x80, 0x02, 0xA9, 0xFF]),

        # X-menu per-character FP display ($C3:1621-$C3:163E):
        # switch 2-digit print ($C3:78D2) -> 3-digit print ($C3:78EC)
        # and shift the LDX dest pointer 2 tiles left ($4630 -> $462C).
        0x31622: bytes([0x2C]),
        0x3162F: bytes([0xEC]),
        0x3163F: bytes([0xEC]),

        # X-menu party-total Flowers line at $C3:35FF.
        0x335EB: bytes([0xAA]),
        0x33606: bytes([0xEC]),
        0x33616: bytes([0xEC]),

        # X-menu item-submenu Flowers display ($C3:2CC0).
        0x32CC1: bytes([0x90]),

        # Trampoline at $C1:9564 (free space, 2049 bytes available):
        #   AND #$00FF              -- mask high byte from m16 LDA
        #   JMP $5D6A               -- tail-call HP 3-digit converter
        0x19564: bytes([0x29, 0xFF, 0x00, 0x4C, 0x6A, 0x5D]),

        # Renderer at $C1:62F6 (in-place 26-byte replacement):
        #   REP #$30                -- m16/x16
        #   STZ $8C                 -- partition offset = 0; $5D6A does
        #                              STA $7000,X with X = Y+$8C, so
        #                              $8C must be the offset from $7000
        #                              (not absolute address).
        #   LDA $FA0C / LDY #$0028  -- cur FP value, dest offset
        #   JSR $9564               -- emit 3 cur digits at $7028+
        #   LDA $FA0D / LDY #$0030  -- max FP value, dest offset
        #   JSR $9564               -- emit 3 max digits at $7030+
        #   NOP x4                  -- pad to 26 bytes; falls through to
        #                              $C1:6310 (F-tile animator).
        0x162F6: bytes([
            0xC2, 0x30,
            0x64, 0x8C,
            0xAD, 0x0C, 0xFA, 0xA0, 0x28, 0x00, 0x20, 0x64, 0x95,
            0xAD, 0x0D, 0xFA, 0xA0, 0x30, 0x00, 0x20, 0x64, 0x95,
            0xEA, 0xEA, 0xEA, 0xEA,
        ]),

        # Static MVN tilemap source at $C1:639D (22 bytes, same length).
        # Move '/' from byte 16 ($7030) to byte 14 ($702E) and zero the
        # digit slots so they idle as blanks before the renderer runs:
        #   $7020 F | $7022 P | $7024-$702C blanks | $702E '/'
        #   $7030-$7034 blanks
        0x1639D: bytes([
            0x14, 0x24, 0x15, 0x24, 0x00, 0x24, 0x00, 0x24,
            0x00, 0x24, 0x00, 0x24, 0x00, 0x24, 0x16, 0x24,
            0x00, 0x24, 0x00, 0x24, 0x00, 0x24,
        ]),
    }
