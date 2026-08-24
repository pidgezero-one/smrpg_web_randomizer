from __future__ import annotations
from typing import TYPE_CHECKING
from smrpgpatchbuilder.datatypes.overworld_scripts.event_scripts.commands import *
from randomizer.data.variables.room_names import *
from randomizer.data.variables.event_script_names import *
from randomizer.data.variables.action_script_names import *
from randomizer.data.variables.pack_names import *
from randomizer.logic.progression.prizes import *
from randomizer.types.flags import *
from randomizer.logic.progression.prizelocations.access import (expect_good_movement, not_earlygame, expect_halfway_decent_movement, almost_earlygame, is_midgame, expect_ok_movement, lategame)
from randomizer.types.logic import (Inventory)
from randomizer.types.prizelocation import (ShuffleLocationSelector, StarPieceLocation, WorldAreaEnum)
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.area_objects import (NPC_9)
if TYPE_CHECKING:
    from randomizer.types.gameworld import (GameWorld)


class StarHillStarPiece(StarPieceLocation):
    _originally_held = StarPiece4
    _rooms = [R159_STAR_HILL_AREA_04]
    _id = ShuffleLocationSelector.STAR_HILL_STAR_PIECE_1
    _world_area = WorldAreaEnum.STAR_HILL
    _hint = [
        # SetVarToConst(PRIMARY_TEMP_7000, 204),
        # RunDialog(
            # dialog_id=DI2010_DEBUG_7000,
            # above_object=BOWSER,
            # closable=True,
            # sync=False,
            # multiline=True,
            # use_background=True,
        # ),
        JmpIfObjectInSpecificLevel(
            NPC_9, R159_STAR_HILL_AREA_04, ["star_hill_hint_text"]
        ),
        JmpIfBitSet(STAR_HILL_CHECKED, ["next"]),
        Jmp(["star_hill_hint_text"]),
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return expect_halfway_decent_movement(world, inventory)


__all__ = ["StarHillStarPiece"]
