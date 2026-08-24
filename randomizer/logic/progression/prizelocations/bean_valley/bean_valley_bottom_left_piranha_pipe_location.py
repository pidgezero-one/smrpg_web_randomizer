from __future__ import annotations
from typing import TYPE_CHECKING
from smrpgpatchbuilder.datatypes.overworld_scripts.event_scripts.commands import *
from randomizer.data.variables.room_names import *
from randomizer.data.variables.event_script_names import *
from randomizer.data.variables.action_script_names import *
from randomizer.data.variables.pack_names import *
from randomizer.logic.progression.prizes import *
from randomizer.types.flags import *
from randomizer.types.prizelocation import (ShuffleLocationSelector, TreasureChestLocationRow1, WorldAreaEnum)
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.area_objects import (NPC_0)
from randomizer.logic.progression.prizelocations.access import (can_access_valley, can_do_valley_pipes, not_earlygame, is_early_midgame, is_late_midgame, is_lategame, expect_good_movement, expect_halfway_decent_movement, almost_earlygame, is_midgame, expect_ok_movement, lategame)
from randomizer.types.logic import (Inventory)
if TYPE_CHECKING:
    from randomizer.types.gameworld import (GameWorld)


class BeanValleyBottomLeftPiranhaPipeLocation(TreasureChestLocationRow1):
    _originally_held = SlotsPrize2
    _rooms = [R348_BEAN_VALLEY_PIPE_ROOM_BOTTOM_LEFT]
    _npc_ids = [NPC_0]
    _id = ShuffleLocationSelector.BEAN_VALLEY_BOTTOM_LEFT_PIRANHA_PIPE
    _world_area = WorldAreaEnum.BEAN_VALLEY
    _blacklist = [EXPStarPrize]
    _hint = [
        # SetVarToConst(PRIMARY_TEMP_7000, 307),
        # RunDialog(
            # dialog_id=DI2010_DEBUG_7000,
            # above_object=BOWSER,
            # closable=True,
            # sync=False,
            # multiline=True,
            # use_background=True,
        # ),
        JmpIfObjectTriggerDisabledInSpecificLevel(
            NPC_0, R348_BEAN_VALLEY_PIPE_ROOM_BOTTOM_LEFT, ["next"]
        ),
        Jmp(["bean_valley_hint_text"]),
    ]
    _access_conditions = "Not a check if \"Shuffle slot machine chests\" is disabled."
    
    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_do_valley_pipes(world, inventory)


__all__ = ["BeanValleyBottomLeftPiranhaPipeLocation"]
