"""ASM patch: bound the character-id offset in the game-over auto-continue.

Bug
---

``ResetAndChooseGame`` (event opcode $FB, handler $C0:5716) is a soft
reset: it resets the stack and jumps to $C0:02CD, leaving WRAM intact.
$C0:02CD first tries the *auto-continue* path ($58 = $0A -> bank C3
mode 10 = $C3:7B4C), which is what preserves character EXP across a
game over:

1. $C3:7B75  backs up the live 2KB save block $7F:F800-FFFF to $7E:F800
2. $C3:7B7F  loads the save slot over $7F:F800 (flags, position, items)
3. $C3:7B8D  for each character in the *saved* roster ($7F:FBC2 = count,
   $7F:FBC3+ = ids), copies bytes $00-$0B (level, HP, maxHP, stats and
   the 2-byte EXP) plus $10-$13 (spells) back out of the backup
4. full-heals HP/FP and starts the game

Step 3 turns the character id into a record offset with::

    C3/7B8E  BF C3 FB 7F  LDA $7FFBC3,X   ; character id
    C3/7B92  EB           XBA
    C3/7B93  A9 14        LDA #$14
    C3/7B95  20 84 04     JSR $0484       ; id * $14
    C3/7B98  C2 20        REP #$20
    C3/7B9A  48           PHA
    C3/7B9B  18 69 00 F8  CLC : ADC #$F800
    C3/7B9F  AA A8        TAX : TAY
    C3/7BA1  A9 0B 00     LDA #$000B
    C3/7BA4  54 7F 7E     MVN $7F,$7E

and never range-checks the result. Two ways that goes wrong:

* $C3:0484 is a *shared, non-reentrant* hardware-multiply helper --
  ``STA $004202`` / 3x NOP / ``LDA $004216`` with no interrupt guard.
  NMI is enabled for this whole sequence ($C0:0936 writes $4200 = $01
  just before ``JSL $C30000``; bank C3's ``SEI`` at $C3:0046 masks IRQ
  only). The NMI vector during the title/continue is $C3:00DF, which
  dispatches up to four queued tasks through $00:00A0-A7 -- direct page
  that a soft reset does not clear -- and bank C3 has 51 call sites of
  ``JSR $0484``. One landing inside the ~10-cycle window replaces the
  product with an arbitrary 16-bit value.

* the loop counter is a do-while (``STA $7E`` ... ``DEC $7E`` /
  ``BNE``), so a saved slot count of 0 runs 256 iterations and reads
  event-flag bytes as character ids.

Either way the ``MVN`` destination walks out of the character block.
Offsets $3E5-$4EF land in $7F:FBF0-FCEF, which is the saved copy of
event flags $00:7000-70FF and gets pushed straight back into BW-RAM at
$C0:035C. That is the reported symptom exactly: EXP silently reverts to
the save value (the real records were never copied back) *and* NPCs
despawn in unrelated rooms (corrupted flags), looking like a save from
a different ROM.

This is vanilla behaviour -- $C3:0484 and $C3:7B40-7BFF are byte
identical between the vanilla ROM and a built randomizer ROM.

Fix
---

Point the multiply at a private helper that clamps the character id to
0-4 and computes ``id * $14`` with shifts instead of $4202/$4216:

* no hardware multiplier, so the NMI race cannot reach it
* every ``MVN`` destination is forced inside $7F:F800-F863, which also
  defuses the 256-iteration case (it degenerates to re-copying valid
  character records, which is idempotent)

$C3:0484 itself is left alone; its other 50 callers recompute every
frame and are unaffected by a one-frame glitch.

Register contract matches $C3:0484 exactly: entered with M=8/X=16 and
C = (id << 8) | $14, returns C = id * $14 with M=8. X is dead across
the call ($C3:7B9F overwrites it with TAX), so the helper is free to
clobber it.

Layout
------

Hook: ROM $03:7B95 - 3 bytes, JSR $0484 -> JSR $FC40.
Patch: ROM $03:FC40 (SNES $C3:FC40) - 24-byte helper in end-of-bank
free space.
"""

# Hook at ROM $037B95: retarget the multiply call.
_HOOK_OFFSET = 0x037B95
_HOOK_BYTES = bytes([0x20, 0x40, 0xFC])   # JSR $FC40

# Helper at ROM $03FC40 (SNES $C3:FC40).
_PATCH_OFFSET = 0x03FC40
_PATCH_BYTES = bytes([
    0xEB,                     # XBA              A = character id
    0xC9, 0x05,               # CMP #$05
    0x90, 0x02,               # BCC +2           id 0-4: use as-is
    0xA9, 0x00,               # LDA #$00         out of range: clamp to slot 0
    0xC2, 0x20,               # REP #$20
    0x29, 0xFF, 0x00,         # AND #$00FF       drop the $14 left in B
    0x0A,                     # ASL
    0x0A,                     # ASL              id * 4
    0x48,                     # PHA
    0x0A,                     # ASL
    0x0A,                     # ASL              id * 16
    0x18,                     # CLC
    0x63, 0x01,               # ADC $01,S        + id * 4  ->  id * $14
    0xFA,                     # PLX              discard scratch (X is dead)
    0xE2, 0x20,               # SEP #$20         return in 8-bit M, as $0484 does
    0x60,                     # RTS
])


def get_patch() -> dict[int, bytes]:
    """Return the hook + helper bytes for the game-over continue fix."""
    return {
        _HOOK_OFFSET: _HOOK_BYTES,
        _PATCH_OFFSET: _PATCH_BYTES,
    }
