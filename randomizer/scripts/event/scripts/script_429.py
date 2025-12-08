# pylint: disable=C0301

"""E0429_PIPE_VAULT_THWOMP_ROOM_LOADER_BACKGROUND"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        JmpIfBitSet(
            TEMP_7043_1,
            ["EVENT_429_set_action_script_async_3"],
            identifier="EVENT_429_jmp_if_bit_set_0"),
        Pause(1),
        Jmp(["EVENT_429_jmp_if_bit_set_0"]),
        SetAsyncActionScript(
            SCREEN_FOCUS,
            A0658_PIPE_VAULT_THWOMP_ROOM_SHAKE_CAMERA,
            identifier="EVENT_429_set_action_script_async_3"),
        Jmp(["EVENT_429_jmp_if_bit_set_0"]),
    ]
)
