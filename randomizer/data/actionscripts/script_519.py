from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data.eventtables import RadialDirections, AreaObjects, NPCPackets, Sounds, Coords, CoordUnits, Rooms
script = [
    {
        "identifier": 'ACTION_519_face_southwest_0',
        "command": 'face_southwest'
    },
    {
        "identifier": 'ACTION_519_fixed_f_coord_on_1',
        "command": 'fixed_f_coord_on'
    },
    {
        "identifier": 'ACTION_519_pause_2',
        "command": 'pause',
        "args": [120]
    },
    {
        "identifier": 'ACTION_519_set_animation_speed_3',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
    },
    {
        "identifier": 'ACTION_519_shift_south_pixels_4',
        "command": 'shift_south_pixels',
        "args": [15]
    },
    {
        "identifier": 'ACTION_519_jmp_if_bit_set_5',
        "command": 'jmp_if_bit_set',
        "args": [0x7053, 7, 'ACTION_519_visibility_off_14']
    },
    {
        "identifier": 'ACTION_519_pause_6',
        "command": 'pause',
        "args": [120]
    },
    {
        "identifier": 'ACTION_519_pause_7',
        "command": 'pause',
        "args": [120]
    },
    {
        "identifier": 'ACTION_519_pause_8',
        "command": 'pause',
        "args": [120]
    },
    {
        "identifier": 'ACTION_519_pause_9',
        "command": 'pause',
        "args": [120]
    },
    {
        "identifier": 'ACTION_519_jmp_if_bit_set_10',
        "command": 'jmp_if_bit_set',
        "args": [0x7053, 7, 'ACTION_519_visibility_off_14']
    },
    {
        "identifier": 'ACTION_519_shift_north_pixels_11',
        "command": 'shift_north_pixels',
        "args": [15]
    },
    {
        "identifier": 'ACTION_519_pause_12',
        "command": 'pause',
        "args": [60]
    },
    {
        "identifier": 'ACTION_519_jmp_13',
        "command": 'jmp',
        "args": ['ACTION_519_face_southwest_0']
    },
    {
        "identifier": 'ACTION_519_visibility_off_14',
        "command": 'visibility_off'
    },
    {
        "identifier": 'ACTION_519_ret_15',
        "command": 'ret'
    }
]
