from __future__ import annotations
from typing import TYPE_CHECKING
from smrpgpatchbuilder.datatypes.overworld_scripts.event_scripts.commands import *
from randomizer.data.variables.room_names import *
from randomizer.data.variables.event_script_names import *
from randomizer.data.variables.action_script_names import *
from randomizer.data.variables.pack_names import *
from randomizer.logic.progression.prizes import *
from randomizer.types.flags import *
from randomizer.logic.progression.prizelocations.access import (not_earlygame)
from randomizer.logic.progression.prizelocations.bean_valley.mimic3_boss_fight import (Mimic3BossFight)
from randomizer.types.logic import (Inventory)
from randomizer.types.prizelocation import (ShuffleLocationSelector, StarPieceLocation, WorldAreaEnum)
if TYPE_CHECKING:
    from randomizer.types.gameworld import (GameWorld)


class Mimic3StarPiece(StarPieceLocation):
    _bias = True
    _originally_held = None
    _id = ShuffleLocationSelector.BOX_BOY_BOSS
    _rooms = [514]
    _world_area = WorldAreaEnum.BEAN_VALLEY
    _override_id = 514
    _parent = Mimic3BossFight

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return (
            super().can_access(inventory, world)
            and inventory.has_item(ThirdMimicFightLauncher)
            and not_earlygame(world, inventory)
        )


__all__ = ["Mimic3StarPiece"]
