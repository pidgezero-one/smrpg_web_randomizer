# pylint: disable=C0301

"""E0312_MUSHROOM_KINGDOM_OCCUPIED_RUNNING_KID"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        RunDialog(
            dialog_id=DI0607_KID_STUCK_INDOORS,
            above_object=MEM_70A8,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        Return(),
    ]
)
