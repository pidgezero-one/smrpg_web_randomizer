# pylint: disable=C0301,C0103

"""referenced by battle_events BE0053_DOMINO_TEAMS_UP_WITH_MAD_ADDER"""

from randomizer.scripts.animation.script_imports import *

script = SubroutineOrBanklessScript(
    expected_size=10,
    script=[
        ResetTargetMappingMemory(),
        SetAMEM40ToXYZCoords(
            origin=ABSOLUTE_POSITION,
            x=184,
            y=128,
            z=0,
            set_x=True,
            set_y=True,
            set_z=True),
        ReturnSubroutine(),
    ])
