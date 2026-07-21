from __future__ import annotations
from smrpgpatchbuilder.datatypes.overworld_scripts.event_scripts.commands import *
from randomizer.data.variables.room_names import *
from randomizer.data.variables.event_script_names import *
from randomizer.data.variables.action_script_names import *
from randomizer.data.variables.pack_names import *
from randomizer.progression.prizes import *
from randomizer.types.flags import *
from randomizer.types.prizelocation import (NPCLocationRow1, ShuffleLocationSelector, WorldAreaEnum)


class RoseTownInnToadPrizeLocation(NPCLocationRow1):
    _originally_held = FlowerTabPrize
    _rooms = [
        R095_ROSE_TOWN_DURING_BOWYER_INN_2F,
        R096_ROSE_TOWN_INN_2F,
    ]
    _id = ShuffleLocationSelector.ROSE_TOWN_TOAD
    _world_area = WorldAreaEnum.ROSE_TOWN
    _blacklist = [RecoveryMushroomPrize]
    _hint = [
        # SetVarToConst(PRIMARY_TEMP_7000, 73),
        # RunDialog(
            # dialog_id=DI2010_DEBUG_7000,
            # above_object=BOWSER,
            # closable=True,
            # sync=False,
            # multiline=True,
            # use_background=True,
        # ),
        JmpIfBitSet(ROSE_TOWN_INN_TOAD_ITEM_RECEIVED, ["next"]),
        Jmp(["rose_town_hint_text"]),
    ]


__all__ = ["RoseTownInnToadPrizeLocation"]
