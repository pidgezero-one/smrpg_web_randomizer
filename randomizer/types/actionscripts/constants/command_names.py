from .classes import ActionScriptCommandName

JMP_TO_SCRIPT: ActionScriptCommandName = "jmp_to_script"  # D0
JMP: ActionScriptCommandName = "jmp"  # D2
JMP_TO_SUBROUTINE: ActionScriptCommandName = "jmp_to_subroutine"
START_LOOP_N_FRAMES: ActionScriptCommandName = "start_loop_n_frames"  # D5
START_LOOP_N_TIMES: ActionScriptCommandName = "start_loop_n_times"  # D4
END_LOOP: ActionScriptCommandName = "end_loop"  # D7
PAUSE: ActionScriptCommandName = "pause"  # F0, F1
JMP_TO_START_OF_THIS_SCRIPT: ActionScriptCommandName = "jmp_to_start_of_this_script"  # F9
JMP_TO_START_OF_THIS_SCRIPT_FA: ActionScriptCommandName = "jmp_to_start_of_this_script_FA"  # FA
RET: ActionScriptCommandName = "ret"  # FE
END_ALL: ActionScriptCommandName = "end_all"  # FF
DB: ActionScriptCommandName = "db"  # any

# visibility & collision

VISIBILITY_ON: ActionScriptCommandName = "visibility_on"  # 00
VISIBILITY_OFF: ActionScriptCommandName = "visibility_off"  # 01
RESET_PROPERTIES: ActionScriptCommandName = "reset_properties"  # 08
OVERWRITE_SOLIDITY: ActionScriptCommandName = "overwrite_solidity"  # 0A
SET_SOLIDITY_BITS: ActionScriptCommandName = "set_solidity_bits"  # 0B
CLEAR_SOLIDITY_BITS: ActionScriptCommandName = "clear_solidity_bits"  # 0C
SET_MOVEMENT_BITS: ActionScriptCommandName = "set_movement_bits"  # 15
SET_VRAM_PRIORITY: ActionScriptCommandName = "set_vram_priority"  # 13
SET_PRIORITY: ActionScriptCommandName = "set_priority"  # FD 0F
SHADOW_ON: ActionScriptCommandName = "shadow_on"  # FD 00
SHADOW_OFF: ActionScriptCommandName = "shadow_off"  # FD 01
FLOATING_ON: ActionScriptCommandName = "floating_on"  # FD 02
FLOATING_OFF: ActionScriptCommandName = "floating_off"  # FD 03

# memory

