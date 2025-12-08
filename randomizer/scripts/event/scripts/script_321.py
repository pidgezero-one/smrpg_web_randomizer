# pylint: disable=C0301

"""E0321_BELLHOP_WHILE_GUIDING"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        Inc(TEMP_70AE, identifier="EVENT_321_inc_0"),
        JmpIfVarEqualsConst(TEMP_70AE, 1, ["EVENT_321_run_dialog_5"]),
        JmpIfVarEqualsConst(TEMP_70AE, 2, ["EVENT_321_run_dialog_7"]),
        RunDialog(
            dialog_id=DI0553_BELLHOP_3,
            above_object=MEM_70A8,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True),
        Return(),
        RunDialog(
            dialog_id=DI0551_BELLHOP_1,
            above_object=MEM_70A8,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
            identifier="EVENT_321_run_dialog_5"),
        Return(),
        RunDialog(
            dialog_id=DI0552_BELLHOP_2,
            above_object=MEM_70A8,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
            identifier="EVENT_321_run_dialog_7"),
        Return(),
    ]
)
