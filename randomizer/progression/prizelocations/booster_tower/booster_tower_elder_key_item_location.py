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
from randomizer.types.prizelocation import (ShuffleLocationSelector, StandingLocationRow1, WorldAreaEnum)
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.area_objects import (NPC_0, NPC_14)
if TYPE_CHECKING:
    from randomizer.types.gameworld import (GameWorld)


class BoosterTowerElderKeyItemLocation(StandingLocationRow1):
    _bias = True
    _originally_held = ChompPrize
    _rooms = [R200_BOOSTER_TOWER_6F_AREA_03_ELDERS_ROOM_WCHOMP]
    _npc_ids = [NPC_0]
    _id = ShuffleLocationSelector.BOOSTER_TOWER_CHOMP
    _world_area = WorldAreaEnum.BOOSTER_TOWER
    _monstro_shuffle = True
    _hint = [
        # SetVarToConst(PRIMARY_TEMP_7000, 145),
        # RunDialog(
            # dialog_id=DI2010_DEBUG_7000,
            # above_object=BOWSER,
            # closable=True,
            # sync=False,
            # multiline=True,
            # use_background=True,
        # ),
        JmpIfObjectNotInSpecificLevel(
            NPC_0, R200_BOOSTER_TOWER_6F_AREA_03_ELDERS_ROOM_WCHOMP, ["next"]
        ),
        JmpIfObjectNotInSpecificLevel(
            NPC_14,
            R195_BOOSTER_TOWER_6F_AREA_02_BOOSTERS_ANCESTOR_GAME_ROOM,
            ["elder_key_door_opened"],
        ),
        StoreItemAmountTo7000(ElderKeyItem),
        JmpIfVarNotEqualsConst(PRIMARY_TEMP_7000, 1, ["next"]),
        JmpIfBitSet(
            TOWER_OPENED,
            ["booster_tower_hint_text"],
            identifier="elder_key_door_opened",
        ),
        JmpIfBitSet(TOWER_CHARACTER_RECRUITED, ["booster_tower_hint_text"]),
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_tower(world, inventory) and inventory.has_item(ElderKeyPrize)


__all__ = ["BoosterTowerElderKeyItemLocation"]
