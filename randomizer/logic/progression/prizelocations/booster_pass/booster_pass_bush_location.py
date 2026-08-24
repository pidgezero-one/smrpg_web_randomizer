from __future__ import annotations
from smrpgpatchbuilder.datatypes.overworld_scripts.event_scripts.commands import *
from randomizer.data.variables.room_names import *
from randomizer.data.variables.event_script_names import *
from randomizer.data.variables.action_script_names import *
from randomizer.data.variables.pack_names import *
from randomizer.logic.progression.prizes import *
from randomizer.types.flags import *
from randomizer.logic.progression.prizelocations.access import (expect_good_movement, not_earlygame, expect_halfway_decent_movement, almost_earlygame, is_midgame, expect_ok_movement, lategame)
from randomizer.types.logic import (Inventory)
from randomizer.types.prizelocation import (NPCLocationRow1, ShuffleLocationSelector, WorldAreaEnum)


class BoosterPassBushLocation(NPCLocationRow1):
    _originally_held = FrogCoin1Prize
    _rooms = [R100_BOOSTER_PASS_AREA_01]
    _id = ShuffleLocationSelector.BOOSTER_PASS_BUSH
    _world_area = WorldAreaEnum.BOOSTER_PASS
    _hint = [
        # SetVarToConst(PRIMARY_TEMP_7000, 131),
        # RunDialog(
            # dialog_id=DI2010_DEBUG_7000,
            # above_object=BOWSER,
            # closable=True,
            # sync=False,
            # multiline=True,
            # use_background=True,
        # ),
        JmpIfBitSet(BOOSTER_PASS_BUSH_ITEM_FOUND, ["next"]),
        Jmp(["booster_pass_hint_text"]),
    ]


__all__ = ["BoosterPassBushLocation"]
