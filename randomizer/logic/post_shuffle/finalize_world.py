"""Final world mutations, applied once the shuffle is complete.

These steps mutate world state (event scripts, room partitions) rather than
emitting patch bytes, so they run at the end of build_world instead of inside
get_patch. Two of them are NOT idempotent -- `event_2496_startup += [Return()]`
appends every call, and the palette-row shift adds its delta every call -- so
running them from get_patch was only safe because that function memoises via
world._cached_patch. Doing them here makes get_patch a pure serializer.
"""

from __future__ import annotations

from typing import TYPE_CHECKING

from randomizer.data.variables.event_script_names import (
    E1252_FLAG_SPECIFIC_HOUSEKEEPING_GAME_START,
)
from randomizer.logic.credits_palette_fix import (
    shift_palette_row_masks_for_ally_buffer_growth as _shift_palette_row_masks_for_ally_buffer_growth,
)
from randomizer.types.room import Room
from smrpgpatchbuilder.datatypes.overworld_scripts.event_scripts.commands import Return

if TYPE_CHECKING:
    from randomizer.types.gameworld import GameWorld


def finalize_world(world: GameWorld) -> None:
    # Finalize startup script
    world.event_2496_startup += [Return()]
    world.event_scripts.get_script_by_id(
        E1252_FLAG_SPECIFIC_HOUSEKEEPING_GAME_START
    ).set_contents(world.event_2496_startup)

    # Partition + palette-row fixups must run BEFORE event scripts render —
    # the fixup mutates DarkenLayersExceptPaletteRows commands in event scripts,
    # so any post-render mutation would be lost.
    # Ending cutscene rooms keep a static ally_buffer regardless of
    # protagonist. R088/R375/R496 use the Mario-NPC-at-front pattern where
    # the protagonist is rendered through a fixed NPC slot rather than the
    # ally buffer, so growing ally_buffer (e.g. to 2 for Bowser) would
    # only shift palette rows the cutscene scripts hardcoded references to.
    # R269/R432/R435/R441/R486/R506/R595 are other ending credits rooms
    # whose palette/layout assumptions also break under ally_buffer growth.
    _STATIC_PARTITION_ROOM_IDS = frozenset({
        88,   # R088_SMITHYS_FINAL_FORM_DEFEAT_GENOS_REDEMPTION
        269,  # R269_ENDING_CREDITS_NIMBUS_LAND_PRINCE_MALLOW
        375,  # R375_ENDING_CREDITS_STAR_PIECES_SHOOT_THROUGH_THE_SKY
        432,
        435,  # R435_ENDING_CREDITS_BOWSERS_KEEP_BOWSER_TROOPS_REPAIR
        441,
        486,
        292,  # R292 — split second-half of the R496 ending cutscene
        496,  # R496_FACTORY_GROUNDS_FIGHT_WITH_SMITHY_USES_SLEDGE
        505,
        506,
    })
    for room_id, r in enumerate(world.rooms._rooms):
        if r is not None and isinstance(r, Room) and room_id not in _STATIC_PARTITION_ROOM_IDS:
            r.update_partition_by_protagonist(world)

    _shift_palette_row_masks_for_ally_buffer_growth(world)


__all__ = ["finalize_world"]
