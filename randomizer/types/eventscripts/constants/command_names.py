from .classes import EventScriptCommandName

# script operations

START_LOOP_N_FRAMES: EventScriptCommandName = "start_loop_n_frames"  # D5
START_LOOP_N_TIMES: EventScriptCommandName = "start_loop_n_times"  # D4
END_LOOP: EventScriptCommandName = "end_loop"  # D7
JMP: EventScriptCommandName = "jmp"  # D2
JMP_TO_EVENT: EventScriptCommandName = "jmp_to_event"  # D0
JMP_TO_START_OF_THIS_SCRIPT: EventScriptCommandName = (
    "jmp_to_start_of_this_script"  # F9
)
JMP_TO_START_OF_THIS_SCRIPT_FA: EventScriptCommandName = (
    "jmp_to_start_of_this_script_FA"  # FA
)
JMP_TO_SUBROUTINE: EventScriptCommandName = "jmp_to_subroutine"
MOVE_SCRIPT_TO_MAIN_THREAD: EventScriptCommandName = (
    "move_script_to_main_thread"  # FD 40
)
MOVE_SCRIPT_TO_BACKGROUND_THREAD_1: EventScriptCommandName = (
    "move_script_to_background_thread_1"  # FD 41
)
MOVE_SCRIPT_TO_BACKGROUND_THREAD_2: EventScriptCommandName = (
    "move_script_to_background_thread_2"  # FD 42
)
PAUSE: EventScriptCommandName = "pause"  # F0, F1
REMEMBER_LAST_OBJECT: EventScriptCommandName = "remember_last_object"  # FD 32
RESUME_BACKGROUND_EVENT: EventScriptCommandName = "resume_background_event"  # 47
RUN_BACKGROUND_EVENT: EventScriptCommandName = "run_background_event"  # 40
RUN_BACKGROUND_EVENT_WITH_PAUSE: EventScriptCommandName = (
    "run_background_event_with_pause"  # 44
)
RUN_BACKGROUND_EVENT_WITH_PAUSE_RETURN_ON_EXIT: EventScriptCommandName = (
    "run_background_event_with_pause_return_on_exit"  # 45
)
RUN_EVENT_AT_RETURN: EventScriptCommandName = "run_event_at_return"  # FD 46
RUN_EVENT_AS_SUBROUTINE: EventScriptCommandName = "run_event_as_subroutine"  # D1
STOP_ALL_BACKGROUND_EVENTS: EventScriptCommandName = (
    "stop_all_background_events"  # FD 43
)
STOP_BACKGROUND_EVENT: EventScriptCommandName = "stop_background_event"  # FD 5A
RET: EventScriptCommandName = "ret"  # FE
END_ALL: EventScriptCommandName = "end_all"  # FF
RETURN_FD: EventScriptCommandName = "return_fd"  # FD FE
DB: EventScriptCommandName = "db"  # any

# memory operations

