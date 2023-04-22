"""A0497_MUSHROOM_DERBY_UNKNOWN"""

from randomizer.scripts.action.script_imports import *

script = ActionScript(
    [
        ClearSolidityBits(
            bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True
        ),
        FloatingOn(),
        CopyVarToVar(from_var=ROSE_WAY_703E, to_var=PRIMARY_TEMP_700C),
        FaceEast7C(),
        SequencePlaybackOn(),
        ResetProperties(),
        ShadowOn(),
        SetWalkingSpeed(NORMAL),
        JumpToHeight(108),
        WalkFDirectionPixels(12),
        SetSolidityBits(
            bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True
        ),
        WalkFDirectionPixels(12),
        Pause(1, identifier="ACTION_497_pause_12"),
        JmpIfMarioInAir(["ACTION_497_pause_12"]),
        ClearBit(TEMP_7044_4),
        FixedFCoordOff(),
        Return(),
    ]
)
