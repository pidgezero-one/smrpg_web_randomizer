# ENT0011_SLOW_DROP_FROM_ABOVE

from randomizer.scripts.animation.script_imports import *

script = AnimationScript(
    [
        SetAMEM32ToXYZCoords(
            origin=CASTER_INITIAL_POSITION,
            x=0,
            y=-114,
            z=0,
            set_x=True,
            set_y=True,
            set_z=True,
        ),
        Db(bytearray(b"\x18\x00\x80")),
        SetAMEM40ToXYZCoords(
            origin=CASTER_INITIAL_POSITION,
            x=0,
            y=0,
            z=0,
            set_x=True,
            set_y=True,
            set_z=True,
        ),
        MoveSpriteToCoords(shift_type=SHIFT_TYPE_0X00, speed=256, arch_height=0),
        PauseScriptUntil(condition=0x02),
        ResetObjectMappingMemory(),
        ReturnSubroutine(),
    ]
)
