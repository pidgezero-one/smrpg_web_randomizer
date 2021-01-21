from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data.eventtables import RadialDirections, AreaObjects, NPCPackets, Sounds, Coords, CoordUnits, Rooms
script = [
    {
        "identifier": 'ACTION_671_set_700C_to_object_coord_0',
        "command": 'set_700C_to_object_coord',
        "args": [AreaObjects.MARIO, Coords.F]
    },
    {
        "identifier": 'ACTION_671_set_short_mem_1',
        "command": 'set_short_mem',
        "args": [0x7038, 0x700c]
    },
    {
        "identifier": 'ACTION_671_jmp_if_700C_any_bits_set_2',
        "command": 'jmp_if_700C_any_bits_set',
        "args": [[0], 'ACTION_671_jmp_if_bit_set_4']
    },
    {
        "identifier": 'ACTION_671_set_bit_3',
        "command": 'set_bit',
        "args": [0x7049, 7]
    },
    {
        "identifier": 'ACTION_671_jmp_if_bit_set_4',
        "command": 'jmp_if_bit_set',
        "args": [0x7049, 2, 'ACTION_671_jmp_if_bit_set_6']
    },
    {
        "identifier": 'ACTION_671_set_animation_speed_5',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.SEQUENCE]]
    },
    {
        "identifier": 'ACTION_671_jmp_if_bit_set_6',
        "command": 'jmp_if_bit_set',
        "args": [0x7049, 7, 'ACTION_671_set_short_mem_11']
    },
    {
        "identifier": 'ACTION_671_jmp_if_var_equals_short_7',
        "command": 'jmp_if_var_equals_short',
        "args": [0x7038, 1, 'ACTION_671_set_sprite_sequence_19']
    },
    {
        "identifier": 'ACTION_671_jmp_if_var_equals_short_8',
        "command": 'jmp_if_var_equals_short',
        "args": [0x7038, 3, 'ACTION_671_set_sprite_sequence_21']
    },
    {
        "identifier": 'ACTION_671_jmp_if_var_equals_short_9',
        "command": 'jmp_if_var_equals_short',
        "args": [0x7038, 5, 'ACTION_671_set_sprite_sequence_23']
    },
    {
        "identifier": 'ACTION_671_jmp_if_var_equals_short_10',
        "command": 'jmp_if_var_equals_short',
        "args": [0x7038, 7, 'ACTION_671_set_sprite_sequence_25']
    },
    {
        "identifier": 'ACTION_671_set_short_mem_11',
        "command": 'set_short_mem',
        "args": [0x700c, 0x70ae]
    },
    {
        "identifier": 'ACTION_671_set_short_mem_12',
        "command": 'set_short_mem',
        "args": [0x70ab, 0x700c]
    },
    {
        "identifier": 'ACTION_671_db_13',
        "command": 'db',
        "args": [0xfd, 0x24, 0x00, 0x13]
    },
    {
        "identifier": 'ACTION_671_mem_700C_and_const_14',
        "command": 'mem_700C_and_const',
        "args": [0x00c0]
    },
    {
        "identifier": 'ACTION_671_jmp_if_var_equals_short_15',
        "command": 'jmp_if_var_equals_short',
        "args": [0x700c, 0, 'ACTION_671_set_sprite_sequence_19']
    },
    {
        "identifier": 'ACTION_671_jmp_if_var_equals_short_16',
        "command": 'jmp_if_var_equals_short',
        "args": [0x700c, 64, 'ACTION_671_set_sprite_sequence_21']
    },
    {
        "identifier": 'ACTION_671_jmp_if_var_equals_short_17',
        "command": 'jmp_if_var_equals_short',
        "args": [0x700c, 128, 'ACTION_671_set_sprite_sequence_23']
    },
    {
        "identifier": 'ACTION_671_jmp_if_var_equals_short_18',
        "command": 'jmp_if_var_equals_short',
        "args": [0x700c, 192, 'ACTION_671_set_sprite_sequence_25']
    },
    {
        "identifier": 'ACTION_671_set_sprite_sequence_19',
        "command": 'set_sprite_sequence',
        "args": [8, inc_sprite=0, flags=[_0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
    },
    {
        "identifier": 'ACTION_671_jmp_20',
        "command": 'jmp',
        "args": ['ACTION_671_set_bit_26']
    },
    {
        "identifier": 'ACTION_671_set_sprite_sequence_21',
        "command": 'set_sprite_sequence',
        "args": [8, inc_sprite=0, flags=[_0x08Flags.READ_AS_SEQUENCE]]
    },
    {
        "identifier": 'ACTION_671_jmp_22',
        "command": 'jmp',
        "args": ['ACTION_671_set_bit_26']
    },
    {
        "identifier": 'ACTION_671_set_sprite_sequence_23',
        "command": 'set_sprite_sequence',
        "args": [9, inc_sprite=0, flags=[_0x08Flags.READ_AS_SEQUENCE]]
    },
    {
        "identifier": 'ACTION_671_jmp_24',
        "command": 'jmp',
        "args": ['ACTION_671_set_bit_26']
    },
    {
        "identifier": 'ACTION_671_set_sprite_sequence_25',
        "command": 'set_sprite_sequence',
        "args": [9, inc_sprite=0, flags=[_0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
    },
    {
        "identifier": 'ACTION_671_set_bit_26',
        "command": 'set_bit',
        "args": [0x7043, 6]
    },
    {
        "identifier": 'ACTION_671_jmp_if_bit_set_27',
        "command": 'jmp_if_bit_set',
        "args": [0x704a, 3, 'ACTION_671_pause_31']
    },
    {
        "identifier": 'ACTION_671_pause_28',
        "command": 'pause',
        "args": [4]
    },
    {
        "identifier": 'ACTION_671_stop_sound_29',
        "command": 'stop_sound'
    },
    {
        "identifier": 'ACTION_671_play_sound_30',
        "command": 'play_sound',
        "args": [Sounds._056_SHAKE_HEAD, 4]
    },
    {
        "identifier": 'ACTION_671_pause_31',
        "command": 'pause',
        "args": [32]
    },
    {
        "identifier": 'ACTION_671_stop_sound_32',
        "command": 'stop_sound'
    },
    {
        "identifier": 'ACTION_671_sequence_looping_off_33',
        "command": 'sequence_looping_off'
    },
    {
        "identifier": 'ACTION_671_set_animation_speed_34',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.NORMAL, [_0x10Flags.SEQUENCE]]
    },
    {
        "identifier": 'ACTION_671_reset_properties_35',
        "command": 'reset_properties'
    },
    {
        "identifier": 'ACTION_671_set_short_mem_36',
        "command": 'set_short_mem',
        "args": [0x700c, 0x7038]
    },
    {
        "identifier": 'ACTION_671_face_east_37',
        "command": 'face_east'
    },
    {
        "identifier": 'ACTION_671_clear_bit_38',
        "command": 'clear_bit',
        "args": [0x7049, 7]
    },
    {
        "identifier": 'ACTION_671_clear_bit_39',
        "command": 'clear_bit',
        "args": [0x7049, 2]
    },
    {
        "identifier": 'ACTION_671_clear_bit_40',
        "command": 'clear_bit',
        "args": [0x704a, 3]
    },
    {
        "identifier": 'ACTION_671_clear_bit_41',
        "command": 'clear_bit',
        "args": [0x7043, 6]
    },
    {
        "identifier": 'ACTION_671_ret_42',
        "command": 'ret'
    }
]
