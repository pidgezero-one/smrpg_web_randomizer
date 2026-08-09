from __future__ import annotations
from smrpgpatchbuilder.datatypes.overworld_scripts.event_scripts.commands import *
from randomizer.data.variables.room_names import *
from randomizer.data.variables.event_script_names import *
from randomizer.data.variables.action_script_names import *
from randomizer.data.variables.pack_names import *
from randomizer.logic.progression.prizes import *
from randomizer.types.flags import *
from randomizer.types.prizelocation import (NPCLocationRow3, ShuffleLocationSelector, WorldAreaEnum)


class MushroomWay2ToadRescue(NPCLocationRow3):
    _originally_held = FlowerTabPrize
    _rooms = [R204_MUSHROOM_WAY_AREA_02, R205_MUSHROOM_WAY_AREA_03]
    _id = ShuffleLocationSelector.TOAD_RESCUE_2
    _world_area = WorldAreaEnum.MUSHROOM_WAY
    _hint = [
        # SetVarToConst(PRIMARY_TEMP_7000, 5),
        # RunDialog(
            # dialog_id=DI2010_DEBUG_7000,
            # above_object=BOWSER,
            # closable=True,
            # sync=False,
            # multiline=True,
            # use_background=True,
        # ),
        JmpIfBitSet(TOAD_IN_MUSHROOM_WAY_2, ["next"]),
        Jmp(["mushroom_way_hint_text"]),
    ]
    _access_conditions = "Will be given to you automatically if you defeat the area boss without fighting the sky troopa"


__all__ = ["MushroomWay2ToadRescue"]
