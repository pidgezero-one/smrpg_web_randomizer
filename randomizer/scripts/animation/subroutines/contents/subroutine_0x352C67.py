# pylint: disable=C0301,C0103

"""referenced by monster_spells Electroshock, monster_attacks Poison"""

from randomizer.scripts.animation.script_imports import *

script = SubroutineOrBanklessScript(
    expected_size=18,
    script=[
        ResetObjectMappingMemory(identifier="queuestart_0x352c67"),
        MoveObject(
            speed=1,
            start_position=512,
            end_position=0,
            apply_to_y=True,
            should_set_speed=True,
        ),
        ReturnSubroutine(),
        SetAMEMToRandom(amem=0x60, upper_bound=6),
        ObjectQueueAtOffsetAndIndexAtAMEM60(target_address=0x352C79),
        ReturnSubroutine(),
    ],
)
