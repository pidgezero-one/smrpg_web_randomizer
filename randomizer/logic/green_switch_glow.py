"""Aim the green-switch glow at the palette row its sprite actually lands on.

Area-map byte 16 (`effects_npc`) indexes a table of palette animations in bank $DD
— base word `$DD:003E` = `$DD:9CF1`, **entry index = byte - 1** (there is a `DEC` at
`$C0/2316`). Each entry is a list of 3-byte records, and the per-record handler at
`$C0/235F` reads byte 1's low nibble as the CGRAM row to animate (`$2002 + row * 32`).
The record names a *row*, never an NPC.

Overworld CGRAM layout: row 0 is untouched by event scripts, rows 1-7 are background
palettes, row 8 is the protagonist, rows 9-15 are NPCs. `ally_sprite_buffer_size > 1`
extends the protagonist across rows 8..8+size-1 and NPC rows start after it.

NPC rows are handed out **per distinct palette id, in object order** — not per sprite.
Two sprites sharing a palette share one row, and an NPC whose palette id matches the
protagonist's gets no row at all because the protagonist's row already covers it. So
the target row moves whenever the room's palette set changes, which under boss shuffle
it does: room 470's seven henchman objects are one slot, so a filled slot collapses
them to a single model, and Belome 2's clone mirrors the overworld protagonist and
therefore drops out of the allocation entirely.

That is why this recomputes the row rather than shifting the vanilla one by the ally
delta the way the save-point remap and `credits_palette_fix` do — the ally buffer is
only one of the things that moves it.

Each effect id below is set on exactly one room and the `effects_npc` check enforces
that, so rewriting the row nibble in place cannot reach another room. Background-layer
records are absent from the table on purpose: `0x1D` and `0x22` both open with
`6D 81 89` (palette row 1), the factory/keep background glow shared verbatim with
rooms 469 and 471, and BG rows do not move.

NOTE: at vanilla `ally_sprite_buffer_size = 1` room 470's switch computes to row 13
while the vanilla record encodes 14 — an unoccupied row. The vanilla glow there misses
the button; this aims it.
"""
from __future__ import annotations

from typing import TYPE_CHECKING

from smrpgpatchbuilder.datatypes.levels.classes import EffectsNpc

from ..data.variables.sprite_names import SPR0102_SAVE_POINT, SPR0109_GREEN_SWITCH
from ..types.room import Room
# Re-exported, not just used here: these moved to palette_rows but existing
# callers (and test_green_switch_glow) still import them from this module.
# `protagonist_palette_id` and `PROTAGONIST_PALETTE_ROW` look unused locally --
# they are not. Removing them breaks those importers.
from .palette_rows import (
    PROTAGONIST_PALETTE_ROW,
    npc_palette_rows,
    protagonist_palette_id,
)

if TYPE_CHECKING:
    from randomizer.types.gameworld import GameWorld


FIRST_NPC_PALETTE_ROW = 9
MAX_OBJ_PALETTE_ROW = 15

# room id -> (the `effects_npc` that room is expected to hold, records to aim).
# Each record is (ROM address of the record's row byte, the record's high nibble,
# the sprite whose palette the record is meant to animate).
GLOW_RECORDS: dict[int, tuple[EffectsNpc, tuple[tuple[int, int, int], ...]]] = {
    101: (EffectsNpc.UNKNOWN_12, ((0x1D9E72, 0xA0, SPR0109_GREEN_SWITCH),)),
    168: (EffectsNpc.UNKNOWN_21, ((0x1D9EAE, 0xA0, SPR0109_GREEN_SWITCH),)),
    176: (
        EffectsNpc.UNKNOWN_1F,
        (
            (0x1D9EA5, 0x00, SPR0102_SAVE_POINT),
            (0x1D9EA8, 0xA0, SPR0109_GREEN_SWITCH),
        ),
    ),
    221: (EffectsNpc.UNKNOWN_0C, ((0x1D9E48, 0xA0, SPR0109_GREEN_SWITCH),)),
    259: (EffectsNpc.UNKNOWN_16, ((0x1D9E81, 0xA0, SPR0109_GREEN_SWITCH),)),
    406: (EffectsNpc.UNKNOWN_22, ((0x1D9EB4, 0xA0, SPR0109_GREEN_SWITCH),)),
    465: (EffectsNpc.UNKNOWN_20, ((0x1D9EAB, 0xA0, SPR0109_GREEN_SWITCH),)),
    470: (EffectsNpc.UNKNOWN_1D, ((0x1D9E9C, 0xA0, SPR0109_GREEN_SWITCH),)),
}


def get_patch(world: GameWorld) -> dict[int, bytes]:
    """Row bytes aiming each glow record at its sprite's current palette row."""
    patch: dict[int, bytes] = {}
    for room_id, (effects_npc, records) in GLOW_RECORDS.items():
        room = world.rooms._rooms[room_id]
        if room is None or not isinstance(room, Room) or room.partition is None:
            continue
        if room.effects_npc != effects_npc:
            # The id moved, so the record byte may now be shared with another
            # room. Leave vanilla rather than re-aiming someone else's glow.
            continue
        rows = npc_palette_rows(world, room)
        for addr, high_bits, sprite_id in records:
            row = rows.get(world.get_sprite(sprite_id).palette_id)
            if row is None:
                # Sprite left the room, or its palette collapsed onto the
                # protagonist's row, which the glow cannot address.
                continue
            if not FIRST_NPC_PALETTE_ROW <= row <= MAX_OBJ_PALETTE_ROW:
                continue
            patch[addr] = bytes([high_bits | row])
    return patch
