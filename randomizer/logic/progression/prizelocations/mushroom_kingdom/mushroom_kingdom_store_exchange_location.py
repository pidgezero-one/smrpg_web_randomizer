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
from randomizer.logic.progression.prizelocations.access import (can_access_bandits_way)
from randomizer.types.logic import (Inventory)
from randomizer.types.prizelocation import (KeyItemLocation, NPCLocationRow2, ShuffleLocationSelector, WorldAreaEnum)
if TYPE_CHECKING:
    from randomizer.types.gameworld import (GameWorld)


class MushroomKingdomStoreExchangeLocation(NPCLocationRow2, KeyItemLocation):
    _bias = True
    _originally_held = CricketPiePrize
    _rooms = [
        R483_MUSHROOM_KINGDOM_DURING_MACK_ITEM_SHOP_TOP_FLOOR,
        R491_MUSHROOM_KINGDOM_ITEM_SHOP_TOP_FLOOR,
    ]
    _id = ShuffleLocationSelector.MUSHROOM_KINGDOM_STORE_EXCHANGE
    _world_area = WorldAreaEnum.MUSHROOM_KINGDOM
    _hint = [
        # SetVarToConst(PRIMARY_TEMP_7000, 27),
        # RunDialog(
            # dialog_id=DI2010_DEBUG_7000,
            # above_object=BOWSER,
            # closable=True,
            # sync=False,
            # multiline=True,
            # use_background=True,
        # ),
        JmpIfBitSet(RARE_FROG_COIN_EXCHANGED, ["next"]),
        JmpIfBitClear(MUSHROOM_KINGDOM_LIBERATED, ["next"]),
        StoreItemAmountTo7000(RareFrogCoinItem),
        JmpIfVarNotEqualsConst(PRIMARY_TEMP_7000, 1, ["next"]),
        Jmp(["mushroom_kingdom_hint_text"]),
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_bandits_way(world, inventory) and inventory.has_item(
            RareFrogCoinPrize
        )


__all__ = ["MushroomKingdomStoreExchangeLocation"]
