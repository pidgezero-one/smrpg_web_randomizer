"""A0312_SHIP_TROOPA_PUZZLE_CANNONBALL"""

from randomizer.scripts.action.script_imports import *

script = ActionScript(
    [
        SetSpriteSequence(index=2, is_sequence=True, looping=False),
        IncPaletteRowBy(3),
        SetPriority(3),
        Pause(1, identifier="ACTION_312_pause_3"),
        JmpIfObjectWithinRange(
            comparing_npc=NPC_0,
            usually=48,
            tiles=0,
            destinations=["ACTION_312_set_700C_to_object_coord_6"]),
        Jmp(["ACTION_312_pause_3"]),
        Set700CToObjectCoord(
            target_npc=NPC_0,
            coord=COORD_F,
            pixel=True,
            identifier="ACTION_312_set_700C_to_object_coord_6"),
        JmpIfVarEqualsConst(
            TEMP_70AE, 1, ["ACTION_312_jmp_if_700C_not_equals_short_11"]
        ),
        JmpIfVarEqualsConst(
            TEMP_70AE, 2, ["ACTION_312_jmp_if_700C_not_equals_short_20"]
        ),
        JmpIfVarEqualsConst(
            TEMP_70AE, 3, ["ACTION_312_jmp_if_700C_not_equals_short_35"]
        ),
        JmpIfVarEqualsConst(
            TEMP_70AE, 4, ["ACTION_312_jmp_if_700C_not_equals_short_49"]
        ),
        JmpIfVarNotEqualsConst(
            PRIMARY_TEMP_700C,
            1,
            ["ACTION_312_pause_3"],
            identifier="ACTION_312_jmp_if_700C_not_equals_short_11"),
        FixedFCoordOn(),
        FloatingOn(),
        Walk1StepSoutheast(),
        JumpToHeight(height=0, silent=True),
        Pause(10),
        FloatingOff(),
        SetBit(TEMP_7043_0),
        Return(),
        JmpIfVarNotEqualsConst(
            PRIMARY_TEMP_700C,
            7,
            ["ACTION_312_pause_3"],
            identifier="ACTION_312_jmp_if_700C_not_equals_short_20"),
        FixedFCoordOn(),
        FloatingOn(),
        Walk1StepNortheast(),
        ObjectMemoryModifyBits(arg_1=0x09, set_bits=[5], clear_bits=[4, 6]),
        ClearSolidityBits(bit_4=True, cant_walk_through=True),
        JumpToHeight(height=0, silent=True),
        Pause(8),
        SetBit(TEMP_7044_7),
        Pause(1, identifier="ACTION_312_pause_29"),
        JmpIfObjectInAir(DUMMY_0X07, ["ACTION_312_pause_29"]),
        WalkNortheastSteps(2),
        VisibilityOff(),
        ObjectMemorySetBit(arg_1=0x30, bits=[4]),
        Return(),
        JmpIfVarNotEqualsConst(
            PRIMARY_TEMP_700C,
            3,
            ["ACTION_312_pause_3"],
            identifier="ACTION_312_jmp_if_700C_not_equals_short_35"),
        FixedFCoordOn(),
        FloatingOn(),
        Walk1StepSouthwest(),
        ClearSolidityBits(bit_4=True, cant_walk_through=True),
        JumpToHeight(height=0, silent=True),
        Pause(8),
        SetBit(TEMP_7044_7),
        Pause(1, identifier="ACTION_312_pause_43"),
        JmpIfObjectInAir(DUMMY_0X07, ["ACTION_312_pause_43"]),
        WalkSouthwestSteps(3),
        VisibilityOff(),
        ObjectMemorySetBit(arg_1=0x30, bits=[4]),
        Return(),
        JmpIfVarNotEqualsConst(
            PRIMARY_TEMP_700C,
            5,
            ["ACTION_312_pause_3"],
            identifier="ACTION_312_jmp_if_700C_not_equals_short_49"),
        FixedFCoordOn(),
        FloatingOn(),
        Walk1StepNorthwest(),
        ObjectMemoryModifyBits(arg_1=0x09, set_bits=[5], clear_bits=[4, 6]),
        ClearSolidityBits(bit_4=True, cant_walk_through=True),
        JumpToHeight(height=0, silent=True),
        Pause(8),
        SetBit(TEMP_7044_7),
        Pause(1, identifier="ACTION_312_pause_58"),
        JmpIfObjectInAir(DUMMY_0X07, ["ACTION_312_pause_58"]),
        WalkNorthwestSteps(2),
        VisibilityOff(),
        ObjectMemorySetBit(arg_1=0x30, bits=[4]),
        Return(),
    ]
)
