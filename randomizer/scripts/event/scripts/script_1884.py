# pylint: disable=C0301

"""E1884_WHIRLPOOL_SHOGUN_2"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        CopyVarToVar(from_var=ACTIVE_NPC, to_var=PRIMARY_TEMP_7000),
        CopyVarToVar(from_var=PRIMARY_TEMP_7000, to_var=TEMP_70AF),
        JmpIfBitClear(TEMP_7043_1, ["EVENT_1884_jmp_if_bit_set_4"]),
        JmpIfMarioOnAnObjectOrNot(
            [
                "EVENT_1745_freeze_all_npcs_until_return_43",
                "EVENT_1884_jmp_if_bit_set_4",
            ]
        ),
        JmpIfBitSet(
            SHOGUN_2_CLEARED,
            ["EVENT_1884_jmp_to_subroutine_9"],
            identifier="EVENT_1884_jmp_if_bit_set_4",
        ),
        RunEventAsSubroutine(E1745_WHIRLPOOL_SHOGUN),
        JmpIfBitClear(TEMP_7043_3, ["EVENT_1884_ret_8"]),
        SetBit(SHOGUN_2_CLEARED),
        Return(identifier="EVENT_1884_ret_8"),
        JmpToSubroutine(
            ["EVENT_1745_freeze_all_npcs_until_return_60"],
            identifier="EVENT_1884_jmp_to_subroutine_9",
        ),
        ActionQueueSync(
            target=NPC_6,
            subscript=[
                ASPause(90),
                ASSummonObjectToSpecificLevel(NPC_6, R402_LANDS_END_DESERT_AREA_03),
                ASObjectMemoryClearBit(arg_1=0x30, bits=[4]),
            ],
        ),
        Return(),
    ]
)
