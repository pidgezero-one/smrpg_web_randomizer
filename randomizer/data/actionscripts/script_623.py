from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data.eventtables import RadialDirections, AreaObjects, NPCPackets, Sounds, Coords, CoordUnits, Rooms
script = [
    {
        "identifier": 'ACTION_623_visibility_off_0',
        "command": 'visibility_off'
    },
    {
        "identifier": 'ACTION_623_set_vram_priority_1',
        "command": 'set_vram_priority',
        "args": [VramPriority.OBJECT_OVERLAPS_MARIO_ON_ALL_SIDES]
    },
    {
        "identifier": 'ACTION_623_set_animation_speed_2',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.FASTEST, [_0x10Flags.WALKING]]
    },
    {
        "identifier": 'ACTION_623_shift_west_pixels_3',
        "command": 'shift_west_pixels',
        "args": [20]
    },
    {
        "identifier": 'ACTION_623_shift_z_up_pixels_4',
        "command": 'shift_z_up_pixels',
        "args": [8]
    },
    {
        "identifier": 'ACTION_623_set_sprite_sequence_5',
        "command": 'set_sprite_sequence',
        "args": [1, inc_sprite=0, flags=[_0x08Flags.READ_AS_SEQUENCE]]
    },
    {
        "identifier": 'ACTION_623_visibility_on_6',
        "command": 'visibility_on'
    },
    {
        "identifier": 'ACTION_623_start_loop_n_times_7',
        "command": 'start_loop_n_times',
        "args": [7]
    },
    {
        "identifier": 'ACTION_623_visibility_off_8',
        "command": 'visibility_off'
    },
    {
        "identifier": 'ACTION_623_pause_9',
        "command": 'pause',
        "args": [2]
    },
    {
        "identifier": 'ACTION_623_visibility_on_10',
        "command": 'visibility_on'
    },
    {
        "identifier": 'ACTION_623_pause_11',
        "command": 'pause',
        "args": [2]
    },
    {
        "identifier": 'ACTION_623_end_loop_12',
        "command": 'end_loop'
    },
    {
        "identifier": 'ACTION_623_set_animation_speed_13',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.VERY_SLOW, [_0x10Flags.WALKING]]
    },
    {
        "identifier": 'ACTION_623_shift_southwest_pixels_14',
        "command": 'shift_southwest_pixels',
        "args": [3]
    },
    {
        "identifier": 'ACTION_623_set_animation_speed_15',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.SLOW, [_0x10Flags.WALKING]]
    },
    {
        "identifier": 'ACTION_623_shift_southwest_pixels_16',
        "command": 'shift_southwest_pixels',
        "args": [3]
    },
    {
        "identifier": 'ACTION_623_set_vram_priority_17',
        "command": 'set_vram_priority',
        "args": [VramPriority.NORMAL]
    },
    {
        "identifier": 'ACTION_623_set_animation_speed_18',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
    },
    {
        "identifier": 'ACTION_623_shift_southwest_steps_19',
        "command": 'shift_southwest_steps',
        "args": [2]
    },
    {
        "identifier": 'ACTION_623_set_animation_speed_20',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING]]
    },
    {
        "identifier": 'ACTION_623_shift_southwest_steps_21',
        "command": 'shift_southwest_steps',
        "args": [4]
    },
    {
        "identifier": 'ACTION_623_visibility_off_22',
        "command": 'visibility_off'
    },
    {
        "identifier": 'ACTION_623_ret_23',
        "command": 'ret'
    }
]
