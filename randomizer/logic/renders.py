"""Business logic for custom prize location render methods.

This module contains the extracted business logic from custom render methods
in prizelocations.py, organized by location/area.
"""

from __future__ import annotations

import random
from ast import Return
from typing import TYPE_CHECKING, cast

from smrpgpatchbuilder.datatypes.levels.classes import VramStore
from smrpgpatchbuilder.datatypes.overworld_scripts.action_scripts.commands import (
    A_FixedFCoordOn,
    A_TransferXYZFPixels,
    A_WalkNortheastPixels,
)
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments import EAST

from randomizer.progression.prizes import (
    BowserRecruitmentPrize,
    ClerkBossFight,
    DirectorBossFight,
    DodoBossFight,
    GenoRecruitmentPrize,
    MallowRecruitmentPrize,
    ManagerBossFight,
    MarioRecruitmentPrize,
    ToadstoolRecruitmentPrize,
)
from randomizer.utils.tower_access_scripts import (
    A_EndLoop,
    A_JmpIfRandom1of2,
    A_VisibilityOn,
)
from smrpgpatchbuilder.datatypes.overworld_scripts.action_scripts.classes import (
    ActionScript,
)
from smrpgpatchbuilder.datatypes.overworld_scripts.action_scripts.commands.commands import (
    A_FaceNortheast,
    A_FaceNorthwest,
    A_FaceSoutheast,
    A_FaceSouthwest,
    A_Jmp,
    A_Pause,
    A_ResetProperties,
    A_ReturnQueue,
    A_SetBit,
    A_SetSequenceSpeed,
    A_SetSpriteSequence,
    A_ShiftXYPixels,
    A_ShiftZUpPixels,
    A_ShiftZUpSteps,
    A_ShiftZDownPixels,
    A_StartLoopNTimes,
    A_WalkNorthPixels,
    A_WalkSouthPixels,
)
from smrpgpatchbuilder.datatypes.overworld_scripts.action_scripts.arguments.sequence_speeds import (
    NORMAL,
)
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.area_objects import *
from smrpgpatchbuilder.datatypes.overworld_scripts.event_scripts.commands.commands import (
    ActionQueueAsync,
    ActionQueueSync,
    PaletteSet,
    PaletteSetMorphs,
    RemoveObjectFromSpecificLevel,
    Pause,
)
from ..data.variables.event_palette_names import (
    EPAL0084_MARIO_ENDING,
    EPAL0085_MALLOW_ENDING,
    EPAL0086_GENO_ENDING,
    EPAL0140_BOWSER_ENDING,
    EPAL0141_TOADSTOOL_ENDING,
    EPAL0163_MARIO_ENDING_DARK,
    EPAL0164_TOADSTOOL_ENDING_DARK,
    EPAL0165_BOWSER_ENDING_DARK,
    EPAL0166_MALLOW_ENDING_DARK,
    EPAL0167_GENO_ENDING_DARK,
)

from ..data.variables.action_script_names import (
    A0386_TOWER_SHOOT_BULLET_BILLS,
    A0576_CURTAIN_GAME_OPEN_CURTAIN,
    A0577_CURTAIN_GAME_OPEN_CURTAIN,
    A0845_ACTIVATE_PIRANHA_PLANT_IN_PIPE,
    A0962_FACTORY_3RD_BOSS_LEFT_HAMMER,
    A0963_FACTORY_3RD_BOSS_MID_HAMMER,
    A0964_FACTORY_3RD_BOSS_RIGHT_HAMMER,
    A0015_DO_NOTHING
)
from ..data.variables.event_script_names import (
    E0817_BEAN_VALLEY_BOSS_ROOM_SHUFFLED_NPC_ANIMATION_LOADER,
    E0878_TOWER_EXTERIOR_SHUFFLED_NPC_ANIMATION_LOADER,
    E0936_PECK_SUBROUTINE_LEFT_STATUE,
    E0937_PECK_SUBROUTINE_MIDDLE_STATUE,
    E0944_FINAL_BOSS_ANIMATION_SUBROUTINE_1,
    E3792_FACTORY_FINAL_BOSS_ROOM_LOADER,
    E3794_FACTORY_FINAL_BOSS_FIGHT,
)
from ..data.variables.room_names import (
    R088_SMITHYS_FINAL_FORM_DEFEAT_GENOS_REDEMPTION,
    R202_BOOSTER_TOWER_ENTRANCE,
    R254_BEAN_VALLEY_SMILAX_AREA,
    R269_ENDING_CREDITS_NIMBUS_LAND_PRINCE_MALLOW,
    R375_ENDING_CREDITS_STAR_PIECES_SHOOT_THROUGH_THE_SKY,
    R391_VOLCANO_POSTCD_AREA_04,
    R392_VOLCANO_POSTCD_AREA_06,
    R393_VOLCANO_POSTCD_AREA_07_WARP_TO_WORLD_MAP,
    R394_VOLCANO_POSTCD_AREA_05,
    R435_ENDING_CREDITS_BOWSERS_KEEP_BOWSER_TROOPS_REPAIR,
    R470_FACTORY_GROUNDS_AREA_04_GUN_YOLKS_ROOM,
    R496_FACTORY_GROUNDS_FIGHT_WITH_SMITHY_USES_SLEDGE,
    R509_FACTORY_GROUNDS_SMITHYS_PAD,
)
from ..data.variables.variable_names import TEMP_7043_3
from smrpgpatchbuilder.datatypes.levels.classes import NPC as NPCBase
from ..data.rooms.npcs import (
    BOWSER_DOLL_NPC,
    MALLOW_DOLL_NPC,
    MARIO_DOLL_UNAFFECTED_BY_MAIN_CHARACTER_PALETTE_NPC,
    MARIO_WALKING_DOWN_LEFT_NPC,
    TOADSTOOL_DOLL_NPC,
)
from ..types.physical_objects import BossNPC, SpriteAnimation
from ..types.prize import BossFightHenchman, BossFightPrize, CharacterPrize
from ..types.prizelocation import AllyNPCSub, BossFightLocationNPC
from ..utils.npcs import is_swse_only
from ..utils.snippets.es_castle_statue_room_bonk import script as bonk
from ..utils.snippets.es_castle_statue_room_bonk_mario import script as bonk_mario
from ..utils.snippets.es_mimic_rise import get_mimic_rise_dojo
from ..utils.snippets.create_peck_subroutine import (
    gen_peck_left_subroutine,
    gen_peck_middle_subroutine,
    gen_start_battle,
)
from ..utils.snippets.es_non_smithy_final_boss import (
    es_non_smithy_3792,
    es_non_smithy_3794,
)
from ..types.ally import Ally, SpriteAnimationState

if TYPE_CHECKING:
    from ..types.gameworld import GameWorld


def update_ally_animation(
    seq: A_SetSpriteSequence,
    ally: Ally,
    anim: SpriteAnimationState,
    *,
    use_primary: bool = False,
) -> None:
    """Update an ally animation sequence command with the given animation.

    If no animation is provided, replace the command with a face direction
    command instead.
    """
    sprites = ally._sprites_primary if use_primary else ally._sprites_secondary
    data = sprites[anim]
    seq.set_is_mold(data[2])
    seq.set_index(data[1])
    seq.set_sprite_offset(data[0])


# =============================================================================
# Bandits Way
# =============================================================================


def render_bandits_way_boss(world: GameWorld, prize: BossFightPrize) -> None:
    """Apply animation script changes for Bandits Way boss fight."""
    m = prize.smallest_npc()
    bway = m.animations.bandits_way_distracted
    seq_id_replacements = [
        ("bway_aqueue_1", "bway_distracted_1"),
        ("bway_aqueue_2", "bway_distracted_2"),
        ("bway_aqueue_3", "bway_distracted_3"),
        ("bway_aqueue_4", "bway_distracted_4"),
        ("bway_aqueue_5", "bway_distracted_5"),
        ("ending_credits_croco_animation_aq", "ending_credits_croco_animation"),
    ]
    for eid, aid in seq_id_replacements:
        e = world.event_scripts.get_subscript_command_by_identifier(
            eid, aid, A_SetSpriteSequence
        )
        if bway:
            e.set_index(bway.sequence_id)
        else:
            if e.mirror_sprite:
                world.event_scripts.replace_subscript_command_by_identifier(
                    eid, aid, A_FaceSoutheast()
                )
            else:
                world.event_scripts.replace_subscript_command_by_identifier(
                    eid, aid, A_FaceSouthwest()
                )
    recoil = m.animations.recoil
    if recoil:
        a = world.action_scripts.get_command_by_identifier(
            "bandits_way_ascript_recoil", A_SetSpriteSequence
        )
        a.set_index(recoil.sequence_id)


# =============================================================================
# Forest Maze
# =============================================================================


def render_forest_maze_character_empty(world: GameWorld) -> None:
    """Remove character sprite animations when Toad substitute remains in place."""
    deletions = [
        "forest_character_animation_1",
        "forest_character_animation_2",
        "forest_character_animation_3",
        "forest_character_animation_4",
        "forest_character_animation_5",
        "forest_character_animation_6",
        "forest_character_animation_7",
        "forest_character_animation_8",
        "forest_character_animation_9",
        "forest_character_animation_10",
        "forest_character_animation_11",
    ]
    for d in deletions:
        world.action_scripts.delete_command_by_identifier(d)
    e = cast(
        ActionQueueAsync,
        world.event_scripts.get_command_by_identifier("forest_character_animation_14"),
    )
    ss = e.subscript
    cast(
        A_SetSpriteSequence,
        ss.get_command_by_name("forest_character_animation_13")[1],
    ).set_index(6)
    world.event_scripts.delete_subscript_command_by_identifier(
        "forest_character_animation_14", "forest_character_animation_11"
    )
    e.set_subscript(ss.contents)


def render_forest_maze_character(world: GameWorld, prize: CharacterPrize) -> None:
    ally = prize.ally
    # Mario uses protagonist sprite (0) at this location, so needs _sprites_primary
    # which has sprite_offsets relative to sprite 0. Other allies use _sprites_secondary
    # with offsets relative to their non-protagonist sprite IDs.
    use_primary = isinstance(prize, MarioRecruitmentPrize)

    a1 = world.action_scripts.get_command_by_identifier(
        "forest_character_animation_1", A_SetSpriteSequence
    )
    update_ally_animation(
        a1, ally, SpriteAnimationState.SHAKING_HEAD, use_primary=use_primary
    )
    a3 = world.action_scripts.get_command_by_identifier(
        "forest_character_animation_3", A_SetSpriteSequence
    )
    update_ally_animation(
        a3, ally, SpriteAnimationState.SHAKING_HEAD_BACKWARD, use_primary=use_primary
    )
    a5 = world.action_scripts.get_command_by_identifier(
        "forest_character_animation_5", A_SetSpriteSequence
    )
    update_ally_animation(
        a5, ally, SpriteAnimationState.LOOKING_DOWN, use_primary=use_primary
    )
    a7 = world.action_scripts.get_command_by_identifier(
        "forest_character_animation_7", A_SetSpriteSequence
    )
    update_ally_animation(
        a7, ally, SpriteAnimationState.SHAKING_HEAD_BACKWARD, use_primary=use_primary
    )
    a8 = world.action_scripts.get_command_by_identifier(
        "forest_character_animation_8", A_SetSpriteSequence
    )
    update_ally_animation(
        a8, ally, SpriteAnimationState.SLEEPING, use_primary=use_primary
    )
    a9 = world.action_scripts.get_command_by_identifier(
        "forest_character_animation_9", A_SetSpriteSequence
    )
    update_ally_animation(
        a9,
        ally,
        SpriteAnimationState.SHOCKED_BACKWARDS_SEQUENCE,
        use_primary=use_primary,
    )

    e1 = world.event_scripts.get_subscript_command_by_identifier(
        "forest_character_animation_14",
        "forest_character_animation_13",
        A_SetSpriteSequence,
    )
    update_ally_animation(e1, ally, SpriteAnimationState.SOUTH, use_primary=use_primary)
    e2 = world.event_scripts.get_subscript_command_by_identifier(
        "forest_character_animation_14",
        "forest_character_animation_11",
        A_SetSpriteSequence,
    )
    update_ally_animation(
        e2, ally, SpriteAnimationState.DEFEND, use_primary=use_primary
    )


