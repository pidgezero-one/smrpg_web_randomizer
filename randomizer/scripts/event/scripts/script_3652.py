# pylint: disable=C0301

"""E3652_NIMBUS_OCCUPIED_NORTHEAST_HOUSE_LEFT_GUARD"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        SetVarToConst(TEMP_70AE, 16),
        RunDialog(
            dialog_id=DI3722_NO_ROYAL_BUS,
            above_object=MEM_70A8,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True),
        Return(),
    ]
)
