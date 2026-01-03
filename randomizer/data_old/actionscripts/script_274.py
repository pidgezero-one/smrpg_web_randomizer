
from randomizer.helpers.objectsequencetables import (
    SequenceSpeeds,
    VramPriority,
    _0x08Flags,
    _0x0AFlags,
    _0x10Flags)
from randomizer.helpers.eventtables import (
    RadialDirections,
    AreaObjects,
    NPCPackets,
    Sounds,
    Coords,
    CoordUnits,
    Rooms)

script = [
    {
        "identifier": "ACTION_274_set_animation_speed_0",
        "command": "set_animation_speed",
        "args": [SequenceSpeeds.SLOW, [_0x10Flags.SEQUENCE]],
    },
    {
        "identifier": "ACTION_274_sequence_looping_on_1",
        "command": "sequence_looping_on",
    },
    {
        "identifier": "ACTION_274_jmp_if_bit_set_2",
        "command": "jmp_if_bit_set",
        "args": [0x7076, 0, "ACTION_274_sequence_looping_off_63"],
    },
    {
        "identifier": "ACTION_274_set_700C_to_object_coord_3",
        "command": "set_700C_to_object_coord",
        "args": [AreaObjects.MARIO, Coords.X, [], CoordUnits.PIXEL],
    },
    {
        "identifier": "ACTION_274_copy_var_to_var_4",
        "command": "copy_var_to_var",
        "args": [0x700C, 0x7028],
    },
    {
        "identifier": "ACTION_274_set_700C_to_object_coord_5",
        "command": "set_700C_to_object_coord",
        "args": [AreaObjects.DUMMY_0X07, Coords.X, [], CoordUnits.PIXEL],
    },
    {
        "identifier": "ACTION_274_dec_short_mem_6",
        "command": "dec_short_mem_from_700C",
        "args": [0x7028],
    },
    {
        "identifier": "ACTION_274_add_7",
        "command": "add_const_to_var",
        "args": [0x700C, 256],
    },
    {
        "identifier": "ACTION_274_mem_compare_val_8",
        "command": "compare_var_to_const",
        "args": [0x700C, 128],
    },
    {
        "identifier": "ACTION_274_jmp_if_comparison_result_is_lesser_9",
        "command": "jmp_if_comparison_result_is_lesser",
        "args": ["ACTION_274_set_700C_to_object_coord_13"],
    },
    {
        "identifier": "ACTION_274_mem_compare_val_10",
        "command": "compare_var_to_const",
        "args": [0x700C, 384],
    },
    {
        "identifier": "ACTION_274_jmp_if_comparison_result_is_greater_or_equal_11",
        "command": "jmp_if_comparison_result_is_greater_or_equal",
        "args": ["ACTION_274_set_700C_to_object_coord_13"],
    },
    {
        "identifier": "ACTION_274_jmp_12",
        "command": "jmp",
        "args": ["ACTION_274_shift_f_direction_pixels_24"],
    },
    {
        "identifier": "ACTION_274_set_700C_to_object_coord_13",
        "command": "set_700C_to_object_coord",
        "args": [AreaObjects.MARIO, Coords.Y, [], CoordUnits.PIXEL],
    },
    {
        "identifier": "ACTION_274_copy_var_to_var_14",
        "command": "copy_var_to_var",
        "args": [0x700C, 0x7028],
    },
    {
        "identifier": "ACTION_274_set_700C_to_object_coord_15",
        "command": "set_700C_to_object_coord",
        "args": [AreaObjects.DUMMY_0X07, Coords.Y, [], CoordUnits.PIXEL],
    },
    {
        "identifier": "ACTION_274_dec_short_mem_16",
        "command": "dec_short_mem_from_700C",
        "args": [0x7028],
    },
    {
        "identifier": "ACTION_274_add_17",
        "command": "add_const_to_var",
        "args": [0x700C, 256],
    },
    {
        "identifier": "ACTION_274_mem_compare_val_18",
        "command": "compare_var_to_const",
        "args": [0x700C, 64],
    },
    {
        "identifier": "ACTION_274_jmp_if_comparison_result_is_lesser_19",
        "command": "jmp_if_comparison_result_is_lesser",
        "args": ["ACTION_274_face_mario_23"],
    },
    {
        "identifier": "ACTION_274_mem_compare_val_20",
        "command": "compare_var_to_const",
        "args": [0x700C, 320],
    },
    {
        "identifier": "ACTION_274_jmp_if_comparison_result_is_greater_or_equal_21",
        "command": "jmp_if_comparison_result_is_greater_or_equal",
        "args": ["ACTION_274_face_mario_23"],
    },
    {
        "identifier": "ACTION_274_jmp_22",
        "command": "jmp",
        "args": ["ACTION_274_shift_f_direction_pixels_24"],
    },
    {"identifier": "ACTION_274_face_mario_23", "command": "face_mario"},
    {
        "identifier": "ACTION_274_shift_f_direction_pixels_24",
        "command": "shift_f_direction_pixels",
        "args": [1],
    },
    {
        "identifier": "ACTION_274_set_700C_to_object_coord_25",
        "command": "set_700C_to_object_coord",
        "args": [AreaObjects.MARIO, Coords.Z, [], CoordUnits.PIXEL],
    },
    {
        "identifier": "ACTION_274_add_26",
        "command": "add_const_to_var",
        "args": [0x700C, 192],
    },
    {
        "identifier": "ACTION_274_set_7000_short_mem_to_700C_27",
        "command": "copy_var_to_var",
        "args": [0x700C, 0x7028],
    },
    {
        "identifier": "ACTION_274_set_700C_to_object_coord_28",
        "command": "set_700C_to_object_coord",
        "args": [AreaObjects.DUMMY_0X07, Coords.Z, [], CoordUnits.PIXEL],
    },
    {
        "identifier": "ACTION_274_compare_700C_to_var_29",
        "command": "compare_700C_to_var",
        "args": [0x7028],
    },
    {
        "identifier": "ACTION_274_jmp_if_loaded_memory_is_0_30",
        "command": "jmp_if_loaded_memory_is_0",
        "args": ["ACTION_274_pause_33"],
    },
    {
        "identifier": "ACTION_274_jmp_if_loaded_memory_is_below_0_31",
        "command": "jmp_if_loaded_memory_is_below_0",
        "args": ["ACTION_274_shift_z_down_pixels_35"],
    },
    {
        "identifier": "ACTION_274_jmp_if_loaded_memory_is_above_or_equal_0_32",
        "command": "jmp_if_loaded_memory_is_above_or_equal_0",
        "args": ["ACTION_274_shift_z_up_pixels_37"],
    },
    {"identifier": "ACTION_274_pause_33", "command": "pause", "args": [1]},
    {
        "identifier": "ACTION_274_jmp_34",
        "command": "jmp",
        "args": ["ACTION_274_pause_38"],
    },
    {
        "identifier": "ACTION_274_shift_z_down_pixels_35",
        "command": "shift_z_down_pixels",
        "args": [1],
    },
    {
        "identifier": "ACTION_274_jmp_36",
        "command": "jmp",
        "args": ["ACTION_274_pause_38"],
    },
    {
        "identifier": "ACTION_274_shift_z_up_pixels_37",
        "command": "shift_z_up_pixels",
        "args": [1],
    },
    {"identifier": "ACTION_274_pause_38", "command": "pause", "args": [2]},
    {
        "identifier": "ACTION_274_jmp_if_bit_set_39",
        "command": "jmp_if_bit_set",
        "args": [0x7076, 0, "ACTION_274_sequence_looping_off_63"],
    },
    {
        "identifier": "ACTION_274_set_700C_to_object_coord_40",
        "command": "set_700C_to_object_coord",
        "args": [AreaObjects.DUMMY_0X07, Coords.F, []],
    },
    {
        "identifier": "ACTION_274_set_7000_short_mem_to_700C_41",
        "command": "copy_var_to_var",
        "args": [0x700C, 0x702A],
    },
    {"identifier": "ACTION_274_face_mario_42", "command": "face_mario"},
    {
        "identifier": "ACTION_274_set_700C_to_object_coord_43",
        "command": "set_700C_to_object_coord",
        "args": [AreaObjects.DUMMY_0X07, Coords.F, []],
    },
    {
        "identifier": "ACTION_274_set_7000_short_mem_to_700C_44",
        "command": "copy_var_to_var",
        "args": [0x700C, 0x7028],
    },
    {
        "identifier": "ACTION_274_set_700C_to_7000_short_mem_45",
        "command": "copy_var_to_var",
        "args": [0x702A, 0x700C],
    },
    {"identifier": "ACTION_274_face_east_7C_46", "command": "face_east_7C"},
    {
        "identifier": "ACTION_274_dec_short_mem_47",
        "command": "dec_short_mem_from_700C",
        "args": [0x7028],
    },
    {
        "identifier": "ACTION_274_mem_700C_and_const_48",
        "command": "mem_700C_and_const",
        "args": [0x0007],
    },
    {
        "identifier": "ACTION_274_jmp_if_700C_equals_short_49",
        "command": "jmp_if_var_equals_const",
        "args": [0x700C, 0, "ACTION_274_set_700C_to_object_coord_53"],
    },
    {
        "identifier": "ACTION_274_jmp_if_700C_equals_short_50",
        "command": "jmp_if_var_equals_const",
        "args": [0x700C, 1, "ACTION_274_set_700C_to_object_coord_53"],
    },
    {
        "identifier": "ACTION_274_jmp_if_700C_equals_short_51",
        "command": "jmp_if_var_equals_const",
        "args": [0x700C, 7, "ACTION_274_set_700C_to_object_coord_53"],
    },
    {
        "identifier": "ACTION_274_jmp_52",
        "command": "jmp",
        "args": ["ACTION_274_set_animation_speed_0"],
    },
    {
        "identifier": "ACTION_274_set_700C_to_object_coord_53",
        "command": "set_700C_to_object_coord",
        "args": [AreaObjects.MARIO, Coords.F, []],
    },
    {
        "identifier": "ACTION_274_set_7000_short_mem_to_700C_54",
        "command": "copy_var_to_var",
        "args": [0x700C, 0x7028],
    },
    {
        "identifier": "ACTION_274_set_700C_to_object_coord_55",
        "command": "set_700C_to_object_coord",
        "args": [AreaObjects.DUMMY_0X07, Coords.F, []],
    },
    {
        "identifier": "ACTION_274_dec_short_mem_56",
        "command": "dec_short_mem_from_700C",
        "args": [0x7028],
    },
    {
        "identifier": "ACTION_274_mem_700C_and_const_57",
        "command": "mem_700C_and_const",
        "args": [0x0007],
    },
    {
        "identifier": "ACTION_274_jmp_if_700C_equals_short_58",
        "command": "jmp_if_var_equals_const",
        "args": [0x700C, 3, "ACTION_274_sequence_looping_off_63"],
    },
    {
        "identifier": "ACTION_274_jmp_if_700C_equals_short_59",
        "command": "jmp_if_var_equals_const",
        "args": [0x700C, 4, "ACTION_274_sequence_looping_off_63"],
    },
    {
        "identifier": "ACTION_274_jmp_if_700C_equals_short_60",
        "command": "jmp_if_var_equals_const",
        "args": [0x700C, 5, "ACTION_274_sequence_looping_off_63"],
    },
    {
        "identifier": "ACTION_274_db_61",
        "command": "jmp_if_object_within_range_same_z",
        "args": [AreaObjects.MARIO, 80, 0, "ACTION_274_set_700C_to_object_coord_25"],
    },
    {
        "identifier": "ACTION_274_jmp_62",
        "command": "jmp",
        "args": ["ACTION_274_set_animation_speed_0"],
    },
    {
        "identifier": "ACTION_274_sequence_looping_off_63",
        "command": "sequence_looping_off",
    },
    {
        "identifier": "ACTION_274_set_700C_to_object_coord_64",
        "command": "set_700C_to_object_coord",
        "args": [AreaObjects.DUMMY_0X07, Coords.F, []],
    },
    {
        "identifier": "ACTION_274_jmp_if_700C_equals_short_65",
        "command": "jmp_if_var_equals_const",
        "args": [0x700C, 1, "ACTION_274_set_sprite_sequence_70"],
    },
    {
        "identifier": "ACTION_274_jmp_if_700C_equals_short_66",
        "command": "jmp_if_var_equals_const",
        "args": [0x700C, 3, "ACTION_274_set_sprite_sequence_72"],
    },
    {
        "identifier": "ACTION_274_jmp_if_700C_equals_short_67",
        "command": "jmp_if_var_equals_const",
        "args": [0x700C, 5, "ACTION_274_set_sprite_sequence_74"],
    },
    {
        "identifier": "ACTION_274_set_sprite_sequence_68",
        "command": "set_sprite_sequence",
        "args": [9, 0, [_0x08Flags.LOOPING_OFF, _0x08Flags.MIRROR_SPRITE]],
    },
    {
        "identifier": "ACTION_274_jmp_69",
        "command": "jmp",
        "args": ["ACTION_274_pause_38"],
    },
    {
        "identifier": "ACTION_274_set_sprite_sequence_70",
        "command": "set_sprite_sequence",
        "args": [8, 0, [_0x08Flags.LOOPING_OFF, _0x08Flags.MIRROR_SPRITE]],
    },
    {
        "identifier": "ACTION_274_jmp_71",
        "command": "jmp",
        "args": ["ACTION_274_pause_38"],
    },
    {
        "identifier": "ACTION_274_set_sprite_sequence_72",
        "command": "set_sprite_sequence",
        "args": [8, 0, [_0x08Flags.LOOPING_OFF]],
    },
    {
        "identifier": "ACTION_274_jmp_73",
        "command": "jmp",
        "args": ["ACTION_274_pause_38"],
    },
    {
        "identifier": "ACTION_274_set_sprite_sequence_74",
        "command": "set_sprite_sequence",
        "args": [9, 0, [_0x08Flags.LOOPING_OFF]],
    },
    {
        "identifier": "ACTION_274_jmp_75",
        "command": "jmp",
        "args": ["ACTION_274_pause_38"],
    },
]
