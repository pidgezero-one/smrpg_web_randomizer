# pylint: disable=C0301

"""E3646_NIMBUS_EXTERIOR_GUARD_NEAR_ENTRANCE"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        RunDialog(
            dialog_id=DI2409_DREAM_CUSHION_HINT,
            above_object=MEM_70A8,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        Return(),
    ]
)
