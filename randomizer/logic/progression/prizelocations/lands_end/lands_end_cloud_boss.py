from __future__ import annotations
from typing import TYPE_CHECKING
from smrpgpatchbuilder.datatypes.overworld_scripts.event_scripts.commands import *
from randomizer.data.variables.room_names import *
from randomizer.data.variables.event_script_names import *
from randomizer.data.variables.action_script_names import *
from randomizer.data.variables.pack_names import *
from randomizer.logic.progression.prizes import *
from randomizer.types.flags import *
from randomizer.logic.progression.prizelocations.access import (can_damage_enemies_with_spells, not_earlygame)
from randomizer.types.logic import (Inventory)
from randomizer.types.prize import (Prize)
from randomizer.types.prizelocation import (BossFightLocation, ShuffleLocationSelector, WorldAreaEnum)
if TYPE_CHECKING:
    from randomizer.types.gameworld import (GameWorld)


class LandsEndCloudBoss(BossFightLocation):
    _bias = True
    _originally_held = MokuraBossFight
    _id = ShuffleLocationSelector.LANDS_END_CLOUD_BOSS_FIGHT
    _world_area = WorldAreaEnum.LANDS_END
    _rooms = [
        R137_LANDS_END_AREA_01,
        R317_LANDS_END_DESERT_AREA_01,
        R318_LANDS_END_DESERT_AREA_02,
        R319_LANDS_END_DESERT_AREA_06,
        R402_LANDS_END_DESERT_AREA_03,
        R403_LANDS_END_DESERT_AREA_05,
        R404_LANDS_END_DESERT_AREA_04,
        R424_BELOME_TEMPLE_AREA_03_PIPE_TO_ROOM_DETERMINED_BY_FORTUNE,
        R425_BELOME_TEMPLE_AREA_05_FROM_FORTUNE_ROOM,
        R426_BELOME_TEMPLE_AREA_07_PIPE_TO_BELOMES_ROOM,
        R428_BELOME_TEMPLE_AREA_01_WWARP_TRAMPOLINE,
    ]
    _override_id = 519
    _pack_id = PACK207_LANDS_END_CLOUD
    _post_unlocks_event_id = E1210_CLOUD_BOSS_UNLOCKS

    def can_accept(self, prize: Prize, inventory: Inventory, world: GameWorld) -> bool:
        return super().can_accept(prize, inventory, world) and (
            can_damage_enemies_with_spells(world, inventory)
            or not isinstance(prize, MokuraBossFight)
        )

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return not_earlygame(world, inventory)


__all__ = ["LandsEndCloudBoss"]
