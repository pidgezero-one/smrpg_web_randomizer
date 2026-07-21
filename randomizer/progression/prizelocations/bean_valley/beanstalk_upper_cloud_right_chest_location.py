from __future__ import annotations
from smrpgpatchbuilder.datatypes.overworld_scripts.event_scripts.commands import *
from randomizer.data.variables.room_names import *
from randomizer.data.variables.event_script_names import *
from randomizer.data.variables.action_script_names import *
from randomizer.data.variables.pack_names import *
from randomizer.progression.prizes import *
from randomizer.types.flags import *
from randomizer.types.prizelocation import (ShuffleLocationSelector, TreasureChestLocationRow2, WorldAreaEnum)
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.area_objects import (NPC_2)


class BeanstalkUpperCloudRightChestLocation(TreasureChestLocationRow2):
    _originally_held = RareScarfPrize
    _rooms = [R372_NIMBUS_LAND_FALL_FROM_PLATFORM_2ND]
    _npc_ids = [NPC_2]
    _id = ShuffleLocationSelector.BEAN_VALLEY_CLOUD_2
    _world_area = WorldAreaEnum.BEAN_VALLEY
    _blacklist = [EXPStarPrize]
    _hint = [
        # SetVarToConst(PRIMARY_TEMP_7000, 335),
        # RunDialog(
            # dialog_id=DI2010_DEBUG_7000,
            # above_object=BOWSER,
            # closable=True,
            # sync=False,
            # multiline=True,
            # use_background=True,
        # ),
        JmpIfObjectTriggerDisabledInSpecificLevel(
            NPC_2, R372_NIMBUS_LAND_FALL_FROM_PLATFORM_2ND, ["next"]
        ),
        Jmp(["beanstalk_hint_text"]),
    ]


__all__ = ["BeanstalkUpperCloudRightChestLocation"]
