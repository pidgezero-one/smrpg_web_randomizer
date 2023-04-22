# pylint: disable=C0301

"""E3496_MIDAS_RIVER_MID_RIGHT_TUNNEL_ANIMATION_AND_EXIT_BACKGROUND"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        CopyVarToVar(from_var=TEMP_702A, to_var=PRIMARY_TEMP_7000),
        CopyVarToVar(from_var=PRIMARY_TEMP_7000, to_var=TEMP_7034),
        Pause(1, identifier="EVENT_3496_pause_2"),
        JmpIfBitClear(MIDAS_RIVER_TUNNEL_1_BIT, ["EVENT_3496_pause_2"]),
        Pause(3),
        PauseActionScript(SCREEN_FOCUS),
        PauseActionScript(MARIO),
        ActionQueueSync(
            target=SCREEN_FOCUS,
            subscript=[
                ASSetWalkingSpeed(VERY_FAST),
                ASWalkSouthPixels(4),
                ASWalkNorthPixels(8),
                ASWalkSouthPixels(8),
                ASWalkNorthPixels(8),
                ASWalkSouthPixels(4),
                ASSetWalkingSpeed(SLOW),
                ASJmpIfVarEqualsConst(TEMP_7034, 0, ["EVENT_3496_action_queue_sync_8"]),
                ASPlaySound(sound=SO055_LOSE_COINS_COIN_FOUNTAIN, channel=6),
            ],
        ),
        ActionQueueSync(
            target=MARIO,
            subscript=[
                ASPlaySound(sound=SO065_THWOMP_STOMP, channel=4),
                ASSetSpriteSequence(
                    index=0,
                    sprite_offset=3,
                    is_sequence=True,
                    looping=True,
                    mirror_sprite=True,
                ),
                ASJumpToHeight(height=144, silent=True),
            ],
            identifier="EVENT_3496_action_queue_sync_8",
        ),
        SetVarToConst(PRIMARY_TEMP_700C, 0),
        StartLoopNTimes(7),
        CopyVarToVar(from_var=TEMP_702A, to_var=PRIMARY_TEMP_7000),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 0, ["EVENT_3496_pause_15"]),
        CreatePacketAtObjectCoords(
            packet=P017_SMALL_MINIGAME_COIN,
            target_npc=MARIO,
            destinations=["EVENT_3496_pause_15"],
        ),
        Dec(TEMP_702A),
        Pause(1, identifier="EVENT_3496_pause_15"),
        Inc(PRIMARY_TEMP_700C),
        EndLoop(),
        Pause(1, identifier="EVENT_3496_pause_18"),
        JmpIfMarioInAir(["EVENT_3496_pause_18"]),
        ActionQueueAsync(
            target=MARIO,
            subscript=[
                ASSetSpriteSequence(index=5, sprite_offset=3, looping=False),
                ASPause(4),
                ASSetSpriteSequence(
                    index=10, sprite_offset=1, is_sequence=True, looping=True
                ),
            ],
        ),
        ResumeActionScript(SCREEN_FOCUS),
        ResumeActionScript(MARIO),
        ClearBit(MIDAS_RIVER_TUNNEL_1_BIT),
        SetBit(MIDAS_RIVER_TUNNEL_2_BIT_2),
        Return(),
    ]
)
