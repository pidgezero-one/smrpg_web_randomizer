"""A0815_NIMBUS_NPC_RANDOM_DIRECTIONS"""

from randomizer.scripts.action.script_imports import *

script = ActionScript(
    [
        SetSequenceSpeed(SLOW),
        SetWalkingSpeed(VERY_SLOW),
        Db(bytearray(b" \x04")),
        EmbeddedAnimationRoutine(
            bytearray(b"(\x00\x00\x00\x00\x00@\x00\x02\x00\x01\x00\x00\x00\x08\x80")
        ),
        SetVarToConst(PRIMARY_TEMP_700C, 6, identifier="ACTION_815_set_10"),
        ShiftZ20Steps(),
        TurnClockwise45DegreesNTimes(6),
        Pause(4),
        TurnClockwise45DegreesNTimes(6),
        Pause(4),
        JmpIfRandom1of2(["ACTION_815_jmp_18"]),
        Pause(30),
        Jmp(["ACTION_815_set_10"], identifier="ACTION_815_jmp_18"),
    ]
)
