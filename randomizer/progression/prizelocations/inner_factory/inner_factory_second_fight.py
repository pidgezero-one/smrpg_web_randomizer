from __future__ import annotations
from typing import TYPE_CHECKING
from smrpgpatchbuilder.datatypes.overworld_scripts.event_scripts.commands import *
from randomizer.data.variables.room_names import *
from randomizer.data.variables.event_script_names import *
from randomizer.data.variables.action_script_names import *
from randomizer.data.variables.pack_names import *
from randomizer.progression.prizes import *
from randomizer.types.flags import *
from randomizer.logic.renders import (render_inner_factory_second_fight)
from randomizer.progression.prizelocations.access import (can_access_factory, can_damage_enemies_with_spells, not_earlygame)
from randomizer.types.logic import (Inventory)
from randomizer.types.prize import (Prize)
from randomizer.types.prizelocation import (BossFightLocation, BossFightLocationHenchmanNPC, BossFightLocationNPC, RemoveIfNotFilled, ShuffleLocationSelector, WorldAreaEnum)
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.area_objects import (NPC_12, NPC_13, NPC_14, NPC_15)
from smrpgpatchbuilder.datatypes.overworld_scripts.event_scripts.classes import (UsableEventScriptCommand)
if TYPE_CHECKING:
    from randomizer.types.gameworld import (GameWorld)


class InnerFactorySecondFight(BossFightLocation):
    _bias = True
    _originally_held = ManagerBossFight
    _rooms = [R471_FACTORY_GROUNDS_AREA_02]
    _id = ShuffleLocationSelector.INNER_FACTORY_BOSS_FIGHT_2
    _world_area = WorldAreaEnum.INNER_FACTORY
    _pack_id = PACK147_FACTORY_BOSS_RUSH_2
    _post_unlocks_event_id = E1242_INNER_FACTORY_2_BOSS_UNLOCKS
    _npc_slots = [
        BossFightLocationNPC(
            R471_FACTORY_GROUNDS_AREA_02,
            NPC_15,
            sequence_setter_event_id=E0856_INNER_FACTORY_2ND_ROOM_SHUFFLED_NPC_ANIMATION_LOADER,
        ),
    ]
    _character_henchman_slots = [
        BossFightLocationHenchmanNPC(
            [R471_FACTORY_GROUNDS_AREA_02],
            [NPC_12],
            remove_if_not_filled=RemoveIfNotFilled.ALWAYS,
        ),
        BossFightLocationHenchmanNPC(
            [R471_FACTORY_GROUNDS_AREA_02],
            [NPC_13],
            remove_if_not_filled=RemoveIfNotFilled.ALWAYS,
        ),
        BossFightLocationHenchmanNPC(
            [R471_FACTORY_GROUNDS_AREA_02],
            [NPC_14],
            remove_if_not_filled=RemoveIfNotFilled.ALWAYS,
        ),
    ]

    def can_accept(self, prize: Prize, inventory: Inventory, world: GameWorld) -> bool:
        return super().can_accept(prize, inventory, world) and (
            can_damage_enemies_with_spells(world, inventory)
            or not isinstance(prize, MokuraBossFight)
        )

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_factory(world, inventory) and not_earlygame(world, inventory)

    def render(self, world: GameWorld) -> tuple[
        list[list[UsableEventScriptCommand]],
        list[UsableEventScriptCommand],
        list[tuple[int, int, int]],
    ]:
        op = super().render(world)
        if isinstance(self.prize, self._originally_held):
            return op
        assert isinstance(self.prize, BossFightPrize)
        render_inner_factory_second_fight(world, self.prize)
        return op


__all__ = ["InnerFactorySecondFight"]
