"""StaticE animation"""

from randomizer.scripts.animation.script_imports import *

script = AnimationScript(
    [
        RunSubroutine(["command_0x3536f8"]),
        RunSubroutine(["command_0x35252b"]),
        RunSubroutine(["command_0x3536eb"]),
        PlaySound(sound=S0102_STATIC_E),
        SetAMEM16BitToConst(0x60, 17),
        RunSubroutine(["command_0x35247f"]),
        Db(bytearray(b"\x8c")),
        RunSubroutine(["command_0x3536ff"]),
        ReturnSubroutine(),
    ]
)
