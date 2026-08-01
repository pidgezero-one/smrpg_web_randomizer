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
from randomizer.types.prize import (FPFlowerPrize)
from randomizer.types.prizelocation import (PacketLocationRow1, ShuffleLocationSelector, WorldAreaEnum)
if TYPE_CHECKING:
    from randomizer.types.gameworld import (GameWorld)


class ShipTrampolinePuzzle(PacketLocationRow1):
    _autoterminate_packet = True
    _bias = True
    _originally_held = FPFlowerPrize
    _replace = "spawn_ship_trampoline_item"
    _rooms = [R163_SUNKEN_SHIP_PUZZLE_ROOM_2]
    _world_area = WorldAreaEnum.SUNKEN_SHIP
    _packet_type = PacketType.FALLING
    _packet_id = P026_SUNKEN_SHIP_TRAMPOLINE_PUZZLE
    _id = ShuffleLocationSelector.SUNKEN_SHIP_TRAMPOLINE_PUZZLE
    _hint = [
        # SetVarToConst(PRIMARY_TEMP_7000, 221),
        # RunDialog(
            # dialog_id=DI2010_DEBUG_7000,
            # above_object=BOWSER,
            # closable=True,
            # sync=False,
            # multiline=True,
            # use_background=True,
        # ),
        JmpIfBitClear(MAP_SEA, ["next"]),
        JmpIfBitSet(UNKNOWN_707D_1, ["next"]),
        Jmp(["sunken_ship_hint_text"]),
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_sea(world, inventory)


__all__ = ["ShipTrampolinePuzzle"]