SET_OBJECT_MEMORY_BITS: ActionScriptCommandName = "set_object_memory_bits"  # 11, 12, 14
OBJECT_MEMORY_SET_BIT: ActionScriptCommandName = "object_memory_set_bit"  # FD 04 - 19
OBJECT_MEMORY_CLEAR_BIT: ActionScriptCommandName = "object_memory_clear_bit"
OBJECT_MEMORY_MODIFY_BITS: ActionScriptCommandName = "object_memory_modify_bits"
SET_BIT: ActionScriptCommandName = "set_bit"  # A0, A1, A2
CLEAR_BIT: ActionScriptCommandName = "clear_bit"  # A4, A5, A6
SET_MEM_704X_AT_700C_BIT: ActionScriptCommandName = "set_mem_704x_at_700C_bit"  # A3
CLEAR_MEM_704X_AT_700C_BIT: ActionScriptCommandName = "clear_mem_704x_at_700C_bit"  # A7
SET_VAR_TO_CONST: ActionScriptCommandName = "set_var_to_const"  # A8, AC, B0
ADD_CONST_TO_VAR: ActionScriptCommandName = "add_const_to_var"  # A9, AD, B1
INC: ActionScriptCommandName = "inc"  # AA, AE, B2
DEC: ActionScriptCommandName = "dec"  # AB, AF, B3
COPY_VAR_TO_VAR: ActionScriptCommandName = "copy_var_to_var"  # B4, B5, BA, BB, BC
COMPARE_VAR_TO_CONST: ActionScriptCommandName = "compare_var_to_const"  # C0, C2
COMPARE_700C_TO_VAR: ActionScriptCommandName = "compare_700C_to_var"  # C1
JMP_IF_COMPARISON_RESULT_IS_GREATER_OR_EQUAL: ActionScriptCommandName = (
    "jmp_if_comparison_result_is_greater_or_equal"  # EC
)
JMP_IF_COMPARISON_RESULT_IS_LESSER: ActionScriptCommandName = "jmp_if_comparison_result_is_lesser"  # ED
SET_VAR_TO_RANDOM: ActionScriptCommandName = "set_var_to_random"  # B6, B7
ADD_VAR_TO_700C: ActionScriptCommandName = "add_var_to_700C"  # B8
DEC_VAR_FROM_700C: ActionScriptCommandName = "dec_var_from_700C"  # B9
SWAP_VARS: ActionScriptCommandName = "swap_vars"  # BD
MOVE_7010_7015_TO_7016_701B: ActionScriptCommandName = "move_7010_7015_to_7016_701B"  # BE
MOVE_7016_701B_TO_7010_7015: ActionScriptCommandName = "move_7016_701B_to_7010_7015"  # BF
SET_700C_TO_CURRENT_LEVEL: ActionScriptCommandName = "set_700C_to_current_level"
LOAD_MEM: ActionScriptCommandName = "load_mem"  # D6
JMP_IF_BIT_CLEAR: ActionScriptCommandName = "jmp_if_bit_clear"  # DC, DD, DE
JMP_IF_BIT_SET: ActionScriptCommandName = "jmp_if_bit_set"  # D8, D9, DA
JMP_IF_MEM_704X_AT_700C_BIT_SET: ActionScriptCommandName = "jmp_if_mem_704x_at_700C_bit_set"  # DB
JMP_IF_MEM_704X_AT_700C_BIT_CLEAR: ActionScriptCommandName = "jmp_if_mem_704x_at_700C_bit_clear"  # DF
JMP_IF_VAR_EQUALS_CONST: ActionScriptCommandName = "jmp_if_var_equals_const"  # E0, E2, E4
JMP_IF_VAR_NOT_EQUALS_CONST: ActionScriptCommandName = "jmp_if_var_not_equals_const"  # E1, E3, E5
JMP_IF_700C_ALL_BITS_CLEAR: ActionScriptCommandName = "jmp_if_700C_all_bits_clear"  # E6
JMP_IF_700C_ANY_BITS_SET: ActionScriptCommandName = "jmp_if_700C_any_bits_set"  # E7
JMP_IF_RANDOM_ABOVE_66: ActionScriptCommandName = "jmp_if_random_above_66"  # E9
JMP_IF_RANDOM_ABOVE_128: ActionScriptCommandName = "jmp_if_random_above_128"  # E8
JMP_IF_LOADED_MEMORY_IS_0: ActionScriptCommandName = "jmp_if_loaded_memory_is_0"  # EA
JMP_IF_LOADED_MEMORY_IS_ABOVE_OR_EQUAL_0: ActionScriptCommandName = (
    "jmp_if_loaded_memory_is_above_or_equal_0"  # EF
)
JMP_IF_LOADED_MEMORY_IS_BELOW_0: ActionScriptCommandName = "jmp_if_loaded_memory_is_below_0"  # EE
JMP_IF_LOADED_MEMORY_IS_NOT_0: ActionScriptCommandName = "jmp_if_loaded_memory_is_not_0"  # EB
MEM_700C_AND_CONST: ActionScriptCommandName = "mem_700C_and_const"  # FD B0
MEM_700C_AND_VAR: ActionScriptCommandName = "mem_700C_and_var"  # FD B3
MEM_700C_OR_CONST: ActionScriptCommandName = "mem_700C_or_const"  # FD B1
MEM_700C_OR_VAR: ActionScriptCommandName = "mem_700C_or_var"  # FD B4
MEM_700C_XOR_CONST: ActionScriptCommandName = "mem_700C_xor_const"  # FD B2
MEM_700C_XOR_VAR: ActionScriptCommandName = "mem_700C_xor_var"  # FD B5
MEM_700C_SHIFT_LEFT: ActionScriptCommandName = "mem_700C_shift_left"  # FD B6

# sequencing

