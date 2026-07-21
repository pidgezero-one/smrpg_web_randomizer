from __future__ import annotations
from typing import TYPE_CHECKING
from smrpgpatchbuilder.datatypes.overworld_scripts.event_scripts.commands import *
from randomizer.data.variables.room_names import *
from randomizer.data.variables.event_script_names import *
from randomizer.data.variables.action_script_names import *
from randomizer.data.variables.pack_names import *
from randomizer.progression.prizes import *
from randomizer.types.flags import *
from randomizer.logic.renders import (render_bandits_way_boss)
from randomizer.progression.prizelocations.access import (can_access_bandits_way, can_damage_enemies_with_spells)
from randomizer.types.logic import (Inventory)
from randomizer.types.prize import (Prize)
from randomizer.types.prizelocation import (BossFightLocation, BossFightLocationNPC, ShuffleLocationSelector, WorldAreaEnum)
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.area_objects import (NPC_10, NPC_12, NPC_5, NPC_8)
if TYPE_CHECKING:
    from randomizer.types.gameworld import (GameWorld)


class BanditsWayBossFight(BossFightLocation):
    _bias = True
    _originally_held = Croco1BossFight
    _rooms = [R206_BANDITS_WAY_AREA_05]
    _id = ShuffleLocationSelector.BANDITS_WAY_BOSS_FIGHT
    _world_area = WorldAreaEnum.BANDITS_WAY
    _pack_id = PACK163_BANDITS_WAY_BOSS
    _post_unlocks_event_id = E1195_BANDITS_WAY_BOSS_UNLOCKS

    _npc_slots = [
        BossFightLocationNPC(
            R076_BANDITS_WAY_AREA_01,
            NPC_5,
            sequence_setter_event_id=E0757_BANDITS_WAY_AREA_01_SHUFFLED_NPC_ANIMATION_LOADER,
        ),
        BossFightLocationNPC(
            R207_BANDITS_WAY_AREA_02,
            NPC_8,
            sequence_setter_event_id=E0756_BANDITS_WAY_AREA_02_SHUFFLED_NPC_ANIMATION_LOADER,
        ),
        BossFightLocationNPC(
            R077_BANDITS_WAY_AREA_03,
            NPC_8,
            sequence_setter_event_id=E0758_BANDITS_WAY_AREA_03_SHUFFLED_NPC_ANIMATION_LOADER,
        ),
        BossFightLocationNPC(
            R078_BANDITS_WAY_AREA_04,
            NPC_12,
            sequence_setter_event_id=E0759_BANDITS_WAY_AREA_04_SHUFFLED_NPC_ANIMATION_LOADER,
        ),
        BossFightLocationNPC(
            R206_BANDITS_WAY_AREA_05,
            NPC_8,
            sequence_setter_event_id=E0760_BANDITS_WAY_AREA_05_SHUFFLED_NPC_ANIMATION_LOADER,
        ),
        BossFightLocationNPC(
            R505_ENDING_CREDITS_YOSTER_ISLE_CROCO_RACING_YOSHI,
            NPC_10,
            sequence_setter_event_id=E1193_ENDING_CREDITS_YOSTER_SHUFFLED_NPC_ANIMATION_LOADER,
        ),
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_bandits_way(world, inventory)

    def can_accept(self, prize: Prize, inventory: Inventory, world: GameWorld) -> bool:
        return super().can_accept(prize, inventory, world) and (
            can_damage_enemies_with_spells(world, inventory)
            or not isinstance(prize, MokuraBossFight)
        )

    def render(self, world: GameWorld):
        """Set animation scripts for this boss to be more specific for the character"""
        assert isinstance(self.prize, BossFightPrize)
        w = super().render(world)
        render_bandits_way_boss(world, self.prize)
        return w


__all__ = ["BanditsWayBossFight"]
