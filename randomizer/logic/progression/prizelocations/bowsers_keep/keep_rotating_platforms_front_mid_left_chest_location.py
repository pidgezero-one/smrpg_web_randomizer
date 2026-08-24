from __future__ import annotations
from typing import TYPE_CHECKING
from smrpgpatchbuilder.datatypes.overworld_scripts.event_scripts.commands import *
from randomizer.data.variables.room_names import *
from randomizer.data.variables.event_script_names import *
from randomizer.data.variables.action_script_names import *
from randomizer.data.variables.pack_names import *
from randomizer.logic.progression.prizes import *
from randomizer.types.flags import *
from randomizer.logic.progression.prizelocations.access import (can_pass_obstacle_courses, expect_good_movement, not_earlygame, expect_halfway_decent_movement, almost_earlygame, is_midgame, expect_ok_movement, lategame, can_exit_keep, can_clear_keep)
from randomizer.types.logic import (Inventory)
from randomizer.types.prize import (FPFlowerPrize, SlotsPrize)
from randomizer.types.prizelocation import (ShuffleLocationSelector, TreasureChestLocationRow2, WorldAreaEnum)
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.area_objects import (NPC_2)
if TYPE_CHECKING:
    from randomizer.types.gameworld import (GameWorld)


class KeepRotatingPlatformsFrontMidLeftChestLocation(TreasureChestLocationRow2):
    _bias = True
    _originally_held = FPFlowerPrize
    _rooms = [
        R455_BOWSERS_KEEP_6DOOR_ACTION_ROOM_2C_VERY_SLOW_MOVING_CIRCLING_PLATFORMS
    ]
    _npc_ids = [NPC_2]
    _id = ShuffleLocationSelector.BOWSERS_KEEP_ROTATING_PLATFORMS_2
    _world_area = WorldAreaEnum.BOWSERS_KEEP
    _blacklist = [EXPStarPrize, InfiniteCoinsPrize, FirstMimicFightLauncher, SecondMimicFightLauncher, SlotsPrize]
    _hint = [
        # SetVarToConst(PRIMARY_TEMP_7000, 407),
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
            NPC_2,
            R455_BOWSERS_KEEP_6DOOR_ACTION_ROOM_2C_VERY_SLOW_MOVING_CIRCLING_PLATFORMS,
            ["next"],
        ),
        Jmp(["keep_obstacle_hint_text"]),
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_exit_keep(world, inventory) and can_exit_keep(world, inventory)


__all__ = ["KeepRotatingPlatformsFrontMidLeftChestLocation"]
