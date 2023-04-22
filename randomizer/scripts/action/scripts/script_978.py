"""A0978_RANDOMLY_FACE_SOUTHWEST"""

from randomizer.scripts.action.script_imports import *

script = ActionScript(
    [
        FaceSouthwest7D(identifier="ACTION_978_face_southwest_7D_0"),
        Pause(30),
        JmpIfRandom1of2(["ACTION_978_face_southwest_7D_0"]),
        Pause(30),
        Jmp(["ACTION_978_face_southwest_7D_0"]),
    ]
)
