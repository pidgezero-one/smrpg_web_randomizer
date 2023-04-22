"""A0288_MARIO_DISMOUNT_YOSHI"""

from randomizer.scripts.action.script_imports import *

script = ActionScript(
    [
        CopyVarToVar(from_var=ROSE_WAY_703E, to_var=PRIMARY_TEMP_700C),
        FaceEast7C(),
        ClearSolidityBits(
            bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True
        ),
        FloatingOn(),
        SequencePlaybackOn(),
        ResetProperties(),
        ShadowOn(),
        SetWalkingSpeed(SLOW),
        JumpToHeight(108),
        WalkFDirectionPixels(8),
        SetWalkingSpeed(NORMAL),
        WalkFDirectionPixels(4),
        SetSolidityBits(
            bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True
        ),
        WalkFDirectionPixels(4),
        Pause(1, identifier="ACTION_288_pause_14"),
        JmpIfMarioInAir(["ACTION_288_pause_14"]),
        ClearBit(TEMP_7044_4),
        Return(),
    ]
)
