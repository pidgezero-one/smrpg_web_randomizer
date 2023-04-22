# pylint: disable=C0301,C0103

"""referenced by weapons SlapGlove, weapons Armor, weapons SuperSlap"""

from randomizer.scripts.animation.script_imports import *

script = SubroutineOrBanklessScript(
    expected_size=40,
    script=[
        PauseScriptUntil(
            condition=FRAMES_ELAPSED, frames=16, identifier="queuestart_0x35f369"
        ),
        PlaySound(sound=S0160_SLAP),
        PauseScriptUntil(condition=FRAMES_ELAPSED, frames=9),
        PlaySound(sound=S0160_SLAP),
        ReturnObjectQueue(),
        PauseScriptUntil(
            condition=FRAMES_ELAPSED, frames=18, identifier="queuestart_0x35f376"
        ),
        PlaySound(sound=S0171_SLAP_POWERFUL),
        ReturnObjectQueue(),
        PauseScriptUntil(
            condition=FRAMES_ELAPSED, frames=16, identifier="queuestart_0x35f37d"
        ),
        PlaySound(sound=S0171_SLAP_POWERFUL),
        PauseScriptUntil(condition=FRAMES_ELAPSED, frames=9),
        PlaySound(sound=S0171_SLAP_POWERFUL),
        ReturnObjectQueue(),
        PauseScriptUntil(
            condition=FRAMES_ELAPSED, frames=24, identifier="queuestart_0x35f38a"
        ),
        PlaySound(sound=S0084_WALLOP_4),
        ReturnObjectQueue(),
    ],
)
