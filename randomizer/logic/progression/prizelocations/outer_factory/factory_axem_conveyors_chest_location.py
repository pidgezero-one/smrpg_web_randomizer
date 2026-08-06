from __future__ import annotations
from typing import TYPE_CHECKING
from smrpgpatchbuilder.datatypes.overworld_scripts.event_scripts.commands import *
from randomizer.data.variables.room_names import *
from randomizer.data.variables.event_script_names import *
from randomizer.data.variables.action_script_names import *
from randomizer.data.variables.pack_names import *
from randomizer.logic.progression.prizes import *
from randomizer.types.flags import *
from randomizer.logic.progression.prizelocations.access import (can_access_factory, not_earlygame)
from randomizer.types.logic import (Inventory)
from randomizer.types.prizelocation import (ShuffleLocationSelector, TreasureChestLocationRow1, WorldAreaEnum)
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.area_objects import (NPC_6)
if TYPE_CHECKING:
    from randomizer.types.gameworld import (GameWorld)


class FactoryAxemConveyorsChestLocation(TreasureChestLocationRow1):
    _bias = True
    _originally_held = RecoveryMushroomPrize
    _rooms = [R434_SMITHY_FACTORY_AREA_09_FALLING_AXEM_REDS_ON_CONVEYOR_BELTS]
    _npc_ids = [NPC_6]
    _id = ShuffleLocationSelector.FACTORY_FALLING_AXEMS
    _world_area = WorldAreaEnum.FACTORY
    _blacklist = [EXPStarPrize]
    _hint = [
        # SetVarToConst(PRIMARY_TEMP_7000, 426),
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
            NPC_6,
            R434_SMITHY_FACTORY_AREA_09_FALLING_AXEM_REDS_ON_CONVEYOR_BELTS,
            ["next"],
        ),
        Jmp(["factory_hint_text"]),
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_factory(world, inventory) and not_earlygame(world, inventory)


__all__ = ["FactoryAxemConveyorsChestLocation"]
