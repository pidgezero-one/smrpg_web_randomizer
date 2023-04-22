# pylint: disable=C0301,C0103

"""referenced by battle_events BE0044_CZAR_DRAGON_DIES"""

from randomizer.scripts.animation.script_imports import *

script = SubroutineOrBanklessScript(
    expected_size=26,
    script=[
        ResetObjectMappingMemory(identifier="queuestart_0x3a7f92"),
        MoveObject(
            speed=1,
            start_position=-513,
            end_position=0,
            apply_to_x=True,
            should_set_speed=True,
        ),
        MoveObject(
            speed=1,
            start_position=256,
            end_position=0,
            apply_to_y=True,
            should_set_speed=True,
        ),
        ReturnSubroutine(),
        SetAMEMToRandom(amem=0x60, upper_bound=6),
        ObjectQueueAtOffsetAndIndexAtAMEM60(target_address=0x3A7FAC),
        ReturnSubroutine(),
    ],
)
