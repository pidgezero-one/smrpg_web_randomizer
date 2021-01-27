from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data.eventtables import RadialDirections, AreaObjects, NPCPackets, Sounds, Coords, CoordUnits, Rooms
script = [
    {
        "identifier": 'ACTION_916_visibility_off_0',
        "command": 'visibility_off'
    },
    {
        "identifier": 'ACTION_916_set_sprite_sequence_1',
        "command": 'set_sprite_sequence',
        "args": [1, 0, [_0x08Flags.READ_AS_SEQUENCE]]
    },
    {
        "identifier": 'ACTION_916_jmp_2',
        "command": 'jmp',
        "args": ['ACTION_917_pause_2']
    }
]
