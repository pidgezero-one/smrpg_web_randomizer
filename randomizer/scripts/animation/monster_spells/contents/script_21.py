"""DrainBeam animation"""

from randomizer.scripts.animation.script_imports import *

script = AnimationScript(
    [
        RunSubroutine(["command_0x3536f8"]),
        RunSubroutine(["command_0x3536eb"]),
        RunSubroutine(["command_0x35252b"]),
        PlaySound(sound=S0019_DRAIN_BEAM),
        SetAMEM16BitToConst(0x60, 27),
        RunSubroutine(["command_0x352489"]),
        RunSubroutine(["command_0x3536ff"]),
        Db(bytearray(b"\x8c")),
        ReturnSubroutine(),
    ]
)
