"""Sledge animation"""

from randomizer.scripts.animation.script_imports import *

script = AnimationScript(
    [
        RunSubroutine(["command_0x35252b"]),
        RunSubroutine(["command_0x3536eb"]),
        RunSubroutine(["command_0x3536eb"]),
        PlaySound(sound=S0000_SILENCE),
        SetAMEM16BitToConst(0x60, 32),
        RunSubroutine(["command_0x352475"]),
        Db(bytearray(b"\x8c")),
        ReturnSubroutine(),
    ]
)
