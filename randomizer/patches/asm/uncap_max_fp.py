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

Battle spell-menu FP display — DEFERRED, bisect harness below
--------------------------------------------------------------

Widening the in-battle spell-menu FP header ($C1:62F6) from 2-digit to
3-digit was attempted three different ways and each introduced visible
artifacts that the user considers a crash liability. We're restarting
the investigation by bisecting which patch contributes which artifact.

Set ``_BATTLE_BISECT`` to one of:

* ``"OFF"`` — no battle FP patches (production state).
* ``"A"`` — apply ONLY the static MVN template change at $C1:639D
  (slash $7030 -> $702E, digit slots zeroed). Vanilla renderer
  otherwise. Display: cur-ones overwrites my slash so visually the
  slash is gone; this is fine for artifact isolation. Tests whether the
  template byte change alone causes any artifacts.
* ``"B"`` — apply ONLY the renderer rewrite at $C1:62F6 + trampoline at
  $C1:9564 (STZ $8C + HP 3-digit converter path). Vanilla template
  otherwise. Display: 3-digit cur/max but max-h overwrites the static
  slash at $7030 so no slash visible. Tests whether the renderer
  changes (combination of STZ $8C and the HP converter path) cause
  artifacts.
* ``"C"`` — apply ONLY a minimal ``STZ $8C`` injection (vanilla 2-digit
  converter is still called, no template change, no HP converter
  reuse). Patches the two JSR target operands in the renderer to point
  at a trampoline that does ``STZ $8C`` then tail-calls vanilla
  ``$6378``. Display: identical to vanilla. Tests whether STZ $8C alone
  is the cause.
* ``"D"`` — apply the same trampoline redirection as Test C, but the
  trampoline now SAVES and RESTORES ``$8C``/``$8D`` (m16 LDA / PHA /
  STZ $8C / JSR $6378 / PLA / STA $8C / RTS). Display: identical to
  vanilla. Tests whether properly preserving $8C eliminates the
  artifacts that Test C exposed.

Comparison matrix:

==========  =============================  ============================
Result      Test A    Test B    Test C     Interpretation
==========  =============================  ============================
all clean   clean     clean     clean      Can't reproduce; investigate further
A only      bad       clean     clean      Template change is the cause
B only      clean     bad       clean      Renderer/HP-converter path is the cause
B and C     clean     bad       bad        STZ $8C clobber is the cause
A and B     bad       bad       clean      Both template AND renderer changes contribute (not STZ $8C)
all bad     bad       bad       bad        All changes share root cause (likely $8C or timing)
==========  =============================  ============================

For each test, rebuild the ROM, enter battle, open the special menu,
transition between menus, start casting a spell. Screenshot anything
unusual. The known artifacts to look for:

* Small tile fragments at the edges of the battlefield (especially
  upper-left and right sides)
