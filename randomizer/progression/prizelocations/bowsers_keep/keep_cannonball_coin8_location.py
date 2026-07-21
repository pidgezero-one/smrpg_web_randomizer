from __future__ import annotations
from typing import TYPE_CHECKING
from smrpgpatchbuilder.datatypes.overworld_scripts.event_scripts.commands import *
from randomizer.data.variables.room_names import *
from randomizer.data.variables.event_script_names import *
from randomizer.data.variables.action_script_names import *
from randomizer.data.variables.pack_names import *
from randomizer.progression.prizes import *
from randomizer.types.flags import *
from randomizer.progression.prizelocations.access import (can_pass_obstacle_courses)
from randomizer.types.logic import (Inventory)
from randomizer.types.prizelocation import (ShuffleLocationSelector, StandingLocationRow8, WorldAreaEnum)
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.area_objects import (NPC_15)
if TYPE_CHECKING:
    from randomizer.types.gameworld import (GameWorld)


class KeepCannonballCoin8Location(StandingLocationRow8):
    _bias = True
    _originally_held = Coins10Prize
    _rooms = [R457_BOWSERS_KEEP_6DOOR_ACTION_ROOM_2B_CANNONBALL_RIDING]
    _npc_ids = [NPC_15]
    _id = ShuffleLocationSelector.BOWSERS_KEEP_CANNONBALL_ROOM_COIN_8
    _world_area = WorldAreaEnum.BOWSERS_KEEP
    _hint = [
        # SetVarToConst(PRIMARY_TEMP_7000, 405),
        # RunDialog(
            # dialog_id=DI2010_DEBUG_7000,
            # above_object=BOWSER,
            # closable=True,
            # sync=False,
            # multiline=True,
            # use_background=True,
        # ),
        # JmpIfBitSet(MAP_DIRECTIONAL_NIMBUS_LAND_VISTA_HILL, ["next"]),
        # JmpIfObjectNotInSpecificLevel(NPC_15, R457_BOWSERS_KEEP_6DOOR_ACTION_ROOM_2B_CANNONBALL_RIDING, ["next"]),
        # Jmp(["keep_obstacle_hint_text"])
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_pass_obstacle_courses(world, inventory)


__all__ = ["KeepCannonballCoin8Location"]
