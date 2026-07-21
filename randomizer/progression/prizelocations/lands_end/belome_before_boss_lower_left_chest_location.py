from __future__ import annotations
from typing import TYPE_CHECKING
from smrpgpatchbuilder.datatypes.overworld_scripts.event_scripts.commands import *
from randomizer.data.variables.room_names import *
from randomizer.data.variables.event_script_names import *
from randomizer.data.variables.action_script_names import *
from randomizer.data.variables.pack_names import *
from randomizer.progression.prizes import *
from randomizer.types.flags import *
from randomizer.progression.prizelocations.access import (can_access_lands_end)
from randomizer.types.logic import (Inventory)
from randomizer.types.prizelocation import (ShuffleLocationSelector, TreasureChestLocationRow2, WorldAreaEnum)
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.area_objects import (NPC_1)
if TYPE_CHECKING:
    from randomizer.types.gameworld import (GameWorld)


class BelomeBeforeBossLowerLeftChestLocation(TreasureChestLocationRow2):
    _bias = True
    _originally_held = Coins150Prize
    _rooms = [R425_BELOME_TEMPLE_AREA_05_FROM_FORTUNE_ROOM]
    _npc_ids = [NPC_1]
    _id = ShuffleLocationSelector.BELOME_TEMPLE_AFTER_FORTUNE_2
    _world_area = WorldAreaEnum.TEMPLE
    _blacklist = [EXPStarPrize]
    _hint = [
        # SetVarToConst(PRIMARY_TEMP_7000, 266),
        # RunDialog(
            # dialog_id=DI2010_DEBUG_7000,
            # above_object=BOWSER,
            # closable=True,
            # sync=False,
            # multiline=True,
            # use_background=True,
        # ),
        JmpIfBitSet(LANDS_END_GATED, ["next"]),
        JmpIfObjectTriggerDisabledInSpecificLevel(
            NPC_1, R425_BELOME_TEMPLE_AREA_05_FROM_FORTUNE_ROOM, ["next"]
        ),
        Jmp(["belome_temple_hint_text"]),
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_lands_end(world, inventory)


__all__ = ["BelomeBeforeBossLowerLeftChestLocation"]
