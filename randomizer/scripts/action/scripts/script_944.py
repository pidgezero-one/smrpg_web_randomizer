"""A0944_CRANE_FOR_FINAL_FACTORY_BOSS"""

from randomizer.scripts.action.script_imports import *

script = ActionScript(
    [
        SetWalkingSpeed(NORMAL),
        SetSpriteSequence(index=1, is_mold=True, is_sequence=True, looping=True),
        Db(bytearray(b"\xc8\x87")),
        SetVarToConst(Z_COORD_2, 13),
        WalkTo70167018701A(),
        WalkToXYCoords(x=3, y=82),
        SetBit(TEMP_7044_3),
        WalkToXYCoords(x=6, y=81),
        SetBit(TEMP_7044_4),
        WalkToXYCoords(x=7, y=82),
        Return(),
    ]
)
