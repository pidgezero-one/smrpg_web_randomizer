# pylint: disable=C0301,C0103

"""referenced by ally_spells Psych Bomb"""

from randomizer.scripts.animation.script_imports import *

script = SubroutineOrBanklessScript(
    expected_size=9,
    script=[
        SetAMEM32ToXYZCoords(
            origin=ABSOLUTE_POSITION,
            x=184,
            y=116,
            z=0,
            set_x=True,
            set_y=True,
            set_z=True,
            identifier="queuestart_0x35ac50",
        ),
        ReturnSubroutine(),
    ],
)
