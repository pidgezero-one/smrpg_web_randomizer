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
from randomizer.logic.progression.prizelocations.access import (can_clear_mines)
from randomizer.types.logic import (Inventory)
from randomizer.types.prizelocation import (KeyItemLocation, NPCLocationRow2, ShuffleLocationSelector, WorldAreaEnum)
if TYPE_CHECKING:
    from randomizer.types.gameworld import (GameWorld)


class PurtendStoreLocation(KeyItemLocation, NPCLocationRow2):
    _bias = True
    _originally_held = ProgressiveFireworksPrize
    _rooms = [R108_MOLEVILLE_OUTSIDE]
    _id = ShuffleLocationSelector.PURTEND_STORE
    _world_area = WorldAreaEnum.MOLEVILLE
    _hint = [
        # SetVarToConst(PRIMARY_TEMP_7000, 114),
        # RunDialog(
            # dialog_id=DI2010_DEBUG_7000,
            # above_object=BOWSER,
            # closable=True,
            # sync=False,
            # multiline=True,
            # use_background=True,
        # ),
        JmpIfBitClear(MINES_BOSS_2_DEFEATED, ["next"]),
        JmpIfBitSet(PURTEND_STORE_CHECK_DONE, ["next"]),
        JmpIfBitClear(PROGRESSIVE_FIREWORKS_ENABLED, ["next"]),
        StoreItemAmountTo7000(FireworksItem),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 1, ["moleville_hint_text"]),
        StoreItemAmountTo7000(ShinyStoneItem),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 1, ["moleville_hint_text"]),
        StoreItemAmountTo7000(CarboCookieItem),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 1, ["moleville_hint_text"]),
        JmpIfBitSet(CARBO_COOKIE_GIVEN, ["moleville_hint_text"]),
    ]
    _access_conditions = "Requires the inner Moleville Mines boss to be defeated. Not a check if \"Progressive Fireworks\" is disabled"

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_clear_mines(world, inventory) and inventory.has_item_count(
            ProgressiveFireworksPrize, 1
        )


__all__ = ["PurtendStoreLocation"]
