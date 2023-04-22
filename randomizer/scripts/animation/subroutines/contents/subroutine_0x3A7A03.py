# pylint: disable=C0301,C0103

"""referenced by battle_events BE0044_CZAR_DRAGON_DIES"""

from randomizer.scripts.animation.script_imports import *

script = SubroutineOrBanklessScript(
    expected_size=18,
    script=[
        SetAMEM60ToCurrentTarget(identifier="queuestart_0x3a7a03"),
        SetAMEM32ToXYZCoords(
            origin=CASTER_CURRENT_POSITION,
            x=7,
            y=0,
            z=0,
            set_x=True,
            set_y=True,
            set_z=True,
        ),
        ReturnSubroutine(),
        SetAMEMToRandom(amem=0x60, upper_bound=63),
        ObjectQueueAtOffsetAndIndexAtAMEM60(target_address=0x3A7A15),
        ReturnSubroutine(),
    ],
)
