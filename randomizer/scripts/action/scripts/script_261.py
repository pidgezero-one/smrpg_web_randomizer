"""A0261_NIMBUS_FINAL_HALLWAY_BOSS"""

from randomizer.scripts.action.script_imports import *

script = ActionScript(
    [
        Db(bytearray(b"\xfd\xf2")),
        FaceNortheast(),
        SetWalkingSpeed(VERY_SLOW),
        Walk1StepNortheast(),
        SetWalkingSpeed(SLOW),
        SetSequenceSpeed(FAST),
        WalkNortheastSteps(6),
        SetBit(TEMP_7043_0),
        Pause(20),
        Walk1StepNortheast(),
        VisibilityOff(),
        Return(),
    ]
)
