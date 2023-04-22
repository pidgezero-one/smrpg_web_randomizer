"""Quicksilver animation"""

from randomizer.scripts.animation.script_imports import *

script = AnimationScript(
    [
        RunSubroutine(["command_0x357b73"]),
        RunSubroutine(["command_0x35313b"]),
        PlaySound(sound=S0125_SPIKE_SHOT),
        SetAMEM16BitToConst(0x60, 4),
        RunSubroutine(["command_0x352489"]),
        RunSubroutine(["command_0x3577f2"]),
        ReturnSubroutine(),
    ]
)
