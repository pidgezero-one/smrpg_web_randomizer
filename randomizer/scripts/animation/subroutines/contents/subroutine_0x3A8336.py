# pylint: disable=C0301,C0103

"""referenced by """

from randomizer.scripts.animation.script_imports import *

script = SubroutineOrBanklessScript(
    expected_size=20,
    script=[
        ResetTargetMappingMemory(),
        SetAMEM40ToXYZCoords(
            origin=ABSOLUTE_POSITION,
            x=184,
            y=120,
            z=0,
            set_x=True,
            set_y=True,
            set_z=True),
        ReturnSubroutine(),
        ResetTargetMappingMemory(),
        SetAMEM40ToXYZCoords(
            origin=ABSOLUTE_POSITION,
            x=200,
            y=128,
            z=0,
            set_x=True,
            set_y=True,
            set_z=True),
        ReturnSubroutine(),
    ])
