from __future__ import annotations
from typing import TYPE_CHECKING
from smrpgpatchbuilder.datatypes.overworld_scripts.event_scripts.commands import *
from randomizer.data.variables.room_names import *
from randomizer.data.variables.event_script_names import *
from randomizer.data.variables.action_script_names import *
from randomizer.data.variables.pack_names import *
from randomizer.logic.progression.prizes import *
from randomizer.types.flags import *
from randomizer.logic.progression.prizelocations.access import (can_clear_ship)
from randomizer.logic.progression.prizelocations.sunken_ship.ship_password_boss_fight import (ShipPasswordBossFight)
from randomizer.types.logic import (Inventory)
from randomizer.types.prizelocation import (ShuffleLocationSelector, StarPieceLocation, WorldAreaEnum)
if TYPE_CHECKING:
    from randomizer.types.gameworld import (GameWorld)


class ShipPasswordStarPiece(StarPieceLocation):
    _bias = True
    _originally_held = None
    _rooms = [R173_SUNKEN_SHIP_POSTKC_AREA_01_SMALL_ROOM_WTRAMPOLINE]
    _id = ShuffleLocationSelector.SUNKEN_SHIP_MIDBOSS
    _world_area = WorldAreaEnum.SUNKEN_SHIP
    _parent = ShipPasswordBossFight
    _hint = [
        # SetVarToConst(PRIMARY_TEMP_7000, 227),
        # RunDialog(
            # dialog_id=DI2010_DEBUG_7000,
            # above_object=BOWSER,
            # closable=True,
            # sync=False,
            # multiline=True,
            # use_background=True,
        # ),
        JmpIfBitClear(MAP_SEA, ["next"]),
        JmpIfBitSet(SHIP_MIDBOSS_COMPLETED, ["next"]),
        Jmp(["sunken_ship_hint_text"]),
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return super().can_access(inventory, world) and can_clear_ship(world, inventory)


__all__ = ["ShipPasswordStarPiece"]
