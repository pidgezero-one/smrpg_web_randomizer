from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data.eventtables import RadialDirections, AreaObjects, NPCPackets, Sounds, Coords, CoordUnits, Rooms
script = [
    {
        "identifier": 'ACTION_547_set_animation_speed_0',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.SLOW, [_0x10Flags.WALKING]]
    },
    {
        "identifier": 'ACTION_547_sequence_looping_on_1',
        "command": 'sequence_looping_on'
    },
    {
        "identifier": 'ACTION_547_set_700C_to_pressed_button_2',
        "command": 'set_700C_to_pressed_button'
    },
    {
        "identifier": 'ACTION_547_add_3',
        "command": 'add',
        "args": [0x700c, 65517]
    },
    {
        "identifier": 'ACTION_547_load_mem_4',
        "command": 'load_mem',
        "args": [0x700c]
    },
    {
        "identifier": 'ACTION_547_pause_5',
        "command": 'pause',
        "args": [1]
    },
    {
        "identifier": 'ACTION_547_end_loop_6',
        "command": 'end_loop'
    },
    {
        "identifier": 'ACTION_547_shift_southeast_pixels_7',
        "command": 'shift_southeast_pixels',
        "args": [37]
    },
    {
        "identifier": 'ACTION_547_jmp_if_random_above_128_8',
        "command": 'jmp_if_random_above_128',
        "args": ['ACTION_547_shift_southeast_pixels_30']
    },
    {
        "identifier": 'ACTION_547_set_sprite_sequence_9',
        "command": 'set_sprite_sequence',
        "args": [8, 0, [_0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
    },
    {
        "identifier": 'ACTION_547_jmp_if_var_equals_byte_10',
        "command": 'jmp_if_var_equals_byte',
        "args": [0x70bb, 0, 'ACTION_547_pause_16']
    },
    {
        "identifier": 'ACTION_547_start_loop_n_times_11',
        "command": 'start_loop_n_times',
        "args": [4]
    },
    {
        "identifier": 'ACTION_547_db_12',
        "command": 'db',
        "args": [0x3b, 0x00, 0x80, 0x03, 0x7f, 0x67]
    },
    {
        "identifier": 'ACTION_547_pause_13',
        "command": 'pause',
        "args": [16]
    },
    {
        "identifier": 'ACTION_547_end_loop_14',
        "command": 'end_loop'
    },
    {
        "identifier": 'ACTION_547_jmp_15',
        "command": 'jmp',
        "args": ['ACTION_547_reset_properties_17']
    },
    {
        "identifier": 'ACTION_547_pause_16',
        "command": 'pause',
        "args": [80]
    },
    {
        "identifier": 'ACTION_547_reset_properties_17',
        "command": 'reset_properties'
    },
    {
        "identifier": 'ACTION_547_jmp_if_random_above_128_18',
        "command": 'jmp_if_random_above_128',
        "args": ['ACTION_547_shift_southeast_pixels_30']
    },
    {
        "identifier": 'ACTION_547_face_southwest_19',
        "command": 'face_southwest'
    },
    {
        "identifier": 'ACTION_547_pause_20',
        "command": 'pause',
        "args": [8]
    },
    {
        "identifier": 'ACTION_547_face_northwest_21',
        "command": 'face_northwest'
    },
    {
        "identifier": 'ACTION_547_pause_22',
        "command": 'pause',
        "args": [8]
    },
    {
        "identifier": 'ACTION_547_shift_northwest_pixels_23',
        "command": 'shift_northwest_pixels',
        "args": [37]
    },
    {
        "identifier": 'ACTION_547_pause_24',
        "command": 'pause',
        "args": [8]
    },
    {
        "identifier": 'ACTION_547_face_northeast_25',
        "command": 'face_northeast'
    },
    {
        "identifier": 'ACTION_547_pause_26',
        "command": 'pause',
        "args": [8]
    },
    {
        "identifier": 'ACTION_547_face_southeast_27',
        "command": 'face_southeast'
    },
    {
        "identifier": 'ACTION_547_pause_28',
        "command": 'pause',
        "args": [16]
    },
    {
        "identifier": 'ACTION_547_jmp_29',
        "command": 'jmp',
        "args": ['ACTION_547_shift_southeast_pixels_7']
    },
    {
        "identifier": 'ACTION_547_shift_southeast_pixels_30',
        "command": 'shift_southeast_pixels',
        "args": [37]
    },
    {
        "identifier": 'ACTION_547_pause_31',
        "command": 'pause',
        "args": [8]
    },
    {
        "identifier": 'ACTION_547_face_southwest_32',
        "command": 'face_southwest'
    },
    {
        "identifier": 'ACTION_547_pause_33',
        "command": 'pause',
        "args": [8]
    },
    {
        "identifier": 'ACTION_547_face_northwest_34',
        "command": 'face_northwest'
    },
    {
        "identifier": 'ACTION_547_pause_35',
        "command": 'pause',
        "args": [16]
    },
    {
        "identifier": 'ACTION_547_jmp_36',
        "command": 'jmp',
        "args": ['ACTION_548_shift_northwest_pixels_7']
    }
]
