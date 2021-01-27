from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data.eventtables import RadialDirections, AreaObjects, NPCPackets, Sounds, Coords, CoordUnits, Rooms
script = [
    {
        "identifier": 'ACTION_78_pause_0',
        "command": 'pause',
        "args": [150]
    },
    {
        "identifier": 'ACTION_78_set_sprite_sequence_1',
        "command": 'set_sprite_sequence',
        "args": [3, 3, [_0x08Flags.READ_AS_SEQUENCE]]
    },
    {
        "identifier": 'ACTION_78_pause_2',
        "command": 'pause',
        "args": [120]
    },
    {
        "identifier": 'ACTION_78_reset_properties_3',
        "command": 'reset_properties'
    },
    {
        "identifier": 'ACTION_78_jmp_4',
        "command": 'jmp',
        "args": ['ACTION_78_pause_0']
    }
]