# =============================================================================
# Booster Tower
# =============================================================================


def render_booster_tower_indoor_boss(
    world: GameWorld,
    prize: BossFightPrize,
    npc_slots: list[BossFightLocationNPC],
    is_vanilla: bool,
    henchmen_replaced: bool = True,
) -> None:
    """Apply animation and sprite changes for Booster Tower indoor boss fight."""
    # Adjust the boss sprite behind the Booster Tower door
    entrance = next(
        (s for s in npc_slots if s.room_id == R202_BOOSTER_TOWER_ENTRANCE),
        None,
    )
    assert entrance is not None and entrance.sequence_setter_event_id is not None
    ev = world.event_scripts.get_script_by_id(entrance.sequence_setter_event_id)
    from smrpgpatchbuilder.datatypes.overworld_scripts.action_scripts.classes import (
        UsableActionScriptCommand,
    )

    as_contents: list[UsableActionScriptCommand] = []
    m = prize.smallest_npc()
    if m.tower_entrance_horizontal_shift:
        as_contents.append(A_ShiftXYPixels(m.tower_entrance_horizontal_shift, 0))
    if m.eye_height:
        shift = 17 - m.eye_height
        if shift > 0:
            as_contents.append(A_ShiftZUpPixels(shift))
        elif shift < 0:
            as_contents.append(A_ShiftZDownPixels(-shift))
    if len(as_contents) > 0:
        ev.set_contents(
            [
                ActionQueueAsync(entrance.npc_id, as_contents),
                *ev.contents,
            ]
        )

    # Crown height in the chapel
    ev_crown = world.event_scripts.get_subscript_command_by_identifier(
        "crown_adjust_height_aq", "crown_adjust_height", A_ShiftZUpSteps
    )
    ev_crown.set_steps(m.crown_height)

    # Exit here if vanilla
    if is_vanilla:
        return

    # Chapel laugh animation
    anim = m.animations.chapel_laugh
    seq_id_replacements = [
        ("tower_boss_laughing_aqueue_1", "tower_boss_laughing_seq_1"),
        ("tower_boss_laughing_aqueue_2", "tower_boss_laughing_seq_2"),
        ("tower_boss_laughing_aqueue_3", "tower_boss_laughing_seq_3"),
    ]
    for eid, aid in seq_id_replacements:
        e = world.event_scripts.get_subscript_command_by_identifier(
            eid, aid, A_SetSpriteSequence
        )
        if anim:
            e.set_index(anim.sequence_id)
        elif e.mirror_sprite:
            world.event_scripts.replace_subscript_command_by_identifier(
                eid, aid, A_FaceSoutheast()
            )
        else:
            world.event_scripts.replace_subscript_command_by_identifier(
                eid, aid, A_FaceSouthwest()
            )

    cry = m.animations.tower_crying
    if cry:
        e = world.event_scripts.get_subscript_command_by_identifier(
            "tower_boss_crying_aq_1", "tower_boss_crying_1", A_SetSpriteSequence
        )
        e.set_index(cry.sequence_id)
    else:
        world.event_scripts.delete_subscript_command_by_identifier(
            "tower_boss_crying_aq_1", "tower_boss_crying_1"
        )

    # Delete henchman curtain animations
    deletions = [
        ("tower_henchman_curtain_aqueue_1", "tower_henchman_curtain_1"),
        ("tower_henchman_curtain_aqueue_2", "tower_henchman_curtain_2"),
        ("tower_henchman_curtain_aqueue_3", "tower_henchman_curtain_3"),
        ("tower_henchman_curtain_aqueue_4", "tower_henchman_curtain_4"),
        ("tower_henchman_curtain_aqueue_5", "tower_henchman_curtain_5"),
        ("tower_henchman_curtain_aqueue_6", "tower_henchman_curtain_6"),
        ("tower_henchman_curtain_aqueue_7", "tower_henchman_curtain_7"),
        ("tower_henchman_curtain_aqueue_8", "tower_henchman_curtain_8"),
        ("tower_henchman_curtain_aqueue_9", "tower_henchman_curtain_9"),
        ("tower_henchman_curtain_aqueue_10", "tower_henchman_curtain_10"),
        ("tower_henchman_curtain_aqueue_11", "tower_henchman_curtain_11"),
        ("tower_henchman_curtain_aqueue_12", "tower_henchman_curtain_12"),
        ("tower_henchman_curtain_aqueue_13", "tower_henchman_curtain_13"),
        ("tower_henchman_curtain_aqueue_14", "tower_henchman_curtain_14"),
        ("tower_henchman_curtain_aqueue_15", "tower_henchman_curtain_15"),
        ("tower_henchman_curtain_aqueue_16", "tower_henchman_curtain_16"),
        ("tower_henchman_curtain_aqueue_17", "tower_henchman_curtain_17"),
        ("tower_henchman_curtain_aqueue_18", "tower_henchman_curtain_18"),
        ("tower_henchman_curtain_aqueue_19", "tower_henchman_curtain_19"),
        ("tower_henchman_curtain_aqueue_20", "tower_henchman_curtain_20"),
        ("tower_henchman_curtain_aqueue_21", "tower_henchman_curtain_21"),
        ("tower_henchman_curtain_aqueue_22", "tower_henchman_curtain_22"),
        ("tower_henchman_curtain_aqueue_23", "tower_henchman_curtain_23"),
        ("tower_henchman_curtain_aqueue_24", "tower_henchman_curtain_24"),
        ("tower_henchman_curtain_aqueue_25", "tower_henchman_curtain_25"),
        ("tower_henchman_curtain_aqueue_26", "tower_henchman_curtain_26"),
        ("tower_henchman_curtain_aqueue_27", "tower_henchman_curtain_27"),
        ("tower_henchman_curtain_aqueue_28", "tower_henchman_curtain_28"),
        ("tower_henchman_curtain_aqueue_29", "tower_henchman_curtain_29"),
        ("tower_henchman_curtain_aqueue_30", "tower_henchman_curtain_30"),
        ("tower_henchman_curtain_aqueue_31", "tower_henchman_curtain_31"),
        ("tower_henchman_curtain_aqueue_32", "tower_henchman_curtain_32"),
        ("tower_henchman_curtain_aqueue_33", "tower_henchman_curtain_33"),
        ("tower_henchman_curtain_aqueue_34", "tower_henchman_curtain_34"),
        ("tower_henchman_curtain_aqueue_35", "tower_henchman_curtain_35"),
        ("tower_henchman_curtain_aqueue_36", "tower_henchman_curtain_36"),
        ("tower_henchman_curtain_aqueue_37", "tower_henchman_curtain_37"),
        ("tower_henchman_curtain_aqueue_38", "tower_henchman_curtain_38"),
    ]
    as_deletions = [
        "EVENT_576_open_curtain_async_26",
        "EVENT_576_open_curtain_async_27",
        "EVENT_576_open_curtain_async_28",
        "EVENT_577_open_curtain_async_26",
        "EVENT_577_open_curtain_async_27",
        "EVENT_577_open_curtain_async_28",
        "EVENT_577_open_curtain_async_29",
    ]
    if not is_vanilla and henchmen_replaced:
        for eid, aid in deletions:
            world.event_scripts.delete_subscript_command_by_identifier(eid, aid)
        for aid in as_deletions:
            world.action_scripts.delete_command_by_identifier(aid)
    if not is_vanilla:
        world.event_scripts.delete_subscript_command_by_identifier("tower_henchman_curtain_aqueue_39", "tower_henchman_curtain_39")

    # T-pose replacements
    tpose_replacements = [
        ("chapel_tpose_queue_1", "chapel_tpose_1"),
        ("tower_henchman_curtain_aqueue_39", "tower_henchman_curtain_40"),
    ]
    for eid, aid in tpose_replacements:
        a = world.event_scripts.get_subscript_command_by_identifier(
            eid, aid, A_SetSpriteSequence
        )
        if m.animations.tpose_mold_id is not None:
            a.set_index(m.animations.tpose_mold_id)
        elif a.mirror_sprite:
            world.event_scripts.replace_subscript_command_by_identifier(
                eid, aid, A_FaceNortheast()
            )
        else:
            world.event_scripts.replace_subscript_command_by_identifier(
                eid, aid, A_FaceNorthwest()
            )

    # Stare up replacements
    stare_up_replacements = [
        ("chapel_stare_up_queue_1", "chapel_stare_up_1"),
        ("chapel_stare_up_queue_2", "chapel_stare_up_2"),
        ("chapel_stare_up_queue_3", "chapel_stare_up_3"),
        ("chapel_stare_up_queue_4", "chapel_stare_up_4"),
    ]
    for eid, aid in stare_up_replacements:
        a = world.event_scripts.get_subscript_command_by_identifier(
            eid, aid, A_SetSpriteSequence
        )
        if m.animations.look_at_ceiling_mold_id is not None:
            a.set_index(m.animations.look_at_ceiling_mold_id)
        elif a.mirror_sprite:
            world.event_scripts.replace_subscript_command_by_identifier(
                eid, aid, A_FaceSoutheast()
            )
        else:
            world.event_scripts.replace_subscript_command_by_identifier(
                eid, aid, A_FaceSouthwest()
            )

    # Tower toss animation
    if m.animations.tower_toss is not None:
        tower_toss = m.animations.tower_toss
        from smrpgpatchbuilder.datatypes.overworld_scripts.event_scripts.commands.commands import (
            Pause,
        )
        from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.area_objects import (
            NPC_6,
        )

        pause_length = (
            tower_toss.contact_frame
            if tower_toss.contact_frame is not None
            else tower_toss.total_duration or 0
        )
        cast(
            Pause,
            world.event_scripts.get_command_by_identifier("tower_toss_contact_frame"),
        ).set_length(pause_length + 30)
        world.event_scripts.replace_command_by_identifier(
            "tower_toss_aqueue",
            ActionQueueSync(
                target=NPC_6,
                subscript=[
                    A_FaceSouthwest(),
                    A_Pause(30),
                    A_SetSpriteSequence(index=tower_toss.sequence_id, is_sequence=True),
                ],
                identifier="tower_toss_aqueue",
            ),
        )
    else:
        world.event_scripts.delete_subscript_command_by_identifier(
            "tower_toss_aqueue", "tower_toss"
        )
        

def render_booster_tower_indoor_boss_postgame(
    world: GameWorld,
    prize: BossFightPrize,
) -> None:
    m = prize.smallest_npc()
    anim = m.animations.chapel_laugh
    seq_id_replacements = [
        ("EVENT_704_action_queue_sync_0", "EVENT_704_set_sprite_sequence_0"),
    ]
    for eid, aid in seq_id_replacements:
        e = world.event_scripts.get_subscript_command_by_identifier(
            eid, aid, A_SetSpriteSequence
        )
        if anim:
            e.set_index(anim.sequence_id)
        elif e.mirror_sprite:
            world.event_scripts.replace_subscript_command_by_identifier(
                eid, aid, A_FaceSoutheast()
            )
        else:
            world.event_scripts.replace_subscript_command_by_identifier(
                eid, aid, A_FaceSouthwest()
            )

