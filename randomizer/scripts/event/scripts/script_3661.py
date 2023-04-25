# pylint: disable=C0301

"""E3661_BATHROBE"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        RunDialog(
            dialog_id=DI3845_DUPLICATE,
            above_object=BOWSER,
            closable=True,
            sync=False,
            multiline=True,
            use_background=False,
        ),
        Return(),
    ]
)
