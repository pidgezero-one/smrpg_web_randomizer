from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data.eventtables import RadialDirections, AreaObjects, NPCPackets, Sounds, Coords, CoordUnits, Rooms
script = [
    {
        "identifier": 'ACTION_525_set_sprite_sequence_0',
        "command": 'set_sprite_sequence',
        "args": [6, 0, [_0x08Flags.READ_AS_MOLD]]
    },
    {
        "identifier": 'ACTION_525_set_animation_speed_1',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.SLOW, [_0x10Flags.WALKING]]
    },
    {
        "identifier": 'ACTION_525_shift_southeast_steps_2',
        "command": 'shift_southeast_steps',
        "args": [6]
    },
    {
        "identifier": 'ACTION_525_set_vram_priority_3',
        "command": 'set_vram_priority',
        "args": [VramPriority.NORMAL]
    },
    {
        "identifier": 'ACTION_525_shift_southeast_steps_4',
        "command": 'shift_southeast_steps',
        "args": [3]
    },
    {
        "identifier": 'ACTION_525_pause_5',
        "command": 'pause',
        "args": [120]
    },
    {
        "identifier": 'ACTION_525_pause_6',
        "command": 'pause',
        "args": [30]
    },
    {
        "identifier": 'ACTION_525_reset_properties_7',
        "command": 'reset_properties'
    },
    {
        "identifier": 'ACTION_525_fixed_f_coord_off_8',
        "command": 'fixed_f_coord_off'
    },
    {
        "identifier": 'ACTION_525_sequence_playback_on_9',
        "command": 'sequence_playback_on'
    },
    {
        "identifier": 'ACTION_525_set_animation_speed_10',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING]]
    },
    {
        "identifier": 'ACTION_525_set_animation_speed_11',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.SEQUENCE]]
    },
    {
        "identifier": 'ACTION_525_shift_southwest_pixels_12',
        "command": 'shift_southwest_pixels',
        "args": [6]
    },
    {
        "identifier": 'ACTION_525_set_priority_13',
        "command": 'set_priority',
        "args": [3]
    },
    {
        "identifier": 'ACTION_525_shift_northwest_steps_14',
        "command": 'shift_northwest_steps',
        "args": [10]
    },
    {
        "identifier": 'ACTION_525_set_bit_15',
        "command": 'set_bit',
        "args": [0x7044, 3]
    },
    {
        "identifier": 'ACTION_525_set_vram_priority_16',
        "command": 'set_vram_priority',
        "args": [VramPriority.MARIO_OVERLAPS_ON_ALL_SIDES]
    },
    {
        "identifier": 'ACTION_525_shift_northwest_steps_17',
        "command": 'shift_northwest_steps',
        "args": [5]
    },
    {
        "identifier": 'ACTION_525_visibility_off_18',
        "command": 'visibility_off'
    },
    {
        "identifier": 'ACTION_525_ret_19',
        "command": 'ret'
    }
]
