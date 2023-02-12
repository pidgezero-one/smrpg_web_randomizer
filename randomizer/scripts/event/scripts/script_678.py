# E0678_MARRYMORE_JUMP_ON_ORGAN_PIPE

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        JmpIfBitSet(TEMP_7043_0, ["EVENT_256_ret_0"]),
        SetBit(TEMP_7043_0),
        PlaySound(sound=SO131_JUMP_ON_ORGAN, channel=6),
        SetSyncActionScript(NPC_0, A0636_54_VELOCITY_SINGLE_JUMP),
        SetSyncActionScript(NPC_5, A0636_54_VELOCITY_SINGLE_JUMP),
        SetSyncActionScript(NPC_4, A0636_54_VELOCITY_SINGLE_JUMP),
        Pause(30),
        StopSound(),
        ActionQueueSync(
            target=MARIO,
            subscript=[
                ASSetSpriteSequence(
                    index=0, sprite_offset=3, is_sequence=True, looping=True
                ),
                ASJumpToHeight(height=108, silent=True),
                ASPause(
                    1, identifier="EVENT_678_action_queue_sync_8_SUBSCRIPT_pause_2"
                ),
                ASJmpIfMarioInAir(["EVENT_678_action_queue_sync_8_SUBSCRIPT_pause_2"]),
            ],
        ),
        RunDialog(
            dialog_id=DI2184_JUMP_ON_ORGAN,
            above_object=NPC_12,
            closable=True,
            sync=False,
            multiline=True,
            use_background=False,
        ),
        ActionQueueAsync(
            target=MARIO,
            subscript=[
                ASResetProperties(),
                ASJumpToHeight(96),
                ASShiftSoutheastSteps(2),
                ASShiftSoutheastPixels(8),
                ASPause(
                    1, identifier="EVENT_678_action_queue_async_10_SUBSCRIPT_pause_4"
                ),
                ASJmpIfMarioInAir(
                    ["EVENT_678_action_queue_async_10_SUBSCRIPT_pause_4"]
                ),
            ],
        ),
        ClearBit(TEMP_7043_0),
        SetSyncActionScript(NPC_0, A0119_SLOW_SEQUENCE_LOOP),
        SetSyncActionScript(NPC_5, A0119_SLOW_SEQUENCE_LOOP),
        SetSyncActionScript(NPC_4, A0119_SLOW_SEQUENCE_LOOP),
        Return(),
    ]
)
