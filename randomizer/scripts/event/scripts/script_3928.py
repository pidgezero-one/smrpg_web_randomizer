# pylint: disable=C0301

"""E3928_NIMBUS_CASTLLE_4_WAY_PATH_RIGHT_GUARD"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        RunDialog(
            dialog_id=DI2390_NIMBUS_NPC,
            above_object=MEM_70A8,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        Return(),
    ]
)
