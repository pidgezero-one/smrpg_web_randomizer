# pylint: disable=C0301,C0103

"""referenced by ally_spells Super Flame"""

from randomizer.scripts.animation.script_imports import *

script = SubroutineOrBanklessScript(
    expected_size=5,
    script=[
        PauseScriptUntil(
            condition=FRAMES_ELAPSED, frames=24, identifier="queuestart_0x358166"
        ),
        ReturnSubroutine(),
    ],
)
