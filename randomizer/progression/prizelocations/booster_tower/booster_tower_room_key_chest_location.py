from __future__ import annotations
from typing import TYPE_CHECKING
from smrpgpatchbuilder.datatypes.overworld_scripts.event_scripts.commands import *
from randomizer.data.variables.room_names import *
from randomizer.data.variables.event_script_names import *
from randomizer.data.variables.action_script_names import *
from randomizer.data.variables.pack_names import *
from randomizer.progression.prizes import *
from randomizer.types.flags import *
from randomizer.data.variables.variable_names import (PRIMARY_TEMP_7000)
from randomizer.progression.prizelocations.access import (can_access_tower)
from randomizer.types.logic import (Inventory)
from randomizer.types.prizelocation import (ShuffleLocationSelector, TreasureChestLocationRow1, WorldAreaEnum)
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.area_objects import (NPC_0, NPC_6)
if TYPE_CHECKING:
    from randomizer.types.gameworld import (GameWorld)


class BoosterTowerRoomKeyChestLocation(TreasureChestLocationRow1):
    _bias = True
    _originally_held = ZoomShoesPrize
    _rooms = [R048_BOOSTER_TOWER_8F_AREA_02_ZOOM_SHOES_ROOM]
    _npc_ids = [NPC_0]
    _id = ShuffleLocationSelector.BOOSTER_TOWER_ZOOM_SHOES
    _world_area = WorldAreaEnum.BOOSTER_TOWER
    _blacklist = [EXPStarPrize, ThirdMimicFightLauncher]
    _monstro_shuffle = True
    _hint = [
        # SetVarToConst(PRIMARY_TEMP_7000, 162),
        # RunDialog(
            # dialog_id=DI2010_DEBUG_7000,
            # above_object=BOWSER,
            # closable=True,
            # sync=False,
            # multiline=True,
            # use_background=True,
        # ),
        JmpIfObjectTriggerDisabledInSpecificLevel(
            NPC_0, R048_BOOSTER_TOWER_8F_AREA_02_ZOOM_SHOES_ROOM, ["next"]
        ),
        JmpIfObjectNotInSpecificLevel(
            NPC_6,
            R041_BOOSTER_TOWER_8F_AREA_01_MINESWEEPER_ROOM_WCOINS_AND_HIDDEN_FIREBALLS,
            ["room_key_door_opened"],
        ),
        StoreItemAmountTo7000(RoomKeyItem),
        JmpIfVarNotEqualsConst(PRIMARY_TEMP_7000, 1, ["next"]),
        JmpIfBitSet(
            TOWER_OPENED, ["booster_tower_hint_text"], identifier="room_key_door_opened"
        ),
        JmpIfBitSet(TOWER_CHARACTER_RECRUITED, ["booster_tower_hint_text"]),
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_tower(world, inventory) and inventory.has_item(RoomKeyPrize)


__all__ = ["BoosterTowerRoomKeyChestLocation"]
