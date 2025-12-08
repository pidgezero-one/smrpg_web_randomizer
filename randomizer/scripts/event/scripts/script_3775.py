# pylint: disable=C0301

"""E3775_UNUSED_NIMBUS_DIALOG"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        RunDialog(
            dialog_id=DI3596_NIMBUS_NPC,
            above_object=MEM_70A8,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True),
        Return(),
    ]
)
