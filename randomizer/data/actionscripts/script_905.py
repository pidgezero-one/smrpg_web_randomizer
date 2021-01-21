from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data.eventtables import RadialDirections, AreaObjects, NPCPackets, Sounds, Coords, CoordUnits, Rooms
script = [
    {
        "identifier": 'ACTION_905_set_700C_to_object_coord_0',
        "command": 'set_700C_to_object_coord',
        "args": [AreaObjects.MARIO, Coords.F]
    },
    {
        "identifier": 'ACTION_905_face_east_1',
        "command": 'face_east'
    },
    {
        "identifier": 'ACTION_905_jmp_2',
        "command": 'jmp',
        "args": ['ACTION_903_jump_to_height_silent_1']
    }
]
