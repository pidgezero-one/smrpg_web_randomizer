# E2404_8BIT_END_WEST

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        JmpIfBitClear(TOWER_8BIT_EASTER_EGG_BIT_1, ["EVENT_2404_ret_13"]),
        JmpIfBitSet(TOWER_8BIT_EASTER_EGG_BIT_2, ["EVENT_2404_ret_13"]),
        StopAllBackgroundEvents(),
        FadeOutMusicFDA3(),
        SetBit(TOWER_8BIT_EASTER_EGG_BIT_2),
        ActionQueueSync(
            target=NPC_0,
            subscript=[
                ASSetSpriteSequence(
                    index=2, is_sequence=True, looping=True, mirror_sprite=True
                ),
                ASPause(64),
                ASSetVRAMPriority(PRIORITY_3),
                ASSetWalkingSpeed(FASTEST),
                ASShiftWestPixels(6),
                ASSetSpriteSequence(index=3, is_sequence=True, looping=True),
                ASPause(54),
                ASPause(16),
                ASSetVRAMPriority(NORMAL_PRIORITY),
                ASShiftEastPixels(6),
                ASSetVRAMPriority(PRIORITY_3),
                ASSetSpriteSequence(
                    index=4, is_sequence=True, looping=True, mirror_sprite=True
                ),
            ],
        ),
        Pause(64),
        PlayMusicAtDefaultVolume(M45_HEART_BEATING_A_LITTLE_FASTER_PART_1),
        StopEmbeddedActionScript(NPC_0),
        ActionQueueAsync(
            target=MARIO,
            subscript=[
                ASSetWalkingSpeed(NORMAL),
                ASShadowOn(),
                ASShiftSoutheastSteps(7),
                ASShiftSoutheastPixels(8),
                ASShiftNortheastPixels(8),
                ASJumpToHeight(108),
                ASShiftNortheastSteps(2),
                ASJumpToHeight(108),
                ASShiftNortheastSteps(2),
            ],
        ),
        ActionQueueSync(
            target=NPC_0,
            subscript=[
                ASSetVRAMPriority(NORMAL_PRIORITY),
                ASSetSpriteSequence(index=4, is_sequence=True, looping=True),
            ],
        ),
        ActionQueueAsync(target=MARIO, subscript=[ASShiftNorthwestSteps(8)]),
        Jmp(["EVENT_2403_action_queue_async_9_"]),
        Return(identifier="EVENT_2404_ret_13"),
    ]
)
