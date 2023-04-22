"""behaviour_11_0x35086A animation"""

from randomizer.scripts.animation.script_imports import *

script = SubroutineOrBanklessScript(
    expected_size=46,
    script=[
        SetOMEM60To072C(),
        JmpIfAMEM16BitEqualsConst(0x60, 2, ["command_0x35345a"]),
        JmpIfAMEM16BitEqualsConst(0x60, 3, ["command_0x3505e8"]),
        JmpIfAMEM16BitEqualsConst(0x60, 4, ["command_0x35315a"]),
        JmpIfAMEM16BitEqualsConst(0x60, 5, ["command_0x353160"]),
        JmpIfAMEM16BitEqualsConst(0x60, 6, ["command_0x353166"]),
        JmpIfAMEM16BitEqualsConst(0x60, 7, ["command_0x35316c"]),
        JmpIfAMEM16BitEqualsConst(0x60, 8, ["command_0x353172"]),
        Jmp(["command_0x3505d5"]),
    ],
)
