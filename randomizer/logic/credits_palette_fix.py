"""Shift NPC palette rows in `DarkenLayersExceptPaletteRows` event commands when the
credits room's `ally_sprite_buffer_size` was bumped above its original value.

The credits-room cutscene uses event command `0xFD 0x8E` (`DarkenLayersExceptPaletteRows`)
to darken the level background and all NPCs *except* a hardcoded set of OBJ palette
rows. Per SMRPG's VRAM partition rules, growing `ally_sprite_buffer_size` by N shifts
every NPC palette row by +N, so any preserved NPC row in this command must shift
forward by the same delta to keep targeting the same NPC. The MARIO_PALETTE row never
shifts (the player is always palette row 8 on the OBJ side).

The shift amount is read from room 496's
`(ally_sprite_buffer_size - original_ally_sprite_buffer_size)` after
`update_partition_by_protagonist` has run, and is applied to every
`DarkenLayersExceptPaletteRows` command in events 3797 and 3885.
"""
from __future__ import annotations

from typing import TYPE_CHECKING

from smrpgpatchbuilder.datatypes.overworld_scripts.event_scripts.commands import (
    DarkenLayersExceptPaletteRows,
)
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.types.palette_row import (
    PaletteRow,
)

if TYPE_CHECKING:
    from randomizer.types.gameworld import GameWorld


CREDITS_ROOM_ID = 496

EVENTS_TO_SHIFT: tuple[int, ...] = (
    3797,  # E3797_ENDING_CREDITS_ROOM_LOADER (room 496 entrance)
    3885,  # E3885_END_GAME (called from 3797)
)

MARIO_PALETTE_VALUE = 8  # PaletteRow(8). Never shifts when ally buffer grows.
MAX_OBJ_PALETTE_VALUE = 15  # PaletteRow(15) = NPC_PALETTE_ROW_7. Hard upper cap.


def _shift_row(row: PaletteRow, delta: int) -> PaletteRow | None:
    """Shift a single palette row by `delta`. MARIO_PALETTE never shifts.
    Returns None if the shifted row would overflow past NPC_PALETTE_ROW_7."""
    value = int(row)
    if value == MARIO_PALETTE_VALUE:
        return row
    new_value = value + delta
    if new_value > MAX_OBJ_PALETTE_VALUE:
        return None
    return PaletteRow(new_value)


def shift_palette_row_masks_for_ally_buffer_growth(world: "GameWorld") -> None:
    room = world.rooms._rooms[CREDITS_ROOM_ID]
    if room is None or room.partition is None:
        return

    delta = (
        room.partition.ally_sprite_buffer_size
        - room.partition.original_ally_sprite_buffer_size
    )
    if delta <= 0:
        return

    for script_id in EVENTS_TO_SHIFT:
        script = world.event_scripts.get_script_by_id(script_id)
        for cmd in script.contents:
            if not isinstance(cmd, DarkenLayersExceptPaletteRows):
                continue
            shifted: list[PaletteRow] = []
            for row in cmd.preserve_rows:
                new_row = _shift_row(row, delta)
                if new_row is not None:
                    shifted.append(new_row)
            cmd.set_preserve_rows(shifted)
