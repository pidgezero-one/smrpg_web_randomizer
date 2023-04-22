# pylint: disable=C0301,C0103

"""referenced by monster_spells Blast, monster_attacks Poison"""

from randomizer.scripts.animation.script_imports import *

script = SubroutineOrBanklessScript(
    expected_size=9,
    script=[
        SetAMEM32ToXYZCoords(
            origin=CASTER_CURRENT_POSITION,
            x=-15,
            y=-271,
            z=0,
            set_x=True,
            set_y=True,
            set_z=True,
            identifier="queuestart_0x3525d5",
        ),
        ReturnSubroutine(),
    ],
)
