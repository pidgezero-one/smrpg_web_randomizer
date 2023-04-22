"""A0446_SUMMON_EXTRA_SPARKLES"""

from randomizer.scripts.action.script_imports import *

script = ActionScript(
    [
        ObjectMemorySetBit(arg_1=0x3C, bits=[6]),
        ClearSolidityBits(
            cant_pass_walls=True,
            bit_4=True,
            cant_pass_npcs=True,
            cant_walk_through=True,
            bit_7=True,
        ),
        FloatingOff(),
        TransferToObjectXY(MARIO),
        JmpIfBitSet(EXP_STAR_BIT_5, ["ACTION_446_visibility_off_31"]),
        JmpIfBitSet(EXP_STAR_BIT_6, ["ACTION_446_visibility_off_31"]),
        JmpIfRandom1of2(["ACTION_446_shift_xy_pixels_9"]),
        ShiftXYPixels(x=252, y=4),
        Jmp(["ACTION_446_sequence_looping_on_10"]),
        ShiftXYPixels(x=4, y=252, identifier="ACTION_446_shift_xy_pixels_9"),
        SequenceLoopingOn(identifier="ACTION_446_sequence_looping_on_10"),
        SetSpriteSequence(index=0, is_sequence=True, looping=False),
        StartLoopNTimes(5),
        JmpIfBitSet(EXP_STAR_BIT_5, ["ACTION_446_visibility_off_31"]),
        JmpIfBitSet(EXP_STAR_BIT_6, ["ACTION_446_visibility_off_31"]),
        Pause(1),
        EndLoop(),
        JmpIfBitClear(TEMP_7076_0, ["ACTION_446_start_loop_n_times_19"]),
        CreatePacketAtObjectCoords(
            packet=P023_LOOPING_SINGLE_SPARKLE,
            target_npc=MARIO,
            destinations=["ACTION_446_start_loop_n_times_19"],
        ),
        StartLoopNTimes(5, identifier="ACTION_446_start_loop_n_times_19"),
        JmpIfBitSet(EXP_STAR_BIT_5, ["ACTION_446_visibility_off_31"]),
        JmpIfBitSet(EXP_STAR_BIT_6, ["ACTION_446_visibility_off_31"]),
        Pause(1),
        EndLoop(),
        JmpIfBitClear(TEMP_7076_0, ["ACTION_446_start_loop_n_times_26"]),
        CreatePacketAtObjectCoords(
            packet=P022_RECURSIVE_SPARKLES,
            target_npc=MARIO,
            destinations=["ACTION_446_start_loop_n_times_26"],
        ),
        StartLoopNTimes(11, identifier="ACTION_446_start_loop_n_times_26"),
        JmpIfBitSet(EXP_STAR_BIT_5, ["ACTION_446_visibility_off_31"]),
        JmpIfBitSet(EXP_STAR_BIT_6, ["ACTION_446_visibility_off_31"]),
        Pause(1),
        EndLoop(),
        VisibilityOff(identifier="ACTION_446_visibility_off_31"),
        Return(),
    ]
)
