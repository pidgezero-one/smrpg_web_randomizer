from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data.eventtables import RadialDirections, AreaObjects, NPCPackets, Sounds, Coords, CoordUnits, Rooms
script = [
    {
        "identifier": 'ACTION_183_jmp_if_bit_set_0',
        "command": 'jmp_if_bit_set',
        "args": [0x7048, 7, 'ACTION_183_set_sprite_sequence_3']
    },
    {
        "identifier": 'ACTION_183_sequence_looping_on_1',
        "command": 'sequence_looping_on'
    },
    {
        "identifier": 'ACTION_183_ret_2',
        "command": 'ret'
    },
    {
        "identifier": 'ACTION_183_set_sprite_sequence_3',
        "command": 'set_sprite_sequence',
        "args": [16, inc_sprite=0, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
    },
    {
        "identifier": 'ACTION_183_ret_4',
        "command": 'ret'
    }
]
