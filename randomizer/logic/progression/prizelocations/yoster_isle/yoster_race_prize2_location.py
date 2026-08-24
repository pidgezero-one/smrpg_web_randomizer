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
from randomizer.logic.progression.prizelocations.access import (can_do_mushroom_derby, expect_good_movement, not_earlygame, expect_halfway_decent_movement, almost_earlygame, is_midgame, expect_ok_movement, lategame)
from randomizer.types.logic import (Inventory)
from randomizer.types.prizelocation import (NPCLocationRow3, ShuffleLocationSelector, WorldAreaEnum)
if TYPE_CHECKING:
    from randomizer.types.gameworld import (GameWorld)


class YosterRacePrize2Location(NPCLocationRow3):
    _bias = True
    _originally_held = YoshiCookiePrize
    _rooms = [R034_YOSTER_ISLE]
    _id = ShuffleLocationSelector.YOSTER_ISLE_RACE_REWARD_2
    _world_area = WorldAreaEnum.YOSTER_ISLE
    _hint = [
        # SetVarToConst(PRIMARY_TEMP_7000, 108),
        # RunDialog(
            # dialog_id=DI2010_DEBUG_7000,
            # above_object=BOWSER,
            # closable=True,
            # sync=False,
            # multiline=True,
            # use_background=True,
        # ),
        JmpIfBitSet(COMPLETED_MUSHROOM_DERBY, ["next"]),
        JmpIfBitSet(PIPE_VAULT_GATED, ["next"]),
        JmpIfBitClear(COOKIES_SHUFFLED, ["yoster_isle_hint_text"]),
        JmpIfBitSet(GOT_FREE_COOKIES, ["yoster_isle_hint_text"]),
        StoreItemAmountTo7000(CookiesItem),
        JmpIfVarNotEqualsConst(PRIMARY_TEMP_7000, 1, ["next"]),
        Jmp(["yoster_isle_hint_text"]),
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_do_mushroom_derby(world, inventory)


__all__ = ["YosterRacePrize2Location"]