def render_booster_tower_henchman_scripts(
    world: GameWorld,
    prize: BossFightPrize,
    henchmen_count: int,
) -> None:
    """Apply henchman-related script changes for Booster Tower."""
    # Remove special snifit sprites that other henchmen don't have\
    if henchmen_count >= 3:
        world.action_scripts.replace_script(
            A0576_CURTAIN_GAME_OPEN_CURTAIN,
            ActionScript([A_FaceNorthwest(), A_Pause(12), A_ReturnQueue()]),
        )
        world.action_scripts.replace_script(
            A0577_CURTAIN_GAME_OPEN_CURTAIN,
            ActionScript(
                [
                    A_FaceNorthwest(),
                    A_Pause(17),
                    A_ResetProperties(),
                    A_FaceNorthwest(),
                    A_ReturnQueue(),
                ]
            ),
        )

        # Hill sprite replacements
        hill_ids = [
            "hill_sprite_set_1",
            "hill_sprite_set_2",
            "hill_sprite_set_3",
            "hill_sprite_set_4",
            "hill_sprite_set_5",
        ]
        for h in hill_ids:
            world.action_scripts.replace_command_by_identifier(h, A_FaceNorthwest())

        # Third henchman tower bullet animation
        # The third character slot may be filled by a character henchman or
        # a mook henchman fallback — check both sources.
        third_henchman: BossFightHenchman | None = None
        if prize.character_henchmen is not None and len(prize.character_henchmen) >= 3:
            third_henchman = prize.character_henchmen[2]
        elif prize.mook_henchmen is not None and len(prize.mook_henchmen) > 0:
            third_henchman = prize.mook_henchmen[0]

        if third_henchman is not None:
            third_henchman_animations = third_henchman.model()._animations
            b = third_henchman_animations.tower_bullet
            if b is not None and b.total_duration is not None:
                pelim_pause = 0
                contact_frame = b.contact_frame
                if contact_frame is None:
                    contact_frame = b.total_duration // 2
                if contact_frame < 56:
                    pelim_pause = 56 - contact_frame
                interval_after_shot = min(40, b.total_duration - contact_frame)
                final_interval = max(0, 96 - b.total_duration - pelim_pause)

                world.action_scripts.replace_script(
                    A0386_TOWER_SHOOT_BULLET_BILLS,
                    script=ActionScript(
                        [
                            A_FaceSoutheast(),
                            A_Pause(18),
                            A_FaceSouthwest(),
                            A_Pause(18),
                            *(
                                [
                                    A_Pause(
                                        pelim_pause,
                                        identifier="ACTION_386_set_sprite_sequence_4",
                                    ),
                                    A_SetSpriteSequence(
                                        index=b.sequence_id,
                                        is_sequence=True,
                                        looping=False,
                                    ),
                                ]
                                if pelim_pause > 0
                                else [
                                    A_SetSpriteSequence(
                                        index=b.sequence_id,
                                        is_sequence=True,
                                        looping=False,
                                        identifier="ACTION_386_set_sprite_sequence_4",
                                    )
                                ]
                            ),
                            A_Pause(contact_frame),
                            A_SetBit(TEMP_7043_3),
                            *(
                                [A_Pause(interval_after_shot)]
                                if interval_after_shot > 0
                                else []
                            ),
                            A_SetSpriteSequence(
                                index=0,
                                is_sequence=True,
                                looping=True,
                            ),
                            A_Pause(final_interval),
                            A_Jmp(["ACTION_386_set_sprite_sequence_4"]),
                        ]
                    ),
                )
            else:
                pelim_pause = 0
                if b is not None and b.total_duration is not None:
                    pelim_pause = 56 - (b.total_duration / 2)

                world.action_scripts.replace_script(
                    A0386_TOWER_SHOOT_BULLET_BILLS,
                    script=ActionScript(
                        [
                            A_FaceSoutheast(),
                            A_Pause(18),
                            A_FaceSouthwest(),
                            A_Pause(18),
                            A_Pause(
                                56,
                                identifier="ACTION_386_set_sprite_sequence_4",
                            ),
                            A_SetBit(TEMP_7043_3),
                            A_Pause(40),
                            A_Jmp(["ACTION_386_set_sprite_sequence_4"]),
                        ]
                    ),
                )


# =============================================================================
# Marrymore
# =============================================================================


def render_marrymore_boss_henchmen(
    world: GameWorld,
    henchmen: list[BossFightHenchman],
) -> None:
    """Apply henchman animation changes for Marrymore boss fight."""
    if len(henchmen) >= 1:
        first_henchman = henchmen[0]
        henchman_animations = first_henchman.model()._animations
        if henchman_animations.kitchen_prep is not None:
            cmd = world.action_scripts.get_command_by_identifier(
                "kitchen_chef_seq_1", A_SetSpriteSequence
            )
            cmd.set_index(henchman_animations.kitchen_prep.sequence_id)
        else:
            world.action_scripts.delete_command_by_identifier("kitchen_chef_seq_1")

    if len(henchmen) >= 2:
        second_henchman = henchmen[1]
        henchman_animations = second_henchman.model()._animations
        if henchman_animations.kitchen_prep is not None:
            for cmd_id in ["kitchen_chef_seq_2", "kitchen_chef_seq_3"]:
                cmd = world.action_scripts.get_command_by_identifier(
                    cmd_id, A_SetSpriteSequence
                )
                cmd.set_index(henchman_animations.kitchen_prep.sequence_id)
        else:
            world.action_scripts.delete_command_by_identifier("kitchen_chef_seq_2")
            world.action_scripts.delete_command_by_identifier("kitchen_chef_seq_3")


def render_marrymore_character_empty(world: GameWorld) -> None:
    """Remove character sprite animations when Toad substitute remains in chapel."""
    deletions: list[tuple[str, list[str]]] = [
        (
            "chapel_character_queue_1",
            ["chapel_character_animation_1", "chapel_character_animation_2"],
        ),
        ("chapel_character_queue_2", ["chapel_character_animation_3"]),
        ("chapel_character_queue_3", []),
        (
            "chapel_character_queue_4",
            ["chapel_character_animation_4", "chapel_character_animation_5"],
        ),
        ("chapel_character_queue_5", ["chapel_character_animation_6"]),
        ("chapel_character_queue_6", ["chapel_character_animation_7"]),
        (
            "chapel_character_queue_7",
            ["chapel_character_animation_8", "chapel_character_animation_9"],
        ),
        (
            "chapel_character_queue_8",
            ["chapel_character_animation_10", "chapel_character_animation_11"],
        ),
        ("chapel_character_queue_9", ["chapel_character_animation_12"]),
        (
            "EVENT_3499_action_queue_42",
            ["chapel_character_animation_13", "chapel_character_animation_14"],
        ),
        (
            "EVENT_3499_action_queue_45",
            ["chapel_character_animation_15", "chapel_character_animation_16"],
        ),
        ("chapel_character_queue_10", ["chapel_character_animation_17"]),
        (
            "chapel_character_queue_11",
            ["chapel_character_animation_18", "chapel_character_animation_19"],
        ),
        (
            "chapel_character_queue_12",
            ["chapel_character_animation_20", "chapel_character_animation_21"],
        ),
    ]
    for queue, actions in deletions:
        if len(actions) == 0:
            world.event_scripts.delete_command_by_identifier(queue)
        else:
            e = cast(
                ActionQueueAsync,
                world.event_scripts.get_command_by_identifier(queue),
            )
            ss = e.subscript
            for action in actions:
                idx = ss.get_index_of_identifier(action)
                ss.delete_at_index(idx)
            e.set_subscript(ss.contents)


def render_marrymore_character(world: GameWorld, prize: CharacterPrize) -> None:
    ally = prize.ally
    # Mario uses protagonist sprite (0) at this location, so needs _sprites_primary
    # which has sprite_offsets relative to sprite 0. Other allies use _sprites_secondary
    # with offsets relative to their non-protagonist sprite IDs.
    use_primary = isinstance(prize, MarioRecruitmentPrize)

    a1 = world.event_scripts.get_subscript_command_by_identifier(
        "chapel_character_queue_1", "chapel_character_animation_1", A_SetSpriteSequence
    )
    update_ally_animation(
        a1, ally, SpriteAnimationState.SHOCKED_LOOP, use_primary=use_primary
    )
    a2 = world.event_scripts.get_subscript_command_by_identifier(
        "chapel_character_queue_1", "chapel_character_animation_2", A_SetSpriteSequence
    )
    update_ally_animation(
        a2, ally, SpriteAnimationState.FLOORED, use_primary=use_primary
    )
    a3 = world.event_scripts.get_subscript_command_by_identifier(
        "chapel_character_queue_2", "chapel_character_animation_3", A_SetSpriteSequence
    )
    update_ally_animation(a3, ally, SpriteAnimationState.HURT, use_primary=use_primary)
    a4 = world.event_scripts.get_subscript_command_by_identifier(
        "chapel_character_queue_3", "chapel_character_queue_3_", A_SetSpriteSequence
    )
    update_ally_animation(
        a4, ally, SpriteAnimationState.LOOKING_DOWN_STATIC, use_primary=use_primary
    )
    a5 = world.event_scripts.get_subscript_command_by_identifier(
        "chapel_character_queue_4", "chapel_character_animation_4", A_SetSpriteSequence
    )
    update_ally_animation(
        a5, ally, SpriteAnimationState.SHAKING_HEAD, use_primary=use_primary
    )
    a6 = world.event_scripts.get_subscript_command_by_identifier(
        "chapel_character_queue_4", "chapel_character_animation_5", A_SetSpriteSequence
    )
    update_ally_animation(
        a6, ally, SpriteAnimationState.LOOKING_DOWN_STATIC, use_primary=use_primary
    )
    a7 = world.event_scripts.get_subscript_command_by_identifier(
        "chapel_character_queue_5", "chapel_character_animation_6", A_SetSpriteSequence
    )
    update_ally_animation(
        a7, ally, SpriteAnimationState.CRYING, use_primary=use_primary
    )
    a8 = world.event_scripts.get_subscript_command_by_identifier(
        "chapel_character_queue_6", "chapel_character_animation_7", A_SetSpriteSequence
    )
    update_ally_animation(
        a8, ally, SpriteAnimationState.SHOCKED_LOOP, use_primary=use_primary
    )
    a9 = world.event_scripts.get_subscript_command_by_identifier(
        "chapel_character_queue_7", "chapel_character_animation_9", A_SetSpriteSequence
    )
    update_ally_animation(
        a9, ally, SpriteAnimationState.LOOKING_DOWN_STATIC, use_primary=use_primary
    )
    a10 = world.event_scripts.get_subscript_command_by_identifier(
        "chapel_character_queue_7", "chapel_character_animation_8", A_SetSpriteSequence
    )
    update_ally_animation(
        a10, ally, SpriteAnimationState.CRYING, use_primary=use_primary
    )
    a11 = world.event_scripts.get_subscript_command_by_identifier(
        "chapel_character_queue_8", "chapel_character_animation_10", A_SetSpriteSequence
    )
    update_ally_animation(
        a11, ally, SpriteAnimationState.SHOCKED_LOOP, use_primary=use_primary
    )
    a12 = world.event_scripts.get_subscript_command_by_identifier(
        "chapel_character_queue_8", "chapel_character_animation_11", A_SetSpriteSequence
    )
    update_ally_animation(
        a12, ally, SpriteAnimationState.CRYING_BACKWARDS, use_primary=use_primary
    )
    a13 = world.event_scripts.get_subscript_command_by_identifier(
        "chapel_character_queue_9", "chapel_character_animation_12", A_SetSpriteSequence
    )
    update_ally_animation(
        a13, ally, SpriteAnimationState.SHOCKED_LOOP, use_primary=use_primary
    )
    a14 = world.event_scripts.get_subscript_command_by_identifier(
        "EVENT_3499_action_queue_42",
        "chapel_character_animation_13",
        A_SetSpriteSequence,
    )
    update_ally_animation(
        a14, ally, SpriteAnimationState.SHOCKED_LOOP_BACKWARDS, use_primary=use_primary
    )
    a15 = world.event_scripts.get_subscript_command_by_identifier(
        "EVENT_3499_action_queue_42",
        "chapel_character_animation_14",
        A_SetSpriteSequence,
    )
    update_ally_animation(
        a15, ally, SpriteAnimationState.SHOCKED_LOOP_BACKWARDS, use_primary=use_primary
    )
    a16 = world.event_scripts.get_subscript_command_by_identifier(
        "EVENT_3499_action_queue_45",
        "chapel_character_animation_15",
        A_SetSpriteSequence,
    )
    update_ally_animation(
        a16, ally, SpriteAnimationState.SHOCKED_LOOP_BACKWARDS, use_primary=use_primary
    )
    a17 = world.event_scripts.get_subscript_command_by_identifier(
        "EVENT_3499_action_queue_45",
        "chapel_character_animation_16",
        A_SetSpriteSequence,
    )
    update_ally_animation(
        a17, ally, SpriteAnimationState.SHOCKED_LOOP, use_primary=use_primary
    )
    a18 = world.event_scripts.get_subscript_command_by_identifier(
        "chapel_character_queue_10",
        "chapel_character_animation_17",
        A_SetSpriteSequence,
    )
    update_ally_animation(
        a18, ally, SpriteAnimationState.SHOCKED_LOOP_BACKWARDS, use_primary=use_primary
    )
    a19 = world.event_scripts.get_subscript_command_by_identifier(
        "chapel_character_queue_11",
        "chapel_character_animation_18",
        A_SetSpriteSequence,
    )
    update_ally_animation(
        a19, ally, SpriteAnimationState.SHOCKED_LOOP_BACKWARDS, use_primary=use_primary
    )
    a20 = world.event_scripts.get_subscript_command_by_identifier(
        "chapel_character_queue_11",
        "chapel_character_animation_19",
        A_SetSpriteSequence,
    )
    update_ally_animation(
        a20, ally, SpriteAnimationState.SHOCKED_LOOP_BACKWARDS, use_primary=use_primary
    )
    a21 = world.event_scripts.get_subscript_command_by_identifier(
        "chapel_character_queue_12",
        "chapel_character_animation_20",
        A_SetSpriteSequence,
    )
    update_ally_animation(
        a21, ally, SpriteAnimationState.SHOCKED_LOOP_BACKWARDS, use_primary=use_primary
    )
    a22 = world.event_scripts.get_subscript_command_by_identifier(
        "chapel_character_queue_12",
        "chapel_character_animation_21",
        A_SetSpriteSequence,
    )
    update_ally_animation(
        a22, ally, SpriteAnimationState.SHOCKED_LOOP, use_primary=use_primary
    )

