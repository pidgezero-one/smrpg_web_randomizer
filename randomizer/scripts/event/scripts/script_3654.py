# pylint: disable=C0301

"""E3654_NIMBUS_SOUTH_HOUSE_WOMAN"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        SetVarToConst(TEMP_70AE, 16),
        RunDialog(
            dialog_id=DI3592_NIMBUS_HIDDEN_TREASURE_HINT,
            above_object=MEM_70A8,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True),
        Return(),
    ]
)
