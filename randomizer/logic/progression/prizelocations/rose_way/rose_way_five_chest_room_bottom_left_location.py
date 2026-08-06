from __future__ import annotations
from smrpgpatchbuilder.datatypes.overworld_scripts.event_scripts.commands import *
from randomizer.data.variables.room_names import *
from randomizer.data.variables.event_script_names import *
from randomizer.data.variables.action_script_names import *
from randomizer.data.variables.pack_names import *
from randomizer.logic.progression.prizes import *
from randomizer.types.flags import *
from randomizer.types.prizelocation import (ShuffleLocationSelector, TreasureChestLocationRow2, WorldAreaEnum)
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.area_objects import (NPC_1)


class RoseWayFiveChestRoomBottomLeftLocation(TreasureChestLocationRow2):
    _originally_held = Coins5Prize
    _rooms = [R081_ROSE_WAY_TREASURE_CHESTS_WCOINS_AREA]
    _npc_ids = [NPC_1]
    _id = ShuffleLocationSelector.ROSE_WAY_FIVE_CHESTS_2
    _world_area = WorldAreaEnum.ROSE_WAY
    _blacklist = [SecondMimicFightLauncher, ThirdMimicFightLauncher]
    _hint = [
        # SetVarToConst(PRIMARY_TEMP_7000, 65),
        # RunDialog(
            # dialog_id=DI2010_DEBUG_7000,
            # above_object=BOWSER,
            # closable=True,
            # sync=False,
            # multiline=True,
            # use_background=True,
        # ),
        JmpIfObjectTriggerDisabledInSpecificLevel(
            NPC_1, R081_ROSE_WAY_TREASURE_CHESTS_WCOINS_AREA, ["next"]
        ),
        Jmp(["rose_way_hint_text"]),
    ]


__all__ = ["RoseWayFiveChestRoomBottomLeftLocation"]
