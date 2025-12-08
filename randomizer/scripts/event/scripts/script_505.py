# pylint: disable=C0301

"""E0505_PIPE_VAULT_MARIO_THWOMP_TUMBLE"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        Pause(1, identifier="EVENT_505_pause_0"),
        JmpIfBitSet(TEMP_7043_3, ["EVENT_505_pause_3"]),
        Jmp(["EVENT_505_pause_0"]),
        Pause(1, identifier="EVENT_505_pause_3"),
        JmpIfMarioInAir(["EVENT_505_pause_3"]),
        JmpIfBitClear(TEMP_7043_2, ["EVENT_505_pause_0"]),
        JmpIfBitClear(TEMP_7043_3, ["EVENT_505_pause_0"]),
        EnableControls([]),
        ActionQueueAsync(
            target=MARIO,
            subscript=[
                ASClearSolidityBits(
                    bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True
                ),
                ASSetSpriteSequence(
                    index=9,
                    sprite_offset=3,
                    is_sequence=True,
                    looping=True,
                    mirror_sprite=True),
                ASSetWalkingSpeed(FAST),
                ASJumpToHeight(height=72, silent=True),
                ASWalkSouthwestSteps(2),
                ASPause(
                    1, identifier="EVENT_505_action_queue_async_8_SUBSCRIPT_pause_5"
                ),
                ASJmpIfMarioInAir(["EVENT_505_action_queue_async_8_SUBSCRIPT_pause_5"]),
                ASSetSequenceSpeed(FAST),
                ASSetSpriteSequence(
                    index=6, sprite_offset=3, is_sequence=True, looping=True
                ),
                ASWalkToXYCoords(x=21, y=36),
            ]),
        ActionQueueAsync(
            target=MARIO,
            subscript=[
                ASFaceSouthwest(),
                ASResetProperties(),
                ASSetSolidityBits(
                    bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True
                ),
                ASSetWalkingSpeed(NORMAL),
            ]),
        SetAsyncActionScript(MARIO, A0671_SHAKE_HEAD_NO),
        ClearBit(TEMP_7043_3),
        EnableControls([LEFT, RIGHT, DOWN, UP, X, A, Y, B]),
        JmpToEvent(E0505_PIPE_VAULT_MARIO_THWOMP_TUMBLE),
    ]
)
