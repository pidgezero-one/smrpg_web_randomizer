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
from randomizer.logic.progression.prizelocations.access import (can_access_temple_postgame_boss, expect_good_movement, not_earlygame, expect_halfway_decent_movement, almost_earlygame, is_midgame, expect_ok_movement, lategame, can_dodge_lands_end_enemies, can_pass_whirlpools, can_access_temple)
from randomizer.types.logic import (Inventory)
from randomizer.types.prizelocation import (NPCLocationRow1, ShuffleLocationSelector, WorldAreaEnum)
if TYPE_CHECKING:
    from randomizer.types.gameworld import (GameWorld)


class TemplePostgameFightItemDrop(NPCLocationRow1):
    _bias = True
    _originally_held = SageStickPrize
    _rooms = [R293_BELOME_3_ROOM]
    _id = ShuffleLocationSelector.BELOME_TEMPLE_BOSS_POSTGAME_DROP
    _world_area = WorldAreaEnum.TEMPLE
    _remake_only = True
    _monstro_shuffle = True
    _hint = [
        # SetVarToConst(PRIMARY_TEMP_7000, 286),
        # RunDialog(
            # dialog_id=DI2010_DEBUG_7000,
            # above_object=BOWSER,
            # closable=True,
            # sync=False,
            # multiline=True,
            # use_background=True,
        # ),
        JmpIfBitSet(LANDS_END_GATED, ["next"]),
        JmpIfBitSet(TEMPLE_POSTGAME_BOSS_DEFEATED, ["next"]),
        JmpIfBitSet(STAY_VOUCHER_USED, ["belome3_voucher_used2"]),
        StoreItemAmountTo7000(StayVoucherItem),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 0, ["next"]),
        Jmp(["marrymore_hotel_hint_text"]),
        JmpIfBitSet(
            TEMPLE_BOSS_DEFEATED,
            ["belome_temple_hint_text"],
            identifier="belome3_voucher_used2",
        ),
        JmpIfBitClear(TEMPLE_BOSS_GATED, ["belome_temple_hint_text"]),
        StoreItemAmountTo7000(TempleKeyItem),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 0, ["next"]),
        Jmp(["belome_temple_hint_text"]),
    ]
    _access_conditions = "Must first defeat the boss fight at Belome Temple and use the Stay Voucher. Not a check if \"Enable Remake content\" is turned off."


    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_temple_postgame_boss(world, inventory)


__all__ = ["TemplePostgameFightItemDrop"]
