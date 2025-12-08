# pylint: disable=C0301,C0103

"""referenced by battle_events BE0044_CZAR_DRAGON_DIES"""

from randomizer.scripts.animation.script_imports import *

script = SubroutineOrBanklessScript(
    expected_size=9,
    script=[
        SetAMEM32ToXYZCoords(
            origin=CASTER_CURRENT_POSITION,
            x=23,
            y=-96,
            z=0,
            set_y=True,
            set_z=True,
            identifier="queuestart_0x3a7a93"),
        ReturnSubroutine(),
    ])
