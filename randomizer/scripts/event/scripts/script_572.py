# pylint: disable=C0301

"""E0572_ROSE_TOWN_LIBERATED_HUSBAND"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        RunDialog(
            dialog_id=DI0859_FINALLY_HOME,
            above_object=MEM_70A8,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True),
        Return(),
    ]
)
