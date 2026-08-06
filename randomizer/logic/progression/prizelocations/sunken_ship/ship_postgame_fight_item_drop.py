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
from randomizer.logic.progression.prizelocations.access import (can_access_ship_postgame_boss)
from randomizer.types.logic import (Inventory)
from randomizer.types.prizelocation import (KeyItemLocation, NPCLocationRow1, ShuffleLocationSelector, WorldAreaEnum)
if TYPE_CHECKING:
    from randomizer.types.gameworld import (GameWorld)


class ShipPostgameFightItemDrop(KeyItemLocation, NPCLocationRow1):
    _bias = True
    _originally_held = ExtraShinyStonePrize
    _rooms = [R186_SUNKEN_SHIP_POSTKC_AREA_18_WARP_ROOM_FROM_JOHNNYS_ROOM]
    _id = ShuffleLocationSelector.SUNKEN_SHIP_POSTGAME_DROP
    _world_area = WorldAreaEnum.SUNKEN_SHIP
    _remake_only = True
    _blacklist = [RecoveryMushroomPrize]
    _hint = [
        # SetVarToConst(PRIMARY_TEMP_7000, 245),
        # RunDialog(
            # dialog_id=DI2010_DEBUG_7000,
            # above_object=BOWSER,
            # closable=True,
            # sync=False,
            # multiline=True,
            # use_background=True,
        # ),
        JmpIfBitClear(MAP_SEA, ["next"]),
        JmpIfBitSet(POSTGAME_SHIP_COMPLETED, ["next"]),
        JmpIfBitClear(SHIP_LIBERATED, ["next"]),
        JmpIfBitSet(STAY_VOUCHER_USED, ["sunken_ship_hint_text"]),
        StoreItemAmountTo7000(StayVoucherItem),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 0, ["next"]),
        Jmp(["marrymore_hotel_hint_text"]),
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_ship_postgame_boss(world, inventory)


__all__ = ["ShipPostgameFightItemDrop"]
