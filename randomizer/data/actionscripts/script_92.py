from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data.eventtables import RadialDirections, AreaObjects, NPCPackets, Sounds, Coords, CoordUnits, Rooms
script = [
    {
        "identifier": 'ACTION_92_set_animation_speed_0',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.FAST, [_0x10Flags.SEQUENCE]]
    },
    {
        "identifier": 'ACTION_92_jmp_if_bit_set_1',
        "command": 'jmp_if_bit_set',
        "args": [0x7044, 6, 'ACTION_92_visibility_on_3']
    },
    {
        "identifier": 'ACTION_92_play_sound_2',
        "command": 'play_sound',
        "args": [Sounds._050_WATER_DROPLET, 4]
    },
    {
        "identifier": 'ACTION_92_visibility_on_3',
        "command": 'visibility_on'
    },
    {
        "identifier": 'ACTION_92_set_sprite_sequence_4',
        "command": 'set_sprite_sequence',
        "args": [10, inc_sprite=0, flags=[_0x08Flags.READ_AS_SEQUENCE]]
    },
    {
        "identifier": 'ACTION_92_pause_5',
        "command": 'pause',
        "args": [10]
    },
    {
        "identifier": 'ACTION_92_set_sprite_sequence_6',
        "command": 'set_sprite_sequence',
        "args": [1, inc_sprite=0, flags=[_0x08Flags.READ_AS_SEQUENCE]]
    },
    {
        "identifier": 'ACTION_92_pause_7',
        "command": 'pause',
        "args": [5]
    },
    {
        "identifier": 'ACTION_92_set_animation_speed_8',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING]]
    },
    {
        "identifier": 'ACTION_92_shift_northwest_pixels_9',
        "command": 'shift_northwest_pixels',
        "args": [9]
    },
    {
        "identifier": 'ACTION_92_set_animation_speed_10',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
    },
    {
        "identifier": 'ACTION_92_shift_northwest_pixels_11',
        "command": 'shift_northwest_pixels',
        "args": [11]
    },
    {
        "identifier": 'ACTION_92_set_animation_speed_12',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.SLOW, [_0x10Flags.WALKING]]
    },
    {
        "identifier": 'ACTION_92_shift_northwest_pixels_13',
        "command": 'shift_northwest_pixels',
        "args": [9]
    },
    {
        "identifier": 'ACTION_92_jmp_14',
        "command": 'jmp',
        "args": ['ACTION_154_fixed_f_coord_on_0']
    }
]
