# pylint: disable=C0301

"""E2098_MOVE_HINOPIO_TO_INN"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        JmpIfBitSet(TEMP_7043_2, ["EVENT_2098_ret_6"]),
        JmpIfBitSet(TEMP_7043_3, ["EVENT_2098_set_action_script_sync_4"]),
        SetSyncActionScript(NPC_0, A0864_MOVE_HINOPIO_TO_INN),
        Return(),
        SetSyncActionScript(
            NPC_0,
            A0869_MOVE_HINOPIO_TO_INN,
            identifier="EVENT_2098_set_action_script_sync_4",
        ),
        Return(identifier="EVENT_2098_ret_6"),
    ]
)
