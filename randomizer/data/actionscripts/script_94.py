from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data.eventtables import RadialDirections, AreaObjects, NPCPackets, Sounds, Coords, CoordUnits, Rooms
script = [
    {
        "identifier": 'ACTION_94_set_animation_speed_0',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.FAST, [_0x10Flags.SEQUENCE]]
    },
    {
        "identifier": 'ACTION_94_visibility_on_1',
        "command": 'visibility_on'
    },
    {
        "identifier": 'ACTION_94_play_sound_2',
        "command": 'play_sound',
        "args": [Sounds._050_WATER_DROPLET, 4]
    },
    {
        "identifier": 'ACTION_94_set_sprite_sequence_3',
        "command": 'set_sprite_sequence',
        "args": [10, 0, [_0x08Flags.READ_AS_SEQUENCE]]
    },
    {
        "identifier": 'ACTION_94_pause_4',
        "command": 'pause',
        "args": [12]
    },
    {
        "identifier": 'ACTION_94_set_sprite_sequence_5',
        "command": 'set_sprite_sequence',
        "args": [0, 0, [_0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
    },
    {
        "identifier": 'ACTION_94_play_sound_6',
        "command": 'play_sound',
        "args": [Sounds._043_POP_UP_FROM_WATER, 4]
    },
    {
        "identifier": 'ACTION_94_pause_7',
        "command": 'pause',
        "args": [15]
    },
    {
        "identifier": 'ACTION_94_set_sprite_sequence_8',
        "command": 'set_sprite_sequence',
        "args": [0, 0, [_0x08Flags.READ_AS_SEQUENCE]]
    },
    {
        "identifier": 'ACTION_94_play_sound_9',
        "command": 'play_sound',
        "args": [Sounds._043_POP_UP_FROM_WATER, 4]
    },
    {
        "identifier": 'ACTION_94_pause_10',
        "command": 'pause',
        "args": [15]
    },
    {
        "identifier": 'ACTION_94_set_sprite_sequence_11',
        "command": 'set_sprite_sequence',
        "args": [0, 0, [_0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
    },
    {
        "identifier": 'ACTION_94_play_sound_12',
        "command": 'play_sound',
        "args": [Sounds._043_POP_UP_FROM_WATER, 4]
    },
    {
        "identifier": 'ACTION_94_pause_13',
        "command": 'pause',
        "args": [15]
    },
    {
        "identifier": 'ACTION_94_set_sprite_sequence_14',
        "command": 'set_sprite_sequence',
        "args": [0, 0, [_0x08Flags.READ_AS_SEQUENCE]]
    },
    {
        "identifier": 'ACTION_94_play_sound_15',
        "command": 'play_sound',
        "args": [Sounds._043_POP_UP_FROM_WATER, 4]
    },
    {
        "identifier": 'ACTION_94_jmp_16',
        "command": 'jmp',
        "args": ['ACTION_154_fixed_f_coord_on_0']
    },
    {
        "identifier": 'ACTION_94_ret_17',
        "command": 'ret'
    }
]
