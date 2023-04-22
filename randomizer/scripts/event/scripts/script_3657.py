# pylint: disable=C0301

"""E3657_ROOM_SERVICE_MENU"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        JmpIfDialogOptionBOrCSelected(
            ["EVENT_3657_set_short_41", "EVENT_3657_close_dialog_34"]
        ),
        SetVarToConst(SECONDARY_TEMP_7024, 10),
        RunEventAsSubroutine(E0274_CHECK_IF_HAVE_ENOUGH_COINS),
        JmpIfBitSet(INSUFFICIENT_COINS, ["EVENT_3657_run_dialog_52"]),
        SetVarToConst(ITEM_ID, PickMeUp),
        SetVarToConst(PRIMARY_TEMP_7000, 10),
        CopyVarToVar(from_var=PRIMARY_TEMP_7000, to_var=ROSE_WAY_703A),
        SetVarToConst(PRIMARY_TEMP_7000, 3852, identifier="EVENT_3657_set_30"),
        RunEventAsSubroutine(E3827_GRANT_ITEM_STANDARD_SOUND),
        CopyVarToVar(from_var=ROSE_WAY_703A, to_var=PRIMARY_TEMP_7000),
        Dec7000FromCoins(),
        CloseDialog(identifier="EVENT_3657_close_dialog_34"),
        ActionQueueAsync(
            target=NPC_0, subscript=[ASObjectMemoryClearBit(arg_1=0x30, bits=[4])]
        ),
        SetSyncActionScript(NPC_0, A0978_RANDOMLY_FACE_SOUTHWEST),
        SetSyncActionScript(MARIO, A0395_PLAYER_RESET_PROPERTIES_AND_SOLIDITY),
        Return(),
        SetVarToConst(SECONDARY_TEMP_7024, 150, identifier="EVENT_3657_set_short_41"),
        RunEventAsSubroutine(E0274_CHECK_IF_HAVE_ENOUGH_COINS),
        JmpIfBitSet(INSUFFICIENT_COINS, ["EVENT_3657_run_dialog_52"]),
        SetVarToConst(ITEM_ID, KerokeroCola),
        SetVarToConst(PRIMARY_TEMP_7000, 150),
        CopyVarToVar(from_var=PRIMARY_TEMP_7000, to_var=ROSE_WAY_703A),
        Jmp(["EVENT_3657_set_30"]),
        RunDialog(
            dialog_id=DI3853_ROOM_SERVICE_INSUFFICIENT_COINS,
            above_object=NPC_14,
            closable=True,
            sync=False,
            multiline=True,
            use_background=False,
            identifier="EVENT_3657_run_dialog_52",
        ),
        Jmp(["EVENT_3657_close_dialog_34"]),
    ]
)
