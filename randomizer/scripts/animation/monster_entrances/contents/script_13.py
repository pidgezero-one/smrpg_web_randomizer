"""ENT0013_SPREAD_FROM_FRONT animation"""

from randomizer.scripts.animation.script_imports import *

script = AnimationScript(
    [
        SetAMEM32ToXYZCoords(
            origin=ABSOLUTE_POSITION,
            x=148,
            y=157,
            z=0,
            set_x=True,
            set_y=True,
            set_z=True),
        SetAMEM40ToXYZCoords(
            origin=CASTER_INITIAL_POSITION,
            x=0,
            y=0,
            z=0,
            set_x=True,
            set_y=True,
            set_z=True),
        MoveSpriteToCoords(shift_type=SHIFT_TYPE_TRANSFER, speed=768, arch_height=256),
        PauseScriptUntil(condition=SPRITE_SHIFT_COMPLETE),
        ResetObjectMappingMemory(),
        ReturnSubroutine(),
    ]
)
