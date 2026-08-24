from __future__ import annotations
from typing import TYPE_CHECKING
from smrpgpatchbuilder.datatypes.overworld_scripts.event_scripts.commands import *
from randomizer.data.variables.room_names import *
from randomizer.data.variables.event_script_names import *
from randomizer.data.variables.action_script_names import *
from randomizer.data.variables.pack_names import *
from randomizer.logic.progression.prizes import *
from randomizer.types.flags import *
from randomizer.logic.progression.prizelocations.access import (can_access_factory, not_earlygame, is_early_midgame, is_late_midgame, is_lategame, expect_good_movement, expect_halfway_decent_movement, almost_earlygame, is_midgame, expect_ok_movement, lategame, can_defeat_factory_bosses)
from randomizer.types.logic import (Inventory)
from randomizer.types.prize import (SlotsPrize)
from randomizer.types.prizelocation import (ShuffleLocationSelector, TreasureChestLocationRow1, WorldAreaEnum)
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.area_objects import (NPC_8)
if TYPE_CHECKING:
    from randomizer.types.gameworld import (GameWorld)


class FactoryBigConveyorRoomFirstChestLocation(TreasureChestLocationRow1):
    _bias = True
    _originally_held = RoyalSyrupPrize
    _rooms = [
        R475_SMITHY_FACTORY_AREA_12_LOTS_OF_CONSECUTIVE_CONVEYOR_BELTS_AND_LILXXBOOS
    ]
    _npc_ids = [NPC_8]
    _id = ShuffleLocationSelector.FACTORY_CONVEYOR_PLATFORMS_1
    _world_area = WorldAreaEnum.FACTORY
    _blacklist = [EXPStarPrize, SlotsPrize]
    _hint = [
        # SetVarToConst(PRIMARY_TEMP_7000, 429),
        # RunDialog(
            # dialog_id=DI2010_DEBUG_7000,
            # above_object=BOWSER,
            # closable=True,
            # sync=False,
            # multiline=True,
            # use_background=True,
        # ),
        JmpIfBitClear(MAP_GATE, ["next"]),
        JmpIfObjectTriggerDisabledInSpecificLevel(
            NPC_8,
            R475_SMITHY_FACTORY_AREA_12_LOTS_OF_CONSECUTIVE_CONVEYOR_BELTS_AND_LILXXBOOS,
            ["next"],
        ),
        Jmp(["factory_hint_text"]),
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_defeat_factory_bosses(world, inventory)


__all__ = ["FactoryBigConveyorRoomFirstChestLocation"]
