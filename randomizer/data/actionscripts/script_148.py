from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data.eventtables import RadialDirections, AreaObjects, NPCPackets, Sounds, Coords, CoordUnits, Rooms
script = [
    {
        "identifier": 'ACTION_148_reset_properties_0',
        "command": 'reset_properties'
    },
    {
        "identifier": 'ACTION_148_pause_1',
        "command": 'pause',
        "args": [1]
    },
    {
        "identifier": 'ACTION_148_jmp_2',
        "command": 'jmp',
        "args": ['ACTION_148_reset_properties_0']
    },
    {
        "identifier": 'ACTION_148_ret_3',
        "command": 'ret'
    }
]
