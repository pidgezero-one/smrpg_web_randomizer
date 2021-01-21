from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data import items
script = [
    {
        "identifier": 'EVENT_3372_move_script_to_background_thread_2_0',
        "command": 'move_script_to_background_thread_2'
    },
    {
        "identifier": 'EVENT_3372_jmp_fork_mario_on_object_1',
        "command": 'jmp_fork_mario_on_object',
        "args": ['EVENT_3372_ret_29', 'EVENT_3372_set_bit_7']
    },
    {
        "identifier": 'EVENT_3372_set_bit_2',
        "command": 'set_bit',
        "args": [0x7044, 7]
    },
    {
        "identifier": 'EVENT_3372_resume_action_script_3',
        "command": 'resume_action_script',
        "args": [AreaObjects.MEM_70A8]
    },
    {
        "identifier": 'EVENT_3372_action_queue_async_4',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_3372_action_queue_async_4_SUBSCRIPT_db_0',
                "command": 'db',
                "args": [0xfd, 0x9c, 0x69]
            },
            {
                "identifier": 'EVENT_3372_action_queue_async_4_SUBSCRIPT_set_700C_to_object_coord_1',
                "command": 'set_700C_to_object_coord',
                "args": [AreaObjects.DUMMY_0X07, Coords.F]
            },
            {
                "identifier": 'EVENT_3372_action_queue_async_4_SUBSCRIPT_jmp_if_var_equals_short_2',
                "command": 'jmp_if_var_equals_short',
                "args": [0x700c, 7, 'EVENT_3372_action_queue_async_4_SUBSCRIPT_set_sprite_sequence_10']
            },
            {
                "identifier": 'EVENT_3372_action_queue_async_4_SUBSCRIPT_jmp_if_var_equals_short_3',
                "command": 'jmp_if_var_equals_short',
                "args": [0x700c, 0, 'EVENT_3372_action_queue_async_4_SUBSCRIPT_set_sprite_sequence_10']
            },
            {
                "identifier": 'EVENT_3372_action_queue_async_4_SUBSCRIPT_jmp_if_var_equals_short_4',
                "command": 'jmp_if_var_equals_short',
                "args": [0x700c, 1, 'EVENT_3372_action_queue_async_4_SUBSCRIPT_set_sprite_sequence_12']
            },
            {
                "identifier": 'EVENT_3372_action_queue_async_4_SUBSCRIPT_jmp_if_var_equals_short_5',
                "command": 'jmp_if_var_equals_short',
                "args": [0x700c, 2, 'EVENT_3372_action_queue_async_4_SUBSCRIPT_set_sprite_sequence_12']
            },
            {
                "identifier": 'EVENT_3372_action_queue_async_4_SUBSCRIPT_jmp_if_var_equals_short_6',
                "command": 'jmp_if_var_equals_short',
                "args": [0x700c, 3, 'EVENT_3372_action_queue_async_4_SUBSCRIPT_set_sprite_sequence_14']
            },
            {
                "identifier": 'EVENT_3372_action_queue_async_4_SUBSCRIPT_jmp_if_var_equals_short_7',
                "command": 'jmp_if_var_equals_short',
                "args": [0x700c, 4, 'EVENT_3372_action_queue_async_4_SUBSCRIPT_set_sprite_sequence_14']
            },
            {
                "identifier": 'EVENT_3372_action_queue_async_4_SUBSCRIPT_jmp_if_var_equals_short_8',
                "command": 'jmp_if_var_equals_short',
                "args": [0x700c, 5, 'EVENT_3372_action_queue_async_4_SUBSCRIPT_set_sprite_sequence_16']
            },
            {
                "identifier": 'EVENT_3372_action_queue_async_4_SUBSCRIPT_jmp_if_var_equals_short_9',
                "command": 'jmp_if_var_equals_short',
                "args": [0x700c, 6, 'EVENT_3372_action_queue_async_4_SUBSCRIPT_set_sprite_sequence_16']
            },
            {
                "identifier": 'EVENT_3372_action_queue_async_4_SUBSCRIPT_set_sprite_sequence_10',
                "command": 'set_sprite_sequence',
                "args": [6, inc_sprite=3, flags=[_0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_3372_action_queue_async_4_SUBSCRIPT_jmp_11',
                "command": 'jmp',
                "args": ['EVENT_3372_action_queue_async_4_SUBSCRIPT_fixed_f_coord_on_18']
            },
            {
                "identifier": 'EVENT_3372_action_queue_async_4_SUBSCRIPT_set_sprite_sequence_12',
                "command": 'set_sprite_sequence',
                "args": [7, inc_sprite=3, flags=[_0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3372_action_queue_async_4_SUBSCRIPT_jmp_13',
                "command": 'jmp',
                "args": ['EVENT_3372_action_queue_async_4_SUBSCRIPT_fixed_f_coord_on_18']
            },
            {
                "identifier": 'EVENT_3372_action_queue_async_4_SUBSCRIPT_set_sprite_sequence_14',
                "command": 'set_sprite_sequence',
                "args": [7, inc_sprite=3, flags=[_0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_3372_action_queue_async_4_SUBSCRIPT_jmp_15',
                "command": 'jmp',
                "args": ['EVENT_3372_action_queue_async_4_SUBSCRIPT_fixed_f_coord_on_18']
            },
            {
                "identifier": 'EVENT_3372_action_queue_async_4_SUBSCRIPT_set_sprite_sequence_16',
                "command": 'set_sprite_sequence',
                "args": [6, inc_sprite=3, flags=[_0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3372_action_queue_async_4_SUBSCRIPT_jmp_17',
                "command": 'jmp',
                "args": ['EVENT_3372_action_queue_async_4_SUBSCRIPT_fixed_f_coord_on_18']
            },
            {
                "identifier": 'EVENT_3372_action_queue_async_4_SUBSCRIPT_fixed_f_coord_on_18',
                "command": 'fixed_f_coord_on'
            },
            {
                "identifier": 'EVENT_3372_action_queue_async_4_SUBSCRIPT_set_animation_speed_19',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_3372_action_queue_async_4_SUBSCRIPT_turn_clockwise_45_degrees_n_times_20',
                "command": 'turn_clockwise_45_degrees_n_times',
                "args": [4]
            },
            {
                "identifier": 'EVENT_3372_action_queue_async_4_SUBSCRIPT_shift_f_direction_steps_21',
                "command": 'shift_f_direction_steps',
                "args": [2]
            },
            {
                "identifier": 'EVENT_3372_action_queue_async_4_SUBSCRIPT_turn_clockwise_45_degrees_n_times_22',
                "command": 'turn_clockwise_45_degrees_n_times',
                "args": [4]
            },
            {
                "identifier": 'EVENT_3372_action_queue_async_4_SUBSCRIPT_fixed_f_coord_off_23',
                "command": 'fixed_f_coord_off'
            },
            {
                "identifier": 'EVENT_3372_action_queue_async_4_SUBSCRIPT_set_animation_speed_24',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_3372_action_queue_async_4_SUBSCRIPT_reset_properties_25',
                "command": 'reset_properties'
            }
        ]
    },
    {
        "identifier": 'EVENT_3372_clear_bit_5',
        "command": 'clear_bit',
        "args": [0x7044, 7]
    },
    {
        "identifier": 'EVENT_3372_ret_6',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_3372_set_bit_7',
        "command": 'set_bit',
        "args": [0x7044, 7]
    },
    {
        "identifier": 'EVENT_3372_set_short_mem_8',
        "command": 'set_short_mem',
        "args": [0x7000, 0x70a8]
    },
    {
        "identifier": 'EVENT_3372_set_short_mem_9',
        "command": 'set_short_mem',
        "args": [0x70ab, 0x7000]
    },
    {
        "identifier": 'EVENT_3372_action_queue_sync_10',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MEM_70AB],
        "subscript": [
            {
                "identifier": 'EVENT_3372_action_queue_sync_10_SUBSCRIPT_clear_solidity_bits_0',
                "command": 'clear_solidity_bits',
                "args": [[_0x0AFlags.BIT_4, _0x0AFlags.CANT_WALK_THROUGH]]
            },
            {
                "identifier": 'EVENT_3372_action_queue_sync_10_SUBSCRIPT_set_object_memory_bits_1',
                "command": 'set_object_memory_bits',
                "args": [0x0b, bits=[0, 1]]
            },
            {
                "identifier": 'EVENT_3372_action_queue_sync_10_SUBSCRIPT_set_animation_speed_2',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_3372_action_queue_sync_10_SUBSCRIPT_shift_z_down_steps_3',
                "command": 'shift_z_down_steps',
                "args": [4]
            },
            {
                "identifier": 'EVENT_3372_action_queue_sync_10_SUBSCRIPT_set_animation_speed_4',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_3372_action_queue_sync_10_SUBSCRIPT_set_object_memory_bits_5',
                "command": 'set_object_memory_bits',
                "args": [0x0b, bits=[1]]
            },
            {
                "identifier": 'EVENT_3372_action_queue_sync_10_SUBSCRIPT_set_solidity_bits_6',
                "command": 'set_solidity_bits',
                "args": [[_0x0AFlags.BIT_4, _0x0AFlags.CANT_WALK_THROUGH]]
            }
        ]
    },
    {
        "identifier": 'EVENT_3372_action_queue_async_11',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_3372_action_queue_async_11_SUBSCRIPT_set_vram_priority_0',
                "command": 'set_vram_priority',
                "args": [VramPriority.MARIO_OVERLAPS_ON_ALL_SIDES]
            },
            {
                "identifier": 'EVENT_3372_action_queue_async_11_SUBSCRIPT_clear_solidity_bits_1',
                "command": 'clear_solidity_bits',
                "args": [[_0x0AFlags.CANT_PASS_NPCS, _0x0AFlags.BIT_7]]
            },
            {
                "identifier": 'EVENT_3372_action_queue_async_11_SUBSCRIPT_set_object_memory_bits_2',
                "command": 'set_object_memory_bits',
                "args": [0x0b, bits=[0, 1]]
            },
            {
                "identifier": 'EVENT_3372_action_queue_async_11_SUBSCRIPT_set_animation_speed_3',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_3372_action_queue_async_11_SUBSCRIPT_shift_z_down_steps_4',
                "command": 'shift_z_down_steps',
                "args": [4]
            },
            {
                "identifier": 'EVENT_3372_action_queue_async_11_SUBSCRIPT_set_700C_to_object_coord_5',
                "command": 'set_700C_to_object_coord',
                "args": [AreaObjects.DUMMY_0X07, Coords.F]
            },
            {
                "identifier": 'EVENT_3372_action_queue_async_11_SUBSCRIPT_jmp_if_var_equals_short_6',
                "command": 'jmp_if_var_equals_short',
                "args": [0x700c, 7, 'EVENT_3372_action_queue_async_11_SUBSCRIPT_set_sprite_sequence_14']
            },
            {
                "identifier": 'EVENT_3372_action_queue_async_11_SUBSCRIPT_jmp_if_var_equals_short_7',
                "command": 'jmp_if_var_equals_short',
                "args": [0x700c, 0, 'EVENT_3372_action_queue_async_11_SUBSCRIPT_set_sprite_sequence_14']
            },
            {
                "identifier": 'EVENT_3372_action_queue_async_11_SUBSCRIPT_jmp_if_var_equals_short_8',
                "command": 'jmp_if_var_equals_short',
                "args": [0x700c, 1, 'EVENT_3372_action_queue_async_11_SUBSCRIPT_set_sprite_sequence_20']
            },
            {
                "identifier": 'EVENT_3372_action_queue_async_11_SUBSCRIPT_jmp_if_var_equals_short_9',
                "command": 'jmp_if_var_equals_short',
                "args": [0x700c, 2, 'EVENT_3372_action_queue_async_11_SUBSCRIPT_set_sprite_sequence_20']
            },
            {
                "identifier": 'EVENT_3372_action_queue_async_11_SUBSCRIPT_jmp_if_var_equals_short_10',
                "command": 'jmp_if_var_equals_short',
                "args": [0x700c, 3, 'EVENT_3372_action_queue_async_11_SUBSCRIPT_set_sprite_sequence_18']
            },
            {
                "identifier": 'EVENT_3372_action_queue_async_11_SUBSCRIPT_jmp_if_var_equals_short_11',
                "command": 'jmp_if_var_equals_short',
                "args": [0x700c, 4, 'EVENT_3372_action_queue_async_11_SUBSCRIPT_set_sprite_sequence_18']
            },
            {
                "identifier": 'EVENT_3372_action_queue_async_11_SUBSCRIPT_jmp_if_var_equals_short_12',
                "command": 'jmp_if_var_equals_short',
                "args": [0x700c, 5, 'EVENT_3372_action_queue_async_11_SUBSCRIPT_set_sprite_sequence_16']
            },
            {
                "identifier": 'EVENT_3372_action_queue_async_11_SUBSCRIPT_jmp_if_var_equals_short_13',
                "command": 'jmp_if_var_equals_short',
                "args": [0x700c, 6, 'EVENT_3372_action_queue_async_11_SUBSCRIPT_set_sprite_sequence_16']
            },
            {
                "identifier": 'EVENT_3372_action_queue_async_11_SUBSCRIPT_set_sprite_sequence_14',
                "command": 'set_sprite_sequence',
                "args": [8, inc_sprite=2, flags=[_0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3372_action_queue_async_11_SUBSCRIPT_jmp_15',
                "command": 'jmp',
                "args": ['EVENT_3372_resume_action_script_12']
            },
            {
                "identifier": 'EVENT_3372_action_queue_async_11_SUBSCRIPT_set_sprite_sequence_16',
                "command": 'set_sprite_sequence',
                "args": [8, inc_sprite=2, flags=[_0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_3372_action_queue_async_11_SUBSCRIPT_jmp_17',
                "command": 'jmp',
                "args": ['EVENT_3372_resume_action_script_12']
            },
            {
                "identifier": 'EVENT_3372_action_queue_async_11_SUBSCRIPT_set_sprite_sequence_18',
                "command": 'set_sprite_sequence',
                "args": [1, inc_sprite=3, flags=[_0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3372_action_queue_async_11_SUBSCRIPT_jmp_19',
                "command": 'jmp',
                "args": ['EVENT_3372_resume_action_script_12']
            },
            {
                "identifier": 'EVENT_3372_action_queue_async_11_SUBSCRIPT_set_sprite_sequence_20',
                "command": 'set_sprite_sequence',
                "args": [1, inc_sprite=3, flags=[_0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_3372_action_queue_async_11_SUBSCRIPT_jmp_21',
                "command": 'jmp',
                "args": ['EVENT_3372_resume_action_script_12']
            }
        ]
    },
    {
        "identifier": 'EVENT_3372_resume_action_script_12',
        "command": 'resume_action_script',
        "args": [AreaObjects.MEM_70AB]
    },
    {
        "identifier": 'EVENT_3372_set_short_13',
        "command": 'set_short',
        "args": [0x7024, 0x0000]
    },
    {
        "identifier": 'EVENT_3372_pause_14',
        "command": 'pause',
        "args": [1]
    },
    {
        "identifier": 'EVENT_3372_set_7000_to_tapped_button_15',
        "command": 'set_7000_to_tapped_button'
    },
    {
        "identifier": 'EVENT_3372_jmp_if_var_equals_short_16',
        "command": 'jmp_if_var_equals_short',
        "args": [0x7000, 0, 'EVENT_3372_add_short_19']
    },
    {
        "identifier": 'EVENT_3372_add_short_17',
        "command": 'add_short',
        "args": [0x7024, 0x01]
    },
    {
        "identifier": 'EVENT_3372_jmp_if_var_equals_short_18',
        "command": 'jmp_if_var_equals_short',
        "args": [0x7024, 0, 'EVENT_3372_action_queue_async_23']
    },
    {
        "identifier": 'EVENT_3372_add_short_19',
        "command": 'add_short',
        "args": [0x7024, 0x01]
    },
    {
        "identifier": 'EVENT_3372_add_short_20',
        "command": 'add_short',
        "args": [0x7024, 0x01]
    },
    {
        "identifier": 'EVENT_3372_mem_compare_21',
        "command": 'mem_compare',
        "args": [0x7024, 120]
    },
    {
        "identifier": 'EVENT_3372_jmp_if_comparison_result_is_lesser_22',
        "command": 'jmp_if_comparison_result_is_lesser',
        "args": ['EVENT_3372_pause_14']
    },
    {
        "identifier": 'EVENT_3372_action_queue_async_23',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_3372_action_queue_async_23_SUBSCRIPT_set_vram_priority_0',
                "command": 'set_vram_priority',
                "args": [VramPriority.NORMAL]
            },
            {
                "identifier": 'EVENT_3372_action_queue_async_23_SUBSCRIPT_set_animation_speed_1',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_3372_action_queue_async_23_SUBSCRIPT_reset_properties_2',
                "command": 'reset_properties'
            },
            {
                "identifier": 'EVENT_3372_action_queue_async_23_SUBSCRIPT_fixed_f_coord_on_3',
                "command": 'fixed_f_coord_on'
            },
            {
                "identifier": 'EVENT_3372_action_queue_async_23_SUBSCRIPT_turn_clockwise_45_degrees_n_times_4',
                "command": 'turn_clockwise_45_degrees_n_times',
                "args": [4]
            },
            {
                "identifier": 'EVENT_3372_action_queue_async_23_SUBSCRIPT_walk_1_step_f_direction_5',
                "command": 'walk_1_step_f_direction'
            },
            {
                "identifier": 'EVENT_3372_action_queue_async_23_SUBSCRIPT_turn_clockwise_45_degrees_n_times_6',
                "command": 'turn_clockwise_45_degrees_n_times',
                "args": [4]
            },
            {
                "identifier": 'EVENT_3372_action_queue_async_23_SUBSCRIPT_fixed_f_coord_off_7',
                "command": 'fixed_f_coord_off'
            },
            {
                "identifier": 'EVENT_3372_action_queue_async_23_SUBSCRIPT_set_animation_speed_8',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
            }
        ]
    },
    {
        "identifier": 'EVENT_3372_set_short_mem_24',
        "command": 'set_short_mem',
        "args": [0x7000, 0x70ab]
    },
    {
        "identifier": 'EVENT_3372_set_short_mem_25',
        "command": 'set_short_mem',
        "args": [0x70ae, 0x7000]
    },
    {
        "identifier": 'EVENT_3372_set_action_script_async_26',
        "command": 'set_action_script_async',
        "args": [AreaObjects.MARIO, 671]
    },
    {
        "identifier": 'EVENT_3372_action_queue_async_27',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_3372_action_queue_async_27_SUBSCRIPT_set_solidity_bits_0',
                "command": 'set_solidity_bits',
                "args": [[_0x0AFlags.CANT_PASS_NPCS, _0x0AFlags.BIT_7]]
            }
        ]
    },
    {
        "identifier": 'EVENT_3372_clear_bit_28',
        "command": 'clear_bit',
        "args": [0x7044, 7]
    },
    {
        "identifier": 'EVENT_3372_ret_29',
        "command": 'ret'
    }
]
