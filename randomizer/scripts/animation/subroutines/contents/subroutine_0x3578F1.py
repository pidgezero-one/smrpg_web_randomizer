# referenced by monster_attacks PhysicalAttack81, monster_attacks Magnum, monster_attacks 120, monster_attacks PhysicalAttack7, monster_attacks Psyche

from randomizer.scripts.animation.script_imports import *

script = SubroutineOrBanklessScript(
    expected_size=44,
    script=[
        ResetTargetMappingMemory(identifier="command_0x3578f1"),
        SetAMEM60ToCurrentTarget(),
        Db(bytearray(b"D`")),
        MoveSpriteToCoords(shift_type=SHIFT_TYPE_0X00, speed=1536, arch_height=0),
        SetAMEM16BitToConst(0x60, 10),
        ObjectQueueAtOffsetAndIndex(index=0, target_address=0x355F1D),
        PauseScriptUntil(condition=FRAMES_ELAPSED, frames=4),
        VisibilityOff(),
        PauseScriptUntil(condition=FRAMES_ELAPSED, frames=8),
        ObjectQueueAtOffsetAndIndex(index=0, target_address=0x355F1D),
        VisibilityOn(),
        PauseScriptUntil(condition=FRAMES_ELAPSED, frames=4),
        PauseScriptUntil(condition=SPRITE_SHIFT_COMPLETE),
        ResetObjectMappingMemory(),
        ReturnSubroutine(),
    ],
)
