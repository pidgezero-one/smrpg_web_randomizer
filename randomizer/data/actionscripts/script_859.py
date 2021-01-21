from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data.eventtables import RadialDirections, AreaObjects, NPCPackets, Sounds, Coords, CoordUnits, Rooms
script = [
    {
        "identifier": 'ACTION_859_pause_0',
        "command": 'pause',
        "args": [1]
    },
    {
        "identifier": 'ACTION_859_face_southwest_1',
        "command": 'face_southwest'
    },
    {
        "identifier": 'ACTION_859_fixed_f_coord_on_2',
        "command": 'fixed_f_coord_on'
    },
    {
        "identifier": 'ACTION_859_set_animation_speed_3',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
    },
    {
        "identifier": 'ACTION_859_jmp_if_bit_clear_4',
        "command": 'jmp_if_bit_clear',
        "args": [0x7043, 1, 'ACTION_859_pause_0']
    },
    {
        "identifier": 'ACTION_859_jmp_if_bit_clear_5',
        "command": 'jmp_if_bit_clear',
        "args": [0x7044, 6, 'ACTION_859_pause_0']
    },
    {
        "identifier": 'ACTION_859_set_700C_to_object_coord_6',
        "command": 'set_700C_to_object_coord',
        "args": [AreaObjects.MARIO, Coords.F]
    },
    {
        "identifier": 'ACTION_859_jmp_if_var_equals_short_7',
        "command": 'jmp_if_var_equals_short',
        "args": [0x700c, 4, 'ACTION_859_jmp_if_var_equals_byte_19']
    },
    {
        "identifier": 'ACTION_859_jmp_if_var_equals_short_8',
        "command": 'jmp_if_var_equals_short',
        "args": [0x700c, 3, 'ACTION_859_jmp_if_var_equals_byte_19']
    },
    {
        "identifier": 'ACTION_859_jmp_if_var_equals_short_9',
        "command": 'jmp_if_var_equals_short',
        "args": [0x700c, 2, 'ACTION_859_jmp_if_var_equals_byte_19']
    },
    {
        "identifier": 'ACTION_859_jmp_if_var_equals_short_10',
        "command": 'jmp_if_var_equals_short',
        "args": [0x700c, 1, 'ACTION_859_jmp_if_var_equals_byte_19']
    },
    {
        "identifier": 'ACTION_859_jmp_if_var_equals_byte_11',
        "command": 'jmp_if_var_equals_byte',
        "args": [0x70c2, 16, 'ACTION_859_pause_0']
    },
    {
        "identifier": 'ACTION_859_add_12',
        "command": 'add',
        "args": [0x70c2, 0x01]
    },
    {
        "identifier": 'ACTION_859_set_sprite_sequence_13',
        "command": 'set_sprite_sequence',
        "args": [1, inc_sprite=0, flags=[_0x08Flags.LOOPING_OFF]]
    },
    {
        "identifier": 'ACTION_859_shift_northeast_pixels_14',
        "command": 'shift_northeast_pixels',
        "args": [5]
    },
    {
        "identifier": 'ACTION_859_clear_bit_15',
        "command": 'clear_bit',
        "args": [0x7043, 0]
    },
    {
        "identifier": 'ACTION_859_clear_bit_16',
        "command": 'clear_bit',
        "args": [0x7043, 1]
    },
    {
        "identifier": 'ACTION_859_clear_bit_17',
        "command": 'clear_bit',
        "args": [0x7044, 6]
    },
    {
        "identifier": 'ACTION_859_jmp_18',
        "command": 'jmp',
        "args": ['ACTION_859_pause_0']
    },
    {
        "identifier": 'ACTION_859_jmp_if_var_equals_byte_19',
        "command": 'jmp_if_var_equals_byte',
        "args": [0x70c2, 0, 'ACTION_859_pause_0']
    },
    {
        "identifier": 'ACTION_859_dec_20',
        "command": 'dec',
        "args": [0x70c2]
    },
    {
        "identifier": 'ACTION_859_set_sprite_sequence_21',
        "command": 'set_sprite_sequence',
        "args": [2, inc_sprite=0, flags=[_0x08Flags.LOOPING_OFF]]
    },
    {
        "identifier": 'ACTION_859_shift_southwest_pixels_22',
        "command": 'shift_southwest_pixels',
        "args": [5]
    },
    {
        "identifier": 'ACTION_859_clear_bit_23',
        "command": 'clear_bit',
        "args": [0x7043, 1]
    },
    {
        "identifier": 'ACTION_859_clear_bit_24',
        "command": 'clear_bit',
        "args": [0x7044, 6]
    },
    {
        "identifier": 'ACTION_859_jmp_25',
        "command": 'jmp',
        "args": ['ACTION_859_pause_0']
    }
]
