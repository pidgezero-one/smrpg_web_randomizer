# ENT0007_SPREAD_OUT_FROM_BACK

from randomizer.scripts.animation.script_imports import *

script = AnimationScript(
    [
        SetAMEM32ToXYZCoords(
            origin=ABSOLUTE_POSITION,
            x=196,
            y=104,
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
        ClearAMEM8Bit(0x61),
        SetAMEM8BitTo7E1x(0x60, 0x7EE00D),
        JmpIfAMEM8BitEqualsConst(0x60, 1, ["command_0x352274"]),
        Set7E5xToAMEM8Bit(0x7E0064, 0x61),
        ReturnSubroutine(),
        SetAMEM8BitToConst(0x61, 1, identifier="command_0x352274"),
        Set7E5xToAMEM8Bit(0x7E0064, 0x61),
        ReturnSubroutine(),
    ]
)
