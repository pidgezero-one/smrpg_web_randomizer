
from randomizer.helpers.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.helpers.eventtables import RadialDirections, AreaObjects, NPCPackets, Sounds, Coords, CoordUnits, Rooms
script = [
    {
        "identifier": 'ACTION_22_jump_to_height_silent_0',
        "command": 'jump_to_height_silent',
        "args": [80]
    },
    {
        "identifier": 'ACTION_22_pause_1',
        "command": 'pause',
        "args": [1]
    },
    {
        "identifier": 'ACTION_22_uj_2',
        "command": 'jmp_if_object_in_air',
        "args": [AreaObjects.DUMMY_0X07, 'ACTION_22_pause_1']
    },
    {
        "identifier": 'ACTION_22_jmp_3',
        "command": 'jmp',
        "args": ['ACTION_22_jump_to_height_silent_0']
    }
]
