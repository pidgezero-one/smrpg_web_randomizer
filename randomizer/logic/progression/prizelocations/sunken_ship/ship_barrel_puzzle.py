from __future__ import annotations
from typing import TYPE_CHECKING
from smrpgpatchbuilder.datatypes.overworld_scripts.event_scripts.commands import *
from randomizer.data.variables.room_names import *
from randomizer.data.variables.event_script_names import *
from randomizer.data.variables.action_script_names import *
from randomizer.data.variables.pack_names import *
from randomizer.logic.progression.prizes import *
from randomizer.types.flags import *
from randomizer.logic.progression.prizelocations.access import (can_access_sea, expect_good_movement, not_earlygame, expect_halfway_decent_movement, almost_earlygame, is_midgame, expect_ok_movement, lategame, can_access_early_ship, can_clear_ship)
from randomizer.types.logic import (Inventory)
from randomizer.types.packet_type import (PacketType)
from randomizer.types.prizelocation import (PacketLocationRow1, ShuffleLocationSelector, WorldAreaEnum)
if TYPE_CHECKING:
    from randomizer.types.gameworld import (GameWorld)


class ShipBarrelPuzzle(PacketLocationRow1):
    _autoterminate_packet = True
    _bias = True
    _originally_held = RecoveryMushroomPrize
    _replace = "spawn_ship_barrel_item"
    _rooms = [R176_SUNKEN_SHIP_AREA_08_WSAVE_POINT_AND_GREEN_SWITCH_FOR_BARREL]
    _world_area = WorldAreaEnum.SUNKEN_SHIP
    _packet_type = PacketType.FALLING
    _packet_id = P036_BARREL_PUZZLE_PRIZE
    _id = ShuffleLocationSelector.SUNKEN_SHIP_BARREL_PUZZLE
    _hint = [
        # SetVarToConst(PRIMARY_TEMP_7000, 226),
        # RunDialog(
            # dialog_id=DI2010_DEBUG_7000,
            # above_object=BOWSER,
            # closable=True,
            # sync=False,
            # multiline=True,
            # use_background=True,
        # ),
        JmpIfBitClear(MAP_SEA, ["next"]),
        JmpIfBitSet(UNKNOWN_707D_5, ["next"]),
        Jmp(["sunken_ship_hint_text"]),
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_early_ship(world, inventory)


__all__ = ["ShipBarrelPuzzle"]
