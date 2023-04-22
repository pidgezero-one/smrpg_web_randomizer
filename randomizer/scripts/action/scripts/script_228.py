"""A0228_ENDING_CUTSCENE_EFFECT"""

from randomizer.scripts.action.script_imports import *

script = ActionScript(
    [
        Db(bytearray(b" \x07")),
        EmbeddedAnimationRoutine(
            bytearray(b"&\x00\x00\x00\x00\x00<\x00\x1c\x00\x01\x00\x00\x80\xfe\x80")
        ),
        EmbeddedAnimationRoutine(
            bytearray(b"'\x00\x00\x00\x00\x00\xfc\x00\x15\x00\x01\x00\x00\x80\xfe\x80")
        ),
        Pause(150),
        SetVarToConst(PRIMARY_TEMP_700C, 65024),
        Db(bytearray(b"5\x00\x06")),
        Db(bytearray(b"5\x01\x06")),
        SetVarToConst(PRIMARY_TEMP_700C, 257),
        Db(bytearray(b"5\x00\x04")),
        Db(bytearray(b"5\x01\x04")),
        Db(bytearray(b"% \x00\x00\x00")),
        Pause(180),
        SetVarToConst(PRIMARY_TEMP_700C, 258),
        Db(bytearray(b"5\x00\x04")),
        Db(bytearray(b"5\x01\x04")),
        SetVarToConst(PRIMARY_TEMP_700C, 64768),
        Db(bytearray(b"5\x00\x06")),
        Db(bytearray(b"5\x01\x06")),
        Db(bytearray(b"%\x00\x00\x00\x00")),
        Pause(120),
        SetWalkingSpeed(FASTEST),
        ShiftZUpSteps(20),
        Return(),
    ]
)
