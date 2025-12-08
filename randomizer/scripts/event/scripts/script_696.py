# pylint: disable=C0301

"""E0696_MARRYMORE_YELLOW_TOAD_2"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        Set7000ToCurrentLevel(),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 65, ["EVENT_696_run_dialog_5"]),
        JmpIfBitSet(MARRYMORE_BACKDOOR_OPEN, ["EVENT_696_run_dialog_insert"]),
        RunDialog(
            dialog_id=DI2333_MARRYMORE_NPC,
            above_object=MEM_70A8,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True),
        Return(),
        RunDialog(
            dialog_id=DI2115_MARRYMORE_SHITPOST,
            above_object=MEM_70A8,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
            identifier="EVENT_696_run_dialog_insert"),
        RunEventAsSubroutine(E0200_UNLOCK_FOREST_IF_GATED_BY_MARRYMORE_CHARACTER),
        Return(),
        RunDialog(
            dialog_id=DI2180_CHAPEL_NPC,
            above_object=MEM_70A8,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
            identifier="EVENT_696_run_dialog_5"),
        Return(),
    ]
)
