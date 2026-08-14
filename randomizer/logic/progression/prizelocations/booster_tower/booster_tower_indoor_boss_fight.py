from __future__ import annotations
from smrpgpatchbuilder.datatypes.overworld_scripts.event_scripts.commands.commands import Pause
from typing import TYPE_CHECKING
from smrpgpatchbuilder.datatypes.overworld_scripts.event_scripts.commands import *
from randomizer.data.variables.room_names import *
from randomizer.data.variables.event_script_names import *
from randomizer.data.variables.action_script_names import *
from randomizer.data.variables.pack_names import *
from randomizer.logic.progression.prizes import *
from randomizer.types.flags import *
from smrpgpatchbuilder.datatypes.overworld_scripts.action_scripts.classes import (ActionScript, UsableActionScriptCommand)
from smrpgpatchbuilder.datatypes.overworld_scripts.action_scripts.commands import (A_FixedFCoordOn)
from smrpgpatchbuilder.datatypes.overworld_scripts.action_scripts.commands.commands import (A_FaceNortheast, A_FaceNorthwest, A_FaceSoutheast, A_FaceSouthwest, A_Jmp, A_Pause, A_ResetProperties, A_ReturnQueue, A_SetBit, A_SetSequenceSpeed, A_SetSpriteSequence, A_ShiftXYPixels, A_ShiftZUpSteps, A_WalkNorthPixels, A_WalkSouthPixels)
from typing import (cast)
from randomizer.logic.progression.prizelocations.access import (boss_slot_min_vram_cap_for_room, can_damage_enemies_with_spells, can_do_tower_curtain_game, not_earlygame, is_early_midgame, is_late_midgame, is_lategame)
from randomizer.logic.progression.prizelocations.marrymore.marrymore_character import MarrymoreCharacter
from randomizer.types.logic import (Inventory)
from randomizer.types.prize import (Prize)
from randomizer.types.prizelocation import (BossFightLocation, BossFightLocationHenchmanNPC, BossFightLocationNPC, ShuffleLocationSelector, WorldAreaEnum)
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.area_objects import (NPC_0, NPC_1, NPC_10, NPC_2, NPC_3, NPC_4, NPC_5, NPC_6, NPC_7, NPC_8, NPC_9)
if TYPE_CHECKING:
    from randomizer.types.gameworld import (GameWorld)


def _marrymore_chapel_boss_min_vram_cap(world: GameWorld) -> int:
    return boss_slot_min_vram_cap_for_room(
        world,
        R154_MARRYMORE_CHAPEL_SANCTUARY_DURING_BOOSTER,
        base_budget=1,
        recruit_location=MarrymoreCharacter,
    )


