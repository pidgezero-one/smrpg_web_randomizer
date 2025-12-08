# pylint: disable=C0301

"""E0092_PIPE_VAULT_CLOSED_NOTE"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        RunDialog(
            dialog_id=DI1110_PIPE_VAULT_CLOSED,
            above_object=MEM_70A8,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True),
        Return(),
    ]
)
