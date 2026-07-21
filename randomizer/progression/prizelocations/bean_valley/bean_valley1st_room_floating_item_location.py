from __future__ import annotations
from smrpgpatchbuilder.datatypes.overworld_scripts.event_scripts.commands import *
from randomizer.data.variables.room_names import *
from randomizer.data.variables.event_script_names import *
from randomizer.data.variables.action_script_names import *
from randomizer.data.variables.pack_names import *
from randomizer.progression.prizes import *
from randomizer.types.flags import *
from randomizer.types.prizelocation import (ShuffleLocationSelector, StandingLocationRow1, WorldAreaEnum)
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.area_objects import (NPC_3)


class BeanValley1stRoomFloatingItemLocation(StandingLocationRow1):
    _originally_held = FrogCoin1Prize
    _rooms = [R378_BEAN_VALLEY_BEANSTALKS_AREA_01]
    _npc_ids = [NPC_3]
    _id = ShuffleLocationSelector.BEAN_VALLEY_FIRST_VINE_ROOM_FROG_COIN
    _world_area = WorldAreaEnum.BEAN_VALLEY
    _hint = [
        # SetVarToConst(PRIMARY_TEMP_7000, 317),
        # RunDialog(
            # dialog_id=DI2010_DEBUG_7000,
            # above_object=BOWSER,
            # closable=True,
            # sync=False,
            # multiline=True,
            # use_background=True,
        # ),
        JmpIfObjectNotInSpecificLevel(
            NPC_3, R378_BEAN_VALLEY_BEANSTALKS_AREA_01, ["next"]
        ),
        Jmp(["beanstalk_hint_text"]),
    ]


__all__ = ["BeanValley1stRoomFloatingItemLocation"]
