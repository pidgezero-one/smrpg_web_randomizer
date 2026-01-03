
from randomizer.helpers.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.helpers.eventtables import RadialDirections, AreaObjects, NPCPackets, Sounds, Coords, CoordUnits, Rooms
script = [
    {
        "identifier": 'ACTION_721_visibility_off_0',
        "command": 'visibility_off'
    },
    {
        "identifier": 'ACTION_721_set_sprite_sequence_1',
        "command": 'set_sprite_sequence',
        "args": [2, 0, [_0x08Flags.READ_AS_SEQUENCE]]
    },
    {
        "identifier": 'ACTION_721_sequence_looping_on_0',
        "command": 'sequence_looping_on'
    },
    {
        "identifier": 'ACTION_721_set_priority_3',
        "command": 'set_priority',
        "args": [3]
    },
    {
        "identifier": 'ACTION_721_visibility_on_4',
        "command": 'visibility_on'
    },
    {
        "identifier": 'ACTION_721_set_solidity_bits_18',
        "command": 'set_solidity_bits',
        "args": [[_0x0AFlags.CANT_JUMP_THROUGH]]
    },
    {
        "identifier": 'ACTION_721_pause_8',
        "command": 'pause',
        "args": [1]
    },
    {
        "identifier": 'ACTION_721_jmp_9',
        "command": 'jmp',
        "args": ['ACTION_721_pause_8']
    }
]
