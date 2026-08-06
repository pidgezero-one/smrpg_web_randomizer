from __future__ import annotations
from smrpgpatchbuilder.datatypes.overworld_scripts.event_scripts.commands import *
from randomizer.data.variables.room_names import *
from randomizer.data.variables.event_script_names import *
from randomizer.data.variables.action_script_names import *
from randomizer.data.variables.pack_names import *
from randomizer.logic.progression.prizes import *
from randomizer.types.flags import *
from randomizer.types.prize import (FrogCoinPrize, SlotsPrize)
from randomizer.types.prizelocation import (ShuffleLocationSelector, TreasureChestLocationRow2, WorldAreaEnum)
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.area_objects import (NPC_1)


class MushroomWayRightGoomba(TreasureChestLocationRow2):
    _originally_held = RecoveryMushroomPrize
    _rooms = [R204_MUSHROOM_WAY_AREA_02]
    _npc_ids = [NPC_1]
    _id = ShuffleLocationSelector.MUSHROOM_WAY_4
    _world_area = WorldAreaEnum.MUSHROOM_WAY
    _blacklist = [
        EXPStarPrize,
        SecondMimicFightLauncher,
        ThirdMimicFightLauncher,
        FrogCoinPrize,
        SlotsPrize
    ]
    _hint = [
        # SetVarToConst(PRIMARY_TEMP_7000, 6),
        # RunDialog(
            # dialog_id=DI2010_DEBUG_7000,
            # above_object=BOWSER,
            # closable=True,
            # sync=False,
            # multiline=True,
            # use_background=True,
        # ),
        JmpIfObjectTriggerDisabledInSpecificLevel(
            NPC_1, R204_MUSHROOM_WAY_AREA_02, ["next"]
        ),
        Jmp(["mushroom_way_hint_text"]),
    ]


__all__ = ["MushroomWayRightGoomba"]
