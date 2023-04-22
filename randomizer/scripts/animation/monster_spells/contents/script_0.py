"""Drain animation"""

from randomizer.scripts.animation.script_imports import *

script = AnimationScript(
    [
        RunSubroutine(["command_0x35252b"]),
        PlaySound(sound=S0029_FIRE_SHOOT),
        SetAMEM16BitToConst(0x60, 3),
        RunSubroutine(["command_0x352475"]),
        ReturnSubroutine(),
    ]
)
