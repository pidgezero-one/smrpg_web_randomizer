from __future__ import annotations
from typing import TYPE_CHECKING
from smrpgpatchbuilder.datatypes.overworld_scripts.event_scripts.commands import *
from randomizer.data.variables.room_names import *
from randomizer.data.variables.event_script_names import *
from randomizer.data.variables.action_script_names import *
from randomizer.data.variables.pack_names import *
from randomizer.logic.progression.prizes import *
from randomizer.types.flags import *
from randomizer.logic.progression.prizelocations.access import (can_access_volcano, expect_good_movement, not_earlygame, expect_halfway_decent_movement, almost_earlygame, is_midgame, expect_ok_movement, lategame)
from randomizer.types.logic import (Inventory)
from randomizer.types.prizelocation import (ShuffleLocationSelector, TreasureChestLocationRow2, WorldAreaEnum)
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.area_objects import (NPC_1)
if TYPE_CHECKING:
    from randomizer.types.gameworld import (GameWorld)


class VolcanoSaveRoomUpperChestLocation(TreasureChestLocationRow2):
    _bias = True
    _originally_held = FrogCoin1Prize
    _rooms = [R366_VOLCANO_AREA_13_WSAVE_POINT]
    _npc_ids = [NPC_1]
    _id = ShuffleLocationSelector.BARREL_VOLCANO_SAVE_ROOM_2
    _world_area = WorldAreaEnum.BARREL_VOLCANO
    _blacklist = [EXPStarPrize]
    _hint = [
        # SetVarToConst(PRIMARY_TEMP_7000, 373),
        # RunDialog(
            # dialog_id=DI2010_DEBUG_7000,
            # above_object=BOWSER,
            # closable=True,
            # sync=False,
            # multiline=True,
            # use_background=True,
        # ),
        JmpIfBitClear(MAP_BARREL_VOLCANO, ["next"]),
        JmpIfObjectTriggerDisabledInSpecificLevel(
            NPC_1, R366_VOLCANO_AREA_13_WSAVE_POINT, ["next"]
        ),
        Jmp(["barrel_volcano_hint_text"]),
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_volcano(world, inventory)


__all__ = ["VolcanoSaveRoomUpperChestLocation"]
