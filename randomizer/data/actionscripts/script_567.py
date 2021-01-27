from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data.eventtables import RadialDirections, AreaObjects, NPCPackets, Sounds, Coords, CoordUnits, Rooms
script = [
    {
        "identifier": 'ACTION_567_clear_bit_0',
        "command": 'clear_bit',
        "args": [0x7043, 6]
    },
    {
        "identifier": 'ACTION_567_set_sprite_sequence_1',
        "command": 'set_sprite_sequence',
        "args": [1, 0, [_0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
    },
    {
        "identifier": 'ACTION_567_pause_2',
        "command": 'pause',
        "args": [10]
    },
    {
        "identifier": 'ACTION_567_set_animation_speed_3',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING]]
    },
    {
        "identifier": 'ACTION_567_shift_northeast_pixels_4',
        "command": 'shift_northeast_pixels',
        "args": [16]
    },
    {
        "identifier": 'ACTION_567_set_animation_speed_5',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
    },
    {
        "identifier": 'ACTION_567_shift_northeast_pixels_6',
        "command": 'shift_northeast_pixels',
        "args": [5]
    },
    {
        "identifier": 'ACTION_567_set_animation_speed_7',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.SLOW, [_0x10Flags.WALKING]]
    },
    {
        "identifier": 'ACTION_567_shift_northeast_pixels_8',
        "command": 'shift_northeast_pixels',
        "args": [2]
    },
    {
        "identifier": 'ACTION_567_play_sound_9',
        "command": 'play_sound',
        "args": [Sounds._050_WATER_DROPLET, 4]
    },
    {
        "identifier": 'ACTION_567_set_sprite_sequence_10',
        "command": 'set_sprite_sequence',
        "args": [10, 0, [_0x08Flags.READ_AS_SEQUENCE]]
    },
    {
        "identifier": 'ACTION_567_pause_11',
        "command": 'pause',
        "args": [10]
    },
    {
        "identifier": 'ACTION_567_visibility_off_12',
        "command": 'visibility_off'
    },
    {
        "identifier": 'ACTION_567_ret_13',
        "command": 'ret'
    }
]
