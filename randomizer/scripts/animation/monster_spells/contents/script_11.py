"""Storm animation"""

from randomizer.scripts.animation.script_imports import *

script = AnimationScript(
    [
        RunSubroutine(["command_0x35252b"]),
        RunSubroutine(["command_0x3536f8"]),
        PlaySound(sound=S0019_DRAIN_BEAM),
        SetAMEM16BitToConst(0x60, 10),
        RunSubroutine(["command_0x352475"]),
        StopCurrentSoundEffect(),
        RunSubroutine(["command_0x3536ff"]),
        ReturnSubroutine(),
    ]
)
