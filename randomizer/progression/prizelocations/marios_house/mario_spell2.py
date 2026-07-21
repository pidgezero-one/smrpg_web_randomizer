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
from randomizer.types.prizelocation import (SpellSlotLocation)
if TYPE_CHECKING:
    from randomizer.types.gameworld import (GameWorld)


class MarioSpell2(SpellSlotLocation):
    _bias = True
    _originally_held = FireOrbSpellPrize
    _level = 3

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return inventory.has_item(MarioRecruitmentPrize)


__all__ = ["MarioSpell2"]
