from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data.eventtables import RadialDirections, AreaObjects, NPCPackets, Sounds, Coords, CoordUnits, Rooms
script = [
    {
        "identifier": 'ACTION_259_jmp_if_random_above_128_0',
        "command": 'jmp_if_random_above_128',
        "args": ['ACTION_259_pause_2']
    },
    {
        "identifier": 'ACTION_259_pause_1',
        "command": 'pause',
        "args": [60]
    },
    {
        "identifier": 'ACTION_259_pause_2',
        "command": 'pause',
        "args": [30]
    },
    {
        "identifier": 'ACTION_259_set_sprite_sequence_3',
        "command": 'set_sprite_sequence',
        "args": [3, 0, [_0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
    },
    {
        "identifier": 'ACTION_259_set_bit_4',
        "command": 'set_bit',
        "args": [0x7043, 6]
    },
    {
        "identifier": 'ACTION_259_pause_5',
        "command": 'pause',
        "args": [120]
    },
    {
        "identifier": 'ACTION_259_clear_bit_6',
        "command": 'clear_bit',
        "args": [0x7043, 6]
    },
    {
        "identifier": 'ACTION_259_reset_properties_7',
        "command": 'reset_properties'
    },
    {
        "identifier": 'ACTION_259_jmp_8',
        "command": 'jmp',
        "args": ['ACTION_259_jmp_if_random_above_128_0']
    }
]
