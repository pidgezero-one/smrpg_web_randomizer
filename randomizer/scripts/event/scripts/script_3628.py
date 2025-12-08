# pylint: disable=C0301

"""E3628_NIMBUS_EXTERIOR_BLUE_GUY_IN_FRONT_OF_CASTLE_ENTRANCE"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        RunDialog(
            dialog_id=DI2412_GARRO_HINT,
            above_object=MEM_70A8,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True),
        Return(),
    ]
)
