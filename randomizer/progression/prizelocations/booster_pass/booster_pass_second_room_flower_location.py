from __future__ import annotations
from smrpgpatchbuilder.datatypes.overworld_scripts.event_scripts.commands import *
from randomizer.data.variables.room_names import *
from randomizer.data.variables.event_script_names import *
from randomizer.data.variables.action_script_names import *
from randomizer.data.variables.pack_names import *
from randomizer.progression.prizes import *
from randomizer.types.flags import *
from randomizer.types.prize import (FPFlowerPrize)
from randomizer.types.prizelocation import (ShuffleLocationSelector, StandingLocationRow1, WorldAreaEnum)
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.area_objects import (NPC_6)


class BoosterPassSecondRoomFlowerLocation(StandingLocationRow1):
    _originally_held = FPFlowerPrize
    _rooms = [R101_BOOSTER_PASS_AREA_02]
    _npc_ids = [NPC_6]
    _id = ShuffleLocationSelector.BOOSTER_PASS_FLOWER
    _world_area = WorldAreaEnum.BOOSTER_PASS
    _hint = [
        # SetVarToConst(PRIMARY_TEMP_7000, 134),
        # RunDialog(
            # dialog_id=DI2010_DEBUG_7000,
            # above_object=BOWSER,
            # closable=True,
            # sync=False,
            # multiline=True,
            # use_background=True,
        # ),
        JmpIfObjectNotInSpecificLevel(NPC_6, R101_BOOSTER_PASS_AREA_02, ["next"]),
        Jmp(["booster_pass_hint_text"]),
    ]


__all__ = ["BoosterPassSecondRoomFlowerLocation"]
