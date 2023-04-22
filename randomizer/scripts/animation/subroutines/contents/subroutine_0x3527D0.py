# pylint: disable=C0301,C0103

"""referenced by monster_attacks ScrowFangs"""

from randomizer.scripts.animation.script_imports import *

script = SubroutineOrBanklessScript(
    expected_size=10,
    script=[
        ResetTargetMappingMemory(identifier="queuestart_0x3527d0"),
        SetAMEM40ToXYZCoords(
            origin=ABSOLUTE_POSITION, x=8, y=160, z=0, set_y=True, set_z=True
        ),
        ReturnSubroutine(),
    ],
)
