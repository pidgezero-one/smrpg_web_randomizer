# pylint: disable=C0301

"""E2099_MOVE_HINOPIO_TO_ARMOR_SHOP"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        JmpIfBitSet(TEMP_7043_3, ["EVENT_2099_ret_6"]),
        JmpIfBitSet(TEMP_7043_2, ["EVENT_2099_set_action_script_sync_4"]),
        SetSyncActionScript(NPC_0, A0865_MOVE_HINOPIO_TO_ARMOR_SHOP),
        Return(),
        SetSyncActionScript(
            NPC_0,
            A0867_MOVE_HINOPIO_TO_ARMOR_SHOP,
            identifier="EVENT_2099_set_action_script_sync_4"),
        Return(identifier="EVENT_2099_ret_6"),
    ]
)
