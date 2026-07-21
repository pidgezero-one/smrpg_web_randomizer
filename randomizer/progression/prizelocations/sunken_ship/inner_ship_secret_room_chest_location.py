from __future__ import annotations
from typing import TYPE_CHECKING
from smrpgpatchbuilder.datatypes.overworld_scripts.event_scripts.commands import *
from randomizer.data.variables.room_names import *
from randomizer.data.variables.event_script_names import *
from randomizer.data.variables.action_script_names import *
from randomizer.data.variables.pack_names import *
from randomizer.progression.prizes import *
from randomizer.types.flags import *
from randomizer.progression.prizelocations.access import (can_clear_ship)
from randomizer.types.logic import (Inventory)
from randomizer.types.prizelocation import (ShuffleLocationSelector, TreasureChestLocationRow1, WorldAreaEnum)
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.area_objects import (NPC_0)
if TYPE_CHECKING:
    from randomizer.types.gameworld import (GameWorld)


class InnerShipSecretRoomChestLocation(TreasureChestLocationRow1):
    _bias = True
    _originally_held = SafetyRingPrize
    _rooms = [R185_SUNKEN_SHIP_POSTKC_AREA_14_SECRET_SAFETY_RING]
    _npc_ids = [NPC_0]
    _id = ShuffleLocationSelector.SUNKEN_SHIP_SAFETY_RING
    _world_area = WorldAreaEnum.SUNKEN_SHIP
    _blacklist = [EXPStarPrize, ThirdMimicFightLauncher]
    _hint = [
        # SetVarToConst(PRIMARY_TEMP_7000, 241),
        # RunDialog(
            # dialog_id=DI2010_DEBUG_7000,
            # above_object=BOWSER,
            # closable=True,
            # sync=False,
            # multiline=True,
            # use_background=True,
        # ),
        JmpIfBitClear(MAP_SEA, ["next"]),
        JmpIfObjectTriggerDisabledInSpecificLevel(
            NPC_0, R185_SUNKEN_SHIP_POSTKC_AREA_14_SECRET_SAFETY_RING, ["next"]
        ),
        Jmp(["sunken_ship_hint_text"]),
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_clear_ship(world, inventory)


__all__ = ["InnerShipSecretRoomChestLocation"]
