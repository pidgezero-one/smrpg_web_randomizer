# pylint: disable=C0301

"""E1172_MUSHROOM_BOY"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        JmpIfBitSet(UNKNOWN_7087_2, ["EVENT_1172_run_dialog_3"]),
        RunDialog(
            dialog_id=DI2928_MUSHROOM_BOY_INTRO,
            above_object=MEM_70A8,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True),
        SetBit(UNKNOWN_7087_2),
        RunDialog(
            dialog_id=DI2929_MUSHROOM_BOY_PROMPT,
            above_object=MEM_70A8,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
            identifier="EVENT_1172_run_dialog_3"),
        JmpIfDialogOptionBSelected(["EVENT_1172_run_dialog_35"]),
        StoreItemAmountTo7000(Mushroom),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 0, ["EVENT_1172_run_dialog_34"]),
        RunDialog(
            dialog_id=DI2930_MUSHROOM_BOY_CONFIRM,
            above_object=MEM_70A8,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True),
        RemoveOneOfItemFromInventory(Mushroom),
        ActionQueueAsync(
            target=NPC_0,
            subscript=[ASSequenceLoopingOff(), ASPause(85), ASSequenceLoopingOn()]),
        RunEventAsSubroutine(E1972_MUSHROOM_BOY_ODDS),
        CompareVarToConst(PRIMARY_TEMP_7000, 400),
        JmpIfComparisonResultIsLesser(["EVENT_1172_run_dialog_19"]),
        CompareVarToConst(PRIMARY_TEMP_7000, 1000),
        JmpIfComparisonResultIsLesser(["EVENT_1172_run_dialog_24"]),
        CompareVarToConst(PRIMARY_TEMP_7000, 2400),
        JmpIfComparisonResultIsLesser(["EVENT_1172_run_dialog_29"]),
        JmpToEvent(E1973_CLONE_RESERVED),
        PlaySound(sound=SO085_FLOWER, channel=6, identifier="EVENT_1172_run_dialog_19"),
        RunDialog(
            dialog_id=DI2939_RECEIVED_FLOWER_TAB,
            above_object=BOWSER,
            closable=True,
            sync=False,
            multiline=False,
            use_background=False),
        AddToInventory(FlowerTab),
        Return(),
        JmpToEvent(
            E1971_MUSHROOM_BOY_GRANTS_ROCK_CANDY, identifier="EVENT_1172_run_dialog_24"
        ),
        PlaySound(sound=SO085_FLOWER, channel=6, identifier="EVENT_1172_run_dialog_29"),
        RunDialog(
            dialog_id=DI2937_RECEIVED_MAPLE_SYRUP,
            above_object=BOWSER,
            closable=True,
            sync=False,
            multiline=False,
            use_background=False),
        AddToInventory(MapleSyrup),
        Return(),
        RunDialog(
            dialog_id=DI2936_NO_MUSHROOMS,
            above_object=MEM_70A8,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
            identifier="EVENT_1172_run_dialog_34"),
        RunDialog(
            dialog_id=DI2935_MUSHROOM_BOY_GOODBYE,
            above_object=MEM_70A8,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
            identifier="EVENT_1172_run_dialog_35"),
        Return(),
    ]
)
