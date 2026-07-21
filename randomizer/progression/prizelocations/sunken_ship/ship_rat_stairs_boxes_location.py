from __future__ import annotations
from typing import TYPE_CHECKING
from smrpgpatchbuilder.datatypes.overworld_scripts.event_scripts.commands import *
from randomizer.data.variables.room_names import *
from randomizer.data.variables.event_script_names import *
from randomizer.data.variables.action_script_names import *
from randomizer.data.variables.pack_names import *
from randomizer.progression.prizes import *
from randomizer.types.flags import *
from randomizer.progression.prizelocations.access import (can_access_sea)
from randomizer.types.logic import (Inventory)
from randomizer.types.packet_type import (PacketType)
from randomizer.types.prize import (FPFlowerPrize)
from randomizer.types.prizelocation import (PacketLocationRow1, ShuffleLocationSelector, WorldAreaEnum)
if TYPE_CHECKING:
    from randomizer.types.gameworld import (GameWorld)


class ShipRatStairsBoxesLocation(PacketLocationRow1):
    _bias = True
    _originally_held = FPFlowerPrize
    _replace = "spawn_ship_box_item"
    _rooms = [R167_SUNKEN_SHIP_AREA_05_LONG_STAIRWELL_WITH_RUNNING_ALLEY_RATS]
    _world_area = WorldAreaEnum.SUNKEN_SHIP
    _packet_type = PacketType.CHEST
    _packet_id = P037_SHIP_STAIRCASE
    _id = ShuffleLocationSelector.SUNKEN_SHIP_RAT_STAIRS_FLOWER
    _hint = [
        # SetVarToConst(PRIMARY_TEMP_7000, 219),
        # RunDialog(
            # dialog_id=DI2010_DEBUG_7000,
            # above_object=BOWSER,
            # closable=True,
            # sync=False,
            # multiline=True,
            # use_background=True,
        # ),
        JmpIfBitClear(MAP_SEA, ["next"]),
        JmpIfBitSet(SHIP_STAIRWAY_FREESTANDING_ITEM_OBTAINED, ["next"]),
        Jmp(["sunken_ship_hint_text"]),
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_sea(world, inventory)


__all__ = ["ShipRatStairsBoxesLocation"]