# NPC fills for each ending-cutscene render. Each AllyNPCSub here points at an
# NPC in an ending-cutscene room (e.g. R496, R088) that should be replaced with
# the chosen character's overworld model. These are populated independently of
# the recruitment location's own _npc_fills.
_ENDING_CHARACTER_2_NPC_FILLS: list[AllyNPCSub] = [
    # R496/R088/R375 entries removed — those rooms have a Mario NPC at the
    # front and recruits stay at their native slots (no model swap). Only
    # R269 keeps the model-swap for its single Prince Mallow scene.
    AllyNPCSub(R269_ENDING_CREDITS_NIMBUS_LAND_PRINCE_MALLOW, NPC_0),
]

_ENDING_CHARACTER_3_NPC_FILLS: list[AllyNPCSub] = [
    # R496/R088/R375 entries removed — see _ENDING_CHARACTER_2_NPC_FILLS comment.
]

# NPCs that should be replaced with the doll variant matching the chosen
# character in the Forest Maze ending cutscene (render_ending_character_3).
# Geno is intentionally absent from the doll mapping below — render_ending_character_3
# returns early when the prize is GenoRecruitmentPrize, so these substitutions
# are never applied for Geno. Indices reflect the post-Mario-NPC layout
# (R088 NPC_3 → NPC_4, R375 NPC_2 → NPC_3, R496 NPC_22 → NPC_23).
_ENDING_CHARACTER_3_DOLL_FILLS: list[AllyNPCSub] = [
    AllyNPCSub(R496_FACTORY_GROUNDS_FIGHT_WITH_SMITHY_USES_SLEDGE, NPC_23),
    AllyNPCSub(R088_SMITHYS_FINAL_FORM_DEFEAT_GENOS_REDEMPTION, NPC_4),
    AllyNPCSub(R375_ENDING_CREDITS_STAR_PIECES_SHOOT_THROUGH_THE_SKY, NPC_3),
]

_ENDING_CHARACTER_4_NPC_FILLS: list[AllyNPCSub] = [
    # R496/R088/R375 entries removed — see _ENDING_CHARACTER_2_NPC_FILLS comment.
    AllyNPCSub(R435_ENDING_CREDITS_BOWSERS_KEEP_BOWSER_TROOPS_REPAIR, NPC_7),
    AllyNPCSub(R435_ENDING_CREDITS_BOWSERS_KEEP_BOWSER_TROOPS_REPAIR, NPC_8),
]

_ENDING_CHARACTER_5_NPC_FILLS: list[AllyNPCSub] = [
    # R496/R088/R375 entries removed — see _ENDING_CHARACTER_2_NPC_FILLS comment.
]


# =============================================================================
# R496 ending cutscene: role/coord-swap (replaces NPC model swap)
# =============================================================================
# Each character has a permanent NPC slot in R496. The cutscene script targets
# the script's vanilla-role NPC slots (MARRYMORE_CHARACTER=NPC_20,
# MWAY_CHARACTER=NPC_21, FOREST_CHARACTER=NPC_22, MINES_CHARACTER=NPC_24,
# MARIO=protagonist). At apply time we walk script_3885 and retarget each
# role's NPC reference to whichever character's native slot now plays that
# role. Sprite models are NOT swapped (avoiding partition VRAM-overflow
# issues from mismatched sprite sizes).
#
# R496 NPC layout (Mario placed before the recruits so he allocates first
# in the dynamic VRAM region):
#   NPC_19 = Mario  (sprite 0 always)
#   NPC_20 = Peach
#   NPC_21 = Mallow
#   NPC_22 = Geno
#   NPC_23 = Geno doll  (model-swapped per forest character via _ENDING_CHARACTER_3_DOLL_FILLS)
#   NPC_24 = Bowser

R496_NATIVE_SLOT_FOR_PRIZE: dict[type, AreaObject] = {
    MarioRecruitmentPrize:     NPC_19,
    ToadstoolRecruitmentPrize: NPC_20,
    MallowRecruitmentPrize:    NPC_21,
    GenoRecruitmentPrize:      NPC_22,
    BowserRecruitmentPrize:    NPC_24,
}

R496_VANILLA_ROLE_NPCS: dict[str, AreaObject] = {
    "marrymore":    NPC_20,
    "mushroom_way": NPC_21,
    "forest_maze":  NPC_22,
    "inner_mines":  NPC_24,
}

# Identifiers of script commands the retarget walker must NOT touch (they
# reference the ally-buffer-rendered avatar, not the protagonist's NPC slot).
R496_RETARGET_SKIP_IDENTIFIERS: frozenset[str] = frozenset({
    "hide_player_avatar",
    "hide_player_avatar2",
    "hide_player_avatar3",
})


def _retarget_event_script_targets(
    contents,
    target_map: dict,
    *,
    skip_identifiers: frozenset[str] = frozenset(),
) -> None:
    """Recursively walk an event-script command list (and ActionQueue subscripts)
    and replace each command's `target` according to target_map. Commands
    whose `identifier` is in skip_identifiers are left untouched.
    """
    iterable = contents if isinstance(contents, list) else getattr(contents, "contents", [])
    for cmd in iterable:
        ident = getattr(cmd, "identifier", None)
        ident_label = getattr(ident, "label", None) if ident is not None else None
        if ident_label not in skip_identifiers:
            cmd_target = getattr(cmd, "target", None)
            if cmd_target is not None and cmd_target in target_map:
                cmd.set_target(target_map[cmd_target])
        sub = getattr(cmd, "subscript", None)
        if sub is not None:
            _retarget_event_script_targets(
                sub, target_map, skip_identifiers=skip_identifiers
            )


def _make_protagonist_sprite_31_variant(base: NPCBase) -> NPCBase:
    """Return a copy of `base` with sprite_id set to SPR0031_ALT_PROTAGONIST_1.

    Sprite 31 is the post-cosmetics protagonist sprite; the cosmetics layer
    overwrites sprites 31-37 with the protagonist character's full animation
    set, so any NPC slot using sprite 31 has access to the same animations
    as the protagonist. We use this on the protagonist's native slot when
    the protagonist is not Mario, so the recruit-only sprite at that slot
    is replaced with the full protagonist sprite.
    """
    from ..data.variables.sprite_names import SPR0031_ALT_PROTAGONIST_1
    return NPCBase(
        sprite_id=SPR0031_ALT_PROTAGONIST_1,
        shadow_size=base.shadow_size,
        acute_axis=base.acute_axis,
        obtuse_axis=base.obtuse_axis,
        height=base.height,
        y_shift=base.y_shift,
        show_shadow=base.show_shadow,
        directions=base.directions,
        min_vram_size=base.min_vram_size,
        priority_0=base.priority_0,
        priority_1=base.priority_1,
        priority_2=base.priority_2,
        cannot_clone=base.cannot_clone,
        byte2_bit0=base.byte2_bit0,
        byte2_bit1=base.byte2_bit1,
        byte2_bit2=base.byte2_bit2,
        byte2_bit3=base.byte2_bit3,
        byte2_bit4=base.byte2_bit4,
        byte5_bit6=base.byte5_bit6,
        byte5_bit7=base.byte5_bit7,
        byte6_bit2=base.byte6_bit2,
    )


def _apply_r496_role_assignments(
    world: GameWorld,
    *,
    marrymore_prize: CharacterPrize,
    mushroom_way_prize: CharacterPrize,
    forest_maze_prize: CharacterPrize,
    inner_mines_prize: CharacterPrize,
    protagonist_prize: CharacterPrize,
) -> None:
    """For room 496 (the post-final-boss cutscene): keep each character's
    native sprite at its native slot, retarget script_3885 commands so each
    role's vanilla-NPC reference is redirected to whichever character's slot
    plays that role this seed, override sprite_id on the protagonist's slot
    to sprite 31 (when protagonist isn't Mario), and rebuild
    npc_expected_animations from the room's role_expected_animations plus
    extra_sprite_actions for the protagonist slot.
    """
    from ..data.variables.event_script_names import E3885_END_GAME
    from ..types.room import Room as ExtRoom

    room = world.rooms._rooms[R496_FACTORY_GROUNDS_FIGHT_WITH_SMITHY_USES_SLEDGE]
    if not isinstance(room, ExtRoom):
        return

    role_to_slot: dict[str, AreaObject] = {
        "marrymore":    R496_NATIVE_SLOT_FOR_PRIZE[type(marrymore_prize)],
        "mushroom_way": R496_NATIVE_SLOT_FOR_PRIZE[type(mushroom_way_prize)],
        "forest_maze":  R496_NATIVE_SLOT_FOR_PRIZE[type(forest_maze_prize)],
        "inner_mines":  R496_NATIVE_SLOT_FOR_PRIZE[type(inner_mines_prize)],
    }
    protagonist_slot = R496_NATIVE_SLOT_FOR_PRIZE[type(protagonist_prize)]

    target_map: dict = {}
    for role, slot in role_to_slot.items():
        vanilla_npc = R496_VANILLA_ROLE_NPCS[role]
        if int(vanilla_npc) != int(slot):
            target_map[vanilla_npc] = slot
    if int(protagonist_slot) != int(MARIO):
        target_map[MARIO] = protagonist_slot

    if target_map:
        script = world.event_scripts.get_script_by_id(E3885_END_GAME)
        _retarget_event_script_targets(
            script.contents,
            target_map,
            skip_identifiers=R496_RETARGET_SKIP_IDENTIFIERS,
        )

    if not isinstance(protagonist_prize, MarioRecruitmentPrize):
        obj = room.get_npc_by_target_id(protagonist_slot)
        if obj is not None:
            obj._npc = _make_protagonist_sprite_31_variant(obj._npc)

    role_anims = getattr(room, "role_expected_animations", {}) or {}
    rebuilt: dict[int, list] = {}
    for role, anims in role_anims.items():
        slot = role_to_slot.get(role)
        if slot is None:
            continue
        idx = int(slot) - 20  # AreaObject NPC_X = X + 20; convert back to room object index
        rebuilt[idx] = list(anims)
    extra_anims = list(getattr(room, "extra_sprite_actions", []) or [])
    if extra_anims:
        proto_idx = int(protagonist_slot) - 20
        existing = rebuilt.get(proto_idx, [])
        rebuilt[proto_idx] = list(existing) + extra_anims
    room.npc_expected_animations = rebuilt


