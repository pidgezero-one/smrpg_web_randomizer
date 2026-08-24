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
from randomizer.types.prizelocation import (FrogDiscipleLocation, ShuffleLocationSelector, WorldAreaEnum)


class FrogDiscipleLocation1(FrogDiscipleLocation):
    _originally_held = SeeYaPrize
    _id = ShuffleLocationSelector.FROG_DISCIPLE_1
    _world_area = WorldAreaEnum.SEASIDE_TOWN
    _hint = [
        # SetVarToConst(PRIMARY_TEMP_7000, 205),
        # RunDialog(
            # dialog_id=DI2010_DEBUG_7000,
            # above_object=BOWSER,
            # closable=True,
            # sync=False,
            # multiline=True,
            # use_background=True,
        # ),
        JmpIfBitSet(FROG_DISCIPLE_ITEM_1_PURCHASED, ["next"]),
        Jmp(["frog_disciple_hint_text"]),
    ]


__all__ = ["FrogDiscipleLocation1"]
