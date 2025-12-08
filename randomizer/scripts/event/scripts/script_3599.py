# pylint: disable=C0301

"""E3599_MUSHROOM_DERBY_PRIZE_CALCULATOR"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        SetVarToConst(SECONDARY_TEMP_7024, 0),
        SetVarToConst(TEMP_7026, 0),
        SetVarToConst(TIMER_701C, 0),
        StoreEmptyItemInventorySlotCountTo7000(),
        JmpIfVarEqualsConst(
            PRIMARY_TEMP_7000, 0, ["EVENT_3599_set_7000_to_70A0_short_mem_33"]
        ),
        CopyVarToVar(from_var=PRIMARY_TEMP_7000, to_var=SECONDARY_TEMP_7024),
        CopyVarToVar(from_var=TEMP_70B8, to_var=PRIMARY_TEMP_7000),
        Compare7000ToVar(SECONDARY_TEMP_7024),
        JmpIfComparisonResultIsLesser(["EVENT_3599_set_7000_to_70A0_short_mem_13"]),
        JmpIfLoadedMemoryIs0(["EVENT_3599_set_7000_to_70A0_short_mem_13"]),
        DecVarFrom7000(SECONDARY_TEMP_7024),
        CopyVarToVar(from_var=PRIMARY_TEMP_7000, to_var=TEMP_7026),
        Jmp(["EVENT_3599_set_7000_to_7000_short_mem_15"]),
        CopyVarToVar(
            from_var=TEMP_70B8,
            to_var=PRIMARY_TEMP_7000,
            identifier="EVENT_3599_set_7000_to_70A0_short_mem_13"),
        CopyVarToVar(from_var=PRIMARY_TEMP_7000, to_var=SECONDARY_TEMP_7024),
        CopyVarToVar(
            from_var=SECONDARY_TEMP_7024,
            to_var=PRIMARY_TEMP_7000,
            identifier="EVENT_3599_set_7000_to_7000_short_mem_15"),
        SetObjectMemoryToVar(SECONDARY_TEMP_7024),
        AddToInventory(YoshiCookie),
        EndLoop(),
        JmpIfVarEqualsConst(TEMP_7026, 0, ["EVENT_3599_set_48"]),
        CopyVarToVar(
            from_var=UNKNOWN_70D8,
            to_var=PRIMARY_TEMP_7000,
            identifier="EVENT_3599_set_7000_to_70A0_short_mem_20"),
        AddVarTo7000(TEMP_7026),
        CopyVarToVar(from_var=PRIMARY_TEMP_7000, to_var=SECONDARY_TEMP_7024),
        CompareVarToConst(PRIMARY_TEMP_7000, 201),
        JmpIfComparisonResultIsGreaterOrEqual(["EVENT_3599_set_short_36"]),
        CopyVarToVar(from_var=TEMP_7026, to_var=PRIMARY_TEMP_7000),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 1, ["EVENT_3599_run_dialog_31"]),
        RunDialog(
            dialog_id=DI0950_TOO_MANY_COOKIES,
            above_object=NPC_12,
            closable=True,
            sync=False,
            multiline=True,
            use_background=False),
        CopyVarToVar(
            from_var=SECONDARY_TEMP_7024,
            to_var=PRIMARY_TEMP_7000,
            identifier="EVENT_3599_set_7000_to_7000_short_mem_28"),
        CopyVarToVar(from_var=PRIMARY_TEMP_7000, to_var=UNKNOWN_70D8),
        Jmp(["EVENT_3599_set_48"]),
        RunDialog(
            dialog_id=DI2362_STORE_EXTRA_COOKIES_AFTER_WINNING,
            above_object=NPC_12,
            closable=True,
            sync=False,
            multiline=True,
            use_background=False,
            identifier="EVENT_3599_run_dialog_31"),
        Jmp(["EVENT_3599_set_7000_to_7000_short_mem_28"]),
        CopyVarToVar(
            from_var=TEMP_70B8,
            to_var=PRIMARY_TEMP_7000,
            identifier="EVENT_3599_set_7000_to_70A0_short_mem_33"),
        CopyVarToVar(from_var=PRIMARY_TEMP_7000, to_var=TEMP_7026),
        Jmp(["EVENT_3599_set_7000_to_70A0_short_mem_20"]),
        SetVarToConst(SECONDARY_TEMP_7024, 200, identifier="EVENT_3599_set_short_36"),
        DecVarFrom7000(SECONDARY_TEMP_7024),
        CopyVarToVar(from_var=PRIMARY_TEMP_7000, to_var=SECONDARY_TEMP_7024),
        CopyVarToVar(from_var=UNKNOWN_70D8, to_var=PRIMARY_TEMP_7000),
        CopyVarToVar(from_var=PRIMARY_TEMP_7000, to_var=TEMP_7026),
        SetVarToConst(PRIMARY_TEMP_7000, 200),
        DecVarFrom7000(TEMP_7026),
        RunDialog(
            dialog_id=DI2510_WON_COOKIES_IN_EXCESS,
            above_object=NPC_12,
            closable=True,
            sync=False,
            multiline=True,
            use_background=False),
        PlaySound(sound=SO061_DEEP_UHOH, channel=6),
        Pause(60),
        RunDialog(
            dialog_id=DI0952_DUPLICATE,
            above_object=MARIO,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True),
        SetVarToConst(UNKNOWN_70D8, 200),
        SetVarToConst(TEMP_70AE, 0, identifier="EVENT_3599_set_48"),
        SetVarToConst(TEMP_70B8, 0),
        SetVarToConst(SECONDARY_TEMP_7024, 0),
        SetVarToConst(TEMP_7026, 0),
        Return(),
    ]
)
