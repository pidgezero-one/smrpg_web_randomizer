"""A0467_BANDITS_WAY_5_TROOPA_CHASE"""

from randomizer.scripts.action.script_imports import *

script = ActionScript(
    [
        Db(bytearray(b" \x04")),
        EmbeddedAnimationRoutine(
            bytearray(b"(\x00\x00\x00\x00\x00\x00\x00\x08\x00\x01\x00\x00\x00\x08\x80")
        ),
        FaceMario(),
        TurnClockwise45DegreesNTimes(4),
        WalkFDirectionSteps(10),
        BPL262728(),
        VisibilityOff(),
        Return(),
    ]
)
