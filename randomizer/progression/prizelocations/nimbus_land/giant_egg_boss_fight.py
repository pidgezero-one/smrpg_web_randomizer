from __future__ import annotations
from typing import TYPE_CHECKING
from smrpgpatchbuilder.datatypes.overworld_scripts.event_scripts.commands import *
from randomizer.data.variables.room_names import *
from randomizer.data.variables.event_script_names import *
from randomizer.data.variables.action_script_names import *
from randomizer.data.variables.pack_names import *
from randomizer.progression.prizes import *
from randomizer.types.flags import *
from randomizer.progression.prizelocations.access import (can_access_inner_nimbus, can_damage_enemies_with_spells, not_earlygame)
from randomizer.types.logic import (Inventory)
from randomizer.types.prize import (Prize)
from randomizer.types.prizelocation import (BossFightLocation, ShuffleLocationSelector, WorldAreaEnum)
if TYPE_CHECKING:
    from randomizer.types.gameworld import (GameWorld)


class GiantEggBossFight(BossFightLocation):
    _bias = True
    _originally_held = BirdettaBossFight
    _rooms = [R409_NIMBUS_CASTLE_AREA_09_BIRDOS_ROOM]
    _id = ShuffleLocationSelector.NIMBUS_CASTLE_EGG_BOSS_FIGHT
    _world_area = WorldAreaEnum.NIMBUS_LAND
    _pack_id = PACK175_NIMBUS_CASTLE_SECOND_BOSS
    _post_unlocks_event_id = E1231_EGG_BOSS_UNLOCKS
    _dialogs_expecting_replacement = [DI0049_NIMBUS_EGG_BOSS_TALK_AFTER_WINNING]

    def can_accept(self, prize: Prize, inventory: Inventory, world: GameWorld) -> bool:
        return super().can_accept(prize, inventory, world) and (
            can_damage_enemies_with_spells(world, inventory)
            or not isinstance(prize, MokuraBossFight)
        )

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_inner_nimbus(world, inventory) and not_earlygame(
            world, inventory
        )


__all__ = ["GiantEggBossFight"]
