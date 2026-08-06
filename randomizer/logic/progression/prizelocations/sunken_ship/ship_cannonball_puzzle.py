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
from randomizer.types.packet_type import (PacketType)
from randomizer.types.prizelocation import (PacketLocationRow1, ShuffleLocationSelector, WorldAreaEnum)
if TYPE_CHECKING:
    from randomizer.types.gameworld import (GameWorld)


class ShipCannonballPuzzle(PacketLocationRow1):
    _autoterminate_packet = True
    _bias = True
    _originally_held = MushroomPrize
    _replace = "spawn_ship_cannonball_item"
    _rooms = [R172_SUNKEN_SHIP_PUZZLE_ROOM_5]
    _world_area = WorldAreaEnum.SUNKEN_SHIP
    _packet_type = PacketType.FALLING
    _packet_id = P035_SUNKEN_SHIP_CANNONBALL_PUZZLE
    _id = ShuffleLocationSelector.SUNKEN_SHIP_CANNONBALL_PUZZLE
    _hint = [
        # SetVarToConst(PRIMARY_TEMP_7000, 225),
        # RunDialog(
            # dialog_id=DI2010_DEBUG_7000,
            # above_object=BOWSER,
            # closable=True,
            # sync=False,
            # multiline=True,
            # use_background=True,
        # ),
        JmpIfBitClear(MAP_SEA, ["next"]),
        JmpIfBitSet(SHIP_CANNONBALL_PRIZE, ["next"]),
        Jmp(["sunken_ship_hint_text"]),
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_sea(world, inventory)


__all__ = ["ShipCannonballPuzzle"]
