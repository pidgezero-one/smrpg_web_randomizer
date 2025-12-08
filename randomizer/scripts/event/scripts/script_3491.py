# pylint: disable=C0301

"""E3491_MIDAS_RIVER_TOP_TUNNEL_ANIMATION_AND_EXIT"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        FadeInFromBlack(sync=True),
        FreezeCamera(),
        SetSyncActionScript(MARIO, A0598_MIDAS_RIVER_TOP_TUNNEL_PLAYER_OUTER),
        ActionQueueSync(
            target=SCREEN_FOCUS,
            subscript=[
                ASSetWalkingSpeed(SLOW),
                ASWalkEastSteps(8),
                ASSetWalkingSpeed(NORMAL),
            ]),
        JmpToSubroutine(["EVENT_3491_action_queue_sync_16"]),
        EnterArea(
            room_id=R069_MIDAS_RIVER_WATERFALL, face_direction=SOUTH, x=8, y=31, z=0
        ),
        FadeOutMusicToVolume(duration=1, volume=56),
        PlaySound(sound=SO035_RUNNING_WATER, channel=4),
        ActionQueueAsync(target=MARIO, subscript=[ASVisibilityOff()]),
        FadeInFromBlack(sync=False),
        ActionQueueAsync(
            target=MARIO,
            subscript=[
                ASClearSolidityBits(cant_pass_walls=True),
                ASWalkToXYCoords(x=12, y=29),
                ASSetVarToConst(X_COORD_2, 6528),
                ASSetVarToConst(Y_COORD_2, 3712),
                ASTransferTo70167018(),
            ]),
        JmpToSubroutine(["EVENT_3480_action_queue_async_73"]),
        ActionQueueAsync(
            target=MARIO,
            subscript=[
                ASPlaySound(sound=SO033_JUMPING_BOUNCING_FISH, channel=4),
                ASSetWalkingSpeed(SLOW),
                ASShiftSouthSteps(8),
                ASDb(bytearray(b" \x04")),
                ASDb(bytearray(b"%\x80\x02\xf4\xff")),
                ASSetWalkingSpeed(NORMAL),
                ASPlaySound(sound=SO010_TRAMPOLINE, channel=4),
                ASWalkNorthwestSteps(7),
                ASWalk1StepSouthwest(),
                ASBPL262728(),
                ASSetSolidityBits(cant_pass_walls=True),
            ]),
        SetSyncActionScript(MARIO, A0466_MIDAS_RIVER_TUNNEL_LEAVE),
        Jmp(["EVENT_3489_enable_controls_3"]),
        Return(),
        ActionQueueSync(
            target=MARIO,
            subscript=[
                ASSetSpriteSequence(
                    index=10, sprite_offset=1, is_sequence=True, looping=True
                )
            ],
            identifier="EVENT_3491_action_queue_sync_16"),
        StartLoopNTimes(2, identifier="EVENT_3491_start_loop_n_times_17"),
        Pause(1),
        JmpIfBitSet(TEMP_7043_0, ["EVENT_3491_fade_out_to_black_async_duration_65"]),
        JmpIfBitSet(MIDAS_RIVER_TUNNEL_1_BIT, ["EVENT_3491_start_loop_n_times_17"]),
        EndLoop(),
        ActionQueueSync(
            target=MARIO,
            subscript=[
                ASSetSpriteSequence(
                    index=13, sprite_offset=1, is_sequence=True, looping=True
                )
            ]),
        StartLoopNTimes(2, identifier="EVENT_3491_start_loop_n_times_23"),
        Pause(1),
        JmpIfBitSet(TEMP_7043_0, ["EVENT_3491_fade_out_to_black_async_duration_65"]),
        JmpIfBitSet(MIDAS_RIVER_TUNNEL_1_BIT, ["EVENT_3491_start_loop_n_times_23"]),
        EndLoop(),
        ActionQueueSync(
            target=MARIO,
            subscript=[
                ASSetSpriteSequence(
                    index=12, sprite_offset=1, is_sequence=True, looping=True
                )
            ]),
        StartLoopNTimes(2, identifier="EVENT_3491_start_loop_n_times_29"),
        Pause(1),
        JmpIfBitSet(TEMP_7043_0, ["EVENT_3491_fade_out_to_black_async_duration_65"]),
        JmpIfBitSet(MIDAS_RIVER_TUNNEL_1_BIT, ["EVENT_3491_start_loop_n_times_29"]),
        EndLoop(),
        ActionQueueSync(
            target=MARIO,
            subscript=[
                ASSetSpriteSequence(
                    index=14, sprite_offset=1, is_sequence=True, looping=True
                )
            ]),
        StartLoopNTimes(2, identifier="EVENT_3491_start_loop_n_times_35"),
        Pause(1),
        JmpIfBitSet(TEMP_7043_0, ["EVENT_3491_fade_out_to_black_async_duration_65"]),
        JmpIfBitSet(MIDAS_RIVER_TUNNEL_1_BIT, ["EVENT_3491_start_loop_n_times_35"]),
        EndLoop(),
        ActionQueueSync(
            target=MARIO,
            subscript=[
                ASSetSpriteSequence(
                    index=11, sprite_offset=1, is_sequence=True, looping=True
                )
            ]),
        StartLoopNTimes(2, identifier="EVENT_3491_start_loop_n_times_41"),
        Pause(1),
        JmpIfBitSet(TEMP_7043_0, ["EVENT_3491_fade_out_to_black_async_duration_65"]),
        JmpIfBitSet(MIDAS_RIVER_TUNNEL_1_BIT, ["EVENT_3491_start_loop_n_times_41"]),
        EndLoop(),
        ActionQueueSync(
            target=MARIO,
            subscript=[
                ASSetSpriteSequence(
                    index=14,
                    sprite_offset=1,
                    is_sequence=True,
                    looping=True,
                    mirror_sprite=True)
            ]),
        StartLoopNTimes(2, identifier="EVENT_3491_start_loop_n_times_47"),
        Pause(1),
        JmpIfBitSet(TEMP_7043_0, ["EVENT_3491_fade_out_to_black_async_duration_65"]),
        JmpIfBitSet(MIDAS_RIVER_TUNNEL_1_BIT, ["EVENT_3491_start_loop_n_times_47"]),
        EndLoop(),
        ActionQueueSync(
            target=MARIO,
            subscript=[
                ASSetSpriteSequence(
                    index=12,
                    sprite_offset=1,
                    is_sequence=True,
                    looping=True,
                    mirror_sprite=True)
            ]),
        StartLoopNTimes(2, identifier="EVENT_3491_start_loop_n_times_53"),
        Pause(1),
        JmpIfBitSet(TEMP_7043_0, ["EVENT_3491_fade_out_to_black_async_duration_65"]),
        JmpIfBitSet(MIDAS_RIVER_TUNNEL_1_BIT, ["EVENT_3491_start_loop_n_times_53"]),
        EndLoop(),
        ActionQueueSync(
            target=MARIO,
            subscript=[
                ASSetSpriteSequence(
                    index=13,
                    sprite_offset=1,
                    is_sequence=True,
                    looping=True,
                    mirror_sprite=True)
            ]),
        StartLoopNTimes(2, identifier="EVENT_3491_start_loop_n_times_59"),
        Pause(1),
        JmpIfBitSet(TEMP_7043_0, ["EVENT_3491_fade_out_to_black_async_duration_65"]),
        JmpIfBitSet(MIDAS_RIVER_TUNNEL_1_BIT, ["EVENT_3491_start_loop_n_times_59"]),
        EndLoop(),
        Jmp(["EVENT_3491_action_queue_sync_16"]),
        FadeOutToBlack(
            sync=False,
            duration=32,
            identifier="EVENT_3491_fade_out_to_black_async_duration_65"),
        Return(),
    ]
)
