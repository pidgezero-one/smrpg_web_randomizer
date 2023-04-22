"""A0120_EMBEDDED_ROUTINE"""

from randomizer.scripts.action.script_imports import *

script = ActionScript(
    [
        SequenceLoopingOn(),
        Db(bytearray(b" \x04")),
        EmbeddedAnimationRoutine(
            bytearray(b"(\x00\x00\x00\x00\x00\x00\x00\x04\x00\x01\x00\x00\x00\x04\x80")
        ),
        Pause(1, identifier="ACTION_120_pause_3"),
        Jmp(["ACTION_120_pause_3"]),
    ]
)
