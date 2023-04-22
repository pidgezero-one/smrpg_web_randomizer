# pylint: disable=C0301

"""E0578_ROSE_TOWN_LIBERATED_UPPER_HIDDEN_NPC"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        RunDialog(
            dialog_id=DI1052_PIPE_VAULT_HINT,
            above_object=MEM_70A8,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        Return(),
    ]
)
