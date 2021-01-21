from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data.eventtables import RadialDirections, AreaObjects, NPCPackets, Sounds, Coords, CoordUnits, Rooms
script = [
    {
        "identifier": 'ACTION_603_set_priority_0',
        "command": 'set_priority',
        "args": [3]
    },
    {
        "identifier": 'ACTION_603_db_1',
        "command": 'db',
        "args": [0x20, 0x03]
    },
    {
        "identifier": 'ACTION_603_embedded_animation_routine_2',
        "command": 'embedded_animation_routine',
        "args": [0x26]
    },
    {
        "identifier": 'ACTION_603_embedded_animation_routine_3',
        "command": 'embedded_animation_routine',
        "args": [0x27]
    },
    {
        "identifier": 'ACTION_603_turn_clockwise_45_degrees_n_times_4',
        "command": 'turn_clockwise_45_degrees_n_times',
        "args": [2]
    },
    {
        "identifier": 'ACTION_603_pause_5',
        "command": 'pause',
        "args": [7]
    },
    {
        "identifier": 'ACTION_603_jmp_6',
        "command": 'jmp',
        "args": ['ACTION_603_turn_clockwise_45_degrees_n_times_4']
    }
]
