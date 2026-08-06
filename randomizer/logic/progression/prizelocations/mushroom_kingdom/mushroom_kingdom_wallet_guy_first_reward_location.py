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
from randomizer.types.logic import (Inventory)
from randomizer.types.prizelocation import (NPCLocationRow2, ShuffleLocationSelector, WorldAreaEnum)
if TYPE_CHECKING:
    from randomizer.types.gameworld import (GameWorld)


class MushroomKingdomWalletGuyFirstRewardLocation(NPCLocationRow2):
    _originally_held = FlowerTabPrize
    _rooms = [
        R190_MUSHROOM_KINGDOM_DURING_MACK_OUTSIDE,
        R191_MUSHROOM_KINGDOM_OUTSIDE,
    ]
    _id = ShuffleLocationSelector.WALLET_GUY_1
    _world_area = WorldAreaEnum.MUSHROOM_KINGDOM
    _hint = [
        # SetVarToConst(PRIMARY_TEMP_7000, 20),
        # RunDialog(
            # dialog_id=DI2010_DEBUG_7000,
            # above_object=BOWSER,
            # closable=True,
            # sync=False,
            # multiline=True,
            # use_background=True,
        # ),
        JmpIfBitSet(RETURNED_WALLET, ["next"]),
        StoreItemAmountTo7000(WalletItem),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 0, ["next"]),
        Jmp(["mushroom_kingdom_hint_text"]),
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return inventory.has_item(WalletPrize)


__all__ = ["MushroomKingdomWalletGuyFirstRewardLocation"]
