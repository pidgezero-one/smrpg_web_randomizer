# pylint: disable=C0301,C0103

"""referenced by ally_spells Sleepy Time"""

from randomizer.scripts.animation.script_imports import *

script = SubroutineOrBanklessScript(
    expected_size=9,
    script=[
        SetAMEM16BitToConst(0x60, 0, identifier="queuestart_0x35a4de"),
        ObjectQueueAtOffsetAndIndex(index=24, target_address=0x35A0A5),
        ReturnSubroutine(),
    ],
)
