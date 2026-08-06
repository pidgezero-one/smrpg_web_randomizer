from __future__ import annotations
from typing import TYPE_CHECKING
from smrpgpatchbuilder.datatypes.overworld_scripts.event_scripts.commands import *
from randomizer.data.variables.room_names import *
from randomizer.data.variables.event_script_names import *
from randomizer.data.variables.action_script_names import *
from randomizer.data.variables.pack_names import *
from randomizer.logic.progression.prizes import *
from randomizer.types.flags import *
from randomizer.utils.npcs import (is_swse_only)
from randomizer.utils.event_script_snippets.create_peck_subroutine import (gen_peck_left_subroutine, gen_peck_middle_subroutine, gen_start_battle)
from randomizer.utils.event_script_snippets.es_castle_statue_room_bonk import (script as bonk)
from randomizer.utils.event_script_snippets.es_castle_statue_room_bonk_mario import (script as bonk_mario)
from smrpgpatchbuilder.datatypes.overworld_scripts.action_scripts.commands import (A_FixedFCoordOn, A_TransferXYZFPixels, A_WalkNortheastPixels)
from smrpgpatchbuilder.datatypes.overworld_scripts.action_scripts.commands.commands import (A_Pause, A_SetSpriteSequence)
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments import (EAST)
from typing import (cast)
from randomizer.logic.progression.prizelocations.access import (can_access_nimbus_castle, can_damage_enemies_with_spells, not_earlygame)
from randomizer.types.logic import (Inventory)
from randomizer.types.prize import (Prize)
from randomizer.types.prizelocation import (BossFightLocation, BossFightLocationNPC, ShuffleLocationSelector, WorldAreaEnum)
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.area_objects import (NPC_0, NPC_1, NPC_3)
from smrpgpatchbuilder.datatypes.overworld_scripts.event_scripts.classes import (UsableEventScriptCommand)
if TYPE_CHECKING:
    from randomizer.types.gameworld import (GameWorld)


