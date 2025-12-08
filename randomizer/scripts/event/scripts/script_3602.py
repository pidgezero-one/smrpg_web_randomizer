# pylint: disable=C0301

"""E3602_MUSHROOM_KINGDOM_RAZ_RAINI_NOTE"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        RunDialog(
            dialog_id=DI2328_RAZ_RAINI_NOTE,
            above_object=MEM_70A8,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True),
        Return(),
    ]
)
