from __future__ import annotations
from typing import TYPE_CHECKING
from smrpgpatchbuilder.datatypes.overworld_scripts.event_scripts.commands import *
from randomizer.data.variables.room_names import *
from randomizer.data.variables.event_script_names import *
from randomizer.data.variables.action_script_names import *
from randomizer.data.variables.pack_names import *
from randomizer.logic.progression.prizes import *
from randomizer.types.flags import *
from smrpgpatchbuilder.datatypes.overworld_scripts.action_scripts.classes import (ActionScript)
from smrpgpatchbuilder.datatypes.overworld_scripts.action_scripts.commands.commands import (A_EndLoop, A_Jmp, A_JmpIfRandom1of2, A_Pause, A_ReturnQueue, A_SetSpriteSequence, A_StartLoopNTimes, A_VisibilityOn)
from randomizer.logic.progression.prizelocations.access import (can_damage_enemies_with_spells, can_access_valley, can_do_valley_pipes, not_earlygame, is_early_midgame, is_late_midgame, is_lategame, expect_good_movement, expect_halfway_decent_movement, almost_earlygame, is_midgame, expect_ok_movement, lategame)
from randomizer.types.logic import (Inventory)
from randomizer.types.prize import (Prize)
from randomizer.types.prizelocation import (BossFightLocation, BossFightLocationNPC, ShuffleLocationSelector, WorldAreaEnum)
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.area_objects import (NPC_1, NPC_2)
from smrpgpatchbuilder.datatypes.overworld_scripts.event_scripts.classes import (EventScript, UsableEventScriptCommand)
if TYPE_CHECKING:
    from randomizer.types.gameworld import (GameWorld)


def render_bean_valley_planter_boss(world: GameWorld, prize: BossFightPrize) -> None:
    """Apply NPC position changes for Bean Valley Planter boss fight."""

    complete_sprite = world.get_sprite(prize.smallest_npc().base.sprite_id)
    seqs = complete_sprite.animation.properties.sequences
    if len(seqs) > 0 and len(seqs[0].frames) >= 3:
        mold_0 = seqs[0].frames[0].mold_id
        mold_1 = seqs[0].frames[1].mold_id
        mold_2 = seqs[0].frames[2].mold_id

        world.action_scripts.scripts[A0845_ACTIVATE_PIRANHA_PLANT_IN_PIPE] = (
            ActionScript(
                [
                    A_VisibilityOn(),
                    A_Pause(32),
                    A_JmpIfRandom1of2(["ACTION_845_pause_6"]),
                    A_SetSpriteSequence(
                        index=mold_0, is_mold=True, is_sequence=True, looping=True
                    ),
                    A_Jmp(["ACTION_845_pause_8"]),
                    A_Pause(1, identifier="ACTION_845_pause_6"),
                    A_SetSpriteSequence(
                        index=mold_0,
                        is_mold=True,
                        is_sequence=True,
                        looping=True,
                        mirror_sprite=True,
                    ),
                    A_Pause(48, identifier="ACTION_845_pause_8"),
                    A_JmpIfRandom1of2(
                        ["ACTION_845_start_loop_n_times_23"],
                        identifier="ACTION_845_jmp_if_random_above_128_9",
                    ),
                    A_StartLoopNTimes(2),
                    A_SetSpriteSequence(
                        index=mold_0, is_mold=True, is_sequence=True, looping=True
                    ),
                    A_Pause(2),
                    A_SetSpriteSequence(
                        index=mold_1, is_mold=True, is_sequence=True, looping=True
                    ),
                    A_Pause(4),
                    A_SetSpriteSequence(
                        index=mold_2, is_mold=True, is_sequence=True, looping=True
                    ),
                    A_Pause(8),
                    A_SetSpriteSequence(
                        index=mold_1, is_mold=True, is_sequence=True, looping=True
                    ),
                    A_Pause(2),
                    A_SetSpriteSequence(
                        index=mold_0, is_mold=True, is_sequence=True, looping=True
                    ),
                    A_Pause(4),
                    A_EndLoop(),
                    A_Jmp(["ACTION_845_jmp_if_random_above_128_9"]),
                    A_StartLoopNTimes(2, identifier="ACTION_845_start_loop_n_times_23"),
                    A_SetSpriteSequence(
                        index=mold_0,
                        is_mold=True,
                        is_sequence=True,
                        looping=True,
                        mirror_sprite=True,
                    ),
                    A_Pause(2),
                    A_SetSpriteSequence(
                        index=mold_1,
                        is_mold=True,
                        is_sequence=True,
                        looping=True,
                        mirror_sprite=True,
                    ),
                    A_Pause(4),
                    A_SetSpriteSequence(
                        index=mold_2,
                        is_mold=True,
                        is_sequence=True,
                        looping=True,
                        mirror_sprite=True,
                    ),
                    A_Pause(8),
                    A_SetSpriteSequence(
                        index=mold_1,
                        is_mold=True,
                        is_sequence=True,
                        looping=True,
                        mirror_sprite=True,
                    ),
                    A_Pause(2),
                    A_SetSpriteSequence(
                        index=mold_0,
                        is_mold=True,
                        is_sequence=True,
                        looping=True,
                        mirror_sprite=True,
                    ),
                    A_Pause(4),
                    A_EndLoop(),
                    A_Jmp(["ACTION_845_jmp_if_random_above_128_9"]),
                ]
            )
        )
    else:
        world.action_scripts.scripts[A0845_ACTIVATE_PIRANHA_PLANT_IN_PIPE] = (
            ActionScript([A_VisibilityOn(), A_ReturnQueue()])
        )


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
        return not_earlygame(world, inventory) and can_access_valley(world, inventory)

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
