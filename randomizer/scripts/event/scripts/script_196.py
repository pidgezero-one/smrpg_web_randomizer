# pylint: disable=C0301

"""E0196_BOWSER_JOINS_CONTAINER"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        RunDialog(
            dialog_id=DI1182_BOWSER_JOINS,
            above_object=BOWSER,
            closable=True,
            sync=False,
            multiline=False,
            use_background=False),
        JmpToEvent(E0190_BOWSER_JOINS),
    ]
)
