from __future__ import annotations
from typing import TYPE_CHECKING
from smrpgpatchbuilder.datatypes.overworld_scripts.event_scripts.commands import *
from randomizer.data.variables.room_names import *
from randomizer.data.variables.event_script_names import *
from randomizer.data.variables.action_script_names import *
from randomizer.data.variables.pack_names import *
from randomizer.progression.prizes import *
from randomizer.types.flags import *
from randomizer.progression.prizelocations.access import (can_access_bandits_way)
from randomizer.types.logic import (Inventory)
from randomizer.types.prizelocation import (ShuffleLocationSelector, StandingLocationRow2, WorldAreaEnum)
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.area_objects import (NPC_4)
if TYPE_CHECKING:
    from randomizer.types.gameworld import (GameWorld)


class BanditsWayCoin2Location(StandingLocationRow2):
    _bias = True
    _originally_held = Coins1Prize
    _rooms = [R207_BANDITS_WAY_AREA_02]
    _npc_ids = [NPC_4]
    _id = ShuffleLocationSelector.BANDITS_WAY_COIN_2
    _world_area = WorldAreaEnum.BANDITS_WAY
    _hint = [
        # SetVarToConst(PRIMARY_TEMP_7000, 31),
        # RunDialog(
            # dialog_id=DI2010_DEBUG_7000,
            # above_object=BOWSER,
            # closable=True,
            # sync=False,
            # multiline=True,
            # use_background=True,
        # ),
        #    JmpIfObjectNotInSpecificLevel(NPC_4, R207_BANDITS_WAY_AREA_02, ["next"]),
        #    JmpIfBitClear(MAP_BANDITS_WAY, ["next"]),
        #    Jmp(["bandits_way_hint_text"])
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_bandits_way(world, inventory)


__all__ = ["BanditsWayCoin2Location"]
