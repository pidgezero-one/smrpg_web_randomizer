from __future__ import annotations
from typing import TYPE_CHECKING
from smrpgpatchbuilder.datatypes.overworld_scripts.event_scripts.commands import *
from randomizer.data.variables.room_names import *
from randomizer.data.variables.event_script_names import *
from randomizer.data.variables.action_script_names import *
from randomizer.data.variables.pack_names import *
from randomizer.logic.progression.prizes import *
from randomizer.types.flags import *
from randomizer.logic.progression.prizelocations.access import (can_clear_volcano)
from randomizer.logic.progression.prizelocations.barrel_volcano.volcano_bridge_boss_fight import (VolcanoBridgeBossFight)
from randomizer.types.logic import (Inventory)
from randomizer.types.prizelocation import (ShuffleLocationSelector, StarPieceLocation, WorldAreaEnum)
if TYPE_CHECKING:
    from randomizer.types.gameworld import (GameWorld)


class VolcanoBridgeStarPiece(StarPieceLocation):
    _bias = True
    _originally_held = None
    _rooms = [R352_VOLCANO_AREA_21_CZAR_DRAGONS_ROOM]
    _id = ShuffleLocationSelector.BARREL_VOLCANO_BOSS_1
    _world_area = WorldAreaEnum.BARREL_VOLCANO
    _parent = VolcanoBridgeBossFight
    _hint = [
        # SetVarToConst(PRIMARY_TEMP_7000, 375),
        # RunDialog(
            # dialog_id=DI2010_DEBUG_7000,
            # above_object=BOWSER,
            # closable=True,
            # sync=False,
            # multiline=True,
            # use_background=True,
        # ),
        JmpIfBitClear(MAP_BARREL_VOLCANO, ["next"]),
        JmpIfBitSet(VOLCANO_MIDBOSS_DEFEATED, ["next"]),
        Jmp(["barrel_volcano_hint_text"]),
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return super().can_access(inventory, world) and can_clear_volcano(
            world, inventory
        )


__all__ = ["VolcanoBridgeStarPiece"]
