"""PhysicalAttack51 animation"""

from randomizer.scripts.animation.script_imports import *

script = AnimationScript(
    [
        RunSubroutine(["command_0x357b73"]),
        RunSubroutine(["command_0x352523"]),
        SetAMEM16BitToConst(0x60, 12),
        RunSubroutine(["command_0x35249d"]),
        RunSubroutine(["command_0x3577f2"]),
        RunSubroutine(["command_0x35240c"]),
        ReturnSubroutine(),
    ]
)
