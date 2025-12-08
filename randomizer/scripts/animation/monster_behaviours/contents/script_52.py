"""behaviour_52_0x350F6B animation"""

from randomizer.scripts.animation.script_imports import *

script = SubroutineOrBanklessScript(
    expected_size=15,
    script=[
        SetOMEM60To072C(),
        DecAMEM16BitByConst(0x60, 64),
        ObjectQueueAtOffsetAndIndexAtAMEM60(target_address=0x351026),
        AttackTimerBegins(),
        Db(bytearray(b"<\x00\x08")),
        Jmp(["command_0x350e93"]),
    ])
