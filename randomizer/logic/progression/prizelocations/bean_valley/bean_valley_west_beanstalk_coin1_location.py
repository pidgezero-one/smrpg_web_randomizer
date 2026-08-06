from __future__ import annotations
from smrpgpatchbuilder.datatypes.overworld_scripts.event_scripts.commands import *
from randomizer.data.variables.room_names import *
from randomizer.data.variables.event_script_names import *
from randomizer.data.variables.action_script_names import *
from randomizer.data.variables.pack_names import *
from randomizer.logic.progression.prizes import *
from randomizer.types.flags import *
from randomizer.types.prizelocation import (ShuffleLocationSelector, StandingLocationRow1, WorldAreaEnum)
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.area_objects import (NPC_4)


class BeanValleyWestBeanstalkCoin1Location(StandingLocationRow1):
    _originally_held = Coins10Prize
    _rooms = [R381_BEAN_VALLEY_BEANSTALKS_AREA_04_FROM_LEFT_BEANSTALK_OF_AREA_02]
    _npc_ids = [NPC_4]
    _id = ShuffleLocationSelector.BEAN_VALLEY_WEST_BEANSTALK_COIN_1
    _world_area = WorldAreaEnum.BEAN_VALLEY
    _hint = [
        # SetVarToConst(PRIMARY_TEMP_7000, 330),
        # RunDialog(
            # dialog_id=DI2010_DEBUG_7000,
            # above_object=BOWSER,
            # closable=True,
            # sync=False,
            # multiline=True,
            # use_background=True,
        # ),
        # JmpIfObjectTriggerDisabledInSpecificLevel(NPC_4, R381_BEAN_VALLEY_BEANSTALKS_AREA_04_FROM_LEFT_BEANSTALK_OF_AREA_02, ["next"]),
        # Jmp(["beanstalk_hint_text"])
    ]


__all__ = ["BeanValleyWestBeanstalkCoin1Location"]
