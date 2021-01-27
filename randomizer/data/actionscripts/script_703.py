from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data.eventtables import RadialDirections, AreaObjects, NPCPackets, Sounds, Coords, CoordUnits, Rooms
script = [
    {
        "identifier": 'ACTION_703_jmp_if_random_above_66_0',
        "command": 'jmp_if_random_above_66',
        "args": [0x8191, 'ACTION_703_set_700C_to_pressed_button_18']
    },
    {
        "identifier": 'ACTION_703_jmp_if_random_above_128_1',
        "command": 'jmp_if_random_above_128',
        "args": ['ACTION_703_set_700C_to_pressed_button_10']
    },
    {
        "identifier": 'ACTION_703_set_700C_to_pressed_button_2',
        "command": 'set_700C_to_pressed_button'
    },
    {
        "identifier": 'ACTION_703_jmp_if_700C_equals_short_3',
        "command": 'jmp_if_700C_equals_short',
        "args": [20, 'ACTION_703_set_sprite_sequence_7']
    },
    {
        "identifier": 'ACTION_703_set_sprite_sequence_4',
        "command": 'set_sprite_sequence',
        "args": [3, 0, [_0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
    },
    {
        "identifier": 'ACTION_703_pause_5',
        "command": 'pause',
        "args": [58]
    },
    {
        "identifier": 'ACTION_703_jmp_6',
        "command": 'jmp',
        "args": ['ACTION_703_jmp_if_random_above_66_0']
    },
    {
        "identifier": 'ACTION_703_set_sprite_sequence_7',
        "command": 'set_sprite_sequence',
        "args": [3, 0, [_0x08Flags.READ_AS_SEQUENCE]]
    },
    {
        "identifier": 'ACTION_703_pause_8',
        "command": 'pause',
        "args": [58]
    },
    {
        "identifier": 'ACTION_703_jmp_9',
        "command": 'jmp',
        "args": ['ACTION_703_jmp_if_random_above_66_0']
    },
    {
        "identifier": 'ACTION_703_set_700C_to_pressed_button_10',
        "command": 'set_700C_to_pressed_button'
    },
    {
        "identifier": 'ACTION_703_jmp_if_700C_equals_short_11',
        "command": 'jmp_if_700C_equals_short',
        "args": [20, 'ACTION_703_set_sprite_sequence_15']
    },
    {
        "identifier": 'ACTION_703_set_sprite_sequence_12',
        "command": 'set_sprite_sequence',
        "args": [4, 0, [_0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
    },
    {
        "identifier": 'ACTION_703_pause_13',
        "command": 'pause',
        "args": [56]
    },
    {
        "identifier": 'ACTION_703_jmp_14',
        "command": 'jmp',
        "args": ['ACTION_703_jmp_if_random_above_66_0']
    },
    {
        "identifier": 'ACTION_703_set_sprite_sequence_15',
        "command": 'set_sprite_sequence',
        "args": [4, 0, [_0x08Flags.READ_AS_SEQUENCE]]
    },
    {
        "identifier": 'ACTION_703_pause_16',
        "command": 'pause',
        "args": [56]
    },
    {
        "identifier": 'ACTION_703_jmp_17',
        "command": 'jmp',
        "args": ['ACTION_703_jmp_if_random_above_66_0']
    },
    {
        "identifier": 'ACTION_703_set_700C_to_pressed_button_18',
        "command": 'set_700C_to_pressed_button'
    },
    {
        "identifier": 'ACTION_703_jmp_if_700C_equals_short_19',
        "command": 'jmp_if_700C_equals_short',
        "args": [20, 'ACTION_703_set_sprite_sequence_23']
    },
    {
        "identifier": 'ACTION_703_set_sprite_sequence_20',
        "command": 'set_sprite_sequence',
        "args": [0, 0, [_0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
    },
    {
        "identifier": 'ACTION_703_pause_21',
        "command": 'pause',
        "args": [112]
    },
    {
        "identifier": 'ACTION_703_jmp_22',
        "command": 'jmp',
        "args": ['ACTION_703_jmp_if_random_above_66_0']
    },
    {
        "identifier": 'ACTION_703_set_sprite_sequence_23',
        "command": 'set_sprite_sequence',
        "args": [0, 0, [_0x08Flags.READ_AS_SEQUENCE]]
    },
    {
        "identifier": 'ACTION_703_pause_24',
        "command": 'pause',
        "args": [112]
    },
    {
        "identifier": 'ACTION_703_jmp_25',
        "command": 'jmp',
        "args": ['ACTION_703_jmp_if_random_above_66_0']
    }
]
