# pylint: disable=C0301

"""E1143_SEASIDE_SHED_GUARD_2"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        RunDialog(
            dialog_id=DI2848_OCCUPIED_SEASIDE_HENCHMAN_SHED_GUARD,
            above_object=MEM_70A8,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True),
        Return(),
    ]
)
