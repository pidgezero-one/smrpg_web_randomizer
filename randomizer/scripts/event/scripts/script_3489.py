# pylint: disable=C0301

"""E3489_MIDAS_RIVER_WATERFALL_LISTEN_FOR_BUTTON_INPUTS"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        SetVarToConst(TEMP_702A, 0),
        JmpIfBitSet(UNKNOWN_MIDAS_RIVER_7079_0, ["EVENT_3489_enable_controls_3"]),
        SetVarToConst(MIDAS_RIVER_70D4, 0),
        EnableControls(
            [LEFT, RIGHT, DOWN, UP, X, A, Y, B],
            identifier="EVENT_3489_enable_controls_3"),
        EnableControlsUntilReturn([]),
        RunBackgroundEvent(
            event_id=E3490_MIDAS_SMALL_MARIO_COORD_CALC, return_on_level_exit=True
        ),
        RunBackgroundEvent(
            event_id=E3481_MIDAS_RIVER_TUNNEL_WARP_CHECK,
            return_on_level_exit=True,
            bit_6=True),
        MoveScriptToBackgroundThread2(),
        JmpIfBitSet(
            TEMP_7043_0,
            ["EVENT_3489_fade_out_to_black_async_duration_51"],
            identifier="EVENT_3489_jmp_if_bit_set_8"),
        EnableControlsUntilReturn([]),
        Pause(1),
        Set7000ToTappedButton(),
        JmpIf7000AnyBitsSet(
            bits=[], destinations=["EVENT_3489_enable_controls_until_return_25"]
        ),
        EnableControlsUntilReturn([LEFT, RIGHT]),
        Pause(1),
        Set7000ToTappedButton(),
        JmpIf7000AnyBitsSet(
            bits=[], destinations=["EVENT_3489_enable_controls_until_return_25"]
        ),
        Set7000ToPressedButton(),
        JmpIf7000AnyBitsSet(bits=[], destinations=["EVENT_3489_action_queue_sync_21"]),
        JmpIf7000AnyBitsSet(bits=[], destinations=["EVENT_3489_action_queue_sync_23"]),
        Jmp(["EVENT_3489_jmp_if_bit_set_8"]),
        ActionQueueSync(
            target=NPC_1,
            subscript=[ASFaceWest()],
            identifier="EVENT_3489_action_queue_sync_21"),
        Jmp(["EVENT_3489_jmp_if_bit_set_8"]),
        ActionQueueSync(
            target=NPC_1,
            subscript=[ASFaceEast()],
            identifier="EVENT_3489_action_queue_sync_23"),
        Jmp(["EVENT_3489_jmp_if_bit_set_8"]),
        EnableControlsUntilReturn(
            [], identifier="EVENT_3489_enable_controls_until_return_25"
        ),
        PauseActionScript(MARIO),
        ActionQueueSync(
            target=NPC_1,
            subscript=[ASSetSpriteSequence(index=4, is_sequence=True, looping=True)]),
        SetVarToConst(SECONDARY_TEMP_7024, 0),
        EnableControlsUntilReturn(
            [], identifier="EVENT_3489_enable_controls_until_return_29"
        ),
        ActionQueueAsync(
            target=MARIO,
            subscript=[
                ASPlaySound(sound=SO034_SQUIRM_WRITHE, channel=4),
                ASSetWalkingSpeed(FASTER),
                ASWalkNorthPixels(3),
                ASSetWalkingSpeed(SLOW),
            ]),
        Inc(SECONDARY_TEMP_7024),
        JmpIfVarEqualsConst(
            SECONDARY_TEMP_7024, 5, ["EVENT_3489_enable_controls_until_return_44"]
        ),
        StartLoopNTimes(9),
        SetTempSyncActionScript(MARIO, A0465_PAUSE_SCRIPT_FOR_2_FRAMES),
        EnableControlsUntilReturn([]),
        Pause(1),
        Set7000ToTappedButton(),
        JmpIf7000AnyBitsSet(
            bits=[], destinations=["EVENT_3489_enable_controls_until_return_29"]
        ),
        EnableControlsUntilReturn([LEFT, RIGHT]),
        Pause(1),
        Set7000ToTappedButton(),
        JmpIf7000AnyBitsSet(
            bits=[], destinations=["EVENT_3489_enable_controls_until_return_29"]
        ),
        EndLoop(),
        EnableControlsUntilReturn(
            [], identifier="EVENT_3489_enable_controls_until_return_44"
        ),
        SetObjectMemoryToVar(SECONDARY_TEMP_7024),
        ActionQueueSync(target=NPC_1, subscript=[ASResetProperties()]),
        ActionQueueAsync(
            target=MARIO,
            subscript=[
                ASSetWalkingSpeed(FASTER),
                ASWalkSouthPixels(3),
                ASSetWalkingSpeed(SLOW),
            ]),
        EndLoop(),
        ResumeActionScript(MARIO),
        Jmp(["EVENT_3489_jmp_if_bit_set_8"]),
        FadeOutToBlack(
            sync=False,
            duration=30,
            identifier="EVENT_3489_fade_out_to_black_async_duration_51"),
        StopSound(),
        EnableControls([]),
        EnterArea(
            room_id=R068_MIDAS_RIVER_BARREL_JUMPING_RIVER,
            face_direction=SOUTHWEST,
            x=13,
            y=16,
            z=3,
            run_entrance_event=True),
        Return(),
    ]
)
