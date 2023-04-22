# pylint: disable=C0301,C0103

"""referenced by battle_events BE0082_SMITHY_1ST_FORM_IS_BEATEN_GROUND_SHAKES_ETC"""

from randomizer.scripts.animation.script_imports import *

script = SubroutineOrBanklessScript(
    expected_size=20,
    script=[
        ResetTargetMappingMemory(),
        SetAMEM40ToXYZCoords(
            origin=ABSOLUTE_POSITION,
            x=152,
            y=144,
            z=0,
            set_x=True,
            set_y=True,
            set_z=True,
        ),
        ReturnSubroutine(),
        ResetTargetMappingMemory(),
        SetAMEM40ToXYZCoords(
            origin=ABSOLUTE_POSITION,
            x=168,
            y=152,
            z=0,
            set_x=True,
            set_y=True,
            set_z=True,
        ),
        ReturnSubroutine(),
    ],
)
