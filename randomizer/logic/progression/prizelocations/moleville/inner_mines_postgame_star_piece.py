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
from randomizer.logic.progression.prizelocations.moleville.inner_mines_postgame_boss_fight import (InnerMinesPostgameBossFight)
from randomizer.types.logic import (Inventory)
from randomizer.types.prizelocation import (ShuffleLocationSelector, StarPieceLocation, WorldAreaEnum)
if TYPE_CHECKING:
    from randomizer.types.gameworld import (GameWorld)


class InnerMinesPostgameStarPiece(StarPieceLocation):
    _bias = True
    _originally_held = None
    _rooms = [R271_MOLEVILLE_MINES_AREA_17_PUNCHINELLOS_ROOM_AFTER_BATTLE]
    _override_id = 527
    _id = ShuffleLocationSelector.MOLEVILLE_MINES_BOSS_3
    _world_area = WorldAreaEnum.MOLEVILLE
    _remake_only = True
    _parent = InnerMinesPostgameBossFight
    _hint = [
        # SetVarToConst(PRIMARY_TEMP_7000, 129),
        # RunDialog(
            # dialog_id=DI2010_DEBUG_7000,
            # above_object=BOWSER,
            # closable=True,
            # sync=False,
            # multiline=True,
            # use_background=True,
        # ),
        JmpIfBitSet(MOLEVILLE_MINES_ENTRANCE_GATING, ["next"]),
        JmpIfBitSet(MINES_BACK_OPENED, ["_mines_boss_2_defeated_check"]),
        StoreItemAmountTo7000(BambinoBombItem),
        JmpIfVarNotEqualsConst(PRIMARY_TEMP_7000, 1, ["next"]),
        JmpIfBitClear(
            MINES_BOSS_2_DEFEATED, ["next"], identifier="_mines_boss_2_defeated_check"
        ),
        JmpIfBitSet(STAY_VOUCHER_USED, ["_mines_postgame_completed_check"]),
        StoreItemAmountTo7000(StayVoucherItem),
        JmpIfVarNotEqualsConst(PRIMARY_TEMP_7000, 1, ["next"]),
        Jmp(["marrymore_hotel_hint_text"]),
        JmpIfBitSet(
            MINES_POSTGAME_COMPLETED,
            ["next"],
            identifier="_mines_postgame_completed_check",
        ),
        Jmp(["mines_hint_text"]),
    ]
    _access_conditions = "Must first defeat the boss fight at inner Moleville and use the Stay Voucher. Not a check if \"Enable Remake content\" is turned off."


    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return super().can_access(
            inventory, world
        ) and can_access_moleville_postgame_boss(world, inventory)


__all__ = ["InnerMinesPostgameStarPiece"]
