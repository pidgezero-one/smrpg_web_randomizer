"""EerieJig animation"""

from randomizer.scripts.animation.script_imports import *

script = AnimationScript(
    [
        SetAMEM8BitTo7E1x(0x6F, 0x7EE00F),
        JmpIfAMEM8BitEqualsConst(0x6F, 1, ["command_0x351bca"]),
        RunSubroutine(["command_0x3577e2"]),
        RunSubroutine(["command_0x352523"]),
        Jmp(["command_0x351bcd"]),
        RunSubroutine(["command_0x35251b"], identifier="command_0x351bca"),
        PlaySound(sound=S0132_STINGER_POISON, identifier="command_0x351bcd"),
        SetAMEM8BitTo7E1x(0x6F, 0x7EE00F),
        JmpIfAMEM8BitEqualsConst(0x6F, 1, ["command_0x351bdc"]),
        RunSubroutine(["command_0x3577f2"]),
        RunSubroutine(["command_0x3523ee"], identifier="command_0x351bdc"),
        ReturnSubroutine(),
    ]
)
