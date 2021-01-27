from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data.eventtables import RadialDirections, AreaObjects, NPCPackets, Sounds, Coords, CoordUnits, Rooms
script = [
    {
        "identifier": 'ACTION_225_db_0',
        "command": 'db',
        "args": [0x20, 0x03]
    },
    {
        "identifier": 'ACTION_225_embedded_animation_routine_1',
        "command": 'embedded_animation_routine',
        "args": [0x26, 0x00, 0x00, 0x00, 0x00, 0x00, 0xb4, 0x00, 0x20, 0x00, 0x01, 0x00, 0x00, 0x80, 0xfe, 0x80]
    },
    {
        "identifier": 'ACTION_225_embedded_animation_routine_2',
        "command": 'embedded_animation_routine',
        "args": [0x27, 0x00, 0x00, 0x00, 0x00, 0x00, 0x76, 0x00, 0x1a, 0x00, 0x01, 0x00, 0x00, 0x80, 0xfe, 0x80]
    },
    {
        "identifier": 'ACTION_225_pause_3',
        "command": 'pause',
        "args": [176]
    },
    {
        "identifier": 'ACTION_225_set_4',
        "command": 'set',
        "args": [0x700c, 65120]
    },
    {
        "identifier": 'ACTION_225_db_5',
        "command": 'db',
        "args": [0x35, 0x00, 0x06]
    },
    {
        "identifier": 'ACTION_225_db_6',
        "command": 'db',
        "args": [0x35, 0x01, 0x06]
    },
    {
        "identifier": 'ACTION_225_pause_7',
        "command": 'pause',
        "args": [240]
    },
    {
        "identifier": 'ACTION_225_set_8',
        "command": 'set',
        "args": [0x700c, 64800]
    },
    {
        "identifier": 'ACTION_225_db_9',
        "command": 'db',
        "args": [0x35, 0x00, 0x06]
    },
    {
        "identifier": 'ACTION_225_db_10',
        "command": 'db',
        "args": [0x35, 0x01, 0x06]
    },
    {
        "identifier": 'ACTION_225_pause_11',
        "command": 'pause',
        "args": [120]
    },
    {
        "identifier": 'ACTION_225_set_12',
        "command": 'set',
        "args": [0x700c, 64512]
    },
    {
        "identifier": 'ACTION_225_db_13',
        "command": 'db',
        "args": [0x35, 0x00, 0x06]
    },
    {
        "identifier": 'ACTION_225_db_14',
        "command": 'db',
        "args": [0x35, 0x01, 0x06]
    },
    {
        "identifier": 'ACTION_225_pause_15',
        "command": 'pause',
        "args": [90]
    },
    {
        "identifier": 'ACTION_225_set_16',
        "command": 'set',
        "args": [0x700c, 64000]
    },
    {
        "identifier": 'ACTION_225_db_17',
        "command": 'db',
        "args": [0x35, 0x00, 0x06]
    },
    {
        "identifier": 'ACTION_225_db_18',
        "command": 'db',
        "args": [0x35, 0x01, 0x06]
    },
    {
        "identifier": 'ACTION_225_pause_19',
        "command": 'pause',
        "args": [60]
    },
    {
        "identifier": 'ACTION_225_set_20',
        "command": 'set',
        "args": [0x700c, 63744]
    },
    {
        "identifier": 'ACTION_225_db_21',
        "command": 'db',
        "args": [0x35, 0x00, 0x06]
    },
    {
        "identifier": 'ACTION_225_db_22',
        "command": 'db',
        "args": [0x35, 0x01, 0x06]
    },
    {
        "identifier": 'ACTION_225_pause_23',
        "command": 'pause',
        "args": [30]
    },
    {
        "identifier": 'ACTION_225_set_24',
        "command": 'set',
        "args": [0x700c, 63488]
    },
    {
        "identifier": 'ACTION_225_db_25',
        "command": 'db',
        "args": [0x35, 0x00, 0x06]
    },
    {
        "identifier": 'ACTION_225_db_26',
        "command": 'db',
        "args": [0x35, 0x01, 0x06]
    },
    {
        "identifier": 'ACTION_225_pause_27',
        "command": 'pause',
        "args": [212]
    },
    {
        "identifier": 'ACTION_225_set_28',
        "command": 'set',
        "args": [0x700c, 64256]
    },
    {
        "identifier": 'ACTION_225_db_29',
        "command": 'db',
        "args": [0x35, 0x00, 0x06]
    },
    {
        "identifier": 'ACTION_225_db_30',
        "command": 'db',
        "args": [0x35, 0x01, 0x06]
    },
    {
        "identifier": 'ACTION_225_set_animation_speed_31',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
    },
    {
        "identifier": 'ACTION_225_shift_z_up_pixels_32',
        "command": 'shift_z_up_pixels',
        "args": [8]
    },
    {
        "identifier": 'ACTION_225_set_animation_speed_33',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING]]
    },
    {
        "identifier": 'ACTION_225_add_z_coord_1_step_34',
        "command": 'add_z_coord_1_step'
    },
    {
        "identifier": 'ACTION_225_set_animation_speed_35',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.WALKING]]
    },
    {
        "identifier": 'ACTION_225_shift_z_up_steps_36',
        "command": 'shift_z_up_steps',
        "args": [2]
    },
    {
        "identifier": 'ACTION_225_set_bit_37',
        "command": 'set_bit',
        "args": [0x7043, 3]
    },
    {
        "identifier": 'ACTION_225_shift_z_up_steps_38',
        "command": 'shift_z_up_steps',
        "args": [2]
    },
    {
        "identifier": 'ACTION_225_set_animation_speed_39',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.FASTEST, [_0x10Flags.WALKING]]
    },
    {
        "identifier": 'ACTION_225_shift_z_up_steps_40',
        "command": 'shift_z_up_steps',
        "args": [8]
    },
    {
        "identifier": 'ACTION_225_bpl_26_27_28_41',
        "command": 'bpl_26_27_28'
    },
    {
        "identifier": 'ACTION_225_ret_42',
        "command": 'ret'
    }
]
