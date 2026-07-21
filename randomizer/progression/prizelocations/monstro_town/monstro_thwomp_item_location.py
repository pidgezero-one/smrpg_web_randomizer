from __future__ import annotations
from typing import TYPE_CHECKING
from smrpgpatchbuilder.datatypes.overworld_scripts.event_scripts.commands import *
from randomizer.data.variables.room_names import *
from randomizer.data.variables.event_script_names import *
from randomizer.data.variables.action_script_names import *
from randomizer.data.variables.pack_names import *
from randomizer.progression.prizes import *
from randomizer.types.flags import *
from randomizer.progression.prizelocations.access import (can_access_monstro_town)
from randomizer.types.logic import (Inventory)
from randomizer.types.prizelocation import (KeyItemLocation, ShuffleLocationSelector, StandingLocationRow1, WorldAreaEnum)
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.area_objects import (NPC_0)
if TYPE_CHECKING:
    from randomizer.types.gameworld import (GameWorld)


class MonstroThwompItemLocation(KeyItemLocation, StandingLocationRow1):
    _bias = True
    _originally_held = TempleKeyPrize
    _rooms = [R324_MONSTRO_TOWN_OUTSIDE]
    _npc_ids = [NPC_0]
    _id = ShuffleLocationSelector.MONSTRO_TOWN_THWOMP
    _world_area = WorldAreaEnum.MONSTRO_TOWN
    _hint = [
        # SetVarToConst(PRIMARY_TEMP_7000, 288),
        # RunDialog(
        #     dialog_id=DI2010_DEBUG_7000,
        #     above_object=BOWSER,
        #     closable=True,
        #     sync=False,
        #     multiline=True,
        #     use_background=True,
        # ),
        JmpIfObjectNotInSpecificLevel(NPC_0, R324_MONSTRO_TOWN_OUTSIDE, ["next"]),
        JmpIfBitSet(MAP_MONSTRO_TOWN, ["monstro_town_hint_text"]),
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_monstro_town(world, inventory)


__all__ = ["MonstroThwompItemLocation"]
