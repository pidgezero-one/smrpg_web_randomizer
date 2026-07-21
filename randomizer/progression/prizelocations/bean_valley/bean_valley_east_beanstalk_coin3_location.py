from __future__ import annotations
from smrpgpatchbuilder.datatypes.overworld_scripts.event_scripts.commands import *
from randomizer.data.variables.room_names import *
from randomizer.data.variables.event_script_names import *
from randomizer.data.variables.action_script_names import *
from randomizer.data.variables.pack_names import *
from randomizer.progression.prizes import *
from randomizer.types.flags import *
from randomizer.types.prizelocation import (ShuffleLocationSelector, StandingLocationRow3, WorldAreaEnum)
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.area_objects import (NPC_5)


class BeanValleyEastBeanstalkCoin3Location(StandingLocationRow3):
    _originally_held = Coins10Prize
    _rooms = [R380_BEAN_VALLEY_BEANSTALKS_AREA_03_FROM_RIGHT_BEANSTALK_OF_AREA_02]
    _npc_ids = [NPC_5]
    _id = ShuffleLocationSelector.BEAN_VALLEY_EAST_BEANSTALK_COIN_3
    _world_area = WorldAreaEnum.BEAN_VALLEY
    _hint = [
        # SetVarToConst(PRIMARY_TEMP_7000, 327),
        # RunDialog(
            # dialog_id=DI2010_DEBUG_7000,
            # above_object=BOWSER,
            # closable=True,
            # sync=False,
            # multiline=True,
            # use_background=True,
        # ),
        # JmpIfObjectTriggerDisabledInSpecificLevel(NPC_5, R380_BEAN_VALLEY_BEANSTALKS_AREA_03_FROM_RIGHT_BEANSTALK_OF_AREA_02, ["next"]),
        # Jmp(["beanstalk_hint_text"])
    ]


__all__ = ["BeanValleyEastBeanstalkCoin3Location"]
