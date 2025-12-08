# pylint: disable=C0301

"""E0691_MARRYMORE_YELLOW_TOAD_1"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        Set7000ToCurrentLevel(),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 65, ["EVENT_691_run_dialog_7"]),
        JmpIfBitSet(MARRYMORE_BACKDOOR_OPEN, ["EVENT_691_run_dialog_9"]),
        RunDialog(
            dialog_id=DI2116_UNUSED,
            above_object=MEM_70A8,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True),
        Return(),
        RunDialog(
            dialog_id=DI2182_CHAPEL_NPC,
            above_object=MEM_70A8,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
            identifier="EVENT_691_run_dialog_7"),
        Return(),
        RunDialog(
            dialog_id=DI2117_MARRYMORE_SHITPOST,
            above_object=MEM_70A8,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
            identifier="EVENT_691_run_dialog_9"),
        Return(),
    ]
)
