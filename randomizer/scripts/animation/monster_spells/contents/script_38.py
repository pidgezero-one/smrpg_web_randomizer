"""ArrowRain animation"""

from randomizer.scripts.animation.script_imports import *

script = AnimationScript(
    [
        RunSubroutine(["command_0x3536f8"]),
        RunSubroutine(["command_0x35252b"]),
        RunSubroutine(["command_0x3536eb"]),
        SetAMEM16BitToConst(0x60, 32),
        RunSubroutine(["command_0x352493"]),
        StopCurrentSoundEffect(),
        Db(bytearray(b"\x8c")),
        RunSubroutine(["command_0x3536ff"]),
        ReturnSubroutine(),
    ]
)
