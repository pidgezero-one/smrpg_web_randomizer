"""Boulder animation"""

from randomizer.scripts.animation.script_imports import *

script = AnimationScript(
    [
        RunSubroutine(["command_0x3536f8"]),
        RunSubroutine(["command_0x35252b"]),
        RunSubroutine(["command_0x3536eb"]),
        PlaySound(sound=S0096_RUMBLE_MULTI),
        SetAMEM16BitToConst(0x60, 18),
        RunSubroutine(["command_0x35247f"]),
        StopCurrentSoundEffect(),
        Db(bytearray(b"\x8c")),
        RunSubroutine(["command_0x3536ff"]),
        ReturnSubroutine(),
    ]
)