def _doll_for_prize(prize: CharacterPrize) -> NPCBase | None:
    """Return the doll NPC matching `prize` for the render_ending_character_3
    cutscene, or None if no doll variant exists for this character."""
    if isinstance(prize, MallowRecruitmentPrize):
        return MALLOW_DOLL_NPC
    if isinstance(prize, BowserRecruitmentPrize):
        return BOWSER_DOLL_NPC
    if isinstance(prize, ToadstoolRecruitmentPrize):
        return TOADSTOOL_DOLL_NPC
    if isinstance(prize, MarioRecruitmentPrize):
        return MARIO_DOLL_UNAFFECTED_BY_MAIN_CHARACTER_PALETTE_NPC
    return None


def _apply_ending_character_npc_fills(
    world: GameWorld, prize: CharacterPrize, fills: list[AllyNPCSub]
) -> None:
    """Replace each NPC listed in `fills` with the model corresponding to `prize`.

    Mirrors the AllyNPCSub loop in CharacterRecruitmentLocation.render() so
    that ending-cutscene rooms can be populated with the chosen character
    independently of the recruitment location's own _npc_fills.

    For MarioRecruitmentPrize, MARIO_WALKING_DOWN_LEFT_NPC is used instead of
    `prize.character_model.base` (which would resolve to the SPR0409_MARIO_CLONE
    sprite). The clone sprite uses sprite_offset shifts that crash in many
    cutscene contexts; MARIO_WALKING_DOWN_LEFT_NPC uses the protagonist sprite
    (0) and avoids that problem."""
    if isinstance(prize, MarioRecruitmentPrize):
        model = MARIO_WALKING_DOWN_LEFT_NPC
    else:
        model = prize.character_model.base
    for npc_sub in fills:
        room = world.rooms._rooms[npc_sub.room_id]
        if room is None:
            raise ValueError(
                f"Room ID {npc_sub.room_id} not found while applying ending character NPC fills."
            )
        obj = room.get_npc_by_target_id(npc_sub.npc_id)
        if obj is None:
            raise ValueError(
                f"NPC ID {npc_sub.npc_id} not found in room {npc_sub.room_id} while applying ending character NPC fills."
            )
        obj._npc = model


def _apply_ending_character_3_doll_fills(
    world: GameWorld, prize: CharacterPrize, fills: list[AllyNPCSub]
) -> None:
    """Replace each NPC listed in `fills` with the doll variant matching `prize`."""
    doll = _doll_for_prize(prize)
    if doll is None:
        return
    for npc_sub in fills:
        room = world.rooms._rooms[npc_sub.room_id]
        if room is None:
            raise ValueError(
                f"Room ID {npc_sub.room_id} not found while applying ending character 3 doll fills."
            )
        obj = room.get_npc_by_target_id(npc_sub.npc_id)
        if obj is None:
            raise ValueError(
                f"NPC ID {npc_sub.npc_id} not found in room {npc_sub.room_id} while applying ending character 3 doll fills."
            )
        obj._npc = doll


def render_ending_character_2(
    world: GameWorld,
    prize: CharacterPrize,
    *,
    protagonist_prize: CharacterPrize | None = None,
) -> None:
    if isinstance(prize, MallowRecruitmentPrize):
        return
    _apply_ending_character_npc_fills(world, prize, _ENDING_CHARACTER_2_NPC_FILLS)
    ally = prize.ally
    # use_primary: Mario always uses sprite 0 (_sprites_primary). Non-Mario
    # protagonists use sprite 31 in their R496 slot, which also has full
    # protagonist data → also _sprites_primary. Recruits with their native
    # sprite use _sprites_secondary.
    use_primary = isinstance(prize, MarioRecruitmentPrize) or (
        protagonist_prize is not None and prize is protagonist_prize
    )
    a0 = world.event_scripts.get_subscript_command_by_identifier(
        "ending_prince_aq_1",
        "ending_prince_aq_1_1",
        A_SetSpriteSequence,
    )
    update_ally_animation(
        a0, ally, SpriteAnimationState.PRINCE_NEUTRAL, use_primary=use_primary
    )
    a1 = world.event_scripts.get_subscript_command_by_identifier(
        "ending_prince_aq_2",
        "ending_prince_aq_2_1",
        A_SetSpriteSequence,
    )
    update_ally_animation(
        a1, ally, SpriteAnimationState.PRINCE_DOWN, use_primary=use_primary
    )
    a2 = world.event_scripts.get_subscript_command_by_identifier(
        "ending_prince_aq_2",
        "ending_prince_aq_2_2",
        A_SetSpriteSequence,
    )
    update_ally_animation(
        a2, ally, SpriteAnimationState.PRINCE_NEUTRAL, use_primary=use_primary
    )
    a3 = world.event_scripts.get_subscript_command_by_identifier(
        "ending_prince_aq_2",
        "ending_prince_aq_2_3",
        A_SetSpriteSequence,
    )
    update_ally_animation(
        a3, ally, SpriteAnimationState.PRINCE_LEFT, use_primary=use_primary
    )
    a4 = world.event_scripts.get_subscript_command_by_identifier(
        "ending_prince_aq_2",
        "ending_prince_aq_2_4",
        A_SetSpriteSequence,
    )
    update_ally_animation(
        a4, ally, SpriteAnimationState.PRINCE_NEUTRAL, use_primary=use_primary
    )
    a5 = world.event_scripts.get_subscript_command_by_identifier(
        "ending_prince_aq_2",
        "ending_prince_aq_2_5",
        A_SetSpriteSequence,
    )
    update_ally_animation(
        a5, ally, SpriteAnimationState.PRINCE_JOY, use_primary=use_primary
    )
    a6 = world.event_scripts.get_subscript_command_by_identifier(
        "ending_mway_character_looks_south_aq",
        "ending_mway_character_looks_south",
        A_SetSpriteSequence,
    )
    update_ally_animation(
        a6, ally, SpriteAnimationState.LOOK_TO_DOWN, use_primary=use_primary
    )
    a7 = world.event_scripts.get_subscript_command_by_identifier(
        "ending_mway_character_looks_down_aq",
        "ending_mway_character_looks_down",
        A_SetSpriteSequence,
    )
    update_ally_animation(
        a7, ally, SpriteAnimationState.LOOKING_DOWN, use_primary=use_primary
    )
    a8 = world.event_scripts.get_subscript_command_by_identifier(
        "ending_mway_character_shocked_fwd_aq",
        "ending_mway_character_shocked_fwd",
        A_SetSpriteSequence,
    )
    update_ally_animation(
        a8, ally, SpriteAnimationState.SHOCKED_SHADOW, use_primary=use_primary
    )
    a9 = world.event_scripts.get_subscript_command_by_identifier(
        "ending_mway_character_look_down_2_aq",
        "ending_mway_character_look_down_2",
        A_SetSpriteSequence,
    )
    update_ally_animation(
        a9, ally, SpriteAnimationState.LOOKING_DOWN, use_primary=use_primary
    )
    a10 = world.event_scripts.get_subscript_command_by_identifier(
        "ending_mway_character_sees_geno_aq",
        "ending_mway_character_sees_geno",
        A_SetSpriteSequence,
    )
    update_ally_animation(
        a10, ally, SpriteAnimationState.SEES_GENO, use_primary=use_primary
    )
    a11 = world.event_scripts.get_subscript_command_by_identifier(
        "ending_mway_character_geno_joy_aq",
        "ending_mway_character_geno_joy",
        A_SetSpriteSequence,
    )
    update_ally_animation(
        a11, ally, SpriteAnimationState.JOY, use_primary=use_primary
    )


def render_ending_character_3(
    world: GameWorld,
    prize: CharacterPrize,
    *,
    protagonist_prize: CharacterPrize | None = None,
) -> None:
    if isinstance(prize, GenoRecruitmentPrize):
        return
    _apply_ending_character_npc_fills(world, prize, _ENDING_CHARACTER_3_NPC_FILLS)
    _apply_ending_character_3_doll_fills(world, prize, _ENDING_CHARACTER_3_DOLL_FILLS)
    ally = prize.ally
    use_primary = isinstance(prize, MarioRecruitmentPrize) or (
        protagonist_prize is not None and prize is protagonist_prize
    )
    world.event_scripts.delete_subscript_command_by_identifier(
        "ending_doll_aq_a",
        "ending_doll_",
    )
    world.event_scripts.delete_subscript_command_by_identifier(
        "ending_doll_cliff_seq_aq",
        "ending_doll_cliff_seq",
    )
    a0 = world.action_scripts.get_command_by_identifier(
        "ending_forest_char_spin",
        A_SetSpriteSequence
    )
    update_ally_animation(
        a0, ally, SpriteAnimationState.SPIN, use_primary=use_primary
    )
    a1 = world.event_scripts.get_subscript_command_by_identifier(
        "ending_mway_character_geno_joy_aq",
        "ending_mway_character_geno_joy",
        A_SetSpriteSequence,
    )
    update_ally_animation(
        a1, ally, SpriteAnimationState.JOY, use_primary=use_primary
    )
    a2 = world.event_scripts.get_subscript_command_by_identifier(
        "ending_forest_character_spell_frame_3_aq",
        "ending_forest_character_spell_frame_3",
        A_SetSpriteSequence,
    )
    update_ally_animation(
        a2, ally, SpriteAnimationState.SPELL_FRAME_3, use_primary=use_primary
    )
    a3 = world.event_scripts.get_subscript_command_by_identifier(
        "ending_forest_character_spell_frames_aq",
        "ending_forest_character_spell_frame_3_",
        A_SetSpriteSequence,
    )
    update_ally_animation(
        a3, ally, SpriteAnimationState.SPELL_FRAME_3, use_primary=use_primary
    )
    a4 = world.event_scripts.get_subscript_command_by_identifier(
        "ending_forest_character_spell_frames_aq",
        "ending_forest_character_spell_frame_4",
        A_SetSpriteSequence,
    )
    update_ally_animation(
        a4, ally, SpriteAnimationState.SPELL_FRAME_4, use_primary=use_primary
    )
    a5 = world.event_scripts.get_subscript_command_by_identifier(
        "ending_forest_character_spell_frames_aq",
        "ending_forest_character_spell_frame_5",
        A_SetSpriteSequence,
    )
    update_ally_animation(
        a5, ally, SpriteAnimationState.SPELL_FRAME_5, use_primary=use_primary
    )
    a6 = world.event_scripts.get_subscript_command_by_identifier(
        "ending_forest_character_spell_frames_aq",
        "ending_forest_character_spell_frame_6",
        A_SetSpriteSequence,
    )
    update_ally_animation(
        a6, ally, SpriteAnimationState.SPELL_FRAME_6, use_primary=use_primary
    )
    a7 = world.event_scripts.get_subscript_command_by_identifier(
        "ending_forest_character_looks_down_aq",
        "ending_forest_character_looks_down",
        A_SetSpriteSequence,
    )
    update_ally_animation(
        a7, ally, SpriteAnimationState.LOOKING_DOWN_AWAY, use_primary=use_primary
    )
    a8 = world.event_scripts.get_subscript_command_by_identifier(
        "ending_forest_character_victory_pose_aq",
        "ending_forest_character_victory_pose",
        A_SetSpriteSequence,
    )
    update_ally_animation(
        a8, ally, SpriteAnimationState.VICTORY_POSE, use_primary=use_primary
    )


