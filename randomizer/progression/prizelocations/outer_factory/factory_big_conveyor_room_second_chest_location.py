from __future__ import annotations
from typing import TYPE_CHECKING
from smrpgpatchbuilder.datatypes.overworld_scripts.event_scripts.commands import *
from randomizer.data.variables.room_names import *
from randomizer.data.variables.event_script_names import *
from randomizer.data.variables.action_script_names import *
from randomizer.data.variables.pack_names import *
from randomizer.progression.prizes import *
from randomizer.types.flags import *
from randomizer.progression.prizelocations.access import (can_access_factory, not_earlygame)
from randomizer.types.logic import (Inventory)
from randomizer.types.prizelocation import (ShuffleLocationSelector, TreasureChestLocationRow2, WorldAreaEnum)
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.area_objects import (NPC_9)
if TYPE_CHECKING:
    from randomizer.types.gameworld import (GameWorld)


class FactoryBigConveyorRoomSecondChestLocation(TreasureChestLocationRow2):
    _bias = True
    _originally_held = MaxMushroomPrize
    _rooms = [
        R475_SMITHY_FACTORY_AREA_12_LOTS_OF_CONSECUTIVE_CONVEYOR_BELTS_AND_LILXXBOOS
    ]
    _npc_ids = [NPC_9]
    _id = ShuffleLocationSelector.FACTORY_CONVEYOR_PLATFORMS_2
    _world_area = WorldAreaEnum.FACTORY
    _blacklist = [EXPStarPrize]
    _hint = [
        # SetVarToConst(PRIMARY_TEMP_7000, 430),
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
            NPC_9,
            R475_SMITHY_FACTORY_AREA_12_LOTS_OF_CONSECUTIVE_CONVEYOR_BELTS_AND_LILXXBOOS,
            ["next"],
        ),
        Jmp(["factory_hint_text"]),
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_factory(world, inventory) and not_earlygame(world, inventory)


__all__ = ["FactoryBigConveyorRoomSecondChestLocation"]
