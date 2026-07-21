from __future__ import annotations
from smrpgpatchbuilder.datatypes.overworld_scripts.event_scripts.commands import *
from randomizer.data.variables.room_names import *
from randomizer.data.variables.event_script_names import *
from randomizer.data.variables.action_script_names import *
from randomizer.data.variables.pack_names import *
from randomizer.progression.prizes import *
from randomizer.types.flags import *
from randomizer.types.prizelocation import (ShuffleLocationSelector, TreasureChestLocationRow1, WorldAreaEnum)
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.area_objects import (NPC_0)


class MushroomWay1LowerChest(TreasureChestLocationRow1):
    _originally_held = Coins5Prize
    _rooms = [R203_MUSHROOM_WAY_AREA_01]
    _npc_ids = [NPC_0]
    _id = ShuffleLocationSelector.MUSHROOM_WAY_1
    _world_area = WorldAreaEnum.MUSHROOM_WAY
    _blacklist = [
        EXPStarPrize,
        SecondMimicFightLauncher,
        ThirdMimicFightLauncher,
    ]
    _hint = [
        # SetVarToConst(PRIMARY_TEMP_7000, 1),
        # RunDialog(
            # dialog_id=DI2010_DEBUG_7000,
            # above_object=BOWSER,
            # closable=True,
            # sync=False,
            # multiline=True,
            # use_background=True,
        # ),
        JmpIfObjectTriggerDisabledInSpecificLevel(
            NPC_0, R203_MUSHROOM_WAY_AREA_01, ["next"]
        ),
        Jmp(["mushroom_way_hint_text"]),
    ]


__all__ = ["MushroomWay1LowerChest"]
