from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data.eventtables import RadialDirections, AreaObjects, NPCPackets, Sounds, Coords, CoordUnits, Rooms
script = [
    {
        "identifier": 'ACTION_800_pause_0',
        "command": 'pause',
        "args": [10]
    },
    {
        "identifier": 'ACTION_800_set_sprite_sequence_1',
        "command": 'set_sprite_sequence',
        "args": [0, 6, [_0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
    },
    {
        "identifier": 'ACTION_800_set_animation_speed_2',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.WALKING]]
    },
    {
        "identifier": 'ACTION_800_shift_northeast_pixels_3',
        "command": 'shift_northeast_pixels',
        "args": [1]
    },
    {
        "identifier": 'ACTION_800_start_loop_n_times_4',
        "command": 'start_loop_n_times',
        "args": [29]
    },
    {
        "identifier": 'ACTION_800_shift_southwest_pixels_5',
        "command": 'shift_southwest_pixels',
        "args": [2]
    },
    {
        "identifier": 'ACTION_800_shift_northeast_pixels_6',
        "command": 'shift_northeast_pixels',
        "args": [2]
    },
    {
        "identifier": 'ACTION_800_end_loop_7',
        "command": 'end_loop'
    },
    {
        "identifier": 'ACTION_800_shift_southwest_pixels_8',
        "command": 'shift_southwest_pixels',
        "args": [1]
    },
    {
        "identifier": 'ACTION_800_set_animation_speed_9',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING]]
    },
    {
        "identifier": 'ACTION_800_pause_10',
        "command": 'pause',
        "args": [16]
    },
    {
        "identifier": 'ACTION_800_reset_properties_11',
        "command": 'reset_properties'
    },
    {
        "identifier": 'ACTION_800_face_northwest_12',
        "command": 'face_northwest'
    },
    {
        "identifier": 'ACTION_800_ret_13',
        "command": 'ret'
    }
]
