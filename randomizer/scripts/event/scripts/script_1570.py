# pylint: disable=C0301

"""E1570_MIDAS_RIVER_FISH"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        CopyVarToVar(from_var=TEMP_702A, to_var=PRIMARY_TEMP_7000),
        CopyVarToVar(from_var=PRIMARY_TEMP_7000, to_var=TEMP_7034),
        SetBit(TEMP_7044_2),
        DisableObjectTrigger(NPC_0),
        StartSyncEmbeddedActionScript(
            target=NPC_0,
            prefix=0xF1,
            subscript=[
                ASSetSpriteSequence(index=0, is_sequence=True, looping=True),
                ASJumpToHeight(48),
                ASSetWalkingSpeed(FAST),
                ASWalk1StepWest(),
                ASVisibilityOff(),
            ],
        ),
        CopyVarToVar(from_var=TEMP_7028, to_var=PRIMARY_TEMP_7000),
        CopyVarToVar(from_var=PRIMARY_TEMP_7000, to_var=ACTIVE_NPC),
        PauseActionScript(MEM_70A8),
        PauseActionScript(MARIO),
        PauseActionScript(SCREEN_FOCUS),
        ActionQueueSync(
            target=MARIO,
            subscript=[
                ASSetSpriteSequence(
                    index=0, sprite_offset=3, is_sequence=True, looping=True
                ),
                ASFloatingOff(),
                ASJumpToHeight(height=72, silent=True),
                ASCopyVarToVar(from_var=TEMP_7034, to_var=PRIMARY_TEMP_700C),
                ASJmpIfVarEqualsConst(
                    PRIMARY_TEMP_700C,
                    0,
                    ["EVENT_1570_action_queue_sync_10_SUBSCRIPT_play_sound_8"],
                ),
                ASPlaySound(sound=SO055_LOSE_COINS_COIN_FOUNTAIN, channel=4),
                ASPause(8),
                ASJmp(["EVENT_1570_action_queue_sync_11"]),
                ASPlaySound(
                    sound=SO022_CLOSE_DOOR,
                    channel=4,
                    identifier="EVENT_1570_action_queue_sync_10_SUBSCRIPT_play_sound_8",
                ),
                ASPause(8),
            ],
        ),
        ActionQueueSync(
            target=SCREEN_FOCUS,
            subscript=[
                ASSetWalkingSpeed(VERY_FAST),
                ASWalkSouthPixels(4),
                ASWalkNorthPixels(8),
                ASWalkSouthPixels(8),
                ASWalkNorthPixels(8),
                ASWalkSouthPixels(4),
                ASSetWalkingSpeed(FAST),
            ],
            identifier="EVENT_1570_action_queue_sync_11",
        ),
        SetVarToConst(PRIMARY_TEMP_700C, 5),
        StartLoopNTimes(4),
        CopyVarToVar(from_var=TEMP_702A, to_var=PRIMARY_TEMP_7000),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 0, ["EVENT_1570_pause_18"]),
        CreatePacketAtObjectCoords(
            packet=P017_SMALL_MINIGAME_COIN,
            target_npc=MARIO,
            destinations=["EVENT_1570_pause_18"],
        ),
        Dec(TEMP_702A),
        Pause(1, identifier="EVENT_1570_pause_18"),
        Inc(PRIMARY_TEMP_700C),
        EndLoop(),
        Pause(3),
        ActionQueueAsync(target=MARIO, subscript=[ASResetProperties()]),
        ResumeActionScript(MEM_70A8),
        ResumeActionScript(MARIO),
        ResumeActionScript(SCREEN_FOCUS),
        ClearBit(TEMP_7044_2),
        Return(),
    ]
)
