# pylint: disable=C0301

"""E3719_NIMBUS_CASTLE_RIGHT_RED_CELLAR_WOMAN"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        Set7000ToCurrentLevel(),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 413, ["EVENT_3719_run_dialog_4"]),
        RunDialog(
            dialog_id=DI3661_NIMBUS_KEY_EXPLANATION,
            above_object=MEM_70A8,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        Return(),
        RunDialog(
            dialog_id=DI3760_NIMBUS_NPC,
            above_object=MEM_70A8,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
            identifier="EVENT_3719_run_dialog_4",
        ),
        Return(),
    ]
)
