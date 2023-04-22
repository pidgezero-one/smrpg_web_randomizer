"""behaviour_5_0x350737 animation"""

from randomizer.scripts.animation.script_imports import *

script = SubroutineOrBanklessScript(
    expected_size=34,
    script=[
        ResetTargetMappingMemory(),
        ResetObjectMappingMemory(),
        Db(bytearray(b"T")),
        Db(bytearray(b">")),
        Db(bytearray(b"W")),
        Db(bytearray(b";")),
        Db(bytearray(b"U")),
        Db(bytearray(b";")),
        Db(bytearray(b"V")),
        JmpIfTargetEnabled(["command_0x350755"]),
        PlaySound(sound=S0089_COMMON_MONSTER_EXPLOSION),
        Db(bytearray(b"\xa4")),
        SetAMEM8BitTo7E5x(0x60, 0x7E002C),
        ClearAMEM8Bit(0x61),
        ObjectQueueAtOffsetAndIndexAtAMEM60(target_address=0x350759),
        RemoveObject(),
        SetAMEMToAMEM16Bit(dest_amem=0x6E, amem=0x62),
        Db(bytearray(b"\x98")),
        Db(bytearray(b"F"), identifier="command_0x350755"),
        Jmp(["command_0x3505d5"]),
    ],
)