def render_ending_character_4(
    world: GameWorld,
    prize: CharacterPrize,
    *,
    protagonist_prize: CharacterPrize | None = None,
) -> None:
    if isinstance(prize, BowserRecruitmentPrize):
        return
    _apply_ending_character_npc_fills(world, prize, _ENDING_CHARACTER_4_NPC_FILLS)
    ally = prize.ally
    use_primary = isinstance(prize, MarioRecruitmentPrize) or (
        protagonist_prize is not None and prize is protagonist_prize
    )
    a0 = world.action_scripts.get_command_by_identifier(
        "mines_character_hammering",
        A_SetSpriteSequence
    )
    update_ally_animation(
        a0, ally, SpriteAnimationState.HAMMER, use_primary=use_primary
    )
    a1 = world.action_scripts.get_command_by_identifier(
        "mines_character_hammering_stop",
        A_SetSpriteSequence
    )
    update_ally_animation(
        a1, ally, SpriteAnimationState.HAMMER_STATIC, use_primary=use_primary
    )
    a2 = world.action_scripts.get_command_by_identifier(
        "mines_character_hammering_look_away",
        A_SetSpriteSequence
    )
    update_ally_animation(
        a2, ally, SpriteAnimationState.DISTRACTED, use_primary=use_primary
    )
    a3 = world.action_scripts.get_command_by_identifier(
        "mines_character_hammering_mad",
        A_SetSpriteSequence
    )
    update_ally_animation(
        a3, ally, SpriteAnimationState.DISPLEASED, use_primary=use_primary
    )
    a4 = world.event_scripts.get_subscript_command_by_identifier(
        "ending_mines_character_looks_left_aq",
        "ending_mines_character_looks_left",
        A_SetSpriteSequence,
    )
    update_ally_animation(
        a4, ally, SpriteAnimationState.LOOK_TO_SIDE_BEHIND, use_primary=use_primary
    )
    a5 = world.event_scripts.get_subscript_command_by_identifier(
        "ending_mines_character_looks_down_aq",
        "ending_mines_character_looks_down",
        A_SetSpriteSequence,
    )
    update_ally_animation(
        a5, ally, SpriteAnimationState.LOOKING_DOWN_AWAY, use_primary=use_primary
    )
    a6 = world.event_scripts.get_subscript_command_by_identifier(
        "ending_mines_character_shocked_bwd_aq",
        "ending_mines_character_shocked_bwd",
        A_SetSpriteSequence,
    )
    update_ally_animation(
        a6, ally, SpriteAnimationState.SHOCKED_SHADOW_BACKWARDS, use_primary=use_primary
    )
    a7 = world.event_scripts.get_subscript_command_by_identifier(
        "ending_mines_character_look_down_2_aq",
        "ending_mines_character_look_down_2",
        A_SetSpriteSequence,
    )
    update_ally_animation(
        a7, ally, SpriteAnimationState.LOOKING_DOWN_AWAY, use_primary=use_primary
    )
    a8 = world.event_scripts.get_subscript_command_by_identifier(
        "ending_mines_character_lean_2_aq",
        "ending_mines_character_lean_2_1",
        A_SetSpriteSequence,
    )
    update_ally_animation(
        a8, ally, SpriteAnimationState.LEAN_BACK, use_primary=use_primary
    )
    a9 = world.event_scripts.get_subscript_command_by_identifier(
        "ending_mines_character_lean_2_aq",
        "ending_mines_character_lean_2_2",
        A_SetSpriteSequence,
    )
    update_ally_animation(
        a9, ally, SpriteAnimationState.LEAN_BACK_2, use_primary=use_primary
    )
    a10 = world.event_scripts.get_subscript_command_by_identifier(
        "ending_mines_character_looks_upward_aq",
        "ending_mines_character_looks_upward",
        A_SetSpriteSequence,
    )
    update_ally_animation(
        a10, ally, SpriteAnimationState.DISTRACTED, use_primary=use_primary
    )
    a11 = world.event_scripts.get_subscript_command_by_identifier(
        "ending_mines_character_raised_arms_aq",
        "ending_mines_character_raised_arms",
        A_SetSpriteSequence,
    )
    update_ally_animation(
        a11, ally, SpriteAnimationState.JOY_BEHIND, use_primary=use_primary
    )


def render_ending_character_5(
    world: GameWorld,
    prize: CharacterPrize,
    *,
    protagonist_prize: CharacterPrize | None = None,
) -> None:
    if isinstance(prize, ToadstoolRecruitmentPrize):
        return
    _apply_ending_character_npc_fills(world, prize, _ENDING_CHARACTER_5_NPC_FILLS)
    ally = prize.ally
    use_primary = isinstance(prize, MarioRecruitmentPrize) or (
        protagonist_prize is not None and prize is protagonist_prize
    )
    a23 = world.event_scripts.get_subscript_command_by_identifier(
        "ending_mmr_character_looks_north_aq",
        "ending_mmr_character_looks_north",
        A_SetSpriteSequence,
    )
    update_ally_animation(
        a23, ally, SpriteAnimationState.DISTRACTED, use_primary=use_primary
    )
    a24 = world.event_scripts.get_subscript_command_by_identifier(
        "ending_mmr_character_looks_down_aq",
        "ending_mmr_character_looks_down",
        A_SetSpriteSequence,
    )
    update_ally_animation(
        a24, ally, SpriteAnimationState.LOOKING_DOWN_AWAY, use_primary=use_primary
    )
    a25 = world.event_scripts.get_subscript_command_by_identifier(
        "ending_mmr_character_shocked_bwd_aq",
        "ending_mmr_character_shocked_bwd",
        A_SetSpriteSequence,
    )
    update_ally_animation(
        a25, ally, SpriteAnimationState.SHOCKED_SHADOW_BACKWARDS, use_primary=use_primary
    )
    a26 = world.event_scripts.get_subscript_command_by_identifier(
        "ending_mmr_character_lean_far_aq",
        "ending_mmr_character_lean_far",
        A_SetSpriteSequence,
    )
    update_ally_animation(
        a26, ally, SpriteAnimationState.LEAN_BACK_2, use_primary=use_primary
    )
    a27 = world.event_scripts.get_subscript_command_by_identifier(
        "ending_marrymore_char_look_down_2_aq",
        "ending_marrymore_char_look_down_2",
        A_SetSpriteSequence,
    )
    update_ally_animation(
        a27, ally, SpriteAnimationState.LOOKING_DOWN_AWAY, use_primary=use_primary
    )
    a28 = world.event_scripts.get_subscript_command_by_identifier(
        "ending_mmr_character_lean_2_aq",
        "ending_mmr_character_lean_far_2_partial",
        A_SetSpriteSequence,
    )
    update_ally_animation(
        a28, ally, SpriteAnimationState.LEAN_BACK, use_primary=use_primary
    )
    a29 = world.event_scripts.get_subscript_command_by_identifier(
        "ending_mmr_character_lean_2_aq",
        "ending_mmr_character_lean_far_2_full",
        A_SetSpriteSequence,
    )
    update_ally_animation(
        a29, ally, SpriteAnimationState.LEAN_BACK_2, use_primary=use_primary
    )
    a30 = world.event_scripts.get_subscript_command_by_identifier(
        "ending_marrymore_char_look_left_aq",
        "ending_marrymore_char_look_left",
        A_SetSpriteSequence,
    )
    update_ally_animation(
        a30, ally, SpriteAnimationState.LOOK_TO_SIDE_BEHIND, use_primary=use_primary
    )
    a31 = world.event_scripts.get_subscript_command_by_identifier(
        "ending_marrymore_char_joy_jump_aq",
        "ending_marrymore_char_joy_jump_1",
        A_SetSpriteSequence,
    )
    update_ally_animation(
        a31, ally, SpriteAnimationState.JOY_JUMP_BEHIND, use_primary=use_primary
    )
    a32 = world.event_scripts.get_subscript_command_by_identifier(
        "ending_marrymore_char_joy_jump_aq",
        "ending_marrymore_char_joy_jump_2",
        A_SetSpriteSequence,
    )
    update_ally_animation(
        a32, ally, SpriteAnimationState.JOY_BEHIND, use_primary=use_primary
    )

def _ending_palette_for_prize(prize: CharacterPrize) -> int:
    """Return the light ending-credits palette ID for `prize`."""
    if isinstance(prize, MarioRecruitmentPrize):
        return EPAL0084_MARIO_ENDING
    if isinstance(prize, MallowRecruitmentPrize):
        return EPAL0085_MALLOW_ENDING
    if isinstance(prize, GenoRecruitmentPrize):
        return EPAL0086_GENO_ENDING
    if isinstance(prize, ToadstoolRecruitmentPrize):
        return EPAL0141_TOADSTOOL_ENDING
    if isinstance(prize, BowserRecruitmentPrize):
        return EPAL0140_BOWSER_ENDING
    raise ValueError(f"No light ending palette mapping for {type(prize).__name__}")


def _ending_dark_palette_for_prize(prize: CharacterPrize) -> int:
    """Return the dark ending-credits palette ID for `prize`."""
    if isinstance(prize, MarioRecruitmentPrize):
        return EPAL0163_MARIO_ENDING_DARK
    if isinstance(prize, ToadstoolRecruitmentPrize):
        return EPAL0164_TOADSTOOL_ENDING_DARK
    if isinstance(prize, MallowRecruitmentPrize):
        return EPAL0166_MALLOW_ENDING_DARK
    if isinstance(prize, GenoRecruitmentPrize):
        return EPAL0167_GENO_ENDING_DARK
    if isinstance(prize, BowserRecruitmentPrize):
        return EPAL0165_BOWSER_ENDING_DARK
    raise ValueError(f"No dark ending palette mapping for {type(prize).__name__}")


# Identifiers for the light/dark PaletteSetMorphs and PaletteSet commands in
# script_3951. The light commands are PaletteSetMorphs (use set_palette_set);
# the dark commands are PaletteSet (use set_palette_set_starts_at).
_ENDING_PALETTE_IDS_PROTAGONIST = ("ending_protagonist_palette", "ending_protagonist_palette_dark")
_ENDING_PALETTE_IDS_2 = ("ending_mushroom_way_char_palette", "ending_mushroom_way_char_palette_dark")
_ENDING_PALETTE_IDS_3 = ("ending_forest_maze_char_palette", "ending_forest_character_dark")
_ENDING_PALETTE_IDS_4 = ("ending_inner_mines_char_palette", "ending_inner_mines_palette_dark")
_ENDING_PALETTE_IDS_5 = ("ending_marrymore_char_palette", "ending_marrymore_char_palette_dark")


def _set_ending_palette_pair(
    world: GameWorld, ids: tuple[str, str], prize: CharacterPrize
) -> None:
    """Update the (light, dark) palette command pair identified by `ids` so
    that they show `prize`'s ending palette."""
    light_id, dark_id = ids
    world.event_scripts.get_command_by_identifier(
        light_id, PaletteSetMorphs
    ).set_palette_set(_ending_palette_for_prize(prize))
    world.event_scripts.get_command_by_identifier(
        dark_id, PaletteSet
    ).set_palette_set_starts_at(_ending_dark_palette_for_prize(prize))


