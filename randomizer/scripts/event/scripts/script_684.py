# pylint: disable=C0301

"""E0684_MARRYMORE_LIBERATED_EXTERIOR_HUSBAND"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        RunDialog(
            dialog_id=DI2193_MARRYMORE_PHOTO,
            above_object=MEM_70A8,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True),
        Return(),
    ]
)
