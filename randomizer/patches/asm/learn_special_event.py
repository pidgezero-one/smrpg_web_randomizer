"""Custom "Learn special ability" event-script command (open-mode base).

Source: ``asm_ref/smrpg-learn-event.asm`` (Abyssonym). The randomizer grants
spells via events; this adds an event-script command (opcode ``$CE``) that
teaches a specific character a specific spell, plus the boot-time install of the
custom event-command engine it runs under. Render-disjoint engine code,
faithfully relocated from open_mode.json (verified byte-identical via
``diff_open_mode``).

- ``$C0:00CC``: cold-start init operand ``$9E03`` -> ``$3E0E``. The boot routine
  (``$C0:0071``+) installs the event/dispatch handler through this pointer; open
  mode aims it at the custom engine install site ``$C0:3E0E`` (beside the vanilla
  ``$C0:3E93`` "read event data").
- ``$C0:C841``: event-command pointer-table entry (``$C0:C6A5 + $CE*2``) for
  opcode ``$CE``, redirected ``$5412`` -> ``$8130``.
- ``$C0:8130``: the command handler, placed in the vanilla anti-piracy/copyright
  padding: ``JSL $FA20B0`` (learn-spell logic, carried by :mod:`static_data`)
  then ``JMP $3E93`` (resume the vanilla event reader). The logic sets the
  learned-spell bit at ``$7F:F810 + char*$14 + spell>>3`` (param byte:
  ``$1F`` = spell, ``$E0`` = character).
"""


def get_patch() -> dict[int, bytes]:
    return {
        0x000CC: bytes([0x0E, 0x3E]),
        0x08130: bytes([0x22, 0xB0, 0x20, 0xFA, 0x4C, 0x93, 0x3E]),
        0x0C841: bytes([0x30, 0x81]),
    }
