# pylint: disable=C0301

"""E1633_MOLEVILLE_INN"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        JmpIfBitSet(MOLEVILLE_TOADOFSKY_HINT, ["EVENT_1633_set_short_4"]),
        JmpIfBitClear(MINECART_CLEARED, ["EVENT_1633_set_short_4"]),
        RunDialog(
            dialog_id=DI1091_MOLEVILLE_INN_TOADOFSKY_HINT,
            above_object=MEM_70A8,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        SetBit(MOLEVILLE_TOADOFSKY_HINT),
        SetVarToConst(SECONDARY_TEMP_7024, 10, identifier="EVENT_1633_set_short_4"),
        SetVarToConst(PRIMARY_TEMP_7000, 1088),
        SetVarToConst(TEMP_70AE, 20),
        JmpToSubroutine(["EVENT_1633_clear_bit_12"]),
        JmpIfBitSet(TEMP_7043_0, ["EVENT_1633_set_bit_10"]),
        Return(),
        SetBit(MOLEVILLE_INN, identifier="EVENT_1633_set_bit_10"),
        JmpToEvent(E0280_SLEEP_IN_NIMBUS_INN),
        ClearBit(TEMP_7043_0, identifier="EVENT_1633_clear_bit_12"),
        RunDialog(
            dialog_id=PRIMARY_TEMP_7000,
            above_object=MEM_70A8,
            closable=False,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        Db(bytearray(b"\xbd\x00\x13")),
        StoreCoinCountTo7000(),
        Compare7000ToVar(SECONDARY_TEMP_7024),
        JmpIfComparisonResultIsGreaterOrEqual(["EVENT_1633_db_23"]),
        Db(bytearray(b"\xbd\x00\x13")),
        Inc(PRIMARY_TEMP_7000),
        Inc(PRIMARY_TEMP_7000),
        AppendDialogAt7000ToCurrentDialog(closable=True, sync=False),
        Return(),
        Db(bytearray(b"\xbd\x00\x13"), identifier="EVENT_1633_db_23"),
        Inc(PRIMARY_TEMP_7000),
        AppendDialogAt7000ToCurrentDialog(closable=True, sync=False),
        JmpIfDialogOptionBSelected(["EVENT_1633_pause_33"]),
        CopyVarToVar(from_var=SECONDARY_TEMP_7024, to_var=PRIMARY_TEMP_7000),
        Dec7000FromCoins(),
        Pause(10),
        SetAsyncActionScript(MARIO, A0670_NOD_YES),
        SetBit(TEMP_7043_0),
        Return(),
        Pause(10, identifier="EVENT_1633_pause_33"),
        SetAsyncActionScript(MARIO, A0671_SHAKE_HEAD_NO),
        Return(),
    ]
)
