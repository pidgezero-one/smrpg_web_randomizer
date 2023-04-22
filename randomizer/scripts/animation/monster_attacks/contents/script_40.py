"""ViroPlasm animation"""

from randomizer.scripts.animation.script_imports import *

script = AnimationScript(
    [
        RunSubroutine(["command_0x357b73"]),
        RunSubroutine(["command_0x353148"]),
        PlaySound(sound=S0097_PLASMA_TOSS),
        SetAMEM16BitToConst(0x60, 19),
        RunSubroutine(["command_0x352475"]),
        RunSubroutine(["command_0x3577f2"]),
        RunSubroutine(["command_0x3523c4"]),
        ReturnSubroutine(),
    ]
)
