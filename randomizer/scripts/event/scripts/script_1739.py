# pylint: disable=C0301

"""E1739_REFOCUS_CAMERA"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        Db(bytearray(b"\xc7\x93")),
        AddConstToVar(X_COORD_2, 65532),
        CompareVarToConst(X_COORD_2, 32768),
        JmpIfComparisonResultIsLesser(["EVENT_1739_add_short_5"]),
        SetVarToConst(X_COORD_2, 0),
        AddConstToVar(Y_COORD_2, 65520, identifier="EVENT_1739_add_short_5"),
        CopyVarToVar(from_var=Z_COORD_2, to_var=PRIMARY_TEMP_7000),
        Mem7000XorConst(0xFFFF),
        Inc(PRIMARY_TEMP_7000),
        AddVarTo7000(Y_COORD_2),
        CompareVarToConst(PRIMARY_TEMP_7000, 32768),
        JmpIfComparisonResultIsLesser(["EVENT_1739_set_7000_short_mem_to_7000_13"]),
        SetVarToConst(PRIMARY_TEMP_7000, 0),
        CopyVarToVar(
            from_var=PRIMARY_TEMP_7000,
            to_var=Y_COORD_2,
            identifier="EVENT_1739_set_7000_short_mem_to_7000_13"),
        SetVarToConst(Z_COORD_2, 0),
        ActionQueueAsync(
            target=SCREEN_FOCUS,
            subscript=[
                ASJmpIfBitSet(
                    SKY_BRIDGE_PAN,
                    [
                        "EVENT_1739_action_queue_async_15_SUBSCRIPT_set_animation_speed_4"
                    ]),
                ASJmpIfBitSet(
                    UNKNOWN_PAN,
                    [
                        "EVENT_1739_action_queue_async_15_SUBSCRIPT_set_animation_speed_6"
                    ]),
                ASSetWalkingSpeed(FASTEST),
                ASJmp(["EVENT_1739_action_queue_async_15_SUBSCRIPT_db_7"]),
                ASSetWalkingSpeed(
                    FASTEST,
                    identifier="EVENT_1739_action_queue_async_15_SUBSCRIPT_set_animation_speed_4"),
                ASJmp(["EVENT_1739_action_queue_async_15_SUBSCRIPT_db_7"]),
                ASSetWalkingSpeed(
                    FASTEST,
                    identifier="EVENT_1739_action_queue_async_15_SUBSCRIPT_set_animation_speed_6"),
                ASDb(
                    bytearray(b"\x98"),
                    identifier="EVENT_1739_action_queue_async_15_SUBSCRIPT_db_7"),
                ASSetWalkingSpeed(FASTEST),
            ]),
        Return(),
    ]
)
