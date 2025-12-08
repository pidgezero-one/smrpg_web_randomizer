"""(unknown)"""

from randomizer.scripts.animation.script_imports import *

script = AnimationScript(
    [
        SetAMEM60ToCurrentTarget(identifier="command_0x358251"),
        SetAMEM32ToXYZCoords(
            origin=TARGET_CURRENT_POSITION,
            x=4,
            y=-10,
            z=0,
            set_x=True,
            set_y=True,
            set_z=True),
        ClearAMEM8Bit(0x6F),
        Db(bytearray(b"?\x80\x15\x00\x00\x84")),
        PauseScriptUntilAMEMBitsSet(0x6F, [0, 1, 2, 3, 4, 5, 6, 7]),
        ResetObjectMappingMemory(),
        SetAMEM8BitToConst(0x6F, 1),
        SetOMEMMainToAMEM8Bit(omem=0x6F, amem=0x6F),
        ReturnObjectQueue(),
    ]
)
