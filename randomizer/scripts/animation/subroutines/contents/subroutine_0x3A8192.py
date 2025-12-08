# pylint: disable=C0301,C0103

"""referenced by """

from randomizer.scripts.animation.script_imports import *

script = SubroutineOrBanklessScript(
    expected_size=40,
    script=[
        ResetTargetMappingMemory(),
        SetAMEM40ToXYZCoords(
            origin=ABSOLUTE_POSITION,
            x=72,
            y=144,
            z=0,
            set_x=True,
            set_y=True,
            set_z=True),
        ReturnSubroutine(),
        ResetTargetMappingMemory(),
        SetAMEM40ToXYZCoords(
            origin=ABSOLUTE_POSITION,
            x=88,
            y=152,
            z=0,
            set_x=True,
            set_y=True,
            set_z=True),
        ReturnSubroutine(),
        ResetTargetMappingMemory(),
        SetAMEM40ToXYZCoords(
            origin=ABSOLUTE_POSITION,
            x=104,
            y=160,
            z=0,
            set_x=True,
            set_y=True,
            set_z=True),
        ReturnSubroutine(),
        ResetTargetMappingMemory(),
        SetAMEM40ToXYZCoords(
            origin=ABSOLUTE_POSITION,
            x=120,
            y=168,
            z=0,
            set_x=True,
            set_y=True,
            set_z=True),
        ReturnSubroutine(),
    ])
