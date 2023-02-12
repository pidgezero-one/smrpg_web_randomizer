# ENT0014_SPREAD_FROM_MIDDLE

from randomizer.scripts.animation.script_imports import *

script = AnimationScript(
    [
        SetAMEM32ToXYZCoords(
            origin=ABSOLUTE_POSITION,
            x=183,
            y=127,
            z=0,
            set_x=True,
            set_y=True,
            set_z=True,
        ),
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
        MoveSpriteToCoords(shift_type=SHIFT_TYPE_TRANSFER, speed=1024, arch_height=144),
        PauseScriptUntil(condition=SPRITE_SHIFT_COMPLETE),
        ResetObjectMappingMemory(),
        ReturnSubroutine(),
    ]
)