IF_0210_BITS_012_CLEAR_DO_NOT_JUMP: EventScriptCommandName = (
    "if_0210_bits_012_clear_do_not_jump"  # FD 62
)
JMP_IF_316D_IS_3: EventScriptCommandName = "jmp_if_316D_is_3"  # 41
JMP_IF_7000_ALL_BITS_CLEAR: EventScriptCommandName = "jmp_if_7000_all_bits_clear"  # E6
JMP_IF_7000_ANY_BITS_SET: EventScriptCommandName = "jmp_if_7000_any_bits_set"  # E7
JMP_IF_BIT_CLEAR: EventScriptCommandName = "jmp_if_bit_clear"  # DC, DD, DE
JMP_IF_BIT_SET: EventScriptCommandName = "jmp_if_bit_set"  # D8, D9, DA
JMP_IF_LOADED_MEMORY_IS_0: EventScriptCommandName = "jmp_if_loaded_memory_is_0"  # EA
JMP_IF_LOADED_MEMORY_IS_ABOVE_OR_EQUAL_0: EventScriptCommandName = (
    "jmp_if_loaded_memory_is_above_or_equal_0"  # EF
)
JMP_IF_LOADED_MEMORY_IS_BELOW_0: EventScriptCommandName = (
    "jmp_if_loaded_memory_is_below_0"  # EE
)
JMP_IF_LOADED_MEMORY_IS_NOT_0: EventScriptCommandName = (
    "jmp_if_loaded_memory_is_not_0"  # EB
)
JMP_IF_MEM_704X_AT_7000_BIT_CLEAR: EventScriptCommandName = (
    "jmp_if_mem_704x_at_7000_bit_clear"  # DF
)
JMP_IF_MEM_704X_AT_7000_BIT_SET: EventScriptCommandName = (
    "jmp_if_mem_704x_at_7000_bit_set"  # DB
)
SET_MEM_704X_AT_7000_BIT: EventScriptCommandName = "set_mem_704x_at_7000_bit"  # A3
CLEAR_MEM_704X_AT_7000_BIT: EventScriptCommandName = "clear_mem_704x_at_7000_bit"  # A7
MOVE_7010_7015_TO_7016_701B: EventScriptCommandName = (
    "move_7010_7015_to_7016_701B"  # BE
)
MOVE_7016_701B_TO_7010_7015: EventScriptCommandName = (
    "move_7016_701B_to_7010_7015"  # BF
)
SET_VAR_TO_CONST: EventScriptCommandName = "set_var_to_const"  # A8, AC, B0
READ_FROM_ADDRESS: EventScriptCommandName = "read_from_address"  # 5C
SET_7000_TO_7F_MEM_VAR: EventScriptCommandName = "set_7000_to_7F_mem_var"  # FD AC
SET_BIT: EventScriptCommandName = "set_bit"  # A0, A1, A2
SET_BIT_3: EventScriptCommandName = "set_bit_3"  # FD FA
SET_BIT_3_OFFSET: EventScriptCommandName = "set_bit_3_offset"  # FD 8B
SET_BIT_7_OFFSET: EventScriptCommandName = "set_bit_7_offset"  # FD 88
CLEAR_BIT_7_OFFSET: EventScriptCommandName = "set_bit_7_offset"  # FD 89
COPY_VAR_TO_VAR: EventScriptCommandName = "copy_var_to_var"  # B4, B5, BA, BB, BC
STORE_BYTES_TO_0335_0556: EventScriptCommandName = "store_bytes_to_0335_0556"  # FD 90
STORE_00_TO_0348: EventScriptCommandName = "store_00_to_0248"  # FD FC
STORE_00_TO_0334: EventScriptCommandName = "store_00_to_0334"  # FD 93
STORE_01_TO_0248: EventScriptCommandName = "store_01_to_0248"  # FD FB
STORE_01_TO_0335: EventScriptCommandName = "store_01_to_0335"  # FD 92
STORE_02_TO_0248: EventScriptCommandName = "store_02_to_0248"  # FD FD
STORE_FF_TO_0335: EventScriptCommandName = "store_FF_to_0335"  # FD 91
STORE_7000_MINECART_TIMER: EventScriptCommandName = "store_7000_minecart_timer"  # FD B8
STORE_SET_BITS: EventScriptCommandName = "store_set_bits"  # FD A8, FD A9, FD AA
SWAP_VARS: EventScriptCommandName = "swap_vars"

# math operations

