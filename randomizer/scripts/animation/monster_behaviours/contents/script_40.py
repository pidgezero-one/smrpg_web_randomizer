"""behaviour_40_0x350DA3 animation"""

from randomizer.scripts.animation.script_imports import *

script = SubroutineOrBanklessScript(
    expected_size=12,
    script=[
        ResetTargetMappingMemory(),
        ResetObjectMappingMemory(),
        SetOMEM60To072C(),
        ObjectQueueAtOffsetAndIndexAtAMEM60(target_address=0x351493),
        Db(bytearray(b"<\x00\x08")),
        Jmp(["command_0x350d31"]),
    ],
)
