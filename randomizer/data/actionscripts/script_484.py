from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data.eventtables import RadialDirections, AreaObjects, NPCPackets, Sounds, Coords, CoordUnits, Rooms
script = [
    {
        "identifier": 'ACTION_484_jump_to_height_0',
        "command": 'jump_to_height',
        "args": [64]
    },
    {
        "identifier": 'ACTION_484_pause_1',
        "command": 'pause',
        "args": [1]
    },
    {
        "identifier": 'ACTION_484_jmp_if_mario_in_air_2',
        "command": 'jmp_if_mario_in_air',
        "args": ['ACTION_484_pause_1']
    },
    {
        "identifier": 'ACTION_484_jmp_if_bit_clear_3',
        "command": 'jmp_if_bit_clear',
        "args": [0x7043, 0, 'ACTION_484_jump_to_height_0']
    },
    {
        "identifier": 'ACTION_484_ret_4',
        "command": 'ret'
    }
]
