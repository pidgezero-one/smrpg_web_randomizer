# pylint: disable=C0301

"""E2062_MONSTRO_MIMIC"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        RunDialog(
            dialog_id=DI2636_MIMICS_HINT,
            above_object=MARIO,
            closable=True,
            sync=False,
            multiline=True,
            use_background=False),
        Return(),
    ]
)
