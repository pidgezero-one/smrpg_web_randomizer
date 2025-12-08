# pylint: disable=C0301,C0103

"""referenced by battle_events BE0044_CZAR_DRAGON_DIES"""

from randomizer.scripts.animation.script_imports import *

script = SubroutineOrBanklessScript(
    expected_size=18,
    script=[
        ResetObjectMappingMemory(identifier="queuestart_0x3a7e13"),
        MoveObject(
            speed=1,
            start_position=-513,
            end_position=0,
            apply_to_y=True,
            should_set_speed=True),
        ReturnSubroutine(),
        SetAMEMToRandom(amem=0x60, upper_bound=4),
        ObjectQueueAtOffsetAndIndexAtAMEM60(target_address=0x3A7E25),
        ReturnSubroutine(),
    ])