def render_statue_room_boss(
    world: GameWorld,
    prize: BossFightPrize,
    keep_minigame_sprites: bool,
    chosen_npc_model: type[BossNPC] | None = None,
) -> None:
    """Apply animation changes for Statue Room boss fight."""
    if isinstance(prize, DodoBossFight):
        world.event_scripts.delete_subscript_command_by_identifier(
            "dodo_left_foot_backward_subroutine", "dodo_no_fixed_back_coord_1"
        )
        world.event_scripts.delete_subscript_command_by_identifier(
            "dodo_left_foot_backward_subroutine", "dodo_no_fixed_back_coord_2"
        )
        world.event_scripts.delete_subscript_command_by_identifier(
            "dodo_left_foot_backward_subroutine", "dodo_no_fixed_back_coord_5"
        )
        world.event_scripts.delete_subscript_command_by_identifier(
            "dodo_right_foot_backward_subroutine", "dodo_no_fixed_back_coord_3"
        )
        world.event_scripts.delete_subscript_command_by_identifier(
            "dodo_right_foot_backward_subroutine", "dodo_no_fixed_back_coord_4"
        )
        world.event_scripts.delete_subscript_command_by_identifier(
            "dodo_right_foot_backward_subroutine", "dodo_no_fixed_back_coord_6"
        )
        return
    # wedding ending
    world.event_scripts.delete_subscript_command_by_identifier(
        "wedding_ending_aq", "wedding_ending_shift"
    )
    if keep_minigame_sprites:
        return

    # Prefer the model the placement layer cached; fall back to a generous
    # 6144-cap selection so callers that haven't migrated still work.
    if chosen_npc_model is not None:
        mo = chosen_npc_model
    else:
        mo = prize.get_npc_for_slot(world, 6144)
    m = mo()

    spr = world.sprites.sprites[m.base.sprite_id]
    assert spr is not None
    has_walking_sequence = True
    has_back_walking_sequence = True

    swse_only = is_swse_only(spr) or m.base.directions == VramStore.DIR2_SWSE

    south_mold_map = {}
    walking_molds = []
    for frame in spr.animation.properties.sequences[0].frames:
        if south_mold_map.get(frame.mold_id) is None:
            south_mold_map[frame.mold_id] = 0
        south_mold_map[frame.mold_id] += 1
    for mold_id, count in south_mold_map.items():
        if count == 1:
            walking_molds.append(mold_id)
    if len(walking_molds) < 2:
        has_walking_sequence = False
        walking_molds = []
    else:
        walking_molds = walking_molds[-2:]

    north_mold_map = {}
    back_walking_molds = []
    north_idle_mold = 0
    if not swse_only:
        for frame in spr.animation.properties.sequences[1].frames:
            if north_idle_mold == 0:
                north_idle_mold = frame.mold_id
            if north_mold_map.get(frame.mold_id) is None:
                north_mold_map[frame.mold_id] = 0
            north_mold_map[frame.mold_id] += 1
        for mold_id, count in north_mold_map.items():
            if count == 1:
                back_walking_molds.append(mold_id)
    if len(back_walking_molds) == 0:
        has_back_walking_sequence = False
        back_walking_molds = []
    elif len(back_walking_molds) < 2:
        back_walking_molds = [back_walking_molds[0], back_walking_molds[0]]
    else:
        back_walking_molds = back_walking_molds[-2:]

    if m.animations.statue_peck is None:
        world.event_scripts.get_script_by_id(
            E0936_PECK_SUBROUTINE_LEFT_STATUE
        ).set_contents(bonk.contents)
        world.event_scripts.get_script_by_id(
            E0937_PECK_SUBROUTINE_MIDDLE_STATUE
        ).set_contents(bonk_mario.contents)
        start_battle_subscript: list = [A_FixedFCoordOn()]
        for i in range(4):
            if has_walking_sequence:
                start_battle_subscript.append(
                    A_SetSpriteSequence(
                        index=walking_molds[i % 2],
                        is_mold=True,
                        looping=False,
                        mirror_sprite=False,
                    )
                )
            start_battle_subscript.append(A_WalkNortheastPixels(3))
            start_battle_subscript.append(A_Pause(40))
        cast(
            ActionQueueSync,
            world.event_scripts.get_command_by_identifier("dodo_starts_battle"),
        ).set_subscript(start_battle_subscript)
        world.event_scripts.delete_subscript_command_by_identifier(
            "final_statue_peck_aq", "dodo_fakeout_1"
        )
        world.event_scripts.delete_subscript_command_by_identifier(
            "final_statue_peck_aq", "dodo_fakeout_2"
        )
    else:
        world.event_scripts.get_script_by_id(
            E0936_PECK_SUBROUTINE_LEFT_STATUE
        ).set_contents(gen_peck_left_subroutine(m.animations.statue_peck).contents)
        world.event_scripts.get_script_by_id(
            E0937_PECK_SUBROUTINE_MIDDLE_STATUE
        ).set_contents(gen_peck_middle_subroutine(m.animations.statue_peck).contents)
        cast(
            ActionQueueSync,
            world.event_scripts.get_command_by_identifier("dodo_starts_battle"),
        ).set_subscript(
            gen_start_battle(
                world.get_sprite(m.base.sprite_id), m.animations.statue_peck
            )
        )
        benchmark = 16 + 9 + 8
        shortened_animation = m.animations.statue_peck.contact_frame - 3 # pyright: ignore
        pause_1 = benchmark - shortened_animation
        pause_3 = min(1, shortened_animation // 2)
        pause_2 = min(shortened_animation - pause_3, 1)
        
        world.event_scripts.get_subscript_command_by_identifier(
            "final_statue_peck_aq",
            "dodo_fakeout_pause_1",
            A_Pause,
        ).set_length(pause_1)
        world.event_scripts.get_subscript_command_by_identifier(
            "final_statue_peck_aq",
            "dodo_fakeout_pause_2",
            A_Pause,
        ).set_length(pause_2)
        world.event_scripts.get_subscript_command_by_identifier(
            "final_statue_peck_aq",
            "dodo_fakeout_pause_3",
            A_Pause,
        ).set_length(pause_3)
        world.event_scripts.get_subscript_command_by_identifier(
            "final_statue_peck_aq", "dodo_fakeout_1",
            A_SetSpriteSequence,
        ).set_index(m.animations.statue_peck.sequence_id)
        world.event_scripts.get_subscript_command_by_identifier(
            "final_statue_peck_aq", "dodo_fakeout_2",
            A_SetSpriteSequence,
        ).set_index(north_idle_mold)
        world.event_scripts.get_subscript_command_by_identifier(
            "final_statue_peck_aq", "dodo_fakeout_2",
            A_SetSpriteSequence,
        ).set_mirror_sprite(False)

    if m.animations.look_at_ceiling_mold_id is not None:
        world.event_scripts.get_subscript_command_by_identifier(
            "statue_keeper_introduced_aq",
            "statue_keeper_introduced_1",
            A_SetSpriteSequence,
        ).set_index(m.animations.look_at_ceiling_mold_id)
    else:
        world.event_scripts.delete_subscript_command_by_identifier(
            "statue_keeper_introduced_aq", "statue_keeper_introduced_1"
        )
    if m.animations.statue_intro is not None:
        world.event_scripts.get_subscript_command_by_identifier(
            "statue_keeper_introduced_aq", "statue_keeper_introduced_2",
            A_SetSpriteSequence,
        ).set_index(m.animations.statue_intro.sequence_id)
    else:  
        world.event_scripts.delete_subscript_command_by_identifier(
            "statue_keeper_introduced_aq", "statue_keeper_introduced_2"
        )

      

    if m.animations.statue_flustered is not None:
        world.event_scripts.get_subscript_command_by_identifier(
            "statue_keeper_flustered_aq",
            "statue_keeper_flustered_1",
            A_SetSpriteSequence,
        ).set_index(m.animations.statue_flustered.sequence_id)
        world.event_scripts.get_subscript_command_by_identifier(
            "statue_keeper_flustered_aq",
            "statue_keeper_flustered_1_pause",
            A_Pause,
        ).set_length(max(45, m.animations.statue_flustered.total_duration + 12))
    else:
        world.event_scripts.delete_subscript_command_by_identifier(
            "statue_keeper_flustered_aq", "statue_keeper_flustered_1"
        )

    dodo_replacement_faces_wrong_direction_2 = world.event_scripts.get_subscript_command_by_identifier(
        "final_statue_peck_aq",
        "dodo_circle_around",
        A_SetSpriteSequence,
    )
    dodo_replacement_faces_wrong_direction_2.set_mirror_sprite(False)
    dodo_replacement_faces_wrong_direction_3 = world.event_scripts.get_subscript_command_by_identifier(
        "dodo_circle_around_aq",
        "dodo_circle_around_2",
        A_SetSpriteSequence,
    )
    dodo_replacement_faces_wrong_direction_3.set_mirror_sprite(False)
    dodo_replacement_faces_wrong_direction_4 = world.event_scripts.get_subscript_command_by_identifier(
        "final_statue_peck_aq",
        "dodo_circle_around_3",
        A_SetSpriteSequence,
    )
    dodo_replacement_faces_wrong_direction_4.set_mirror_sprite(False)
    if has_back_walking_sequence:
        dodo_replacement_faces_wrong_direction = (
            world.event_scripts.get_subscript_command_by_identifier(
                "dodo_hallway_mirror_sprite_if_not_vanilla_container",
                "dodo_hallway_mirror_sprite_if_not_vanilla",
                A_SetSpriteSequence,
            )
        )
        dodo_replacement_faces_wrong_direction.set_mirror_sprite(True)
        world.event_scripts.replace_subscript_command_by_identifier(
            "dodo_left_foot_backward_subroutine",
            "dodo_no_fixed_back_coord_face_nw_1",
            A_SetSpriteSequence(index=back_walking_molds[0], is_mold=True, looping=False),
        )
        world.event_scripts.replace_subscript_command_by_identifier(
            "dodo_right_foot_backward_subroutine",
            "dodo_no_fixed_back_coord_face_nw_2",
            A_SetSpriteSequence(index=back_walking_molds[0], is_mold=True, looping=False),
        )
        
    else:
        dodo_hallway_action_script = world.event_scripts.get_command_by_identifier(
            "dodo_hallway_mirror_sprite_if_not_vanilla_container", ActionQueueAsync
        )
        dodo_hallway_action_script.set_subscript(
            [
                A_TransferXYZFPixels(x=252, y=252, z=0, direction=EAST),
                A_FixedFCoordOn(),
                A_SetSpriteSequence(index=0, is_sequence=True, looping=True),
            ]
        )
        dodo_replacement_faces_wrong_direction_2.set_index(0)
        dodo_replacement_faces_wrong_direction_3.set_index(0)
        dodo_replacement_faces_wrong_direction_4.set_index(0)
        world.event_scripts.replace_subscript_command_by_identifier(
            "dodo_left_foot_backward_subroutine",
            "dodo_no_fixed_back_coord_face_nw_1",
            A_SetSpriteSequence(index=0, is_mold=True, looping=False),
        )
        world.event_scripts.replace_subscript_command_by_identifier(
            "dodo_right_foot_backward_subroutine",
            "dodo_no_fixed_back_coord_face_nw_2",
            A_SetSpriteSequence(index=0, is_mold=True, looping=False),
        )

    # walking from statue to statue
    for aq, id in [("dodo_left_foot_forward_subroutine", "dodo_extra_sprite_1")]:
        if has_walking_sequence:
            world.event_scripts.replace_subscript_command_by_identifier(
                aq,
                id,
                A_SetSpriteSequence(
                    index=walking_molds[0],
                    is_sequence=True,
                    looping=False,
                    mirror_sprite=True,
                    is_mold=True,
                ),
            )
        else:
            world.event_scripts.delete_subscript_command_by_identifier(aq, id)

    for aq, id in [("dodo_right_foot_forward_subroutine", "dodo_extra_sprite_2")]:
        if has_walking_sequence:
            world.event_scripts.replace_subscript_command_by_identifier(
                aq,
                id,
                A_SetSpriteSequence(
                    index=walking_molds[1],
                    is_sequence=True,
                    looping=False,
                    mirror_sprite=True,
                    is_mold=True,
                ),
            )
        else:
            world.event_scripts.delete_subscript_command_by_identifier(aq, id)

    for aq, id in [("dodo_left_foot_backward_subroutine", "dodo_left_forward")]:
        if has_back_walking_sequence:
            world.event_scripts.replace_subscript_command_by_identifier(
                aq, id, A_SetSpriteSequence(index=back_walking_molds[0], is_mold=True, looping=True)
            )
        else:
            world.event_scripts.delete_subscript_command_by_identifier(aq, id)

    for aq, id in [("dodo_right_foot_backward_subroutine", "dodo_right_forward")]:
        if has_back_walking_sequence:
            world.event_scripts.replace_subscript_command_by_identifier(
                aq, id, A_SetSpriteSequence(index=back_walking_molds[1], is_mold=True, looping=True)
            )
        else:
            world.event_scripts.delete_subscript_command_by_identifier(aq, id)

    # main 11-step NW walk - base script sets sequence 1 mirrored for Dodo;
    # for non-Dodo shuffles, use sequence 1 un-mirrored when back-walking exists,
    # otherwise drop the command.
    if has_back_walking_sequence:
        world.event_scripts.get_subscript_command_by_identifier(
            "dodo_main_nw_walk_aq", "dodo_main_nw_walk", A_SetSpriteSequence
        ).set_mirror_sprite(False)
    else:
        world.event_scripts.delete_subscript_command_by_identifier(
            "dodo_main_nw_walk_aq", "dodo_main_nw_walk"
        )

    # head-shake
    for aq, id in [
        ("dodo_shake_head_aq", "dodo_shake_head_1"),
        ("dodo_shake_head_aq", "dodo_shake_head_2"),
    ]:
        if m.animations.look_at_camera is None:
            world.event_scripts.replace_subscript_command_by_identifier(
                aq,
                id,
                A_SetSpriteSequence(index=0, is_mold=True, mirror_sprite=True),
            )
        else:
            world.event_scripts.get_subscript_command_by_identifier(
                aq,
                id, A_SetSpriteSequence
            ).set_index(m.animations.look_at_camera.sequence_id)
            
    world.event_scripts.delete_subscript_command_by_identifier(
        "dodo_finished_aq", "dodo_finished_1"
    )
    world.event_scripts.delete_subscript_command_by_identifier(
        "dodo_finished_aq_2", "dodo_finished_2"
    )
    world.event_scripts.delete_subscript_command_by_identifier(
        "dodo_finished_aq_3", "dodo_finished_3"
    )
    world.event_scripts.delete_subscript_command_by_identifier(
        "dodo_possibly_unused_aq", "dodo_possibly_unused"
    )


class StatueRoomBossFight(BossFightLocation):
    _bias = True
    _originally_held = DodoBossFight
    _override_id = 520
    _default_battlefield = BF22_NIMBUS_CASTLE
    _id = ShuffleLocationSelector.NIMBUS_LAND_STATUE_BOSS_FIGHT
    _world_area = WorldAreaEnum.NIMBUS_LAND
    _pack_id = PACK208_NIMBUS_CASTLE_FIRST_BOSS
    _post_unlocks_event_id = E1230_STATUE_BOSS_UNLOCKS
    _rooms = [
        R110_NIMBUS_CASTLE_AREA_18_DODOS_STATUEPOLISHING_ROOM,
        R112_NIMBUS_CASTLE_AREA_17_RIGHT_OF_4WAY_PATH_SAVE_POINT,
    ]
    _npc_slots = [
        BossFightLocationNPC(
            R112_NIMBUS_CASTLE_AREA_17_RIGHT_OF_4WAY_PATH_SAVE_POINT,
            NPC_1,
            sequence_setter_event_id=E0818_NIMBUS_CASTLE_STATUE_POLISHER_BOSS_ROOM_SHUFFLED_NPC_ANIMATION_LOADER,
        ),
        BossFightLocationNPC(
            R506_ENDING_CREDITS_MARRYMORE_CHAPEL_BOOSTER_WEDDING_VALENTINA,
            NPC_0,
            sequence_setter_event_id=E0795_ENDING_CREDITS_CHAPEL_SHUFFLED_NPC_ANIMATION_LOADER,
        ),
        BossFightLocationNPC(
            R110_NIMBUS_CASTLE_AREA_18_DODOS_STATUEPOLISHING_ROOM,
            NPC_3,
            sequence_setter_event_id=E0795_ENDING_CREDITS_CHAPEL_SHUFFLED_NPC_ANIMATION_LOADER,
            skip_swap_if_flag=KeepMinigameSpritesIntact,
        ),
        BossFightLocationNPC(
            R437_NIMBUS_CASTLE_PATH_AFTER_THRONE_ROOM_3RD,
            NPC_0,
            sequence_setter_event_id=E0795_ENDING_CREDITS_CHAPEL_SHUFFLED_NPC_ANIMATION_LOADER,
        ),
    ]
    _dialogs_expecting_replacement = [DI2180_CHAPEL_NPC]

    def can_accept(self, prize: Prize, inventory: Inventory, world: GameWorld) -> bool:
        return super().can_accept(prize, inventory, world) and (
            can_damage_enemies_with_spells(world, inventory)
            or not isinstance(prize, MokuraBossFight)
        )

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_nimbus_castle(world, inventory) and not_earlygame(
            world, inventory
        )

    def render(self, world: GameWorld) -> tuple[
        list[list[UsableEventScriptCommand]],
        list[UsableEventScriptCommand],
        list[tuple[int, int, int]],
    ]:
        op = super().render(world)
        assert isinstance(self.prize, BossFightPrize)

        assert self._npc_slots is not None
        statue_slot = next(
            (
                s
                for s in self._npc_slots
                if s.room_id == R110_NIMBUS_CASTLE_AREA_18_DODOS_STATUEPOLISHING_ROOM
            ),
            None,
        )
        chosen = (
            self.resolve_npc_model_for_slot(world, statue_slot)
            if statue_slot is not None
            else None
        )
        render_statue_room_boss(
            world,
            self.prize,
            world.settings.isflag_enabled(KeepMinigameSpritesIntact),
            chosen_npc_model=chosen,
        )
        return op


__all__ = ["StatueRoomBossFight"]
