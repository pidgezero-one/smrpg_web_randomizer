"""behaviour_22_0x350A3E animation"""

from randomizer.scripts.animation.script_imports import *

script = SubroutineOrBanklessScript(
    expected_size=17,
    script=[
        ResetTargetMappingMemory(),
        ResetObjectMappingMemory(),
        SetOMEM60To072C(),
        ObjectQueueAtOffsetAndIndexAtAMEM60(target_address=0x351493),
        Db(bytearray(b"R\x80\x00O\n")),
        Db(bytearray(b"<\x00\x08")),
        Jmp(["command_0x3509ae"]),
    ])
