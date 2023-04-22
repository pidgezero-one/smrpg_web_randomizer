# pylint: disable=C0301

"""E3366_KEEP_LOGIC_GAME_BOO"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        JmpIfBitSet(TEMP_7043_1, ["EVENT_3366_ret_8"]),
        RunDialog(
            dialog_id=DI1925_EMPTY_AUTO_TERMINATE,
            above_object=MEM_70A8,
            closable=False,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        RunDialog(
            dialog_id=DI1921_BOO,
            above_object=MEM_70A8,
            closable=False,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        JmpIfVarEqualsConst(TEMP_70AF, 1, ["EVENT_3369_set_7000_to_70A0_short_mem_32"]),
        JmpIfVarEqualsConst(SECONDARY_TEMP_7024, 1, ["EVENT_3369_run_dialog_12"]),
        JmpIfVarEqualsConst(SECONDARY_TEMP_7024, 2, ["EVENT_3369_run_dialog_10"]),
        JmpIfVarEqualsConst(SECONDARY_TEMP_7024, 3, ["EVENT_3369_run_dialog_8"]),
        JmpIfVarEqualsConst(SECONDARY_TEMP_7024, 4, ["EVENT_3369_run_dialog_30"]),
        Return(identifier="EVENT_3366_ret_8"),
    ]
)
