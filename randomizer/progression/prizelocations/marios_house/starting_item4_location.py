from __future__ import annotations
from smrpgpatchbuilder.datatypes.overworld_scripts.event_scripts.commands import *
from randomizer.data.variables.room_names import *
from randomizer.data.variables.event_script_names import *
from randomizer.data.variables.action_script_names import *
from randomizer.data.variables.pack_names import *
from randomizer.progression.prizes import *
from randomizer.types.flags import *
from randomizer.types.prizelocation import (NPCLocationRow5, ShuffleLocationSelector, WorldAreaEnum)


class StartingItem4Location(NPCLocationRow5):
    _originally_held = MushroomPrize
    _rooms = [R189_MARIOS_PIPEHOUSE]
    _id = ShuffleLocationSelector = ShuffleLocationSelector.MARIOS_PAD_STARTER_4
    _world_area = WorldAreaEnum.MARIOS_PAD
    _blacklist = [StarPiecePrize, RecoveryMushroomPrize]


__all__ = ["StartingItem4Location"]
