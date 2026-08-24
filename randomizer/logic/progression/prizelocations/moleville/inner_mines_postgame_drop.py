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
from randomizer.logic.progression.prizelocations.access import (can_access_moleville_postgame_boss, expect_good_movement, not_earlygame, expect_halfway_decent_movement, almost_earlygame, is_midgame, expect_ok_movement, lategame)
from randomizer.types.logic import (Inventory)
from randomizer.types.prizelocation import (NPCLocationRow1, ShuffleLocationSelector, WorldAreaEnum)
if TYPE_CHECKING:
    from randomizer.types.gameworld import (GameWorld)


class InnerMinesPostgameDrop(NPCLocationRow1):
    _bias = True
    _originally_held = WonderChompPrize
    _rooms = [R271_MOLEVILLE_MINES_AREA_17_PUNCHINELLOS_ROOM_AFTER_BATTLE]
    _id = ShuffleLocationSelector.MOLEVILLE_MINES_POSTGAME_DROP
    _world_area = WorldAreaEnum.MOLEVILLE
    _remake_only = True
    _monstro_shuffle = True
    _blacklist = [RecoveryMushroomPrize]
    _hint = [
        # SetVarToConst(PRIMARY_TEMP_7000, 130),
        # RunDialog(
            # dialog_id=DI2010_DEBUG_7000,
            # above_object=BOWSER,
            # closable=True,
            # sync=False,
            # multiline=True,
            # use_background=True,
        # ),
        JmpIfBitSet(MOLEVILLE_MINES_ENTRANCE_GATING, ["next"]),
        JmpIfBitSet(MINES_BACK_OPENED, ["__mines_boss_2_defeated_check"]),
        StoreItemAmountTo7000(BambinoBombItem),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 0, ["next"]),
        JmpIfBitClear(
            MINES_BOSS_2_DEFEATED, ["next"], identifier="__mines_boss_2_defeated_check"
        ),
        JmpIfBitSet(STAY_VOUCHER_USED, ["__mines_postgame_completed_check"]),
        StoreItemAmountTo7000(StayVoucherItem),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 0, ["next"]),
        Jmp(["marrymore_hotel_hint_text"]),
        JmpIfBitSet(
            MINES_POSTGAME_COMPLETED,
            ["next"],
            identifier="__mines_postgame_completed_check",
        ),
        Jmp(["mines_hint_text"]),
    ]
    _access_conditions = "Must first defeat the boss fight at inner Moleville and use the Stay Voucher. Not a check if \"Enable Remake content\" is turned off."


    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_moleville_postgame_boss(world, inventory)


__all__ = ["InnerMinesPostgameDrop"]
