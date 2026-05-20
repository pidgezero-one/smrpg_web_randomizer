"""Hybrid per-slot character-index dispatch for the overworld
ally-sprite loader.

Background
----------

The room-load ally loop at ``$C0:9006`` walks each party object slot,
loading the corresponding character's sprite via ``JSR $9B4E``::

    $9006  A0 33 00    LDY #$0033          ; Y = roster table offset
    $9009  B9 00 00    LDA $0000,Y         ; load roster[Y]  (VANILLA)
    $900C  85 60       STA $60             ; → char index for $9B4E
    $900E  20 4E 9B    JSR $9B4E           ; load sprite base + anim idx
    ...
    $9017  C8          INY
    $9018  C6 68       DEC $68             ; loop counter
    $901A  ...                              ; branch back

The base ``open_mode.json`` stamps ``$9009`` with ``A9 00 EA``
(``LDA #$00 / NOP``), forcing the index to ``0`` every iteration. That
collapse is *load-bearing* for three invariants the randomizer relies
on (see [reference_c0_9b4e_sprite_loader] memory):

* Slot 0 always renders as the alt-protagonist sprite ``$1F`` via the
  ``non_mario_character`` ``$9B86 = $1F`` patch.
* Slot 0 always gets the lead-default animation index ``$07`` (Geno's
  special-case ``$05`` would mismatch the alt-protagonist sprite's
  expectations).
* Mid-room party swaps stay visually consistent because the loader
  only runs on room-load.

But the collapse also forces *follower* slots to load char 0, which
means ``CHARACTER_IN_SLOT_2``/``_3`` render with the protagonist's
sprite — breaking cutscenes (e.g. script_1710.py at room 206) that
want a real follower visible.

The hybrid
----------

Replace ``$9009`` with a ``JSR`` to a helper that returns ``0`` for
the lead slot (``Y == $33`` — the first roster offset) and
``LDA $0000,Y`` for follower slots::

    $9009  20 2E E4    JSR $E42E           ; (was: A9 00 EA)

The helper lives in repurposed NOP space at ``$E42C-$E43A`` (15 bytes
that ``open_mode.json`` stamped with ``EA × 15``, NOPing a vanilla
character-resolver loop similar to ``$3EB2``)::

    $E42C  80 0D       BRA $E43B           ; preserve fall-through to A=0
    $E42E  C0 33 00    CPY #$0033          ; (helper entry — JSR target)
    $E431  D0 03       BNE +$3 → $E436
    $E433  A9 00       LDA #$00            ; lead slot → force char 0
    $E435  60          RTS
    $E436  B9 00 00    LDA $0000,Y         ; follower → real roster char
    $E439  60          RTS
    $E43A  EA          (1 byte spare)

The ``BRA $E43B`` at the front preserves the patched fall-through
behavior for the *other* caller of this region — a per-opcode
dispatcher at ``$E3FE`` does ``BCC $E423``, whose path flows through
the prelude (``LDX #$3033 / STZ $81 / LDA $80``) into ``$E42C``. In
open_mode that path was 15 NOPs falling through to ``$E43B``
(``LDA #$00 / BRA $E458``) — i.e. "char not found, return slot 0". Our
``BRA $E43B`` keeps that exact behavior; the helper only runs when
explicitly called via ``JSR $E42E``.

Verification
~~~~~~~~~~~~

* ``CPY #$0033`` is the lead-slot check: ``$9006 LDY #$0033`` sets the
  loop's starting Y, and ``$9017 INY`` advances per iteration. So the
  first iteration sees ``Y == $33``; subsequent iterations see
  ``Y == $34, $35, ...``.
* A is 8-bit at ``$9009`` (vanilla ``LDA $0000,Y`` is a 1-byte load;
  the immediately-following ``STA $60`` is an 8-bit store). Helper's
  ``LDA #$00`` and ``LDA $0000,Y`` both work in 8-bit A mode.
* X is 16-bit (``$9006 LDY #$0033`` uses a 2-byte immediate, requires
  ``X=0``), so ``CPY #$xxxx`` is a 3-byte instruction. Encoded
  ``C0 33 00``.
* No engine code anywhere in either vanilla or patched ROM has a
  ``JSR``/``JSL``/``JMP``/``JML`` targeting ``$E42C`` or ``$E420``.
  Only fall-through reaches ``$E42C``, and ``BRA $E43B`` keeps that
  path consistent with the patched-NOP behavior.

This module pairs with ``non_mario_character``'s existing
``$9B86 = $1F`` patch (kept as-is — slot 0 still loads the alt-
protagonist sprite via the char-0 force in the helper).
"""


def get_patch() -> dict[int, bytes]:
    return {
        # $C0:9009 — replace open_mode's `A9 00 EA` (LDA #$00 / NOP)
        # with `JSR $E42E`, so the lead slot gets char 0 (existing
        # invariant) but followers get their real roster char id.
        0x9009: bytes([0x20, 0x2E, 0xE4]),

        # $C0:E42C — repurpose open_mode's 15-NOP block as the helper.
        # First 2 bytes are BRA $E43B to preserve fall-through behavior
        # for the dispatcher path at $E3FE BCC $E423 → ... → $E42C;
        # remaining 12 bytes are the helper proper (called via JSR
        # $E42E from $9009 above). Final byte $E43A stays NOP.
        0xE42C: bytes([
            0x80, 0x0D,        # BRA $E43B  (skip helper on fall-through)
            0xC0, 0x33, 0x00,  # CPY #$0033 (lead-slot check)
            0xD0, 0x03,        # BNE +$3 → $E436
            0xA9, 0x00,        # LDA #$00   (lead → force char 0)
            0x60,              # RTS
            0xB9, 0x00, 0x00,  # LDA $0000,Y (follower → roster[Y])
            0x60,              # RTS
            0xEA,              # (spare NOP, $E43A)
        ]),
    }
