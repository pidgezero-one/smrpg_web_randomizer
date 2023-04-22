"""IceRock animation"""

from randomizer.scripts.animation.script_imports import *

script = AnimationScript(
    [
        RunSubroutine(["command_0x3536f8"]),
        RunSubroutine(["command_0x35252b"]),
        PlaySound(sound=S0198_ICE_ROCK),
        SetAMEM16BitToConst(0x60, 9),
        RunSubroutine(["command_0x352489"]),
        RunSubroutine(["command_0x3536ff"]),
        ReturnSubroutine(),
    ]
)
