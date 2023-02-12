# behaviour_34_0x350C9E

from randomizer.scripts.animation.script_imports import *

script = SubroutineOrBanklessScript(
    expected_size=62,
    script=[
        ResetTargetMappingMemory(),
        ResetObjectMappingMemory(),
        SetAMEM40ToXYZCoords(
            origin=CASTER_INITIAL_POSITION, x=-22, y=8, z=0, set_y=True, set_z=True
        ),
        MoveSpriteToCoords(shift_type=SHIFT_TYPE_0X00, speed=512, arch_height=0),
        PauseScriptUntil(condition=0x04),
        ResetObjectMappingMemory(),
        SpriteSequence(sequence=4),
        PauseScriptUntilSpriteSequenceDone(),
        ClearAMEM8Bit(0x60),
        SetOMEM60To072C(),
        DecAMEM16BitByConst(0x60, 64),
        ObjectQueueAtOffsetAndIndexAtAMEM60(target_address=0x351026),
        AttackTimerBegins(),
        Db(bytearray(b"<\x00\x08")),
        ResetTargetMappingMemory(),
        ResetObjectMappingMemory(),
        ResetSpriteSequence(),
        SetAMEM40ToXYZCoords(
            origin=CASTER_INITIAL_POSITION, x=0, y=0, z=0, set_y=True, set_z=True
        ),
        MoveSpriteToCoords(shift_type=SHIFT_TYPE_0X00, speed=512, arch_height=0),
        PauseScriptUntil(condition=0x04),
        Jmp(["command_0x350b06"]),
    ],
)
