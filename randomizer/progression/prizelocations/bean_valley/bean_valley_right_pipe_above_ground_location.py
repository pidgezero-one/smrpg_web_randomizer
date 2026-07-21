from __future__ import annotations
from smrpgpatchbuilder.datatypes.overworld_scripts.event_scripts.commands import *
from randomizer.data.variables.room_names import *
from randomizer.data.variables.event_script_names import *
from randomizer.data.variables.action_script_names import *
from randomizer.data.variables.pack_names import *
from randomizer.progression.prizes import *
from randomizer.types.flags import *
from randomizer.types.prize import (SlotsPrize)
from randomizer.types.prizelocation import (ShuffleLocationSelector, TreasureChestLocationRow1, WorldAreaEnum)
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.area_objects import (NPC_14)


class BeanValleyRightPipeAboveGroundLocation(TreasureChestLocationRow1):
    _originally_held = FrogCoin1Prize
    _rooms = [R251_BEAN_VALLEY_PIRANHA_PIPE_AREA]
    _npc_ids = [NPC_14]
    _id = ShuffleLocationSelector.BEAN_VALLEY_PIRANHA_PLANTS
    _world_area = WorldAreaEnum.BEAN_VALLEY
    _blacklist = [EXPStarPrize, SlotsPrize]
    _hint = [
        # SetVarToConst(PRIMARY_TEMP_7000, 313),
        # RunDialog(
            # dialog_id=DI2010_DEBUG_7000,
            # above_object=BOWSER,
            # closable=True,
            # sync=False,
            # multiline=True,
            # use_background=True,
        # ),
        JmpIfObjectTriggerDisabledInSpecificLevel(
            NPC_14, R251_BEAN_VALLEY_PIRANHA_PIPE_AREA, ["next"]
        ),
        Jmp(["bean_valley_hint_text"]),
    ]


__all__ = ["BeanValleyRightPipeAboveGroundLocation"]
