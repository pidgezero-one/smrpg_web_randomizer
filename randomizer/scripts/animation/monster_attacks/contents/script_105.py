"""Jinxed animation"""

from randomizer.scripts.animation.script_imports import *

script = AnimationScript(
    [
        RunSubroutine(["command_0x35313b"]),
        PlaySound(sound=S0125_SPIKE_SHOT),
        SetAMEM16BitToConst(0x60, 22),
        RunSubroutine(["command_0x352475"]),
        ReturnSubroutine(),
    ]
)
