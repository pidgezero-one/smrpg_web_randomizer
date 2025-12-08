# pylint: disable=C0301,C0103

"""referenced by monster_attacks Poison"""

from randomizer.scripts.animation.script_imports import *

script = SubroutineOrBanklessScript(
    expected_size=9,
    script=[
        MoveObject(
            speed=17,
            start_position=-1153,
            end_position=-129,
            apply_to_x=True,
            should_set_start_position=True,
            should_set_end_position=True,
            should_set_speed=True,
            identifier="queuestart_0x352e01"),
        ReturnSubroutine(),
    ])
