"""A0378_MARRYMORE_LIBERATED_EXTERIOR_PHOTO_MOM"""

from randomizer.scripts.action.script_imports import *

script = ActionScript(
    [
        SequenceLoopingOn(identifier="ACTION_378_sequence_looping_on_0"),
        SetSequenceSpeed(SLOW),
        Pause(120),
        FaceSouthwest(),
        SetBit(TEMP_7043_1),
        Pause(120),
        ClearBit(TEMP_7043_1),
        FaceSoutheast(),
        JmpIfRandom1of2(["ACTION_378_sequence_looping_on_0"]),
        Pause(60),
        Jmp(["ACTION_378_sequence_looping_on_0"]),
    ]
)
