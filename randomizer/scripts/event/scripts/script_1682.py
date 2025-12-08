# pylint: disable=C0301

"""E1682_TRAMPOLINE_SHAMAN"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        CopyVarToVar(
            from_var=ACTIVE_NPC,
            to_var=PRIMARY_TEMP_7000,
            identifier="EVENT_1682_set_7000_to_70A0_short_mem_0"),
        CopyVarToVar(from_var=PRIMARY_TEMP_7000, to_var=TEMP_70AE),
        StoreCoinCountTo7000(),
        CompareVarToConst(PRIMARY_TEMP_7000, 100),
        JmpIfComparisonResultIsLesser(["EVENT_1682_action_queue_async_19"]),
        RunDialog(
            dialog_id=DI1228_SHAMAN_TRAMPOLINE_SALE,
            above_object=NPC_12,
            closable=True,
            sync=False,
            multiline=True,
            use_background=False),
        JmpIfDialogOptionBSelected(["EVENT_1682_pause_22"]),
        Pause(10),
        SetAsyncActionScript(MARIO, A0670_NOD_YES),
        ActionQueueAsync(
            target=NPC_0,
            subscript=[
                ASSetSequenceSpeed(VERY_FAST),
                ASSequenceLoopingOn(),
                ASPause(30),
                ASSetSequenceSpeed(VERY_SLOW),
            ]),
        SetVarToConst(PRIMARY_TEMP_7000, 100),
        Dec7000FromCoins(),
        PlaySound(sound=SO055_LOSE_COINS_COIN_FOUNTAIN, channel=6),
        Pause(50),
        SetVarToConst(TEMP_70AA, 20),
        JmpToSubroutine(["EVENT_1794_action_queue_async_73"]),
        RemoveObjectFromSpecificLevel(
            NPC_0, R428_BELOME_TEMPLE_AREA_01_WWARP_TRAMPOLINE
        ),
        SetBit(TRAMPOLINE_SHAMAN_PAID),
        Return(),
        ActionQueueAsync(
            target=NPC_0,
            subscript=[ASFaceMario()],
            identifier="EVENT_1682_action_queue_async_19"),
        RunDialog(
            dialog_id=DI1229_SHAMAN_TRAMPOLINE_SALE_NOT_ENOUGH_MONEY,
            above_object=NPC_12,
            closable=True,
            sync=False,
            multiline=True,
            use_background=False),
        Return(),
        Pause(10, identifier="EVENT_1682_pause_22"),
        SetAsyncActionScript(MARIO, A0671_SHAKE_HEAD_NO),
        Return(),
    ]
)
