from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data.eventtables import RadialDirections, AreaObjects, NPCPackets, Sounds, Coords, CoordUnits, Rooms
script = [
    {
        "identifier": 'ACTION_224_floating_off_0',
        "command": 'floating_off'
    },
    {
        "identifier": 'ACTION_224_db_1',
        "command": 'db',
        "args": [0x20, 0x03]
    },
    {
        "identifier": 'ACTION_224_embedded_animation_routine_2',
        "command": 'embedded_animation_routine',
        "args": [0x26]
    },
    {
        "identifier": 'ACTION_224_embedded_animation_routine_3',
        "command": 'embedded_animation_routine',
        "args": [0x27]
    },
    {
        "identifier": 'ACTION_224_pause_4',
        "command": 'pause',
        "args": [200]
    },
    {
        "identifier": 'ACTION_224_set_5',
        "command": 'set',
        "args": [0x700c, 65120]
    },
    {
        "identifier": 'ACTION_224_db_6',
        "command": 'db',
        "args": [0x35, 0x00, 0x06]
    },
    {
        "identifier": 'ACTION_224_db_7',
        "command": 'db',
        "args": [0x35, 0x01, 0x06]
    },
    {
        "identifier": 'ACTION_224_pause_8',
        "command": 'pause',
        "args": [240]
    },
    {
        "identifier": 'ACTION_224_set_9',
        "command": 'set',
        "args": [0x700c, 64800]
    },
    {
        "identifier": 'ACTION_224_db_10',
        "command": 'db',
        "args": [0x35, 0x00, 0x06]
    },
    {
        "identifier": 'ACTION_224_db_11',
        "command": 'db',
        "args": [0x35, 0x01, 0x06]
    },
    {
        "identifier": 'ACTION_224_pause_12',
        "command": 'pause',
        "args": [120]
    },
    {
        "identifier": 'ACTION_224_set_13',
        "command": 'set',
        "args": [0x700c, 64512]
    },
    {
        "identifier": 'ACTION_224_db_14',
        "command": 'db',
        "args": [0x35, 0x00, 0x06]
    },
    {
        "identifier": 'ACTION_224_db_15',
        "command": 'db',
        "args": [0x35, 0x01, 0x06]
    },
    {
        "identifier": 'ACTION_224_pause_16',
        "command": 'pause',
        "args": [90]
    },
    {
        "identifier": 'ACTION_224_set_17',
        "command": 'set',
        "args": [0x700c, 64000]
    },
    {
        "identifier": 'ACTION_224_db_18',
        "command": 'db',
        "args": [0x35, 0x00, 0x06]
    },
    {
        "identifier": 'ACTION_224_db_19',
        "command": 'db',
        "args": [0x35, 0x01, 0x06]
    },
    {
        "identifier": 'ACTION_224_pause_20',
        "command": 'pause',
        "args": [60]
    },
    {
        "identifier": 'ACTION_224_set_21',
        "command": 'set',
        "args": [0x700c, 63744]
    },
    {
        "identifier": 'ACTION_224_db_22',
        "command": 'db',
        "args": [0x35, 0x00, 0x06]
    },
    {
        "identifier": 'ACTION_224_db_23',
        "command": 'db',
        "args": [0x35, 0x01, 0x06]
    },
    {
        "identifier": 'ACTION_224_pause_24',
        "command": 'pause',
        "args": [30]
    },
    {
        "identifier": 'ACTION_224_set_25',
        "command": 'set',
        "args": [0x700c, 63488]
    },
    {
        "identifier": 'ACTION_224_db_26',
        "command": 'db',
        "args": [0x35, 0x00, 0x06]
    },
    {
        "identifier": 'ACTION_224_db_27',
        "command": 'db',
        "args": [0x35, 0x01, 0x06]
    },
    {
        "identifier": 'ACTION_224_pause_28',
        "command": 'pause',
        "args": [330]
    },
    {
        "identifier": 'ACTION_224_set_29',
        "command": 'set',
        "args": [0x700c, 64256]
    },
    {
        "identifier": 'ACTION_224_db_30',
        "command": 'db',
        "args": [0x35, 0x00, 0x06]
    },
    {
        "identifier": 'ACTION_224_db_31',
        "command": 'db',
        "args": [0x35, 0x01, 0x06]
    },
    {
        "identifier": 'ACTION_224_set_animation_speed_32',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
    },
    {
        "identifier": 'ACTION_224_shift_z_up_pixels_33',
        "command": 'shift_z_up_pixels',
        "args": [8]
    },
    {
        "identifier": 'ACTION_224_set_animation_speed_34',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING]]
    },
    {
        "identifier": 'ACTION_224_add_z_coord_1_step_35',
        "command": 'add_z_coord_1_step'
    },
    {
        "identifier": 'ACTION_224_set_animation_speed_36',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.WALKING]]
    },
    {
        "identifier": 'ACTION_224_shift_z_up_steps_37',
        "command": 'shift_z_up_steps',
        "args": [2]
    },
    {
        "identifier": 'ACTION_224_set_bit_38',
        "command": 'set_bit',
        "args": [0x7043, 6]
    },
    {
        "identifier": 'ACTION_224_shift_z_up_steps_39',
        "command": 'shift_z_up_steps',
        "args": [2]
    },
    {
        "identifier": 'ACTION_224_set_animation_speed_40',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.FASTEST, [_0x10Flags.WALKING]]
    },
    {
        "identifier": 'ACTION_224_shift_z_up_steps_41',
        "command": 'shift_z_up_steps',
        "args": [8]
    },
    {
        "identifier": 'ACTION_224_bpl_26_27_28_42',
        "command": 'bpl_26_27_28'
    },
    {
        "identifier": 'ACTION_224_ret_43',
        "command": 'ret'
    }
]
