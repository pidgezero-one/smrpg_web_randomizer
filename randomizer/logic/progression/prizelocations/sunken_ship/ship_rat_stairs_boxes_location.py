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
from randomizer.types.prize import (FPFlowerPrize)
from randomizer.types.prizelocation import (NPCLocationRow1, PacketLocation, ShuffleLocationSelector, WorldAreaEnum)
if TYPE_CHECKING:
    from randomizer.types.gameworld import (GameWorld)


# NPC grant path + cosmetic packet: the packet is only the picture here. Action
# script 875 -> 992 already despawns it, so nothing needs the freestanding
# grant's ActionQueueSync on $70A8 - which targeted room 167's NPC_5, an
# EMPTY_NPC declared visible=False that is never summoned.
class ShipRatStairsBoxesLocation(NPCLocationRow1, PacketLocation):
    _container_event = E0253_NPC_QUEST_1_GRANT
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
        return can_access_early_ship(world, inventory)


__all__ = ["ShipRatStairsBoxesLocation"]
