# pylint: disable=C0301

"""E0632_MARRYMORE_EXTERIOR_CHAPEL_LOCKED_FRONT_DOOR"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        JmpIfBitClear(MARRYMORE_BACKDOOR_OPEN, ["EVENT_632_run_dialog_3"]),
        RunDialog(
            dialog_id=DI2063_MARRYMORE_LOCKED_DOOR,
            above_object=MEM_70A8,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        Return(),
        RunDialog(
            dialog_id=DI2811_ITS_LOCKED,
            above_object=BOWSER,
            closable=True,
            sync=False,
            multiline=False,
            use_background=False,
            identifier="EVENT_632_run_dialog_3",
        ),
        Return(),
    ]
)
