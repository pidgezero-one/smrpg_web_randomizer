# pylint: disable=C0301

"""E3307_SHIP_PASSWORD_TUTORIAL"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        StopAllBackgroundEvents(),
        RunDialog(
            dialog_id=DI1688_PASSWORD_ENTRY_INSTRUCTIONS,
            above_object=NPC_12,
            closable=True,
            sync=False,
            multiline=True,
            use_background=False),
        JmpIfBitSet(TEMP_7043_0, ["EVENT_3307_ret_4"]),
        RunBackgroundEvent(
            event_id=E3225_SHIP_PASSWORD_BOX_DIALOG, return_on_level_exit=True
        ),
        Return(identifier="EVENT_3307_ret_4"),
    ]
)
