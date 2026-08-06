from __future__ import annotations
from typing import TYPE_CHECKING
from smrpgpatchbuilder.datatypes.overworld_scripts.event_scripts.commands import *
from randomizer.data.variables.room_names import *
from randomizer.data.variables.event_script_names import *
from randomizer.data.variables.action_script_names import *
from randomizer.data.variables.pack_names import *
from randomizer.logic.progression.prizes import *
from randomizer.types.flags import *
from randomizer.logic.progression.prizelocations.access import (can_access_sea)
from randomizer.types.logic import (Inventory)
from randomizer.types.prize import (SlotsPrize)
from randomizer.types.prizelocation import (ShuffleLocationSelector, TreasureChestLocationRow1, WorldAreaEnum)
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.area_objects import (NPC_0)
if TYPE_CHECKING:
    from randomizer.types.gameworld import (GameWorld)


class SeaWhirlpoolChestLocation(TreasureChestLocationRow1):
    _bias = True
    _originally_held = MaxMushroomPrize
    _rooms = [R133_SEA_AREA_06_WATER_ROOM_WWHIRLPOOLS]
    _npc_ids = [NPC_0]
    _id = ShuffleLocationSelector.SEA_WHIRLPOOL_CHEST
    _world_area = WorldAreaEnum.SEA
    _blacklist = [EXPStarPrize, ThirdMimicFightLauncher, SlotsPrize]
    _hint = [
        # SetVarToConst(PRIMARY_TEMP_7000, 217),
        # RunDialog(
            # dialog_id=DI2010_DEBUG_7000,
            # above_object=BOWSER,
            # closable=True,
            # sync=False,
            # multiline=True,
            # use_background=True,
        # ),
        JmpIfBitClear(MAP_SEA, ["next"]),
        JmpIfObjectTriggerDisabledInSpecificLevel(
            NPC_0, R133_SEA_AREA_06_WATER_ROOM_WWHIRLPOOLS, ["next"]
        ),
        Jmp(["sea_hint_text"]),
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_sea(world, inventory)


__all__ = ["SeaWhirlpoolChestLocation"]