ADD_CONST_TO_VAR: EventScriptCommandName = "add_const_to_var"  # A9, AD, B1
INC: EventScriptCommandName = "inc"  # AA, AE, B2
DEC: EventScriptCommandName = "dec"  # AB, AF, B3
ADD_VAR_TO_7000: EventScriptCommandName = "add_var_to_7000"  # B8
DEC_VAR_FROM_7000: EventScriptCommandName = "dec_var_from_7000"  # # B9
CLEAR_BIT: EventScriptCommandName = "clear_bit"  # 0xA4, 0xA5, 0xA6
CLEAR_7016_TO_7018_AND_ISOLATE_701A_HIGH_BYTE_IF_7018_BIT_0_SET: EventScriptCommandName = (
    "clear_7016_to_7018_and_isolate_701A_high_byte_if_7018_bit_0_set"  # FD 0xC6
)
GENERATE_RANDOM_NUM_FROM_RANGE_VAR: EventScriptCommandName = (
    "generate_random_num_from_range_var"  # FD B7
)
JMP_IF_RANDOM_ABOVE_66: EventScriptCommandName = "jmp_if_random_above_66"  # E9
JMP_IF_RANDOM_ABOVE_128: EventScriptCommandName = "jmp_if_random_above_128"  # E8
SET_VAR_TO_RANDOM: EventScriptCommandName = "set_var_to_random"  # B6, B7
COMPARE_VAR_TO_CONST: EventScriptCommandName = "compare_var_to_const"  # C0, C2
COMPARE_7000_TO_VAR: EventScriptCommandName = "compare_7000_to_var"  # C1
JMP_IF_COMPARISON_RESULT_IS_GREATER_OR_EQUAL: EventScriptCommandName = (
    "jmp_if_comparison_result_is_greater_or_equal"  # EC
)
JMP_IF_COMPARISON_RESULT_IS_LESSER: EventScriptCommandName = (
    "jmp_if_comparison_result_is_lesser"  # ED
)
JMP_IF_VAR_EQUALS_CONST: EventScriptCommandName = (
    "jmp_if_var_equals_const"  # E0, E2, E4
)
JMP_IF_VAR_NOT_EQUALS_CONST: EventScriptCommandName = (
    "jmp_if_var_not_equals_const"  # E1, E3, E5
)
MEM_7000_AND_CONST: EventScriptCommandName = "mem_7000_and_const"  # FD B0
MEM_7000_AND_VAR: EventScriptCommandName = "mem_7000_and_var"  # FD B3
MEM_7000_OR_CONST: EventScriptCommandName = "mem_7000_or_const"  # FD B1
MEM_7000_OR_VAR: EventScriptCommandName = "mem_7000_or_var"  # FD B4
MEM_7000_SHIFT_LEFT: EventScriptCommandName = "mem_7000_shift_left"  # FD B6
MEM_7000_XOR_CONST: EventScriptCommandName = "mem_7000_xor_const"  # FD B2
MEM_7000_XOR_VAR: EventScriptCommandName = "mem_7000_xor_var"  # FD B5
MULTIPLY_AND_ADD_MEM_3148_STORE_TO_OFFSET_7FB000_PLUS_OUTPUTX2: EventScriptCommandName = (
    "multiply_and_add_mem_3148_store_to_offset_7FB000_plus_outputx2"  # FD C8
)
XOR_3105_WITH_01: EventScriptCommandName = "xor_3105_with_01"  # FD FE

# room objects & camera