def apply_ending_characters(
    world: GameWorld,
    *,
    mushroom_way_prize: CharacterPrize | None,
    forest_maze_prize: CharacterPrize | None,
    inner_mines_prize: CharacterPrize | None,
    marrymore_prize: CharacterPrize | None,
    substitute_prizes: list[CharacterPrize],
    mario_override: CharacterPrize | None = None,
) -> None:
    """Resolve the four ending-cutscene character prizes plus the protagonist
    and dispatch to the matching render_ending_character_N function.

    Mapping of named recruitment slot to ending-cutscene function:
        MushroomWayCharacter -> render_ending_character_2
        ForestMazeCharacter  -> render_ending_character_3
        InnerMinesCharacter  -> render_ending_character_4
        MarrymoreCharacter   -> render_ending_character_5

    `substitute_prizes` is the pool of CharacterPrize instances that are not
    placed in any of the named recruitment slots above — i.e. the StartingCharacterX
    prizes plus stand-in prizes for any character excluded from the seed via
    the AvailableCharacters flag. The pool is shuffled and drained without
    replacement: each empty named slot pops one prize, and the single remaining
    prize is used as the protagonist (whose palette goes into the
    "ending_protagonist_palette" pair).

    `mario_override`, when provided, replaces every MarioRecruitmentPrize among
    the inputs (the four named-slot prizes and the substitute pool) with the
    given prize. This is used when PlayAsStarter is disabled and Mario is not
    the starter: the player visually plays as the starter character but Mario
    is conceptually the protagonist, so any Mario placement in the ending
    cutscene should display the starter instead.

    Side effects:
      - The five ending-cutscene PaletteSetMorphs / PaletteSet command pairs
        in script_3951 are updated to match each character's actual ending
        slot.
      - Each render_ending_character_N function is called with its resolved
        prize."""

    def _apply_mario_override(p: CharacterPrize | None) -> CharacterPrize | None:
        if mario_override is None or p is None:
            return p
        if isinstance(p, MarioRecruitmentPrize):
            return mario_override
        return p

    ending_prizes: list[CharacterPrize | None] = [
        _apply_mario_override(mushroom_way_prize),
        _apply_mario_override(forest_maze_prize),
        _apply_mario_override(inner_mines_prize),
        _apply_mario_override(marrymore_prize),
    ]
    empty_indexes = [i for i, p in enumerate(ending_prizes) if p is None]

    pool: list[CharacterPrize] = []
    for sp in substitute_prizes:
        overridden = _apply_mario_override(sp)
        assert isinstance(overridden, CharacterPrize)
        pool.append(overridden)
    random.shuffle(pool)

    for i in empty_indexes:
        if not pool:
            raise RuntimeError(
                "Cannot resolve ending character slots: not enough substitute "
                "prizes to cover every empty named recruitment slot."
            )
        ending_prizes[i] = pool.pop()

    if not pool:
        raise RuntimeError(
            "Cannot resolve protagonist for ending cutscene: substitute pool "
            "is empty after filling named slots."
        )
    # Whoever is left in the pool is the protagonist. If somehow more than one
    # character is left (shouldn't happen with five total characters mapped
    # across nine recruitment slots), pick one at random.
    protagonist_prize = pool.pop() if len(pool) == 1 else random.choice(pool)

    p2, p3, p4, p5 = ending_prizes
    assert (
        isinstance(p2, CharacterPrize)
        and isinstance(p3, CharacterPrize)
        and isinstance(p4, CharacterPrize)
        and isinstance(p5, CharacterPrize)
    )

    # DEBUG OVERRIDE: force vanilla cutscene assignment regardless of recruit
    # shuffle. Set R496_FORCE_VANILLA_CUTSCENE_ASSIGNMENT = False to disable.
    # When enabled, Peach is marrymore (p5), Mallow is mushroom_way (p2),
    # Geno is forest (p3), Bowser is inner_mines (p4), Mario is protagonist —
    # so the only non-trivial retarget in _apply_r496_role_assignments is
    # MARIO → NPC_19 (Mario's native slot). Recruit-room placements are
    # untouched; only the ending cutscene is reassigned. Useful for
    # isolating Mario-NPC-as-protagonist behavior from the role-swap path.
    R496_FORCE_VANILLA_CUTSCENE_ASSIGNMENT = True
    if R496_FORCE_VANILLA_CUTSCENE_ASSIGNMENT:
        all_five: list[CharacterPrize] = [p2, p3, p4, p5, protagonist_prize]
        by_type: dict[type, CharacterPrize] = {type(p): p for p in all_five}
        if len(by_type) == 5:
            p2 = by_type[MallowRecruitmentPrize]
            p3 = by_type[GenoRecruitmentPrize]
            p4 = by_type[BowserRecruitmentPrize]
            p5 = by_type[ToadstoolRecruitmentPrize]
            protagonist_prize = by_type[MarioRecruitmentPrize]
        # If fewer than 5 distinct character types are present (excluded char,
        # duplicate stand-ins), leave the random assignment alone.

    _set_ending_palette_pair(world, _ENDING_PALETTE_IDS_PROTAGONIST, protagonist_prize)
    _set_ending_palette_pair(world, _ENDING_PALETTE_IDS_2, p2)
    _set_ending_palette_pair(world, _ENDING_PALETTE_IDS_3, p3)
    _set_ending_palette_pair(world, _ENDING_PALETTE_IDS_4, p4)
    _set_ending_palette_pair(world, _ENDING_PALETTE_IDS_5, p5)

    # R496 ending cutscene role-swap path is disabled by default. With Mario at
    # NPC_19 and target=MARIO references hardcoded to target=NPC_19 in
    # script_3885 (similarly NPC_0 in script_3950 / script_3951 for R088 / R375),
    # no apply-time retargeting is needed for the vanilla cutscene assignments.
    # The helper and its support code are kept around to revisit shuffled-recruit
    # cutscene assignments later, where we'll need a way to lock per-NPC vram
    # sizes so the partition orchestrator doesn't over-size animations.
    R496_USE_ROLE_SWAP_PATH = False
    if R496_USE_ROLE_SWAP_PATH:
        _apply_r496_role_assignments(
            world,
            marrymore_prize=p5,
            mushroom_way_prize=p2,
            forest_maze_prize=p3,
            inner_mines_prize=p4,
            protagonist_prize=protagonist_prize,
        )

    render_ending_character_2(world, p2, protagonist_prize=protagonist_prize)
    render_ending_character_3(world, p3, protagonist_prize=protagonist_prize)
    render_ending_character_4(world, p4, protagonist_prize=protagonist_prize)
    render_ending_character_5(world, p5, protagonist_prize=protagonist_prize)


# =============================================================================
# Seaside / Ship
# =============================================================================


def render_seaside_beach_boss(world: GameWorld, prize: BossFightPrize) -> None:
    """Apply animation changes for Seaside Beach boss fight."""
    m = prize.smallest_npc()

    # large boss sprite
    world.event_scripts.delete_subscript_command_by_identifier(
        "seaside_boss_reveal_sequence", "seaside_boss_reveal_sequence_1"
    )


def render_ship_password_boss(world: GameWorld, prize: BossFightPrize) -> None:
    """Apply animation changes for Ship Password boss fight."""
    world.action_scripts.delete_command_by_identifier("password_boss_vanilla_1")
    world.action_scripts.delete_command_by_identifier("password_boss_vanilla_2")
    m = prize.smallest_npc()
    if m.animations.ship_beckon is not None:
        c = world.action_scripts.get_command_by_identifier(
            "password_boss_reveal_sequence", A_SetSpriteSequence
        )
        c.set_index(m.animations.ship_beckon.sequence_id)
    else:
        world.action_scripts.delete_command_by_identifier(
            "password_boss_reveal_sequence"
        )


def render_ship_final_boss(world: GameWorld, prize: BossFightPrize) -> None:
    """Apply animation changes for Ship Final boss fight."""
    m = prize.smallest_npc()
    # boss room on revisit
    if m.animations.ship_chair is not None:
        c = world.action_scripts.get_command_by_identifier(
            "ship_boss_idle_sequence", A_SetSpriteSequence
        )
        c.set_index(m.animations.ship_chair.sequence_id)
    else:
        world.action_scripts.replace_command_by_identifier(
            "ship_boss_idle_sequence", A_FaceSouthwest()
        )
        world.action_scripts.delete_command_by_identifier(
            "ship_boss_idle_sequence_loop"
        )

    # ending credits
    if m.animations.tpose_mold_id is not None:
        world.event_scripts.replace_subscript_command_by_identifier(
            "ending_credits_sunset_npc_0_sequence_setup",
            "ending_credits_sunset_npc_0_sequence",
            A_SetSpriteSequence(index=m.animations.tpose_mold_id, is_mold=True),
        )
    else:
        world.event_scripts.replace_subscript_command_by_identifier(
            "ending_credits_sunset_npc_0_sequence_setup",
            "ending_credits_sunset_npc_0_sequence",
            A_FaceNorthwest(),
        )

    # Delete event script commands for unfilled character henchman slots
    assigned_count = (
        len(prize.character_henchmen) if prize.character_henchmen is not None else 0
    )
    if assigned_count > 0 and assigned_count < 2:
        # Slot 0 unfilled
        if assigned_count < 1:
            for d in [
                "ship_henchman_1_beach_1",
                "ship_henchman_1_beach_2",
                "ship_henchman_1_beach_3",
            ]:
                world.event_scripts.delete_command_by_identifier(d)
        # Slot 1 unfilled
        if assigned_count < 2:
            world.event_scripts.delete_command_by_identifier("ship_henchman_2_beach_1")

def render_ship_postgame_boss(world: GameWorld, prize: BossFightPrize) -> None:
    """Apply animation changes for Ship Final boss fight."""
    m = prize.smallest_npc()
    # boss room on revisit
    if m.animations.ship_chair is not None:
        c = world.event_scripts.get_subscript_command_by_identifier(
            "ship_boss_idle_script_2", "ship_boss_idle_sequence_2", A_SetSpriteSequence
        )
        c.set_index(m.animations.ship_chair.sequence_id)
    else:
        world.event_scripts.replace_subscript_command_by_identifier(
            "ship_boss_idle_script_2", "ship_boss_idle_sequence_2", A_FaceSouthwest()
        )
        world.event_scripts.delete_subscript_command_by_identifier(
            "ship_boss_idle_script_2", "ship_boss_idle_sequence_loop_2"
        )
        
# =============================================================================
# Dojo
# =============================================================================


def render_dojo_first_fight(world: GameWorld, prize: BossFightPrize) -> None:
    """Apply animation changes for Dojo first fight."""
    m = prize.smallest_npc()
    # Check if prize is a mimic-type boss
    from ..progression.prizes import (
        PandoriteBossFight,
        HidonBossFight,
        BoxBoyBossFight,
        ChesterBossFight,
    )

    if isinstance(
        prize, (PandoriteBossFight, HidonBossFight, BoxBoyBossFight, ChesterBossFight)
    ):
        cast(
            ActionQueueAsync,
            world.event_scripts.get_command_by_identifier("dojo_boss_1_initiate_aq"),
        ).set_subscript(get_mimic_rise_dojo())
    else:
        if m.animations.dojo_challenge is not None:
            world.event_scripts.get_subscript_command_by_identifier(
                "dojo_boss_1_initiate_aq",
                "dojo_boss_1_initiate",
                A_SetSpriteSequence,
            ).set_index(m.animations.dojo_challenge.sequence_id)
            if m.animations.dojo_challenge.contact_frame is not None:
                world.event_scripts.get_subscript_command_by_identifier(
                    "dojo_boss_1_initiate_aq", "dojo_boss_1_pause", A_Pause
                ).set_length(m.animations.dojo_challenge.contact_frame)
        else:
            world.event_scripts.get_subscript_command_by_identifier(
                "dojo_boss_1_initiate_aq",
                "dojo_boss_1_initiate",
                A_SetSpriteSequence,
            ).set_index(0)
    if m.animations.recoil is not None:
        world.event_scripts.get_subscript_command_by_identifier(
            "dojo_boss_1_recoil_aq", "dojo_boss_1_recoil", A_SetSpriteSequence
        ).set_index(m.animations.recoil.sequence_id)
    else:
        world.event_scripts.delete_subscript_command_by_identifier(
            "dojo_boss_1_recoil_aq", "dojo_boss_1_recoil"
        )
    world.event_scripts.replace_subscript_command_by_identifier(
        "EVENT_2067_action_queue_0", "jagger_looks_around", A_FaceNorthwest()
    )


