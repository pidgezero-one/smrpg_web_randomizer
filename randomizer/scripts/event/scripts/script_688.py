# pylint: disable=C0301

"""E0688_MARRYMORE_RAZ"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        Set7000ToCurrentLevel(),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 65, ["EVENT_688_run_dialog_7"]),
        JmpIfBitSet(MARRYMORE_BACKDOOR_OPEN, ["EVENT_688_run_dialog__2"]),
        RunDialog(
            dialog_id=DI2109_RAZ_OUTSIDE,
            above_object=MEM_70A8,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True),
        Return(),
        RunDialog(
            dialog_id=DI2112_RAZ_OCCUPIED,
            above_object=MEM_70A8,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
            identifier="EVENT_688_run_dialog__2"),
        RunEventAsSubroutine(E0200_UNLOCK_FOREST_IF_GATED_BY_MARRYMORE_CHARACTER),
        Return(),
        RunDialog(
            dialog_id=DI2183_TOWER_KNIFE_GUY_REMINDER,
            above_object=MEM_70A8,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
            identifier="EVENT_688_run_dialog_7"),
        Return(),
    ]
)
