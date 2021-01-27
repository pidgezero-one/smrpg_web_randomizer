from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data.eventtables import RadialDirections, AreaObjects, NPCPackets, Sounds, Coords, CoordUnits, Rooms
script = [
    {
        "identifier": 'ACTION_410_set_priority_0',
        "command": 'set_priority',
        "args": [3]
    },
    {
        "identifier": 'ACTION_410_set_animation_speed_1',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.NORMAL, [_0x10Flags.SEQUENCE]]
    },
    {
        "identifier": 'ACTION_410_sequence_looping_on_2',
        "command": 'sequence_looping_on'
    },
    {
        "identifier": 'ACTION_410_db_3',
        "command": 'db',
        "args": [0x20, 0x07]
    },
    {
        "identifier": 'ACTION_410_embedded_animation_routine_4',
        "command": 'embedded_animation_routine',
        "args": [0x26, 0x00, 0x00, 0x00, 0x00, 0x00, 0x40, 0x00, 0x10, 0x00, 0x01, 0x00, 0x00, 0x00, 0x02, 0x80]
    },
    {
        "identifier": 'ACTION_410_embedded_animation_routine_5',
        "command": 'embedded_animation_routine',
        "args": [0x27, 0x00, 0x00, 0x00, 0x00, 0x00, 0xc0, 0x00, 0x18, 0x00, 0x01, 0x00, 0x00, 0x00, 0x02, 0x80]
    },
    {
        "identifier": 'ACTION_410_embedded_animation_routine_6',
        "command": 'embedded_animation_routine',
        "args": [0x28, 0x00, 0x00, 0x00, 0x00, 0x00, 0x80, 0x00, 0x10, 0x00, 0x01, 0x00, 0x00, 0x00, 0x04, 0x80]
    },
    {
        "identifier": 'ACTION_410_pause_7',
        "command": 'pause',
        "args": [1]
    },
    {
        "identifier": 'ACTION_410_jmp_8',
        "command": 'jmp',
        "args": ['ACTION_410_pause_7']
    }
]
