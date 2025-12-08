# pylint: disable=C0301

"""E0705_MARRYMORE_LIBERATED_CHAPEL_GREEN_TOAD"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        RunDialog(
            dialog_id=DI2107_MARRYMORE_TOADOFSKY_HINT,
            above_object=MEM_70A8,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True),
        Return(),
    ]
)
