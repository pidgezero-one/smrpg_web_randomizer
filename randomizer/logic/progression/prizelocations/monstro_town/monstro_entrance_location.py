from __future__ import annotations
from typing import TYPE_CHECKING
from smrpgpatchbuilder.datatypes.overworld_scripts.event_scripts.commands import *
from randomizer.data.variables.room_names import *
from randomizer.data.variables.event_script_names import *
from randomizer.data.variables.action_script_names import *
from randomizer.data.variables.pack_names import *
from randomizer.logic.progression.prizes import *
from randomizer.types.flags import *
from randomizer.logic.progression.prizelocations.access import (can_access_monstro_town)
from randomizer.types.logic import (Inventory)
from randomizer.types.prizelocation import (ShuffleLocationSelector, TreasureChestLocationRow1, WorldAreaEnum)
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.area_objects import (NPC_1)
if TYPE_CHECKING:
    from randomizer.types.gameworld import (GameWorld)


class MonstroEntranceLocation(TreasureChestLocationRow1):
    _bias = True
    _originally_held = FrogCoin1Prize
    _rooms = [R267_MONSTRO_TOWN_ENTRANCE]
    _npc_ids = [NPC_1]
    _id = ShuffleLocationSelector.MONSTRO_TOWN_ENTRANCE
    _world_area = WorldAreaEnum.MONSTRO_TOWN
    _blacklist = [EXPStarPrize]
    _hint = [
        # SetVarToConst(PRIMARY_TEMP_7000, 287),
        # RunDialog(
        #     dialog_id=DI2010_DEBUG_7000,
        #     above_object=BOWSER,
        #     closable=True,
        #     sync=False,
        #     multiline=True,
        #     use_background=True,
        # ),
        JmpIfObjectTriggerDisabledInSpecificLevel(
            NPC_1, R267_MONSTRO_TOWN_ENTRANCE, ["next"]
        ),
        JmpIfBitSet(MAP_MONSTRO_TOWN, ["monstro_town_hint_text"]),
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_monstro_town(world, inventory)


__all__ = ["MonstroEntranceLocation"]
