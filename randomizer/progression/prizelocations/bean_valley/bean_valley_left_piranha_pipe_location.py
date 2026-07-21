from __future__ import annotations
from smrpgpatchbuilder.datatypes.overworld_scripts.event_scripts.commands import *
from randomizer.data.variables.room_names import *
from randomizer.data.variables.event_script_names import *
from randomizer.data.variables.action_script_names import *
from randomizer.data.variables.pack_names import *
from randomizer.progression.prizes import *
from randomizer.types.flags import *
from randomizer.types.prizelocation import (ShuffleLocationSelector, TreasureChestLocationRow1, WorldAreaEnum)
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.area_objects import (NPC_0)


class BeanValleyLeftPiranhaPipeLocation(TreasureChestLocationRow1):
    _originally_held = SlotsPrize1
    _rooms = [R334_BEAN_VALLEY_PIPE_ROOM_LEFTMOST_PIPE]
    _npc_ids = [NPC_0]
    _id = ShuffleLocationSelector.BEAN_VALLEY_LEFT_PIRANHA_PIPE
    _world_area = WorldAreaEnum.BEAN_VALLEY
    _blacklist = [EXPStarPrize]
    _hint = [
        # SetVarToConst(PRIMARY_TEMP_7000, 306),
        # RunDialog(
            # dialog_id=DI2010_DEBUG_7000,
            # above_object=BOWSER,
            # closable=True,
            # sync=False,
            # multiline=True,
            # use_background=True,
        # ),
        JmpIfObjectTriggerDisabledInSpecificLevel(
            NPC_0, R334_BEAN_VALLEY_PIPE_ROOM_LEFTMOST_PIPE, ["next"]
        ),
        Jmp(["bean_valley_hint_text"]),
    ]


__all__ = ["BeanValleyLeftPiranhaPipeLocation"]
