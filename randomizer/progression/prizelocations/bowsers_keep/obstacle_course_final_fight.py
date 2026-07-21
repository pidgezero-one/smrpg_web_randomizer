from __future__ import annotations
from typing import TYPE_CHECKING
from smrpgpatchbuilder.datatypes.overworld_scripts.event_scripts.commands import *
from randomizer.data.variables.room_names import *
from randomizer.data.variables.event_script_names import *
from randomizer.data.variables.action_script_names import *
from randomizer.data.variables.pack_names import *
from randomizer.progression.prizes import *
from randomizer.types.flags import *
from randomizer.progression.prizelocations.access import (can_damage_enemies_with_spells, can_pass_obstacle_courses, not_earlygame)
from randomizer.types.logic import (Inventory)
from randomizer.types.prize import (Prize)
from randomizer.types.prizelocation import (BossFightLocation, BossFightLocationNPC, ShuffleLocationSelector, WorldAreaEnum)
from smrpgpatchbuilder.datatypes.overworld_scripts.action_scripts.commands import (A_FaceSouthwest, A_Pause, A_SetSpriteSequence, A_VisibilityOn)
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.area_objects import (NPC_4)
from smrpgpatchbuilder.datatypes.overworld_scripts.event_scripts.classes import (UsableEventScriptCommand)
from typing import (cast)
if TYPE_CHECKING:
    from randomizer.types.gameworld import (GameWorld)


class ObstacleCourseFinalFight(BossFightLocation):
    _bias = True
    _originally_held = ChesterBossFight
    _rooms = [R461_BOWSERS_KEEP_6DOOR_BATTLE_ROOM_1C_1ST_FIGHT_BOBOMB]
    _id = ShuffleLocationSelector.BOWSERS_KEEP_BOSS_FIGHT_CHESTER
    _world_area = WorldAreaEnum.BOWSERS_KEEP
    _pack_id = PACK159_SIX_DOOR_RUSH_FIGHT
    _post_unlocks_event_id = E1235_OBSTACLE_COURSE_BOSS_UNLOCKS
    _npc_slots = [
        BossFightLocationNPC(
            R461_BOWSERS_KEEP_6DOOR_BATTLE_ROOM_1C_1ST_FIGHT_BOBOMB,
            NPC_4,
            sequence_setter_event_id=E0845_VOLCANO_BRIEF_HENCHMAN_ROOM_SHUFFLED_NPC_ANIMATION_LOADER,
        )
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
        if not isinstance(
            self.prize,
            (PandoriteBossFight, HidonBossFight, BoxBoyBossFight, ChesterBossFight),
        ):
            m = self.prize.smallest_npc()
            a = m.animations.dojo_challenge
            if a is not None and a.total_duration is not None:
                cast(
                    ActionQueueAsync,
                    world.event_scripts.get_command_by_identifier(
                        "keep_obstacle_boss_intro",
                    ),
                ).set_subscript(
                    [
                        A_FaceSouthwest(),
                        A_VisibilityOn(),
                        A_Pause(40),
                        A_SetSpriteSequence(
                            index=a.sequence_id, looping=False, is_sequence=True
                        ),
                        A_Pause(a.total_duration),
                    ]
                )
            else:
                cast(
                    ActionQueueAsync,
                    world.event_scripts.get_command_by_identifier(
                        "keep_obstacle_boss_intro",
                    ),
                ).set_subscript(
                    [
                        A_FaceSouthwest(),
                        A_VisibilityOn(),
                        A_Pause(40),
                        A_Pause(50),
                    ]
                )
        return op


__all__ = ["ObstacleCourseFinalFight"]
