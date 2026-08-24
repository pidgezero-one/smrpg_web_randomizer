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
from randomizer.logic.progression.prizelocations.access import (can_do_tower_curtain_game, expect_good_movement, not_earlygame, expect_halfway_decent_movement, almost_earlygame, is_midgame, expect_ok_movement, lategame)
from randomizer.types.logic import (Inventory)
from randomizer.types.prizelocation import (KeyItemLocation, NPCLocationRow1, ShuffleLocationSelector, WorldAreaEnum)
if TYPE_CHECKING:
    from randomizer.types.gameworld import (GameWorld)


class BoosterTowerKnifeGuyPrizeLocation(KeyItemLocation, NPCLocationRow1):
    _bias = True
    _originally_held = BrightCardPrize
    _rooms = [R039_BOOSTER_TOWER_5F_KNIFE_GUYS_ROOM]
    _id = ShuffleLocationSelector.BOOSTER_TOWER_KNIFE_GUY
    _world_area = WorldAreaEnum.BOOSTER_TOWER
    _hint = [
        # SetVarToConst(PRIMARY_TEMP_7000, 142),
        # RunDialog(
            # dialog_id=DI2010_DEBUG_7000,
            # above_object=BOWSER,
            # closable=True,
            # sync=False,
            # multiline=True,
            # use_background=True,
        # ),
        JmpIfBitSet(TOWER_OPENED, ["returned_mario_doll_check"]),
        JmpIfBitSet(TOWER_CHARACTER_RECRUITED, ["returned_mario_doll_check"]),
        Jmp(["next"]),
        JmpIfBitClear(
            MARIO_DOLL_SHUFFLE_ENABLED,
            ["tower_boss_2_check"],
            identifier="returned_mario_doll_check",
        ),
        JmpIfBitSet(RETURNED_MARIO_DOLL, ["tower_boss_2_check"]),
        StoreItemAmountTo7000(MarioDollItem),
        JmpIfVarNotEqualsConst(PRIMARY_TEMP_7000, 1, ["next"]),
        JmpIfBitSet(KNIFE_GUY_PRIZE_GRANTED, ["next"], identifier="tower_boss_2_check"),
        Jmp(["booster_tower_hint_text"]),
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_do_tower_curtain_game(world, inventory)


__all__ = ["BoosterTowerKnifeGuyPrizeLocation"]
