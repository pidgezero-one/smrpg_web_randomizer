from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data.eventtables import RadialDirections, AreaObjects, NPCPackets, Sounds, Coords, CoordUnits, Rooms
script = [
    {
        "identifier": 'ACTION_207_set_vram_priority_0',
        "command": 'set_vram_priority',
        "args": [VramPriority.OBJECT_OVERLAPS_MARIO_ON_ALL_SIDES]
    },
    {
        "identifier": 'ACTION_207_set_priority_1',
        "command": 'set_priority',
        "args": [3]
    },
    {
        "identifier": 'ACTION_207_set_sprite_sequence_2',
        "command": 'set_sprite_sequence',
        "args": [1, 0, [_0x08Flags.READ_AS_SEQUENCE]]
    },
    {
        "identifier": 'ACTION_207_set_3',
        "command": 'set',
        "args": [0x70c0, 1]
    },
    {
        "identifier": 'ACTION_207_jmp_if_bit_set_4',
        "command": 'jmp_if_bit_set',
        "args": [0x7045, 4, 'ACTION_207_pause_8']
    },
    {
        "identifier": 'ACTION_207_jmp_if_bit_set_5',
        "command": 'jmp_if_bit_set',
        "args": [0x7045, 5, 'ACTION_207_pause_10']
    },
    {
        "identifier": 'ACTION_207_pause_6',
        "command": 'pause',
        "args": [7]
    },
    {
        "identifier": 'ACTION_207_jmp_7',
        "command": 'jmp',
        "args": ['ACTION_207_set_sprite_sequence_11']
    },
    {
        "identifier": 'ACTION_207_pause_8',
        "command": 'pause',
        "args": [4]
    },
    {
        "identifier": 'ACTION_207_jmp_9',
        "command": 'jmp',
        "args": ['ACTION_207_set_sprite_sequence_11']
    },
    {
        "identifier": 'ACTION_207_pause_10',
        "command": 'pause',
        "args": [9]
    },
    {
        "identifier": 'ACTION_207_set_sprite_sequence_11',
        "command": 'set_sprite_sequence',
        "args": [0, 0, [_0x08Flags.READ_AS_SEQUENCE]]
    },
    {
        "identifier": 'ACTION_207_set_12',
        "command": 'set',
        "args": [0x70c0, 0]
    },
    {
        "identifier": 'ACTION_207_jmp_if_bit_set_13',
        "command": 'jmp_if_bit_set',
        "args": [0x7045, 4, 'ACTION_207_pause_17']
    },
    {
        "identifier": 'ACTION_207_jmp_if_bit_set_14',
        "command": 'jmp_if_bit_set',
        "args": [0x7045, 5, 'ACTION_207_pause_19']
    },
    {
        "identifier": 'ACTION_207_pause_15',
        "command": 'pause',
        "args": [7]
    },
    {
        "identifier": 'ACTION_207_jmp_16',
        "command": 'jmp',
        "args": ['ACTION_207_set_sprite_sequence_20']
    },
    {
        "identifier": 'ACTION_207_pause_17',
        "command": 'pause',
        "args": [4]
    },
    {
        "identifier": 'ACTION_207_jmp_18',
        "command": 'jmp',
        "args": ['ACTION_207_set_sprite_sequence_20']
    },
    {
        "identifier": 'ACTION_207_pause_19',
        "command": 'pause',
        "args": [9]
    },
    {
        "identifier": 'ACTION_207_set_sprite_sequence_20',
        "command": 'set_sprite_sequence',
        "args": [3, 0, [_0x08Flags.READ_AS_SEQUENCE]]
    },
    {
        "identifier": 'ACTION_207_set_21',
        "command": 'set',
        "args": [0x70c0, 2]
    },
    {
        "identifier": 'ACTION_207_jmp_if_bit_set_22',
        "command": 'jmp_if_bit_set',
        "args": [0x7045, 4, 'ACTION_207_pause_26']
    },
    {
        "identifier": 'ACTION_207_jmp_if_bit_set_23',
        "command": 'jmp_if_bit_set',
        "args": [0x7045, 5, 'ACTION_207_pause_28']
    },
    {
        "identifier": 'ACTION_207_pause_24',
        "command": 'pause',
        "args": [7]
    },
    {
        "identifier": 'ACTION_207_jmp_25',
        "command": 'jmp',
        "args": ['ACTION_207_set_sprite_sequence_2']
    },
    {
        "identifier": 'ACTION_207_pause_26',
        "command": 'pause',
        "args": [4]
    },
    {
        "identifier": 'ACTION_207_jmp_27',
        "command": 'jmp',
        "args": ['ACTION_207_set_sprite_sequence_2']
    },
    {
        "identifier": 'ACTION_207_pause_28',
        "command": 'pause',
        "args": [9]
    },
    {
        "identifier": 'ACTION_207_jmp_29',
        "command": 'jmp',
        "args": ['ACTION_207_set_sprite_sequence_2']
    }
]
