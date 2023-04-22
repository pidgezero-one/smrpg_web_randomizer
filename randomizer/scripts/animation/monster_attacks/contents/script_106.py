"""TripleKick animation"""

from randomizer.scripts.animation.script_imports import *

script = AnimationScript(
    [
        RunSubroutine(["command_0x35251b"]),
        PlaySound(sound=S0125_SPIKE_SHOT),
        SetAMEM16BitToConst(0x60, 22),
        RunSubroutine(["command_0x35247f"]),
        RunSubroutine(["command_0x352439"]),
        ReturnSubroutine(),
    ]
)
