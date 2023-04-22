"""behaviour_12_0x3508A4 animation"""

from randomizer.scripts.animation.script_imports import *

script = SubroutineOrBanklessScript(
    expected_size=22,
    script=[
        Db(bytearray(b"X")),
        Db(bytearray(b"Y")),
        JmpIfTargetDisabled(["command_0x350916"]),
        VisibilityOn(),
        SetAMEM8BitTo7E5x(0x60, 0x7E002E),
        ClearAMEM8Bit(0x61),
        ObjectQueueAtOffsetAndIndexAtAMEM60(target_address=0x352128),
        Db(bytearray(b"\x16")),
        Db(bytearray(b"\x15"), identifier="command_0x3508b5"),
        Pause1Frame(),
        Jmp(["command_0x3508b5"]),
    ],
)
