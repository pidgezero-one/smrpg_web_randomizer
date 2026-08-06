from __future__ import annotations
from typing import TYPE_CHECKING
from smrpgpatchbuilder.datatypes.overworld_scripts.event_scripts.commands import *
from randomizer.data.variables.room_names import *
from randomizer.data.variables.event_script_names import *
from randomizer.data.variables.action_script_names import *
from randomizer.data.variables.pack_names import *
from randomizer.logic.progression.prizes import *
from randomizer.types.flags import *
from randomizer.logic.progression.prizelocations.access import (can_access_tower)
from randomizer.types.logic import (Inventory)
from randomizer.types.prizelocation import (KeyItemLocation, ShuffleLocationSelector, StandingLocationRow14, WorldAreaEnum)
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.area_objects import (NPC_5)
if TYPE_CHECKING:
    from randomizer.types.gameworld import (GameWorld)


class BoosterTowerCheckerboardRightmostItemLocation(
    KeyItemLocation, StandingLocationRow14
):
    _originally_held = RoomKeyPrize
    _rooms = [
        R041_BOOSTER_TOWER_8F_AREA_01_MINESWEEPER_ROOM_WCOINS_AND_HIDDEN_FIREBALLS
    ]
    _npc_ids = [NPC_5]
    _id = ShuffleLocationSelector.BOOSTER_TOWER_ROOM_KEY
    _world_area = WorldAreaEnum.BOOSTER_TOWER
    _hint = [
        # SetVarToConst(PRIMARY_TEMP_7000, 148),
        # RunDialog(
            # dialog_id=DI2010_DEBUG_7000,
            # above_object=BOWSER,
            # closable=True,
            # sync=False,
            # multiline=True,
            # use_background=True,
        # ),
        JmpIfObjectNotInSpecificLevel(
            NPC_5,
            R041_BOOSTER_TOWER_8F_AREA_01_MINESWEEPER_ROOM_WCOINS_AND_HIDDEN_FIREBALLS,
            ["next"],
        ),
        JmpIfBitSet(TOWER_OPENED, ["booster_tower_hint_text"]),
        JmpIfBitSet(TOWER_CHARACTER_RECRUITED, ["booster_tower_hint_text"]),
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_tower(world, inventory)


__all__ = ["BoosterTowerCheckerboardRightmostItemLocation"]
