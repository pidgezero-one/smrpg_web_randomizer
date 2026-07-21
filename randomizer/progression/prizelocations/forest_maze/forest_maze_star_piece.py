from __future__ import annotations
from typing import TYPE_CHECKING
from smrpgpatchbuilder.datatypes.overworld_scripts.event_scripts.commands import *
from randomizer.data.variables.room_names import *
from randomizer.data.variables.event_script_names import *
from randomizer.data.variables.action_script_names import *
from randomizer.data.variables.pack_names import *
from randomizer.progression.prizes import *
from randomizer.types.flags import *
from randomizer.progression.prizelocations.access import (can_clear_forest)
from randomizer.progression.prizelocations.forest_maze.forest_maze_boss_fight import (ForestMazeBossFight)
from randomizer.types.logic import (Inventory)
from randomizer.types.prizelocation import (ShuffleLocationSelector, StarPieceLocation, WorldAreaEnum)
if TYPE_CHECKING:
    from randomizer.types.gameworld import (GameWorld)


class ForestMazeStarPiece(StarPieceLocation):
    _bias = True
    _originally_held = StarPiece2
    _rooms = [R232_FOREST_MAZE_BOWYERS_PRACTICE_PAD]
    _id = ShuffleLocationSelector.FOREST_MAZE_STAR_PIECE
    _world_area = WorldAreaEnum.FOREST_MAZE
    _parent = ForestMazeBossFight
    _hint = [
        # SetVarToConst(PRIMARY_TEMP_7000, 90),
        # RunDialog(
            # dialog_id=DI2010_DEBUG_7000,
            # above_object=BOWSER,
            # closable=True,
            # sync=False,
            # multiline=True,
            # use_background=True,
        # ),
        JmpIfBitSet(FOREST_LIBERATED, ["next"]),
        JmpIfBitClear(MAP_FOREST_MAZE, ["next"]),
        Jmp(["forest_maze_hint_text"]),
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return super().can_access(inventory, world) and can_clear_forest(
            world, inventory
        )


__all__ = ["ForestMazeStarPiece"]
