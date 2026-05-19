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

Battle spell-menu FP display — DEFERRED
----------------------------------------

Widening the in-battle spell-menu FP header ($C1:62F6) from 2-digit to
3-digit was attempted three different ways and each introduced its own
class of artifacts that turned out to be a crash liability rather than a
purely cosmetic issue:

* In-place trampoline using the HP 3-digit converter at $C1:5D6A —
  truncates the "Hold Y for ..." battle-start dialog (STZ $8C clobbers
  the dialog tilemap cursor) and displaces a fragment of the A-button
  HUD sprite during action selection.

* Relocated renderer with $8C / $8E save/restore — introduced
  accumulating tile artifacts during menu transitions and spell casting
  (suspected timing/flag-mode interaction with the F-tile animator at
  $C1:6310).

* Custom 3-digit converter avoiding $8C entirely (only $80 and $86,
  with save/restore) — different but still substantial artifacts
  (sprite fragments on the battlefield, garbled tile rows below the
  spell list).

Static analysis cannot pinpoint the mechanism. A fresh attempt should
start by instrumenting bsnes-plus with SA-1 read-watchpoints on the
relevant zero-page bytes ($8C, $86, $80) and OAM mirror writes to
identify exactly what gets corrupted at the moment of artifact
appearance. Until then, the in-battle FP display stays vanilla 2-digit
and clips values >99 — the underlying max-FP storage is still raised by
the two cap-handler patches above, so gameplay (cast checks, FP
deduction) operates on the real value.
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
    }
