from __future__ import annotations
from smrpgpatchbuilder.datatypes.overworld_scripts.event_scripts.commands import *
from randomizer.data.variables.room_names import *
from randomizer.data.variables.event_script_names import *
from randomizer.data.variables.action_script_names import *
from randomizer.data.variables.pack_names import *
from randomizer.progression.prizes import *
from randomizer.types.flags import *
from randomizer.types.prizelocation import (ShuffleLocationSelector, StandingLocationRow6, WorldAreaEnum)
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.area_objects import (NPC_19)


class RoseWayCoin2Location(StandingLocationRow6):
    _originally_held = Coins10Prize
    _rooms = [R079_ROSE_WAY_MAIN_AREA]
    _npc_ids = [NPC_19]
    _id = ShuffleLocationSelector.ROSE_WAY_COIN_2
    _world_area = WorldAreaEnum.ROSE_WAY
    _hint = [
        # SetVarToConst(PRIMARY_TEMP_7000, 60),
        # RunDialog(
            # dialog_id=DI2010_DEBUG_7000,
            # above_object=BOWSER,
            # closable=True,
            # sync=False,
            # multiline=True,
            # use_background=True,
        # ),
        # JmpIfObjectNotInSpecificLevel(NPC_19, R079_ROSE_WAY_MAIN_AREA, ["next"]),
        # Jmp(["rose_way_hint_text"])
    ]


__all__ = ["RoseWayCoin2Location"]
