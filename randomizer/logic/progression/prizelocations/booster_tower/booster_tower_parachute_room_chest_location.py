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
from randomizer.types.prizelocation import (ShuffleLocationSelector, TreasureChestLocationRow1, WorldAreaEnum)
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.area_objects import (NPC_9)
if TYPE_CHECKING:
    from randomizer.types.gameworld import (GameWorld)


class BoosterTowerParachuteRoomChestLocation(TreasureChestLocationRow1):
    _bias = True
    _originally_held = FrogCoin1Prize
    _rooms = [R035_BOOSTER_TOWER_7F_3LEVEL_WPARACHUTING_SPOOKUMS]
    _npc_ids = [NPC_9]
    _id = ShuffleLocationSelector.BOOSTER_TOWER_PARACHUTE
    _world_area = WorldAreaEnum.BOOSTER_TOWER
    _blacklist = [EXPStarPrize, ThirdMimicFightLauncher]
    _hint = [
        # SetVarToConst(PRIMARY_TEMP_7000, 146),
        # RunDialog(
            # dialog_id=DI2010_DEBUG_7000,
            # above_object=BOWSER,
            # closable=True,
            # sync=False,
            # multiline=True,
            # use_background=True,
        # ),
        JmpIfObjectTriggerDisabledInSpecificLevel(
            NPC_9, R035_BOOSTER_TOWER_7F_3LEVEL_WPARACHUTING_SPOOKUMS, ["next"]
        ),
        JmpIfBitSet(TOWER_OPENED, ["booster_tower_hint_text"]),
        JmpIfBitSet(TOWER_CHARACTER_RECRUITED, ["booster_tower_hint_text"]),
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_tower(world, inventory)


__all__ = ["BoosterTowerParachuteRoomChestLocation"]
