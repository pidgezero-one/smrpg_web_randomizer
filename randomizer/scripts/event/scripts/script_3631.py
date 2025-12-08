# pylint: disable=C0301

"""E3631_NIMBUS_EXTERIOR_BLUE_GUY_NEAR_GARROS_HOUSE"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        RunDialog(
            dialog_id=DI2411_TALK_TO_NPCS_AGAIN_HINT,
            above_object=MEM_70A8,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True),
        Return(),
    ]
)
