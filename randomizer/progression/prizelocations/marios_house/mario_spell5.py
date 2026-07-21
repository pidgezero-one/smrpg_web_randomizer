from __future__ import annotations
from typing import TYPE_CHECKING
from smrpgpatchbuilder.datatypes.overworld_scripts.event_scripts.commands import *
from randomizer.data.variables.room_names import *
from randomizer.data.variables.event_script_names import *
from randomizer.data.variables.action_script_names import *
from randomizer.data.variables.pack_names import *
from randomizer.progression.prizes import *
from randomizer.types.flags import *
from randomizer.progression.prizelocations.access import (not_earlygame)
from randomizer.types.logic import (Inventory)
from randomizer.types.prizelocation import (SpellSlotLocation)
if TYPE_CHECKING:
    from randomizer.types.gameworld import (GameWorld)


class MarioSpell5(SpellSlotLocation):
    _bias = True
    _originally_held = UltraJumpSpellPrize
    _level = 14

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return not_earlygame(world, inventory) and inventory.has_item(
            MarioRecruitmentPrize
        )


__all__ = ["MarioSpell5"]
