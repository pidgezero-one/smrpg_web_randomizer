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
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.area_objects import (NPC_4, NPC_5)


class RoseTownShopRightChestLocation(TreasureChestLocationRow1):
    _originally_held = FPFlowerPrize
    _rooms = [R087_ROSE_TOWN_ITEM_SHOP]
    _npc_ids = [NPC_4]
    _id = ShuffleLocationSelector.ROSE_TOWN_STORE_1
    _world_area = WorldAreaEnum.ROSE_TOWN
    _blacklist = [EXPStarPrize, SecondMimicFightLauncher, ThirdMimicFightLauncher]
    _hint = [
        # SetVarToConst(PRIMARY_TEMP_7000, 70),
        # RunDialog(
            # dialog_id=DI2010_DEBUG_7000,
            # above_object=BOWSER,
            # closable=True,
            # sync=False,
            # multiline=True,
            # use_background=True,
        # ),
        JmpIfObjectTriggerDisabledInSpecificLevel(
            NPC_5, R087_ROSE_TOWN_ITEM_SHOP, ["next"]
        ),
        Jmp(["rose_town_hint_text"]),
    ]


__all__ = ["RoseTownShopRightChestLocation"]
