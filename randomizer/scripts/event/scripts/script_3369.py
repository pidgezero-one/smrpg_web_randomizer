# pylint: disable=C0301

"""E3369_KEEP_LOGIC_GAME_KIPP"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        JmpIfBitSet(TEMP_7043_4, ["EVENT_3366_ret_8"]),
        RunDialog(
            dialog_id=DI1925_EMPTY_AUTO_TERMINATE,
            above_object=MEM_70A8,
            closable=False,
            sync=False,
            multiline=True,
            use_background=True),
        RunDialog(
            dialog_id=DI1924_KIPP,
            above_object=MEM_70A8,
            closable=False,
            sync=False,
            multiline=True,
            use_background=True),
        JmpIfVarEqualsConst(TEMP_70AF, 1, ["EVENT_3369_set_7000_to_70A0_short_mem_32"]),
        JmpIfVarEqualsConst(TEMP_702A, 1, ["EVENT_3369_run_dialog_12"]),
        JmpIfVarEqualsConst(TEMP_702A, 2, ["EVENT_3369_run_dialog_10"]),
        JmpIfVarEqualsConst(TEMP_702A, 3, ["EVENT_3369_run_dialog_8"]),
        JmpIfVarEqualsConst(TEMP_702A, 4, ["EVENT_3369_run_dialog_30"]),
        RunDialog(
            dialog_id=DI1926_MARATHON_3RD_PLACE,
            above_object=MEM_70A8,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
            identifier="EVENT_3369_run_dialog_8"),
        Return(),
        RunDialog(
            dialog_id=DI1927_MARATHON_2ND_PLACE,
            above_object=MEM_70A8,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
            identifier="EVENT_3369_run_dialog_10"),
        Return(),
        RunDialog(
            dialog_id=DI1928_MARATHON_1ST_PLACE,
            above_object=MEM_70A8,
            closable=False,
            sync=False,
            multiline=True,
            use_background=True,
            identifier="EVENT_3369_run_dialog_12"),
        JmpToSubroutine(["EVENT_3369_jmp_if_var_equals_const_18"]),
        RunDialog(
            dialog_id=DI1929_MARATHON_1ST_PLACE,
            above_object=MEM_70A8,
            closable=False,
            sync=False,
            multiline=True,
            use_background=True),
        JmpToSubroutine(["EVENT_3369_jmp_if_var_equals_const_18"]),
        RunDialog(
            dialog_id=DI1930_MARATHON_1ST_PLACE,
            above_object=MEM_70A8,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True),
        Return(),
        JmpIfVarEqualsConst(
            SECONDARY_TEMP_7024,
            2,
            ["EVENT_3369_run_dialog_22"],
            identifier="EVENT_3369_jmp_if_var_equals_const_18"),
        JmpIfVarEqualsConst(TEMP_7026, 2, ["EVENT_3369_run_dialog_24"]),
        JmpIfVarEqualsConst(TEMP_7028, 2, ["EVENT_3369_run_dialog_26"]),
        JmpIfVarEqualsConst(TEMP_702A, 2, ["EVENT_3369_run_dialog_28"]),
        RunDialog(
            dialog_id=DI1921_BOO,
            above_object=MEM_70A8,
            closable=False,
            sync=False,
            multiline=True,
            use_background=True,
            identifier="EVENT_3369_run_dialog_22"),
        Return(),
        RunDialog(
            dialog_id=DI1922_GOO,
            above_object=MEM_70A8,
            closable=False,
            sync=False,
            multiline=True,
            use_background=True,
            identifier="EVENT_3369_run_dialog_24"),
        Return(),
        RunDialog(
            dialog_id=DI1923_BONES,
            above_object=MEM_70A8,
            closable=False,
            sync=False,
            multiline=True,
            use_background=True,
            identifier="EVENT_3369_run_dialog_26"),
        Return(),
        RunDialog(
            dialog_id=DI1924_KIPP,
            above_object=MEM_70A8,
            closable=False,
            sync=False,
            multiline=True,
            use_background=True,
            identifier="EVENT_3369_run_dialog_28"),
        Return(),
        RunDialog(
            dialog_id=DI1931_MARATHON_4TH_PLACE,
            above_object=MEM_70A8,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
            identifier="EVENT_3369_run_dialog_30"),
        Return(),
        CopyVarToVar(
            from_var=TEMP_70AE,
            to_var=PRIMARY_TEMP_7000,
            identifier="EVENT_3369_set_7000_to_70A0_short_mem_32"),
        Inc(PRIMARY_TEMP_7000),
        RunDialog(
            dialog_id=DI1934_MARATHON_CONFIRM_PLACEMENT,
            above_object=MEM_70A8,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True),
        JmpIfDialogOptionBSelected(["EVENT_3366_ret_8"]),
        Inc(TEMP_70AE),
        CopyVarToVar(from_var=ACTIVE_NPC, to_var=PRIMARY_TEMP_7000),
        AddConstToVar(PRIMARY_TEMP_7000, 4),
        SetMem704XAt7000Bit(),
        CopyVarToVar(from_var=TEMP_70AE, to_var=PRIMARY_TEMP_7000),
        JmpIfVarEqualsConst(
            ACTIVE_NPC, 21, ["EVENT_3369_set_7000_short_mem_to_7000_45"]
        ),
        JmpIfVarEqualsConst(
            ACTIVE_NPC, 23, ["EVENT_3369_set_7000_short_mem_to_7000_47"]
        ),
        JmpIfVarEqualsConst(
            ACTIVE_NPC, 22, ["EVENT_3369_set_7000_short_mem_to_7000_49"]
        ),
        JmpIfVarEqualsConst(
            ACTIVE_NPC, 24, ["EVENT_3369_set_7000_short_mem_to_7000_51"]
        ),
        CopyVarToVar(
            from_var=PRIMARY_TEMP_7000,
            to_var=TEMP_702C,
            identifier="EVENT_3369_set_7000_short_mem_to_7000_45"),
        Return(),
        CopyVarToVar(
            from_var=PRIMARY_TEMP_7000,
            to_var=TEMP_702E,
            identifier="EVENT_3369_set_7000_short_mem_to_7000_47"),
        Return(),
        CopyVarToVar(
            from_var=PRIMARY_TEMP_7000,
            to_var=TEMP_7030,
            identifier="EVENT_3369_set_7000_short_mem_to_7000_49"),
        Return(),
        CopyVarToVar(
            from_var=PRIMARY_TEMP_7000,
            to_var=TEMP_7032,
            identifier="EVENT_3369_set_7000_short_mem_to_7000_51"),
        Return(),
    ]
)
