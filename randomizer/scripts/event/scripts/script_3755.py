# pylint: disable=C0301

"""E3755_HOT_SPRINGS_NOTE"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        RunDialog(
            dialog_id=DI3677_VOLCANO_WARNING,
            above_object=MEM_70A8,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True),
        Return(),
    ]
)
