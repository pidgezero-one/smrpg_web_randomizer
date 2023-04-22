# pylint: disable=C0301

"""E0400_GUEST_ROOM_GUARD"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        Set7000ToCurrentLevel(),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 21, ["EVENT_400_run_dialog_4"]),
        RunDialog(
            dialog_id=DI0690_GUEST_ROOM_BEFORE_SAMUS,
            above_object=MEM_70A8,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        Return(),
        RunDialog(
            dialog_id=DI3919_DUPLICATE,
            above_object=MEM_70A8,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
            identifier="EVENT_400_run_dialog_4",
        ),
        Return(),
    ]
)
