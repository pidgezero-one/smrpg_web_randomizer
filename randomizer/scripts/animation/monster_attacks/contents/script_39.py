"""PhysicalAttack47 animation"""

from randomizer.scripts.animation.script_imports import *

script = AnimationScript(
    [
        RunSubroutine(["command_0x357b73"]),
        RunSubroutine(["command_0x352523"]),
        PlaySound(sound=S0138_ENDOBUBBLE),
        SetAMEM16BitToConst(0x60, 7),
        RunSubroutine(["command_0x352489"]),
        RunSubroutine(["command_0x3577f2"]),
        RunSubroutine(["command_0x35242a"]),
        ReturnSubroutine(),
    ]
)
