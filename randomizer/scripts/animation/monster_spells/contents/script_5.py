"""FlameStone animation"""

from randomizer.scripts.animation.script_imports import *

script = AnimationScript(
    [
        RunSubroutine(["command_0x3536f8"]),
        RunSubroutine(["command_0x35252b"]),
        PlaySound(sound=S0026_FLAME_WALL),
        SetAMEM16BitToConst(0x60, 3),
        RunSubroutine(["command_0x35247f"]),
        RunSubroutine(["command_0x3536ff"]),
        ReturnSubroutine(),
    ]
)
