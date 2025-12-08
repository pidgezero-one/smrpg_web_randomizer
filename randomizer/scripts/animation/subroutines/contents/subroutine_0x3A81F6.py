# pylint: disable=C0301,C0103

"""referenced by battle_events BE0059_BELOME_CONFRONTS_A_CHARACTER_YOU_ALL_LOOK_DELICIOUS, battle_events BE0002_BELOME_SWALLOWS_MALLOW"""

from randomizer.scripts.animation.script_imports import *

script = SubroutineOrBanklessScript(
    expected_size=40,
    script=[
        ResetTargetMappingMemory(),
        SetAMEM40ToXYZCoords(
            origin=ABSOLUTE_POSITION,
            x=120,
            y=152,
            z=0,
            set_x=True,
            set_y=True,
            set_z=True),
        ReturnSubroutine(),
        ResetTargetMappingMemory(),
        SetAMEM40ToXYZCoords(
            origin=ABSOLUTE_POSITION,
            x=136,
            y=160,
            z=0,
            set_x=True,
            set_y=True,
            set_z=True),
        ReturnSubroutine(),
        ResetTargetMappingMemory(),
        SetAMEM40ToXYZCoords(
            origin=ABSOLUTE_POSITION,
            x=152,
            y=168,
            z=0,
            set_x=True,
            set_y=True,
            set_z=True),
        ReturnSubroutine(),
        ResetTargetMappingMemory(),
        SetAMEM40ToXYZCoords(
            origin=ABSOLUTE_POSITION,
            x=168,
            y=176,
            z=0,
            set_x=True,
            set_y=True,
            set_z=True),
        ReturnSubroutine(),
    ])
