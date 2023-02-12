# ENT0003_HOP_3_TIMES

from randomizer.scripts.animation.script_imports import *

script = AnimationScript(
    [
        SetAMEM32ToXYZCoords(
            origin=CASTER_INITIAL_POSITION,
            x=100,
            y=-50,
            z=0,
            set_x=True,
            set_y=True,
            set_z=True,
        ),
        Db(bytearray(b"\x18\x00\x80")),
        ResetSpriteSequence(),
        SetAMEM40ToXYZCoords(
            origin=CASTER_INITIAL_POSITION,
            x=72,
            y=-36,
            z=0,
            set_x=True,
            set_y=True,
            set_z=True,
        ),
        MoveSpriteToCoords(shift_type=SHIFT_TYPE_TRANSFER, speed=1024, arch_height=96),
        PauseScriptUntil(condition=SPRITE_SHIFT_COMPLETE),
        ResetTargetMappingMemory(),
        SetAMEM40ToXYZCoords(
            origin=CASTER_INITIAL_POSITION,
            x=50,
            y=-22,
            z=0,
            set_x=True,
            set_y=True,
            set_z=True,
        ),
        MoveSpriteToCoords(shift_type=SHIFT_TYPE_TRANSFER, speed=1024, arch_height=128),
        PauseScriptUntil(condition=0x01),
        ResetTargetMappingMemory(),
        SetAMEM40ToXYZCoords(
            origin=CASTER_INITIAL_POSITION,
            x=0,
            y=0,
            z=0,
            set_x=True,
            set_y=True,
            set_z=True,
        ),
        MoveSpriteToCoords(shift_type=SHIFT_TYPE_TRANSFER, speed=1024, arch_height=352),
        PauseScriptUntil(condition=0x01),
        ResetObjectMappingMemory(),
        ReturnSubroutine(),
    ]
)