ACTION_QUEUE: EventScriptCommandName = "action_queue"
START_EMBEDDED_ACTION_SCRIPT: EventScriptCommandName = (
    "start_embedded_action_script"  # xx F0, xx F1
)
NON_EMBEDDED_ACTION_QUEUE: EventScriptCommandName = "non_embedded_action_queue"
SET_ACTION_SCRIPT: EventScriptCommandName = "set_action_script"  # xx F2, xx F3
SET_TEMP_ACTION_SCRIPT: EventScriptCommandName = (
    "set_temp_action_script"  # xx F4, xx F5
)
UNSYNC_ACTION_SCRIPT: EventScriptCommandName = "unsync_action_script"  # xx F6
SUMMON_TO_LEVEL: EventScriptCommandName = "summon_to_level"  # F2
SUMMON_TO_CURRENT_LEVEL: EventScriptCommandName = "summon_to_current_level"  # xx F8
SUMMON_TO_CURRENT_LEVEL_AT_MARIOS_COORDS: EventScriptCommandName = (
    "summon_to_current_level_at_marios_coords"  # xx F7
)
SUMMON_OBJECT_AT_70A8_TO_CURRENT_LEVEL: EventScriptCommandName = (
    "summon_object_at_70A8_to_current_level"  # F4
)
REMOVE_FROM_LEVEL: EventScriptCommandName = "remove_from_level"  # F2
REMOVE_FROM_CURRENT_LEVEL: EventScriptCommandName = "remove_from_current_level"  # xx F9
REMOVE_OBJECT_AT_70A8_FROM_CURRENT_LEVEL: EventScriptCommandName = (
    "remove_object_at_70A8_from_current_level"  # F5
)
PAUSE_ACTION_SCRIPT: EventScriptCommandName = "pause_action_script"  # xx FA
RESUME_ACTION_SCRIPT: EventScriptCommandName = "resume_action_script"  # xx FB
ENABLE_TRIGGER: EventScriptCommandName = "enable_trigger"  # xx FC
ENABLE_TRIGGER_IN_LEVEL: EventScriptCommandName = "enable_trigger_in_level"  # F3
ENABLE_TRIGGER_AT_70A8: EventScriptCommandName = "enable_trigger_at_70A8"  # F6
DISABLE_TRIGGER: EventScriptCommandName = "disable_trigger"  # xx FD
DISABLE_TRIGGER_IN_LEVEL: EventScriptCommandName = "disable_trigger_in_level"  # F3
DISABLE_TRIGGER_AT_70A8: EventScriptCommandName = "disable_trigger_at_70A8"  # F7
STOP_EMBEDDED_ACTION_SCRIPT: EventScriptCommandName = (
    "stop_embedded_action_script"  # xx FE
)
RESET_COORDS: EventScriptCommandName = "reset_coords"  # xx FF
CREATE_PACKET_AT_NPC_COORDS: EventScriptCommandName = (
    "create_packet_at_npc_coords"  # 3E
)
CREATE_PACKET_AT_7010: EventScriptCommandName = "create_packet_at_7010"  # 3F
CREATE_PACKET_AT_7010_WITH_EVENT: EventScriptCommandName = (
    "create_packet_at_7010_with_event"  # FD 3E
)
FREEZE_ALL_NPCS_UNTIL_RETURN: EventScriptCommandName = (
    "freeze_all_npcs_until_return"  # 30
)
FREEZE_CAMERA: EventScriptCommandName = "freeze_camera"  # FD 31
UNFREEZE_CAMERA: EventScriptCommandName = "unfreeze_camera"  # FD 30
JMP_IF_MARIO_ON_OBJECT: EventScriptCommandName = "jmp_if_mario_on_object"  # 39
JMP_FORK_MARIO_ON_OBJECT: EventScriptCommandName = "jmp_fork_mario_on_object"  # 42
JMP_IF_OBJECT_IN_AIR: EventScriptCommandName = "jmp_if_object_in_air"  # FD 3D
JMP_IF_OBJECT_IN_LEVEL: EventScriptCommandName = "jmp_if_object_in_level"  # F8
JMP_IF_PRESENT_IN_CURRENT_LEVEL: EventScriptCommandName = (
    "jmp_if_present_in_current_level"  # 32
)
JMP_IF_OBJECT_NOT_IN_LEVEL: EventScriptCommandName = "jmp_if_object_not_in_level"  # F8
JMP_IF_OBJECT_TRIGGER_ENABLED: EventScriptCommandName = (
    "jmp_if_object_trigger_enabled"  # FD F0
)
JMP_IF_OBJECT_TRIGGER_DISABLED: EventScriptCommandName = (
    "jmp_if_object_trigger_disabled"  # FD F0
)
JMP_IF_OBJECT_UNDERWATER: EventScriptCommandName = "jmp_if_object_underwater"  # FD 34
JMP_IF_OBJECTS_ACTION_SCRIPT_RUNNING: EventScriptCommandName = (
    "jmp_if_objects_action_script_running"  # FD 33
)
JMP_IF_OBJECTS_LESS_THAN_XY_STEPS_APART: EventScriptCommandName = (
    "jmp_if_objects_less_than_xy_steps_apart"  # 3A
)
JMP_IF_OBJECTS_LESS_THAN_XY_STEPS_APART_SAME_Z_COORD: EventScriptCommandName = (
    "jmp_if_objects_less_than_xy_steps_apart_same_z_coord"  # 3B
)
REACTIVATE_TRIGGER_IF_MARIO_ON_TOP_OF_OBJECT: EventScriptCommandName = (
    "reactivate_trigger_if_mario_on_top_of_object"  # 5D
)
SET_7000_TO_OBJECT_COORD: EventScriptCommandName = (
    "set_7000_to_object_coord"  # C4, C5, C6
)
SET_7010_TO_OBJECT_XYZ: EventScriptCommandName = "set_7010_to_object_xyz"  # C7
SET_7016_TO_OBJECT_XYZ: EventScriptCommandName = "set_7016_to_object_xyz"  # C8
SET_OBJECT_MEMORY_TO: EventScriptCommandName = "set_object_memory_to"  # D6
UNFREEZE_ALL_NPCS: EventScriptCommandName = "unfreeze_all_npcs"  # 31

# controls

ENABLE_CONTROLS: EventScriptCommandName = "enable_controls"  # 35
ENABLE_CONTROLS_UNTIL_RETURN: EventScriptCommandName = (
    "enable_controls_until_return"  # 34
)
SET_7000_TO_PRESSED_BUTTON: EventScriptCommandName = "set_7000_to_pressed_button"  # CA
SET_7000_TO_TAPPED_BUTTON: EventScriptCommandName = "set_7000_to_tapped_button"  # CB

