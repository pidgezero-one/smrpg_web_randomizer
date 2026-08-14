from __future__ import annotations
from typing import TYPE_CHECKING
from smrpgpatchbuilder.datatypes.overworld_scripts.event_scripts.commands import *
from randomizer.data.variables.room_names import *
from randomizer.data.variables.event_script_names import *
from randomizer.data.variables.action_script_names import *
from randomizer.data.variables.pack_names import *
from randomizer.logic.progression.prizes import *
from randomizer.types.flags import *
from randomizer.logic.progression.prizelocations.access import (can_damage_enemies_with_spells, can_pass_obstacle_courses, not_earlygame, is_early_midgame, is_late_midgame, is_lategame)
from randomizer.types.logic import (Inventory)
from randomizer.types.prize import (Prize)
from randomizer.types.prizelocation import (BossFightLocation, BossFightLocationNPC, ShuffleLocationSelector, WorldAreaEnum)
from smrpgpatchbuilder.datatypes.overworld_scripts.action_scripts.commands import (A_Pause, A_SetSpriteSequence)
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.area_objects import (NPC_0)
from smrpgpatchbuilder.datatypes.overworld_scripts.event_scripts.classes import (UsableEventScriptCommand)
if TYPE_CHECKING:
    from randomizer.types.gameworld import (GameWorld)


class KeepChandelierBossFight(BossFightLocation):
    _bias = True
    _originally_held = BoomerBossFight
    _id = ShuffleLocationSelector.BOWSERS_KEEP_BOSS_FIGHT_2
    _world_area = WorldAreaEnum.BOWSERS_KEEP
    _rooms = [R400_BOWSERS_KEEP_AREA_13_2ND_THRONE_ROOM_BOOMERS_ROOM]
    _override_id = 521
    _default_battlefield = BF07_BOWSERS_KEEP
    _pack_id = PACK210_KEEP_SECOND_BOSS
    _post_unlocks_event_id = E1237_KEEP_CHANDELIER_BOSS_UNLOCKS
    _npc_slots = [
        BossFightLocationNPC(
            R400_BOWSERS_KEEP_AREA_13_2ND_THRONE_ROOM_BOOMERS_ROOM,
            NPC_0,
            sequence_setter_event_id=E0853_KEEP_FINAL_BOSS_ROOM_SHUFFLED_NPC_ANIMATION_LOADER,
        ),
    ]

    def can_accept(self, prize: Prize, inventory: Inventory, world: GameWorld) -> bool:
        return super().can_accept(prize, inventory, world) and (
            can_damage_enemies_with_spells(world, inventory)
            or not isinstance(prize, MokuraBossFight)
        )

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_pass_obstacle_courses(world, inventory) and not_earlygame(
            world, inventory
        )

    def render(self, world: GameWorld) -> tuple[
        list[list[UsableEventScriptCommand]],
        list[UsableEventScriptCommand],
        list[tuple[int, int, int]],
    ]:
        op = super().render(world)
        assert isinstance(self.prize, BossFightPrize)
        if not isinstance(self.prize, BoomerBossFight):
            assert self._npc_slots is not None
            # Read the NPC model placement chose (cached on the location).
            npc_model = self.resolve_npc_model_for_slot(world, self._npc_slots[0])
            m = npc_model()
            if m.animations.chandelier_challenge is not None:
                world.event_scripts.get_subscript_command_by_identifier(
                    "chandelier_challenge_action_queue_0",
                    "chandelier_challenge",
                    A_SetSpriteSequence,
                ).set_index(m.animations.chandelier_challenge.sequence_id)
                world.event_scripts.get_subscript_command_by_identifier(
                    "chandelier_challenge_action_queue_0",
                    "chandelier_challenge_pause_45",
                    A_Pause,
                ).set_length(m.animations.chandelier_challenge.total_duration)
            else:
                world.event_scripts.delete_subscript_command_by_identifier(
                    "chandelier_challenge_action_queue_0",
                    "chandelier_challenge",
                )
        return op


__all__ = ["KeepChandelierBossFight"]
