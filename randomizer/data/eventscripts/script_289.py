from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data import items
script = [
    {
        "identifier": 'EVENT_289_set_7000_to_current_level_0',
        "command": 'set_7000_to_current_level'
    },
    {
        "identifier": 'EVENT_289_jmp_if_var_equals_short_1',
        "command": 'jmp_if_var_equals_short',
        "args": [0x7000, 485, 'EVENT_289_set_short_8']
    },
    {
        "identifier": 'EVENT_289_jmp_if_var_equals_short_2',
        "command": 'jmp_if_var_equals_short',
        "args": [0x7000, 493, 'EVENT_289_set_short_11']
    },
    {
        "identifier": 'EVENT_289_jmp_if_var_equals_short_3',
        "command": 'jmp_if_var_equals_short',
        "args": [0x7000, 85, 'EVENT_289_jmp_if_bit_set_15']
    },
    {
        "identifier": 'EVENT_289_jmp_if_var_equals_short_4',
        "command": 'jmp_if_var_equals_short',
        "args": [0x7000, 86, 'EVENT_289_set_bit_14']
    },
    {
        "identifier": 'EVENT_289_set_short_5',
        "command": 'set_short',
        "args": [0x7024, 0x0003]
    },
    {
        "identifier": 'EVENT_289_set_bit_6',
        "command": 'set_bit',
        "args": [0x7042, 7]
    },
    {
        "identifier": 'EVENT_289_jmp_to_event_7',
        "command": 'jmp_to_event',
        "args": [273]
    },
    {
        "identifier": 'EVENT_289_set_short_8',
        "command": 'set_short',
        "args": [0x7024, 0x0003]
    },
    {
        "identifier": 'EVENT_289_set_bit_9',
        "command": 'set_bit',
        "args": [0x7084, 5]
    },
    {
        "identifier": 'EVENT_289_jmp_to_event_10',
        "command": 'jmp_to_event',
        "args": [273]
    },
    {
        "identifier": 'EVENT_289_set_short_11',
        "command": 'set_short',
        "args": [0x7024, 0x0003]
    },
    {
        "identifier": 'EVENT_289_set_bit_12',
        "command": 'set_bit',
        "args": [0x705d, 6]
    },
    {
        "identifier": 'EVENT_289_jmp_to_event_13',
        "command": 'jmp_to_event',
        "args": [273]
    },
    {
        "identifier": 'EVENT_289_set_bit_14',
        "command": 'set_bit',
        "args": [0x7044, 2]
    },
    {
        "identifier": 'EVENT_289_jmp_if_bit_set_15',
        "command": 'jmp_if_bit_set',
        "args": [0x7043, 7, 'EVENT_289_set_7010_to_object_xyz_36']
    },
    {
        "identifier": 'EVENT_289_jmp_if_bit_set_16',
        "command": 'jmp_if_bit_set',
        "args": [0x7044, 5, 'EVENT_289_set_7010_to_object_xyz_36']
    },
    {
        "identifier": 'EVENT_289_run_dialog_17',
        "command": 'run_dialog',
        "args": [766, AreaObjects.MEM_70A8, [_0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]]
    },
    {
        "identifier": 'EVENT_289_jmp_if_dialog_option_b_18',
        "command": 'jmp_if_dialog_option_b',
        "args": ['EVENT_289_pause_29']
    },
    {
        "identifier": 'EVENT_289_pause_19',
        "command": 'pause',
        "args": [10]
    },
    {
        "identifier": 'EVENT_289_run_event_as_subroutine_20',
        "command": 'run_event_as_subroutine',
        "args": [3587]
    },
    {
        "identifier": 'EVENT_289_set_action_script_async_21',
        "command": 'set_action_script_async',
        "args": [AreaObjects.MARIO, 670]
    },
    {
        "identifier": 'EVENT_289_pause_22',
        "command": 'pause',
        "args": [10]
    },
    {
        "identifier": 'EVENT_289_run_dialog_23',
        "command": 'run_dialog',
        "args": [767, AreaObjects.MEM_70A8, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]]
    },
    {
        "identifier": 'EVENT_289_jmp_if_bit_set_24',
        "command": 'jmp_if_bit_set',
        "args": [0x7044, 2, 'EVENT_289_set_bit_27']
    },
    {
        "identifier": 'EVENT_289_set_bit_25',
        "command": 'set_bit',
        "args": [0x7084, 6]
    },
    {
        "identifier": 'EVENT_289_jmp_26',
        "command": 'jmp',
        "args": ['EVENT_273_fade_out_music_to_volume_17']
    },
    {
        "identifier": 'EVENT_289_set_bit_27',
        "command": 'set_bit',
        "args": [0x7061, 1]
    },
    {
        "identifier": 'EVENT_289_jmp_28',
        "command": 'jmp',
        "args": ['EVENT_273_fade_out_music_to_volume_17']
    },
    {
        "identifier": 'EVENT_289_pause_29',
        "command": 'pause',
        "args": [10]
    },
    {
        "identifier": 'EVENT_289_run_event_as_subroutine_30',
        "command": 'run_event_as_subroutine',
        "args": [3587]
    },
    {
        "identifier": 'EVENT_289_set_action_script_async_31',
        "command": 'set_action_script_async',
        "args": [AreaObjects.MARIO, 671]
    },
    {
        "identifier": 'EVENT_289_remember_last_object_32',
        "command": 'remember_last_object'
    },
    {
        "identifier": 'EVENT_289_pause_33',
        "command": 'pause',
        "args": [10]
    },
    {
        "identifier": 'EVENT_289_run_dialog_34',
        "command": 'run_dialog',
        "args": [768, AreaObjects.MEM_70A8, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]]
    },
    {
        "identifier": 'EVENT_289_ret_35',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_289_set_7010_to_object_xyz_36',
        "command": 'set_7010_to_object_xyz',
        "args": [0x94]
    },
    {
        "identifier": 'EVENT_289_mem_compare_37',
        "command": 'mem_compare',
        "args": [0x7010, 5]
    },
    {
        "identifier": 'EVENT_289_jmp_if_comparison_result_is_lesser_38',
        "command": 'jmp_if_comparison_result_is_lesser',
        "args": ['EVENT_256_ret_0']
    },
    {
        "identifier": 'EVENT_289_jmp_if_bit_set_39',
        "command": 'jmp_if_bit_set',
        "args": [0x7056, 3, 'EVENT_289_jmp_if_bit_set_15']
    },
    {
        "identifier": 'EVENT_289_enable_controls_until_return_40',
        "command": 'enable_controls_until_return',
        "args": [[]]
    },
    {
        "identifier": 'EVENT_289_unsync_dialog_41',
        "command": 'unsync_dialog'
    },
    {
        "identifier": 'EVENT_289_pause_action_script_42',
        "command": 'pause_action_script',
        "args": [AreaObjects.NPC_0]
    },
    {
        "identifier": 'EVENT_289_pause_action_script_43',
        "command": 'pause_action_script',
        "args": [AreaObjects.NPC_1]
    },
    {
        "identifier": 'EVENT_289_jmp_if_bit_set_44',
        "command": 'jmp_if_bit_set',
        "args": [0x7044, 0, 'EVENT_289_run_dialog_63']
    },
    {
        "identifier": 'EVENT_289_run_dialog_45',
        "command": 'run_dialog',
        "args": [776, AreaObjects.MEM_70A8, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]]
    },
    {
        "identifier": 'EVENT_289_jmp_if_dialog_option_b_46',
        "command": 'jmp_if_dialog_option_b',
        "args": ['EVENT_289_pause_55']
    },
    {
        "identifier": 'EVENT_289_pause_47',
        "command": 'pause',
        "args": [10]
    },
    {
        "identifier": 'EVENT_289_action_queue_async_48',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_289_action_queue_async_48_SUBSCRIPT_clear_solidity_bits_0',
                "command": 'clear_solidity_bits',
                "args": [[_0x0AFlags.BIT_4, _0x0AFlags.CANT_PASS_NPCS, _0x0AFlags.CANT_WALK_THROUGH, _0x0AFlags.BIT_7]]
            },
            {
                "identifier": 'EVENT_289_action_queue_async_48_SUBSCRIPT_start_loop_n_times_1',
                "command": 'start_loop_n_times',
                "args": [7]
            },
            {
                "identifier": 'EVENT_289_action_queue_async_48_SUBSCRIPT_turn_clockwise_45_degrees_n_times_2',
                "command": 'turn_clockwise_45_degrees_n_times',
                "args": [1]
            },
            {
                "identifier": 'EVENT_289_action_queue_async_48_SUBSCRIPT_pause_3',
                "command": 'pause',
                "args": [2]
            },
            {
                "identifier": 'EVENT_289_action_queue_async_48_SUBSCRIPT_end_loop_4',
                "command": 'end_loop'
            },
            {
                "identifier": 'EVENT_289_action_queue_async_48_SUBSCRIPT_jump_to_height_5',
                "command": 'jump_to_height',
                "args": [108]
            },
            {
                "identifier": 'EVENT_289_action_queue_async_48_SUBSCRIPT_pause_6',
                "command": 'pause',
                "args": [1]
            },
            {
                "identifier": 'EVENT_289_action_queue_async_48_SUBSCRIPT_jmp_if_mario_in_air_7',
                "command": 'jmp_if_mario_in_air',
                "args": ['EVENT_289_action_queue_async_48_SUBSCRIPT_pause_6']
            },
            {
                "identifier": 'EVENT_289_action_queue_async_48_SUBSCRIPT_set_solidity_bits_8',
                "command": 'set_solidity_bits',
                "args": [[_0x0AFlags.BIT_4, _0x0AFlags.CANT_PASS_NPCS, _0x0AFlags.CANT_WALK_THROUGH, _0x0AFlags.BIT_7]]
            }
        ]
    },
    {
        "identifier": 'EVENT_289_pause_49',
        "command": 'pause',
        "args": [10]
    },
    {
        "identifier": 'EVENT_289_run_dialog_50',
        "command": 'run_dialog',
        "args": [777, AreaObjects.MEM_70A8, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]]
    },
    {
        "identifier": 'EVENT_289_resume_action_script_51',
        "command": 'resume_action_script',
        "args": [AreaObjects.NPC_0]
    },
    {
        "identifier": 'EVENT_289_resume_action_script_52',
        "command": 'resume_action_script',
        "args": [AreaObjects.NPC_1]
    },
    {
        "identifier": 'EVENT_289_enable_controls_until_return_53',
        "command": 'enable_controls_until_return',
        "args": [[ControllerDirections.LEFT, ControllerDirections.RIGHT, ControllerDirections.DOWN, ControllerDirections.UP, ControllerDirections.A, ControllerDirections.Y, ControllerDirections.B]]
    },
    {
        "identifier": 'EVENT_289_ret_54',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_289_pause_55',
        "command": 'pause',
        "args": [10]
    },
    {
        "identifier": 'EVENT_289_action_queue_async_56',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_289_action_queue_async_56_SUBSCRIPT_set_700C_to_object_coord_0',
                "command": 'set_700C_to_object_coord',
                "args": [AreaObjects.MARIO, Coords.F]
            },
            {
                "identifier": 'EVENT_289_action_queue_async_56_SUBSCRIPT_set_short_mem_1',
                "command": 'set_short_mem',
                "args": [0x7024, 0x700c]
            },
            {
                "identifier": 'EVENT_289_action_queue_async_56_SUBSCRIPT_db_2',
                "command": 'db',
                "args": [0xfd, 0x24, 0x00, 0x10]
            },
            {
                "identifier": 'EVENT_289_action_queue_async_56_SUBSCRIPT_set_short_mem_3',
                "command": 'set_short_mem',
                "args": [0x7000, 0x700c]
            },
            {
                "identifier": 'EVENT_289_action_queue_async_56_SUBSCRIPT_mem_700C_and_const_4',
                "command": 'mem_700C_and_const',
                "args": [0x00c0]
            },
            {
                "identifier": 'EVENT_289_action_queue_async_56_SUBSCRIPT_jmp_if_var_equals_short_5',
                "command": 'jmp_if_var_equals_short',
                "args": [0x700c, 0, 'EVENT_289_action_queue_async_56_SUBSCRIPT_set_sprite_sequence_9']
            },
            {
                "identifier": 'EVENT_289_action_queue_async_56_SUBSCRIPT_jmp_if_var_equals_short_6',
                "command": 'jmp_if_var_equals_short',
                "args": [0x700c, 64, 'EVENT_289_action_queue_async_56_SUBSCRIPT_set_sprite_sequence_15']
            },
            {
                "identifier": 'EVENT_289_action_queue_async_56_SUBSCRIPT_jmp_if_var_equals_short_7',
                "command": 'jmp_if_var_equals_short',
                "args": [0x700c, 128, 'EVENT_289_action_queue_async_56_SUBSCRIPT_set_sprite_sequence_21']
            },
            {
                "identifier": 'EVENT_289_action_queue_async_56_SUBSCRIPT_jmp_if_var_equals_short_8',
                "command": 'jmp_if_var_equals_short',
                "args": [0x700c, 192, 'EVENT_289_action_queue_async_56_SUBSCRIPT_set_sprite_sequence_27']
            },
            {
                "identifier": 'EVENT_289_action_queue_async_56_SUBSCRIPT_set_sprite_sequence_9',
                "command": 'set_sprite_sequence',
                "args": [0, 0, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_289_action_queue_async_56_SUBSCRIPT_pause_10',
                "command": 'pause',
                "args": [20]
            },
            {
                "identifier": 'EVENT_289_action_queue_async_56_SUBSCRIPT_set_sprite_sequence_11',
                "command": 'set_sprite_sequence',
                "args": [6, 0, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_289_action_queue_async_56_SUBSCRIPT_pause_12',
                "command": 'pause',
                "args": [40]
            },
            {
                "identifier": 'EVENT_289_action_queue_async_56_SUBSCRIPT_set_sprite_sequence_13',
                "command": 'set_sprite_sequence',
                "args": [0, 0, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_289_action_queue_async_56_SUBSCRIPT_jmp_14',
                "command": 'jmp',
                "args": ['EVENT_289_action_queue_async_56_SUBSCRIPT_pause_32']
            },
            {
                "identifier": 'EVENT_289_action_queue_async_56_SUBSCRIPT_set_sprite_sequence_15',
                "command": 'set_sprite_sequence',
                "args": [0, 0, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_289_action_queue_async_56_SUBSCRIPT_pause_16',
                "command": 'pause',
                "args": [20]
            },
            {
                "identifier": 'EVENT_289_action_queue_async_56_SUBSCRIPT_set_sprite_sequence_17',
                "command": 'set_sprite_sequence',
                "args": [6, 0, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_289_action_queue_async_56_SUBSCRIPT_pause_18',
                "command": 'pause',
                "args": [40]
            },
            {
                "identifier": 'EVENT_289_action_queue_async_56_SUBSCRIPT_set_sprite_sequence_19',
                "command": 'set_sprite_sequence',
                "args": [0, 0, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_289_action_queue_async_56_SUBSCRIPT_jmp_20',
                "command": 'jmp',
                "args": ['EVENT_289_action_queue_async_56_SUBSCRIPT_pause_32']
            },
            {
                "identifier": 'EVENT_289_action_queue_async_56_SUBSCRIPT_set_sprite_sequence_21',
                "command": 'set_sprite_sequence',
                "args": [3, 0, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_289_action_queue_async_56_SUBSCRIPT_pause_22',
                "command": 'pause',
                "args": [20]
            },
            {
                "identifier": 'EVENT_289_action_queue_async_56_SUBSCRIPT_set_sprite_sequence_23',
                "command": 'set_sprite_sequence',
                "args": [7, 0, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_289_action_queue_async_56_SUBSCRIPT_pause_24',
                "command": 'pause',
                "args": [40]
            },
            {
                "identifier": 'EVENT_289_action_queue_async_56_SUBSCRIPT_set_sprite_sequence_25',
                "command": 'set_sprite_sequence',
                "args": [3, 0, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_289_action_queue_async_56_SUBSCRIPT_jmp_26',
                "command": 'jmp',
                "args": ['EVENT_289_action_queue_async_56_SUBSCRIPT_pause_32']
            },
            {
                "identifier": 'EVENT_289_action_queue_async_56_SUBSCRIPT_set_sprite_sequence_27',
                "command": 'set_sprite_sequence',
                "args": [3, 0, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_289_action_queue_async_56_SUBSCRIPT_pause_28',
                "command": 'pause',
                "args": [20]
            },
            {
                "identifier": 'EVENT_289_action_queue_async_56_SUBSCRIPT_set_sprite_sequence_29',
                "command": 'set_sprite_sequence',
                "args": [7, 0, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_289_action_queue_async_56_SUBSCRIPT_pause_30',
                "command": 'pause',
                "args": [40]
            },
            {
                "identifier": 'EVENT_289_action_queue_async_56_SUBSCRIPT_set_sprite_sequence_31',
                "command": 'set_sprite_sequence',
                "args": [3, 0, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_289_action_queue_async_56_SUBSCRIPT_pause_32',
                "command": 'pause',
                "args": [20]
            },
            {
                "identifier": 'EVENT_289_action_queue_async_56_SUBSCRIPT_reset_properties_33',
                "command": 'reset_properties'
            },
            {
                "identifier": 'EVENT_289_action_queue_async_56_SUBSCRIPT_set_solidity_bits_34',
                "command": 'set_solidity_bits',
                "args": [[_0x0AFlags.BIT_4, _0x0AFlags.CANT_PASS_NPCS, _0x0AFlags.CANT_WALK_THROUGH, _0x0AFlags.BIT_7]]
            }
        ]
    },
    {
        "identifier": 'EVENT_289_pause_57',
        "command": 'pause',
        "args": [10]
    },
    {
        "identifier": 'EVENT_289_run_dialog_58',
        "command": 'run_dialog',
        "args": [778, AreaObjects.MEM_70A8, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]]
    },
    {
        "identifier": 'EVENT_289_enable_controls_until_return_59',
        "command": 'enable_controls_until_return',
        "args": [[ControllerDirections.LEFT, ControllerDirections.RIGHT, ControllerDirections.DOWN, ControllerDirections.UP, ControllerDirections.A, ControllerDirections.Y, ControllerDirections.B]]
    },
    {
        "identifier": 'EVENT_289_resume_action_script_60',
        "command": 'resume_action_script',
        "args": [AreaObjects.NPC_0]
    },
    {
        "identifier": 'EVENT_289_resume_action_script_61',
        "command": 'resume_action_script',
        "args": [AreaObjects.NPC_1]
    },
    {
        "identifier": 'EVENT_289_ret_62',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_289_run_dialog_63',
        "command": 'run_dialog',
        "args": [782, AreaObjects.MEM_70A8, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]]
    },
    {
        "identifier": 'EVENT_289_resume_action_script_64',
        "command": 'resume_action_script',
        "args": [AreaObjects.NPC_0]
    },
    {
        "identifier": 'EVENT_289_resume_action_script_65',
        "command": 'resume_action_script',
        "args": [AreaObjects.NPC_1]
    },
    {
        "identifier": 'EVENT_289_enable_controls_until_return_66',
        "command": 'enable_controls_until_return',
        "args": [[ControllerDirections.LEFT, ControllerDirections.RIGHT, ControllerDirections.DOWN, ControllerDirections.UP, ControllerDirections.A, ControllerDirections.Y, ControllerDirections.B]]
    },
    {
        "identifier": 'EVENT_289_ret_67',
        "command": 'ret'
    }
]
