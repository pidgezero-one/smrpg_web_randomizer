# pylint: disable=C0301,C0103

"""referenced by monster_attacks Vigorup"""

from randomizer.scripts.animation.script_imports import *

script = SubroutineOrBanklessScript(
    expected_size=8,
    script=[
        SetAMEMToRandom(amem=0x60, upper_bound=8),
        ObjectQueueAtOffsetAndIndexAtAMEM60(target_address=0x352E67),
        ReturnSubroutine(),
    ],
)
