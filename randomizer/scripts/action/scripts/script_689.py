"""A0689_BEAN_VALLEY_BOSS_PRIZE_DRIFTS_DOWN"""

from randomizer.scripts.action.script_imports import *

script = ActionScript(
    [
        Pause(64),
        ClearSolidityBits(cant_walk_through=True),
        SetVRAMPriority(MARIO_OVERLAPS_ON_ALL_SIDES),
        WalkNorthwestPixels(5),
        SetSpriteSequence(index=1, is_sequence=True, looping=True, mirror_sprite=True),
        VisibilityOn(),
        Db(bytearray(b" \x07")),
        EmbeddedAnimationRoutine(
            bytearray(b"&\x00\x00\x00\x00\x00 \xf0\x03\x00\x01\x00\x00\x00\x04\x80")
        ),
        EmbeddedAnimationRoutine(
            bytearray(b"'\x00\x00\x00\x00\x00 \xf0\x03\x00\x01\x00\x00\x00\x04\x80")
        ),
        EmbeddedAnimationRoutine(
            bytearray(b"(\x00\x00\x00\x00\x00 \xf0\x03\x00\x01\x00\x00\x00\x08\x80")
        ),
        ShiftZDownSteps(10),
        SetSolidityBits(cant_walk_through=True),
        Return(),
    ]
)
