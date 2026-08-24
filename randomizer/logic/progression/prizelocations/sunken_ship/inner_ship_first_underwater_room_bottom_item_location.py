from __future__ import annotations
from typing import TYPE_CHECKING
from smrpgpatchbuilder.datatypes.overworld_scripts.event_scripts.commands import *
from randomizer.data.variables.room_names import *
from randomizer.data.variables.event_script_names import *
from randomizer.data.variables.action_script_names import *
from randomizer.data.variables.pack_names import *
from randomizer.logic.progression.prizes import *
from randomizer.types.flags import *
from randomizer.data.physical_objects.items import (BigCoinObject, DefaultItem, FlowerObject, FrogCoinObject, KeyObject, RecoveryMushroomObject, SmallCoinObject, SmallFrogCoinObject)
from randomizer.logic.progression.prizelocations.access import (can_clear_ship, expect_good_movement, not_earlygame, expect_halfway_decent_movement, almost_earlygame, is_midgame, expect_ok_movement, lategame, can_access_early_ship)
from randomizer.types.logic import (Inventory)
from randomizer.types.prizelocation import (ShuffleLocationSelector, StandingLocationRow1, WorldAreaEnum)
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.area_objects import (NPC_0)
if TYPE_CHECKING:
    from randomizer.types.gameworld import (GameWorld)


class InnerShipFirstUnderwaterRoomBottomItemLocation(StandingLocationRow1):
    _bias = True
    _originally_held = FrogCoin1Prize
    _rooms = [R187_SUNKEN_SHIP_POSTKC_AREA_10_WATER_ROOM_WITH_FROG_COINS]
    _npc_ids = [NPC_0]
    _id = ShuffleLocationSelector.SUNKEN_SHIP_UNDERWATER_FROG_COIN_1
    _world_area = WorldAreaEnum.SUNKEN_SHIP
    _model_allowlist = [DefaultItem, FlowerObject, KeyObject, RecoveryMushroomObject, FrogCoinObject, SmallFrogCoinObjectNoMoney, SmallFrogCoinObject, SmallCoinObject, BigCoinObject]
    _hint = [
        # SetVarToConst(PRIMARY_TEMP_7000, 237),
        # RunDialog(
            # dialog_id=DI2010_DEBUG_7000,
            # above_object=BOWSER,
            # closable=True,
            # sync=False,
            # multiline=True,
            # use_background=True,
        # ),
        JmpIfBitClear(MAP_SEA, ["next"]),
        JmpIfObjectNotInSpecificLevel(
            NPC_0, R187_SUNKEN_SHIP_POSTKC_AREA_10_WATER_ROOM_WITH_FROG_COINS, ["next"]
        ),
        Jmp(["sunken_ship_hint_text"]),
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_clear_ship(world, inventory)


__all__ = ["InnerShipFirstUnderwaterRoomBottomItemLocation"]
