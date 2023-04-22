# pylint: disable=C0301

"""E3091_MULTI_FROG_COIN_CHEST_SINGLE_HIT"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        CopyVarToVar(from_var=ITEM_ID, to_var=PRIMARY_TEMP_7000),
        SetVarToConst(PRIMARY_TEMP_7000, 0),
        JmpIfVarEqualsConst(
            COIN_CHEST_MULTIPLIER,
            0,
            ["EVENT_3091_store_multiplier"],
            identifier="EVENT_3091_check_multiplier",
        ),
        AddConstToVar(PRIMARY_TEMP_7000, 15),
        Dec(COIN_CHEST_MULTIPLIER),
        Jmp(["EVENT_3091_check_multiplier"]),
        CopyVarToVar(
            from_var=PRIMARY_TEMP_7000,
            to_var=COIN_CHEST_MULTIPLIER,
            identifier="EVENT_3091_store_multiplier",
        ),
        CopyVarToVar(from_var=ITEM_ID, to_var=PRIMARY_TEMP_7000),
        Mem7000AndConst(0x000F),
        AddVarTo7000(COIN_CHEST_MULTIPLIER),
        CopyVarToVar(from_var=PRIMARY_TEMP_7000, to_var=COIN_CHEST_MULTIPLIER),
        SetVarToConst(PRIMARY_TEMP_7000, 0),
        JmpIfVarEqualsConst(
            COIN_CHEST_MULTIPLIER,
            0,
            ["EVENT_3091_add_coins_260"],
            identifier="EVENT_3091_use_multiplier",
        ),
        Inc(PRIMARY_TEMP_7000),
        Dec(COIN_CHEST_MULTIPLIER),
        Jmp(["EVENT_3091_use_multiplier"]),
        AddFrogCoins(PRIMARY_TEMP_7000, identifier="EVENT_3091_add_coins_260"),
        SummonObjectToCurrentLevel(MEM_70A8),
        RunDialog(
            dialog_id=DI1310_RECEIVED_X_FROG_COINS,
            above_object=MARIO,
            closable=False,
            sync=True,
            multiline=False,
            use_background=False,
            bit_6=True,
        ),
        DisableObjectTrigger(MEM_70A8),
        PlaySound(sound=SO005_BLOCK_SWITCH, channel=6),
        DisableTriggerOfObjectAt70A8InCurrentLevel(),
        SetSyncActionScript(MEM_70A8, A0007_HIT_TREASURE_CHEST_CONTENTS_DEPLETED),
        Set70107015ToObjectXYZ(MEM_70A8),
        CopyVarToVar(from_var=Z_COORD_1, to_var=PRIMARY_TEMP_7000),
        AddConstToVar(PRIMARY_TEMP_7000, 608),
        CopyVarToVar(from_var=PRIMARY_TEMP_7000, to_var=Z_COORD_1),
        JmpIfBitSet(UNKNOWN_704A_3, ["EVENT_3091_clear_bit_273"]),
        PlaySound(sound=SO094_FROG_COIN, channel=6),
        ClearBit(UNKNOWN_704A_3, identifier="EVENT_3091_clear_bit_273"),
        CreatePacketAt7010(
            packet=P019_FROG_COIN_BEING_COLLECTED, destinations=["EVENT_3091_ret"]
        ),
        Return(identifier="EVENT_3091_ret"),
    ]
)
