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
from randomizer.types.prize import (FPFlowerPrize)
from randomizer.types.prizelocation import (ShuffleLocationSelector, TreasureChestLocationRow2, WorldAreaEnum)
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.area_objects import (NPC_2)
if TYPE_CHECKING:
    from randomizer.types.gameworld import (GameWorld)


class BeanstalkLowerCloudRightChestLocation(TreasureChestLocationRow2):
    _originally_held = FPFlowerPrize
    _rooms = [R373_NIMBUS_LAND_FALL_FROM_PLATFORM_3RD]
    _npc_ids = [NPC_2]
    _id = ShuffleLocationSelector.BEAN_VALLEY_FALL_2
    _world_area = WorldAreaEnum.BEAN_VALLEY
    _blacklist = [EXPStarPrize]
    _hint = [
        # SetVarToConst(PRIMARY_TEMP_7000, 337),
        # RunDialog(
            # dialog_id=DI2010_DEBUG_7000,
            # above_object=BOWSER,
            # closable=True,
            # sync=False,
            # multiline=True,
            # use_background=True,
        # ),
        JmpIfObjectTriggerDisabledInSpecificLevel(
            NPC_2, R373_NIMBUS_LAND_FALL_FROM_PLATFORM_3RD, ["next"]
        ),
        Jmp(["beanstalk_hint_text"]),
    ]
    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_valley(world, inventory)


__all__ = ["BeanstalkLowerCloudRightChestLocation"]
