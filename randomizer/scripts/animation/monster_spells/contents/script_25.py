"""Solidify animation"""

from randomizer.scripts.animation.script_imports import *

script = AnimationScript(
    [
        RunSubroutine(["command_0x3536f8"]),
        RunSubroutine(["command_0x35252b"]),
        RunSubroutine(["command_0x3536eb"]),
        PlaySound(sound=S0174_SOLIDIFY),
        ClearAMEM8Bit(0x6F),
        SetAMEM16BitToConst(0x60, 26),
        ObjectQueueAtOffsetAndIndex(index=2, target_address=0x353706),
        ObjectQueueAtOffsetAndIndex(index=0, target_address=0x353706),
        PauseScriptUntilAMEMBitsSet(0x6F, [0]),
        Db(bytearray(b"\x8c")),
        RunSubroutine(["command_0x3536ff"]),
        ReturnSubroutine(),
    ]
)
