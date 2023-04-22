# pylint: disable=C0301

"""E3655_NIMBUS_EXTERIOR_SOUTHERNMOST_BLUE_GUY"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        RunDialog(
            dialog_id=DI2474_NIMBUS_NPC,
            above_object=MEM_70A8,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        Return(),
    ]
)
