from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data.eventtables import RadialDirections, AreaObjects, NPCPackets, Sounds, Coords, CoordUnits, Rooms
script = [
    {
        "identifier": 'ACTION_678_set_700C_to_current_level_0',
        "command": 'set_700C_to_current_level'
    },
    {
        "identifier": 'ACTION_678_jmp_if_var_equals_short_1',
        "command": 'jmp_if_var_equals_short',
        "args": [0x700c, 22, 'ACTION_678_set_sprite_sequence_7']
    },
    {
        "identifier": 'ACTION_678_sequence_looping_on_2',
        "command": 'sequence_looping_on'
    },
    {
        "identifier": 'ACTION_678_set_animation_speed_3',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.FAST, [_0x10Flags.SEQUENCE]]
    },
    {
        "identifier": 'ACTION_678_pause_4',
        "command": 'pause',
        "args": [32]
    },
    {
        "identifier": 'ACTION_678_set_animation_speed_5',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.SLOW, [_0x10Flags.SEQUENCE]]
    },
    {
        "identifier": 'ACTION_678_ret_6',
        "command": 'ret'
    },
    {
        "identifier": 'ACTION_678_set_sprite_sequence_7',
        "command": 'set_sprite_sequence',
        "args": [0, inc_sprite=0, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
    },
    {
        "identifier": 'ACTION_678_pause_8',
        "command": 'pause',
        "args": [40]
    },
    {
        "identifier": 'ACTION_678_set_sprite_sequence_9',
        "command": 'set_sprite_sequence',
        "args": [1, inc_sprite=0, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
    },
    {
        "identifier": 'ACTION_678_pause_10',
        "command": 'pause',
        "args": [4]
    },
    {
        "identifier": 'ACTION_678_set_sprite_sequence_11',
        "command": 'set_sprite_sequence',
        "args": [2, inc_sprite=0, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
    },
    {
        "identifier": 'ACTION_678_pause_12',
        "command": 'pause',
        "args": [8]
    },
    {
        "identifier": 'ACTION_678_jmp_13',
        "command": 'jmp',
        "args": ['ACTION_678_set_sprite_sequence_7']
    }
]
