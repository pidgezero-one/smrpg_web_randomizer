# pylint: disable=C0301

"""E0318_MUSHROOM_KINGDOM_OCCUPIED_CASTLE_TOAD"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        RunDialog(
            dialog_id=DI0649_HELP,
            above_object=MEM_70A8,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        Return(),
    ]
)
