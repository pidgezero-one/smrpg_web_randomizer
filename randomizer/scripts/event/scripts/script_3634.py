# pylint: disable=C0301

"""E3634_NIMBUS_EXTERIOR_WOMAN_NEAR_ENTRANCE"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        RunDialog(
            dialog_id=DI2414_GIANT_EGG_HINT,
            above_object=MEM_70A8,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True),
        Return(),
    ]
)
