from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data.eventtables import RadialDirections, AreaObjects, NPCPackets, Sounds, Coords, CoordUnits, Rooms
script = [
    {
        "identifier": 'ACTION_190_pause_0',
        "command": 'pause',
        "args": [1]
    },
    {
        "identifier": 'ACTION_190_face_southeast_1',
        "command": 'face_southeast'
    },
    {
        "identifier": 'ACTION_190_fixed_f_coord_on_2',
        "command": 'fixed_f_coord_on'
    },
    {
        "identifier": 'ACTION_190_set_animation_speed_3',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
    },
    {
        "identifier": 'ACTION_190_jmp_if_bit_clear_4',
        "command": 'jmp_if_bit_clear',
        "args": [0x7043, 3, 'ACTION_190_pause_0']
    },
    {
        "identifier": 'ACTION_190_jmp_if_bit_clear_5',
        "command": 'jmp_if_bit_clear',
        "args": [0x7044, 6, 'ACTION_190_pause_0']
    },
    {
        "identifier": 'ACTION_190_set_700C_to_object_coord_6',
        "command": 'set_700C_to_object_coord',
        "args": [AreaObjects.MARIO, Coords.F, []]
    },
    {
        "identifier": 'ACTION_190_jmp_if_700C_equals_short_7',
        "command": 'jmp_if_700C_equals_short',
        "args": [7, 'ACTION_190_jmp_if_var_equals_byte_18']
    },
    {
        "identifier": 'ACTION_190_jmp_if_700C_equals_short_8',
        "command": 'jmp_if_700C_equals_short',
        "args": [0, 'ACTION_190_jmp_if_var_equals_byte_18']
    },
    {
        "identifier": 'ACTION_190_jmp_if_700C_equals_short_9',
        "command": 'jmp_if_700C_equals_short',
        "args": [1, 'ACTION_190_jmp_if_var_equals_byte_18']
    },
    {
        "identifier": 'ACTION_190_jmp_if_700C_equals_short_10',
        "command": 'jmp_if_700C_equals_short',
        "args": [2, 'ACTION_190_jmp_if_var_equals_byte_18']
    },
    {
        "identifier": 'ACTION_190_jmp_if_var_equals_byte_11',
        "command": 'jmp_if_var_equals_byte',
        "args": [0x70c4, 0, 'ACTION_190_pause_0']
    },
    {
        "identifier": 'ACTION_190_dec_12',
        "command": 'dec',
        "args": [0x70c4]
    },
    {
        "identifier": 'ACTION_190_set_sprite_sequence_13',
        "command": 'set_sprite_sequence',
        "args": [1, 0, [_0x08Flags.LOOPING_OFF, _0x08Flags.MIRROR_SPRITE]]
    },
    {
        "identifier": 'ACTION_190_shift_northwest_pixels_14',
        "command": 'shift_northwest_pixels',
        "args": [5]
    },
    {
        "identifier": 'ACTION_190_clear_bit_15',
        "command": 'clear_bit',
        "args": [0x7043, 3]
    },
    {
        "identifier": 'ACTION_190_clear_bit_16',
        "command": 'clear_bit',
        "args": [0x7044, 6]
    },
    {
        "identifier": 'ACTION_190_jmp_17',
        "command": 'jmp',
        "args": ['ACTION_190_pause_0']
    },
    {
        "identifier": 'ACTION_190_jmp_if_var_equals_byte_18',
        "command": 'jmp_if_var_equals_byte',
        "args": [0x70c4, 16, 'ACTION_190_pause_0']
    },
    {
        "identifier": 'ACTION_190_inc_19',
        "command": 'inc',
        "args": [0x70c4]
    },
    {
        "identifier": 'ACTION_190_set_sprite_sequence_20',
        "command": 'set_sprite_sequence',
        "args": [2, 0, [_0x08Flags.LOOPING_OFF, _0x08Flags.MIRROR_SPRITE]]
    },
    {
        "identifier": 'ACTION_190_shift_southeast_pixels_21',
        "command": 'shift_southeast_pixels',
        "args": [5]
    },
    {
        "identifier": 'ACTION_190_clear_bit_22',
        "command": 'clear_bit',
        "args": [0x7043, 3]
    },
    {
        "identifier": 'ACTION_190_clear_bit_23',
        "command": 'clear_bit',
        "args": [0x7044, 6]
    },
    {
        "identifier": 'ACTION_190_jmp_24',
        "command": 'jmp',
        "args": ['ACTION_190_pause_0']
    }
]
