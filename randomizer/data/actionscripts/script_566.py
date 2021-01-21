from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data.eventtables import RadialDirections, AreaObjects, NPCPackets, Sounds, Coords, CoordUnits, Rooms
script = [
    {
        "identifier": 'ACTION_566_set_bit_0',
        "command": 'set_bit',
        "args": [0x7043, 6]
    },
    {
        "identifier": 'ACTION_566_shirt_to_xy_coords_1',
        "command": 'shirt_to_xy_coords',
        "args": [7, 40]
    },
    {
        "identifier": 'ACTION_566_visibility_on_2',
        "command": 'visibility_on'
    },
    {
        "identifier": 'ACTION_566_set_animation_speed_3',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.FAST, [_0x10Flags.SEQUENCE]]
    },
    {
        "identifier": 'ACTION_566_play_sound_4',
        "command": 'play_sound',
        "args": [Sounds._050_WATER_DROPLET, 4]
    },
    {
        "identifier": 'ACTION_566_set_sprite_sequence_5',
        "command": 'set_sprite_sequence',
        "args": [10, inc_sprite=0, flags=[_0x08Flags.READ_AS_SEQUENCE]]
    },
    {
        "identifier": 'ACTION_566_pause_6',
        "command": 'pause',
        "args": [10]
    },
    {
        "identifier": 'ACTION_566_set_sprite_sequence_7',
        "command": 'set_sprite_sequence',
        "args": [0, inc_sprite=0, flags=[_0x08Flags.READ_AS_SEQUENCE]]
    },
    {
        "identifier": 'ACTION_566_pause_8',
        "command": 'pause',
        "args": [5]
    },
    {
        "identifier": 'ACTION_566_set_animation_speed_9',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING]]
    },
    {
        "identifier": 'ACTION_566_shift_southwest_pixels_10',
        "command": 'shift_southwest_pixels',
        "args": [16]
    },
    {
        "identifier": 'ACTION_566_set_animation_speed_11',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
    },
    {
        "identifier": 'ACTION_566_shift_southwest_pixels_12',
        "command": 'shift_southwest_pixels',
        "args": [5]
    },
    {
        "identifier": 'ACTION_566_set_animation_speed_13',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.SLOW, [_0x10Flags.WALKING]]
    },
    {
        "identifier": 'ACTION_566_shift_southwest_pixels_14',
        "command": 'shift_southwest_pixels',
        "args": [2]
    },
    {
        "identifier": 'ACTION_566_ret_15',
        "command": 'ret'
    }
]