SEQUENCE_PLAYBACK_ON: ActionScriptCommandName = "sequence_playback_on"  # 02
SEQUENCE_PLAYBACK_OFF: ActionScriptCommandName = "sequence_playback_off"  # 03
SEQUENCE_LOOPING_ON: ActionScriptCommandName = "sequence_looping_on"  # 04
SEQUENCE_LOOPING_OFF: ActionScriptCommandName = "sequence_looping_off"  # 05
SET_ANIMATION_SPEED: ActionScriptCommandName = "set_animation_speed"  # 10
EMBEDDED_ANIMATION_ROUTINE: ActionScriptCommandName = "embedded_animation_routine"  # 26, 27, 28
MAXIMIZE_SEQUENCE_SPEED: ActionScriptCommandName = "maximize_sequence_speed"  # 85
MAXIMIZE_SEQUENCE_SPEED_86: ActionScriptCommandName = "maximize_sequence_speed_86"  # 86

# positioning

FIXED_F_COORD_ON: ActionScriptCommandName = "fixed_f_coord_on"  # 06
FIXED_F_COORD_OFF: ActionScriptCommandName = "fixed_f_coord_off"  # 07
JMP_IF_OBJECT_WITHIN_RANGE: ActionScriptCommandName = "jmp_if_object_within_range"  # 3A
JMP_IF_OBJECT_WITHIN_RANGE_SAME_Z: ActionScriptCommandName = "jmp_if_object_within_range_same_z"  # 3B
WALK_1_STEP_EAST: ActionScriptCommandName = "walk_1_step_east"  # 40
WALK_1_STEP_SOUTHEAST: ActionScriptCommandName = "walk_1_step_southeast"  # 41
WALK_1_STEP_SOUTH: ActionScriptCommandName = "walk_1_step_south"  # 42
WALK_1_STEP_SOUTHWEST: ActionScriptCommandName = "walk_1_step_southwest"  # 43
WALK_1_STEP_WEST: ActionScriptCommandName = "walk_1_step_west"  # 44
WALK_1_STEP_NORTHWEST: ActionScriptCommandName = "walk_1_step_northwest"  # 45
WALK_1_STEP_NORTH: ActionScriptCommandName = "walk_1_step_north"  # 46
WALK_1_STEP_NORTHEAST: ActionScriptCommandName = "walk_1_step_northeast"  # 47
WALK_1_STEP_F_DIRECTION: ActionScriptCommandName = "walk_1_step_f_direction"  # 48
ADD_Z_COORD_1_STEP: ActionScriptCommandName = "add_z_coord_1_step"  # 4A
DEC_Z_COORD_1_STEP: ActionScriptCommandName = "dec_z_coord_1_step"  # 4B
SHIFT_EAST_STEPS: ActionScriptCommandName = "shift_east_steps"  # 50
SHIFT_SOUTHEAST_STEPS: ActionScriptCommandName = "shift_southeast_steps"  # 51
SHIFT_SOUTH_STEPS: ActionScriptCommandName = "shift_south_steps"  # 52
SHIFT_SOUTHWEST_STEPS: ActionScriptCommandName = "shift_southwest_steps"  # 53
SHIFT_WEST_STEPS: ActionScriptCommandName = "shift_west_steps"  # 54
SHIFT_NORTHWEST_STEPS: ActionScriptCommandName = "shift_northwest_steps"  # 55
SHIFT_NORTH_STEPS: ActionScriptCommandName = "shift_north_steps"  # 56
SHIFT_NORTHEAST_STEPS: ActionScriptCommandName = "shift_northeast_steps"  # 57
SHIFT_F_DIRECTION_STEPS: ActionScriptCommandName = "shift_f_direction_steps"  # 58
SHIFT_Z_20_STEPS: ActionScriptCommandName = "shift_z_20_steps"  # 59
SHIFT_Z_UP_STEPS: ActionScriptCommandName = "shift_z_up_steps"  # 5A
SHIFT_Z_DOWN_STEPS: ActionScriptCommandName = "shift_z_down_steps"  # 5B
SHIFT_Z_UP_20_STEPS: ActionScriptCommandName = "shift_z_up_20_steps"  # 5C
SHIFT_Z_DOWN_20_STEPS: ActionScriptCommandName = "shift_z_down_20_steps"  # 5D
SHIFT_EAST_PIXELS: ActionScriptCommandName = "shift_east_pixels"  # 60
SHIFT_SOUTHEAST_PIXELS: ActionScriptCommandName = "shift_southeast_pixels"  # 61
SHIFT_SOUTH_PIXELS: ActionScriptCommandName = "shift_south_pixels"  # 62
SHIFT_SOUTHWEST_PIXELS: ActionScriptCommandName = "shift_southwest_pixels"  # 63
SHIFT_WEST_PIXELS: ActionScriptCommandName = "shift_west_pixels"  # 64
SHIFT_NORTHWEST_PIXELS: ActionScriptCommandName = "shift_northwest_pixels"  # 65
SHIFT_NORTH_PIXELS: ActionScriptCommandName = "shift_north_pixels"  # 66
SHIFT_NORTHEAST_PIXELS: ActionScriptCommandName = "shift_northeast_pixels"  # 67
SHIFT_F_DIRECTION_PIXELS: ActionScriptCommandName = "shift_f_direction_pixels"  # 68
WALK_F_DIRECTION_16_PIXELS: ActionScriptCommandName = "walk_f_direction_16_pixels"  # 69
SHIFT_Z_UP_PIXELS: ActionScriptCommandName = "shift_z_up_pixels"  # 6A
SHIFT_Z_DOWN_PIXELS: ActionScriptCommandName = "shift_z_down_pixels"  # 6B
FACE_EAST: ActionScriptCommandName = "face_east"  # 70
FACE_EAST_7C: ActionScriptCommandName = "face_east"  # 7C
FACE_SOUTHEAST: ActionScriptCommandName = "face_southeast"  # 71
FACE_SOUTH: ActionScriptCommandName = "face_southeast"  # 72
FACE_SOUTHWEST: ActionScriptCommandName = "face_southwest"  # 73
FACE_SOUTHWEST_7D: ActionScriptCommandName = "face_southwest_7D"  # 7D
FACE_WEST: ActionScriptCommandName = "face_west"  # 74
FACE_NORTHWEST: ActionScriptCommandName = "face_northwest"  # 75
FACE_NORTH: ActionScriptCommandName = "face_north"  # 76
FACE_NORTHEAST: ActionScriptCommandName = "face_northeast"  # 77
FACE_MARIO: ActionScriptCommandName = "face_mario"  # 78
TURN_CLOCKWISE_45_DEGREES: ActionScriptCommandName = "turn_clockwise_45_degrees"  # 79
TURN_RANDOM_DIRECTION: ActionScriptCommandName = "turn_random_direction"  # 7A
TURN_CLOCKWISE_45_DEGREES_N_TIMES: ActionScriptCommandName = "turn_clockwise_45_degrees_n_times"  # 7B
JUMP_TO_HEIGHT_SILENT: ActionScriptCommandName = "jump_to_height_silent"  # 7E
JUMP_TO_HEIGHT: ActionScriptCommandName = "jump_to_height"  # 7F
WALK_TO_XY_COORDS: ActionScriptCommandName = "walk_to_xy_coords"  # 80
WALK_XY_STEPS: ActionScriptCommandName = "walk_xy_steps"  # 81
SHIFT_TO_XY_COORDS: ActionScriptCommandName = "shift_to_xy_coords"  # 82
SHIFT_XY_STEPS: ActionScriptCommandName = "shift_xy_steps"  # 83
SHIFT_XY_PIXELS: ActionScriptCommandName = "shift_xy_pixels"  # 84
TRANSFER_TO_OBJECT_XY: ActionScriptCommandName = "transfer_to_object_xy"  # 87
TRANSFER_TO_OBJECT_XYZ: ActionScriptCommandName = "transfer_to_object_xyz"  # 95
RUN_AWAY_SHIFT: ActionScriptCommandName = "run_away_shift"  # 88
TRANSFER_TO_7016_7018: ActionScriptCommandName = "transfer_to_7016_7018"  # 89
TRANSFER_TO_7016_7018_701A: ActionScriptCommandName = "transfer_to_7016_7018_701A"  # 99
WALK_TO_7016_7018: ActionScriptCommandName = "walk_to_7016_7018"  # 8A
WALK_TO_7016_7018_701A: ActionScriptCommandName = "walk_to_7016_7018_701A"  # 98
BOUNCE_TO_XY_WITH_HEIGHT: ActionScriptCommandName = "bounce_to_xy_with_height"  # 90
BOUNCE_XY_STEPS_WITH_HEIGHT: ActionScriptCommandName = "bounce_xy_steps_with_height"  # 91
TRANSFER_TO_XYZF: ActionScriptCommandName = "transfer_to_xyzf"  # 92
TRANSFER_XYZF_STEPS: ActionScriptCommandName = "transfer_xyzf_steps"  # 93
TRANSFER_XYZF_PIXELS: ActionScriptCommandName = "transfer_xyzf_pixels"  # 94

