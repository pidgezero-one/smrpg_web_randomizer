# pylint: disable=C0301

"""E0706_MARRYMORE_LIBERATED_CHAPEL_PINK_KID"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        RunDialog(
            dialog_id=DI2111_BELLHOP_IN_CHAPEL,
            above_object=MEM_70A8,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        Return(),
    ]
)
