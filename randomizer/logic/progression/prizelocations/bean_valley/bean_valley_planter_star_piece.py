from __future__ import annotations
from typing import TYPE_CHECKING
from smrpgpatchbuilder.datatypes.overworld_scripts.event_scripts.commands import *
from randomizer.data.variables.room_names import *
from randomizer.data.variables.event_script_names import *
from randomizer.data.variables.action_script_names import *
from randomizer.data.variables.pack_names import *
from randomizer.logic.progression.prizes import *
from randomizer.types.flags import *
from randomizer.logic.progression.prizelocations.access import (not_earlygame, is_early_midgame, is_late_midgame, is_lategame)
from randomizer.logic.progression.prizelocations.bean_valley.bean_valley_planter_boss_fight import (BeanValleyPlanterBossFight)
from randomizer.types.logic import (Inventory)
from randomizer.types.prizelocation import (ShuffleLocationSelector, StarPieceLocation, WorldAreaEnum)
if TYPE_CHECKING:
    from randomizer.types.gameworld import (GameWorld)


class BeanValleyPlanterStarPiece(StarPieceLocation):
    _bias = True
    _originally_held = None
    _rooms = [R254_BEAN_VALLEY_SMILAX_AREA]
    _id = ShuffleLocationSelector.BEAN_VALLEY_BOSS
    _world_area = WorldAreaEnum.BEAN_VALLEY
    _parent = BeanValleyPlanterBossFight
    _hint = [
        # SetVarToConst(PRIMARY_TEMP_7000, 314),
        # RunDialog(
            # dialog_id=DI2010_DEBUG_7000,
            # above_object=BOWSER,
            # closable=True,
            # sync=False,
            # multiline=True,
            # use_background=True,
        # ),
        JmpIfBitSet(BEAN_VALLEY_BOSS_DEFEATED, ["next"]),
        Jmp(["bean_valley_hint_text"]),
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return super().can_access(inventory, world) and not_earlygame(world, inventory)


__all__ = ["BeanValleyPlanterStarPiece"]
