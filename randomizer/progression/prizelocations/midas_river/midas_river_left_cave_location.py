from __future__ import annotations
from smrpgpatchbuilder.datatypes.overworld_scripts.event_scripts.commands import *
from randomizer.data.variables.room_names import *
from randomizer.data.variables.event_script_names import *
from randomizer.data.variables.action_script_names import *
from randomizer.data.variables.pack_names import *
from randomizer.progression.prizes import *
from randomizer.types.flags import *
from randomizer.types.prize import (FPFlowerPrize)
from randomizer.types.prizelocation import (RiverLocationRow2, ShuffleLocationSelector, WorldAreaEnum)
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.area_objects import (NPC_5)


class MidasRiverLeftCaveLocation(RiverLocationRow2):
    _originally_held = FPFlowerPrize
    _rooms = [R071_MIDAS_RIVER_2ND_TUNNEL_BOTH_LEFT_AND_RIGHT]
    _npc_ids = [NPC_5]
    _id = ShuffleLocationSelector.MIDAS_RIVER_LEFT_CAVE
    _world_area = WorldAreaEnum.MIDAS_RIVER
    _hint = [
        # SetVarToConst(PRIMARY_TEMP_7000, 48),
        # RunDialog(
            # dialog_id=DI2010_DEBUG_7000,
            # above_object=BOWSER,
            # closable=True,
            # sync=False,
            # multiline=True,
            # use_background=True,
        # ),
        JmpIfBitSet(MIDAS_RIVER_TUNNEL_2_BIT_1, ["next"]),
        Jmp(["midas_river_hint_text"]),
    ]


__all__ = ["MidasRiverLeftCaveLocation"]
