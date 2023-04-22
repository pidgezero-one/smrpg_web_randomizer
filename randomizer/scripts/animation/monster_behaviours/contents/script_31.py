"""behaviour_31_0x350BFD animation"""

from randomizer.scripts.animation.script_imports import *

script = SubroutineOrBanklessScript(
    expected_size=17,
    script=[
        ResetTargetMappingMemory(),
        ResetObjectMappingMemory(),
        SetOMEM60To072C(),
        ObjectQueueAtOffsetAndIndexAtAMEM60(
            target_address=0x351493, identifier="queuestart_0x350c00"
        ),
        Db(bytearray(b"R\x80\x00\x0e\x0c")),
        Db(bytearray(b"<\x00\x08")),
        Jmp(["command_0x350b06"]),
    ],
)
