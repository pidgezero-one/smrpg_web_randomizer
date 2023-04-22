"""A0363_SKY_BRIDGE_HIT_BY_BULLET_BILL"""

from randomizer.scripts.action.script_imports import *

script = ActionScript(
    [
        ClearSolidityBits(bit_7=True),
        SetWalkingSpeed(FAST),
        WalkSoutheastPixels(2, identifier="ACTION_363_shift_southeast_pixels_2"),
        JmpIfMarioInAir(["ACTION_363_clear_bit_5"]),
        Jmp(["ACTION_363_shift_southeast_pixels_2"]),
        ClearBit(TEMP_7044_7, identifier="ACTION_363_clear_bit_5"),
        ResetProperties(),
        FaceNorthwest(),
        SetAllSpeeds(NORMAL),
        ShiftZDownPixels(1),
        SetSolidityBits(bit_7=True),
        Return(),
    ]
)
