from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data.eventtables import RadialDirections, AreaObjects, NPCPackets, Sounds, Coords, CoordUnits, Rooms
script = [
    {
        "identifier": 'ACTION_101_jmp_if_bit_set_0',
        "command": 'jmp_if_bit_set',
        "args": [0x7043, 6, 'ACTION_101_jmp_if_random_above_128_6']
    },
    {
        "identifier": 'ACTION_101_jmp_if_random_above_128_1',
        "command": 'jmp_if_random_above_128',
        "args": ['ACTION_101_transfer_xyzf_pixels_4']
    },
    {
        "identifier": 'ACTION_101_transfer_xyzf_pixels_2',
        "command": 'transfer_xyzf_pixels',
        "args": [0, 0, 21, RadialDirections.EAST]
    },
    {
        "identifier": 'ACTION_101_jmp_3',
        "command": 'jmp',
        "args": ['ACTION_103_set_animation_speed_15']
    },
    {
        "identifier": 'ACTION_101_transfer_xyzf_pixels_4',
        "command": 'transfer_xyzf_pixels',
        "args": [0, 0, 14, RadialDirections.EAST]
    },
    {
        "identifier": 'ACTION_101_jmp_5',
        "command": 'jmp',
        "args": ['ACTION_103_set_animation_speed_23']
    },
    {
        "identifier": 'ACTION_101_jmp_if_random_above_128_6',
        "command": 'jmp_if_random_above_128',
        "args": ['ACTION_101_pause_9']
    },
    {
        "identifier": 'ACTION_101_pause_7',
        "command": 'pause',
        "args": [8]
    },
    {
        "identifier": 'ACTION_101_jmp_8',
        "command": 'jmp',
        "args": ['ACTION_103_clear_solidity_bits_0']
    },
    {
        "identifier": 'ACTION_101_pause_9',
        "command": 'pause',
        "args": [20]
    },
    {
        "identifier": 'ACTION_101_jmp_10',
        "command": 'jmp',
        "args": ['ACTION_103_clear_solidity_bits_0']
    }
]
