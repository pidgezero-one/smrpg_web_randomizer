# pylint: disable=C0301

"""E2097_MOVE_HINOPIO_TO_ITEM_SHOP"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        JmpIfBitSet(TEMP_7043_1, ["EVENT_2097_ret_6"]),
        JmpIfBitSet(TEMP_7043_3, ["EVENT_2097_set_action_script_sync_4"]),
        SetSyncActionScript(NPC_0, A0866_MOVE_HINOPIO_TO_ITEM_SHOP),
        Return(),
        SetSyncActionScript(
            NPC_0,
            A0868_MOVE_HINOPIO_TO_ITEM_SHOP,
            identifier="EVENT_2097_set_action_script_sync_4",
        ),
        Return(identifier="EVENT_2097_ret_6"),
    ]
)