# inventory / party

ADD_COINS: EventScriptCommandName = "add_coins"  # 52, FD 52
DEC_COINS: EventScriptCommandName = "dec_coins"  # FD 53
ADD_FROG_COINS: EventScriptCommandName = "add_frog_coins"  # 53, FD 54
DEC_7000_FROM_FROG_COINS: EventScriptCommandName = "dec_7000_from_frog_coins"  # FD 55
ADD_7000_TO_CURRENT_FP: EventScriptCommandName = "add_7000_to_current_FP"  # FD 56
DEC_7000_FROM_CURRENT_FP: EventScriptCommandName = "dec_7000_from_current_FP"  # 57
ADD_7000_TO_MAX_FP: EventScriptCommandName = "add_7000_to_max_FP"  # FD 57
DEC_7000_FROM_CURRENT_HP: EventScriptCommandName = "dec_7000_from_current_HP"  # 56
EQUIP_ITEM_TO_CHARACTER: EventScriptCommandName = "equip_item_to_character"  # 54
INC_EXP_BY_PACKET: EventScriptCommandName = "inc_exp_by_packet"  # FD 48
JOIN_PARTY: EventScriptCommandName = "join_party"  # 36
LEAVE_PARTY: EventScriptCommandName = "leave_party"  # 36
PUT_70A7_EQUIPS_INVENTORY: EventScriptCommandName = "put_70A7_equips_inventory"  # FD 51
PUT_INVENTORY: EventScriptCommandName = "put_inventory"  # 50
REMOVE_ONE_FROM_INVENTORY: EventScriptCommandName = "remove_one_from_inventory"  # 51
RESTORE_ALL_FP: EventScriptCommandName = "restore_all_fp"  # FD 5C
RESTORE_ALL_HP: EventScriptCommandName = "restore_all_hp"  # FD 5B
SET_EXPERIENCE_PACKET_7000: EventScriptCommandName = (
    "set_experience_packet_7000"  # FD 64
)
SET_7000_TO_MEMBER_IN_SLOT: EventScriptCommandName = "set_7000_to_member_in_slot"  # 38
SET_7000_TO_PARTY_CAPACITY: EventScriptCommandName = "set_7000_to_party_capacity"  # 37
STORE_7000_ITEM_QUANTITY_TO_70A7: EventScriptCommandName = (
    "store_7000_item_quantity_to_70A7"  # FD 5E
)
STORE_CHARACTER_EQUIPMENT_7000: EventScriptCommandName = (
    "store_character_equipment_7000"  # FD 5D
)
STORE_CURRENT_FP_7000: EventScriptCommandName = "store_current_FP_7000"  # 58
STORE_EMPTY_INVENTORY_SLOT_COUNT_7000: EventScriptCommandName = (
    "store_empty_inventory_slot_count_7000"  # 55
)
STORE_COIN_AMOUNT_7000: EventScriptCommandName = "store_coin_amount_7000"  # FD 58
STORE_ITEM_AMOUNT_7000: EventScriptCommandName = "store_item_amount_7000"  # FD 59
STORE_FROG_COIN_AMOUNT_7000: EventScriptCommandName = (
    "store_frog_coin_amount_7000"  # FD 5A
)

# yourself

JMP_IF_MARIO_IN_AIR: EventScriptCommandName = "jmp_if_mario_in_air"  # 3D
MARIO_GLOWS: EventScriptCommandName = "mario_glows"  # FD F9

# palettes & screen effects

PALETTE_SET: EventScriptCommandName = "palette_set"  # 8A
PALETTE_SET_MORPHS: EventScriptCommandName = "palette_set_morphs"  # 0x89
PAUSE_SCRIPT_UNTIL_EFFECT_DONE: EventScriptCommandName = (
    "pause_script_until_effect_done"  # 7F
)
PIXELATE_LAYERS: EventScriptCommandName = "pixelate_layers"  # 84
PRIORITY_SET: EventScriptCommandName = "priority_set"  # 81
RESET_PRIORITY_SET: EventScriptCommandName = "reset_priority_set"  # 82
SCREEN_FLASHES_WITH_COLOUR: EventScriptCommandName = "screen_flashes_with_colour"  # 83
TINT_LAYERS: EventScriptCommandName = "tint_layers"  # 80

# screen transitions

