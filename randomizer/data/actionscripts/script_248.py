from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data.eventtables import RadialDirections, AreaObjects, NPCPackets, Sounds, Coords, CoordUnits, Rooms
script = [
    {
        "identifier": 'ACTION_248_db_0',
        "command": 'db',
        "args": [0x20, 0x03]
    },
    {
        "identifier": 'ACTION_248_embedded_animation_routine_1',
        "command": 'embedded_animation_routine',
        "args": [0x26, 0x00, 0x00, 0x00, 0x00, 0x00, 0x18, 0x00, 0x7f, 0xff, 0x00, 0xee, 0xff, 0x80, 0xfe, 0x80]
    },
    {
        "identifier": 'ACTION_248_embedded_animation_routine_2',
        "command": 'embedded_animation_routine',
        "args": [0x27, 0x00, 0x00, 0x00, 0x00, 0x00, 0xe4, 0x00, 0x5c, 0xff, 0x00, 0xee, 0xff, 0x80, 0xfe, 0x80]
    },
    {
        "identifier": 'ACTION_248_set_animation_speed_3',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.VERY_SLOW, [_0x10Flags.WALKING]]
    },
    {
        "identifier": 'ACTION_248_add_z_coord_1_step_4',
        "command": 'add_z_coord_1_step'
    },
    {
        "identifier": 'ACTION_248_pause_short_5',
        "command": 'pause_short',
        "args": [392]
    },
    {
        "identifier": 'ACTION_248_bpl_26_27_28_6',
        "command": 'bpl_26_27_28'
    },
    {
        "identifier": 'ACTION_248_ret_7',
        "command": 'ret'
    }
]
