from __future__ import annotations
from typing import TYPE_CHECKING
from smrpgpatchbuilder.datatypes.overworld_scripts.event_scripts.commands import *
from randomizer.data.variables.room_names import *
from randomizer.data.variables.event_script_names import *
from randomizer.data.variables.action_script_names import *
from randomizer.data.variables.pack_names import *
from randomizer.progression.prizes import *
from randomizer.types.flags import *
from randomizer.data.physical_objects.items import (BigCoinObject, DefaultItem, FlowerObject, FrogCoinObject, RecoveryMushroomObject, SmallCoinObject, SmallFrogCoinObject)
from randomizer.data.variables.variable_names import (PRIMARY_TEMP_7000)
from randomizer.progression.prizelocations.access import (can_access_lands_end)
from randomizer.types.logic import (Inventory)
from randomizer.types.prize import (FPFlowerPrize)
from randomizer.types.prizelocation import (ShuffleLocationSelector, StandingLocationRow1, WorldAreaEnum)
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.area_objects import (NPC_0)
if TYPE_CHECKING:
    from randomizer.types.gameworld import (GameWorld)


class BelomeTempleTreasuryUpperCornerLeftItemLocation(StandingLocationRow1):
    _bias = True
    _originally_held = FPFlowerPrize
    _rooms = [R422_BELOME_TEMPLE_AREA_09_BELOMES_TREASURE_ROOM]
    _npc_ids = [NPC_0]
    _id = ShuffleLocationSelector.BELOME_TEMPLE_TREASURE_FLOWER_1
    _world_area = WorldAreaEnum.TEMPLE
    _model_allowlist = [
        DefaultItem,
        FrogCoinItemObject,
        FrogCoinObject,
        SmallFrogCoinObject,
        FlowerItemObject,
        RecoveryMushroomObject,
        CoinStillObject,
        FlowerObject,
        SmallCoinItemObject,
        SmallCoinStillObject,
    ]
    _hint = [
        # SetVarToConst(PRIMARY_TEMP_7000, 269),
        # RunDialog(
            # dialog_id=DI2010_DEBUG_7000,
            # above_object=BOWSER,
            # closable=True,
            # sync=False,
            # multiline=True,
            # use_background=True,
        # ),
        JmpIfBitSet(LANDS_END_GATED, ["next"]),
        JmpIfObjectNotInSpecificLevel(
            NPC_0, R422_BELOME_TEMPLE_AREA_09_BELOMES_TREASURE_ROOM, ["next"]
        ),
        JmpIfBitSet(TEMPLE_KEY_USED, ["belome_temple_hint_text"]),
        StoreItemAmountTo7000(TempleKeyItem),
        JmpIfVarNotEqualsConst(PRIMARY_TEMP_7000, 1, ["next"]),
        Jmp(["belome_temple_hint_text"]),
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_lands_end(world, inventory) and inventory.has_item(
            TempleKeyPrize
        )


__all__ = ["BelomeTempleTreasuryUpperCornerLeftItemLocation"]
