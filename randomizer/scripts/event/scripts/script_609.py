# pylint: disable=C0301

"""E0609_MARRYMORE_INN_3F_HALLWAY_BELLHOP"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        RunDialog(
            dialog_id=DI0979_INACTIVE_BELLHOP,
            above_object=MEM_70A8,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        Return(),
    ]
)
