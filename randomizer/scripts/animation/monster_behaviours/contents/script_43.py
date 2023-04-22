"""behaviour_43_0x350E38 animation"""

from randomizer.scripts.animation.script_imports import *

script = SubroutineOrBanklessScript(
    expected_size=18,
    script=[
        ClearAMEM8Bit(0x60),
        SetOMEM60To072C(),
        DecAMEM16BitByConst(0x60, 64),
        ObjectQueueAtOffsetAndIndexAtAMEM60(target_address=0x351026),
        AttackTimerBegins(),
        Db(bytearray(b"<\x00\x08")),
        ResetSpriteSequence(),
        Jmp(["command_0x350d31"]),
    ],
)
