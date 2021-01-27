from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data.eventtables import RadialDirections, AreaObjects, NPCPackets, Sounds, Coords, CoordUnits, Rooms
script = [
    {
        "identifier": 'ACTION_91_set_animation_speed_0',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.FAST, [_0x10Flags.SEQUENCE]]
    },
    {
        "identifier": 'ACTION_91_jmp_if_bit_set_1',
        "command": 'jmp_if_bit_set',
        "args": [0x7044, 6, 'ACTION_91_visibility_on_3']
    },
    {
        "identifier": 'ACTION_91_play_sound_2',
        "command": 'play_sound',
        "args": [Sounds._050_WATER_DROPLET, 4]
    },
    {
        "identifier": 'ACTION_91_visibility_on_3',
        "command": 'visibility_on'
    },
    {
        "identifier": 'ACTION_91_set_sprite_sequence_4',
        "command": 'set_sprite_sequence',
        "args": [10, 0, [_0x08Flags.READ_AS_SEQUENCE]]
    },
    {
        "identifier": 'ACTION_91_pause_5',
        "command": 'pause',
        "args": [10]
    },
    {
        "identifier": 'ACTION_91_set_sprite_sequence_6',
        "command": 'set_sprite_sequence',
        "args": [0, 0, [_0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
    },
    {
        "identifier": 'ACTION_91_pause_7',
        "command": 'pause',
        "args": [5]
    },
    {
        "identifier": 'ACTION_91_set_animation_speed_8',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING]]
    },
    {
        "identifier": 'ACTION_91_shift_southeast_pixels_9',
        "command": 'shift_southeast_pixels',
        "args": [12]
    },
    {
        "identifier": 'ACTION_91_set_animation_speed_10',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
    },
    {
        "identifier": 'ACTION_91_shift_southeast_pixels_11',
        "command": 'shift_southeast_pixels',
        "args": [11]
    },
    {
        "identifier": 'ACTION_91_set_animation_speed_12',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.SLOW, [_0x10Flags.WALKING]]
    },
    {
        "identifier": 'ACTION_91_shift_southeast_pixels_13',
        "command": 'shift_southeast_pixels',
        "args": [9]
    },
    {
        "identifier": 'ACTION_91_jmp_14',
        "command": 'jmp',
        "args": ['ACTION_154_fixed_f_coord_on_0']
    }
]
