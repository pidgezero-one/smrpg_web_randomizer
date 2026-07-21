from __future__ import annotations
from typing import TYPE_CHECKING
from smrpgpatchbuilder.datatypes.overworld_scripts.event_scripts.commands import *
from randomizer.data.variables.room_names import *
from randomizer.data.variables.event_script_names import *
from randomizer.data.variables.action_script_names import *
from randomizer.data.variables.pack_names import *
from randomizer.progression.prizes import *
from randomizer.types.flags import *
from randomizer.logic.renders import (render_inner_factory_third_fight_slot)
from randomizer.progression.prizelocations.access import (can_access_factory, can_damage_enemies_with_spells, not_earlygame)
from randomizer.types.logic import (Inventory)
from randomizer.types.prize import (Prize)
from randomizer.types.prizelocation import (BossFightLocation, BossFightLocationHenchmanNPC, BossFightLocationNPC, ShuffleLocationSelector, WorldAreaEnum)
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.area_objects import (NPC_10, NPC_7, NPC_8, NPC_9)
from smrpgpatchbuilder.datatypes.overworld_scripts.event_scripts.classes import (UsableEventScriptCommand)
if TYPE_CHECKING:
    from randomizer.types.gameworld import (GameWorld)


class InnerFactoryThirdFight(BossFightLocation):
    _bias = True
    _originally_held = DirectorBossFight
    _rooms = [R472_FACTORY_GROUNDS_AREA_03]
    _id = ShuffleLocationSelector.INNER_FACTORY_BOSS_FIGHT_3
    _world_area = WorldAreaEnum.INNER_FACTORY
    _pack_id = PACK148_FACTORY_BOSS_RUSH_3
    _post_unlocks_event_id = E1243_INNER_FACTORY_3_BOSS_UNLOCKS
    _npc_slots = [
        BossFightLocationNPC(
            R472_FACTORY_GROUNDS_AREA_03,
            NPC_10,
            sequence_setter_event_id=E0857_INNER_FACTORY_3RD_ROOM_SHUFFLED_NPC_ANIMATION_LOADER,
        ),
    ]
    _character_henchman_slots = [
        BossFightLocationHenchmanNPC([R472_FACTORY_GROUNDS_AREA_03], [NPC_7]),
        BossFightLocationHenchmanNPC([R472_FACTORY_GROUNDS_AREA_03], [NPC_8]),
        BossFightLocationHenchmanNPC([R472_FACTORY_GROUNDS_AREA_03], [NPC_9]),
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
        assert isinstance(self.prize, BossFightPrize)

        # Process each slot separately
        for slot_index in range(3):
            if (
                self.prize.character_henchmen is not None
                and len(self.prize.character_henchmen) > slot_index
            ):
                render_inner_factory_third_fight_slot(
                    world, self.prize.character_henchmen[slot_index], slot_index
                )

        return op


__all__ = ["InnerFactoryThirdFight"]
