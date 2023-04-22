# pylint: disable=C0301

"""E3395_MIDAS_CAVE_BEETLEMANIA_GRANTER"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        SetBit(BEETLEMANIA_UNLOCKED),
        RunDialog(
            dialog_id=DI3074_GOT_BEETLEMANIA,
            above_object=Bowser,
            closable=False,
            sync=False,
            multiline=False,
            use_background=False,
        ),
        Return(),
    ]
)
