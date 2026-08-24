from __future__ import annotations
from typing import TYPE_CHECKING
from smrpgpatchbuilder.datatypes.overworld_scripts.event_scripts.commands import *
from randomizer.data.variables.room_names import *
from randomizer.data.variables.event_script_names import *
from randomizer.data.variables.action_script_names import *
from randomizer.data.variables.pack_names import *
from randomizer.logic.progression.prizes import *
from randomizer.types.flags import *
from randomizer.logic.progression.prizelocations.access import (can_access_forest, expect_good_movement, not_earlygame, expect_halfway_decent_movement, almost_earlygame, is_midgame, expect_ok_movement, lategame)
from randomizer.types.logic import (Inventory)
from randomizer.types.prize import (FPFlowerPrize, SlotsPrize)
from randomizer.types.prizelocation import (ShuffleLocationSelector, TreasureChestLocationRow3, WorldAreaEnum)
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.area_objects import (NPC_3)
if TYPE_CHECKING:
    from randomizer.types.gameworld import (GameWorld)


class ForestMazeSecretTopMiddleChestLocation(TreasureChestLocationRow3):
    _bias = True
    _originally_held = FPFlowerPrize
    _rooms = [R234_FOREST_MAZE_SECRET]
    _npc_ids = [NPC_3]
    _id = ShuffleLocationSelector.FOREST_MAZE_SECRET_3
    _world_area = WorldAreaEnum.FOREST_MAZE
    _blacklist = [EXPStarPrize, SecondMimicFightLauncher, ThirdMimicFightLauncher, SlotsPrize]
    _hint = [
        # SetVarToConst(PRIMARY_TEMP_7000, 87),
        # RunDialog(
            # dialog_id=DI2010_DEBUG_7000,
            # above_object=BOWSER,
            # closable=True,
            # sync=False,
            # multiline=True,
            # use_background=True,
        # ),
        JmpIfBitClear(MAP_FOREST_MAZE, ["next"]),
        JmpIfObjectTriggerDisabledInSpecificLevel(
            NPC_3, R234_FOREST_MAZE_SECRET, ["next"]
        ),
        Jmp(["forest_maze_hint_text"]),
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_forest(world, inventory) and expect_halfway_decent_movement(world, inventory)


__all__ = ["ForestMazeSecretTopMiddleChestLocation"]
