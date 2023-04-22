# pylint: disable=C0301

"""E3187_MINECART_TUTORIAL"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        RunDialog(
            dialog_id=DI1650_MINECART_INSTRUCTIONS,
            above_object=NPC_12,
            closable=True,
            sync=False,
            multiline=True,
            use_background=False,
        ),
        JmpIfDialogOptionBSelected(["EVENT_3187_ret_3"]),
        RunDialog(
            dialog_id=DI1651_MINECART_INSTRUCTIONS_EXTENDED,
            above_object=NPC_12,
            closable=True,
            sync=False,
            multiline=True,
            use_background=False,
        ),
        Return(identifier="EVENT_3187_ret_3"),
    ]
)
