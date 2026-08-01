from __future__ import annotations
from smrpgpatchbuilder.datatypes.overworld_scripts.event_scripts.commands import *
from randomizer.data.variables.room_names import *
from randomizer.data.variables.event_script_names import *
from randomizer.data.variables.action_script_names import *
from randomizer.data.variables.pack_names import *
from randomizer.logic.progression.prizes import *
from randomizer.types.flags import *
from randomizer.types.prizelocation import (ShuffleLocationSelector, StandingLocationRow1, WorldAreaEnum)
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.area_objects import (NPC_10)


class MushroomWayLeftItemRemake(StandingLocationRow1):
    _bias = True
    _originally_held = FlowerTabPrize
    _rooms = [R204_MUSHROOM_WAY_AREA_02]
    _npc_ids = [NPC_10]
    _id = ShuffleLocationSelector.REMAKE_1
    _world_area = WorldAreaEnum.MUSHROOM_WAY
    _remake_only = True
    _hint = [
        # SetVarToConst(PRIMARY_TEMP_7000, 7),
        # RunDialog(
            # dialog_id=DI2010_DEBUG_7000,
            # above_object=BOWSER,
            # closable=True,
            # sync=False,
            # multiline=True,
            # use_background=True,
        # ),
        JmpIfObjectNotInSpecificLevel(NPC_10, R204_MUSHROOM_WAY_AREA_02, ["next"]),
        Jmp(["mushroom_way_hint_text"]),
    ]


__all__ = ["MushroomWayLeftItemRemake"]
