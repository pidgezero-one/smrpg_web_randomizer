from __future__ import annotations
from smrpgpatchbuilder.datatypes.overworld_scripts.event_scripts.commands import *
from randomizer.data.variables.room_names import *
from randomizer.data.variables.event_script_names import *
from randomizer.data.variables.action_script_names import *
from randomizer.data.variables.pack_names import *
from randomizer.logic.progression.prizes import *
from randomizer.types.flags import *
from randomizer.types.prize import (FPFlowerPrize)
from randomizer.types.prizelocation import (ShuffleLocationSelector, TreasureChestLocationRow1, WorldAreaEnum)
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.area_objects import (NPC_0)


class RoseTownTreasureHouseLeftChestLocation(TreasureChestLocationRow1):
    _originally_held = FPFlowerPrize
    _rooms = [
        R093_ROSE_TOWN_DURING_BOWYER_TREASURE_HOUSE_1F,
        R094_ROSE_TOWN_TREASURE_HOUSE_1F,
    ]
    _npc_ids = [NPC_0, NPC_0]
    _id = ShuffleLocationSelector.ROSE_TOWN_TREASURE_HOUSE_1
    _world_area = WorldAreaEnum.ROSE_TOWN
    _blacklist = [
        EXPStarPrize,
        SecondMimicFightLauncher,
        ThirdMimicFightLauncher,
    ]
    _hint = [
        # SetVarToConst(PRIMARY_TEMP_7000, 75),
        # RunDialog(
            # dialog_id=DI2010_DEBUG_7000,
            # above_object=BOWSER,
            # closable=True,
            # sync=False,
            # multiline=True,
            # use_background=True,
        # ),
        JmpIfObjectTriggerDisabledInSpecificLevel(
            NPC_0, R093_ROSE_TOWN_DURING_BOWYER_TREASURE_HOUSE_1F, ["next"]
        ),
        Jmp(["rose_town_hint_text"]),
    ]


__all__ = ["RoseTownTreasureHouseLeftChestLocation"]
