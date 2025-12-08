# pylint: disable=C0301

"""E0194_MALLOW_JOINS_CONTAINER"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        RunDialog(
            dialog_id=DI1180_MALLOW_JOINS,
            above_object=BOWSER,
            closable=True,
            sync=False,
            multiline=False,
            use_background=False),
        JmpToEvent(E0188_MALLOW_JOINS),
    ]
)
