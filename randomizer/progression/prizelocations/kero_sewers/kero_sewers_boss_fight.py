from __future__ import annotations
from typing import TYPE_CHECKING
from smrpgpatchbuilder.datatypes.overworld_scripts.event_scripts.commands import *
from randomizer.data.variables.room_names import *
from randomizer.data.variables.event_script_names import *
from randomizer.data.variables.action_script_names import *
from randomizer.data.variables.pack_names import *
from randomizer.progression.prizes import *
from randomizer.types.flags import *
from randomizer.progression.prizelocations.access import (can_access_sewer, can_damage_enemies_with_spells)
from randomizer.types.logic import (Inventory)
from randomizer.types.prize import (Prize)
from randomizer.types.prizelocation import (BossFightLocation, BossFightLocationNPC, ShuffleLocationSelector, WorldAreaEnum)
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.area_objects import (NPC_1)
if TYPE_CHECKING:
    from randomizer.types.gameworld import (GameWorld)


class KeroSewersBossFight(BossFightLocation):
    _bias = True
    _originally_held = Belome1BossFight
    _rooms = [R302_KERO_SEWERS_AREA_08_BELOMES_ROOM]
    _id = ShuffleLocationSelector.KERO_SEWERS_BOSS
    _world_area = WorldAreaEnum.KERO_SEWERS
    _pack_id = PACK168_SEWER_BOSS
    _post_unlocks_event_id = E1197_KERO_SEWER_BOSS_UNLOCKS
    _npc_slots = [
        BossFightLocationNPC(
            R302_KERO_SEWERS_AREA_08_BELOMES_ROOM,
            NPC_1,
            sequence_setter_event_id=E0772_KERO_SEWERS_BELOME_ROOM_SHUFFLED_NPC_ANIMATION_LOADER,
        ),
    ]

    def can_accept(self, prize: Prize, inventory: Inventory, world: GameWorld) -> bool:
        return super().can_accept(prize, inventory, world) and (
            can_damage_enemies_with_spells(world, inventory)
            or not isinstance(prize, MokuraBossFight)
        )

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_sewer(world, inventory)


__all__ = ["KeroSewersBossFight"]
