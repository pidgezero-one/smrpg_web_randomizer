"""ENT0005_ZOOM_IN_FROM_RIGHT animation"""

from randomizer.scripts.animation.script_imports import *

script = AnimationScript(
    [
        SetAMEM32ToXYZCoords(
            origin=CASTER_INITIAL_POSITION,
            x=100,
            y=-100,
            z=0,
            set_x=True,
            set_y=True,
            set_z=True),
        Db(bytearray(b"\x18\x00\x80")),
        ResetSpriteSequence(),
        SetAMEM40ToXYZCoords(
            origin=CASTER_INITIAL_POSITION,
            x=0,
            y=0,
            z=0,
            set_x=True,
            set_y=True,
            set_z=True),
        MoveSpriteToCoords(shift_type=SHIFT_TYPE_0X00, speed=1280, arch_height=0),
        PauseScriptUntil(condition=SPRITE_SHIFT_COMPLETE),
        ResetObjectMappingMemory(),
        ReturnSubroutine(),
    ]
)
