# pylint: disable=C0301

"""E0193_MARIO_JOINS_CONTAINER"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        RunDialog(
            dialog_id=DI1179_MARIO_JOINS,
            above_object=Bowser,
            closable=True,
            sync=False,
            multiline=False,
            use_background=False,
        ),
        JmpToEvent(E0187_MARIO_JOINS),
    ]
)
