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
from randomizer.types.prizelocation import (ShuffleLocationSelector, StandingLocationRow1, WorldAreaEnum)
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.area_objects import (NPC_0, NPC_1, NPC_10, NPC_11, NPC_12, NPC_13, NPC_14, NPC_15, NPC_16, NPC_2, NPC_3, NPC_4, NPC_5, NPC_6, NPC_7, NPC_8, NPC_9)
if TYPE_CHECKING:
    from randomizer.types.gameworld import (GameWorld)


class ShipCoinSnakePuzzleLocation(StandingLocationRow1):
    _bias = True
    _originally_held = Coins150Prize
    _rooms = [
        R171_SUNKEN_SHIP_PUZZLE_ROOM_4,
        R171_SUNKEN_SHIP_PUZZLE_ROOM_4,
        R171_SUNKEN_SHIP_PUZZLE_ROOM_4,
        R171_SUNKEN_SHIP_PUZZLE_ROOM_4,
        R171_SUNKEN_SHIP_PUZZLE_ROOM_4,
        R171_SUNKEN_SHIP_PUZZLE_ROOM_4,
        R171_SUNKEN_SHIP_PUZZLE_ROOM_4,
        R171_SUNKEN_SHIP_PUZZLE_ROOM_4,
        R171_SUNKEN_SHIP_PUZZLE_ROOM_4,
        R171_SUNKEN_SHIP_PUZZLE_ROOM_4,
        R171_SUNKEN_SHIP_PUZZLE_ROOM_4,
        R171_SUNKEN_SHIP_PUZZLE_ROOM_4,
        R171_SUNKEN_SHIP_PUZZLE_ROOM_4,
        R171_SUNKEN_SHIP_PUZZLE_ROOM_4,
        R171_SUNKEN_SHIP_PUZZLE_ROOM_4,
        R171_SUNKEN_SHIP_PUZZLE_ROOM_4,
        R171_SUNKEN_SHIP_PUZZLE_ROOM_4,
    ]
    _world_area = WorldAreaEnum.SUNKEN_SHIP
    _npc_ids = [
        NPC_0,
        NPC_1,
        NPC_2,
        NPC_3,
        NPC_4,
        NPC_5,
        NPC_6,
        NPC_7,
        NPC_8,
        NPC_9,
        NPC_10,
        NPC_11,
        NPC_12,
        NPC_13,
        NPC_14,
        NPC_15,
        NPC_16,
    ]
    _id = ShuffleLocationSelector.SUNKEN_SHIP_COIN_SNAKE
    _hint = [
        # SetVarToConst(PRIMARY_TEMP_7000, 224),
        # RunDialog(
            # dialog_id=DI2010_DEBUG_7000,
            # above_object=BOWSER,
            # closable=True,
            # sync=False,
            # multiline=True,
            # use_background=True,
        # ),
        JmpIfBitClear(MAP_SEA, ["next"]),
        JmpIfBitSet(SHIP_COIN_PRIZE, ["next"]),
        Jmp(["sunken_ship_hint_text"]),
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_early_ship(world, inventory)

__all__ = ["ShipCoinSnakePuzzleLocation"]