# room objects and camera

SET_700C_TO_OBJECT_COORD: ActionScriptCommandName = "set_700C_to_object_coord"  # C4, C5, C6
CREATE_PACKET_AT_NPC_COORDS: ActionScriptCommandName = "create_packet_at_npc_coords"  # 3E
CREATE_PACKET_AT_7010: ActionScriptCommandName = "create_packet_at_7010"  # 3F
CREATE_PACKET_AT_7010_WITH_EVENT: ActionScriptCommandName = "create_packet_at_7010_with_event"  # FD 3E
SUMMON_TO_LEVEL: ActionScriptCommandName = "summon_to_level"  # F2
SUMMON_OBJECT_AT_70A8_TO_CURRENT_LEVEL: ActionScriptCommandName = (
    "summon_object_at_70A8_to_current_level"  # F4
)
REMOVE_FROM_LEVEL: ActionScriptCommandName = "remove_from_level"  # F2
REMOVE_OBJECT_AT_70A8_FROM_CURRENT_LEVEL: ActionScriptCommandName = (
    "remove_object_at_70A8_from_current_level"  # F5
)
ENABLE_TRIGGER_IN_LEVEL: ActionScriptCommandName = "enable_trigger_in_level"  # F3
ENABLE_TRIGGER_AT_70A8: ActionScriptCommandName = "enable_trigger_at_70A8"  # F6
DISABLE_TRIGGER_IN_LEVEL: ActionScriptCommandName = "disable_trigger_in_level"  # F3
DISABLE_TRIGGER_AT_70A8: ActionScriptCommandName = "disable_trigger_at_70A8"  # F7
JMP_IF_OBJECT_IN_LEVEL: ActionScriptCommandName = "jmp_if_object_in_level"  # F8
JMP_IF_OBJECT_NOT_IN_LEVEL: ActionScriptCommandName = "jmp_if_object_not_in_level"  # F8
JMP_IF_OBJECT_IN_AIR: ActionScriptCommandName = "jmp_if_object_in_air"  # FD 3D

