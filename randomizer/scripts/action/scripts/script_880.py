"""A0880_CROWD_AROUND_NIMBUS_BOSS"""

from randomizer.scripts.action.script_imports import *

script = ActionScript(
    [
        Db(bytearray(b" \x04")),
        EmbeddedAnimationRoutine(
            bytearray(b"(\x00\x00\x00\x00\x00@\x00\x03\x00\x01\x00\x00\x00\x08\x80")
        ),
        Pause(1, identifier="ACTION_880_pause_2"),
        Jmp(["ACTION_880_pause_2"]),
    ]
)
