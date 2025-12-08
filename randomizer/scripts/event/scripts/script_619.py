# pylint: disable=C0301

"""E0619_REAL_BELLHOP_BLOCKS_EXIT_1"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        EnableControlsUntilReturn([LEFT, RIGHT, DOWN, UP, A, Y, B]),
        JmpIfBitSet(EMPLOYMENT_704C_2, ["EVENT_256_ret_0"]),
        JmpIfBitSet(TEMP_704C_0, ["EVENT_619_jmp_if_bit_set_5"]),
        JmpIfBitSet(GUEST_DROPPED_OFF, ["EVENT_619_jmp_if_bit_set_5"]),
        Return(),
        JmpIfBitSet(
            TEMP_7043_3, ["EVENT_256_ret_0"], identifier="EVENT_619_jmp_if_bit_set_5"
        ),
        SetBit(TEMP_7043_3),
        ClearBit(TEMP_7043_4),
        Set7000ToObjectCoord(target_npc=NPC_5, coord=COORD_Y, pixel=True, bit_7=True),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 63, ["EVENT_256_ret_0"]),
        ActionQueueAsync(
            target=NPC_5,
            subscript=[
                ASSetWalkingSpeed(VERY_FAST),
                ASWalk1StepNortheast(),
                ASFaceNorthwest(),
            ]),
        Return(),
    ]
)
