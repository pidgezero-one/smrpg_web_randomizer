from __future__ import annotations
from typing import TYPE_CHECKING
from smrpgpatchbuilder.datatypes.overworld_scripts.event_scripts.commands import *
from randomizer.data.variables.room_names import *
from randomizer.data.variables.event_script_names import *
from randomizer.data.variables.action_script_names import *
from randomizer.data.variables.pack_names import *
from randomizer.progression.prizes import *
from randomizer.types.flags import *
from randomizer.types.logic import (Inventory)
from randomizer.types.prizelocation import (NPCLocationRow1, ShuffleLocationSelector, WorldAreaEnum)
if TYPE_CHECKING:
    from randomizer.types.gameworld import (GameWorld)


class Mimic2DropRewardLocation(NPCLocationRow1):
    _bias = True
    _originally_held = SafetyBadgePrize
    _rooms = [513]  # can be in any room, custom id.
    _id = ShuffleLocationSelector.HIDON_REWARD_1
    _world_area = WorldAreaEnum.SUNKEN_SHIP
    _override_id = 513

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return inventory.has_item(SecondMimicFightLauncher)


__all__ = ["Mimic2DropRewardLocation"]
