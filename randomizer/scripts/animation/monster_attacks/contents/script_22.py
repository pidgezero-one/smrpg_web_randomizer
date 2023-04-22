"""PhysicalAttack28 animation"""

from randomizer.scripts.animation.script_imports import *

script = AnimationScript(
    [
        RunSubroutine(["command_0x357b73"]),
        RunSubroutine(["command_0x352523"]),
        PlaySound(sound=S0146_SLAP),
        SetAMEM16BitToConst(0x60, 2),
        RunSubroutine(["command_0x35247f"]),
        RunSubroutine(["command_0x3577f2"]),
        RunSubroutine(["command_0x3523c4"]),
        ReturnSubroutine(),
    ]
)
