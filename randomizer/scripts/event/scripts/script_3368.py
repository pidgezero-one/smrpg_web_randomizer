# pylint: disable=C0301

"""E3368_KEEP_LOGIC_GAME_BONES"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        JmpIfBitSet(TEMP_7043_2, ["EVENT_3366_ret_8"]),
        RunDialog(
            dialog_id=DI1925_EMPTY_AUTO_TERMINATE,
            above_object=MEM_70A8,
            closable=False,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        RunDialog(
            dialog_id=DI1923_BONES,
            above_object=MEM_70A8,
            closable=False,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        JmpIfVarEqualsConst(TEMP_70AF, 1, ["EVENT_3369_set_7000_to_70A0_short_mem_32"]),
        JmpIfVarEqualsConst(TEMP_7028, 1, ["EVENT_3369_run_dialog_12"]),
        JmpIfVarEqualsConst(TEMP_7028, 2, ["EVENT_3369_run_dialog_10"]),
        JmpIfVarEqualsConst(TEMP_7028, 3, ["EVENT_3369_run_dialog_8"]),
        JmpIfVarEqualsConst(TEMP_7028, 4, ["EVENT_3369_run_dialog_30"]),
    ]
)
