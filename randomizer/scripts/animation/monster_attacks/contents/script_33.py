"""Endobubble animation"""

from randomizer.scripts.animation.script_imports import *

script = AnimationScript(
    [
        SetAMEM8BitTo7E1x(0x6F, 0x7EE00F),
        JmpIfAMEM8BitEqualsConst(0x6F, 1, ["command_0x351872"]),
        RunSubroutine(["command_0x357b73"]),
        RunSubroutine(["command_0x352523"], identifier="command_0x351872"),
        SetAMEM16BitToConst(0x60, 5),
        RunSubroutine(["command_0x352493"]),
        RunSubroutine(["command_0x3577f2"]),
        RunSubroutine(["command_0x352448"]),
        ReturnSubroutine(),
    ]
)
