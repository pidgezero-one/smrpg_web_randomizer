from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data.eventtables import RadialDirections, AreaObjects, NPCPackets, Sounds, Coords, CoordUnits, Rooms
script = [
    {
        "identifier": 'ACTION_403_db_0',
        "command": 'db',
        "args": [0x3b, 0x00, 0x80, 0x03, 0x67, 0x49]
    },
    {
        "identifier": 'ACTION_403_db_1',
        "command": 'db',
        "args": [0x3b, 0x00, 0x00, 0x05, 0x67, 0x49]
    },
    {
        "identifier": 'ACTION_403_jmp_if_random_above_128_2',
        "command": 'jmp_if_random_above_128',
        "args": ['ACTION_403_set_random_5']
    },
    {
        "identifier": 'ACTION_403_turn_random_direction_3',
        "command": 'turn_random_direction'
    },
    {
        "identifier": 'ACTION_403_pause_4',
        "command": 'pause',
        "args": [8]
    },
    {
        "identifier": 'ACTION_403_set_random_5',
        "command": 'set_random',
        "args": [0x700c, 2]
    },
    {
        "identifier": 'ACTION_403_inc_short_6',
        "command": 'inc_short',
        "args": [0x700c]
    },
    {
        "identifier": 'ACTION_403_shift_z_20_steps_7',
        "command": 'shift_z_20_steps'
    },
    {
        "identifier": 'ACTION_403_jmp_8',
        "command": 'jmp',
        "args": ['ACTION_403_db_0']
    },
    {
        "identifier": 'ACTION_403_face_mario_9',
        "command": 'face_mario'
    },
    {
        "identifier": 'ACTION_403_pause_10',
        "command": 'pause',
        "args": [8]
    },
    {
        "identifier": 'ACTION_403_set_random_11',
        "command": 'set_random',
        "args": [0x700c, 2]
    },
    {
        "identifier": 'ACTION_403_inc_short_12',
        "command": 'inc_short',
        "args": [0x700c]
    },
    {
        "identifier": 'ACTION_403_shift_z_20_steps_13',
        "command": 'shift_z_20_steps'
    },
    {
        "identifier": 'ACTION_403_jmp_14',
        "command": 'jmp',
        "args": ['ACTION_403_db_1']
    }
]
