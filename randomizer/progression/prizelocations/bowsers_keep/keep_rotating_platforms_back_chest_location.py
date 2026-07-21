from __future__ import annotations
from typing import TYPE_CHECKING
from smrpgpatchbuilder.datatypes.overworld_scripts.event_scripts.commands import *
from randomizer.data.variables.room_names import *
from randomizer.data.variables.event_script_names import *
from randomizer.data.variables.action_script_names import *
from randomizer.data.variables.pack_names import *
from randomizer.progression.prizes import *
from randomizer.types.flags import *
from randomizer.progression.prizelocations.access import (can_pass_obstacle_courses)
from randomizer.types.logic import (Inventory)
from randomizer.types.prize import (SlotsPrize)
from randomizer.types.prizelocation import (ShuffleLocationSelector, TreasureChestLocationRow6, WorldAreaEnum)
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.area_objects import (NPC_6)
if TYPE_CHECKING:
    from randomizer.types.gameworld import (GameWorld)


class KeepRotatingPlatformsBackChestLocation(TreasureChestLocationRow6):
    _bias = True
    _originally_held = KerokeroColaPrize
    _rooms = [
        R455_BOWSERS_KEEP_6DOOR_ACTION_ROOM_2C_VERY_SLOW_MOVING_CIRCLING_PLATFORMS
    ]
    _npc_ids = [NPC_6]
    _id = ShuffleLocationSelector.BOWSERS_KEEP_ROTATING_PLATFORMS_6
    _world_area = WorldAreaEnum.BOWSERS_KEEP
    _blacklist = [EXPStarPrize, InfiniteCoinsPrize, FirstMimicFightLauncher, SecondMimicFightLauncher, SlotsPrize]
    _hint = [
        # SetVarToConst(PRIMARY_TEMP_7000, 411),
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
            NPC_6,
            R455_BOWSERS_KEEP_6DOOR_ACTION_ROOM_2C_VERY_SLOW_MOVING_CIRCLING_PLATFORMS,
            ["next"],
        ),
        Jmp(["keep_obstacle_hint_text"]),
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_pass_obstacle_courses(world, inventory)


__all__ = ["KeepRotatingPlatformsBackChestLocation"]
