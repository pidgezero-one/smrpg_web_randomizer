"""Business logic for custom prize location render methods.

This module contains the extracted business logic from custom render methods
in prizelocations.py, organized by location/area.
"""

from __future__ import annotations

import random
from ast import Return
from typing import TYPE_CHECKING, Mapping, cast
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.directions import Direction

from smrpgpatchbuilder.datatypes.levels.classes import VramStore
from smrpgpatchbuilder.datatypes.overworld_scripts.action_scripts.commands import (
    A_FixedFCoordOn,
    A_TransferXYZFPixels,
    A_WalkNortheastPixels,
)
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments import EAST, NORTHWEST, SOUTHWEST
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.palette_rows import (
    MARIO_PALETTE,
    NPC_PALETTE_ROW_1,
)
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.types.palette_row import (
    PaletteRow,
)
from smrpgpatchbuilder.datatypes.overworld_scripts.event_scripts.commands.types.classes import (
    UsableEventScriptCommand,
)
from smrpgpatchbuilder.datatypes.overworld_scripts.event_scripts.classes import EventScript

from randomizer.progression.prizes import (
    BowserRecruitmentPrize,
    ClerkBossFight,
    DirectorBossFight,
    DodoBossFight,
    GenoRecruitmentPrize,
    KingCalamariBossFight,
    MallowRecruitmentPrize,
    ManagerBossFight,
    MarioRecruitmentPrize,
    ToadstoolRecruitmentPrize,
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
    A_EndLoop,
    A_JmpIfRandom1of2,
    A_VisibilityOn,
    A_SetWalkingSpeed,
    A_JumpToHeight,
    A_WalkSouthwestSteps,
    A_PlaySound,
)
from smrpgpatchbuilder.datatypes.overworld_scripts.action_scripts.arguments.sequence_speeds import (
    NORMAL, FAST
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
    R292_UNMAPPED_HOUSE_ROOM,
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
from ..data.variables.overworld_sfx_names import *
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
from smrpgpatchbuilder.datatypes.overworld_scripts.action_scripts.classes import (
        UsableActionScriptCommand,
    )
from ..data.variables.sprite_names import SPR0031_ALT_PROTAGONIST_1
from ..data.variables.event_script_names import (
        E3885_END_GAME,
        E3950_POST_FINAL_BOSS_INIT,
        E3951_STAR_PIECE_CREDITS_INIT,
    )
from ..data.overworld_scripts.event.scripts import (
        script_3885,
        script_3950,
        script_3951,
    )
from ..progression.prizes import (
        PandoriteBossFight,
        HidonBossFight,
        BoxBoyBossFight,
        ChesterBossFight,
    )

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
    else:
        a = world.action_scripts.delete_command_by_identifier(
            "bandits_way_ascript_recoil"
        )


# =============================================================================
# Forest Maze
# =============================================================================


def render_mushroom_way_character(world: GameWorld, prize: CharacterPrize | None) -> None:
    if prize is None:
        world.event_scripts.delete_subscript_command_by_identifier(
            "EVENT_1710_mario_mad_slot1_aq", "EVENT_1710_mario_mad_slot1"
        )
    else:
        ally_index = prize.ally.index
        if ally_index == 0:
            cmd = world.event_scripts.get_subscript_command_by_identifier(
                "EVENT_1710_mario_mad_slot1_aq", "EVENT_1710_mario_mad_slot1", A_SetSpriteSequence
            )
            cmd.set_index(3)
            cmd.set_sprite_offset(3)
    

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

    as_contents: list[UsableActionScriptCommand] = [
        A_FixedFCoordOn(),
    ]
    m = prize.smallest_npc()
    if m.tower_entrance_horizontal_shift:
        as_contents.append(A_ShiftXYPixels(m.tower_entrance_horizontal_shift, 0))
    shift = 17 - m.eye_height
    if shift > 0:
        as_contents.append(A_WalkNorthPixels(shift))
    elif shift < 0:
        as_contents.append(A_WalkSouthPixels(-shift))
    if len(as_contents) > 0:
        ev.set_contents(
            [
                ActionQueueAsync(entrance.npc_id, as_contents),
                *ev.contents,
            ]
        )

    # Crown height in the chapel
    ev_crown = world.action_scripts.get_command_by_identifier(
        "crown_adjust_height", A_ShiftZUpSteps
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
        ("tower_henchman_curtain_aqueue_33", "tower_henchman_curtain_33_"),
        ("tower_henchman_curtain_aqueue_34", "tower_henchman_curtain_34_"),
        ("tower_henchman_curtain_aqueue_35", "tower_henchman_curtain_35_"),
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
            else tower_toss.total_duration
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
            third_henchman_animations = third_henchman.model().animations
            b = third_henchman_animations.tower_bullet
            if b is not None:
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
                            A_SetSequenceSpeed(
                                b.speed
                            ),
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
        henchman_animations = first_henchman.model().animations
        if henchman_animations.kitchen_prep is not None:
            cmd = world.action_scripts.get_command_by_identifier(
                "kitchen_chef_seq_1", A_SetSpriteSequence
            )
            cmd.set_index(henchman_animations.kitchen_prep.sequence_id)
        else:
            world.action_scripts.delete_command_by_identifier("kitchen_chef_seq_1")

    if len(henchmen) >= 2:
        second_henchman = henchmen[1]
        henchman_animations = second_henchman.model().animations
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
        (
            "chapel_reload_crying_aq",
            ["chapel_reload_crying"],
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
    a23 = world.event_scripts.get_subscript_command_by_identifier(
        "chapel_reload_crying_aq", "chapel_reload_crying", A_SetSpriteSequence
    )
    update_ally_animation(
        a23, ally, SpriteAnimationState.CRYING_BACKWARDS, use_primary=use_primary
    )

# NPC fills for each ending-cutscene render. Each AllyNPCSub here points at an
# NPC in an ending-cutscene room (e.g. R496, R088) that should be replaced with
# the chosen character's overworld model. These are populated independently of
# the recruitment location's own _npc_fills.
_ENDING_CHARACTER_1_NPC_FILLS: list[AllyNPCSub] = [
    # Protagonist's Mario-NPC slot stays Mario (sprite 0) for Mario protagonist
    # and is cosmetics-remapped to sprite 31 for non-Mario protagonists, so no
    # NPC model swap is needed here.
]

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
# are never applied for Geno. R375 doll lives at NPC_4 (between Geno=NPC_3
# and Bowser=NPC_6) so its palette is engine-assigned implicitly.
_ENDING_CHARACTER_3_DOLL_FILLS: list[AllyNPCSub] = [
    # AllyNPCSub(R496_FACTORY_GROUNDS_FIGHT_WITH_SMITHY_USES_SLEDGE, NPC_23),
    AllyNPCSub(R088_SMITHYS_FINAL_FORM_DEFEAT_GENOS_REDEMPTION, NPC_4),
    AllyNPCSub(R375_ENDING_CREDITS_STAR_PIECES_SHOOT_THROUGH_THE_SKY, NPC_4),
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

# Native (x, y, z, direction) per role in R496. Each role-character's NPC slot
# moves to that role's coord, so the visible character at e.g. Mario's coord is
# always whoever is currently the protagonist.
_R496_COORDS = {
    "protagonist":  (4, 48, 0, SOUTHWEST),
    "marrymore":    (6, 12, 0, SOUTHWEST),
    "mushroom_way": (6, 14, 0, SOUTHWEST),
    "forest_maze":  (6, 16, 0, SOUTHWEST),
    "inner_mines":  (6, 20, 0, SOUTHWEST),
}

# R292 — second-half of the R496 ending cutscene (post-RunStarPieceSequence).
# NPC IDs match R496 exactly so script_3885 references resolve consistently
# across the EnterArea(R292) transition.
R292_NATIVE_SLOT_FOR_PRIZE: dict[type, AreaObject] = {
    MarioRecruitmentPrize:     NPC_19,
    ToadstoolRecruitmentPrize: NPC_20,
    MallowRecruitmentPrize:    NPC_21,
    GenoRecruitmentPrize:      NPC_22,
    BowserRecruitmentPrize:    NPC_24,
}
_R292_COORDS = dict(_R496_COORDS)

# R088 (script_3950 / E3950_POST_FINAL_BOSS_INIT). Bowser moved to last object
# slot (NPC_8); a new GENO_ENDING NPC inserted at NPC_5 anchors palette row 4
# next to the doll at NPC_4.
R88_NATIVE_SLOT_FOR_PRIZE: dict[type, AreaObject] = {
    MarioRecruitmentPrize:     NPC_0,
    ToadstoolRecruitmentPrize: NPC_1,
    MallowRecruitmentPrize:    NPC_3,
    GenoRecruitmentPrize:      NPC_5,
    BowserRecruitmentPrize:    NPC_8,
}
_R88_COORDS = {
    "protagonist":  (5, 90, 0, NORTHWEST),
    "marrymore":    (5, 90, 0, NORTHWEST),
    "mushroom_way": (6, 92, 0, NORTHWEST),
    "inner_mines":  (4, 93, 0, NORTHWEST),
    # forest character is removed before fade-in; coord doesn't matter
}

# R375 (script_3951 / E3951_STAR_PIECE_CREDITS_INIT). Layout reads
# Mario/Peach/Mallow/Geno/Doll/GenoRedemption/Bowser; the doll sits between
# Geno (NPC_3) and Bowser (NPC_6) so its palette is implicitly assigned by
# the engine — see _apply_r375_protagonist_palette_rows.
R375_NATIVE_SLOT_FOR_PRIZE: dict[type, AreaObject] = {
    MarioRecruitmentPrize:     NPC_0,
    ToadstoolRecruitmentPrize: NPC_1,
    MallowRecruitmentPrize:    NPC_2,
    GenoRecruitmentPrize:      NPC_3,
    BowserRecruitmentPrize:    NPC_6,
}
_R375_COORDS = {
    "protagonist":  (5, 91, 0, NORTHWEST),
    "marrymore":    (5, 91, 0, NORTHWEST),
    "mushroom_way": (6, 93, 0, NORTHWEST),
    "inner_mines":  (5, 94, 0, NORTHWEST),
}


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


def _make_protagonist_sprite_31_variant(
    base: NPCBase, directions: VramStore | None = None
) -> NPCBase:
    """Return a copy of `base` with sprite_id set to SPR0031_ALT_PROTAGONIST_1.

    Sprite 31 is the post-cosmetics protagonist sprite; the cosmetics layer
    overwrites sprites 31-37 with the protagonist character's full animation
    set, so any NPC slot using sprite 31 has access to the same animations
    as the protagonist. We use this on the protagonist's native slot when
    the protagonist is not Mario, so the recruit-only sprite at that slot
    is replaced with the full protagonist sprite.

    Pass `directions` (e.g. VramStore.DIR4_ALL_DIRECTIONS) to also override
    the VRAM-store directions; defaults to copying base's existing value.
    """
    return NPCBase(
        sprite_id=SPR0031_ALT_PROTAGONIST_1,
        shadow_size=base.shadow_size,
        acute_axis=base.acute_axis,
        obtuse_axis=base.obtuse_axis,
        height=base.height,
        y_shift=base.y_shift,
        show_shadow=base.show_shadow,
        directions=directions if directions is not None else base.directions,
        min_vram_size=base.min_vram_size,
        priority_0=base.priority_0,
        priority_1=base.priority_1,
        priority_2=base.priority_2,
        cannot_clone=base.cannot_clone,
        extra_palette_source_offset=base.extra_palette_source_offset,
        extra_palette_row_count=base.extra_palette_row_count,
        byte5_bit6=base.byte5_bit6,
        byte5_bit7=base.byte5_bit7,
        byte6_bit2=base.byte6_bit2,
    )


def _swap_room_npc_coords(
    world: GameWorld,
    room_id: int,
    role_slots: "dict[str, AreaObject]",
    coords: "Mapping[str, tuple[int, int, int, Direction]]",
) -> None:
    """Move each role's NPC slot to that role's native (x, y, z, direction)."""
    room = world.rooms._rooms[room_id]
    if room is None:
        return
    for role, slot in role_slots.items():
        c = coords.get(role)
        if c is None:
            continue
        obj = room.get_npc_by_target_id(slot)
        if obj is None:
            continue
        x, y, z, direction = c
        obj.set_x(x)
        obj.set_y(y)
        obj.set_z(z)
        obj.set_direction(direction)


def _apply_overworld_character_sprite_swap(
    world: GameWorld,
    room_id: int,
    slot_for_prize: "dict[type, AreaObject]",
) -> None:
    """Swap the overworld character's NPC slot to sprite 31.

    Cosmetics writes sprite 31-37 with the **overworld character**'s sprite
    data (driven by `world.overworld_character.ally`, which is StartingCharacter1
    by default). Whichever NPC slot belongs to that character — Toadstool's,
    Mallow's, Geno's, or Bowser's — needs to render via sprite 31 so its
    cosmetic data lands. The cutscene "protagonist" role is unrelated; that
    role can be played by any character.

    No-op for Mario, since Mario's slot already uses sprite 0 and cosmetics
    doesn't remap it.

    Also reduces Mario's NPC slot's VRAM-store directions to DIR0_SWSE_NWNE
    when the overworld character isn't Mario, since Mario's slot won't run
    the full DIR4 animation set.
    """
    ally_index = world.overworld_character.ally.index
    if ally_index == 0:
        return  # Mario — no swap needed
    ally_index_to_prize_class: dict[int, type[CharacterPrize]] = {
        1: ToadstoolRecruitmentPrize,
        2: BowserRecruitmentPrize,
        3: GenoRecruitmentPrize,
        4: MallowRecruitmentPrize,
    }
    overworld_prize_class = ally_index_to_prize_class[ally_index]
    overworld_slot = slot_for_prize[overworld_prize_class]
    mario_slot = slot_for_prize[MarioRecruitmentPrize]

    room = world.rooms._rooms[room_id]
    if room is None:
        return
    overworld_obj = room.get_npc_by_target_id(overworld_slot)
    if overworld_obj is not None:
        overworld_obj._npc = _make_protagonist_sprite_31_variant(
            overworld_obj._npc, directions=VramStore.DIR4_ALL_DIRECTIONS
        )
    mario_obj = room.get_npc_by_target_id(mario_slot)
    if mario_obj is not None:
        mario_obj._npc = _swap_npc_directions(
            mario_obj._npc, VramStore.DIR0_SWSE_NWNE
        )


def _swap_npc_directions(base: NPCBase, directions: VramStore) -> NPCBase:
    """Return a copy of `base` with the given VramStore directions value."""
    return NPCBase(
        sprite_id=base.sprite_id,
        shadow_size=base.shadow_size,
        acute_axis=base.acute_axis,
        obtuse_axis=base.obtuse_axis,
        height=base.height,
        y_shift=base.y_shift,
        show_shadow=base.show_shadow,
        directions=directions,
        min_vram_size=base.min_vram_size,
        priority_0=base.priority_0,
        priority_1=base.priority_1,
        priority_2=base.priority_2,
        cannot_clone=base.cannot_clone,
        extra_palette_source_offset=base.extra_palette_source_offset,
        extra_palette_row_count=base.extra_palette_row_count,
        byte5_bit6=base.byte5_bit6,
        byte5_bit7=base.byte5_bit7,
        byte6_bit2=base.byte6_bit2,
    )


def _apply_ending_cutscene_assignments(
    world: GameWorld,
    *,
    marrymore_prize: CharacterPrize,
    mushroom_way_prize: CharacterPrize,
    forest_maze_prize: CharacterPrize,
    inner_mines_prize: CharacterPrize,
    protagonist_prize: CharacterPrize,
) -> None:
    """Per-seed ending-cutscene plumbing for R496/R088/R375.

    For each of the three rooms:
      1. Rebuild the cutscene event script via its `build_contents` factory,
         passing the role NPC slots so script-internal references resolve to
         the right NPC for whichever character now plays each role.
      2. Move each character's NPC slot to its role's native (x, y, z,
         direction) so the cutscene visuals line up.
      3. When the protagonist isn't Mario, swap that NPC's sprite_id to
         sprite 31 and grow its VRAM directions to DIR4_ALL_DIRECTIONS;
         reduce the Mario NPC's directions to DIR0_SWSE_NWNE so its VRAM
         footprint stays compact.

    Per-character "native NPC slot" is the slot that always renders that
    character's model regardless of cutscene role. The slot is moved to a
    role-specific coord so the same slot can play different roles per seed.
    """
    # =========================================================================
    # TOGGLE: bump R292 forest NPC min_vram_size to 1.
    # Set True to apply, False to skip. R496 forest is bumped unconditionally
    # below; this flag only gates the R292 bump (which we currently leave off
    # because R292's cannot_clone budget is tight and the bump can push
    # NPC_24/Bowser into the spinning-stars buffer).
    # =========================================================================
    R292_FOREST_MIN_VRAM_BUMP = True
    # =========================================================================


    rooms = (
        (
            R496_FACTORY_GROUNDS_FIGHT_WITH_SMITHY_USES_SLEDGE,
            R496_NATIVE_SLOT_FOR_PRIZE,
            _R496_COORDS,
            E3885_END_GAME,
            script_3885.build_contents,
            ("marrymore", "mushroom_way", "forest_maze", "inner_mines"),
        ),
        # R292 shares script_3885 with R496 (same E3885_END_GAME). Re-running
        # build_contents is idempotent — the second call overwrites with the
        # same content. The coord-swap and sprite-31 logic must apply to R292
        # too so the post-RunStarPieceSequence half of the cutscene renders
        # correctly after EnterArea(R292).
        (
            R292_UNMAPPED_HOUSE_ROOM,
            R292_NATIVE_SLOT_FOR_PRIZE,
            _R292_COORDS,
            E3885_END_GAME,
            script_3885.build_contents,
            ("marrymore", "mushroom_way", "forest_maze", "inner_mines"),
        ),
        (
            R088_SMITHYS_FINAL_FORM_DEFEAT_GENOS_REDEMPTION,
            R88_NATIVE_SLOT_FOR_PRIZE,
            _R88_COORDS,
            E3950_POST_FINAL_BOSS_INIT,
            script_3950.build_contents,
            ("marrymore", "mushroom_way", "inner_mines"),  # forest is removed in 3950
        ),
        (
            R375_ENDING_CREDITS_STAR_PIECES_SHOOT_THROUGH_THE_SKY,
            R375_NATIVE_SLOT_FOR_PRIZE,
            _R375_COORDS,
            E3951_STAR_PIECE_CREDITS_INIT,
            script_3951.build_contents,
            ("marrymore", "mushroom_way", "inner_mines"),  # forest is removed in 3951
        ),
    )

    for (
        room_id,
        slot_for_prize,
        coords,
        script_id,
        build_contents,
        coord_roles,
    ) in rooms:
        protagonist_slot = slot_for_prize[type(protagonist_prize)]
        marrymore_slot = slot_for_prize[type(marrymore_prize)]
        mway_slot = slot_for_prize[type(mushroom_way_prize)]
        forest_slot = slot_for_prize[type(forest_maze_prize)]
        mines_slot = slot_for_prize[type(inner_mines_prize)]
        mario_slot = slot_for_prize[MarioRecruitmentPrize]

        # 1. Rebuild script and replace contents in-place.
        new_contents = build_contents(
            protagonist=protagonist_slot,
            marrymore=marrymore_slot,
            mway=mway_slot,
            forest=forest_slot,
            mines=mines_slot,
        )
        world.event_scripts.get_script_by_id(script_id).set_contents(new_contents)

        # 2. Coord swap. Compose role → slot only for roles this room cares
        # about; protagonist always gets coord-swapped too.
        full_role_to_slot: dict[str, AreaObject] = {
            "protagonist":  protagonist_slot,
            "marrymore":    marrymore_slot,
            "mushroom_way": mway_slot,
            "forest_maze":  forest_slot,
            "inner_mines":  mines_slot,
        }
        active_role_slots = {
            r: full_role_to_slot[r]
            for r in ("protagonist",) + coord_roles
        }
        _swap_room_npc_coords(world, room_id, active_role_slots, coords)

        # 3. Sprite 31 swap on the OVERWORLD CHARACTER's NPC slot. Cosmetics
        # has written that character's sprite data to sprite 31, so it must
        # be the slot belonging to the overworld character — not whatever
        # the cutscene's protagonist role happens to be (those can differ).
        _apply_overworld_character_sprite_swap(world, room_id, slot_for_prize)

        # 4. Bump min_vram_size on the slot whose role uses sprite_offset alt
        # sprites. Adds one 16-subtile row so the alt sprite molds fit when
        # the base character's sprite is gridplane-only (e.g. Toadstool's
        # sprite 7) and the slot's tilemap allocation would otherwise be 0
        # subtiles per direction.
        #   R496: forest role (spell frames pre-sequence). Always applied.
        #   R292: forest role (victory_pose post-sequence). Gated by toggle.
        #   R088: mines role (shocked_bwd sprite_offset=1) by default.
        #     Special case: if mines is Bowser, his NPC default is already
        #     min_vram_size=1 — bumping is a no-op. Bump the marrymore slot
        #     instead so its sprite_offset=1 frames have headroom too.
        #     Note: the cannot_clone region in R088 is tight; this bump is
        #     only safe because NPC_2 (Sparkle) is now cannot_clone=False,
        #     freeing space that the bump's growth consumes.
        #   R375: no bump (no sprite_offset alts in that cutscene).
        bump_slot: AreaObject | None = None
        if room_id == R496_FACTORY_GROUNDS_FIGHT_WITH_SMITHY_USES_SLEDGE:
            bump_slot = forest_slot
        elif room_id == R292_UNMAPPED_HOUSE_ROOM and R292_FOREST_MIN_VRAM_BUMP:
            bump_slot = forest_slot
        elif room_id == R088_SMITHYS_FINAL_FORM_DEFEAT_GENOS_REDEMPTION:
            if isinstance(inner_mines_prize, BowserRecruitmentPrize):
                bump_slot = marrymore_slot
            else:
                bump_slot = mines_slot

        if bump_slot is not None:
            room = world.rooms._rooms[room_id]
            if room is not None:
                obj = room.get_npc_by_target_id(bump_slot)
                if obj is not None:
                    obj.set_min_vram_size(1)

        # 5. Palette-collision fix (Geno protagonist only, R292 only). The
        # hardcoded Geno doll (NPC_7) carries Geno's palette. When Geno is the
        # overworld protagonist, the doll dedups against the protagonist in
        # R292's OBJ palette-row arrangement, so the star-piece ("glow") palette
        # lands one row off and the spinning stars render with the wrong palette.
        # Swap the doll to a Peach doll: Peach is always present in this
        # cutscene, so this only rearranges existing palette rows (adds no new
        # palette) and restores the row the star piece expects. Only R292 needs
        # it — the spinning stars live in R292's half of the cutscene.
        if room_id == R292_UNMAPPED_HOUSE_ROOM and isinstance(
            world.overworld_character, GenoRecruitmentPrize
        ):
            r292 = world.rooms._rooms[room_id]
            if r292 is not None:
                doll_obj = r292.get_npc_by_target_id(NPC_7)
                if doll_obj is not None:
                    doll_obj._npc = TOADSTOOL_DOLL_NPC


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


def render_ending_character_1(
    world: GameWorld,
    prize: CharacterPrize,
    *,
    protagonist_prize: CharacterPrize | None = None,
) -> None:
    """Apply animation/sprite changes for the protagonist's NPC slot in the
    ending cutscenes (the Mario-NPC slot at the front of R088/R375/R496).

    For Mario protagonist this is a no-op — the script source already hardcodes
    Mario's correct mold (index=23, sprite_offset=2). For non-Mario protagonists
    the cosmetics layer remaps sprite 31 to the protagonist character's full
    sprite, so the LEAN_BACK mold-id refs in script_3885 must come from
    `_sprites_primary` (the protagonist character's full sprite data).
    """
    if isinstance(prize, MarioRecruitmentPrize):
        return
    _apply_ending_character_npc_fills(world, prize, _ENDING_CHARACTER_1_NPC_FILLS)
    ally = prize.ally
    # The protagonist's NPC slot is rendered through sprite 31 = the cosmetics-
    # remapped full protagonist sprite, so always use _sprites_primary here.
    use_primary = isinstance(prize, MarioRecruitmentPrize) or (
        protagonist_prize is not None and prize is protagonist_prize
    )
    a0 = world.event_scripts.get_subscript_command_by_identifier(
        "ending_protag_lean_back_1_aq",
        "ending_protag_lean_back_1",
        A_SetSpriteSequence,
    )
    update_ally_animation(
        a0, ally, SpriteAnimationState.LEAN_BACK, use_primary=use_primary
    )
    a1 = world.event_scripts.get_subscript_command_by_identifier(
        "ending_protag_lean_back_2_aq",
        "ending_protag_lean_back_2",
        A_SetSpriteSequence,
    )
    update_ally_animation(
        a1, ally, SpriteAnimationState.LEAN_BACK, use_primary=use_primary
    )
    a2 = world.event_scripts.get_subscript_command_by_identifier(
        "ending_protag_look_at_doll_aq",
        "ending_protag_look_at_doll",
        A_SetSpriteSequence,
    )
    update_ally_animation(
        a2, ally, SpriteAnimationState.LOOK_AT_DOLL, use_primary=use_primary
    )


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
    # a1 = world.event_scripts.get_subscript_command_by_identifier(
    #     "ending_mway_character_geno_joy_aq",
    #     "ending_mway_character_geno_joy",
    #     A_SetSpriteSequence,
    # )
    # update_ally_animation(
    #     a1, ally, SpriteAnimationState.JOY, use_primary=use_primary
    # )
    a2 = world.event_scripts.get_subscript_command_by_identifier(
        "ending_geno_palette_spell_frame_3_aq",
        "ending_geno_palette_spell_frame_3",
        A_SetSpriteSequence,
    )
    update_ally_animation(
        a2, ally, SpriteAnimationState.SPELL_FRAME_3, use_primary=use_primary
    )
    a3 = world.event_scripts.get_subscript_command_by_identifier(
        "ending_geno_palette_spell_frames_aq",
        "ending_geno_palette_spell_frame_3_",
        A_SetSpriteSequence,
    )
    update_ally_animation(
        a3, ally, SpriteAnimationState.SPELL_FRAME_3, use_primary=use_primary
    )
    a4 = world.event_scripts.get_subscript_command_by_identifier(
        "ending_geno_palette_spell_frames_aq",
        "ending_geno_palette_spell_frame_4",
        A_SetSpriteSequence,
    )
    update_ally_animation(
        a4, ally, SpriteAnimationState.SPELL_FRAME_4, use_primary=use_primary
    )
    a5 = world.event_scripts.get_subscript_command_by_identifier(
        "ending_geno_palette_spell_frames_aq",
        "ending_geno_palette_spell_frame_5",
        A_SetSpriteSequence,
    )
    update_ally_animation(
        a5, ally, SpriteAnimationState.SPELL_FRAME_5, use_primary=use_primary
    )
    a6 = world.event_scripts.get_subscript_command_by_identifier(
        "ending_geno_palette_spell_frames_aq",
        "ending_geno_palette_spell_frame_6",
        A_SetSpriteSequence,
    )
    update_ally_animation(
        a6, ally, SpriteAnimationState.SPELL_FRAME_6, use_primary=use_primary
    )
    a7 = world.event_scripts.get_subscript_command_by_identifier(
        "ending_geno_palette_looks_down_aq",
        "ending_geno_palette_looks_down",
        A_SetSpriteSequence,
    )
    update_ally_animation(
        a7, ally, SpriteAnimationState.LOOKING_DOWN_AWAY, use_primary=use_primary
    )
    a8 = world.event_scripts.get_subscript_command_by_identifier(
        "ending_geno_palette_victory_pose_aq",
        "ending_geno_palette_victory_pose",
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
        a31, ally, SpriteAnimationState.JOY_JUMP, use_primary=use_primary
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
_ENDING_PALETTE_IDS_PROTAGONIST = ("ending_mario_palette", "ending_mario_palette_dark")
_ENDING_PALETTE_IDS_2 = ("ending_mallow_palette", "ending_mallow_palette_dark")
_ENDING_PALETTE_IDS_3 = ("ending_geno_palette", "ending_geno_palette_dark")
_ENDING_PALETTE_IDS_4 = ("ending_bowser_palette", "ending_bowser_palette_dark")
_ENDING_PALETTE_IDS_5 = ("ending_toadstool_palette", "ending_toadstool_palette_dark")


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


# script_3951 (R375 ending credits) per-NPC palette command info. Each tuple is
# (character class, light morph id, dark set id, light palette id, dark palette id).
# Every NPC slot in R375 has a static sprite, so each command's palette content
# is fixed by character — only the target row varies based on the protagonist
# and forest character's identity (see _apply_r375_protagonist_palette_rows).
_R375_CHARACTER_PALETTE_INFO: list[
    tuple[type[CharacterPrize], str, str, int, int]
] = [
    (MarioRecruitmentPrize,
     "ending_mario_palette",     "ending_mario_palette_dark",
     EPAL0084_MARIO_ENDING,      EPAL0163_MARIO_ENDING_DARK),
    (ToadstoolRecruitmentPrize,
     "ending_toadstool_palette", "ending_toadstool_palette_dark",
     EPAL0141_TOADSTOOL_ENDING,  EPAL0164_TOADSTOOL_ENDING_DARK),
    (MallowRecruitmentPrize,
     "ending_mallow_palette",    "ending_mallow_palette_dark",
     EPAL0085_MALLOW_ENDING,     EPAL0166_MALLOW_ENDING_DARK),
    (GenoRecruitmentPrize,
     "ending_geno_palette",      "ending_geno_palette_dark",
     EPAL0086_GENO_ENDING,       EPAL0167_GENO_ENDING_DARK),
    (BowserRecruitmentPrize,
     "ending_bowser_palette",    "ending_bowser_palette_dark",
     EPAL0140_BOWSER_ENDING,     EPAL0165_BOWSER_ENDING_DARK),
]

_R375_DOLL_LIGHT_ID = "ending_doll_palette"
_R375_DOLL_DARK_ID = "ending_doll_palette_dark"

# NPC slot order in R375 with each slot's "kind" used by the row-allocation
# walk. "DOLL" = NPC_4 (palette tracks forest character; Mario doll has its
# own unique palette). "FILLER" = NPC_5 Geno_redemption (non-ally, consumes a
# row but receives no PaletteSet command).
_R375_SLOT_ORDER: list[tuple[int, "type[CharacterPrize] | str"]] = [
    (0, MarioRecruitmentPrize),
    (1, ToadstoolRecruitmentPrize),
    (2, MallowRecruitmentPrize),
    (3, GenoRecruitmentPrize),
    (4, "DOLL"),
    (5, "FILLER"),
    (6, BowserRecruitmentPrize),
]


def _apply_r375_protagonist_palette_rows(
    world: GameWorld, forest_maze_prize: CharacterPrize
) -> None:
    """Assign rows + palette content to script_3951's per-character palette
    commands based on the overworld protagonist and the forest character.

    Walking NPC slots 0–6 in order with a counter starting at NPC_PALETTE_ROW_1:
    the protagonist's NPC takes MARIO_PALETTE without consuming the counter;
    every other unique palette gets the next NPC_PALETTE_ROW. Repeated palettes
    (e.g. a non-Mario doll matching its character) reuse the existing row. The
    Mario doll has a unique palette ID so it always consumes its own row when
    Mario is the forest character; in every other case the doll's palette is
    provided by its character's command, so `ending_doll_palette[/_dark]` are
    deleted from the script.
    """
    proto = world.overworld_character
    is_mario_forest = isinstance(forest_maze_prize, MarioRecruitmentPrize)
    forest_class = type(forest_maze_prize)

    counter = 1
    palette_to_row: dict[str, PaletteRow] = {}

    def _next_npc_row() -> PaletteRow:
        nonlocal counter
        row = PaletteRow(int(NPC_PALETTE_ROW_1) + (counter - 1))
        counter += 1
        return row

    for _slot, kind in _R375_SLOT_ORDER:
        if isinstance(kind, str) and kind == "DOLL":
            if is_mario_forest:
                pal_key = "MARIO_DOLL"
                is_proto_pal = False
            else:
                pal_key = forest_class.__name__
                is_proto_pal = isinstance(proto, forest_class)
        elif isinstance(kind, str) and kind == "FILLER":
            pal_key = "GENO_REDEMPTION"
            is_proto_pal = False
        else:
            assert isinstance(kind, type)
            pal_key = kind.__name__
            is_proto_pal = isinstance(proto, kind)

        if pal_key in palette_to_row:
            continue
        if is_proto_pal:
            palette_to_row[pal_key] = MARIO_PALETTE
        else:
            palette_to_row[pal_key] = _next_npc_row()

    for cls, light_id, dark_id, light_pal, dark_pal in _R375_CHARACTER_PALETTE_INFO:
        row = palette_to_row[cls.__name__]
        light_cmd = world.event_scripts.get_command_by_identifier(
            light_id, PaletteSetMorphs
        )
        light_cmd.set_row(row)
        light_cmd.set_palette_set(light_pal)
        dark_cmd = world.event_scripts.get_command_by_identifier(dark_id, PaletteSet)
        dark_cmd.set_from_row(row)
        dark_cmd.set_to_row(row)
        dark_cmd.set_palette_set_starts_at(dark_pal)

    if is_mario_forest:
        row = palette_to_row["MARIO_DOLL"]
        light_cmd = world.event_scripts.get_command_by_identifier(
            _R375_DOLL_LIGHT_ID, PaletteSetMorphs
        )
        light_cmd.set_row(row)
        light_cmd.set_palette_set(EPAL0084_MARIO_ENDING)
        dark_cmd = world.event_scripts.get_command_by_identifier(
            _R375_DOLL_DARK_ID, PaletteSet
        )
        dark_cmd.set_from_row(row)
        dark_cmd.set_to_row(row)
        dark_cmd.set_palette_set_starts_at(EPAL0163_MARIO_ENDING_DARK)
    else:
        world.event_scripts.delete_command_by_identifier(_R375_DOLL_LIGHT_ID)
        world.event_scripts.delete_command_by_identifier(_R375_DOLL_DARK_ID)


def apply_ending_characters(
    world: GameWorld,
    *,
    mushroom_way_prize: CharacterPrize | None,
    forest_maze_prize: CharacterPrize | None,
    inner_mines_prize: CharacterPrize | None,
    marrymore_prize: CharacterPrize | None,
    substitute_prizes: list[CharacterPrize],
    mario_override: CharacterPrize | None = None,
    protagonist_override: CharacterPrize | None = None,
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
    "ending_mario_palette" pair).

    `mario_override`, when provided, replaces every MarioRecruitmentPrize among
    the named-slot prizes and the substitute pool — but NOT the protagonist —
    with the given prize. This is used when PlayAsStarter is disabled and Mario
    is not the starter: the player plays as Mario in the overworld, so Mario is
    the cutscene protagonist, but Mario is *also* recruited as a battle
    character in one of the named slots. To avoid showing Mario twice, that
    named slot displays the starter instead (the starter is recruited at the
    start and so has no named slot of its own). The protagonist is the literal
    overworld character and is never routed through this override.

    `protagonist_override`, when provided, locks the cutscene protagonist to
    that prize regardless of pool draw. Required because the cutscene script
    targets the protagonist-role NPC for the player-character animations
    (lean back, hold star, etc.) — that NPC must be the slot that belongs to
    the actual overworld character, not whoever happens to be left in the
    pool after filling empty named slots.

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

    # Lock the protagonist to the override (the overworld character). Remove
    # one matching prize from the pool so it doesn't get popped into a named
    # slot, leaving someone else stranded as protagonist.
    locked_protagonist: CharacterPrize | None = None
    if protagonist_override is not None:
        # The protagonist is the literal overworld character (Mario when
        # PlayAsStarter is disabled) and must NOT be routed through
        # `_apply_mario_override`. That override rewrites Mario's *named-slot*
        # appearance into the starter; applying it here would rewrite the Mario
        # protagonist into the starter too, animating the starter in the
        # protagonist role and stranding Mario in his recruitment slot.
        locked_protagonist = protagonist_override
        assert isinstance(locked_protagonist, CharacterPrize)
        for i, sp in enumerate(pool):
            if type(sp) is type(locked_protagonist):
                pool.pop(i)
                break

    random.shuffle(pool)

    for i in empty_indexes:
        if not pool:
            raise RuntimeError(
                "Cannot resolve ending character slots: not enough substitute "
                "prizes to cover every empty named recruitment slot."
            )
        ending_prizes[i] = pool.pop()

    if locked_protagonist is not None:
        protagonist_prize = locked_protagonist
    else:
        if not pool:
            raise RuntimeError(
                "Cannot resolve protagonist for ending cutscene: substitute pool "
                "is empty after filling named slots."
            )
        # Whoever is left in the pool is the protagonist. If somehow more than
        # one character is left, pick one at random.
        protagonist_prize = pool.pop() if len(pool) == 1 else random.choice(pool)

    # Dedupe character types across the 5 final ending slots.
    # `_apply_mario_override` can replace a real Mario prize with the starter
    # character — and if that starter is already present somewhere else (as a
    # real recruit or another starter slot), we end up with two prizes of the
    # same type. The role-to-NPC slot mapping (R{496,292,88,375}_NATIVE_SLOT_FOR_PRIZE)
    # is keyed by prize TYPE, so duplicates collapse two cutscene roles onto
    # the same NPC slot, leaving the missing character type entirely absent
    # from the cutscene.
    #
    # Fix: walk the 5 final prizes; for each duplicate type beyond the first,
    # swap it with a stand-in for whichever character type is currently absent.
    _all_ending_prize_classes: tuple[type[CharacterPrize], ...] = (
        MarioRecruitmentPrize,
        ToadstoolRecruitmentPrize,
        MallowRecruitmentPrize,
        GenoRecruitmentPrize,
        BowserRecruitmentPrize,
    )
    _five_slots: list[CharacterPrize | None] = list(ending_prizes) + [protagonist_prize]
    _present = {type(p) for p in _five_slots if p is not None}
    _missing = [cls for cls in _all_ending_prize_classes if cls not in _present]
    # Process the protagonist slot (position 4) FIRST so its type is locked in
    # _seen — duplicates in named slots (positions 0-3) get replaced instead.
    # Without this protection, `_apply_mario_override` rewriting a real Mario
    # prize into the starter could create a duplicate that gets resolved by
    # replacing the protagonist (since the loop processes indices in order),
    # which silently breaks the protagonist_override lock.
    _seen: set[type] = set()
    if _five_slots[4] is not None:
        _seen.add(type(_five_slots[4]))
    for i in range(4):
        p = _five_slots[i]
        if p is None:
            continue
        t = type(p)
        if t in _seen and _missing:
            stand_in = _missing.pop(0)()
            _five_slots[i] = stand_in
            _seen.add(type(stand_in))
        else:
            _seen.add(t)
    ending_prizes = _five_slots[:4]
    protagonist_prize = _five_slots[4]
    assert protagonist_prize is not None

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
    R496_FORCE_VANILLA_CUTSCENE_ASSIGNMENT = False
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

    # Rebuild scripts 3885/3950/3951 with role NPCs baked in, swap room NPC
    # coords/directions, and apply sprite-31 + VRAM-store overrides. This MUST
    # run before the palette pair / palette-row logic below so the rebuilt
    # script contents (carrying the same identifiers) are what subsequent
    # `get_command_by_identifier` calls operate on.
    _apply_ending_cutscene_assignments(
        world,
        marrymore_prize=p5,
        mushroom_way_prize=p2,
        forest_maze_prize=p3,
        inner_mines_prize=p4,
        protagonist_prize=protagonist_prize,
    )

    _apply_r375_protagonist_palette_rows(world, p3)

    render_ending_character_1(world, protagonist_prize, protagonist_prize=protagonist_prize)
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
    world.event_scripts.delete_subscript_command_by_identifier(
        "seaside_boss_reveal_sequence_0_aq", "seaside_boss_reveal_sequence_0"
    )
    


def render_ship_password_boss(world: GameWorld, prize: BossFightPrize) -> None:
    """Apply animation changes for Ship Password boss fight."""
    if not isinstance(prize, KingCalamariBossFight):
        world.action_scripts.delete_command_by_identifier("password_boss_vanilla_1")
        world.action_scripts.delete_command_by_identifier("password_boss_vanilla_2")
        world.action_scripts.delete_command_by_identifier("password_boss_vanilla_3")
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
        c = world.action_scripts.get_command_by_identifier(
            "ship_boss_idle_sequence_2", A_SetSpriteSequence
        )
        c.set_index(m.animations.ship_chair.sequence_id)
    else:
        world.action_scripts.replace_command_by_identifier(
            "ship_boss_idle_sequence_2", A_FaceSouthwest()
        )
        world.action_scripts.delete_command_by_identifier(
            "ship_boss_idle_sequence_loop_2"
        )
        
# =============================================================================
# Dojo
# =============================================================================



def mario_dojo_challenge(total_duration) -> UsableEventScriptCommand:
    if total_duration <= 45:
        pre_pause = 1
    else:
        pre_pause = 1 + total_duration - 45
    return ActionQueueSync(target=MARIO, subscript=[
            A_FixedFCoordOn(),
            A_SetWalkingSpeed(FAST),
            A_JumpToHeight(height=53, silent=True),
            A_WalkSouthwestSteps(1),
            A_Pause(19),
            A_Pause(pre_pause),
            A_SetSequenceSpeed(NORMAL),
            A_SetSpriteSequence(index=2, sprite_offset=4, is_sequence=True, looping=False),
            A_PlaySound(sound=SO096_SWINGING_FIST, channel=6),
            A_Pause(15),
            A_PlaySound(sound=SO096_SWINGING_FIST, channel=6),
            A_Pause(30)
        ])

def mallow_dojo_challenge(total_duration) -> UsableEventScriptCommand:
    if total_duration <= 45:
        pre_pause = 1
    else:
        pre_pause = 1 + total_duration - 45
    return ActionQueueSync(target=MARIO, subscript=[
            A_FixedFCoordOn(),
            A_SetWalkingSpeed(FAST),
            A_JumpToHeight(height=53, silent=True),
            A_WalkSouthwestSteps(1),
            A_Pause(19),
            A_Pause(pre_pause),
            A_Pause(5),
            A_SetSequenceSpeed(NORMAL),
            A_SetSpriteSequence(index=6, sprite_offset=4, is_sequence=True, looping=False),
            A_Pause(7),
            A_PlaySound(sound=SO096_SWINGING_FIST, channel=6),
            A_Pause(15),
            A_PlaySound(sound=SO096_SWINGING_FIST, channel=6),
            A_Pause(18)
        ])

def geno_dojo_challenge(total_duration) -> UsableEventScriptCommand:
    if total_duration <= 45:
        pre_pause = 1
    else:
        pre_pause = 1 + total_duration - 45
    return ActionQueueSync(target=MARIO, subscript=[
            A_FixedFCoordOn(),
            A_SetWalkingSpeed(FAST),
            A_JumpToHeight(height=53, silent=True),
            A_WalkSouthwestSteps(1),
            A_Pause(19),
            A_Pause(pre_pause),
            A_Pause(19),
            A_SetSequenceSpeed(NORMAL),
            A_SetSpriteSequence(index=0, sprite_offset=5, is_sequence=True, looping=False),
            A_Pause(20),
            A_PlaySound(sound=SO096_SWINGING_FIST, channel=6),
            A_Pause(6)
        ])

def bowser_dojo_challenge(total_duration) -> UsableEventScriptCommand:
    if total_duration <= 45:
        pre_pause = 1
    else:
        pre_pause = 1 + total_duration - 45
    return ActionQueueSync(target=MARIO, subscript=[
            A_FixedFCoordOn(),
            A_SetWalkingSpeed(FAST),
            A_JumpToHeight(height=53, silent=True),
            A_WalkSouthwestSteps(1),
            A_Pause(19),
            A_Pause(pre_pause),
            A_Pause(9),
            A_SetSequenceSpeed(NORMAL),
            A_SetSpriteSequence(index=0, sprite_offset=4, is_sequence=True, looping=False),
            A_Pause(24),
            A_PlaySound(sound=SO096_SWINGING_FIST, channel=6),
            A_Pause(12)
        ])
        

def peach_dojo_challenge(total_duration) -> UsableEventScriptCommand:
    if total_duration <= 45:
        pre_pause = 1
    else:
        pre_pause = 1 + total_duration - 45
    return ActionQueueSync(target=MARIO, subscript=[
            A_FixedFCoordOn(),
            A_SetWalkingSpeed(FAST),
            A_JumpToHeight(height=53, silent=True),
            A_WalkSouthwestSteps(1),
            A_Pause(19),
            A_Pause(pre_pause),
            A_Pause(9),
            A_SetSequenceSpeed(NORMAL),
            A_SetSpriteSequence(index=0, sprite_offset=4, is_sequence=True, looping=False),
            A_Pause(8),
            A_PlaySound(sound=SO096_SWINGING_FIST, channel=6),
            A_Pause(14),
            A_PlaySound(sound=SO096_SWINGING_FIST, channel=6),
            A_Pause(14)
        ])
    
def update_ally_challenge(world: GameWorld, duration: int, id: str):
    if world.overworld_character.ally.index == 0:
        world.event_scripts.replace_command_by_identifier(id, mario_dojo_challenge(duration))
    elif world.overworld_character.ally.index == 1:
        world.event_scripts.replace_command_by_identifier(id, peach_dojo_challenge(duration))
    elif world.overworld_character.ally.index == 2:
        world.event_scripts.replace_command_by_identifier(id, bowser_dojo_challenge(duration))
    elif world.overworld_character.ally.index == 3:
        world.event_scripts.replace_command_by_identifier(id, geno_dojo_challenge(duration))
    elif world.overworld_character.ally.index == 4:
        world.event_scripts.replace_command_by_identifier(id, mallow_dojo_challenge(duration))



def render_dojo_first_fight(world: GameWorld, prize: BossFightPrize) -> None:
    """Apply animation changes for Dojo first fight."""
    m = prize.smallest_npc()
    # Check if prize is a mimic-type boss
    duration = 45
    

    if isinstance(
        prize, (PandoriteBossFight, HidonBossFight, BoxBoyBossFight, ChesterBossFight)
    ):
        cast(
            ActionQueueAsync,
            world.event_scripts.get_command_by_identifier("dojo_boss_1_initiate_aq"),
        ).set_subscript(get_mimic_rise_dojo())
    else:
        if m.animations.dojo_challenge is not None:
            duration = max(45, m.animations.dojo_challenge.total_duration + 12)
            world.event_scripts.get_subscript_command_by_identifier(
                "dojo_boss_1_initiate_aq",
                "dojo_boss_1_initiate",
                A_SetSpriteSequence,
            ).set_index(m.animations.dojo_challenge.sequence_id)
            world.event_scripts.get_subscript_command_by_identifier(
                "dojo_boss_1_initiate_aq", "dojo_boss_1_pause", A_Pause
            ).set_length(duration)
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
        world.event_scripts.get_subscript_command_by_identifier(
            "dojo_boss_1_recoil_aq", "dojo_boss_1_recoil_pause", A_Pause
        ).set_length(m.animations.recoil.total_duration)
    else:
        world.event_scripts.delete_subscript_command_by_identifier(
            "dojo_boss_1_recoil_aq", "dojo_boss_1_recoil"
        )
    world.event_scripts.replace_subscript_command_by_identifier(
        "EVENT_2067_action_queue_0", "jagger_looks_around", A_FaceNorthwest()
    )
    update_ally_challenge(world, duration, "EVENT_2066_player_challenge_aq")


def render_dojo_fight(
    world: GameWorld,
    prize: BossFightPrize,
    initiate_aq_id: str,
    initiate_id: str,
    pause_id: str,
    player_challenge_id: str,
) -> None:
    """Apply animation changes for a generic Dojo fight."""
    m = prize.smallest_npc()

    duration = 45
    if isinstance(
        prize, (PandoriteBossFight, HidonBossFight, BoxBoyBossFight, ChesterBossFight)
    ):
        cast(
            ActionQueueAsync,
            world.event_scripts.get_command_by_identifier(initiate_aq_id),
        ).set_subscript(get_mimic_rise_dojo())
    else:
        if m.animations.dojo_challenge is not None:
            duration = max(45, m.animations.dojo_challenge.total_duration + 12)
            world.event_scripts.get_subscript_command_by_identifier(
                initiate_aq_id,
                initiate_id,
                A_SetSpriteSequence,
            ).set_index(m.animations.dojo_challenge.sequence_id)
            world.event_scripts.get_subscript_command_by_identifier(
                initiate_aq_id, pause_id, A_Pause
            ).set_length(duration)
        else:
            world.event_scripts.get_subscript_command_by_identifier(
                initiate_aq_id,
                initiate_id,
                A_SetSpriteSequence,
            ).set_index(0)    
    update_ally_challenge(world, duration, player_challenge_id) 

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
        world.event_scripts.delete_subscript_command_by_identifier("axem_trampoline_aqueue", "axem_trampoline_loop")
        world.event_scripts.delete_subscript_command_by_identifier("axem_trampoline_aqueue", "axem_trampoline_endloop")
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
    anim = henchman.model().animations.factory_pierce

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
        if anim.total_duration > 55:
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
