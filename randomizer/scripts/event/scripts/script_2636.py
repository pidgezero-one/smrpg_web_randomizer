# pylint: disable=C0301

"""E2636_CASINO_GUARD"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        SetVarToConst(ITEM_ID, BrightCard),
        StoreItemAt70A7QuantityTo7000(),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 0, ["EVENT_2636_jmp_if_bit_set_13"]),
        JmpIfBitSet(DIRECTIONAL_7046_1, ["EVENT_2636_run_dialog_11"]),
        RunDialog(
            dialog_id=DI3300_BOUNCER_ALLOW,
            above_object=MEM_70A8,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True),
        JmpIfBitSet(TEMP_7043_0, ["EVENT_2636_ret_10"]),
        SetBit(TEMP_7043_0),
        ApplySolidityModToLevel(
            permanent=True, room_id=R104_GRATE_GUYS_CASINO_FRONT_DOOR, mod_id=0
        ),
        ActionQueueSync(target=NPC_0, subscript=[ASWalkNorthwestPixels(8)]),
        ActionQueueAsync(target=NPC_1, subscript=[ASWalkSoutheastPixels(8)]),
        Return(identifier="EVENT_2636_ret_10"),
        RunDialog(
            dialog_id=DI3301_BOUNCER_LEAVE,
            above_object=MEM_70A8,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
            identifier="EVENT_2636_run_dialog_11"),
        Return(),
        JmpIfBitSet(
            KNIFE_GUY_PRIZE_GRANTED,
            ["EVENT_2636_run_dialog_16"],
            identifier="EVENT_2636_jmp_if_bit_set_13"),
        RunDialog(
            dialog_id=DI3298_BOUNCER_REJECT,
            above_object=MEM_70A8,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True),
        Return(),
        RunDialog(
            dialog_id=DI3299_BOUNCER_REJECT,
            above_object=MEM_70A8,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
            identifier="EVENT_2636_run_dialog_16"),
        Return(),
    ]
)
