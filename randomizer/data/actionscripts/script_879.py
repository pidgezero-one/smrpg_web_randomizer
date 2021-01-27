from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data.eventtables import RadialDirections, AreaObjects, NPCPackets, Sounds, Coords, CoordUnits, Rooms
script = [
    {
        "identifier": 'ACTION_879_pause_0',
        "command": 'pause',
        "args": [3]
    },
    {
        "identifier": 'ACTION_879_jmp_if_random_above_128_1',
        "command": 'jmp_if_random_above_128',
        "args": ['ACTION_879_pause_0']
    },
    {
        "identifier": 'ACTION_879_set_700C_to_object_coord_2',
        "command": 'set_700C_to_object_coord',
        "args": [AreaObjects.NPC_1, Coords.F, []]
    },
    {
        "identifier": 'ACTION_879_face_east_7C_3',
        "command": 'face_east_7C'
    },
    {
        "identifier": 'ACTION_879_pause_4',
        "command": 'pause',
        "args": [1]
    },
    {
        "identifier": 'ACTION_879_jmp_5',
        "command": 'jmp',
        "args": ['ACTION_879_pause_0']
    }
]
