from __future__ import annotations
from smrpgpatchbuilder.datatypes.overworld_scripts.event_scripts.commands import *
from randomizer.data.variables.room_names import *
from randomizer.data.variables.event_script_names import *
from randomizer.data.variables.action_script_names import *
from randomizer.data.variables.pack_names import *
from randomizer.logic.progression.prizes import *
from randomizer.types.flags import *
from randomizer.types.prize import (FPFlowerPrize)
from randomizer.types.prizelocation import (ShuffleLocationSelector, TreasureChestLocationRow1, WorldAreaEnum)
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.area_objects import (NPC_1)


class BeanstalkUpperCloudLeftChestLocation(TreasureChestLocationRow1):
    _originally_held = FPFlowerPrize
    _rooms = [R372_NIMBUS_LAND_FALL_FROM_PLATFORM_2ND]
    _npc_ids = [NPC_1]
    _id = ShuffleLocationSelector.BEAN_VALLEY_CLOUD_1
    _world_area = WorldAreaEnum.BEAN_VALLEY
    _blacklist = [EXPStarPrize]
    _hint = [
        # SetVarToConst(PRIMARY_TEMP_7000, 334),
        # RunDialog(
            # dialog_id=DI2010_DEBUG_7000,
            # above_object=BOWSER,
            # closable=True,
            # sync=False,
            # multiline=True,
            # use_background=True,
        # ),
        JmpIfObjectTriggerDisabledInSpecificLevel(
            NPC_1, R372_NIMBUS_LAND_FALL_FROM_PLATFORM_2ND, ["next"]
        ),
        Jmp(["beanstalk_hint_text"]),
    ]


__all__ = ["BeanstalkUpperCloudLeftChestLocation"]
