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
from randomizer.types.prizelocation import (ShuffleLocationSelector, StandingLocationRow2, WorldAreaEnum)
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.area_objects import (NPC_8)


class RoseWayMiddleIslandLocation(StandingLocationRow2):
    _originally_held = RecoveryMushroomPrize
    _rooms = [R079_ROSE_WAY_MAIN_AREA]
    _npc_ids = [NPC_8]
    _id = ShuffleLocationSelector.ROSE_WAY_MUSHROOM
    _world_area = WorldAreaEnum.ROSE_WAY
    _hint = [
        # SetVarToConst(PRIMARY_TEMP_7000, 58),
        # RunDialog(
            # dialog_id=DI2010_DEBUG_7000,
            # above_object=BOWSER,
            # closable=True,
            # sync=False,
            # multiline=True,
            # use_background=True,
        # ),
        JmpIfObjectNotInSpecificLevel(NPC_8, R079_ROSE_WAY_MAIN_AREA, ["next"]),
        Jmp(["rose_way_hint_text"]),
    ]


__all__ = ["RoseWayMiddleIslandLocation"]
