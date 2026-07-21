from __future__ import annotations
from smrpgpatchbuilder.datatypes.overworld_scripts.event_scripts.commands import *
from randomizer.data.variables.room_names import *
from randomizer.data.variables.event_script_names import *
from randomizer.data.variables.action_script_names import *
from randomizer.data.variables.pack_names import *
from randomizer.progression.prizes import *
from randomizer.types.flags import *
from randomizer.types.prizelocation import (NPCLocationRow1, ShuffleLocationSelector, WorldAreaEnum)


class MushroomWayBossFightRewardItem(NPCLocationRow1):
    _bias = True
    _originally_held = HammerPrize
    _rooms = [R205_MUSHROOM_WAY_AREA_03]
    _id = ShuffleLocationSelector.HAMMER_BROS_REWARD
    _world_area = WorldAreaEnum.MUSHROOM_WAY
    _blacklist = [RecoveryMushroomPrize]
    _hint = [
        # SetVarToConst(PRIMARY_TEMP_7000, 10),
        # RunDialog(
            # dialog_id=DI2010_DEBUG_7000,
            # above_object=BOWSER,
            # closable=True,
            # sync=False,
            # multiline=True,
            # use_background=True,
        # ),
        JmpIfBitSet(TOAD_IN_MUSHROOM_WAY_3, ["next"]),
        Jmp(["mushroom_way_hint_text"]),
    ]


__all__ = ["MushroomWayBossFightRewardItem"]
