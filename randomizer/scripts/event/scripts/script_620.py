# E0620_REAL_BELLHOP_BLOCKS_EXIT_2

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        EnableControlsUntilReturn([LEFT, RIGHT, DOWN, UP, A, Y, B]),
        JmpIfBitSet(EMPLOYMENT_704C_2, ["EVENT_256_ret_0"]),
        JmpIfBitSet(TEMP_704C_0, ["EVENT_620_jmp_if_bit_set_5"]),
        JmpIfBitSet(GUEST_DROPPED_OFF, ["EVENT_620_jmp_if_bit_set_5"]),
        Return(),
        JmpIfBitSet(
            TEMP_7043_4, ["EVENT_256_ret_0"], identifier="EVENT_620_jmp_if_bit_set_5"
        ),
        SetBit(TEMP_7043_4),
        ClearBit(TEMP_7043_3),
        Set7000ToObjectCoord(object=NPC_5, coord=COORD_Y, pixel=True, bit_7=True),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 64, ["EVENT_256_ret_0"]),
        ActionQueueAsync(
            target=NPC_5,
            subscript=[
                ASSetWalkingSpeed(VERY_FAST),
                ASWalk1StepSouthwest(),
                ASFaceNorthwest(),
            ],
        ),
        Return(),
    ]
)
