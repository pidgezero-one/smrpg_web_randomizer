from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data.eventtables import RadialDirections, AreaObjects, NPCPackets, Sounds, Coords, CoordUnits, Rooms
script = [
    {
        "identifier": 'ACTION_277_visibility_off_0',
        "command": 'visibility_off'
    },
    {
        "identifier": 'ACTION_277_set_700C_to_current_level_1',
        "command": 'set_700C_to_current_level'
    },
    {
        "identifier": 'ACTION_277_jmp_if_700C_not_equals_short_2',
        "command": 'jmp_if_700C_not_equals_short',
        "args": [389, 'ACTION_277_clear_solidity_bits_4']
    },
    {
        "identifier": 'ACTION_277_set_priority_3',
        "command": 'set_priority',
        "args": [2]
    },
    {
        "identifier": 'ACTION_277_clear_solidity_bits_4',
        "command": 'clear_solidity_bits',
        "args": [[_0x0AFlags.BIT_4, _0x0AFlags.CANT_WALK_THROUGH]]
    },
    {
        "identifier": 'ACTION_277_object_memory_set_bit_5',
        "command": 'object_memory_set_bit',
        "args": [0x30, [4]]
    },
    {
        "identifier": 'ACTION_277_sequence_looping_on_6',
        "command": 'sequence_looping_on'
    },
    {
        "identifier": 'ACTION_277_set_animation_speed_7',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
    },
    {
        "identifier": 'ACTION_277_jmp_if_bit_set_8',
        "command": 'jmp_if_bit_set',
        "args": [0x7044, 3, 'ACTION_277_set_700C_to_pressed_button_10']
    },
    {
        "identifier": 'ACTION_277_db_9',
        "command": 'db',
        "args": [0x3b, 0x00, 0x00, 0x05, 0x64, 0x33]
    },
    {
        "identifier": 'ACTION_277_set_700C_to_pressed_button_10',
        "command": 'set_700C_to_pressed_button'
    },
    {
        "identifier": 'ACTION_277_mem_700C_and_const_11',
        "command": 'mem_700C_and_const',
        "args": [0x0007]
    },
    {
        "identifier": 'ACTION_277_jmp_if_700C_equals_short_12',
        "command": 'jmp_if_700C_equals_short',
        "args": [7, 'ACTION_277_pause_26']
    },
    {
        "identifier": 'ACTION_277_jmp_if_700C_equals_short_13',
        "command": 'jmp_if_700C_equals_short',
        "args": [6, 'ACTION_277_pause_25']
    },
    {
        "identifier": 'ACTION_277_jmp_if_700C_equals_short_14',
        "command": 'jmp_if_700C_equals_short',
        "args": [5, 'ACTION_277_pause_24']
    },
    {
        "identifier": 'ACTION_277_jmp_if_700C_equals_short_15',
        "command": 'jmp_if_700C_equals_short',
        "args": [4, 'ACTION_277_pause_23']
    },
    {
        "identifier": 'ACTION_277_jmp_if_700C_equals_short_16',
        "command": 'jmp_if_700C_equals_short',
        "args": [3, 'ACTION_277_pause_22']
    },
    {
        "identifier": 'ACTION_277_jmp_if_700C_equals_short_17',
        "command": 'jmp_if_700C_equals_short',
        "args": [2, 'ACTION_277_pause_21']
    },
    {
        "identifier": 'ACTION_277_jmp_if_700C_equals_short_18',
        "command": 'jmp_if_700C_equals_short',
        "args": [1, 'ACTION_277_pause_20']
    },
    {
        "identifier": 'ACTION_277_pause_19',
        "command": 'pause',
        "args": [5]
    },
    {
        "identifier": 'ACTION_277_pause_20',
        "command": 'pause',
        "args": [9]
    },
    {
        "identifier": 'ACTION_277_pause_21',
        "command": 'pause',
        "args": [13]
    },
    {
        "identifier": 'ACTION_277_pause_22',
        "command": 'pause',
        "args": [19]
    },
    {
        "identifier": 'ACTION_277_pause_23',
        "command": 'pause',
        "args": [23]
    },
    {
        "identifier": 'ACTION_277_pause_24',
        "command": 'pause',
        "args": [17]
    },
    {
        "identifier": 'ACTION_277_pause_25',
        "command": 'pause',
        "args": [11]
    },
    {
        "identifier": 'ACTION_277_pause_26',
        "command": 'pause',
        "args": [7]
    },
    {
        "identifier": 'ACTION_277_visibility_on_27',
        "command": 'visibility_on'
    },
    {
        "identifier": 'ACTION_277_set_solidity_bits_28',
        "command": 'set_solidity_bits',
        "args": [[_0x0AFlags.BIT_4, _0x0AFlags.CANT_WALK_THROUGH]]
    },
    {
        "identifier": 'ACTION_277_object_memory_clear_bit_29',
        "command": 'object_memory_clear_bit',
        "args": [0x30, [4]]
    },
    {
        "identifier": 'ACTION_277_play_sound_30',
        "command": 'play_sound',
        "args": [Sounds._084_SMOKED, 4]
    },
    {
        "identifier": 'ACTION_277_face_mario_31',
        "command": 'face_mario'
    },
    {
        "identifier": 'ACTION_277_set_700C_to_object_coord_32',
        "command": 'set_700C_to_object_coord',
        "args": [AreaObjects.DUMMY_0X07, Coords.F, []]
    },
    {
        "identifier": 'ACTION_277_jmp_if_700C_equals_short_33',
        "command": 'jmp_if_700C_equals_short',
        "args": [7, 'ACTION_277_set_sprite_sequence_37']
    },
    {
        "identifier": 'ACTION_277_jmp_if_700C_equals_short_34',
        "command": 'jmp_if_700C_equals_short',
        "args": [1, 'ACTION_277_set_sprite_sequence_37']
    },
    {
        "identifier": 'ACTION_277_set_sprite_sequence_35',
        "command": 'set_sprite_sequence',
        "args": [8, 0, [_0x08Flags.READ_AS_SEQUENCE]]
    },
    {
        "identifier": 'ACTION_277_jmp_36',
        "command": 'jmp',
        "args": ['ACTION_277_pause_38']
    },
    {
        "identifier": 'ACTION_277_set_sprite_sequence_37',
        "command": 'set_sprite_sequence',
        "args": [8, 0, [_0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
    },
    {
        "identifier": 'ACTION_277_pause_38',
        "command": 'pause',
        "args": [8]
    },
    {
        "identifier": 'ACTION_277_set_700C_to_object_coord_39',
        "command": 'set_700C_to_object_coord',
        "args": [AreaObjects.DUMMY_0X07, Coords.F, []]
    },
    {
        "identifier": 'ACTION_277_jmp_if_700C_equals_short_40',
        "command": 'jmp_if_700C_equals_short',
        "args": [7, 'ACTION_277_set_sprite_sequence_44']
    },
    {
        "identifier": 'ACTION_277_jmp_if_700C_equals_short_41',
        "command": 'jmp_if_700C_equals_short',
        "args": [1, 'ACTION_277_set_sprite_sequence_44']
    },
    {
        "identifier": 'ACTION_277_set_sprite_sequence_42',
        "command": 'set_sprite_sequence',
        "args": [9, 0, [_0x08Flags.READ_AS_SEQUENCE]]
    },
    {
        "identifier": 'ACTION_277_jmp_43',
        "command": 'jmp',
        "args": ['ACTION_277_jump_to_height_silent_45']
    },
    {
        "identifier": 'ACTION_277_set_sprite_sequence_44',
        "command": 'set_sprite_sequence',
        "args": [9, 0, [_0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
    },
    {
        "identifier": 'ACTION_277_jump_to_height_silent_45',
        "command": 'jump_to_height_silent',
        "args": [180]
    },
    {
        "identifier": 'ACTION_277_pause_46',
        "command": 'pause',
        "args": [28]
    },
    {
        "identifier": 'ACTION_277_reset_properties_47',
        "command": 'reset_properties'
    },
    {
        "identifier": 'ACTION_277_sequence_looping_on_48',
        "command": 'sequence_looping_on'
    },
    {
        "identifier": 'ACTION_277_pause_49',
        "command": 'pause',
        "args": [2]
    },
    {
        "identifier": 'ACTION_277_db_50',
        "command": 'db',
        "args": [0xfd, 0x3d, 0x07, 0x43, 0x33]
    },
    {
        "identifier": 'ACTION_277_set_700C_to_object_coord_51',
        "command": 'set_700C_to_object_coord',
        "args": [AreaObjects.DUMMY_0X07, Coords.F, []]
    },
    {
        "identifier": 'ACTION_277_jmp_if_700C_equals_short_52',
        "command": 'jmp_if_700C_equals_short',
        "args": [7, 'ACTION_277_set_sprite_sequence_56']
    },
    {
        "identifier": 'ACTION_277_jmp_if_700C_equals_short_53',
        "command": 'jmp_if_700C_equals_short',
        "args": [1, 'ACTION_277_set_sprite_sequence_56']
    },
    {
        "identifier": 'ACTION_277_set_sprite_sequence_54',
        "command": 'set_sprite_sequence',
        "args": [8, 0, [_0x08Flags.READ_AS_SEQUENCE]]
    },
    {
        "identifier": 'ACTION_277_jmp_55',
        "command": 'jmp',
        "args": ['ACTION_277_pause_57']
    },
    {
        "identifier": 'ACTION_277_set_sprite_sequence_56',
        "command": 'set_sprite_sequence',
        "args": [8, 0, [_0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
    },
    {
        "identifier": 'ACTION_277_pause_57',
        "command": 'pause',
        "args": [4]
    },
    {
        "identifier": 'ACTION_277_jmp_58',
        "command": 'jmp',
        "args": ['ACTION_277_visibility_off_0']
    },
    {
        "identifier": 'ACTION_277_reset_properties_59',
        "command": 'reset_properties'
    },
    {
        "identifier": 'ACTION_277_visibility_on_60',
        "command": 'visibility_on'
    },
    {
        "identifier": 'ACTION_277_set_solidity_bits_61',
        "command": 'set_solidity_bits',
        "args": [[_0x0AFlags.BIT_4, _0x0AFlags.CANT_WALK_THROUGH]]
    },
    {
        "identifier": 'ACTION_277_object_memory_clear_bit_62',
        "command": 'object_memory_clear_bit',
        "args": [0x30, [4]]
    },
    {
        "identifier": 'ACTION_277_db_63',
        "command": 'db',
        "args": [0x20, 0x07]
    },
    {
        "identifier": 'ACTION_277_embedded_animation_routine_64',
        "command": 'embedded_animation_routine',
        "args": [0x28, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x14, 0x00, 0x01, 0x00, 0x00, 0x80, 0x03, 0x80]
    },
    {
        "identifier": 'ACTION_277_db_65',
        "command": 'db',
        "args": [0x2f, 0x00, 0x08, 0x80, 0x00, 0x01, 0x00]
    },
    {
        "identifier": 'ACTION_277_face_mario_66',
        "command": 'face_mario'
    },
    {
        "identifier": 'ACTION_277_set_700C_to_object_coord_67',
        "command": 'set_700C_to_object_coord',
        "args": [AreaObjects.MARIO, Coords.Z, [], CoordUnits.PIXEL]
    },
    {
        "identifier": 'ACTION_277_add_68',
        "command": 'add',
        "args": [0x700c, 256]
    },
    {
        "identifier": 'ACTION_277_set_7000_short_mem_to_700C_69',
        "command": 'set_7000_short_mem_to_700C',
        "args": [0x7028]
    },
    {
        "identifier": 'ACTION_277_set_700C_to_object_coord_70',
        "command": 'set_700C_to_object_coord',
        "args": [AreaObjects.DUMMY_0X07, Coords.Z, [], CoordUnits.PIXEL]
    },
    {
        "identifier": 'ACTION_277_mem_compare_address_71',
        "command": 'mem_compare_address',
        "args": [0x7028]
    },
    {
        "identifier": 'ACTION_277_jmp_if_loaded_memory_is_0_72',
        "command": 'jmp_if_loaded_memory_is_0',
        "args": ['ACTION_277_pause_75']
    },
    {
        "identifier": 'ACTION_277_jmp_if_loaded_memory_is_below_0_73',
        "command": 'jmp_if_loaded_memory_is_below_0',
        "args": ['ACTION_277_shift_z_down_pixels_77']
    },
    {
        "identifier": 'ACTION_277_jmp_if_loaded_memory_is_above_or_equal_0_74',
        "command": 'jmp_if_loaded_memory_is_above_or_equal_0',
        "args": ['ACTION_277_shift_z_up_pixels_79']
    },
    {
        "identifier": 'ACTION_277_pause_75',
        "command": 'pause',
        "args": [1]
    },
    {
        "identifier": 'ACTION_277_jmp_76',
        "command": 'jmp',
        "args": ['ACTION_277_face_mario_66']
    },
    {
        "identifier": 'ACTION_277_shift_z_down_pixels_77',
        "command": 'shift_z_down_pixels',
        "args": [1]
    },
    {
        "identifier": 'ACTION_277_jmp_78',
        "command": 'jmp',
        "args": ['ACTION_277_face_mario_66']
    },
    {
        "identifier": 'ACTION_277_shift_z_up_pixels_79',
        "command": 'shift_z_up_pixels',
        "args": [1]
    },
    {
        "identifier": 'ACTION_277_jmp_80',
        "command": 'jmp',
        "args": ['ACTION_277_face_mario_66']
    }
]
