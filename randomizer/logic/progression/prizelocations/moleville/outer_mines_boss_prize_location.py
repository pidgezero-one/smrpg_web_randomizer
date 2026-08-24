from __future__ import annotations
from typing import TYPE_CHECKING
from smrpgpatchbuilder.datatypes.overworld_scripts.event_scripts.commands import *
from randomizer.data.variables.room_names import *
from randomizer.data.variables.event_script_names import *
from randomizer.data.variables.action_script_names import *
from randomizer.data.variables.pack_names import *
from randomizer.logic.progression.prizes import *
from randomizer.types.flags import *
from randomizer.logic.progression.prizelocations.access import (can_access_moleville_entrance, expect_good_movement, not_earlygame, expect_halfway_decent_movement, almost_earlygame, is_midgame, expect_ok_movement, lategame)
from randomizer.types.logic import (Inventory)
from randomizer.types.prizelocation import (KeyItemLocation, NPCLocationRow1, ShuffleLocationSelector, WorldAreaEnum)
if TYPE_CHECKING:
    from randomizer.types.gameworld import (GameWorld)


class OuterMinesBossPrizeLocation(KeyItemLocation, NPCLocationRow1):
    _bias = True
    _originally_held = BambinoBombPrize
    _id = ShuffleLocationSelector.CROCO_2_ITEM
    _world_area = WorldAreaEnum.MOLEVILLE
    _rooms = [
        R273_MOLEVILLE_MINES_AREA_04_WTRAMPOLINE,
        R275_MOLEVILLE_MINES_AREA_06_SMALL_ROOM_LEADING_TO_AREA_06,
        R277_MOLEVILLE_MINES_AREA_05_LEFT_OF_TRAMPOLINE_ROOM,
        R279_MOLEVILLE_MINES_AREA_08_CROCOS_BOMBED_ROOM,
        R281_MOLEVILLE_MINES_AREA_07_FROM_CROCOS_BOMBED_ROOM,
        R283_MOLEVILLE_MINES_AREA_09_LEADS_LEFT_TO_CROCOS_BOMBED_ROOM,
    ]
    _blacklist = [RecoveryMushroomPrize]
    _hint = [
        # SetVarToConst(PRIMARY_TEMP_7000, 121),
        # RunDialog(
            # dialog_id=DI2010_DEBUG_7000,
            # above_object=BOWSER,
            # closable=True,
            # sync=False,
            # multiline=True,
            # use_background=True,
        # ),
        JmpIfBitSet(MOLEVILLE_MINES_ENTRANCE_GATING, ["next"]),
        JmpIfBitSet(MINES_BOSS_1_DEFEATED, ["next"]),
        Jmp(["mines_hint_text"]),
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_moleville_entrance(world, inventory) and almost_earlygame(world, inventory)


__all__ = ["OuterMinesBossPrizeLocation"]