# controls

SET_700C_TO_PRESSED_BUTTON: ActionScriptCommandName = "set_700C_to_pressed_button"  # CA
SET_700C_TO_TAPPED_BUTTON: ActionScriptCommandName = "set_700C_to_tapped_button"  # CB

# palettes

SET_PALETTE_ROW: ActionScriptCommandName = "set_palette_row"  # 0D
INC_PALETTE_ROW_BY: ActionScriptCommandName = "inc_palette_row_by"  # 0E
INC_PALETTE_ROW_BY_1: ActionScriptCommandName = "inc_palette_row_by_1"  # 0F

# branching / jumps

BPL_26_27_28: ActionScriptCommandName = "bpl_26_27_28"  # 21
BMI_26_27_28: ActionScriptCommandName = "bmi_26_27_28"  # 22
BPL_26_27: ActionScriptCommandName = "bpl_26_27"  # 2A
UNKNOWN_JMP_3C: ActionScriptCommandName = "unknown_jmp_3C"  # 3C
JMP_IF_MARIO_IN_AIR: ActionScriptCommandName = "jmp_if_mario_in_air"  # 3D

# music

STOP_SOUND: ActionScriptCommandName = "stop_sound"  # 9B
PLAY_SOUND: ActionScriptCommandName = "play_sound"  # 9C, FD 9E
PLAY_SOUND_BALANCE: ActionScriptCommandName = "play_sound_balance"  # 9D
FADE_OUT_SOUND_TO_VOLUME: ActionScriptCommandName = "fade_out_sound_to_volume"  # 9E
