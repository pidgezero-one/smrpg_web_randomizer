from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data.eventtables import RadialDirections, AreaObjects, NPCPackets, Sounds, Coords, CoordUnits, Rooms
script = [
    {
        "identifier": 'ACTION_45_visibility_on_0',
        "command": 'visibility_on'
    },
    {
        "identifier": 'ACTION_45_pause_1',
        "command": 'pause',
        "args": [117]
    },
    {
        "identifier": 'ACTION_45_jmp_if_bit_set_2',
        "command": 'jmp_if_bit_set',
        "args": [0x7078, 7, 'ACTION_45_reset_properties_13']
    },
    {
        "identifier": 'ACTION_45_jump_to_height_3',
        "command": 'jump_to_height',
        "args": [108]
    },
    {
        "identifier": 'ACTION_45_shift_southwest_steps_4',
        "command": 'shift_southwest_steps',
        "args": [2]
    },
    {
        "identifier": 'ACTION_45_play_sound_5',
        "command": 'play_sound',
        "args": [Sounds._085_FLOWER, 4]
    },
    {
        "identifier": 'ACTION_45_start_loop_n_times_6',
        "command": 'start_loop_n_times',
        "args": [4]
    },
    {
        "identifier": 'ACTION_45_visibility_on_7',
        "command": 'visibility_on'
    },
    {
        "identifier": 'ACTION_45_pause_8',
        "command": 'pause',
        "args": [2]
    },
    {
        "identifier": 'ACTION_45_visibility_off_9',
        "command": 'visibility_off'
    },
    {
        "identifier": 'ACTION_45_pause_10',
        "command": 'pause',
        "args": [2]
    },
    {
        "identifier": 'ACTION_45_end_loop_11',
        "command": 'end_loop'
    },
    {
        "identifier": 'ACTION_45_ret_12',
        "command": 'ret'
    },
    {
        "identifier": 'ACTION_45_reset_properties_13',
        "command": 'reset_properties'
    },
    {
        "identifier": 'ACTION_45_set_animation_speed_14',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.SLOW, [_0x10Flags.WALKING]]
    },
    {
        "identifier": 'ACTION_45_set_animation_speed_15',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.FASTER, [_0x10Flags.SEQUENCE]]
    },
    {
        "identifier": 'ACTION_45_walk_1_step_east_16',
        "command": 'walk_1_step_east'
    },
    {
        "identifier": 'ACTION_45_walk_1_step_west_17',
        "command": 'walk_1_step_west'
    },
    {
        "identifier": 'ACTION_45_jmp_18',
        "command": 'jmp',
        "args": ['ACTION_45_reset_properties_13']
    }
]
