# pylint: disable=C0301,C0103

"""referenced by monster_spells Flame"""

from randomizer.scripts.animation.script_imports import *

script = SubroutineOrBanklessScript(
    expected_size=8,
    script=[
        SetAMEMToRandom(amem=0x60, upper_bound=4),
        ObjectQueueAtOffsetAndIndexAtAMEM60(target_address=0x352C09),
        ReturnSubroutine(),
    ],
)
