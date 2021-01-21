from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data.eventtables import RadialDirections, AreaObjects, NPCPackets, Sounds, Coords, CoordUnits, Rooms
script = [
    {
        "identifier": 'ACTION_411_set_priority_0',
        "command": 'set_priority',
        "args": [3]
    },
    {
        "identifier": 'ACTION_411_set_animation_speed_1',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.NORMAL, [_0x10Flags.SEQUENCE]]
    },
    {
        "identifier": 'ACTION_411_sequence_looping_on_2',
        "command": 'sequence_looping_on'
    },
    {
        "identifier": 'ACTION_411_db_3',
        "command": 'db',
        "args": [0x20, 0x07]
    },
    {
        "identifier": 'ACTION_411_embedded_animation_routine_4',
        "command": 'embedded_animation_routine',
        "args": [0x26]
    },
    {
        "identifier": 'ACTION_411_embedded_animation_routine_5',
        "command": 'embedded_animation_routine',
        "args": [0x27]
    },
    {
        "identifier": 'ACTION_411_embedded_animation_routine_6',
        "command": 'embedded_animation_routine',
        "args": [0x28]
    },
    {
        "identifier": 'ACTION_411_pause_7',
        "command": 'pause',
        "args": [1]
    },
    {
        "identifier": 'ACTION_411_jmp_8',
        "command": 'jmp',
        "args": ['ACTION_411_pause_7']
    }
]
