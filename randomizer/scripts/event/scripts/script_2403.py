# pylint: disable=C0301

"""E2403_8BIT_END_EAST"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        JmpIfBitClear(TOWER_8BIT_EASTER_EGG_BIT_1, ["EVENT_2403_ret_21"]),
        JmpIfBitSet(TOWER_8BIT_EASTER_EGG_BIT_2, ["EVENT_2403_ret_21"]),
        StopAllBackgroundEvents(),
        FadeOutMusicFDA3(),
        SetBit(TOWER_8BIT_EASTER_EGG_BIT_2),
        ActionQueueSync(
            target=NPC_0,
            subscript=[
                ASSetSpriteSequence(index=2, is_sequence=True, looping=True),
                ASPause(64),
                ASSetVRAMPriority(PRIORITY_3),
                ASSetSpriteSequence(index=3, is_sequence=True, looping=True),
                ASDb(bytearray(b" \x04")),
                ASDb(bytearray(b"%\xc0\x06\xc0\xff")),
                ASPause(54),
                ASBPL262728(),
                ASPause(16),
                ASSetVRAMPriority(NORMAL_PRIORITY),
                ASSetSpriteSequence(index=4, is_sequence=True, looping=True),
            ]),
        Pause(64),
        PlayMusicAtDefaultVolume(M45_HEART_BEATING_A_LITTLE_FASTER_PART_1),
        StopEmbeddedActionScript(NPC_0),
        ActionQueueAsync(
            target=MARIO,
            subscript=[
                ASSetWalkingSpeed(NORMAL),
                ASWalk1StepSouthwest(),
                ASWalkNorthwestSteps(8),
            ]),
        ActionQueueAsync(
            target=NPC_0,
            subscript=[ASResetProperties(), ASVisibilityOff()],
            identifier="EVENT_2403_action_queue_async_9_"),
        ResetCoords(NPC_0),
        FadeOutMusicFDA3(),
        ActionQueueSync(
            target=MARIO,
            subscript=[
                ASSetPriority(2),
                ASSetVRAMPriority(NORMAL_PRIORITY),
                ASShadowOff(),
                ASPause(16),
                ASSetSequenceSpeed(FAST),
                ASWalkSoutheastSteps(5),
                ASPause(24),
                ASFaceSouthwest(),
                ASSetSpriteSequence(index=6, is_sequence=True, looping=True),
                ASPause(8),
            ]),
        Pause(32),
        PlayMusicAtDefaultVolume(M46_HEART_BEATING_A_LITTLE_FASTER_PART_2),
        StopEmbeddedActionScript(MARIO),
        SetAsyncActionScript(MARIO, A0384_PLAYER_LOOK_DOWN_SHAKE_HEAD),
        SetAsyncActionScript(MARIO, A0395_PLAYER_RESET_PROPERTIES_AND_SOLIDITY),
        Pause(16),
        PlayMusicAtDefaultVolume(M32_AND_MY_NAMES_BOOSTER),
        EnableControls([LEFT, RIGHT, DOWN, UP, X, A, Y, B]),
        ResetPrioritySet(),
        ClearBit(TOWER_8BIT_EASTER_EGG_BIT_1),
        ClearBit(TOWER_8BIT_EASTER_EGG_BIT_2),
        Return(identifier="EVENT_2403_ret_21"),
    ]
)
