"""Crystal animation"""

from randomizer.scripts.animation.script_imports import *

script = AnimationScript(
    [
        RunSubroutine(["command_0x3536f8"]),
        RunSubroutine(["command_0x35252b"]),
        SetAMEM16BitToConst(0x60, 9),
        RunSubroutine(["command_0x352475"]),
        RunSubroutine(["command_0x3536ff"]),
        ReturnSubroutine(),
    ]
)
