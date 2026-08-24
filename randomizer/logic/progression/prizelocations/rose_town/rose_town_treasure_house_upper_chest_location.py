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
from randomizer.types.prizelocation import (ShuffleLocationSelector, TreasureChestLocationRow1, WorldAreaEnum)
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.area_objects import (NPC_1)


class RoseTownTreasureHouseUpperChestLocation(TreasureChestLocationRow1):
    _originally_held = FrogCoin1Prize
    _rooms = [
        R097_ROSE_TOWN_DURING_BOWYER_TREASURE_HOUSE_2F,
        R098_ROSE_TOWN_TREASURE_HOUSE_2F,
    ]
    _npc_ids = [NPC_1, NPC_1]
    _id = ShuffleLocationSelector.ROSE_TOWN_TREASURE_HOUSE_3
    _world_area = WorldAreaEnum.ROSE_TOWN
    _blacklist = [EXPStarPrize, SecondMimicFightLauncher, ThirdMimicFightLauncher]
    _hint = [
        # SetVarToConst(PRIMARY_TEMP_7000, 78),
        # RunDialog(
            # dialog_id=DI2010_DEBUG_7000,
            # above_object=BOWSER,
            # closable=True,
            # sync=False,
            # multiline=True,
            # use_background=True,
        # ),
        JmpIfBitClear(MAP_FOREST_MAZE, ["next"]),
        JmpIfObjectTriggerDisabledInSpecificLevel(
            NPC_1, R097_ROSE_TOWN_DURING_BOWYER_TREASURE_HOUSE_2F, ["next"]
        ),
        Jmp(["rose_town_hint_text"]),
    ]


__all__ = ["RoseTownTreasureHouseUpperChestLocation"]
