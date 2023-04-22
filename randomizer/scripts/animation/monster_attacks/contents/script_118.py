"""(unknown)"""

from randomizer.scripts.animation.script_imports import *

script = AnimationScript(
    [
        PlaySound(sound=S0012_BOMB_EXPLOSION),
        VisibilityOff(),
        SetAMEM16BitToConst(0x60, 11),
        RunSubroutine(["command_0x352475"]),
        SetAMEM8BitTo7E1x(0x6F, 0x7EE00F),
        JmpIfAMEM8BitEqualsConst(0x6F, 1, ["command_0x352041"]),
        RunSubroutine(["command_0x3523c4"]),
        ReturnSubroutine(identifier="command_0x352041"),
    ]
)
