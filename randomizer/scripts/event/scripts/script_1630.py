# pylint: disable=C0301

"""E1630_MOLEVILLE_LIBERATED_PA_MOLE_IN_HOUSE"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        RunDialog(
            dialog_id=DI1118_PA_MOLE,
            above_object=MEM_70A8,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        Return(),
    ]
)
