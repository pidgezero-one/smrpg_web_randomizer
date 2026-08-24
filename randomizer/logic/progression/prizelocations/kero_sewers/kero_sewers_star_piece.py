from __future__ import annotations
from typing import TYPE_CHECKING
from smrpgpatchbuilder.datatypes.overworld_scripts.event_scripts.commands import *
from randomizer.data.variables.room_names import *
from randomizer.data.variables.event_script_names import *
from randomizer.data.variables.action_script_names import *
from randomizer.data.variables.pack_names import *
from randomizer.logic.progression.prizes import *
from randomizer.types.flags import *
from randomizer.logic.progression.prizelocations.access import (can_access_sewer, expect_good_movement, not_earlygame, expect_halfway_decent_movement, almost_earlygame, is_midgame, expect_ok_movement, lategame)
from randomizer.logic.progression.prizelocations.kero_sewers.kero_sewers_boss_fight import (KeroSewersBossFight)
from randomizer.types.logic import (Inventory)
from randomizer.types.prizelocation import (ShuffleLocationSelector, StarPieceLocation, WorldAreaEnum)
if TYPE_CHECKING:
    from randomizer.types.gameworld import (GameWorld)


class KeroSewersStarPiece(StarPieceLocation):
    _bias = True
    _originally_held = None
    _rooms = [R301_KERO_SEWERS_AREA_07_WATER_SWITCH_ROOM_WBOOS]
    _id = ShuffleLocationSelector.KERO_SEWERS_STAR_PIECE
    _world_area = WorldAreaEnum.KERO_SEWERS
    _parent = KeroSewersBossFight
    _hint = [
        # SetVarToConst(PRIMARY_TEMP_7000, 46),
        # RunDialog(
            # dialog_id=DI2010_DEBUG_7000,
            # above_object=BOWSER,
            # closable=True,
            # sync=False,
            # multiline=True,
            # use_background=True,
        # ),
        JmpIfBitClear(SEWERS_CLOSED, ["sewers_closed_check_6"]),
        JmpIfBitSet(LANDS_END_GATED, ["next"]),
        JmpIfBitSet(SEWER_BOSS_DEFEATED, ["next"], identifier="sewers_closed_check_6"),
        Jmp(["kero_sewers_hint_text"]),
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return super().can_access(inventory, world) and can_access_sewer(
            world, inventory
        )


__all__ = ["KeroSewersStarPiece"]
