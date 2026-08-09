from __future__ import annotations
from smrpgpatchbuilder.datatypes.overworld_scripts.event_scripts.commands import *
from randomizer.data.variables.room_names import *
from randomizer.data.variables.event_script_names import *
from randomizer.data.variables.action_script_names import *
from randomizer.data.variables.pack_names import *
from randomizer.logic.progression.prizes import *
from randomizer.types.flags import *
from randomizer.types.prizelocation import (ShuffleLocationSelector, StandingLocationRow2, WorldAreaEnum)
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.area_objects import (NPC_11)


class MushroomWayRightItemRemake(StandingLocationRow2):
    _bias = True
    _originally_held = PickMeUpPrize
    _rooms = [R204_MUSHROOM_WAY_AREA_02]
    _npc_ids = [NPC_11]
    _id = ShuffleLocationSelector.REMAKE_2
    _world_area = WorldAreaEnum.MUSHROOM_WAY
    _remake_only = True
    _hint = [
        # SetVarToConst(PRIMARY_TEMP_7000, 8),
        # RunDialog(
            # dialog_id=DI2010_DEBUG_7000,
            # above_object=BOWSER,
            # closable=True,
            # sync=False,
            # multiline=True,
            # use_background=True,
        # ),
        JmpIfObjectNotInSpecificLevel(NPC_11, R204_MUSHROOM_WAY_AREA_02, ["next"]),
        Jmp(["mushroom_way_hint_text"]),
    ]
    _access_conditions = "Not a check if \"Enable Remake content\" is turned off."



__all__ = ["MushroomWayRightItemRemake"]
