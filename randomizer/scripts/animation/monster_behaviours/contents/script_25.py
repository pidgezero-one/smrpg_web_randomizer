"""behaviour_25_0x350ABD animation"""

from randomizer.scripts.animation.script_imports import *

script = SubroutineOrBanklessScript(
    expected_size=22,
    script=[
        SetOMEM60To072C(),
        JmpIfAMEM16BitEqualsConst(0x60, 0, ["command_0x353225"]),
        JmpIfAMEM16BitEqualsConst(0x60, 2, ["command_0x353453"]),
        JmpIfAMEM16BitEqualsConst(0x60, 3, ["command_0x3509e3"]),
        Jmp(["command_0x3509ae"]),
    ],
)
