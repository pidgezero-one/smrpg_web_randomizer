"""ENT0002_LONG_JUMP animation"""

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
            x=0,
            y=0,
            z=0,
            set_x=True,
            set_y=True,
            set_z=True,
        ),
        MoveSpriteToCoords(shift_type=SHIFT_TYPE_TRANSFER, speed=1024, arch_height=96),
        ResetTargetMappingMemory(),
        Db(bytearray(b"\x12\x81")),
        SetAMEM40ToXYZCoords(
            origin=CASTER_INITIAL_POSITION,
            x=0,
            y=0,
            z=0,
            set_x=True,
            set_y=True,
            set_z=True,
        ),
        PauseScriptUntil(condition=0x01),
        ResetObjectMappingMemory(),
        ReturnSubroutine(),
    ]
)
