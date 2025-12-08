"""ENT0012_WAIT_THEN_APPEAR animation"""

from randomizer.scripts.animation.script_imports import *

script = AnimationScript(
    [
        SetAMEM32ToXYZCoords(
            origin=CASTER_INITIAL_POSITION,
            x=0,
            y=-256,
            z=0,
            set_x=True,
            set_y=True,
            set_z=True),
        EnableSpritesOnSubscreen(),
        VisibilityOff(),
        SetAMEM32ToXYZCoords(
            origin=CASTER_INITIAL_POSITION,
            x=0,
            y=48,
            z=0,
            set_x=True,
            set_y=True,
            set_z=True),
        ResetTargetMappingMemory(),
        SetAMEM40ToXYZCoords(
            origin=CASTER_INITIAL_POSITION,
            x=0,
            y=0,
            z=0,
            set_x=True,
            set_y=True,
            set_z=True),
        MoveSpriteToCoords(shift_type=SHIFT_TYPE_SHIFT, speed=256, arch_height=0),
        Db(bytearray(b"\x84\x00\x08")),
        Db(bytearray(b"\x9e\x00\x00")),
        FadeInSprite(duration=4),
        VisibilityOn(),
        PauseScriptUntil(condition=FADE_4BPP_COMPLETE),
        PauseScriptUntil(condition=0x07),
        Db(bytearray(b"\x84\x80\x00")),
        Db(bytearray(b"\x9e\x00 ")),
        DisableSpritesOnSubscreen(),
        ResetObjectMappingMemory(),
        ReturnSubroutine(),
    ]
)
