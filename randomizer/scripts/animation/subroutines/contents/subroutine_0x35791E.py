# pylint: disable=C0301,C0103

"""referenced by monster_attacks PhysicalAttack8"""

from randomizer.scripts.animation.script_imports import *

script = SubroutineOrBanklessScript(
    expected_size=50,
    script=[
        ResetTargetMappingMemory(identifier="command_0x35791e"),
        SetAMEM60ToCurrentTarget(),
        Db(bytearray(b"DH")),
        MoveSpriteToCoords(shift_type=SHIFT_TYPE_TRANSFER, speed=1024, arch_height=128),
        PauseScriptUntil(condition=SPRITE_SHIFT_COMPLETE),
        ResetObjectMappingMemory(),
        ResetTargetMappingMemory(),
        SetAMEM60ToCurrentTarget(),
        Db(bytearray(b"D`")),
        MoveSpriteToCoords(shift_type=SHIFT_TYPE_TRANSFER, speed=512, arch_height=256),
        SpriteSequence(sequence=0, mirror=True),
        PauseScriptUntil(condition=FRAMES_ELAPSED, frames=4),
        SpriteSequence(sequence=1, mirror=True),
        PauseScriptUntil(condition=FRAMES_ELAPSED, frames=3),
        SpriteSequence(sequence=1),
        PauseScriptUntil(condition=FRAMES_ELAPSED, frames=2),
        SpriteSequence(sequence=0),
        PauseScriptUntil(condition=FRAMES_ELAPSED, frames=1),
        ReturnSubroutine(),
    ])
