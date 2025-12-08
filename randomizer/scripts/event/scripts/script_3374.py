# pylint: disable=C0301

"""E3374_KEEP_THWOMP_ROOM_BACKGROUND"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        JmpIfBitSet(
            TEMP_7044_7,
            ["EVENT_3374_jmp_if_bit_set_2"],
            identifier="EVENT_3374_jmp_if_bit_set_0"),
        EnableControlsUntilReturn([LEFT, RIGHT, DOWN, UP, X, A, Y, B]),
        JmpIfBitSet(
            TEMP_7043_0,
            ["EVENT_3374_jmp_if_mario_in_air_9"],
            identifier="EVENT_3374_jmp_if_bit_set_2"),
        JmpIfBitSet(TEMP_7043_1, ["EVENT_3374_jmp_if_mario_in_air_9"]),
        JmpIfBitSet(TEMP_7043_2, ["EVENT_3374_jmp_if_mario_in_air_9"]),
        JmpIfBitSet(TEMP_7043_3, ["EVENT_3374_jmp_if_mario_in_air_9"]),
        JmpIfBitSet(TEMP_7043_4, ["EVENT_3374_jmp_if_mario_in_air_9"]),
        Pause(1),
        Jmp(["EVENT_3374_jmp_if_bit_set_0"]),
        JmpIfMarioInAir(
            ["EVENT_3374_action_queue_async_11"],
            identifier="EVENT_3374_jmp_if_mario_in_air_9"),
        EnableControlsUntilReturn([]),
        ActionQueueAsync(
            target=SCREEN_FOCUS,
            subscript=[
                ASSetWalkingSpeed(VERY_FAST),
                ASShiftZDownPixels(4),
                ASShiftZUpPixels(4),
                ASSetWalkingSpeed(NORMAL),
            ],
            identifier="EVENT_3374_action_queue_async_11"),
        Jmp(["EVENT_3374_jmp_if_bit_set_0"]),
    ]
)
