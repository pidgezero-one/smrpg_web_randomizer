# pylint: disable=C0301,C0103

"""referenced by monster_spells Recover, monster_attacks ScrowFangs"""

from randomizer.scripts.animation.script_imports import *

script = SubroutineOrBanklessScript(
    expected_size=18,
    script=[
        SetAMEM60ToCurrentTarget(identifier="queuestart_0x352720"),
        SetAMEM32ToXYZCoords(
            origin=TARGET_CURRENT_POSITION,
            x=7,
            y=0,
            z=0,
            set_x=True,
            set_y=True,
            set_z=True,
        ),
        ReturnSubroutine(),
        SetAMEMToRandom(amem=0x60, upper_bound=79),
        ObjectQueueAtOffsetAndIndexAtAMEM60(target_address=0x352732),
        ReturnSubroutine(),
    ],
)
