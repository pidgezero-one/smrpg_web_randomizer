from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data.eventtables import RadialDirections, AreaObjects, NPCPackets, Sounds, Coords, CoordUnits, Rooms
script = [
    {
        "identifier": 'ACTION_929_set_bit_0',
        "command": 'set_bit',
        "args": [0x7044, 6]
    },
    {
        "identifier": 'ACTION_929_jmp_if_var_equals_byte_1',
        "command": 'jmp_if_var_equals_byte',
        "args": [0x70af, 6, 'ACTION_929_play_sound_7']
    },
    {
        "identifier": 'ACTION_929_jmp_if_var_equals_byte_2',
        "command": 'jmp_if_var_equals_byte',
        "args": [0x70af, 7, 'ACTION_929_set_sprite_sequence_10']
    },
    {
        "identifier": 'ACTION_929_jmp_if_var_equals_byte_3',
        "command": 'jmp_if_var_equals_byte',
        "args": [0x70af, 135, 'ACTION_929_set_sprite_sequence_12']
    },
    {
        "identifier": 'ACTION_929_set_animation_speed_4',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.FAST, [_0x10Flags.SEQUENCE]]
    },
    {
        "identifier": 'ACTION_929_set_sprite_sequence_5',
        "command": 'set_sprite_sequence',
        "args": [4, inc_sprite=0, flags=[_0x08Flags.LOOPING_OFF, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
    },
    {
        "identifier": 'ACTION_929_jmp_6',
        "command": 'jmp',
        "args": ['ACTION_929_pause_14']
    },
    {
        "identifier": 'ACTION_929_play_sound_7',
        "command": 'play_sound',
        "args": [Sounds._120_METAL_BOLT_STRIKE, 4]
    },
    {
        "identifier": 'ACTION_929_set_sprite_sequence_8',
        "command": 'set_sprite_sequence',
        "args": [6, inc_sprite=0, flags=[_0x08Flags.LOOPING_OFF, _0x08Flags.READ_AS_SEQUENCE]]
    },
    {
        "identifier": 'ACTION_929_jmp_9',
        "command": 'jmp',
        "args": ['ACTION_929_pause_14']
    },
    {
        "identifier": 'ACTION_929_set_sprite_sequence_10',
        "command": 'set_sprite_sequence',
        "args": [7, inc_sprite=0, flags=[_0x08Flags.LOOPING_OFF, _0x08Flags.READ_AS_SEQUENCE]]
    },
    {
        "identifier": 'ACTION_929_jmp_11',
        "command": 'jmp',
        "args": ['ACTION_929_pause_14']
    },
    {
        "identifier": 'ACTION_929_set_sprite_sequence_12',
        "command": 'set_sprite_sequence',
        "args": [7, inc_sprite=0, flags=[_0x08Flags.LOOPING_OFF, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
    },
    {
        "identifier": 'ACTION_929_jmp_13',
        "command": 'jmp',
        "args": ['ACTION_929_pause_14']
    },
    {
        "identifier": 'ACTION_929_pause_14',
        "command": 'pause',
        "args": [1]
    },
    {
        "identifier": 'ACTION_929_jmp_if_bit_set_15',
        "command": 'jmp_if_bit_set',
        "args": [0x7044, 6, 'ACTION_929_pause_14']
    },
    {
        "identifier": 'ACTION_929_pause_16',
        "command": 'pause',
        "args": [1]
    },
    {
        "identifier": 'ACTION_929_ret_17',
        "command": 'ret'
    }
]
