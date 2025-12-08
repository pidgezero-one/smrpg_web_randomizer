# pylint: disable=C0301

"""E0338_MUSHROOM_KINGDOM_SHOPKEEPER"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        Db(bytearray(b"\xc7\x80")),
        CompareVarToConst(Z_COORD_1, 5),
        JmpIfComparisonResultIsGreaterOrEqual(["EVENT_338_run_dialog_9"]),
        CompareVarToConst(Y_COORD_1, 19),
        JmpIfComparisonResultIsLesser(["EVENT_338_run_dialog_9"]),
        JmpIfLoadedMemoryIs0(["EVENT_338_mem_compare_11"]),
        Jmp(["EVENT_338_jmp_if_bit_set_355"]),
        RunDialog(
            dialog_id=DI0609_SHOPKEEPER_YELLS_AT_YOU_BEHIND_COUNTER,
            above_object=MEM_70A8,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
            identifier="EVENT_338_run_dialog_9"),
        Return(),
        CompareVarToConst(X_COORD_1, 14, identifier="EVENT_338_mem_compare_11"),
        JmpIfComparisonResultIsGreaterOrEqual(["EVENT_338_run_dialog_9"]),
        JmpToEvent(
            E0290_MUSHROOM_KINGDOM_SHOP_LOGIC, identifier="EVENT_338_jmp_if_bit_set_355"
        ),
    ]
)
