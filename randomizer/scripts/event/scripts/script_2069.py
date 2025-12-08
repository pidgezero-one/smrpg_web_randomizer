# pylint: disable=C0301

"""E2069_MONSTRO_MOUSE"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        RunDialog(
            dialog_id=DI1276_GARDENER_UNLOCK_HINT,
            above_object=MARIO,
            closable=True,
            sync=False,
            multiline=True,
            use_background=False),
        Return(),
    ]
)
