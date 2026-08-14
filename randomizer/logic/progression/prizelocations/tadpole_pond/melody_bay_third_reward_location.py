from __future__ import annotations
from typing import TYPE_CHECKING
from smrpgpatchbuilder.datatypes.overworld_scripts.event_scripts.commands import *
from randomizer.data.variables.room_names import *
from randomizer.data.variables.event_script_names import *
from randomizer.data.variables.action_script_names import *
from randomizer.data.variables.pack_names import *
from randomizer.logic.progression.prizes import *
from randomizer.types.flags import *
from randomizer.logic.progression.prizelocations.access import (can_access_temple_boss, can_clear_mines, not_earlygame, is_early_midgame, is_late_midgame, is_lategame)
from randomizer.types.logic import (Inventory)
from randomizer.types.prizelocation import (KeyItemLocation, NPCLocationRow3, ShuffleLocationSelector, WorldAreaEnum)
if TYPE_CHECKING:
    from randomizer.types.gameworld import (GameWorld)


class MelodyBayThirdRewardLocation(NPCLocationRow3, KeyItemLocation):
    _bias = True
    _originally_held = ProgressiveCardPrize
    _rooms = [R074_TADPOLE_POND_AREA_02]
    _id = ShuffleLocationSelector.MELODY_BAY_3
    _world_area = WorldAreaEnum.TADPOLE_POND
    _hint = [
        # SetVarToConst(PRIMARY_TEMP_7000, 55),
        # RunDialog(
            # dialog_id=DI2010_DEBUG_7000,
            # above_object=BOWSER,
            # closable=True,
            # sync=False,
            # multiline=True,
            # use_background=True,
        # ),
        JmpIfBitSet(MELODY_BAY_ITEM_3_GRANTED, ["next"]),
        JmpIfBitClear(MELODY_BAY_ITEM_2_GRANTED, ["next"]),
        JmpIfBitClear(TEMPLE_BOSS_DEFEATED, ["next"]),
        Jmp(["tadpole_pond_hint_text"]),
    ]
    _access_conditions = "Requires the Belome Temple boss to be defeated"

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return (
            can_clear_mines(world, inventory)
            and can_access_temple_boss(world, inventory)
            and not_earlygame(world, inventory)
        )


__all__ = ["MelodyBayThirdRewardLocation"]
