from __future__ import annotations
from typing import TYPE_CHECKING
from smrpgpatchbuilder.datatypes.overworld_scripts.event_scripts.commands import *
from randomizer.data.variables.room_names import *
from randomizer.data.variables.event_script_names import *
from randomizer.data.variables.action_script_names import *
from randomizer.data.variables.pack_names import *
from randomizer.progression.prizes import *
from randomizer.types.flags import *
from randomizer.progression.prizelocations.access import (can_access_outer_nimbus)
from randomizer.types.logic import (Inventory)
from randomizer.types.prizelocation import (ShuffleLocationSelector, TreasureChestLocationRow1, WorldAreaEnum)
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.area_objects import (NPC_0)
if TYPE_CHECKING:
    from randomizer.types.gameworld import (GameWorld)


class NimbusShopChestLocation(TreasureChestLocationRow1):
    _bias = True
    _originally_held = FrogCoin1Prize
    _rooms = [R344_NIMBUS_LAND_ITEM_SHOP]
    _npc_ids = [NPC_0]
    _id = ShuffleLocationSelector.NIMBUS_LAND_SHOP
    _world_area = WorldAreaEnum.NIMBUS_LAND
    _blacklist = [EXPStarPrize]
    _hint = [
        # SetVarToConst(PRIMARY_TEMP_7000, 339),
        # RunDialog(
            # dialog_id=DI2010_DEBUG_7000,
            # above_object=BOWSER,
            # closable=True,
            # sync=False,
            # multiline=True,
            # use_background=True,
        # ),
        JmpIfBitClear(NIMBUS_MAINLAND_UNLOCKED, ["next"]),
        JmpIfObjectTriggerDisabledInSpecificLevel(
            NPC_0, R344_NIMBUS_LAND_ITEM_SHOP, ["next"]
        ),
        Jmp(["nimbus_land_hint_text"]),
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_outer_nimbus(world, inventory)


__all__ = ["NimbusShopChestLocation"]
