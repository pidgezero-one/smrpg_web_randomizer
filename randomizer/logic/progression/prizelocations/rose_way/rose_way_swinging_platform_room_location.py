from __future__ import annotations
from smrpgpatchbuilder.datatypes.overworld_scripts.event_scripts.commands import *
from randomizer.data.variables.room_names import *
from randomizer.data.variables.event_script_names import *
from randomizer.data.variables.action_script_names import *
from randomizer.data.variables.pack_names import *
from randomizer.logic.progression.prizes import *
from randomizer.types.flags import *
from randomizer.types.prize import (SlotsPrize)
from randomizer.types.prizelocation import (ShuffleLocationSelector, TreasureChestLocationRow1, WorldAreaEnum)
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.area_objects import (NPC_0)


class RoseWaySwingingPlatformRoomLocation(TreasureChestLocationRow1):
    _originally_held = FrogCoin1Prize
    _rooms = [R080_ROSE_WAY_TWO_FASTFLOATING_PLATFORMS]
    _npc_ids = [NPC_0]
    _id = ShuffleLocationSelector.ROSE_WAY_PLATFORM
    _world_area = WorldAreaEnum.ROSE_WAY
    _blacklist = [
        EXPStarPrize,
        SecondMimicFightLauncher,
        ThirdMimicFightLauncher,
        SlotsPrize,
    ]  # SlotsPrize can go here graphically, it's just too annoying to hit 4 times
    _hint = [
        # SetVarToConst(PRIMARY_TEMP_7000, 56),
        # RunDialog(
            # dialog_id=DI2010_DEBUG_7000,
            # above_object=BOWSER,
            # closable=True,
            # sync=False,
            # multiline=True,
            # use_background=True,
        # ),
        JmpIfObjectTriggerDisabledInSpecificLevel(
            NPC_0, R080_ROSE_WAY_TWO_FASTFLOATING_PLATFORMS, ["next"]
        ),
        Jmp(["rose_way_hint_text"]),
    ]


__all__ = ["RoseWaySwingingPlatformRoomLocation"]
