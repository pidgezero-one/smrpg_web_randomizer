# pylint: disable=C0301,C0103

"""referenced by monster_attacks Poison"""

from randomizer.scripts.animation.script_imports import *

script = SubroutineOrBanklessScript(
    expected_size=8,
    script=[
        SetAMEMToRandom(amem=0x60, upper_bound=6),
        ObjectQueueAtOffsetAndIndexAtAMEM60(target_address=0x352DC8),
        ReturnSubroutine(),
    ])
