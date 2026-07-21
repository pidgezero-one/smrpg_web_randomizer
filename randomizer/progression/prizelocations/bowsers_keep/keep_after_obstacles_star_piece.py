from __future__ import annotations
from typing import TYPE_CHECKING
from smrpgpatchbuilder.datatypes.overworld_scripts.event_scripts.commands import *
from randomizer.data.variables.room_names import *
from randomizer.data.variables.event_script_names import *
from randomizer.data.variables.action_script_names import *
from randomizer.data.variables.pack_names import *
from randomizer.progression.prizes import *
from randomizer.types.flags import *
from randomizer.progression.prizelocations.access import (can_pass_obstacle_courses, not_earlygame)
from randomizer.progression.prizelocations.bowsers_keep.keep_after_obstacles_boss_fight import (KeepAfterObstaclesBossFight)
from randomizer.types.logic import (Inventory)
from randomizer.types.prizelocation import (ShuffleLocationSelector, StarPieceLocation, WorldAreaEnum)
if TYPE_CHECKING:
    from randomizer.types.gameworld import (GameWorld)


class KeepAfterObstaclesStarPiece(StarPieceLocation):
    _bias = True
    _originally_held = None
    _rooms = [R266_BOWSERS_KEEP_AREA_10_MAGIKOOPAS_ROOM]
    _id = ShuffleLocationSelector.BOWSERS_KEEP_BOSS_1
    _world_area = WorldAreaEnum.BOWSERS_KEEP
    _parent = KeepAfterObstaclesBossFight
    _hint = [
        # SetVarToConst(PRIMARY_TEMP_7000, 419),
        # RunDialog(
            # dialog_id=DI2010_DEBUG_7000,
            # above_object=BOWSER,
            # closable=True,
            # sync=False,
            # multiline=True,
            # use_background=True,
        # ),
        JmpIfBitSet(MAP_DIRECTIONAL_NIMBUS_LAND_VISTA_HILL, ["next"]),
        JmpIfBitSet(KEEP_BOSS_1_DEFEATED, ["next"]),
        Jmp(["bowsers_keep_hint_text"]),
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_pass_obstacle_courses(world, inventory) and not_earlygame(
            world, inventory
        )


__all__ = ["KeepAfterObstaclesStarPiece"]