CIRCLE_MASK_EXPAND_FROM_SCREEN_CENTER: EventScriptCommandName = (
    "circle_mask_expand_from_screen_center"  # 7C
)
CIRCLE_MASK_NONSTATIC: EventScriptCommandName = "circle_mask_nonstatic"  # 87
CIRCLE_MASK_SHRINK_TO_SCREEN_CENTER: EventScriptCommandName = (
    "circle_mask_shrink_to_screen_center"  # 7D
)
CIRCLE_MASK_STATIC: EventScriptCommandName = "circle_mask_static"  # 8F
STAR_MASK_EXPAND_FROM_SCREEN_CENTER: EventScriptCommandName = (
    "star_mask_expand_from_screen_center"  # 7A
)
STAR_MASK_SHRINK_TO_SCREEN_CENTER: EventScriptCommandName = (
    "star_mask_shrink_to_screen_center"  # 7B
)
FADE_IN_FROM_BLACK_SYNC: EventScriptCommandName = "fade_in_from_black_sync"  # 70
FADE_IN_FROM_BLACK_ASYNC: EventScriptCommandName = "fade_in_from_black_async"  # 71
FADE_IN_FROM_BLACK_SYNC_DURATION: EventScriptCommandName = (
    "fade_in_from_black_sync_duration"  # 72
)
FADE_IN_FROM_BLACK_ASYNC_DURATION: EventScriptCommandName = (
    "fade_in_from_black_async_duration"  # 73
)
FADE_IN_FROM_COLOUR_DURATION: EventScriptCommandName = (
    "fade_in_from_colour_duration"  # 78
)
FADE_OUT_TO_BLACK_SYNC: EventScriptCommandName = "fade_out_to_black_sync"  # 74
FADE_OUT_TO_BLACK_ASYNC: EventScriptCommandName = "fade_out_to_black_async"  # 71
FADE_OUT_TO_BLACK_SYNC_DURATION: EventScriptCommandName = (
    "fade_out_to_black_sync_duration"  # 76
)
FADE_OUT_TO_BLACK_ASYNC_DURATION: EventScriptCommandName = (
    "fade_out_to_black_async_duration"  # 77
)
FADE_OUT_TO_COLOUR_DURATION: EventScriptCommandName = (
    "fade_out_to_colour_duration"  # 79
)
INITIATE_BATTLE_MASK: EventScriptCommandName = "initiate_battle_mask"  # 7E

# music

ADJUST_MUSIC_TEMPO: EventScriptCommandName = "adjust_music_tempo"  # 97
DEACTIVATE_SOUND_CHANNELS: EventScriptCommandName = "deactivate_sound_channels"  # FD 94
FADE_IN_MUSIC: EventScriptCommandName = "fade_in_music"  # 92
FADE_OUT_MUSIC: EventScriptCommandName = "fade_out_music"  # 93
FADE_OUT_MUSIC_FDA3: EventScriptCommandName = "fade_out_music_FDA3"  # FD A3
FADE_OUT_MUSIC_TO_VOLUME: EventScriptCommandName = "fade_out_music_to_volume"  # 95
FADE_OUT_SOUND_TO_VOLUME: EventScriptCommandName = "fade_out_sound_to_volume"  # 9E
JMP_IF_AUDIO_MEMORY_AT_LEAST: EventScriptCommandName = (
    "jmp_if_audio_memory_at_least"  # FD 96
)
JMP_IF_AUDIO_MEMORY_EQUALS: EventScriptCommandName = (
    "jmp_if_audio_memory_equals"  # FD 97
)
PLAY_MUSIC: EventScriptCommandName = "play_music"  # FD 9E
PLAY_MUSIC_CURRENT_VOLUME: EventScriptCommandName = "play_music_current_volume"  # 90
PLAY_MUSIC_DEFAULT_VOLUME: EventScriptCommandName = "play_music_default_volume"  # 91
PLAY_SOUND: EventScriptCommandName = "play_sound"  # 9C, FD 9C
PLAY_SOUND_BALANCE: EventScriptCommandName = "play_sound_balance"  # 9D
PLAY_SOUND_BALANCE_FD9D: EventScriptCommandName = "play_sound_balance_FD9D"  # FD 9D
SLOW_DOWN_MUSIC: EventScriptCommandName = "slow_down_music"  # FD A4
SPEED_UP_MUSIC_TO_NORMAL: EventScriptCommandName = "speed_up_music_to_normal"  # FD A5
STOP_MUSIC: EventScriptCommandName = "stop_music"  # 94
STOP_MUSIC_FD9F: EventScriptCommandName = "stop_music_FD9F"  # FD 9F
STOP_MUSIC_FDA0: EventScriptCommandName = "stop_music_FDA0"  # FD A0
STOP_MUSIC_FDA1: EventScriptCommandName = "stop_music_FDA1"  # FD A1
STOP_MUSIC_FDA2: EventScriptCommandName = "stop_music_FDA2"  # FD A2
STOP_MUSIC_FDA6: EventScriptCommandName = "stop_music_FDA6"  # FD A6
STOP_SOUND: EventScriptCommandName = "stop_sound"  # 9B

