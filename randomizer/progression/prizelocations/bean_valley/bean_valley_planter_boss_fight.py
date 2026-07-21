from __future__ import annotations
from typing import TYPE_CHECKING
from smrpgpatchbuilder.datatypes.overworld_scripts.event_scripts.commands import *
from randomizer.data.variables.room_names import *
from randomizer.data.variables.event_script_names import *
from randomizer.data.variables.action_script_names import *
from randomizer.data.variables.pack_names import *
from randomizer.progression.prizes import *
from randomizer.types.flags import *
from randomizer.logic.renders import (render_bean_valley_planter_boss)
from randomizer.progression.prizelocations.access import (can_damage_enemies_with_spells, not_earlygame)
from randomizer.types.logic import (Inventory)
from randomizer.types.prize import (Prize)
from randomizer.types.prizelocation import (BossFightLocation, BossFightLocationNPC, ShuffleLocationSelector, WorldAreaEnum)
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.area_objects import (NPC_1, NPC_2)
from smrpgpatchbuilder.datatypes.overworld_scripts.event_scripts.classes import (EventScript, UsableEventScriptCommand)
if TYPE_CHECKING:
    from randomizer.types.gameworld import (GameWorld)


class BeanValleyPlanterBossFight(BossFightLocation):
    _bias = True
    _originally_held = MegasmilaxBossFight
    _rooms = [R254_BEAN_VALLEY_SMILAX_AREA]
    _id = ShuffleLocationSelector.BEAN_VALLEY_BOSS_FIGHT
    _world_area = WorldAreaEnum.BEAN_VALLEY
    _pack_id = PACK173_VALLEY_BOSS
    _post_unlocks_event_id = E1229_BEAN_VALLEY_BOSS_UNLOCKS
    _npc_slots = [
        BossFightLocationNPC(
            R254_BEAN_VALLEY_SMILAX_AREA,
            NPC_1,
            sequence_setter_event_id=E0817_BEAN_VALLEY_BOSS_ROOM_SHUFFLED_NPC_ANIMATION_LOADER,
        ),
    ]

    def can_accept(self, prize: Prize, inventory: Inventory, world: GameWorld) -> bool:
        return super().can_accept(prize, inventory, world) and (
            can_damage_enemies_with_spells(world, inventory)
            or not isinstance(prize, MokuraBossFight)
        )

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return not_earlygame(world, inventory)

    def post_unlocks(self, world: GameWorld) -> EventScript:
        content: list[UsableEventScriptCommand] = []
        if world.settings.is_flag_value(NimbusGate, NimbusGating.VALLEY):
            content.extend(
                [
                    SetBit(NIMBUS_MAINLAND_UNLOCKED),
                    RemoveObjectFromSpecificLevel(
                        NPC_2, R369_NIMBUS_LAND_ENTRANCE_WWARP_TRAMPOLINE
                    ),
                ]
            )
        parent = super().post_unlocks(world)
        return EventScript(content + parent.contents + [Return()])

    def render(self, world: GameWorld) -> tuple[
        list[list[UsableEventScriptCommand]],
        list[UsableEventScriptCommand],
        list[tuple[int, int, int]],
    ]:
        op = super().render(world)
        assert isinstance(self.prize, BossFightPrize)
        if not isinstance(self.prize, (MegasmilaxBossFight)):
            render_bean_valley_planter_boss(world, self.prize)
        return op


__all__ = ["BeanValleyPlanterBossFight"]
