from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data.eventtables import RadialDirections, AreaObjects, NPCPackets, Sounds, Coords, CoordUnits, Rooms
script = [
    {
        "identifier": 'ACTION_716_play_sound_0',
        "command": 'play_sound',
        "args": [Sounds._085_FLOWER, 4]
    },
    {
        "identifier": 'ACTION_716_db_1',
        "command": 'db',
        "args": [0x97, 0x1c]
    },
    {
        "identifier": 'ACTION_716_set_vram_priority_2',
        "command": 'set_vram_priority',
        "args": [VramPriority.PRIORITY_3]
    },
    {
        "identifier": 'ACTION_716_set_priority_3',
        "command": 'set_priority',
        "args": [3]
    },
    {
        "identifier": 'ACTION_716_set_animation_speed_4',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.FASTEST, [_0x10Flags.WALKING]]
    },
    {
        "identifier": 'ACTION_716_add_z_coord_1_step_5',
        "command": 'add_z_coord_1_step'
    },
    {
        "identifier": 'ACTION_716_visibility_on_6',
        "command": 'visibility_on'
    },
    {
        "identifier": 'ACTION_716_set_animation_speed_7',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
    },
    {
        "identifier": 'ACTION_716_floating_off_8',
        "command": 'floating_off'
    },
    {
        "identifier": 'ACTION_716_jump_to_height_9',
        "command": 'jump_to_height',
        "args": [64]
    },
    {
        "identifier": 'ACTION_716_shift_southeast_pixels_10',
        "command": 'shift_southeast_pixels',
        "args": [12]
    },
    {
        "identifier": 'ACTION_716_floating_off_11',
        "command": 'floating_off'
    },
    {
        "identifier": 'ACTION_716_set_animation_speed_12',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.WALKING]]
    },
    {
        "identifier": 'ACTION_716_add_z_coord_1_step_13',
        "command": 'add_z_coord_1_step'
    },
    {
        "identifier": 'ACTION_716_start_loop_n_times_14',
        "command": 'start_loop_n_times',
        "args": [8]
    },
    {
        "identifier": 'ACTION_716_visibility_on_15',
        "command": 'visibility_on'
    },
    {
        "identifier": 'ACTION_716_pause_16',
        "command": 'pause',
        "args": [4]
    },
    {
        "identifier": 'ACTION_716_visibility_off_17',
        "command": 'visibility_off'
    },
    {
        "identifier": 'ACTION_716_pause_18',
        "command": 'pause',
        "args": [1]
    },
    {
        "identifier": 'ACTION_716_end_loop_19',
        "command": 'end_loop'
    },
    {
        "identifier": 'ACTION_716_ret_20',
        "command": 'ret'
    }
]
