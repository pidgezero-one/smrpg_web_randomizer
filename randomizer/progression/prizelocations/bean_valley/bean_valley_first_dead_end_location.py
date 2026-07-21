from __future__ import annotations
from smrpgpatchbuilder.datatypes.overworld_scripts.event_scripts.commands import *
from randomizer.data.variables.room_names import *
from randomizer.data.variables.event_script_names import *
from randomizer.data.variables.action_script_names import *
from randomizer.data.variables.pack_names import *
from randomizer.progression.prizes import *
from randomizer.types.flags import *
from randomizer.types.prize import (FPFlowerPrize)
from randomizer.types.prizelocation import (ShuffleLocationSelector, TreasureChestLocationRow1, WorldAreaEnum)
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.area_objects import (NPC_3)


class BeanValleyFirstDeadEndLocation(TreasureChestLocationRow1):
    _originally_held = FPFlowerPrize
    _rooms = [R252_BEAN_VALLEY_MAIN_AREA]
    _npc_ids = [NPC_3]
    _id = ShuffleLocationSelector.BEAN_VALLEY_1
    _world_area = WorldAreaEnum.BEAN_VALLEY
    _blacklist = [EXPStarPrize]
    _hint = [
        # SetVarToConst(PRIMARY_TEMP_7000, 304),
        # RunDialog(
            # dialog_id=DI2010_DEBUG_7000,
            # above_object=BOWSER,
            # closable=True,
            # sync=False,
            # multiline=True,
            # use_background=True,
        # ),
        JmpIfObjectTriggerDisabledInSpecificLevel(
            NPC_3, R252_BEAN_VALLEY_MAIN_AREA, ["next"]
        ),
        Jmp(["bean_valley_hint_text"]),
    ]


__all__ = ["BeanValleyFirstDeadEndLocation"]
