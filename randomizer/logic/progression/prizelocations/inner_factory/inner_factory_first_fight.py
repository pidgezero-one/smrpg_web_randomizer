from __future__ import annotations
from typing import TYPE_CHECKING
from smrpgpatchbuilder.datatypes.overworld_scripts.event_scripts.commands import *
from randomizer.data.variables.room_names import *
from randomizer.data.variables.event_script_names import *
from randomizer.data.variables.action_script_names import *
from randomizer.data.variables.pack_names import *
from randomizer.logic.progression.prizes import *
from randomizer.types.flags import *
from randomizer.logic.progression.prizelocations.access import (can_access_factory, can_damage_enemies_with_spells, not_earlygame, is_early_midgame, is_late_midgame, is_lategame)
from randomizer.types.logic import (Inventory)
from randomizer.types.prize import (Prize)
from randomizer.types.prizelocation import (BossFightLocation, BossFightLocationHenchmanNPC, BossFightLocationNPC, RemoveIfNotFilled, ShuffleLocationSelector, WorldAreaEnum)
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.area_objects import (NPC_6, NPC_7, NPC_8)
if TYPE_CHECKING:
    from randomizer.types.gameworld import (GameWorld)


class InnerFactoryFirstFight(BossFightLocation):
    _bias = True
    _originally_held = ClerkBossFight
    _rooms = [R469_FACTORY_GROUNDS_AREA_01]
    _id = ShuffleLocationSelector.INNER_FACTORY_BOSS_FIGHT_1
    _world_area = WorldAreaEnum.INNER_FACTORY
    _pack_id = PACK146_FACTORY_BOSS_RUSH_1
    _post_unlocks_event_id = E1241_INNER_FACTORY_1_BOSS_UNLOCKS
    _npc_slots = [
        BossFightLocationNPC(
            R469_FACTORY_GROUNDS_AREA_01,
            NPC_8,
            sequence_setter_event_id=E0855_INNER_FACTORY_1ST_ROOM_SHUFFLED_NPC_ANIMATION_LOADER,
        ),
    ]

    _character_henchman_slots = [
        BossFightLocationHenchmanNPC(
            [R469_FACTORY_GROUNDS_AREA_01],
            [NPC_7],
            PACK150_FACTORY_BOSS_RUSH_HENCHMAN,
            skip_swap_if_flag=KeepMinigameSpritesIntact,
            remove_if_not_filled=RemoveIfNotFilled.IF_ANY_FILLED,
        ),
        BossFightLocationHenchmanNPC(
            [R469_FACTORY_GROUNDS_AREA_01],
            [NPC_6],
            skip_swap_if_flag=KeepMinigameSpritesIntact,
            remove_if_not_filled=RemoveIfNotFilled.IF_ANY_FILLED,
        ),
    ]

    def can_accept(self, prize: Prize, inventory: Inventory, world: GameWorld) -> bool:
        return super().can_accept(prize, inventory, world) and (
            can_damage_enemies_with_spells(world, inventory)
            or not isinstance(prize, MokuraBossFight)
        )

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_factory(world, inventory) and not_earlygame(world, inventory)


__all__ = ["InnerFactoryFirstFight"]
