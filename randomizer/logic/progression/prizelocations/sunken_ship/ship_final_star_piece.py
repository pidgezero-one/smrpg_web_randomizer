from __future__ import annotations
from typing import TYPE_CHECKING
from smrpgpatchbuilder.datatypes.overworld_scripts.event_scripts.commands import *
from randomizer.data.variables.room_names import *
from randomizer.data.variables.event_script_names import *
from randomizer.data.variables.action_script_names import *
from randomizer.data.variables.pack_names import *
from randomizer.logic.progression.prizes import *
from randomizer.types.flags import *
from randomizer.logic.progression.prizelocations.access import (can_clear_ship, expect_good_movement, not_earlygame, expect_halfway_decent_movement, almost_earlygame, is_midgame, expect_ok_movement, lategame, can_access_early_ship)
from randomizer.logic.progression.prizelocations.sunken_ship.ship_final_boss_fight import (ShipFinalBossFight)
from randomizer.types.logic import (Inventory)
from randomizer.types.prizelocation import (ShuffleLocationSelector, StarPieceLocation, WorldAreaEnum)
if TYPE_CHECKING:
    from randomizer.types.gameworld import (GameWorld)


class ShipFinalStarPiece(StarPieceLocation):
    _bias = True
    _originally_held = None
    _rooms = [R028_SUNKEN_SHIP_POSTKC_AREA_17_JOHNNYS_ROOM]
    _id = ShuffleLocationSelector.SUNKEN_SHIP_BOSS
    _world_area = WorldAreaEnum.SUNKEN_SHIP
    _parent = ShipFinalBossFight
    _hint = [
        # SetVarToConst(PRIMARY_TEMP_7000, 244),
        # RunDialog(
            # dialog_id=DI2010_DEBUG_7000,
            # above_object=BOWSER,
            # closable=True,
            # sync=False,
            # multiline=True,
            # use_background=True,
        # ),
        JmpIfBitClear(MAP_SEA, ["next"]),
        JmpIfBitSet(SHIP_LIBERATED, ["next"]),
        Jmp(["sunken_ship_hint_text"]),
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return super().can_access(inventory, world) and can_clear_ship(world, inventory)


__all__ = ["ShipFinalStarPiece"]
