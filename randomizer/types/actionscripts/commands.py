from strenum import StrEnum


class ActionScriptCommandNames(StrEnum):

    # script operations

    JMP_TO_SCRIPT: str = "jmp_to_script"  # D0
    JMP: str = "jmp"  # D2
    JMP_TO_SUBROUTINE: str = "jmp_to_subroutine"
    START_LOOP_N_FRAMES: str = "start_loop_n_frames"  # D5
    START_LOOP_N_TIMES: str = "start_loop_n_times"  # D4
    END_LOOP: str = "end_loop"  # D7
    PAUSE: str = "pause"  # F0, F1
    JMP_TO_START_OF_THIS_SCRIPT: str = "jmp_to_start_of_this_script"  # F9
    JMP_TO_START_OF_THIS_SCRIPT_FA: str = "jmp_to_start_of_this_script_FA"  # FA
    RET: str = "ret"  # FE
    END_ALL: str = "end_all"  # FF
    DB: str = "db"  # any

    # visibility & collision

    VISIBILITY_ON: str = "visibility_on"  # 00
    VISIBILITY_OFF: str = "visibility_off"  # 01
    RESET_PROPERTIES: str = "reset_properties"  # 08
    OVERWRITE_SOLIDITY: str = "overwrite_solidity"  # 0A
    SET_SOLIDITY_BITS: str = "set_solidity_bits"  # 0B
    CLEAR_SOLIDITY_BITS: str = "clear_solidity_bits"  # 0C
    SET_VRAM_PRIORITY: str = "set_vram_priority"  # 13
    SET_PRIORITY: str = "set_priority"  # FD 0F
    SET_MOVEMENT_BITS: str = "set_movement_bits"  # 15
    SHADOW_ON: str = "shadow_on"  # FD 00
    SHADOW_OFF: str = "shadow_off"  # FD 01
    FLOATING_ON: str = "floating_on"  # FD 02
    FLOATING_OFF: str = "floating_off"  # FD 03

    # memory

    SET_OBJECT_MEMORY_BITS: str = "set_object_memory_bits"  # 11, 12, 14
    OBJECT_MEMORY_SET_BIT: str = "object_memory_set_bit"  # FD 04 - 19
    OBJECT_MEMORY_CLEAR_BIT: str = "object_memory_clear_bit"
    OBJECT_MEMORY_MODIFY_BITS: str = "object_memory_modify_bits"
    SET_BIT: str = "set_bit"  # A0, A1, A2
    CLEAR_BIT: str = "clear_bit"  # A4, A5, A6
    SET_MEM_704X_AT_700C_BIT: str = "set_mem_704x_at_700C_bit"  # A3
    CLEAR_MEM_704X_AT_700C_BIT: str = "clear_mem_704x_at_700C_bit"  # A7
    SET_VAR_TO_CONST: str = "set_var_to_const"  # A8, AC, B0
    ADD_CONST_TO_VAR: str = "add_const_to_var"  # A9, AD, B1
    INC: str = "inc"  # AA, AE, B2
    DEC: str = "dec"  # AB, AF, B3
    COPY_VAR_TO_VAR: str = "copy_var_to_var"  # B4, B5, BA, BB, BC
    COMPARE_VAR_TO_CONST: str = "compare_var_to_const"  # C0, C2
    COMPARE_700C_TO_VAR: str = "compare_700C_to_var"  # C1
    JMP_IF_COMPARISON_RESULT_IS_GREATER_OR_EQUAL: str = (
        "jmp_if_comparison_result_is_greater_or_equal"  # EC
    )
    JMP_IF_COMPARISON_RESULT_IS_LESSER: str = "jmp_if_comparison_result_is_lesser"  # ED
    SET_VAR_TO_RANDOM: str = "set_var_to_random"  # B6, B7
    ADD_VAR_TO_700C: str = "add_var_to_700C"  # B8
    DEC_VAR_FROM_700C: str = "dec_var_from_700C"  # B9
    SWAP_VARS: str = "swap_vars"  # BD
    MOVE_7010_7015_TO_7016_701B: str = "move_7010_7015_to_7016_701B"  # BE
    MOVE_7016_701B_TO_7010_7015: str = "move_7016_701B_to_7010_7015"  # BF
    SET_700C_TO_CURRENT_LEVEL: str = "set_700C_to_current_level"
    LOAD_MEM: str = "load_mem"  # D6
    JMP_IF_BIT_CLEAR: str = "jmp_if_bit_clear"  # DC, DD, DE
    JMP_IF_BIT_SET: str = "jmp_if_bit_set"  # D8, D9, DA
    JMP_IF_MEM_704X_AT_700C_BIT_SET: str = "jmp_if_mem_704x_at_700C_bit_set"  # DB
    JMP_IF_MEM_704X_AT_700C_BIT_CLEAR: str = "jmp_if_mem_704x_at_700C_bit_clear"  # DF
    JMP_IF_VAR_EQUALS_CONST: str = "jmp_if_var_equals_const"  # E0, E2, E4
    JMP_IF_VAR_NOT_EQUALS_CONST: str = "jmp_if_var_not_equals_const"  # E1, E3, E5
    JMP_IF_700C_ALL_BITS_CLEAR: str = "jmp_if_700C_all_bits_clear"  # E6
    JMP_IF_700C_ANY_BITS_SET: str = "jmp_if_700C_any_bits_set"  # E7
    JMP_IF_RANDOM_ABOVE_66: str = "jmp_if_random_above_66"  # E9
    JMP_IF_RANDOM_ABOVE_128: str = "jmp_if_random_above_128"  # E8
    JMP_IF_LOADED_MEMORY_IS_0: str = "jmp_if_loaded_memory_is_0"  # EA
    JMP_IF_LOADED_MEMORY_IS_ABOVE_OR_EQUAL_0: str = (
        "jmp_if_loaded_memory_is_above_or_equal_0"  # EF
    )
    JMP_IF_LOADED_MEMORY_IS_BELOW_0: str = "jmp_if_loaded_memory_is_below_0"  # EE
    JMP_IF_LOADED_MEMORY_IS_NOT_0: str = "jmp_if_loaded_memory_is_not_0"  # EB
    MEM_700C_AND_CONST: str = "mem_700C_and_const"  # FD B0
    MEM_700C_AND_VAR: str = "mem_700C_and_var"  # FD B3
    MEM_700C_OR_CONST: str = "mem_700C_or_const"  # FD B1
    MEM_700C_OR_VAR: str = "mem_700C_or_var"  # FD B4
    MEM_700C_XOR_CONST: str = "mem_700C_xor_const"  # FD B2
    MEM_700C_XOR_VAR: str = "mem_700C_xor_var"  # FD B5
    MEM_700C_SHIFT_LEFT: str = "mem_700C_shift_left"  # FD B6

    # sequencing

    SEQUENCE_PLAYBACK_ON: str = "sequence_playback_on"  # 02
    SEQUENCE_PLAYBACK_OFF: str = "sequence_playback_off"  # 03
    SEQUENCE_LOOPING_ON: str = "sequence_looping_on"  # 04
    SEQUENCE_LOOPING_OFF: str = "sequence_looping_off"  # 05
    SET_ANIMATION_SPEED: str = "set_animation_speed"  # 10
    EMBEDDED_ANIMATION_ROUTINE: str = "embedded_animation_routine"  # 26, 27, 28
    MAXIMIZE_SEQUENCE_SPEED: str = "maximize_sequence_speed"  # 85
    MAXIMIZE_SEQUENCE_SPEED_86: str = "maximize_sequence_speed_86"  # 86

    # positioning

    FIXED_F_COORD_ON: str = "fixed_f_coord_on"  # 06
    FIXED_F_COORD_OFF: str = "fixed_f_coord_off"  # 07
    JMP_IF_OBJECT_WITHIN_RANGE: str = "jmp_if_object_within_range"  # 3A
    JMP_IF_OBJECT_WITHIN_RANGE_SAME_Z: str = "jmp_if_object_within_range_same_z"  # 3B
    WALK_1_STEP_EAST: str = "walk_1_step_east"  # 40
    WALK_1_STEP_SOUTHEAST: str = "walk_1_step_southeast"  # 41
    WALK_1_STEP_SOUTH: str = "walk_1_step_south"  # 42
    WALK_1_STEP_SOUTHWEST: str = "walk_1_step_southwest"  # 43
    WALK_1_STEP_WEST: str = "walk_1_step_west"  # 44
    WALK_1_STEP_NORTHWEST: str = "walk_1_step_northwest"  # 45
    WALK_1_STEP_NORTH: str = "walk_1_step_north"  # 46
    WALK_1_STEP_NORTHEAST: str = "walk_1_step_northeast"  # 47
    WALK_1_STEP_F_DIRECTION: str = "walk_1_step_f_direction"  # 48
    ADD_Z_COORD_1_STEP: str = "add_z_coord_1_step"  # 4A
    DEC_Z_COORD_1_STEP: str = "dec_z_coord_1_step"  # 4B
    SHIFT_EAST_STEPS: str = "shift_east_steps"  # 50
    SHIFT_SOUTHEAST_STEPS: str = "shift_southeast_steps"  # 51
    SHIFT_SOUTH_STEPS: str = "shift_south_steps"  # 52
    SHIFT_SOUTHWEST_STEPS: str = "shift_southwest_steps"  # 53
    SHIFT_WEST_STEPS: str = "shift_west_steps"  # 54
    SHIFT_NORTHWEST_STEPS: str = "shift_northwest_steps"  # 55
    SHIFT_NORTH_STEPS: str = "shift_north_steps"  # 56
    SHIFT_NORTHEAST_STEPS: str = "shift_northeast_steps"  # 57
    SHIFT_F_DIRECTION_STEPS: str = "shift_f_direction_steps"  # 58
    SHIFT_Z_20_STEPS: str = "shift_z_20_steps"  # 59
    SHIFT_Z_UP_STEPS: str = "shift_z_up_steps"  # 5A
    SHIFT_Z_DOWN_STEPS: str = "shift_z_down_steps"  # 5B
    SHIFT_Z_UP_20_STEPS: str = "shift_z_up_20_steps"  # 5C
    SHIFT_Z_DOWN_20_STEPS: str = "shift_z_down_20_steps"  # 5D
    SHIFT_EAST_PIXELS: str = "shift_east_pixels"  # 60
    SHIFT_SOUTHEAST_PIXELS: str = "shift_southeast_pixels"  # 61
    SHIFT_SOUTH_PIXELS: str = "shift_south_pixels"  # 62
    SHIFT_SOUTHWEST_PIXELS: str = "shift_southwest_pixels"  # 63
    SHIFT_WEST_PIXELS: str = "shift_west_pixels"  # 64
    SHIFT_NORTHWEST_PIXELS: str = "shift_northwest_pixels"  # 65
    SHIFT_NORTH_PIXELS: str = "shift_north_pixels"  # 66
    SHIFT_NORTHEAST_PIXELS: str = "shift_northeast_pixels"  # 67
    SHIFT_F_DIRECTION_PIXELS: str = "shift_f_direction_pixels"  # 68
    WALK_F_DIRECTION_16_PIXELS: str = "walk_f_direction_16_pixels"  # 69
    SHIFT_Z_UP_PIXELS: str = "shift_z_up_pixels"  # 6A
    SHIFT_Z_DOWN_PIXELS: str = "shift_z_down_pixels"  # 6B
    FACE_EAST: str = "face_east"  # 70
    FACE_EAST_7C: str = "face_east"  # 7C
    FACE_SOUTHEAST: str = "face_southeast"  # 71
    FACE_SOUTH: str = "face_southeast"  # 72
    FACE_SOUTHWEST: str = "face_southwest"  # 73
    FACE_SOUTHWEST_7D: str = "face_southwest_7D"  # 7D
    FACE_WEST: str = "face_west"  # 74
    FACE_NORTHWEST: str = "face_northwest"  # 75
    FACE_NORTH: str = "face_north"  # 76
    FACE_NORTHEAST: str = "face_northeast"  # 77
    FACE_MARIO: str = "face_mario"  # 78
    TURN_CLOCKWISE_45_DEGREES: str = "turn_clockwise_45_degrees"  # 79
    TURN_RANDOM_DIRECTION: str = "turn_random_direction"  # 7A
    TURN_CLOCKWISE_45_DEGREES_N_TIMES: str = "turn_clockwise_45_degrees_n_times"  # 7B
    JUMP_TO_HEIGHT_SILENT: str = "jump_to_height_silent"  # 7E
    JUMP_TO_HEIGHT: str = "jump_to_height"  # 7F
    WALK_TO_XY_COORDS: str = "walk_to_xy_coords"  # 80
    WALK_XY_STEPS: str = "walk_xy_steps"  # 81
    SHIFT_TO_XY_COORDS: str = "shift_to_xy_coords"  # 82
    SHIFT_XY_STEPS: str = "shift_xy_steps"  # 83
    SHIFT_XY_PIXELS: str = "shift_xy_pixels"  # 84
    TRANSFER_TO_OBJECT_XY: str = "transfer_to_object_xy"  # 87
    TRANSFER_TO_OBJECT_XYZ: str = "transfer_to_object_xyz"  # 95
    RUN_AWAY_SHIFT: str = "run_away_shift"  # 88
    TRANSFER_TO_7016_7018: str = "transfer_to_7016_7018"  # 89
    TRANSFER_TO_7016_7018_701A: str = "transfer_to_7016_7018_701A"  # 99
    WALK_TO_7016_7018: str = "walk_to_7016_7018"  # 8A
    WALK_TO_7016_7018_701A: str = "walk_to_7016_7018_701A"  # 98
    BOUNCE_TO_XY_WITH_HEIGHT: str = "bounce_to_xy_with_height"  # 90
    BOUNCE_XY_STEPS_WITH_HEIGHT: str = "bounce_xy_steps_with_height"  # 91
    TRANSFER_TO_XYZF: str = "transfer_to_xyzf"  # 92
    TRANSFER_XYZF_STEPS: str = "transfer_xyzf_steps"  # 93
    TRANSFER_XYZF_PIXELS: str = "transfer_xyzf_pixels"  # 94

    # room objects and camera

    SET_700C_TO_OBJECT_COORD: str = "set_700C_to_object_coord"  # C4, C5, C6
    CREATE_PACKET_AT_NPC_COORDS: str = "create_packet_at_npc_coords"  # 3E
    CREATE_PACKET_AT_7010: str = "create_packet_at_7010"  # 3F
    CREATE_PACKET_AT_7010_WITH_EVENT: str = "create_packet_at_7010_with_event"  # FD 3E
    SUMMON_TO_LEVEL: str = "summon_to_level"  # F2
    SUMMON_OBJECT_AT_70A8_TO_CURRENT_LEVEL: str = (
        "summon_object_at_70A8_to_current_level"  # F4
    )
    REMOVE_FROM_LEVEL: str = "remove_from_level"  # F2
    REMOVE_OBJECT_AT_70A8_FROM_CURRENT_LEVEL: str = (
        "remove_object_at_70A8_from_current_level"  # F5
    )
    ENABLE_TRIGGER_IN_LEVEL: str = "enable_trigger_in_level"  # F3
    ENABLE_TRIGGER_AT_70A8: str = "enable_trigger_at_70A8"  # F6
    DISABLE_TRIGGER_IN_LEVEL: str = "disable_trigger_in_level"  # F3
    DISABLE_TRIGGER_AT_70A8: str = "disable_trigger_at_70A8"  # F7
    JMP_IF_OBJECT_IN_LEVEL: str = "jmp_if_object_in_level"  # F8
    JMP_IF_OBJECT_NOT_IN_LEVEL: str = "jmp_if_object_not_in_level"  # F8
    JMP_IF_OBJECT_IN_AIR: str = "jmp_if_object_in_air"  # FD 3D

    # controls

    SET_700C_TO_PRESSED_BUTTON: str = "set_700C_to_pressed_button"  # CA
    SET_700C_TO_TAPPED_BUTTON: str = "set_700C_to_tapped_button"  # CB

    # palettes

    SET_PALETTE_ROW: str = "set_palette_row"  # 0D
    INC_PALETTE_ROW_BY: str = "inc_palette_row_by"  # 0E
    INC_PALETTE_ROW_BY_1: str = "inc_palette_row_by_1"  # 0F

    # branching / jumps

    BPL_26_27_28: str = "bpl_26_27_28"  # 21
    BMI_26_27_28: str = "bmi_26_27_28"  # 22
    BPL_26_27: str = "bpl_26_27"  # 2A
    UNKNOWN_JMP_3C: str = "unknown_jmp_3C"  # 3C
    JMP_IF_MARIO_IN_AIR: str = "jmp_if_mario_in_air"  # 3D

    # music

    STOP_SOUND: str = "stop_sound"  # 9B
    PLAY_SOUND: str = "play_sound"  # 9C, FD 9E
    PLAY_SOUND_BALANCE: str = "play_sound_balance"  # 9D
    FADE_OUT_SOUND_TO_VOLUME: str = "fade_out_sound_to_volume"  # 9E


class ActionScriptCommand:
    command_name: ActionScriptCommandNames = None
    identifier: str = None

    def __init__(self, identifier) -> None:
        self.identifier = identifier


# script operations


class JmpToScript(ActionScriptCommand):
    command_name: ActionScriptCommandNames = ActionScriptCommandNames.JMP_TO_SCRIPT
    destination: int = -1

    def __init__(self, identifier, destination: int) -> None:
        assert 0 <= destination <= 4095
        super().__init__(identifier)
        self.destination = destination
