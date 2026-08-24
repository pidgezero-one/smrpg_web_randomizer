from __future__ import annotations
from typing import TYPE_CHECKING
from smrpgpatchbuilder.datatypes.overworld_scripts.event_scripts.commands import *
from randomizer.data.variables.room_names import *
from randomizer.data.variables.event_script_names import *
from randomizer.data.variables.action_script_names import *
from randomizer.data.variables.pack_names import *
from randomizer.logic.progression.prizes import *
from randomizer.types.flags import *
from randomizer.data.variables.variable_names import (PRIMARY_TEMP_7000)
from randomizer.logic.progression.prizelocations.access import (can_clear_mines, expect_good_movement, not_earlygame, expect_halfway_decent_movement, almost_earlygame, is_midgame, expect_ok_movement, lategame)
from randomizer.logic.progression.prizelocations.moleville.inner_mines_boss_fight import (InnerMinesBossFight)
from randomizer.types.logic import (Inventory)
from randomizer.types.prizelocation import (ShuffleLocationSelector, StarPieceLocation, WorldAreaEnum)
if TYPE_CHECKING:
    from randomizer.types.gameworld import (GameWorld)


class InnerMinesStarPiece(StarPieceLocation):
    _bias = True
    _originally_held = StarPiece3
    _rooms = [R271_MOLEVILLE_MINES_AREA_17_PUNCHINELLOS_ROOM_AFTER_BATTLE]
    _id = ShuffleLocationSelector.MOLEVILLE_MINES_BOSS_2
    _world_area = WorldAreaEnum.MOLEVILLE
    _parent = InnerMinesBossFight
    _hint = [
        # SetVarToConst(PRIMARY_TEMP_7000, 127),
        # RunDialog(
            # dialog_id=DI2010_DEBUG_7000,
            # above_object=BOWSER,
            # closable=True,
            # sync=False,
            # multiline=True,
            # use_background=True,
        # ),
        JmpIfBitSet(MOLEVILLE_MINES_ENTRANCE_GATING, ["next"]),
        JmpIfBitSet(MINES_BOSS_2_DEFEATED, ["next"]),
        JmpIfBitSet(MINES_BACK_OPENED, ["mines_hint_text"]),
        StoreItemAmountTo7000(BambinoBombItem),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 1, ["mines_hint_text"]),
    ]
    # Flag as checked: MINES_BOSS_2_DEFEATED

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return super().can_access(inventory, world) and can_clear_mines(
            world, inventory
        )


__all__ = ["InnerMinesStarPiece"]
