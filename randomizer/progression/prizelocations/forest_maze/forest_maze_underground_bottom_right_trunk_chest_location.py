from __future__ import annotations
from typing import TYPE_CHECKING
from smrpgpatchbuilder.datatypes.overworld_scripts.event_scripts.commands import *
from randomizer.data.variables.room_names import *
from randomizer.data.variables.event_script_names import *
from randomizer.data.variables.action_script_names import *
from randomizer.data.variables.pack_names import *
from randomizer.progression.prizes import *
from randomizer.types.flags import *
from randomizer.progression.prizelocations.access import (can_access_forest)
from randomizer.types.logic import (Inventory)
from randomizer.types.prize import (CoinPrize, FPFlowerPrize, FrogCoinPrize, SlotsPrize)
from randomizer.types.prizelocation import (ShuffleLocationSelector, TreasureChestLocationRow2, WorldAreaEnum)
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.area_objects import (NPC_3)
if TYPE_CHECKING:
    from randomizer.types.gameworld import (GameWorld)


class ForestMazeUndergroundBottomRightTrunkChestLocation(TreasureChestLocationRow2):
    _bias = True
    _originally_held = FPFlowerPrize
    _rooms = [R242_FOREST_MAZE_ALL_TREE_TRUNK_UNDERGROUND_AREAS]
    _npc_ids = [NPC_3]
    _id = ShuffleLocationSelector.FOREST_MAZE_UNDERGROUND_2
    _world_area = WorldAreaEnum.FOREST_MAZE
    _blacklist = [
        SecondMimicFightLauncher,
        ThirdMimicFightLauncher,
        FrogCoinPrize,
        CoinPrize,
        SlotsPrize
    ]
    _hint = [
        # SetVarToConst(PRIMARY_TEMP_7000, 82),
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
            NPC_3, R242_FOREST_MAZE_ALL_TREE_TRUNK_UNDERGROUND_AREAS, ["next"]
        ),
        Jmp(["forest_maze_hint_text"]),
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_forest(world, inventory)


__all__ = ["ForestMazeUndergroundBottomRightTrunkChestLocation"]
