"""ENT0010_FADE_IN animation"""

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
        Db(bytearray(b"\x18\x00\x80")),
        EnableSpritesOnSubscreen(),
        VisibilityOff(),
        SetAMEM32ToXYZCoords(
            origin=CASTER_INITIAL_POSITION,
            x=0,
            y=0,
            z=0,
            set_x=True,
            set_y=True,
            set_z=True),
        Db(bytearray(b"\x84\x00\x08")),
        Db(bytearray(b"\x9e\x00\x00")),
        FadeInSprite(duration=2),
        VisibilityOn(),
        PauseScriptUntil(condition=FADE_4BPP_COMPLETE),
        Db(bytearray(b"\x84\x80\x00")),
        Db(bytearray(b"\x9e\x00 ")),
        DisableSpritesOnSubscreen(),
        ReturnSubroutine(),
    ]
)
