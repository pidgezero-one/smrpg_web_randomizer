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
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.area_objects import (NPC_14)
if TYPE_CHECKING:
    from randomizer.types.gameworld import (GameWorld)


class BeanValleyRightPipeAboveGroundLocation(TreasureChestLocationRow1):
    _originally_held = FrogCoin1Prize
    _rooms = [R251_BEAN_VALLEY_PIRANHA_PIPE_AREA]
    _npc_ids = [NPC_14]
    _id = ShuffleLocationSelector.BEAN_VALLEY_PIRANHA_PLANTS
    _world_area = WorldAreaEnum.BEAN_VALLEY
    _blacklist = [EXPStarPrize, SlotsPrize]
    _hint = [
        # SetVarToConst(PRIMARY_TEMP_7000, 313),
        # RunDialog(
            # dialog_id=DI2010_DEBUG_7000,
            # above_object=BOWSER,
            # closable=True,
            # sync=False,
            # multiline=True,
            # use_background=True,
        # ),
        JmpIfObjectTriggerDisabledInSpecificLevel(
            NPC_14, R251_BEAN_VALLEY_PIRANHA_PIPE_AREA, ["next"]
        ),
        Jmp(["bean_valley_hint_text"]),
    ]
    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_do_valley_pipes(world, inventory)


__all__ = ["BeanValleyRightPipeAboveGroundLocation"]
