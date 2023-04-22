"""(unknown)"""

from randomizer.scripts.animation.script_imports import *

script = AnimationScript(
    [
        PlaySound(sound=S0169_TELEPORT_ATTACK),
        RunSubroutine(["command_0x3577e2"]),
        RunSubroutine(["command_0x35251b"]),
        PlaySound(sound=S0110_HUGE_EXPLOSION),
        RunSubroutine(["command_0x35358a"]),
        RunSubroutine(["command_0x3577f2"]),
        ReturnSubroutine(),
    ]
)
