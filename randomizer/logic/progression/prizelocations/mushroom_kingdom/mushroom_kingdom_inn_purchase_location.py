from __future__ import annotations
from typing import TYPE_CHECKING
from smrpgpatchbuilder.datatypes.overworld_scripts.event_scripts.commands import *
from randomizer.data.variables.room_names import *
from randomizer.data.variables.event_script_names import *
from randomizer.data.variables.action_script_names import *
from randomizer.data.variables.pack_names import *
from randomizer.logic.progression.prizes import *
from randomizer.types.flags import *
from randomizer.logic.progression.prizelocations.access import (can_access_bandits_way, expect_good_movement, not_earlygame, expect_halfway_decent_movement, almost_earlygame, is_midgame, expect_ok_movement, lategame)
from randomizer.types.logic import (Inventory)
from randomizer.types.prizelocation import (KeyItemLocation, NPCLocationRow1, ShuffleLocationSelector, WorldAreaEnum)
if TYPE_CHECKING:
    from randomizer.types.gameworld import (GameWorld)


class MushroomKingdomInnPurchaseLocation(NPCLocationRow1, KeyItemLocation):
    _bias = True
    _originally_held = BeetlemaniaPrize
    _rooms = [
        R493_MUSHROOM_KINGDOM_INN_1F,
    ]
    _id = ShuffleLocationSelector.MUSHROOM_KINGDOM_INN
    _world_area = WorldAreaEnum.MUSHROOM_KINGDOM
    _hint = [
        # SetVarToConst(PRIMARY_TEMP_7000, 28),
        # RunDialog(
            # dialog_id=DI2010_DEBUG_7000,
            # above_object=BOWSER,
            # closable=True,
            # sync=False,
            # multiline=True,
            # use_background=True,
        # ),
        JmpIfBitSet(GAMEBOY_KID_PURCHASE_COMPLETE, ["next"]),
        JmpIfBitClear(MUSHROOM_KINGDOM_LIBERATED, ["next"]),
        Jmp(["mushroom_kingdom_hint_text"]),
    ]
    _access_conditions = "Requires the Mushroom Kingdom boss to be defeated. Not a check if \"Shuffle Beetlemania\" is disabled."

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_bandits_way(world, inventory)


__all__ = ["MushroomKingdomInnPurchaseLocation"]
