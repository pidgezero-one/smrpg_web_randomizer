# pylint: disable=C0301

"""E0686_MARRYMORE_LIBERATED_EXTERIOR_RED_TOAD"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        RunDialog(
            dialog_id=DI2199_MARRYMORE_PHOTO,
            above_object=MEM_70A8,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True),
        Return(),
    ]
)
