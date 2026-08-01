from __future__ import annotations
from typing import TYPE_CHECKING
from smrpgpatchbuilder.datatypes.overworld_scripts.event_scripts.commands import *
from randomizer.data.variables.room_names import *
from randomizer.data.variables.event_script_names import *
from randomizer.data.variables.action_script_names import *
from randomizer.data.variables.pack_names import *
from randomizer.logic.progression.prizes import *
from randomizer.types.flags import *
from randomizer.types.logic import (Inventory)
from randomizer.types.prizelocation import (SpellSlotLocation)
if TYPE_CHECKING:
    from randomizer.types.gameworld import (GameWorld)


class GenoSpell2(SpellSlotLocation):
    _bias = True
    _originally_held = GenoBoostSpellPrize
    _level = 8

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return inventory.has_item(GenoRecruitmentPrize)


__all__ = ["GenoSpell2"]
