"""A0049_SEWERS_3RD_WATER_ROOM_RATS"""

from randomizer.scripts.action.script_imports import *

script = ActionScript(
    [
        ObjectMemorySetBit(
            arg_1=0x0B, bits=[3], identifier="ACTION_49_object_memory_set_bit_0"
        ),
        ClearSolidityBits(cant_pass_walls=True, cant_pass_npcs=True, bit_7=True),
        Pause(13),
        Inc(TEMP_702C),
        Walk1StepSouthwest(),
        Walk1StepSoutheast(),
        WalkSouthwestSteps(3),
        WalkNorthwestSteps(3),
        JmpIfRandom1of2(["ACTION_49_shift_southeast_steps_13"]),
        WalkNortheastSteps(3),
        WalkSoutheastSteps(2),
        Walk1StepNortheast(),
        Jmp(["ACTION_49_object_memory_set_bit_0"]),
        WalkSoutheastSteps(2, identifier="ACTION_49_shift_southeast_steps_13"),
        WalkNortheastSteps(4),
        Jmp(["ACTION_49_object_memory_set_bit_0"]),
    ]
)
