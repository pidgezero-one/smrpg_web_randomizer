from __future__ import annotations
from typing import TYPE_CHECKING
from smrpgpatchbuilder.datatypes.overworld_scripts.event_scripts.commands import *
from randomizer.data.variables.room_names import *
from randomizer.data.variables.event_script_names import *
from randomizer.data.variables.action_script_names import *
from randomizer.data.variables.pack_names import *
from randomizer.logic.progression.prizes import *
from randomizer.types.flags import *
from randomizer.logic.progression.prizelocations.access import (can_pass_obstacle_courses)
from randomizer.types.logic import (Inventory)
from randomizer.types.prize import (FPFlowerPrize)
from randomizer.types.prizelocation import (ShuffleLocationSelector, TreasureChestLocationRow1, WorldAreaEnum)
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.area_objects import (NPC_10)
if TYPE_CHECKING:
    from randomizer.types.gameworld import (GameWorld)


class KeepXYPlatformsBackLeftChestLocation(TreasureChestLocationRow1):
    _bias = True
    _originally_held = FPFlowerPrize
    _rooms = [R458_BOWSERS_KEEP_6DOOR_ACTION_ROOM_1B_MOVING_PLATFORMS]
    _npc_ids = [NPC_10]
    _id = ShuffleLocationSelector.BOWSERS_KEEP_MOVING_PLATFORMS_1
    _world_area = WorldAreaEnum.BOWSERS_KEEP
    _blacklist = [EXPStarPrize, InfiniteCoinsPrize, FirstMimicFightLauncher, SecondMimicFightLauncher]
    _hint = [
        # SetVarToConst(PRIMARY_TEMP_7000, 388),
        # RunDialog(
            # dialog_id=DI2010_DEBUG_7000,
            # above_object=BOWSER,
            # closable=True,
            # sync=False,
            # multiline=True,
            # use_background=True,
        # ),
        JmpIfBitSet(MAP_DIRECTIONAL_NIMBUS_LAND_VISTA_HILL, ["next"]),
        JmpIfObjectTriggerDisabledInSpecificLevel(
            NPC_10, R458_BOWSERS_KEEP_6DOOR_ACTION_ROOM_1B_MOVING_PLATFORMS, ["next"]
        ),
        Jmp(["keep_obstacle_hint_text"]),
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_pass_obstacle_courses(world, inventory)


__all__ = ["KeepXYPlatformsBackLeftChestLocation"]
