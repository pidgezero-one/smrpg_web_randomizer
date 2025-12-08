# pylint: disable=C0301,C0103

"""referenced by monster_spells WaterBlast"""

from randomizer.scripts.animation.script_imports import *

script = SubroutineOrBanklessScript(
    expected_size=9,
    script=[
        SetAMEM32ToXYZCoords(
            origin=ABSOLUTE_POSITION,
            x=32,
            y=32,
            z=0,
            set_y=True,
            set_z=True,
            identifier="queuestart_0x352b20"),
        ReturnSubroutine(),
    ])
