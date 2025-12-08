# pylint: disable=C0301

"""E1692_TEMPLE_FORTUNE_SCROLL"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        ClearBit(UNKNOWN_BELOME_TEMPLE, identifier="EVENT_1692_clear_bit_0"),
        PlaySound(sound=SO084_SMOKED, channel=6),
        SetVarToConst(TEMP_7034, 1),
        Set70107015ToObjectXYZ(NPC_2),
        StartLoopNTimes(2),
        Pause(1, identifier="EVENT_1692_pause_5"),
        CreatePacketAt7010(packet=P032_BLUE_CLOUD, destinations=["EVENT_1692_pause_5"]),
        Pause(4),
        AddConstToVar(TEMP_7034, 3),
        EndLoop(),
        RemoveObjectFromCurrentLevel(NPC_2),
        RemoveObjectFromSpecificLevel(
            NPC_6, R421_BELOME_TEMPLE_AREA_04_ROOM_DETERMINED_BY_FORTUNE
        ),
        RemoveObjectFromSpecificLevel(
            NPC_7, R421_BELOME_TEMPLE_AREA_04_ROOM_DETERMINED_BY_FORTUNE
        ),
        RemoveObjectFromSpecificLevel(
            NPC_8, R421_BELOME_TEMPLE_AREA_04_ROOM_DETERMINED_BY_FORTUNE
        ),
        RemoveObjectFromSpecificLevel(
            NPC_9, R421_BELOME_TEMPLE_AREA_04_ROOM_DETERMINED_BY_FORTUNE
        ),
        RunDialog(
            dialog_id=DI1249_FORTUNE_PREAMBLE,
            above_object=BOWSER,
            closable=False,
            sync=False,
            multiline=True,
            use_background=False),
        CopyVarToVar(from_var=TEMP_70AC, to_var=PRIMARY_TEMP_7000),
        Mem7000AndConst(0x000F),
        JmpIfVarEqualsConst(
            PRIMARY_TEMP_7000, 9, ["EVENT_1692_run_dialog_duration_30"]
        ),
        JmpIfVarEqualsConst(
            PRIMARY_TEMP_7000, 13, ["EVENT_1692_run_dialog_duration_39"]
        ),
        JmpIfVarEqualsConst(
            PRIMARY_TEMP_7000, 6, ["EVENT_1692_run_dialog_duration_43"]
        ),
        JmpIfVarEqualsConst(
            PRIMARY_TEMP_7000, 14, ["EVENT_1692_run_dialog_duration_48"]
        ),
        JmpIfVarEqualsConst(
            PRIMARY_TEMP_7000, 7, ["EVENT_1692_run_dialog_duration_56"]
        ),
        JmpIfVarEqualsConst(
            PRIMARY_TEMP_7000, 11, ["EVENT_1692_run_dialog_duration_65"]
        ),
        RunDialogForDuration(
            dialog_id=DI1242_UNUSED_DEFAULT_FORTUNE, duration=1, sync=False
        ),
        Return(),
        RunDialogForDuration(
            dialog_id=DI1243_FORTUNE_1,
            duration=1,
            sync=False,
            identifier="EVENT_1692_run_dialog_duration_30"),
        SummonObjectToSpecificLevel(
            NPC_6, R421_BELOME_TEMPLE_AREA_04_ROOM_DETERMINED_BY_FORTUNE
        ),
        JmpIfObjectTriggerDisabledInSpecificLevel(
            NPC_6,
            R421_BELOME_TEMPLE_AREA_04_ROOM_DETERMINED_BY_FORTUNE,
            ["EVENT_1692_ret_68_-"]),
        Return(),
        RunDialogForDuration(
            dialog_id=DI1244_FORTUNE_2,
            duration=1,
            sync=False,
            identifier="EVENT_1692_run_dialog_duration_39"),
        SummonObjectToSpecificLevel(
            NPC_7, R421_BELOME_TEMPLE_AREA_04_ROOM_DETERMINED_BY_FORTUNE
        ),
        JmpIfObjectTriggerDisabledInSpecificLevel(
            NPC_7,
            R421_BELOME_TEMPLE_AREA_04_ROOM_DETERMINED_BY_FORTUNE,
            ["EVENT_1692_ret_68_-"]),
        Return(),
        RunDialogForDuration(
            dialog_id=DI1245_FORTUNE_3,
            duration=1,
            sync=False,
            identifier="EVENT_1692_run_dialog_duration_43"),
        SummonObjectToSpecificLevel(
            NPC_0, R421_BELOME_TEMPLE_AREA_04_ROOM_DETERMINED_BY_FORTUNE
        ),
        SummonObjectToSpecificLevel(
            NPC_1, R421_BELOME_TEMPLE_AREA_04_ROOM_DETERMINED_BY_FORTUNE
        ),
        SummonObjectToSpecificLevel(
            NPC_2, R421_BELOME_TEMPLE_AREA_04_ROOM_DETERMINED_BY_FORTUNE
        ),
        Return(),
        RunDialogForDuration(
            dialog_id=DI1246_FORTUNE_4,
            duration=1,
            sync=False,
            identifier="EVENT_1692_run_dialog_duration_48"),
        SummonObjectToSpecificLevel(
            NPC_5, R421_BELOME_TEMPLE_AREA_04_ROOM_DETERMINED_BY_FORTUNE
        ),
        Return(),
        RunDialogForDuration(
            dialog_id=DI1247_FORTUNE_5,
            duration=1,
            sync=False,
            identifier="EVENT_1692_run_dialog_duration_56"),
        SummonObjectToSpecificLevel(
            NPC_8, R421_BELOME_TEMPLE_AREA_04_ROOM_DETERMINED_BY_FORTUNE
        ),
        JmpIfObjectTriggerDisabledInSpecificLevel(
            NPC_8,
            R421_BELOME_TEMPLE_AREA_04_ROOM_DETERMINED_BY_FORTUNE,
            ["EVENT_1692_ret_68_-"]),
        Return(),
        RunDialogForDuration(
            dialog_id=DI1248_FORTUNE_6,
            duration=1,
            sync=False,
            identifier="EVENT_1692_run_dialog_duration_65"),
        SummonObjectToSpecificLevel(
            NPC_9, R421_BELOME_TEMPLE_AREA_04_ROOM_DETERMINED_BY_FORTUNE
        ),
        JmpIfObjectTriggerDisabledInSpecificLevel(
            NPC_9,
            R421_BELOME_TEMPLE_AREA_04_ROOM_DETERMINED_BY_FORTUNE,
            ["EVENT_1692_ret_68_-"]),
        Return(),
        SetBit(HAS_A_PRIZE_FORTUNE, identifier="EVENT_1692_ret_68_-"),
        Return(),
    ]
)