* A fragmented A-button HUD sprite during action selection
* Garbled tile row directly below the spell list
* "Hold Y for ..." dialog text truncated mid-text
* Unexpected pattern at the right edge of the dialog frame
"""

# Edit this and rebuild between tests. Set back to "OFF" when done.
_BATTLE_BISECT: str = "D"  # "OFF" | "A" | "B" | "C" | "D"


def _battle_bisect_patches() -> dict[int, bytes]:
    """Return the battle FP patches selected by ``_BATTLE_BISECT``."""
    if _BATTLE_BISECT == "OFF":
        return {}

    if _BATTLE_BISECT == "A":
        # Static MVN tilemap source at $C1:639D (22 bytes, same length).
        # Slash moves byte 16 ($7030) -> byte 14 ($702E); digit slots
        # zeroed so they idle as blanks. Vanilla renderer otherwise.
        return {
            0x1639D: bytes([
                0x14, 0x24, 0x15, 0x24, 0x00, 0x24, 0x00, 0x24,
                0x00, 0x24, 0x00, 0x24, 0x00, 0x24, 0x16, 0x24,
                0x00, 0x24, 0x00, 0x24, 0x00, 0x24,
            ]),
        }

    if _BATTLE_BISECT == "B":
        # Renderer rewrite at $C1:62F6 + trampoline at $C1:9564.
        # No template change (max-h will overwrite the static slash at
        # $7030, so no slash will be visible — this is fine, we're only
        # looking for artifacts).
        return {
            # Trampoline at $C1:9564: AND #$00FF / JMP $5D6A
            0x19564: bytes([0x29, 0xFF, 0x00, 0x4C, 0x6A, 0x5D]),
            # Renderer at $C1:62F6 (in-place 26-byte replacement):
            #   REP #$30 / STZ $8C / LDA $FA0C / LDY #$0028 / JSR $9564
            #   LDA $FA0D / LDY #$0030 / JSR $9564 / NOP x4
            0x162F6: bytes([
                0xC2, 0x30,
                0x64, 0x8C,
                0xAD, 0x0C, 0xFA, 0xA0, 0x28, 0x00, 0x20, 0x64, 0x95,
                0xAD, 0x0D, 0xFA, 0xA0, 0x30, 0x00, 0x20, 0x64, 0x95,
                0xEA, 0xEA, 0xEA, 0xEA,
            ]),
        }

    if _BATTLE_BISECT in ("C", "D"):
        # Both C and D redirect the two JSR $6378 calls in the vanilla
        # renderer to a trampoline at $C1:9564. Display is identical to
        # vanilla (still 2-digit, still uses static slash at $7030). The
        # only difference is whether the trampoline saves/restores $8C.
        #
        # Renderer layout (vanilla bytes for reference):
        #   $C1:62FB  20 78 63  JSR $6378   ROM 0x162FB/FC/FD
        #   $C1:6307  20 78 63  JSR $6378   ROM 0x16307/08/09
        # Patch only the operand bytes (positions +1 and +2 after each
        # JSR opcode), leaving the 0x20 opcode bytes intact.
        jsr_redirect: dict[int, bytes] = {
            # First JSR operand ($C1:62FC / 62FD):
            0x162FC: bytes([0x64]),  # low byte of new target $9564
            0x162FD: bytes([0x95]),  # high byte
            # Second JSR operand ($C1:6308 / 6309):
            0x16308: bytes([0x64]),
            0x16309: bytes([0x95]),
        }
        if _BATTLE_BISECT == "C":
            # Test C trampoline (6 bytes): STZ $8C clobber only, no
            # save/restore. Tests whether STZ $8C alone causes artifacts.
            #   $C1:9564: 64 8C       STZ $8C  (m16: clears $8C:$8D)
            #   $C1:9566: 20 78 63    JSR $6378
            #   $C1:9569: 60          RTS
            return {**jsr_redirect, 0x19564: bytes([
                0x64, 0x8C, 0x20, 0x78, 0x63, 0x60,
            ])}
        # Test D trampoline (12 bytes): save $8C:$8D, clobber, JSR,
        # restore. Tests whether properly preserving $8C eliminates the
        # artifacts that Test C exposed.
        #   $C1:9564: A5 8C       LDA $8C  (m16: reads $8C:$8D)
        #   $C1:9566: 48          PHA
        #   $C1:9567: 64 8C       STZ $8C
        #   $C1:9569: 20 78 63    JSR $6378
        #   $C1:956C: 68          PLA
        #   $C1:956D: 85 8C       STA $8C
        #   $C1:956F: 60          RTS
        return {**jsr_redirect, 0x19564: bytes([
            0xA5, 0x8C,
            0x48,
            0x64, 0x8C,
            0x20, 0x78, 0x63,
            0x68,
            0x85, 0x8C,
            0x60,
        ])}

    raise ValueError(
        f"Unknown _BATTLE_BISECT value {_BATTLE_BISECT!r}; "
        f"expected one of 'OFF', 'A', 'B', 'C', 'D'."
    )


def get_patch() -> dict[int, bytes]:
    patches: dict[int, bytes] = {
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
    patches.update(_battle_bisect_patches())
    return patches
