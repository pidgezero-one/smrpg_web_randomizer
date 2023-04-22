"""behaviour_20_0x3509D5 animation"""

from randomizer.scripts.animation.script_imports import *

script = SubroutineOrBanklessScript(
    expected_size=44,
    script=[
        ResetTargetMappingMemory(),
        ResetObjectMappingMemory(),
        Db(bytearray(b"T")),
        Db(bytearray(b"n")),
        Db(bytearray(b">")),
        ResetSpriteSequence(),
        Db(bytearray(b"W")),
        Db(bytearray(b";")),
        Db(bytearray(b"U")),
        Db(bytearray(b";")),
        Db(bytearray(b"V")),
        JmpIfTargetEnabled(["command_0x3509f6"]),
        PlaySound(sound=S0089_COMMON_MONSTER_EXPLOSION),
        Db(bytearray(b"Z")),
        Db(bytearray(b"\xa4")),
        SetAMEM8BitTo7E5x(0x60, 0x7E002C),
        ClearAMEM8Bit(0x61),
        ObjectQueueAtOffsetAndIndexAtAMEM60(target_address=0x350A01),
        RemoveObject(),
        SetAMEMToAMEM16Bit(dest_amem=0x6E, amem=0x62),
        Db(bytearray(b"\x98")),
        Db(bytearray(b"F"), identifier="command_0x3509f6"),
        Db(bytearray(b"\x15")),
        Pause1Frame(),
        Db(bytearray(b"R\x80\x08\xf7\t")),
        Jmp(["command_0x3509ae"]),
    ],
)
