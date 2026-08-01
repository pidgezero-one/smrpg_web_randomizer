from __future__ import annotations
from smrpgpatchbuilder.datatypes.overworld_scripts.event_scripts.commands import *
from randomizer.data.variables.room_names import *
from randomizer.data.variables.event_script_names import *
from randomizer.data.variables.action_script_names import *
from randomizer.data.variables.pack_names import *
from randomizer.logic.progression.prizes import *
from randomizer.types.flags import *
from randomizer.types.prizelocation import (KeyItemLocation, NPCLocationRow1, ShuffleLocationSelector, WorldAreaEnum)


class MelodyBayFirstRewardLocation(NPCLocationRow1, KeyItemLocation):
    _originally_held = ProgressiveCardPrize
    _rooms = [R074_TADPOLE_POND_AREA_02]
    _id = ShuffleLocationSelector.MELODY_BAY_1
    _world_area = WorldAreaEnum.TADPOLE_POND
    _hint = [
        # SetVarToConst(PRIMARY_TEMP_7000, 53),
        # RunDialog(
            # dialog_id=DI2010_DEBUG_7000,
            # above_object=BOWSER,
            # closable=True,
            # sync=False,
            # multiline=True,
            # use_background=True,
        # ),
        JmpIfBitSet(MELODY_BAY_ITEM_1_GRANTED, ["next"]),
        Jmp(["tadpole_pond_hint_text"]),
    ]


__all__ = ["MelodyBayFirstRewardLocation"]
