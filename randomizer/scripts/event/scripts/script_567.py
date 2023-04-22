# pylint: disable=C0301

"""E0567_ROSE_TOWN_LIBERATED_GRANDMA"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        RunDialog(
            dialog_id=DI0863_STOPPED_RAINING_ARROWS,
            above_object=MEM_70A8,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        Return(),
    ]
)
