from __future__ import annotations
from smrpgpatchbuilder.datatypes.overworld_scripts.event_scripts.commands import *
from randomizer.data.variables.room_names import *
from randomizer.data.variables.event_script_names import *
from randomizer.data.variables.action_script_names import *
from randomizer.data.variables.pack_names import *
from randomizer.logic.progression.prizes import *
from randomizer.types.flags import *
from randomizer.types.prizelocation import (ShuffleLocationSelector, TreasureChestLocationRow2, WorldAreaEnum)
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.area_objects import (NPC_2)


class BeanValleyBottomRightPiranhaPipeLowerLocation(TreasureChestLocationRow2):
    _originally_held = KerokeroColaPrize
    _rooms = [R349_BEAN_VALLEY_PIPE_ROOM_BOTTOM_RIGHT]
    _npc_ids = [NPC_2]
    _id = ShuffleLocationSelector.BEAN_VALLEY_BOTTOM_RIGHT_PIRANHA_PIPE_LOWER
    _world_area = WorldAreaEnum.BEAN_VALLEY
    _blacklist = [EXPStarPrize]
    _hint = [
        # SetVarToConst(PRIMARY_TEMP_7000, 309),
        # RunDialog(
            # dialog_id=DI2010_DEBUG_7000,
            # above_object=BOWSER,
            # closable=True,
            # sync=False,
            # multiline=True,
            # use_background=True,
        # ),
        JmpIfObjectTriggerDisabledInSpecificLevel(
            NPC_2, R349_BEAN_VALLEY_PIPE_ROOM_BOTTOM_RIGHT, ["next"]
        ),
        Jmp(["bean_valley_hint_text"]),
    ]


__all__ = ["BeanValleyBottomRightPiranhaPipeLowerLocation"]
