from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data.eventtables import RadialDirections, AreaObjects, NPCPackets, Sounds, Coords, CoordUnits, Rooms
script = [
    {
        "identifier": 'ACTION_608_shadow_off_0',
        "command": 'shadow_off'
    },
    {
        "identifier": 'ACTION_608_set_vram_priority_1',
        "command": 'set_vram_priority',
        "args": [VramPriority.PRIORITY_3]
    },
    {
        "identifier": 'ACTION_608_set_priority_2',
        "command": 'set_priority',
        "args": [3]
    },
    {
        "identifier": 'ACTION_608_set_object_memory_bits_3',
        "command": 'set_object_memory_bits',
        "args": [0x0e, [0, 2]]
    },
    {
        "identifier": 'ACTION_608_face_mario_4',
        "command": 'face_mario'
    },
    {
        "identifier": 'ACTION_608_pause_5',
        "command": 'pause',
        "args": [1]
    },
    {
        "identifier": 'ACTION_608_set_700C_to_pressed_button_6',
        "command": 'set_700C_to_pressed_button'
    },
    {
        "identifier": 'ACTION_608_add_7',
        "command": 'add',
        "args": [0x700c, 65535]
    },
    {
        "identifier": 'ACTION_608_jmp_if_mem_704x_at_700C_bit_clear_8',
        "command": 'jmp_if_mem_704x_at_700C_bit_clear',
        "args": ['ACTION_608_face_mario_4']
    },
    {
        "identifier": 'ACTION_608_shadow_on_9',
        "command": 'shadow_on'
    },
    {
        "identifier": 'ACTION_608_set_object_memory_bits_10',
        "command": 'set_object_memory_bits',
        "args": [0x0e, []]
    },
    {
        "identifier": 'ACTION_608_jump_to_height_11',
        "command": 'jump_to_height',
        "args": [108]
    },
    {
        "identifier": 'ACTION_608_set_700C_to_object_coord_12',
        "command": 'set_700C_to_object_coord',
        "args": [AreaObjects.DUMMY_0X07, Coords.F, []]
    },
    {
        "identifier": 'ACTION_608_mem_compare_val_13',
        "command": 'mem_compare_val',
        "args": [3]
    },
    {
        "identifier": 'ACTION_608_jmp_if_comparison_result_is_greater_or_equal_14',
        "command": 'jmp_if_comparison_result_is_greater_or_equal',
        "args": ['ACTION_608_set_sprite_sequence_19']
    },
    {
        "identifier": 'ACTION_608_mem_compare_val_15',
        "command": 'mem_compare_val',
        "args": [7]
    },
    {
        "identifier": 'ACTION_608_jmp_if_comparison_result_is_lesser_16',
        "command": 'jmp_if_comparison_result_is_lesser',
        "args": ['ACTION_608_set_sprite_sequence_19']
    },
    {
        "identifier": 'ACTION_608_set_sprite_sequence_17',
        "command": 'set_sprite_sequence',
        "args": [4, 0, [_0x08Flags.LOOPING_OFF, _0x08Flags.MIRROR_SPRITE]]
    },
    {
        "identifier": 'ACTION_608_jmp_18',
        "command": 'jmp',
        "args": ['ACTION_608_shift_f_direction_steps_20']
    },
    {
        "identifier": 'ACTION_608_set_sprite_sequence_19',
        "command": 'set_sprite_sequence',
        "args": [4, 0, [_0x08Flags.LOOPING_OFF]]
    },
    {
        "identifier": 'ACTION_608_shift_f_direction_steps_20',
        "command": 'shift_f_direction_steps',
        "args": [2]
    },
    {
        "identifier": 'ACTION_608_set_vram_priority_21',
        "command": 'set_vram_priority',
        "args": [VramPriority.NORMAL]
    },
    {
        "identifier": 'ACTION_608_object_memory_modify_bits_22',
        "command": 'object_memory_modify_bits',
        "args": [0x09, [5], [4, 6]]
    },
    {
        "identifier": 'ACTION_608_play_sound_23',
        "command": 'play_sound',
        "args": [Sounds._079_YELP_IN_DISTANCE, 4]
    },
    {
        "identifier": 'ACTION_608_pause_24',
        "command": 'pause',
        "args": [30]
    },
    {
        "identifier": 'ACTION_608_reset_properties_25',
        "command": 'reset_properties'
    },
    {
        "identifier": 'ACTION_608_set_700C_to_pressed_button_26',
        "command": 'set_700C_to_pressed_button'
    },
    {
        "identifier": 'ACTION_608_set_short_27',
        "command": 'set_short',
        "args": [0x7024, 0x0005]
    },
    {
        "identifier": 'ACTION_608_dec_short_mem_28',
        "command": 'dec_short_mem',
        "args": [0x700c, 0x7024]
    },
    {
        "identifier": 'ACTION_608_set_70A0_short_mem_to_700C_29',
        "command": 'set_70A0_short_mem_to_700C',
        "args": [0x70a9]
    },
    {
        "identifier": 'ACTION_608_face_southwest_7D_30',
        "command": 'face_southwest_7D',
        "args": [0x11]
    },
    {
        "identifier": 'ACTION_608_walk_1_step_f_direction_31',
        "command": 'walk_1_step_f_direction'
    },
    {
        "identifier": 'ACTION_608_jump_to_height_32',
        "command": 'jump_to_height',
        "args": [56]
    },
    {
        "identifier": 'ACTION_608_pause_33',
        "command": 'pause',
        "args": [25]
    },
    {
        "identifier": 'ACTION_608_jmp_if_random_above_66_34',
        "command": 'jmp_if_random_above_66',
        "args": [0x6ef7, 'ACTION_608_set_700C_to_pressed_button_26']
    },
    {
        "identifier": 'ACTION_608_turn_random_direction_35',
        "command": 'turn_random_direction'
    },
    {
        "identifier": 'ACTION_608_walk_1_step_f_direction_36',
        "command": 'walk_1_step_f_direction'
    },
    {
        "identifier": 'ACTION_608_jmp_37',
        "command": 'jmp',
        "args": ['ACTION_608_set_700C_to_pressed_button_26']
    }
]
