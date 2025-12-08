# pylint: disable=C0301

"""E0697_MARRYMORE_ENTRANCE_TOAD"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        Set7000ToCurrentLevel(),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 65, ["EVENT_697_run_dialog_17"]),
        JmpIfBitSet(MARRYMORE_BACKDOOR_OPEN, ["EVENT_697_run_dialog_3"]),
        RunDialog(
            dialog_id=DI2159_MARRYMORE_FIELD_NPC,
            above_object=MEM_70A8,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True),
        Return(),
        RunDialog(
            dialog_id=DI2158_MARRYMORE_FIELD_NPC,
            above_object=MEM_70A8,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
            identifier="EVENT_697_run_dialog_3"),
        Return(),
        RunDialog(
            dialog_id=DI2179_CHAPEL_NPC,
            above_object=MEM_70A8,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
            identifier="EVENT_697_run_dialog_17"),
        Return(),
    ]
)
