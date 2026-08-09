from __future__ import annotations
from typing import TYPE_CHECKING
from smrpgpatchbuilder.datatypes.overworld_scripts.event_scripts.commands import *
from randomizer.data.variables.room_names import *
from randomizer.data.variables.event_script_names import *
from randomizer.data.variables.action_script_names import *
from randomizer.data.variables.pack_names import *
from randomizer.logic.progression.prizes import *
from randomizer.types.flags import *
from randomizer.logic.progression.prizelocations.access import (can_damage_enemies_with_spells)
from randomizer.types.logic import (Inventory)
from randomizer.types.prize import (Prize)
from randomizer.types.prizelocation import (MimicFightLocation, ShuffleLocationSelector, WorldAreaEnum)
if TYPE_CHECKING:
    from randomizer.types.gameworld import (GameWorld)


class Mimic1BossFight(MimicFightLocation):
    _bias = True
    _originally_held = PandoriteBossFight
    _rooms = [512]  # can be in any room.
    _override_id = 512
    _id = ShuffleLocationSelector.PANDORITE_BOSS_FIGHT
    _world_area = WorldAreaEnum.KERO_SEWERS
    _pack_id = PACK156_SEWER_CHEST_FIGHT
    _post_unlocks_event_id = E1249_MIMIC_1_BOSS_UNLOCKS
    _access_conditions = "Stays in Kero Sewers if \"Shuffle mimic chests\" is disabled."

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return inventory.has_item(FirstMimicFightLauncher)

    def can_accept(self, prize: Prize, inventory: Inventory, world: GameWorld) -> bool:
        return super().can_accept(prize, inventory, world) and (
            can_damage_enemies_with_spells(world, inventory)
            or not isinstance(prize, MokuraBossFight)
        )


__all__ = ["Mimic1BossFight"]
