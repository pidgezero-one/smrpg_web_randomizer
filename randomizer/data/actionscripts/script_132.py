from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data.eventtables import RadialDirections, AreaObjects, NPCPackets, Sounds, Coords, CoordUnits, Rooms
script = [
    {
        "identifier": 'ACTION_132_set_priority_0',
        "command": 'set_priority',
        "args": [3]
    },
    {
        "identifier": 'ACTION_132_db_1',
        "command": 'db',
        "args": [0x20, 0x04]
    },
    {
        "identifier": 'ACTION_132_db_2',
        "command": 'db',
        "args": [0x25, 0x00, 0x07, 0xa0, 0xff]
    },
    {
        "identifier": 'ACTION_132_set_animation_speed_3',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.SLOW, [_0x10Flags.WALKING]]
    },
    {
        "identifier": 'ACTION_132_shift_northwest_pixels_4',
        "command": 'shift_northwest_pixels',
        "args": [16]
    },
    {
        "identifier": 'ACTION_132_bpl_26_27_28_5',
        "command": 'bpl_26_27_28'
    },
    {
        "identifier": 'ACTION_132_face_southeast_6',
        "command": 'face_southeast'
    },
    {
        "identifier": 'ACTION_132_db_7',
        "command": 'db',
        "args": [0x20, 0x04]
    },
    {
        "identifier": 'ACTION_132_db_8',
        "command": 'db',
        "args": [0x25, 0x00, 0x04, 0xa0, 0xff]
    },
    {
        "identifier": 'ACTION_132_shift_southeast_pixels_9',
        "command": 'shift_southeast_pixels',
        "args": [16]
    },
    {
        "identifier": 'ACTION_132_bpl_26_27_28_10',
        "command": 'bpl_26_27_28'
    },
    {
        "identifier": 'ACTION_132_jmp_11',
        "command": 'jmp',
        "args": ['ACTION_132_set_priority_0']
    }
]
