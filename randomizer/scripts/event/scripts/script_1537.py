# E1537_SPINNING_FLOWER_CORE_LOGIC

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        JmpIfBitClear(SPINNING_FLOWER_1, ["EVENT_1537_set_bit_2"]),
        Return(),
        SetBit(SPINNING_FLOWER_1, identifier="EVENT_1537_set_bit_2"),
        MoveScriptToBackgroundThread2(),
        CopyVarToVar(from_var=X_COORD_2, to_var=Y_COORD_2),
        VarShiftLeft(X_COORD_2, 8),
        SetAsyncActionScript(MARIO, A0781_PLAYER_SPINS_ON_FLOWER),
        SetVarToConst(TEMP_70AE, 0),
        PlaySound(
            sound=SO031_SPINNING_FLOWER, channel=6, identifier="EVENT_1537_play_sound_8"
        ),
        StartLoopNTimes(15),
        Pause(1),
        Set7000ToTappedButton(),
        JmpIf7000AnyBitsSet(destinations=["EVENT_1537_set_action_script_async_18"]),
        EndLoop(),
        ActionQueueSync(target=MARIO, subscript=[ASTurnClockwise45DegreesNTimes(1)]),
        Inc(TEMP_70AE),
        JmpIfVarEqualsConst(TEMP_70AE, 40, ["EVENT_1537_set_action_script_sync_23"]),
        Jmp(["EVENT_1537_play_sound_8"]),
        SetAsyncActionScript(
            MARIO,
            A0820_JUMP_OFF_SPINNING_FLOWER,
            identifier="EVENT_1537_set_action_script_async_18",
        ),
        ClearBit(SPINNING_FLOWER_1),
        ClearBit(SPINNING_FLOWER_2),
        MoveScriptToMainThread(),
        Return(),
        SetSyncActionScript(
            MARIO,
            A0165_FALL_OFF_SPINNING_FLOWER,
            identifier="EVENT_1537_set_action_script_sync_23",
        ),
        ActionQueueAsync(
            target=MARIO,
            subscript=[
                ASFixedFCoordOff(),
                ASTurnClockwise45DegreesNTimes(1),
                ASFixedFCoordOn(),
            ],
            identifier="EVENT_1537_action_queue_async_24",
        ),
        Pause(6),
        JmpIfObjectActionScriptIsRunning(MARIO, ["EVENT_1537_action_queue_async_24"]),
        ActionQueueAsync(
            target=MARIO,
            subscript=[
                ASSequencePlaybackOn(),
                ASFixedFCoordOff(),
                ASSetWalkingSpeed(NORMAL),
                ASSetSpriteSequence(
                    index=7, sprite_offset=2, is_sequence=True, looping=True
                ),
                ASPause(40),
                ASPlaySound(sound=SO022_CLOSE_DOOR, channel=4),
                ASSetSpriteSequence(
                    index=8, sprite_offset=2, is_sequence=True, looping=True
                ),
            ],
        ),
        Pause(1, identifier="EVENT_1537_pause_28"),
        Set7000ToTappedButton(),
        JmpIf7000AnyBitsSet(destinations=["EVENT_1537_action_queue_sync_32"]),
        Jmp(["EVENT_1537_pause_28"]),
        ActionQueueSync(
            target=MARIO,
            subscript=[ASResetProperties(), ASFaceSouth(), ASJumpToHeight(108)],
            identifier="EVENT_1537_action_queue_sync_32",
        ),
        ClearBit(SPINNING_FLOWER_1),
        ClearBit(SPINNING_FLOWER_2),
        MoveScriptToMainThread(),
        Return(),
    ]
)
