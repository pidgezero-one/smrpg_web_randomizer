from __future__ import annotations
from smrpgpatchbuilder.datatypes.overworld_scripts.event_scripts.commands import *
from randomizer.data.variables.room_names import *
from randomizer.data.variables.event_script_names import *
from randomizer.data.variables.action_script_names import *
from randomizer.data.variables.pack_names import *
from randomizer.logic.progression.prizes import *
from randomizer.types.flags import *
from randomizer.types.prizelocation import (NPCLocationRow3, ShuffleLocationSelector, WorldAreaEnum)


class MarrymoreThirdSuitePrizeLocation(NPCLocationRow3):
    _originally_held = FrogCoin1Prize
    _rooms = [R007_MARRYMORE_INN_1F]
    _id = ShuffleLocationSelector.MARRYMORE_PRIZE_3
    _world_area = WorldAreaEnum.MARRYMORE
    _blacklist = [RecoveryMushroomPrize]
    _hint = [
        # SetVarToConst(PRIMARY_TEMP_7000, 190),
        # RunDialog(
            # dialog_id=DI2010_DEBUG_7000,
            # above_object=BOWSER,
            # closable=True,
            # sync=False,
            # multiline=True,
            # use_background=True,
        # ),
        RunEventAsSubroutine(E0711_SUITE_3_HINT_SUBR),
    ]


__all__ = ["MarrymoreThirdSuitePrizeLocation"]
