"""A0248_ENDING_CUTSCENE_EFFECT"""

from randomizer.scripts.action.script_imports import *

script = ActionScript(
    [
        Db(bytearray(b" \x03")),
        EmbeddedAnimationRoutine(
            bytearray(b"&\x00\x00\x00\x00\x00\x18\x00\x7f\xff\x00\xee\xff\x80\xfe\x80")
        ),
        EmbeddedAnimationRoutine(
            bytearray(b"'\x00\x00\x00\x00\x00\xe4\x00\\\xff\x00\xee\xff\x80\xfe\x80")
        ),
        SetWalkingSpeed(VERY_SLOW),
        AddZCoord1Step(),
        Pause(392),
        BPL262728(),
        Return(),
    ]
)
