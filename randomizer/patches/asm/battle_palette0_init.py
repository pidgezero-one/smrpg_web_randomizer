"""Battle-intro palette-0 initialization.

Fixes a graphical glitch where battles started with ``StartBattleAtBattlefield``
show neon-coloured blocks around background-object edges during the intro,
clearing only when the player first touches the command menu.

Root cause
----------

A battle's CGRAM is assembled in the WRAM buffer ``$7E:2000`` and DMA'd to
CGRAM from there. The battlefield-palette loader at ``$C1:2214`` fills only
**color 0 and CGRAM palettes 2-7** of that buffer (``$34D000 + bf_idx*$B6``,
182 bytes per battlefield); it never writes **palette 0, colors 1-15**
(``$7E:2002-$7E:201F``). Those bytes keep stale leftover data from the
previous scene, and the battle-start CGRAM upload copies the garbage straight
to screen. The engine writes the real palette-0 colors only later, when the
command menu engages (observed at ``$C1:6CEC``) -- which is why pressing any
command button clears the glitch.

Vanilla never shows this because its fixed battlefield/pack pairings leave
benign leftovers in palette 0; the randomizer's novel
``StartBattleAtBattlefield`` pairings expose it.

The fix
-------

Hook the instant *after* ``$C1:2214`` returns (the battlefield palette is now
in ``$7E:2000``) and *before* the CGRAM upload, and zero palette 0 colors
1-15. The intro then shows black instead of neon in those slots -- effectively
unnoticeable in the 1-2 second intro -- and the menu phase still writes the
real palette 0 afterwards, exactly as before.

ROM sites
---------

* ``$C1:2136`` (4 bytes, ROM ``$012136``) -- replaces the two instructions::

      C2 30   REP #$30
      E2 20   SEP #$20

  with a ``JSL`` to the helper. The helper replays both displaced
  instructions (``REP #$30`` at its start, ``SEP #$20`` before ``RTL``).

* ``$CF:FF00`` (18 bytes, ROM ``$0FFF00``) -- helper routine, placed in the
  zero-filled free space at the end of bank ``$0F``
  (``$0F:F7B0-$0F:FFFF``; ``belome3_brooch`` occupies only
  ``$0FF7B0-$0FF97B``). Audited collision-free via ``smrpg-patch-audit``.

The helper clobbers X only (reloaded at ``$C1:214D`` before its next use) and
touches no other register. DB is ``$7E`` at the hook, so the ``STZ $2000,X``
stores land in ``$7E:2002+``. The hook code path runs on the S-CPU, which can
``JSL`` into bank ``$CF`` freely.
"""


# -----------------------------------------------------------------------
# Patch sites
# -----------------------------------------------------------------------
_HOOK_OFFSET = 0x012136            # SNES $C1:2136 -- REP #$30 / SEP #$20
_HELPER_OFFSET = 0x0FFF00          # SNES $CF:FF00 -- end-of-bank free space

# JSL $CF:FF00  (replaces exactly REP #$30 + SEP #$20)
_HOOK_BYTES = bytes([
    0x22, 0x00, 0xFF, 0xCF,
])
assert len(_HOOK_BYTES) == 4

# Helper: zero $7E:2002-$7E:201F (palette 0, colors 1-15), then replay the
# displaced REP #$30 / SEP #$20 and RTL back to $C1:213A.
_HELPER_BYTES = bytes([
    0xC2, 0x30,              # REP #$30        A/X/Y -> 16-bit (displaced #1)
    0xA2, 0x02, 0x00,        # LDX #$0002      byte offset of palette 0 color 1
    0x9E, 0x00, 0x20,        # STZ $2000,X     [loop] $7E:2000+X = 0
    0xE8,                    # INX
    0xE8,                    # INX
    0xE0, 0x20, 0x00,        # CPX #$0020      reached end of palette 0?
    0x90, 0xF6,              # BCC -10         -> STZ (loop)
    0xE2, 0x20,              # SEP #$20        (displaced #2)
    0x6B,                    # RTL
])
assert len(_HELPER_BYTES) == 18


def get_patch() -> dict[int, bytes]:
    """Return ``{rom_offset: bytes}`` -- the JSL hook plus the helper."""
    return {
        _HOOK_OFFSET: _HOOK_BYTES,
        _HELPER_OFFSET: _HELPER_BYTES,
    }
