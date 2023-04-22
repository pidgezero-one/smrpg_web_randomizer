# pylint: disable=C0301

"""E1805_TEMPLE_3_FORTUNE_SHAMAN"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        CopyVarToVar(from_var=ACTIVE_NPC, to_var=PRIMARY_TEMP_7000),
        CopyVarToVar(from_var=PRIMARY_TEMP_7000, to_var=TEMP_70AE),
        JmpIfMarioOnAnObjectOrNot(["EVENT_1805_set_41", "EVENT_1805_set_41"]),
        StoreCoinCountTo7000(),
        CompareVarToConst(PRIMARY_TEMP_7000, 50),
        JmpIfComparisonResultIsLesser(["EVENT_1805_run_dialog_39"]),
        RunDialog(
            dialog_id=DI1240_FORTUNE_SHAMAN_PROMPT,
            above_object=MEM_70A8,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        JmpIfDialogOptionBSelected(["EVENT_1805_pause_44"]),
        Pause(10),
        SetAsyncActionScript(MARIO, A0670_NOD_YES),
        ActionQueueAsync(
            target=MEM_70A8,
            subscript=[
                ASSetSequenceSpeed(VERY_FAST),
                ASSequenceLoopingOn(),
                ASPause(30),
                ASSetSequenceSpeed(VERY_SLOW),
            ],
        ),
        SetVarToConst(PRIMARY_TEMP_7000, 50),
        Dec7000FromCoins(),
        PlaySound(sound=SO055_LOSE_COINS_COIN_FOUNTAIN, channel=6),
        RunDialog(
            dialog_id=DI1241_FORTUNE_SHAMAN_INSTRUCTIONS,
            above_object=MEM_70A8,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        SetVarToConst(TEMP_70AA, 23),
        JmpToSubroutine(["EVENT_1794_action_queue_async_73"]),
        SetBit(BELOME_FORTUNE_1),
        ClearBit(UNKNOWN_BELOME_FORTUNE),
        Inc(UNKNOWN_70AD),
        JmpIfBitClear(HAS_A_PRIZE_FORTUNE, ["EVENT_1805_ret_38"]),
        Pause(16),
        SetVarToConst(TEMP_70AB, 24),
        RunEventAsSubroutine(E1739_REFOCUS_CAMERA),
        PlaySound(sound=SO084_SMOKED, channel=6),
        ActionQueueSync(
            target=NPC_0,
            subscript=[
                ASVisibilityOff(),
                ASTransferToXYZF(x=10, y=26, z=20, direction=EAST),
            ],
        ),
        ActionQueueSync(
            target=NPC_1,
            subscript=[
                ASVisibilityOff(),
                ASTransferToXYZF(x=10, y=26, z=23, direction=EAST),
            ],
        ),
        SetVarToConst(TEMP_7034, 1),
        Set70107015ToObjectXYZ(NPC_0),
        StartLoopNTimes(14),
        Pause(1, identifier="EVENT_1805_pause_30"),
        CreatePacketAt7010(
            packet=P032_BLUE_CLOUD, destinations=["EVENT_1805_pause_30"]
        ),
        Pause(4),
        AddConstToVar(TEMP_7034, 3),
        AddConstToVar(Z_COORD_1, 80),
        EndLoop(),
        SetVarToConst(TEMP_70AB, 0),
        RunEventAsSubroutine(E1739_REFOCUS_CAMERA),
        RemoveObjectFromSpecificLevel(NPC_3, R420_BELOME_TEMPLE_AREA_02_FORTUNE_ROOM),
        Return(identifier="EVENT_1805_ret_38"),
        RunDialog(
            dialog_id=DI1239_FORTUNE_SHAMAN_NOT_ENOUGH_COINS,
            above_object=MEM_70A8,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
            identifier="EVENT_1805_run_dialog_39",
        ),
        Return(),
        SetVarToConst(TEMP_70AA, 23, identifier="EVENT_1805_set_41"),
        JmpToSubroutine(["EVENT_1794_action_queue_async_73"]),
        Return(),
        Pause(10, identifier="EVENT_1805_pause_44"),
        SetAsyncActionScript(MARIO, A0671_SHAKE_HEAD_NO),
        Return(),
    ]
)
