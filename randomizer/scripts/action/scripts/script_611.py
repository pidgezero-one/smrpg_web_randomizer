"""A0611_ROSE_WAY_LAKITU_SHY_GUY"""

from randomizer.scripts.action.script_imports import *

script = ActionScript(
    [
        VisibilityOff(identifier="ACTION_611_visibility_off_0"),
        ObjectMemorySetBit(arg_1=0x0D, bits=[6]),
        SetPriority(3),
        SetVarToConst(TEMP_70AE, 21),
        SetObjectMemoryBits(arg_1=0x0E, bits=[0]),
        Pause(1),
        JmpIfVarNotEqualsConst(TEMP_70AE, 21, ["ACTION_611_visibility_off_0"]),
        VisibilityOn(),
        SetSequenceSpeed(VERY_FAST),
        SequenceLoopingOn(),
        WalkSoutheastPixels(18),
        ShiftZDownSteps(3),
        FaceMario(identifier="ACTION_611_face_mario_12"),
        Pause(1),
        Jmp(["ACTION_611_face_mario_12"]),
    ]
)
