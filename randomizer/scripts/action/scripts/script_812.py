"""A0812_NIMBUS_NPC_RANDOM_DIRECTIONS"""

from randomizer.scripts.action.script_imports import *

script = ActionScript(
    [
        SetPriority(3),
        SetSequenceSpeed(SLOW),
        SetWalkingSpeed(VERY_SLOW),
        Db(bytearray(b" \x04")),
        EmbeddedAnimationRoutine(
            bytearray(b"(\x00\x00\x00\x00\x00@\x00\x02\x00\x01\x00\x00\x00\x08\x80")
        ),
        SetVarToConst(PRIMARY_TEMP_700C, 2, identifier="ACTION_812_set_14"),
        ShiftZ20Steps(),
        TurnClockwise45DegreesNTimes(6),
        Pause(4),
        TurnClockwise45DegreesNTimes(6),
        Pause(4),
        TurnClockwise45DegreesNTimes(6),
        JmpIfRandom1of2(["ACTION_812_pause_23"]),
        Pause(30),
        Pause(10, identifier="ACTION_812_pause_23"),
        Jmp(["ACTION_812_set_14"]),
    ]
)
