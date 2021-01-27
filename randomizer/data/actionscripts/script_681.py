from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data.eventtables import RadialDirections, AreaObjects, NPCPackets, Sounds, Coords, CoordUnits, Rooms
script = [
    {
        "identifier": 'ACTION_681_set_sprite_sequence_0',
        "command": 'set_sprite_sequence',
        "args": [5, 6, [_0x08Flags.READ_AS_SEQUENCE]]
    },
    {
        "identifier": 'ACTION_681_jump_to_height_silent_1',
        "command": 'jump_to_height_silent',
        "args": [108]
    },
    {
        "identifier": 'ACTION_681_pause_2',
        "command": 'pause',
        "args": [1]
    },
    {
        "identifier": 'ACTION_681_jmp_if_bit_set_3',
        "command": 'jmp_if_bit_set',
        "args": [0x7043, 1, 'ACTION_681_ret_7']
    },
    {
        "identifier": 'ACTION_681_jmp_if_mario_in_air_4',
        "command": 'jmp_if_mario_in_air',
        "args": ['ACTION_681_pause_2']
    },
    {
        "identifier": 'ACTION_681_pause_5',
        "command": 'pause',
        "args": [30]
    },
    {
        "identifier": 'ACTION_681_jmp_6',
        "command": 'jmp',
        "args": ['ACTION_681_set_sprite_sequence_0']
    },
    {
        "identifier": 'ACTION_681_ret_7',
        "command": 'ret'
    }
]
