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
from randomizer.types.prizelocation import (ShuffleLocationSelector, StandingLocationRow2, WorldAreaEnum)
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.area_objects import (NPC_4)
if TYPE_CHECKING:
    from randomizer.types.gameworld import (GameWorld)


class BeanValley1stRoomMiddleCoinLocation(StandingLocationRow2):
    _originally_held = Coins10Prize
    _rooms = [R378_BEAN_VALLEY_BEANSTALKS_AREA_01]
    _npc_ids = [NPC_4]
    _id = ShuffleLocationSelector.BEAN_VALLEY_FIRST_VINE_ROOM_MIDDLE_COIN
    _world_area = WorldAreaEnum.BEAN_VALLEY
    _hint = [
        # SetVarToConst(PRIMARY_TEMP_7000, 318),
        # RunDialog(
            # dialog_id=DI2010_DEBUG_7000,
            # above_object=BOWSER,
            # closable=True,
            # sync=False,
            # multiline=True,
            # use_background=True,
        # ),
        # JmpIfObjectNotInSpecificLevel(NPC_4, R378_BEAN_VALLEY_BEANSTALKS_AREA_01, ["next"]),
        # Jmp(["beanstalk_hint_text"])
    ]
    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_valley(world, inventory)


__all__ = ["BeanValley1stRoomMiddleCoinLocation"]
