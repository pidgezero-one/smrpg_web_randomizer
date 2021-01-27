from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data.eventtables import RadialDirections, AreaObjects, NPCPackets, Sounds, Coords, CoordUnits, Rooms
script = [
    {
        "identifier": 'ACTION_254_floating_off_0',
        "command": 'floating_off'
    },
    {
        "identifier": 'ACTION_254_db_1',
        "command": 'db',
        "args": [0x20, 0x03]
    },
    {
        "identifier": 'ACTION_254_embedded_animation_routine_2',
        "command": 'embedded_animation_routine',
        "args": [0x26, 0x00, 0x00, 0x00, 0x00, 0x00, 0xb4, 0x00, 0x20, 0x00, 0x01, 0x00, 0x00, 0x80, 0xfe, 0x80]
    },
    {
        "identifier": 'ACTION_254_embedded_animation_routine_3',
        "command": 'embedded_animation_routine',
        "args": [0x27, 0x00, 0x00, 0x00, 0x00, 0x00, 0x76, 0x00, 0x1a, 0x00, 0x01, 0x00, 0x00, 0x80, 0xfe, 0x80]
    },
    {
        "identifier": 'ACTION_254_pause_4',
        "command": 'pause',
        "args": [248]
    },
    {
        "identifier": 'ACTION_254_set_5',
        "command": 'set',
        "args": [0x700c, 65120]
    },
    {
        "identifier": 'ACTION_254_db_6',
        "command": 'db',
        "args": [0x35, 0x00, 0x06]
    },
    {
        "identifier": 'ACTION_254_db_7',
        "command": 'db',
        "args": [0x35, 0x01, 0x06]
    },
    {
        "identifier": 'ACTION_254_pause_8',
        "command": 'pause',
        "args": [240]
    },
    {
        "identifier": 'ACTION_254_set_9',
        "command": 'set',
        "args": [0x700c, 64800]
    },
    {
        "identifier": 'ACTION_254_db_10',
        "command": 'db',
        "args": [0x35, 0x00, 0x06]
    },
    {
        "identifier": 'ACTION_254_db_11',
        "command": 'db',
        "args": [0x35, 0x01, 0x06]
    },
    {
        "identifier": 'ACTION_254_pause_12',
        "command": 'pause',
        "args": [120]
    },
    {
        "identifier": 'ACTION_254_set_13',
        "command": 'set',
        "args": [0x700c, 64512]
    },
    {
        "identifier": 'ACTION_254_db_14',
        "command": 'db',
        "args": [0x35, 0x00, 0x06]
    },
    {
        "identifier": 'ACTION_254_db_15',
        "command": 'db',
        "args": [0x35, 0x01, 0x06]
    },
    {
        "identifier": 'ACTION_254_pause_16',
        "command": 'pause',
        "args": [90]
    },
    {
        "identifier": 'ACTION_254_set_17',
        "command": 'set',
        "args": [0x700c, 64000]
    },
    {
        "identifier": 'ACTION_254_db_18',
        "command": 'db',
        "args": [0x35, 0x00, 0x06]
    },
    {
        "identifier": 'ACTION_254_db_19',
        "command": 'db',
        "args": [0x35, 0x01, 0x06]
    },
    {
        "identifier": 'ACTION_254_pause_20',
        "command": 'pause',
        "args": [60]
    },
    {
        "identifier": 'ACTION_254_set_21',
        "command": 'set',
        "args": [0x700c, 63744]
    },
    {
        "identifier": 'ACTION_254_db_22',
        "command": 'db',
        "args": [0x35, 0x00, 0x06]
    },
    {
        "identifier": 'ACTION_254_db_23',
        "command": 'db',
        "args": [0x35, 0x01, 0x06]
    },
    {
        "identifier": 'ACTION_254_pause_24',
        "command": 'pause',
        "args": [30]
    },
    {
        "identifier": 'ACTION_254_set_25',
        "command": 'set',
        "args": [0x700c, 63488]
    },
    {
        "identifier": 'ACTION_254_db_26',
        "command": 'db',
        "args": [0x35, 0x00, 0x06]
    },
    {
        "identifier": 'ACTION_254_db_27',
        "command": 'db',
        "args": [0x35, 0x01, 0x06]
    },
    {
        "identifier": 'ACTION_254_pause_28',
        "command": 'pause',
        "args": [230]
    },
    {
        "identifier": 'ACTION_254_set_animation_speed_29',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
    },
    {
        "identifier": 'ACTION_254_shift_z_up_pixels_30',
        "command": 'shift_z_up_pixels',
        "args": [8]
    },
    {
        "identifier": 'ACTION_254_set_animation_speed_31',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING]]
    },
    {
        "identifier": 'ACTION_254_add_z_coord_1_step_32',
        "command": 'add_z_coord_1_step'
    },
    {
        "identifier": 'ACTION_254_set_animation_speed_33',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.WALKING]]
    },
    {
        "identifier": 'ACTION_254_shift_z_up_steps_34',
        "command": 'shift_z_up_steps',
        "args": [2]
    },
    {
        "identifier": 'ACTION_254_set_bit_35',
        "command": 'set_bit',
        "args": [0x7043, 4]
    },
    {
        "identifier": 'ACTION_254_shift_z_up_steps_36',
        "command": 'shift_z_up_steps',
        "args": [2]
    },
    {
        "identifier": 'ACTION_254_set_animation_speed_37',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.FASTEST, [_0x10Flags.WALKING]]
    },
    {
        "identifier": 'ACTION_254_shift_z_up_steps_38',
        "command": 'shift_z_up_steps',
        "args": [8]
    },
    {
        "identifier": 'ACTION_254_bpl_26_27_28_39',
        "command": 'bpl_26_27_28'
    },
    {
        "identifier": 'ACTION_254_ret_40',
        "command": 'ret'
    }
]