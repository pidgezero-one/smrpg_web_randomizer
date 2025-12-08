# pylint: disable=C0301

"""E1167_SEASIDE_ELDER"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        RunDialog(
            dialog_id=DI2923_SEASIDE_ELDER_WELCOME,
            above_object=MEM_70A8,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True),
        Return(),
    ]
)
