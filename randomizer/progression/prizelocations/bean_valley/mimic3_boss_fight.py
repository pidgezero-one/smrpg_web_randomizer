from __future__ import annotations
from typing import TYPE_CHECKING
from smrpgpatchbuilder.datatypes.overworld_scripts.event_scripts.commands import *
from randomizer.data.variables.room_names import *
from randomizer.data.variables.event_script_names import *
from randomizer.data.variables.action_script_names import *
from randomizer.data.variables.pack_names import *
from randomizer.progression.prizes import *
from randomizer.types.flags import *
from randomizer.progression.prizelocations.access import (can_damage_enemies_with_spells, not_earlygame)
from randomizer.types.logic import (Inventory)
from randomizer.types.prize import (Prize)
from randomizer.types.prizelocation import (MimicFightLocation, ShuffleLocationSelector, WorldAreaEnum)
if TYPE_CHECKING:
    from randomizer.types.gameworld import (GameWorld)


class Mimic3BossFight(MimicFightLocation):
    _bias = True
    _originally_held = BoxBoyBossFight
    _rooms = [514]  # can be in any room.
    _override_id = 514
    _id = ShuffleLocationSelector.BOX_BOY_BOSS_FIGHT
    _world_area = WorldAreaEnum.BEAN_VALLEY
    _pack_id = PACK158_VALLEY_CHEST_FIGHT
    _slots_pack_id = PACK160_SLOTS_CHEST_FIGHT
    _post_unlocks_event_id = E1251_MIMIC_3_BOSS_UNLOCKS

    def can_accept(self, prize: Prize, inventory: Inventory, world: GameWorld) -> bool:
        return super().can_accept(prize, inventory, world) and (
            can_damage_enemies_with_spells(world, inventory)
            or not isinstance(prize, MokuraBossFight)
        )

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return inventory.has_item(ThirdMimicFightLauncher) and not_earlygame(
            world, inventory
        )


__all__ = ["Mimic3BossFight"]
