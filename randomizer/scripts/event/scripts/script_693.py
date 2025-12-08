# pylint: disable=C0301

"""E0693_MARRYMORE_GREY_TOAD"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        Set7000ToCurrentLevel(),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 65, ["EVENT_693_run_dialog_5"]),
        JmpIfBitSet(MARRYMORE_BACKDOOR_OPEN, ["EVENT_693_run_dialog_insert"]),
        RunDialog(
            dialog_id=DI2327_MARRYMORE_NPC,
            above_object=MEM_70A8,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True),
        Return(),
        RunDialog(
            dialog_id=DI2118_MARRYMORE_SHITPOST,
            above_object=MEM_70A8,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
            identifier="EVENT_693_run_dialog_insert"),
        Return(),
        RunDialog(
            dialog_id=DI2178_CHAPEL_NPC,
            above_object=MEM_70A8,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
            identifier="EVENT_693_run_dialog_5"),
        Return(),
    ]
)
