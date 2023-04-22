# pylint: disable=C0301,C0103

"""referenced by behaviour_33_0x350C5B, behaviour_34_0x350C9E, behaviour_51_0x350F56, behaviour_24_0x350A9C, behaviour_8_0x3507A2, behaviour_41_0x350DAF, behaviour_16_0x350928, behaviour_32_0x350C14, behaviour_52_0x350F6B, behaviour_23_0x350A55, behaviour_9_0x3507E9, weapons PunchGlove, behaviour_42_0x350DED, behaviour_43_0x350E38"""

from randomizer.scripts.animation.script_imports import *

script = SubroutineOrBanklessScript(
    expected_size=15,
    script=[
        PlaySound(sound=S0080_WALLOP_1, identifier="queuestart_0x35f128"),
        PauseScriptUntil(condition=FRAMES_ELAPSED, frames=10),
        PlaySound(sound=S0081_WALLOP_2),
        PauseScriptUntil(condition=FRAMES_ELAPSED, frames=10),
        PlaySound(sound=S0082_WALLOP_3),
        ReturnObjectQueue(),
    ],
)
