from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data import items
script = [
    {
        "identifier": 'EVENT_297_jmp_if_bit_set_0',
        "command": 'jmp_if_bit_set',
        "args": [0x709c, 1, 'EVENT_297_jmp_to_event_8']
    },
    {
        "identifier": 'EVENT_297_jmp_if_bit_set_1',
        "command": 'jmp_if_bit_set',
        "args": [0x7081, 5, 'EVENT_297_run_dialog_6']
    },
    {
        "identifier": 'EVENT_297_jmp_fork_mario_on_object_2',
        "command": 'jmp_fork_mario_on_object',
        "args": ['EVENT_297_set_7000_to_current_level_9', 'EVENT_297_set_7000_to_current_level_9']
    },
    {
        "identifier": 'EVENT_297_run_dialog_3',
        "command": 'run_dialog',
        "args": [534, AreaObjects.MEM_70A8, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]]
    },
    {
        "identifier": 'EVENT_297_jmp_if_bit_set_4',
        "command": 'jmp_if_bit_set',
        "args": [0x7053, 6, 'EVENT_297_jmp_to_event_8']
    },
    {
        "identifier": 'EVENT_297_ret_5',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_297_run_dialog_6',
        "command": 'run_dialog',
        "args": [607, AreaObjects.MEM_70A8, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]]
    },
    {
        "identifier": 'EVENT_297_ret_7',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_297_jmp_to_event_8',
        "command": 'jmp_to_event',
        "args": [934]
    },
    {
        "identifier": 'EVENT_297_set_7000_to_current_level_9',
        "command": 'set_7000_to_current_level'
    },
    {
        "identifier": 'EVENT_297_jmp_if_var_equals_short_10',
        "command": 'jmp_if_var_equals_short',
        "args": [0x7000, 495, 'EVENT_256_ret_0']
    },
    {
        "identifier": 'EVENT_297_jmp_if_var_equals_short_11',
        "command": 'jmp_if_var_equals_short',
        "args": [0x7000, 51, 'EVENT_256_ret_0']
    },
    {
        "identifier": 'EVENT_297_resume_action_script_12',
        "command": 'resume_action_script',
        "args": [AreaObjects.MEM_70A8]
    },
    {
        "identifier": 'EVENT_297_pause_13',
        "command": 'pause',
        "args": [1]
    },
    {
        "identifier": 'EVENT_297_jmp_if_mario_in_air_14',
        "command": 'jmp_if_mario_in_air',
        "args": ['EVENT_297_pause_13']
    },
    {
        "identifier": 'EVENT_297_enable_controls_until_return_15',
        "command": 'enable_controls_until_return',
        "args": [[ControllerDirections.LEFT, ControllerDirections.RIGHT, ControllerDirections.DOWN, ControllerDirections.UP, ControllerDirections.A, ControllerDirections.Y, ControllerDirections.B]]
    },
    {
        "identifier": 'EVENT_297_start_loop_n_times_16',
        "command": 'start_loop_n_times',
        "args": [239]
    },
    {
        "identifier": 'EVENT_297_pause_17',
        "command": 'pause',
        "args": [1]
    },
    {
        "identifier": 'EVENT_297_jmp_if_mario_in_air_18',
        "command": 'jmp_if_mario_in_air',
        "args": ['EVENT_256_ret_0']
    },
    {
        "identifier": 'EVENT_297_end_loop_19',
        "command": 'end_loop'
    },
    {
        "identifier": 'EVENT_297_enable_controls_until_return_20',
        "command": 'enable_controls_until_return',
        "args": [[]]
    },
    {
        "identifier": 'EVENT_297_set_7000_to_current_level_21',
        "command": 'set_7000_to_current_level'
    },
    {
        "identifier": 'EVENT_297_jmp_if_var_equals_short_22',
        "command": 'jmp_if_var_equals_short',
        "args": [0x7000, 191, 'EVENT_297_set_7000_to_object_coord_25']
    },
    {
        "identifier": 'EVENT_297_set_7000_to_object_coord_23',
        "command": 'set_7000_to_object_coord',
        "args": [AreaObjects.NPC_6, Coords.F]
    },
    {
        "identifier": 'EVENT_297_jmp_24',
        "command": 'jmp',
        "args": ['EVENT_297_set_short_mem_26']
    },
    {
        "identifier": 'EVENT_297_set_7000_to_object_coord_25',
        "command": 'set_7000_to_object_coord',
        "args": [AreaObjects.NPC_7, Coords.F]
    },
    {
        "identifier": 'EVENT_297_set_short_mem_26',
        "command": 'set_short_mem',
        "args": [0x700c, 0x7000]
    },
    {
        "identifier": 'EVENT_297_action_queue_async_27',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_297_action_queue_async_27_SUBSCRIPT_sequence_playback_off_0',
                "command": 'sequence_playback_off'
            },
            {
                "identifier": 'EVENT_297_action_queue_async_27_SUBSCRIPT_jump_to_height_1',
                "command": 'jump_to_height',
                "args": [64]
            },
            {
                "identifier": 'EVENT_297_action_queue_async_27_SUBSCRIPT_jmp_if_var_equals_short_2',
                "command": 'jmp_if_var_equals_short',
                "args": [0x700c, 1, 'EVENT_297_action_queue_async_27_SUBSCRIPT_walk_1_step_southwest_7']
            },
            {
                "identifier": 'EVENT_297_action_queue_async_27_SUBSCRIPT_jmp_if_var_equals_short_3',
                "command": 'jmp_if_var_equals_short',
                "args": [0x700c, 5, 'EVENT_297_action_queue_async_27_SUBSCRIPT_walk_1_step_northeast_9']
            },
            {
                "identifier": 'EVENT_297_action_queue_async_27_SUBSCRIPT_jmp_if_var_equals_short_4',
                "command": 'jmp_if_var_equals_short',
                "args": [0x700c, 3, 'EVENT_297_action_queue_async_27_SUBSCRIPT_walk_1_step_northwest_11']
            },
            {
                "identifier": 'EVENT_297_action_queue_async_27_SUBSCRIPT_walk_1_step_southeast_5',
                "command": 'walk_1_step_southeast'
            },
            {
                "identifier": 'EVENT_297_action_queue_async_27_SUBSCRIPT_jmp_6',
                "command": 'jmp',
                "args": ['EVENT_297_action_queue_async_27_SUBSCRIPT_pause_12']
            },
            {
                "identifier": 'EVENT_297_action_queue_async_27_SUBSCRIPT_walk_1_step_southwest_7',
                "command": 'walk_1_step_southwest'
            },
            {
                "identifier": 'EVENT_297_action_queue_async_27_SUBSCRIPT_jmp_8',
                "command": 'jmp',
                "args": ['EVENT_297_action_queue_async_27_SUBSCRIPT_pause_12']
            },
            {
                "identifier": 'EVENT_297_action_queue_async_27_SUBSCRIPT_walk_1_step_northeast_9',
                "command": 'walk_1_step_northeast'
            },
            {
                "identifier": 'EVENT_297_action_queue_async_27_SUBSCRIPT_jmp_10',
                "command": 'jmp',
                "args": ['EVENT_297_action_queue_async_27_SUBSCRIPT_pause_12']
            },
            {
                "identifier": 'EVENT_297_action_queue_async_27_SUBSCRIPT_walk_1_step_northwest_11',
                "command": 'walk_1_step_northwest'
            },
            {
                "identifier": 'EVENT_297_action_queue_async_27_SUBSCRIPT_pause_12',
                "command": 'pause',
                "args": [1]
            },
            {
                "identifier": 'EVENT_297_action_queue_async_27_SUBSCRIPT_jmp_if_mario_in_air_13',
                "command": 'jmp_if_mario_in_air',
                "args": ['EVENT_297_action_queue_async_27_SUBSCRIPT_pause_12']
            },
            {
                "identifier": 'EVENT_297_action_queue_async_27_SUBSCRIPT_sequence_playback_on_14',
                "command": 'sequence_playback_on'
            },
            {
                "identifier": 'EVENT_297_action_queue_async_27_SUBSCRIPT_start_loop_n_times_15',
                "command": 'start_loop_n_times',
                "args": [7]
            },
            {
                "identifier": 'EVENT_297_action_queue_async_27_SUBSCRIPT_turn_clockwise_45_degrees_n_times_16',
                "command": 'turn_clockwise_45_degrees_n_times',
                "args": [1]
            },
            {
                "identifier": 'EVENT_297_action_queue_async_27_SUBSCRIPT_pause_17',
                "command": 'pause',
                "args": [2]
            },
            {
                "identifier": 'EVENT_297_action_queue_async_27_SUBSCRIPT_end_loop_18',
                "command": 'end_loop'
            },
            {
                "identifier": 'EVENT_297_action_queue_async_27_SUBSCRIPT_turn_clockwise_45_degrees_n_times_19',
                "command": 'turn_clockwise_45_degrees_n_times',
                "args": [1]
            },
            {
                "identifier": 'EVENT_297_action_queue_async_27_SUBSCRIPT_pause_20',
                "command": 'pause',
                "args": [2]
            },
            {
                "identifier": 'EVENT_297_action_queue_async_27_SUBSCRIPT_set_700C_to_object_coord_21',
                "command": 'set_700C_to_object_coord',
                "args": [AreaObjects.MARIO, Coords.F]
            },
            {
                "identifier": 'EVENT_297_action_queue_async_27_SUBSCRIPT_jmp_if_var_equals_short_22',
                "command": 'jmp_if_var_equals_short',
                "args": [0x700c, 7, 'EVENT_297_action_queue_async_27_SUBSCRIPT_start_loop_n_times_24']
            },
            {
                "identifier": 'EVENT_297_action_queue_async_27_SUBSCRIPT_jmp_23',
                "command": 'jmp',
                "args": ['EVENT_297_action_queue_async_27_SUBSCRIPT_turn_clockwise_45_degrees_n_times_19']
            },
            {
                "identifier": 'EVENT_297_action_queue_async_27_SUBSCRIPT_start_loop_n_times_24',
                "command": 'start_loop_n_times',
                "args": [2]
            },
            {
                "identifier": 'EVENT_297_action_queue_async_27_SUBSCRIPT_set_sprite_sequence_25',
                "command": 'set_sprite_sequence',
                "args": [19, 2, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_297_action_queue_async_27_SUBSCRIPT_pause_26',
                "command": 'pause',
                "args": [4]
            },
            {
                "identifier": 'EVENT_297_action_queue_async_27_SUBSCRIPT_set_sprite_sequence_27',
                "command": 'set_sprite_sequence',
                "args": [3, 2, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_297_action_queue_async_27_SUBSCRIPT_pause_28',
                "command": 'pause',
                "args": [4]
            },
            {
                "identifier": 'EVENT_297_action_queue_async_27_SUBSCRIPT_set_sprite_sequence_29',
                "command": 'set_sprite_sequence',
                "args": [23, 2, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_297_action_queue_async_27_SUBSCRIPT_pause_30',
                "command": 'pause',
                "args": [6]
            },
            {
                "identifier": 'EVENT_297_action_queue_async_27_SUBSCRIPT_set_sprite_sequence_31',
                "command": 'set_sprite_sequence',
                "args": [3, 2, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_297_action_queue_async_27_SUBSCRIPT_pause_32',
                "command": 'pause',
                "args": [2]
            },
            {
                "identifier": 'EVENT_297_action_queue_async_27_SUBSCRIPT_end_loop_33',
                "command": 'end_loop'
            },
            {
                "identifier": 'EVENT_297_action_queue_async_27_SUBSCRIPT_set_sprite_sequence_34',
                "command": 'set_sprite_sequence',
                "args": [19, 2, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_297_action_queue_async_27_SUBSCRIPT_pause_35',
                "command": 'pause',
                "args": [2]
            },
            {
                "identifier": 'EVENT_297_action_queue_async_27_SUBSCRIPT_play_sound_36',
                "command": 'play_sound',
                "args": [Sounds._022_CLOSE_DOOR, 4]
            },
            {
                "identifier": 'EVENT_297_action_queue_async_27_SUBSCRIPT_set_sprite_sequence_37',
                "command": 'set_sprite_sequence',
                "args": [8, 2, [_0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_297_action_queue_async_27_SUBSCRIPT_pause_38',
                "command": 'pause',
                "args": [30]
            },
            {
                "identifier": 'EVENT_297_action_queue_async_27_SUBSCRIPT_reset_properties_39',
                "command": 'reset_properties'
            }
        ]
    },
    {
        "identifier": 'EVENT_297_pause_28',
        "command": 'pause',
        "args": [10]
    },
    {
        "identifier": 'EVENT_297_set_action_script_async_29',
        "command": 'set_action_script_async',
        "args": [AreaObjects.MARIO, 671]
    },
    {
        "identifier": 'EVENT_297_set_action_script_sync_30',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.MARIO, 395]
    },
    {
        "identifier": 'EVENT_297_ret_31',
        "command": 'ret'
    }
]
