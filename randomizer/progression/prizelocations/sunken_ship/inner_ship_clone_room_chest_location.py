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
from randomizer.types.prize import (SlotsPrize)
from randomizer.types.prizelocation import (ShuffleLocationSelector, TreasureChestLocationRow1, WorldAreaEnum)
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.area_objects import (NPC_2)
if TYPE_CHECKING:
    from randomizer.types.gameworld import (GameWorld)


class InnerShipCloneRoomChestLocation(TreasureChestLocationRow1):
    _bias = True
    _originally_held = KerokeroColaPrize
    _rooms = [R179_SUNKEN_SHIP_POSTKC_AREA_06_MARIO_MIRROR_ROOM]
    _npc_ids = [NPC_2]
    _id = ShuffleLocationSelector.SUNKEN_SHIP_CLONE_ROOM
    _world_area = WorldAreaEnum.SUNKEN_SHIP
    _blacklist = [ThirdMimicFightLauncher, SlotsPrize]
    _hint = [
        # SetVarToConst(PRIMARY_TEMP_7000, 230),
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
            NPC_2, R179_SUNKEN_SHIP_POSTKC_AREA_06_MARIO_MIRROR_ROOM, ["next"]
        ),
        Jmp(["sunken_ship_hint_text"]),
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_clear_ship(world, inventory)


__all__ = ["InnerShipCloneRoomChestLocation"]
