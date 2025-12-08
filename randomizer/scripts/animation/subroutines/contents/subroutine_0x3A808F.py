# pylint: disable=C0301,C0103

"""referenced by battle_events BE0044_CZAR_DRAGON_DIES"""

from randomizer.scripts.animation.script_imports import *

script = SubroutineOrBanklessScript(
    expected_size=9,
    script=[
        MoveObject(
            speed=17,
            start_position=640,
            end_position=2048,
            apply_to_y=True,
            should_set_start_position=True,
            should_set_end_position=True,
            should_set_speed=True,
            identifier="queuestart_0x3a808f"),
        ReturnSubroutine(),
    ])
