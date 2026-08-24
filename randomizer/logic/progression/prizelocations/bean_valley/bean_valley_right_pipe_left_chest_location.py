from __future__ import annotations
from typing import TYPE_CHECKING
from smrpgpatchbuilder.datatypes.overworld_scripts.event_scripts.commands import *
from randomizer.data.variables.room_names import *
from randomizer.data.variables.event_script_names import *
from randomizer.data.variables.action_script_names import *
from randomizer.data.variables.pack_names import *
from randomizer.logic.progression.prizes import *
from randomizer.types.flags import *
from randomizer.logic.progression.prizelocations.access import (can_access_valley, can_do_valley_pipes, not_earlygame, is_early_midgame, is_late_midgame, is_lategame, expect_good_movement, expect_halfway_decent_movement, almost_earlygame, is_midgame, expect_ok_movement, lategame)
from randomizer.types.logic import (Inventory)
from randomizer.types.prize import (SlotsPrize)
from randomizer.types.prizelocation import (ShuffleLocationSelector, TreasureChestLocationRow1, WorldAreaEnum)
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.area_objects import (NPC_5)
if TYPE_CHECKING:
    from randomizer.types.gameworld import (GameWorld)


class BeanValleyRightPipeLeftChestLocation(TreasureChestLocationRow1):
    _originally_held = ThirdMimicFightLauncher
    _rooms = [R335_BEAN_VALLEY_PIPE_ROOM_RIGHTMOST_PIPE_LARGE_ROOM]
    _npc_ids = [NPC_5]
    _id = ShuffleLocationSelector.BEAN_VALLEY_BOX_BOY_ROOM_1
    _world_area = WorldAreaEnum.BEAN_VALLEY
    _blacklist = [EXPStarPrize, SlotsPrize]
    _hint = [
        # SetVarToConst(PRIMARY_TEMP_7000, 310),
        # RunDialog(
            # dialog_id=DI2010_DEBUG_7000,
            # above_object=BOWSER,
            # closable=True,
            # sync=False,
            # multiline=True,
            # use_background=True,
        # ),
        JmpIfObjectTriggerDisabledInSpecificLevel(
            NPC_5, R335_BEAN_VALLEY_PIPE_ROOM_RIGHTMOST_PIPE_LARGE_ROOM, ["next"]
        ),
        Jmp(["bean_valley_hint_text"]),
    ]
    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_do_valley_pipes(world, inventory)


__all__ = ["BeanValleyRightPipeLeftChestLocation"]