# dialogs

APPEND_TO_DIALOG_AT_7000: EventScriptCommandName = "append_to_dialog_at_7000"  # 63
CLOSE_DIALOG: EventScriptCommandName = "close_dialog"  # 64
JMP_IF_DIALOG_OPTION_B: EventScriptCommandName = "jmp_if_dialog_option_b"  # 66
JMP_IF_DIALOG_OPTION_B_OR_C: EventScriptCommandName = (
    "jmp_if_dialog_option_b_or_c"  # 67
)
PAUSE_SCRIPT_RESUME_ON_NEXT_DIALOG_PAGE_A: EventScriptCommandName = (
    "pause_script_resume_on_next_dialog_page_a"  # FD 60
)
PAUSE_SCRIPT_RESUME_ON_NEXT_DIALOG_PAGE_B: EventScriptCommandName = (
    "pause_script_resume_on_next_dialog_page_b"  # FD 61
)
RUN_DIALOG: EventScriptCommandName = "run_dialog"  # 60, 61
RUN_DIALOG_DURATION: EventScriptCommandName = "run_dialog_duration"  # 62
UNSYNC_DIALOG: EventScriptCommandName = "unsync_dialog"  # 65

# levels

ENTER_AREA: EventScriptCommandName = "enter_area"  # 68
APPLY_TILE_MOD: EventScriptCommandName = "apply_tile_mod"  # 6A
APPLY_SOLIDITY_MOD: EventScriptCommandName = "apply_solidity_mod"  # 6B
OPEN_LOCATION: EventScriptCommandName = "open_location"  # 4B
SET_7000_TO_CURRENT_LEVEL: EventScriptCommandName = "set_7000_to_current_level"  # C3

# scenes

DISPLAY_INTRO_TITLE: EventScriptCommandName = "display_intro_title"  # FD 66
EXOR_CRASHES_INTO_KEEP: EventScriptCommandName = "exor_crashes_into_keep"  # FD F8
OPEN_MENU_OR_RUN_EVENT_SEQUENCE: EventScriptCommandName = (
    "open_menu_or_run_event_sequence"  # 4F
)
OPEN_SAVE_MENU: EventScriptCommandName = "open_save_menu"  # FD 4A
OPEN_SHOP: EventScriptCommandName = "open_shop"  # 4C
PAUSE_SCRIPT_IF_MENU_OPEN: EventScriptCommandName = "pause_script_if_menu_open"  # 5B
RESET_AND_CHOOSE_GAME: EventScriptCommandName = "reset_and_choose_game"  # FB
RESET_GAME: EventScriptCommandName = "reset_game"  # FC
RUN_ENDING_CREDITS: EventScriptCommandName = "run_ending_credits"  # FD 67
RUN_EVENT_SEQUENCE: EventScriptCommandName = "run_event_sequence"  # 4E
RUN_LEVELUP_BONUS_SEQUENCE: EventScriptCommandName = (
    "run_levelup_bonus_sequence"  # FD 65
)
RUN_MENU_TUTORIAL: EventScriptCommandName = "run_menu_tutorial"  # FD 4C
RUN_MOLEVILLE_MOUNTAIN_INTRO_SEQUENCE: EventScriptCommandName = (
    "run_moleville_mountain_intro_sequence"  # FD 4F
)
RUN_MOLEVILLE_MOUNTAIN_SEQUENCE: EventScriptCommandName = (
    "run_moleville_mountain_sequence"  # FD 4E
)
RUN_STAR_PIECE_SEQUENCE: EventScriptCommandName = "run_star_piece_sequence"  # FD 4D
START_BATTLE: EventScriptCommandName = "start_battle"  # 4A
START_BATTLE_700E: EventScriptCommandName = "start_battle_700E"  # 49
