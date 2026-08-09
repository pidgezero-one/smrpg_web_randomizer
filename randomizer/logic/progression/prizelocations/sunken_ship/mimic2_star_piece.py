from __future__ import annotations
from typing import TYPE_CHECKING
from smrpgpatchbuilder.datatypes.overworld_scripts.event_scripts.commands import *
from randomizer.data.variables.room_names import *
from randomizer.data.variables.event_script_names import *
from randomizer.data.variables.action_script_names import *
from randomizer.data.variables.pack_names import *
from randomizer.logic.progression.prizes import *
from randomizer.types.flags import *
from randomizer.logic.progression.prizelocations.sunken_ship.mimic2_boss_fight import (Mimic2BossFight)
from randomizer.types.logic import (Inventory)
from randomizer.types.prizelocation import (ShuffleLocationSelector, StarPieceLocation, WorldAreaEnum)
if TYPE_CHECKING:
    from randomizer.types.gameworld import (GameWorld)


class Mimic2StarPiece(StarPieceLocation):
    _bias = True
    _originally_held = None
    _id = ShuffleLocationSelector.HIDON_BOSS
    _world_area = WorldAreaEnum.SUNKEN_SHIP
    _rooms = [513]
    _override_id = 513
    _parent = Mimic2BossFight
    _access_conditions = "Stays in Sunken Ship if \"Shuffle mimic chests\" is disabled."

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return inventory.has_item(SecondMimicFightLauncher)


__all__ = ["Mimic2StarPiece"]
