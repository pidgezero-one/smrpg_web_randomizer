# pylint: disable=C0301,C0103

"""referenced by battle_events BE0022_YARIDOVICH_MIRAGE_ATTACK"""

from randomizer.scripts.animation.script_imports import *

script = SubroutineOrBanklessScript(
    expected_size=10,
    script=[
        ResetTargetMappingMemory(),
        SetAMEM40ToXYZCoords(
            origin=ABSOLUTE_POSITION,
            x=152,
            y=104,
            z=0,
            set_x=True,
            set_y=True,
            set_z=True,
        ),
        ReturnSubroutine(),
    ],
)
