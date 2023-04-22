"""behaviour_44_0x350E4A animation"""

from randomizer.scripts.animation.script_imports import *

script = SubroutineOrBanklessScript(
    expected_size=22,
    script=[
        SetOMEM60To072C(),
        JmpIfAMEM16BitEqualsConst(0x60, 0, ["command_0x3531f8"]),
        JmpIfAMEM16BitEqualsConst(0x60, 3, ["command_0x350d44"]),
        JmpIfAMEM16BitEqualsConst(0x60, 4, ["command_0x353577"]),
        Jmp(["command_0x350d31"]),
    ],
)