def _booster_hill_dummy_boss_min_vram_cap(world: GameWorld) -> int:
    return boss_slot_min_vram_cap_for_room(
        world,
        R054_BOOSTER_HILL_DUMMY,
        base_budget=1,
        recruit_location=MarrymoreCharacter,
    )


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

            if m.base.directions == VramStore.DIR2_SWSE:
                a.set_mirror_sprite(not a.mirror_sprite)
        else:
            if m.base.directions != VramStore.DIR2_SWSE:
                if a.mirror_sprite:
                    world.event_scripts.replace_subscript_command_by_identifier(
                        eid, aid, A_FaceNortheast()
                    )
                else:
                    world.event_scripts.replace_subscript_command_by_identifier(
                        eid, aid, A_FaceNorthwest()
                    )
            else:
                world.event_scripts.replace_subscript_command_by_identifier(
                    eid, aid, A_FaceSouthwest()
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
        # a mook henchman fallback - check both sources.
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


class BoosterTowerIndoorBossFight(BossFightLocation):
    _bias = True
    _originally_held = BoosterBossFight
    _rooms = [R192_BOOSTER_TOWER_9F_AREA_02_BOOSTERS_CURTAIN_GAME_ROOM]
    _id = ShuffleLocationSelector.BOOSTER_TOWER_BOSS_1
    _world_area = WorldAreaEnum.BOOSTER_TOWER
    _pack_id = PACK161_TOWER_FIRST_FIGHT
    _post_unlocks_event_id = E1201_TOWER_CURTAIN_BOSS_UNLOCKS
    _henchman_can_run_away = False
    _npc_slots = [
        BossFightLocationNPC(
            R192_BOOSTER_TOWER_9F_AREA_02_BOOSTERS_CURTAIN_GAME_ROOM,
            NPC_0,
            sequence_setter_event_id=E0789_TOWER_CURTAIN_GAME_ROOM_SHUFFLED_NPC_ANIMATION_LOADER,
        ),
        BossFightLocationNPC(
            R154_MARRYMORE_CHAPEL_SANCTUARY_DURING_BOOSTER,
            NPC_9,
            sequence_setter_event_id=E0790_MARRYMORE_OCCUPIED_SANCTUARY_SHUFFLED_NPC_ANIMATION_LOADER,
            # Adaptive cap: ally buffer + Marrymore recruit (NPC_10) compete
            # for VRAM in this room.
            min_vram_size_override=_marrymore_chapel_boss_min_vram_cap,
            min_vram_from_seq0_override=_marrymore_chapel_boss_min_vram_cap,
        ),
        BossFightLocationNPC(
            R294_MARRYMORE_CHAPEL_CLONE_BOSS_LAUNCHER,
            NPC_9,
            sequence_setter_event_id=E0790_MARRYMORE_OCCUPIED_SANCTUARY_SHUFFLED_NPC_ANIMATION_LOADER,
            # Adaptive cap: ally buffer + Marrymore recruit (NPC_10) compete
            # for VRAM in this room.
            min_vram_size_override=_marrymore_chapel_boss_min_vram_cap,
            min_vram_from_seq0_override=_marrymore_chapel_boss_min_vram_cap,
        ),
        BossFightLocationNPC(
            R195_BOOSTER_TOWER_6F_AREA_02_BOOSTERS_ANCESTOR_GAME_ROOM,
            NPC_6,
            sequence_setter_event_id=E0791_TOWER_ANCESTOR_GAME_ROOM_SHUFFLED_NPC_ANIMATION_LOADER,
        ),
        BossFightLocationNPC(
            R193_BOOSTER_TOWER_2F_AREA_03_STEPS_WCIRCLING_BOBOMBS,
            NPC_6,
            sequence_setter_event_id=E0792_TOWER_FIRST_BOBOMB_STAIRCASE_SHUFFLED_NPC_ANIMATION_LOADER,
        ),
        BossFightLocationNPC(
            R054_BOOSTER_HILL_DUMMY,
            NPC_7,
            # Adaptive cap: ally buffer + Marrymore recruit (NPC_8) compete
            # for VRAM in this room.
            min_vram_size_override=_booster_hill_dummy_boss_min_vram_cap,
            min_vram_from_seq0_override=_booster_hill_dummy_boss_min_vram_cap,
        ),
        BossFightLocationNPC(
            R202_BOOSTER_TOWER_ENTRANCE,
            NPC_1,
            sequence_setter_event_id=E0878_TOWER_EXTERIOR_SHUFFLED_NPC_ANIMATION_LOADER,
        ),
        BossFightLocationNPC(
            R043_BOOSTER_TOWER_1F_AREA_01_MAIN_ROOM,
            NPC_3,
            sequence_setter_event_id=E0797_TOWER_LOBBY_SHUFFLED_NPC_ANIMATION_LOADER,
        ),
        BossFightLocationNPC(
            R258_BOOSTER_TOWER_BALCONY_AT_TOP_FLOOR,
            NPC_3,
            sequence_setter_event_id=E0794_TOWER_BALCONY_SHUFFLED_NPC_ANIMATION_LOADER,
        ),
        BossFightLocationNPC(
            R506_ENDING_CREDITS_MARRYMORE_CHAPEL_BOOSTER_WEDDING_VALENTINA,
            NPC_10,
            sequence_setter_event_id=E0795_ENDING_CREDITS_CHAPEL_SHUFFLED_NPC_ANIMATION_LOADER,
        ),
    ]
    _character_henchman_slots = [
        BossFightLocationHenchmanNPC(
            [
                R043_BOOSTER_TOWER_1F_AREA_01_MAIN_ROOM,
                R192_BOOSTER_TOWER_9F_AREA_02_BOOSTERS_CURTAIN_GAME_ROOM,
                R154_MARRYMORE_CHAPEL_SANCTUARY_DURING_BOOSTER,
                R054_BOOSTER_HILL_DUMMY,
                R258_BOOSTER_TOWER_BALCONY_AT_TOP_FLOOR,
                R506_ENDING_CREDITS_MARRYMORE_CHAPEL_BOOSTER_WEDDING_VALENTINA,
            ],
            [NPC_4, NPC_1, NPC_0, NPC_3, NPC_0, NPC_2],
            PACK000_TOWER_HENCHMAN_1,
            skip_swap_if_flag=KeepMinigameSpritesIntact,
            container_event=E0053_HENCHMAN_CONTAINER_3,
        ),
        BossFightLocationHenchmanNPC(
            [
                R194_BOOSTER_TOWER_2F_AREA_02_BOOSTERS_RAILWAY_ROOM,
                R192_BOOSTER_TOWER_9F_AREA_02_BOOSTERS_CURTAIN_GAME_ROOM,
                R154_MARRYMORE_CHAPEL_SANCTUARY_DURING_BOOSTER,
                R054_BOOSTER_HILL_DUMMY,
                R258_BOOSTER_TOWER_BALCONY_AT_TOP_FLOOR,
                R506_ENDING_CREDITS_MARRYMORE_CHAPEL_BOOSTER_WEDDING_VALENTINA,
            ],
            [NPC_0, NPC_2, NPC_1, NPC_4, NPC_1, NPC_1],
            PACK001_TOWER_HENCHMAN_2,
            skip_swap_if_flag=KeepMinigameSpritesIntact,
            container_event=E0054_HENCHMAN_CONTAINER_4,
        ),
        BossFightLocationHenchmanNPC(
            [
                R037_BOOSTER_TOWER_4F_3LEVEL_ROOM_WJUMPING_SPOOKUMS,
                R192_BOOSTER_TOWER_9F_AREA_02_BOOSTERS_CURTAIN_GAME_ROOM,
                R154_MARRYMORE_CHAPEL_SANCTUARY_DURING_BOOSTER,
                R054_BOOSTER_HILL_DUMMY,
                R258_BOOSTER_TOWER_BALCONY_AT_TOP_FLOOR,
                R506_ENDING_CREDITS_MARRYMORE_CHAPEL_BOOSTER_WEDDING_VALENTINA,
            ],
            [NPC_8, NPC_3, NPC_2, NPC_5, NPC_2, NPC_3],
            PACK054_TOWER_HENCHMAN_3,
            skip_swap_if_flag=KeepMinigameSpritesIntact,
            container_event=E0055_HENCHMAN_CONTAINER_5,
        ),
        BossFightLocationHenchmanNPC(
            [R506_ENDING_CREDITS_MARRYMORE_CHAPEL_BOOSTER_WEDDING_VALENTINA], [NPC_4]
        ),
        BossFightLocationHenchmanNPC(
            [R506_ENDING_CREDITS_MARRYMORE_CHAPEL_BOOSTER_WEDDING_VALENTINA], [NPC_5]
        ),
        BossFightLocationHenchmanNPC(
            [R506_ENDING_CREDITS_MARRYMORE_CHAPEL_BOOSTER_WEDDING_VALENTINA], [NPC_6]
        ),
        BossFightLocationHenchmanNPC(
            [R506_ENDING_CREDITS_MARRYMORE_CHAPEL_BOOSTER_WEDDING_VALENTINA], [NPC_7]
        ),
        BossFightLocationHenchmanNPC(
            [R506_ENDING_CREDITS_MARRYMORE_CHAPEL_BOOSTER_WEDDING_VALENTINA], [NPC_8]
        ),
    ]
    _mook_henchman_slots = [
        BossFightLocationHenchmanNPC(
            [R405_BOOSTER_PASS_SECRET],
            [NPC_9],
            PACK032_TOWER_PASS_HENCHMAN,
            skip_swap_if_flag=KeepMinigameSpritesIntact,
        )
    ]
    _dialogs_expecting_replacement = [
        DI2503_NEED_X_MORE_ITEMS_MARRYMORE,
        DI2560_TOWER_HENCHMAN_1,
        DI2572_TOWER_HENCHMAN_2,
        DI3072_TOWER_HENCHMAN_3_WINDOW,
        DI3073_TOWER_HENCHMAN_3,
        DI4060_NEED_TO_DO_CHAPEL_CHECKS,
    ]

    def can_accept(self, prize: Prize, inventory: Inventory, world: GameWorld) -> bool:
        return super().can_accept(prize, inventory, world) and (
            can_damage_enemies_with_spells(world, inventory)
            or not isinstance(prize, MokuraBossFight)
        )

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_do_tower_curtain_game(world, inventory) and not_earlygame(
            world, inventory
        )

    def render(self, world: GameWorld):
        op = super().render(world)
        if self.npc_slots and self.prize and self.prize.model:
            assert isinstance(self.prize, BossFightPrize)
            is_vanilla = isinstance(
                self.prize, (self._originally_held, Booster2BossFight)
            )

            # Check if character henchman slots are assigned (KeepMinigameSpritesIntact not set)
            keep_minigame_sprites = world.settings.isflag_enabled(
                KeepMinigameSpritesIntact
            )
            character_henchmen_assigned = not keep_minigame_sprites and (
                (
                    self.prize.character_henchmen is not None
                    and len(self.prize.character_henchmen) >= 3
                )
                or (
                    self.prize.mook_henchmen is not None
                    and len(self.prize.mook_henchmen) > 0
                )
            )

            render_booster_tower_indoor_boss(
                world,
                self.prize,
                self.npc_slots,
                is_vanilla,
                character_henchmen_assigned,
            )
            if character_henchmen_assigned:
                char_count = (
                    len(self.prize.character_henchmen)
                    if self.prize.character_henchmen
                    else 0
                )
                has_mook_fallback = (
                    char_count < 3
                    and self.prize.mook_henchmen is not None
                    and len(self.prize.mook_henchmen) > 0
                )
                effective_count = 3 if has_mook_fallback else char_count
                if not is_vanilla:
                    render_booster_tower_henchman_scripts(
                        world,
                        self.prize,
                        effective_count,
                    )

            # Only if mook henchman slot is assigned
            mook_henchmen_assigned = (
                not keep_minigame_sprites
                and self.prize.mook_henchmen is not None
                and len(self.prize.mook_henchmen) > 0
            )

        return op


__all__ = ["BoosterTowerIndoorBossFight"]
