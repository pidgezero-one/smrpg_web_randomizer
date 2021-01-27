from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data.eventtables import RadialDirections, AreaObjects, NPCPackets, Sounds, Coords, CoordUnits, Rooms
script = [
    {
        "identifier": 'ACTION_878_set_animation_speed_0',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.NORMAL, [_0x10Flags.SEQUENCE]]
    },
    {
        "identifier": 'ACTION_878_sequence_looping_on_1',
        "command": 'sequence_looping_on'
    },
    {
        "identifier": 'ACTION_878_set_700C_to_object_coord_2',
        "command": 'set_700C_to_object_coord',
        "args": [AreaObjects.DUMMY_0X07, Coords.F, []]
    },
    {
        "identifier": 'ACTION_878_set_7000_short_mem_to_700C_3',
        "command": 'set_7000_short_mem_to_700C',
        "args": [0x7024]
    },
    {
        "identifier": 'ACTION_878_face_southwest_7D_4',
        "command": 'face_southwest_7D',
        "args": [0x00]
    },
    {
        "identifier": 'ACTION_878_set_700C_to_object_coord_5',
        "command": 'set_700C_to_object_coord',
        "args": [AreaObjects.DUMMY_0X07, Coords.F, []]
    },
    {
        "identifier": 'ACTION_878_jmp_if_700C_not_equals_short_6',
        "command": 'jmp_if_700C_not_equals_short',
        "args": [5, 'ACTION_878_face_east_7C_8']
    },
    {
        "identifier": 'ACTION_878_set_700C_to_7000_short_mem_7',
        "command": 'set_700C_to_7000_short_mem',
        "args": [0x7024]
    },
    {
        "identifier": 'ACTION_878_face_east_7C_8',
        "command": 'face_east_7C'
    },
    {
        "identifier": 'ACTION_878_pause_9',
        "command": 'pause',
        "args": [1]
    },
    {
        "identifier": 'ACTION_878_jmp_10',
        "command": 'jmp',
        "args": ['ACTION_878_set_animation_speed_0']
    }
]
