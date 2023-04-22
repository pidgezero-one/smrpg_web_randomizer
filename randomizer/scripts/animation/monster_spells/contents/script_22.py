"""MeteorBlast animation"""

from randomizer.scripts.animation.script_imports import *

script = AnimationScript(
    [
        RunSubroutine(["command_0x3536f8"]),
        RunSubroutine(["command_0x35252b"]),
        RunSubroutine(["command_0x3536eb"]),
        PlaySound(sound=S0105_ROCK_CANDY),
        SetAMEM16BitToConst(0x60, 24),
        RunSubroutine(["command_0x352475"]),
        Db(bytearray(b"\x8c")),
        RunSubroutine(["command_0x3536ff"]),
        ReturnSubroutine(),
    ]
)
