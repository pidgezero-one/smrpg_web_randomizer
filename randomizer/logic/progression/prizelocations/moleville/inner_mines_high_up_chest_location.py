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
from randomizer.logic.progression.prizelocations.access import (can_access_inner_mines, expect_good_movement, not_earlygame, expect_halfway_decent_movement, almost_earlygame, is_midgame, expect_ok_movement, lategame)
from randomizer.types.logic import (Inventory)
from randomizer.types.prize import (FPFlowerPrize)
from randomizer.types.prizelocation import (ShuffleLocationSelector, TreasureChestLocationRow2, WorldAreaEnum)
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.area_objects import (NPC_1)
if TYPE_CHECKING:
    from randomizer.types.gameworld import (GameWorld)


class InnerMinesHighUpChestLocation(TreasureChestLocationRow2):
    _bias = True
    _originally_held = FPFlowerPrize
    _rooms = [R288_MOLEVILLE_MINES_AREA_16_LARGE_SAVEPOINT_ROOM_WFOUR_BOBOMBS]
    _npc_ids = [NPC_1]
    _id = ShuffleLocationSelector.MOLEVILLE_MINES_PUNCHINELLO_2
    _world_area = WorldAreaEnum.MOLEVILLE
    _blacklist = [EXPStarPrize, ThirdMimicFightLauncher, InfiniteCoinsPrize]
    _hint = [
        # SetVarToConst(PRIMARY_TEMP_7000, 126),
        # RunDialog(
            # dialog_id=DI2010_DEBUG_7000,
            # above_object=BOWSER,
            # closable=True,
            # sync=False,
            # multiline=True,
            # use_background=True,
        # ),
        JmpIfBitSet(MOLEVILLE_MINES_ENTRANCE_GATING, ["next"]),
        JmpIfObjectTriggerDisabledInSpecificLevel(
            NPC_1,
            R288_MOLEVILLE_MINES_AREA_16_LARGE_SAVEPOINT_ROOM_WFOUR_BOBOMBS,
            ["next"],
        ),
        JmpIfBitSet(MINES_BACK_OPENED, ["mines_hint_text"]),
        StoreItemAmountTo7000(BambinoBombItem),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 1, ["mines_hint_text"]),
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_inner_mines(world, inventory)


__all__ = ["InnerMinesHighUpChestLocation"]
