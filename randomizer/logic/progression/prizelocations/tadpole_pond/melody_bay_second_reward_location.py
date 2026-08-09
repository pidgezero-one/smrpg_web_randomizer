from __future__ import annotations
from typing import TYPE_CHECKING
from smrpgpatchbuilder.datatypes.overworld_scripts.event_scripts.commands import *
from randomizer.data.variables.room_names import *
from randomizer.data.variables.event_script_names import *
from randomizer.data.variables.action_script_names import *
from randomizer.data.variables.pack_names import *
from randomizer.logic.progression.prizes import *
from randomizer.types.flags import *
from randomizer.logic.progression.prizelocations.access import (can_clear_mines)
from randomizer.types.logic import (Inventory)
from randomizer.types.prizelocation import (KeyItemLocation, NPCLocationRow2, ShuffleLocationSelector, WorldAreaEnum)
if TYPE_CHECKING:
    from randomizer.types.gameworld import (GameWorld)


class MelodyBaySecondRewardLocation(NPCLocationRow2, KeyItemLocation):
    _bias = True
    _originally_held = ProgressiveCardPrize
    _rooms = [R074_TADPOLE_POND_AREA_02]
    _id = ShuffleLocationSelector.MELODY_BAY_2
    _world_area = WorldAreaEnum.TADPOLE_POND
    _hint = [
        # SetVarToConst(PRIMARY_TEMP_7000, 54),
        # RunDialog(
            # dialog_id=DI2010_DEBUG_7000,
            # above_object=BOWSER,
            # closable=True,
            # sync=False,
            # multiline=True,
            # use_background=True,
        # ),
        JmpIfBitSet(MELODY_BAY_ITEM_2_GRANTED, ["next"]),
        JmpIfBitClear(MELODY_BAY_ITEM_1_GRANTED, ["next"]),
        JmpIfBitClear(MINES_BOSS_2_DEFEATED, ["next"]),
        Jmp(["tadpole_pond_hint_text"]),
    ]
    _access_conditions = "Requires the inner Moleville Mines boss to be defeated"

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_clear_mines(world, inventory)


__all__ = ["MelodyBaySecondRewardLocation"]
