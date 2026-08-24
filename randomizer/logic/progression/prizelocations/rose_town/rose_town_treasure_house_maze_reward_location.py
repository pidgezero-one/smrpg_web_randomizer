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
from randomizer.types.prizelocation import (NPCLocationRow1, ShuffleLocationSelector, WorldAreaEnum)
if TYPE_CHECKING:
    from randomizer.types.gameworld import (GameWorld)


class RoseTownTreasureHouseMazeRewardLocation(NPCLocationRow1):
    _bias = True
    _originally_held = FrogCoin1Prize
    _rooms = [
        R093_ROSE_TOWN_DURING_BOWYER_TREASURE_HOUSE_1F,
        R094_ROSE_TOWN_TREASURE_HOUSE_1F,
    ]
    _id = ShuffleLocationSelector.ROSE_TOWN_TREASURE_HOUSE_MAZE_REWARD
    _world_area = WorldAreaEnum.ROSE_TOWN
    _blacklist = [EXPStarPrize]
    _hint = [
        # SetVarToConst(PRIMARY_TEMP_7000, 77),
        # RunDialog(
            # dialog_id=DI2010_DEBUG_7000,
            # above_object=BOWSER,
            # closable=True,
            # sync=False,
            # multiline=True,
            # use_background=True,
        # ),
        JmpIfBitSet(TREASURE_HUNTER_HOUSE_PRIZE, ["next"]),
        JmpIfBitClear(MAP_FOREST_MAZE, ["next"]),
        JmpIfBitClear(FOREST_MAZE_SECRET_FOUND, ["forest_maze_hint_text"]),
        Jmp(["rose_town_hint_text"]),
    ]
    _access_conditions = "Requires you to have visited the Forest Maze secret. Does not require the Forest Maze boss to be defeated"

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_forest(world, inventory) and expect_halfway_decent_movement(world, inventory)


__all__ = ["RoseTownTreasureHouseMazeRewardLocation"]
