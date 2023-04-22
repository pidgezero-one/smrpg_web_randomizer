# pylint: disable=C0301

"""E0689_MARRYMORE_RAINI"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        Set7000ToCurrentLevel(),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 65, ["EVENT_689_run_dialog_5"]),
        JmpIfBitSet(MARRYMORE_BACKDOOR_OPEN, ["EVENT_689_run_dialog_2"]),
        RunDialog(
            dialog_id=DI2110_RAINI_OUTSIDE,
            above_object=MEM_70A8,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        Return(),
        RunDialog(
            dialog_id=DI2113_RAINI_OCCUPIED,
            above_object=MEM_70A8,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
            identifier="EVENT_689_run_dialog_2",
        ),
        Return(),
        RunDialog(
            dialog_id=DI2177_I_DO,
            above_object=MEM_70A8,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
            identifier="EVENT_689_run_dialog_5",
        ),
        Return(),
    ]
)
