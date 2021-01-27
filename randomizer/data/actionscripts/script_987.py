from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data.eventtables import RadialDirections, AreaObjects, NPCPackets, Sounds, Coords, CoordUnits, Rooms
script = [
    {
        "identifier": 'ACTION_987_jmp_if_bit_set_0',
        "command": 'jmp_if_bit_set',
        "args": [0x7043, 2, 'ACTION_987_set_animation_speed_3']
    },
    {
        "identifier": 'ACTION_987_transfer_xyzf_pixels_1',
        "command": 'transfer_xyzf_pixels',
        "args": [250, 4, 30, RadialDirections.NORTHEAST]
    },
    {
        "identifier": 'ACTION_987_set_sprite_sequence_2',
        "command": 'set_sprite_sequence',
        "args": [2, 0, [_0x08Flags.READ_AS_SEQUENCE]]
    },
    {
        "identifier": 'ACTION_987_set_animation_speed_3',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
    },
    {
        "identifier": 'ACTION_987_shift_z_up_pixels_4',
        "command": 'shift_z_up_pixels',
        "args": [1]
    },
    {
        "identifier": 'ACTION_987_pause_5',
        "command": 'pause',
        "args": [7]
    },
    {
        "identifier": 'ACTION_987_shift_z_up_pixels_6',
        "command": 'shift_z_up_pixels',
        "args": [1]
    },
    {
        "identifier": 'ACTION_987_pause_7',
        "command": 'pause',
        "args": [11]
    },
    {
        "identifier": 'ACTION_987_shift_z_down_pixels_8',
        "command": 'shift_z_down_pixels',
        "args": [1]
    },
    {
        "identifier": 'ACTION_987_pause_9',
        "command": 'pause',
        "args": [7]
    },
    {
        "identifier": 'ACTION_987_shift_z_down_pixels_10',
        "command": 'shift_z_down_pixels',
        "args": [1]
    },
    {
        "identifier": 'ACTION_987_pause_11',
        "command": 'pause',
        "args": [11]
    },
    {
        "identifier": 'ACTION_987_jmp_if_bit_set_12',
        "command": 'jmp_if_bit_set',
        "args": [0x7043, 1, 'ACTION_988_ret_14']
    },
    {
        "identifier": 'ACTION_987_jmp_13',
        "command": 'jmp',
        "args": ['ACTION_987_set_animation_speed_3']
    }
]
