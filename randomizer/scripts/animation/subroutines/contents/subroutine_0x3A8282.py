# pylint: disable=C0301,C0103

"""referenced by battle_events BE0082_SMITHY_1ST_FORM_IS_BEATEN_GROUND_SHAKES_ETC"""

from randomizer.scripts.animation.script_imports import *

script = SubroutineOrBanklessScript(
    expected_size=30,
    script=[
        ResetTargetMappingMemory(),
        SetAMEM40ToXYZCoords(
            origin=ABSOLUTE_POSITION,
            x=120,
            y=120,
            z=0,
            set_x=True,
            set_y=True,
            set_z=True,
        ),
        ReturnSubroutine(),
        ResetTargetMappingMemory(),
        SetAMEM40ToXYZCoords(
            origin=ABSOLUTE_POSITION,
            x=136,
            y=128,
            z=0,
            set_x=True,
            set_y=True,
            set_z=True,
        ),
        ReturnSubroutine(),
        ResetTargetMappingMemory(),
        SetAMEM40ToXYZCoords(
            origin=ABSOLUTE_POSITION,
            x=152,
            y=136,
            z=0,
            set_x=True,
            set_y=True,
            set_z=True,
        ),
        ReturnSubroutine(),
    ],
)
