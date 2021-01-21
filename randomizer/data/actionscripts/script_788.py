from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data.eventtables import RadialDirections, AreaObjects, NPCPackets, Sounds, Coords, CoordUnits, Rooms
script = [
    {
        "identifier": 'ACTION_788_fixed_f_coord_on_0',
        "command": 'fixed_f_coord_on'
    },
    {
        "identifier": 'ACTION_788_floating_off_1',
        "command": 'floating_off'
    },
    {
        "identifier": 'ACTION_788_set_animation_speed_2',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.WALKING]]
    },
    {
        "identifier": 'ACTION_788_object_memory_modify_bits_3',
        "command": 'object_memory_modify_bits',
        "args": [0x09, [5], [4, 6]]
    },
    {
        "identifier": 'ACTION_788_walk_1_step_northwest_4',
        "command": 'walk_1_step_northwest'
    },
    {
        "identifier": 'ACTION_788_sequence_looping_on_5',
        "command": 'sequence_looping_on'
    },
    {
        "identifier": 'ACTION_788_set_animation_speed_6',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.SEQUENCE]]
    },
    {
        "identifier": 'ACTION_788_pause_7',
        "command": 'pause',
        "args": [30]
    },
    {
        "identifier": 'ACTION_788_sequence_looping_off_8',
        "command": 'sequence_looping_off'
    },
    {
        "identifier": 'ACTION_788_sequence_playback_off_9',
        "command": 'sequence_playback_off'
    },
    {
        "identifier": 'ACTION_788_set_animation_speed_10',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
    },
    {
        "identifier": 'ACTION_788_shift_z_down_pixels_11',
        "command": 'shift_z_down_pixels',
        "args": [1]
    },
    {
        "identifier": 'ACTION_788_set_animation_speed_12',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING]]
    },
    {
        "identifier": 'ACTION_788_shift_z_down_pixels_13',
        "command": 'shift_z_down_pixels',
        "args": [2]
    },
    {
        "identifier": 'ACTION_788_set_animation_speed_14',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.WALKING]]
    },
    {
        "identifier": 'ACTION_788_shift_z_down_pixels_15',
        "command": 'shift_z_down_pixels',
        "args": [4]
    },
    {
        "identifier": 'ACTION_788_set_animation_speed_16',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.FASTEST, [_0x10Flags.WALKING]]
    },
    {
        "identifier": 'ACTION_788_shift_z_down_pixels_17',
        "command": 'shift_z_down_pixels',
        "args": [9]
    },
    {
        "identifier": 'ACTION_788_fixed_f_coord_on_18',
        "command": 'fixed_f_coord_on'
    },
    {
        "identifier": 'ACTION_788_shift_northwest_pixels_19',
        "command": 'shift_northwest_pixels',
        "args": [1]
    },
    {
        "identifier": 'ACTION_788_shift_southeast_pixels_20',
        "command": 'shift_southeast_pixels',
        "args": [1]
    },
    {
        "identifier": 'ACTION_788_jmp_21',
        "command": 'jmp',
        "args": ['ACTION_788_shift_northwest_pixels_19']
    }
]
