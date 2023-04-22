"""KnockOut animation"""

from randomizer.scripts.animation.script_imports import *

script = AnimationScript(
    [
        RunSubroutine(["command_0x35252b"]),
        RunSubroutine(["command_0x3536eb"]),
        PlaySound(sound=S0000_SILENCE),
        SetAMEM16BitToConst(0x60, 3),
        RunSubroutine(["command_0x352475"]),
        Db(bytearray(b"\x8c")),
        ReturnSubroutine(),
    ]
)
