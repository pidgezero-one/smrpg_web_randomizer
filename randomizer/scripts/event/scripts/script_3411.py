# pylint: disable=C0301

"""E3411_SHIP_PASSWORD_CORRECTNESS_CHECK"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        JmpIfVarNotEqualsConst(
            SECONDARY_TEMP_7024, 4, ["EVENT_3411_jmp_if_var_not_equals_const_33"]
        ),
        Inc(TEMP_70AC),
        JmpIfVarNotEqualsConst(
            TEMP_7026,
            2,
            ["EVENT_3411_jmp_if_var_not_equals_const_35"],
            identifier="EVENT_3411_jmp_if_var_not_equals_const_33",
        ),
        Inc(TEMP_70AC),
        JmpIfVarNotEqualsConst(
            TEMP_7028,
            0,
            ["EVENT_3411_jmp_if_var_not_equals_const_37"],
            identifier="EVENT_3411_jmp_if_var_not_equals_const_35",
        ),
        Inc(TEMP_70AC),
        JmpIfVarNotEqualsConst(
            TEMP_702A,
            2,
            ["EVENT_3411_jmp_if_var_not_equals_const_39"],
            identifier="EVENT_3411_jmp_if_var_not_equals_const_37",
        ),
        Inc(TEMP_70AC),
        JmpIfVarNotEqualsConst(
            TEMP_702C,
            3,
            ["EVENT_3411_jmp_if_var_not_equals_const_41"],
            identifier="EVENT_3411_jmp_if_var_not_equals_const_39",
        ),
        Inc(TEMP_70AC),
        JmpIfVarNotEqualsConst(
            TEMP_702E,
            0,
            ["EVENT_3411_ret"],
            identifier="EVENT_3411_jmp_if_var_not_equals_const_41",
        ),
        Inc(TEMP_70AC),
        Return(identifier="EVENT_3411_ret"),
    ]
)
