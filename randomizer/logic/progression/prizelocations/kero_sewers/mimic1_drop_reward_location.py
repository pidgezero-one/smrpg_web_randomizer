from __future__ import annotations
from typing import TYPE_CHECKING
from smrpgpatchbuilder.datatypes.overworld_scripts.event_scripts.commands import *
from randomizer.data.variables.room_names import *
from randomizer.data.variables.event_script_names import *
from randomizer.data.variables.action_script_names import *
from randomizer.data.variables.pack_names import *
from randomizer.logic.progression.prizes import *
from randomizer.types.flags import *
from randomizer.logic.progression.prizelocations.access import (expect_good_movement, not_earlygame, expect_halfway_decent_movement, almost_earlygame, is_midgame, expect_ok_movement, lategame)
from randomizer.types.logic import (Inventory)
from randomizer.types.prizelocation import (NPCLocationRow1, ShuffleLocationSelector, WorldAreaEnum)
if TYPE_CHECKING:
    from randomizer.types.gameworld import (GameWorld)


class Mimic1DropRewardLocation(NPCLocationRow1):
    _bias = True
    _originally_held = TrueformPinPrize
    _rooms = [512]  # can be in any room, custom id.
    _id = ShuffleLocationSelector.PANDORITE_REWARD_1
    _world_area = WorldAreaEnum.KERO_SEWERS
    _override_id = 512
    _access_conditions = "Stays in Kero Sewers if \"Shuffle mimic chests\" is disabled."

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return inventory.has_item(FirstMimicFightLauncher)


__all__ = ["Mimic1DropRewardLocation"]
