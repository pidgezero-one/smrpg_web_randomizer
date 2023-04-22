"""PhysicalAttack46 animation"""

from randomizer.scripts.animation.script_imports import *

script = AnimationScript(
    [
        SetAMEM8BitTo7E1x(0x6F, 0x7EE00F),
        JmpIfAMEM8BitEqualsConst(0x6F, 1, ["command_0x351934"]),
        RunSubroutine(["command_0x357b73"]),
        RunSubroutine(["command_0x352523"], identifier="command_0x351934"),
        PlaySound(sound=S0097_PLASMA_TOSS),
        SetAMEM16BitToConst(0x60, 7),
        RunSubroutine(["command_0x352475"]),
        RunSubroutine(["command_0x3577f2"]),
        RunSubroutine(["command_0x352448"]),
        ReturnSubroutine(),
    ]
)