def render_dojo_fight(
    world: GameWorld,
    prize: BossFightPrize,
    initiate_aq_id: str,
    initiate_id: str,
    pause_id: str,
    deescalate_aq_id: str | None = None,
    deescalate_id: str | None = None,
) -> None:
    """Apply animation changes for a generic Dojo fight."""
    m = prize.smallest_npc()
    from ..progression.prizes import (
        PandoriteBossFight,
        HidonBossFight,
        BoxBoyBossFight,
        ChesterBossFight,
    )

    if isinstance(
        prize, (PandoriteBossFight, HidonBossFight, BoxBoyBossFight, ChesterBossFight)
    ):
        cast(
            ActionQueueAsync,
            world.event_scripts.get_command_by_identifier(initiate_aq_id),
        ).set_subscript(get_mimic_rise_dojo())
    else:
        if m.animations.dojo_challenge is not None:
            world.event_scripts.get_subscript_command_by_identifier(
                initiate_aq_id,
                initiate_id,
                A_SetSpriteSequence,
            ).set_index(m.animations.dojo_challenge.sequence_id)
            if m.animations.dojo_challenge.contact_frame is not None:
                world.event_scripts.get_subscript_command_by_identifier(
                    initiate_aq_id, pause_id, A_Pause
                ).set_length(m.animations.dojo_challenge.contact_frame)
            if deescalate_aq_id is not None and deescalate_id is not None:
                world.event_scripts.get_subscript_command_by_identifier(
                    deescalate_aq_id,
                    deescalate_id,
                    A_SetSpriteSequence,
                ).set_index(m.animations.dojo_challenge.sequence_id)
        else:
            world.event_scripts.get_subscript_command_by_identifier(
                initiate_aq_id,
                initiate_id,
                A_SetSpriteSequence,
            ).set_index(0)
            if deescalate_aq_id is not None and deescalate_id is not None:
                world.event_scripts.delete_subscript_command_by_identifier(
                    deescalate_aq_id, deescalate_id
                )


# =============================================================================
# Bean Valley
# =============================================================================


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


# =============================================================================
# Nimbus Castle / Statue Room
# =============================================================================


def render_statue_room_boss(
    world: GameWorld,
    prize: BossFightPrize,
    keep_minigame_sprites: bool,
    chosen_npc_model: type[BossNPC] | None = None,
) -> None:
    """Apply animation changes for Statue Room boss fight."""
    if isinstance(prize, DodoBossFight):
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

    if m.animations.statue_flustered is not None:
        world.event_scripts.get_subscript_command_by_identifier(
            "statue_keeper_flustered_aq",
            "statue_keeper_flustered_1",
            A_SetSpriteSequence,
        ).set_index(m.animations.statue_flustered.sequence_id)
    else:
        world.event_scripts.delete_subscript_command_by_identifier(
            "statue_keeper_flustered_aq", "statue_keeper_flustered_1"
        )

    if has_back_walking_sequence:
        dodo_replacement_faces_wrong_direction = (
            world.event_scripts.get_subscript_command_by_identifier(
                "dodo_hallway_mirror_sprite_if_not_vanilla_container",
                "dodo_hallway_mirror_sprite_if_not_vanilla",
                A_SetSpriteSequence,
            )
        )
        dodo_replacement_faces_wrong_direction.set_mirror_sprite(True)
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

    # main 11-step NW walk — base script sets sequence 1 mirrored for Dodo;
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
    world.event_scripts.delete_subscript_command_by_identifier(
        "statue_keeper_introduced_aq", "statue_keeper_introduced_2"
    )



# =============================================================================
# Volcano
# =============================================================================


def render_volcano_exit_boss(
    world: GameWorld,
    prize: BossFightPrize,
) -> None:
    """Apply henchman slot event script changes for Volcano Exit boss fight."""

    def slot_has_henchman(slot_index: int) -> bool:
        return (
            prize.character_henchmen is not None
            and len(prize.character_henchmen) > slot_index
        )

    loops = 0

    # Slot 0 - black
    if not slot_has_henchman(0):
        world.event_scripts.delete_command_by_identifier("axem_henchman_1_aq")
        world.event_scripts.delete_command_by_identifier("axem_henchman_1_aq_2")
        world.event_scripts.delete_command_by_identifier("axem_henchman_1_aq_3")
        world.get_room(R392_VOLCANO_POSTCD_AREA_06).get_npc_by_target_id(
            NPC_1
        ).set_visible(False)
        world.get_room(R391_VOLCANO_POSTCD_AREA_04).get_npc_by_target_id(
            NPC_0
        ).set_visible(False)
        world.get_room(
            R393_VOLCANO_POSTCD_AREA_07_WARP_TO_WORLD_MAP
        ).get_npc_by_target_id(NPC_2).set_visible(False)
    else:
        loops += 1

    # Slot 1 - pink
    if not slot_has_henchman(1):
        world.event_scripts.delete_command_by_identifier("axem_henchman_2_aq")
        world.event_scripts.delete_command_by_identifier("axem_henchman_2_aq_2")
        world.get_room(R392_VOLCANO_POSTCD_AREA_06).get_npc_by_target_id(
            NPC_2
        ).set_visible(False)
        world.get_room(
            R393_VOLCANO_POSTCD_AREA_07_WARP_TO_WORLD_MAP
        ).get_npc_by_target_id(NPC_3).set_visible(False)
    else:
        loops += 1

    # Slot 2 - green
    if not slot_has_henchman(2):
        world.event_scripts.delete_command_by_identifier("axem_henchman_3_aq")
        world.event_scripts.delete_command_by_identifier("axem_henchman_3_aq_2")
        world.get_room(R392_VOLCANO_POSTCD_AREA_06).get_npc_by_target_id(
            NPC_3
        ).set_visible(False)
        world.get_room(
            R393_VOLCANO_POSTCD_AREA_07_WARP_TO_WORLD_MAP
        ).get_npc_by_target_id(NPC_4).set_visible(False)
        world.get_room(R394_VOLCANO_POSTCD_AREA_05).get_npc_by_target_id(
            NPC_1
        ).set_visible(False)
    else:
        loops += 1

    # Slot 3 - yellow
    if not slot_has_henchman(3):
        world.event_scripts.delete_command_by_identifier("axem_henchman_4_aq")
        world.event_scripts.delete_command_by_identifier("axem_henchman_4_aq_2")
        world.get_room(R392_VOLCANO_POSTCD_AREA_06).get_npc_by_target_id(
            NPC_4
        ).set_visible(False)
        world.get_room(
            R393_VOLCANO_POSTCD_AREA_07_WARP_TO_WORLD_MAP
        ).get_npc_by_target_id(NPC_5).set_visible(False)
        world.get_room(R394_VOLCANO_POSTCD_AREA_05).get_npc_by_target_id(
            NPC_0
        ).set_visible(False)
    else:
        loops += 1

    if loops == 0:
        world.event_scripts.delete_command_by_identifier("axem_trampoline_aqueue")
    else:
        # Get the loop command and set its count (don't delete it)
        world.event_scripts.get_subscript_command_by_identifier(
            "axem_trampoline_aqueue",
            "axem_trampoline_loop",
            A_StartLoopNTimes,
        ).set_count(loops)


# =============================================================================
# Inner Factory
# =============================================================================


def render_inner_factory_second_fight(world: GameWorld, prize: BossFightPrize) -> None:
    """Apply look-up animation changes for Inner Factory Second Fight."""
    if isinstance(prize, (ClerkBossFight, ManagerBossFight, DirectorBossFight)):
        return
    m = prize.smallest_npc()
    look_up_replacements = [
        ("factory_2nd_boss_look_up_aq_1", "factory_2nd_boss_look_up_1"),
        ("factory_2nd_boss_look_up_aq_2", "factory_2nd_boss_look_up_2"),
        ("factory_2nd_boss_look_up_aq_3", "factory_2nd_boss_look_up_3"),
    ]
    for eid, aid in look_up_replacements:
        if m.animations.look_at_ceiling_mold_id is not None:
            world.event_scripts.get_subscript_command_by_identifier(
                eid, aid, A_SetSpriteSequence
            ).set_index(m.animations.look_at_ceiling_mold_id)
        else:
            world.event_scripts.delete_subscript_command_by_identifier(eid, aid)


def render_inner_factory_third_fight_slot(
    world: GameWorld,
    henchman: BossFightHenchman,
    slot_index: int,
) -> None:
    """Apply factory pierce animation for a single henchman slot."""
    anim = henchman.model()._animations.factory_pierce

    slot_configs = [
        (
            A0962_FACTORY_3RD_BOSS_LEFT_HAMMER,
            "factory_3rd_boss_left_hammer_attack",
            "factory_3rd_boss_left_hammer_attack_pause_32",
        ),
        (
            A0963_FACTORY_3RD_BOSS_MID_HAMMER,
            "factory_3rd_boss_mid_hammer_attack",
            "factory_3rd_boss_mid_hammer_attack_pause_32",
        ),
        (
            A0964_FACTORY_3RD_BOSS_RIGHT_HAMMER,
            "factory_3rd_boss_right_hammer_attack",
            "factory_3rd_boss_right_hammer_attack_pause_32",
        ),
    ]

    if slot_index >= len(slot_configs):
        return

    script_id, attack_id, pause_id = slot_configs[slot_index]

    if (
        anim is not None
        and anim.total_duration is not None
        and anim.contact_frame is not None
    ):
        prepause = 32 - anim.total_duration
        world.action_scripts.get_command_by_identifier(
            attack_id, A_SetSpriteSequence
        ).set_index(anim.sequence_id)
        world.action_scripts.get_command_by_identifier(pause_id, A_Pause).set_length(
            anim.contact_frame
        )
        if anim.speed is not NORMAL:
            world.action_scripts.scripts[script_id].insert_before_identifier(
                attack_id, A_SetSequenceSpeed(anim.speed)
            )
        if prepause != 0:
            world.action_scripts.scripts[script_id].insert_before_identifier(
                attack_id, A_Pause(prepause)
            )


def render_inner_factory_fourth_fight(world: GameWorld) -> None:
    """Hide NPCs 0-6 in Gun Yolk's room for non-vanilla boss."""
    room = world.rooms._rooms[R470_FACTORY_GROUNDS_AREA_04_GUN_YOLKS_ROOM]
    assert (
        room is not None
    ), f"Room {R470_FACTORY_GROUNDS_AREA_04_GUN_YOLKS_ROOM} not found"
    for npc_id in [NPC_0, NPC_1, NPC_2, NPC_3, NPC_4, NPC_5, NPC_6]:
        obj = room.get_npc_by_target_id(npc_id)
        assert (
            obj is not None
        ), f"NPC {npc_id} not found in room {R470_FACTORY_GROUNDS_AREA_04_GUN_YOLKS_ROOM}"
        obj.set_visible(False)


def render_final_boss_fight(
    world: GameWorld,
    prize: BossFightPrize,
) -> None:
    """Apply animation changes for Final Boss fight."""

    e3792 = world.event_scripts.get_script_by_id(E3792_FACTORY_FINAL_BOSS_ROOM_LOADER)
    e3794 = world.event_scripts.get_script_by_id(E3794_FACTORY_FINAL_BOSS_FIGHT)
    e3792.set_contents(es_non_smithy_3792.contents)
    e3794.set_contents(es_non_smithy_3794.contents)

    anim = prize.largest_npc().animations.endgame_challenge
    if anim is not None:
        if anim.total_duration is not None and anim.total_duration > 55:
            cast(
                Pause, world.event_scripts.get_command_by_identifier("final_boss_pause")
            ).set_length(anim.total_duration)
            cast(
                ActionQueueSync,
                world.event_scripts.get_command_by_identifier("final_boss_mario_rise"),
            ).subscript.insert_before_nth_command(0, A_Pause(anim.total_duration - 55))
        world.event_scripts.get_script_by_id(
            E0944_FINAL_BOSS_ANIMATION_SUBROUTINE_1
        ).insert_before_nth_command(
            0,
            ActionQueueSync(
                NPC_0,
                [
                    A_SetSpriteSequence(
                        index=anim.sequence_id,
                        is_sequence=True,
                    )
                ],
            ),
        )

        
    room = world.rooms._rooms[R509_FACTORY_GROUNDS_SMITHYS_PAD]
    assert (
        room is not None
    ), f"Room {R509_FACTORY_GROUNDS_SMITHYS_PAD} not found"
    for npc_id in [NPC_4, NPC_5, NPC_6, NPC_7, NPC_9]:
        obj = room.get_npc_by_target_id(npc_id)
        assert (
            obj is not None
        ), f"NPC {npc_id} not found in room {R509_FACTORY_GROUNDS_SMITHYS_PAD}"
        obj.set_visible(False)
    obj = room.get_npc_by_target_id(NPC_8)
    obj.set_z(0)
    obj.set_action_script(A0015_DO_NOTHING)
