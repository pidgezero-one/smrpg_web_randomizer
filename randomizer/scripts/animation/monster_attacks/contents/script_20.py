"""SpritzBomb animation"""

from randomizer.scripts.animation.script_imports import *

script = AnimationScript(
    [
        SetAMEM8BitTo7E1x(0x6F, 0x7EE00F),
        JmpIfAMEM8BitEqualsConst(0x6F, 1, ["command_0x351733"]),
        RunSubroutine(["command_0x357b73"]),
        RunSubroutine(["command_0x353148"], identifier="command_0x351733"),
        PlaySound(sound=S0125_SPIKE_SHOT),
        SetAMEM16BitToConst(0x60, 2),
        RunSubroutine(["command_0x352475"]),
        SetAMEM8BitTo7E1x(0x6F, 0x7EE00F),
        JmpIfAMEM8BitEqualsConst(0x6F, 1, ["command_0x35174c"]),
        RunSubroutine(["command_0x3577f2"]),
        RunSubroutine(["command_0x3523c4"], identifier="command_0x35174c"),
        ReturnSubroutine(),
    ]
)
