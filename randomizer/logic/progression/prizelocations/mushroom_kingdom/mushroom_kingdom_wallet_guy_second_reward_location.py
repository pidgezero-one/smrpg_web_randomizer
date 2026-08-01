from __future__ import annotations
from typing import TYPE_CHECKING
from smrpgpatchbuilder.datatypes.overworld_scripts.event_scripts.commands import *
from randomizer.data.variables.room_names import *
from randomizer.data.variables.event_script_names import *
from randomizer.data.variables.action_script_names import *
from randomizer.data.variables.pack_names import *
from randomizer.logic.progression.prizes import *
from randomizer.types.flags import *
from randomizer.logic.progression.prizelocations.access import (can_clear_chapel)
from randomizer.types.logic import (Inventory)
from randomizer.types.prizelocation import (NPCLocationRow3, ShuffleLocationSelector, WorldAreaEnum)
if TYPE_CHECKING:
    from randomizer.types.gameworld import (GameWorld)


class MushroomKingdomWalletGuySecondRewardLocation(NPCLocationRow3):
    _bias = True
    _originally_held = FrogCoin1Prize
    _rooms = [
        R190_MUSHROOM_KINGDOM_DURING_MACK_OUTSIDE,
        R191_MUSHROOM_KINGDOM_OUTSIDE,
    ]
    _id = ShuffleLocationSelector.WALLET_GUY_2
    _world_area = WorldAreaEnum.MUSHROOM_KINGDOM
    _hint = [
        # SetVarToConst(PRIMARY_TEMP_7000, 21),
        # RunDialog(
            # dialog_id=DI2010_DEBUG_7000,
            # above_object=BOWSER,
            # closable=True,
            # sync=False,
            # multiline=True,
            # use_background=True,
        # ),
        JmpIfBitSet(SECOND_WALLET_PRIZE_RECEIVED, ["next"]),
        JmpIfBitClear(MARRYMORE_LIBERATED, ["next"]),
        JmpIfBitClear(RETURNED_WALLET, ["next"]),
        Jmp(["mushroom_kingdom_hint_text"]),
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_clear_chapel(world, inventory) and inventory.has_item(WalletPrize)


__all__ = ["MushroomKingdomWalletGuySecondRewardLocation"]
