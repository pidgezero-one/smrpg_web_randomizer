from __future__ import annotations
from typing import TYPE_CHECKING
from smrpgpatchbuilder.datatypes.overworld_scripts.event_scripts.commands import *
from randomizer.data.variables.room_names import *
from randomizer.data.variables.event_script_names import *
from randomizer.data.variables.action_script_names import *
from randomizer.data.variables.pack_names import *
from randomizer.logic.progression.prizes import *
from randomizer.types.flags import *
from randomizer.logic.progression.prizelocations.access import (can_damage_enemies_with_spells, can_pass_obstacle_courses, not_earlygame, is_early_midgame, is_late_midgame, is_lategame, expect_good_movement, expect_halfway_decent_movement, almost_earlygame, is_midgame, expect_ok_movement, lategame, can_exit_keep, can_clear_keep)
from randomizer.types.logic import (Inventory)
from randomizer.types.prize import (Prize)
from randomizer.types.prizelocation import (BossFightLocation, ShuffleLocationSelector, WorldAreaEnum)
from smrpgpatchbuilder.datatypes.overworld_scripts.event_scripts.classes import (EventScript, UsableEventScriptCommand)
if TYPE_CHECKING:
    from randomizer.types.gameworld import (GameWorld)


class KeepFinalBossFight(BossFightLocation):
    _bias = True
    _originally_held = ExorBossFight
    _id = ShuffleLocationSelector.BOWSERS_KEEP_BOSS_FIGHT_3
    _world_area = WorldAreaEnum.BOWSERS_KEEP
    _rooms = [R400_BOWSERS_KEEP_AREA_13_2ND_THRONE_ROOM_BOOMERS_ROOM]
    _override_id = 522
    _default_battlefield = BF07_BOWSERS_KEEP
    _pack_id = PACK186_KEEP_THIRD_BOSS
    _post_unlocks_event_id = E1238_KEEP_EXIT_BOSS_UNLOCKS

    def can_accept(self, prize: Prize, inventory: Inventory, world: GameWorld) -> bool:
        return super().can_accept(prize, inventory, world) and (
            can_damage_enemies_with_spells(world, inventory)
            or not isinstance(prize, MokuraBossFight)
        )

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return (
            can_clear_keep(world, inventory)
        )

    def post_unlocks(self, world: GameWorld) -> EventScript:
        content: list[UsableEventScriptCommand] = []
        if world.settings.is_flag_value(FactoryGate, FactoryGating.KEEP):
            content.extend(
                [
                    SetBit(MAP_GATE),
                    SetBit(MAP_DIRECTIONAL_BOWSERS_KEEP_GATE),
                ]
            )
        parent = super().post_unlocks(world)
        return EventScript(content + parent.contents + [Return()])


__all__ = ["KeepFinalBossFight"]
