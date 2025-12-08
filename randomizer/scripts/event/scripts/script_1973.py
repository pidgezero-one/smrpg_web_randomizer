# pylint: disable=C0301

"""E1973_CLONE_RESERVED"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        RunDialog(
            dialog_id=DI2931_MUSHROOM_BOY_NO_PRIZE,
            above_object=MEM_70A8,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True),
        Return(),
    ]
)
