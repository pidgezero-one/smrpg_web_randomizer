"""A0321_BELLHOP_FACE_PLAYER"""

from randomizer.scripts.action.script_imports import *

script = ActionScript(
    [
        SetSequenceSpeed(SLOW),
        FaceMario(identifier="ACTION_321_face_mario_1"),
        Pause(1),
        Jmp(["ACTION_321_face_mario_1"]),
    ]
)
