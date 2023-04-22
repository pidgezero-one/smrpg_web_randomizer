# pylint: disable=C0301

"""E1646_MOLEVILLE_SONG_HINT_GIRL"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        JmpIfBitClear(TEMP_7042_1, ["EVENT_1646_run_dialog_3"]),
        RunDialog(
            dialog_id=DI1174_CANT_WAIT_TO_GET_OLDER,
            above_object=MEM_70A8,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        Return(),
        RunDialog(
            dialog_id=DI1142_MOLEVILLE_BLUES_HINT,
            above_object=MEM_70A8,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
            identifier="EVENT_1646_run_dialog_3",
        ),
        Return(),
    ]
)
