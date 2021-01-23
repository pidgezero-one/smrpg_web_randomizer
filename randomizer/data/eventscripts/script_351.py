from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data import items
script = [
    {
        "identifier": 'EVENT_351_jmp_if_bit_set_0',
        "command": 'jmp_if_bit_set',
        "args": [0x7062, 3, 'EVENT_351_run_dialog_42']
    },
    {
        "identifier": 'EVENT_351_jmp_if_bit_set_1',
        "command": 'jmp_if_bit_set',
        "args": [0x7090, 6, 'EVENT_351_action_queue_async_28']
    },
    {
        "identifier": 'EVENT_351_set_short_mem_2',
        "command": 'set_short_mem',
        "args": [0x7000, 0x70af]
    },
    {
        "identifier": 'EVENT_351_mem_compare_val_3',
        "command": 'mem_compare_val',
        "args": [3]
    },
    {
        "identifier": 'EVENT_351_jmp_if_comparison_result_is_greater_or_equal_4',
        "command": 'jmp_if_comparison_result_is_greater_or_equal',
        "args": ['EVENT_351_jmp_if_bit_set_20']
    },
    {
        "identifier": 'EVENT_351_jmp_if_random_above_128_5',
        "command": 'jmp_if_random_above_128',
        "args": ['EVENT_351_jmp_if_bit_set_13']
    },
    {
        "identifier": 'EVENT_351_jmp_if_bit_set_6',
        "command": 'jmp_if_bit_set',
        "args": [0x7082, 0, 'EVENT_351_run_dialog_10']
    },
    {
        "identifier": 'EVENT_351_run_dialog_7',
        "command": 'run_dialog',
        "args": [3732, AreaObjects.MEM_70A8, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]]
    },
    {
        "identifier": 'EVENT_351_inc_8',
        "command": 'inc',
        "args": [0x70af]
    },
    {
        "identifier": 'EVENT_351_ret_9',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_351_run_dialog_10',
        "command": 'run_dialog',
        "args": [3735, AreaObjects.MEM_70A8, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]]
    },
    {
        "identifier": 'EVENT_351_inc_11',
        "command": 'inc',
        "args": [0x70af]
    },
    {
        "identifier": 'EVENT_351_ret_12',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_351_jmp_if_bit_set_13',
        "command": 'jmp_if_bit_set',
        "args": [0x7082, 0, 'EVENT_351_run_dialog_17']
    },
    {
        "identifier": 'EVENT_351_run_dialog_14',
        "command": 'run_dialog',
        "args": [3733, AreaObjects.MEM_70A8, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]]
    },
    {
        "identifier": 'EVENT_351_inc_15',
        "command": 'inc',
        "args": [0x70af]
    },
    {
        "identifier": 'EVENT_351_ret_16',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_351_run_dialog_17',
        "command": 'run_dialog',
        "args": [3736, AreaObjects.MEM_70A8, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]]
    },
    {
        "identifier": 'EVENT_351_inc_18',
        "command": 'inc',
        "args": [0x70af]
    },
    {
        "identifier": 'EVENT_351_ret_19',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_351_jmp_if_bit_set_20',
        "command": 'jmp_if_bit_set',
        "args": [0x704c, 6, 'EVENT_351_jmp_if_bit_set_25']
    },
    {
        "identifier": 'EVENT_351_action_queue_async_21',
        "command": 'action_queue_async',
        "args": [AreaObjects.MEM_70A8],
        "subscript": [
            {
                "identifier": 'EVENT_351_action_queue_async_21_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_351_action_queue_async_21_SUBSCRIPT_fixed_f_coord_on_1',
                "command": 'fixed_f_coord_on'
            },
            {
                "identifier": 'EVENT_351_action_queue_async_21_SUBSCRIPT_shift_northwest_pixels_2',
                "command": 'shift_northwest_pixels',
                "args": [1]
            },
            {
                "identifier": 'EVENT_351_action_queue_async_21_SUBSCRIPT_start_loop_n_times_3',
                "command": 'start_loop_n_times',
                "args": [7]
            },
            {
                "identifier": 'EVENT_351_action_queue_async_21_SUBSCRIPT_shift_southeast_pixels_4',
                "command": 'shift_southeast_pixels',
                "args": [2]
            },
            {
                "identifier": 'EVENT_351_action_queue_async_21_SUBSCRIPT_shift_northwest_pixels_5',
                "command": 'shift_northwest_pixels',
                "args": [2]
            },
            {
                "identifier": 'EVENT_351_action_queue_async_21_SUBSCRIPT_end_loop_6',
                "command": 'end_loop'
            },
            {
                "identifier": 'EVENT_351_action_queue_async_21_SUBSCRIPT_shift_southeast_pixels_7',
                "command": 'shift_southeast_pixels',
                "args": [1]
            },
            {
                "identifier": 'EVENT_351_action_queue_async_21_SUBSCRIPT_fixed_f_coord_off_8',
                "command": 'fixed_f_coord_off'
            }
        ]
    },
    {
        "identifier": 'EVENT_351_run_dialog_22',
        "command": 'run_dialog',
        "args": [3734, AreaObjects.MEM_70A8, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]]
    },
    {
        "identifier": 'EVENT_351_set_23',
        "command": 'set',
        "args": [0x70af, 0]
    },
    {
        "identifier": 'EVENT_351_ret_24',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_351_jmp_if_bit_set_25',
        "command": 'jmp_if_bit_set',
        "args": [0x7062, 3, 'EVENT_351_run_dialog_42']
    },
    {
        "identifier": 'EVENT_351_set_bit_26',
        "command": 'set_bit',
        "args": [0x7090, 6]
    },
    {
        "identifier": 'EVENT_351_run_dialog_27',
        "command": 'run_dialog',
        "args": [3737, AreaObjects.MEM_70A8, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]]
    },
    {
        "identifier": 'EVENT_351_action_queue_async_28',
        "command": 'action_queue_async',
        "args": [AreaObjects.MEM_70A8],
        "subscript": [
            {
                "identifier": 'EVENT_351_action_queue_async_28_SUBSCRIPT_db_0',
                "command": 'db',
                "args": [0xfd, 0x24, 0x17, 0x00]
            },
            {
                "identifier": 'EVENT_351_action_queue_async_28_SUBSCRIPT_mem_700C_and_const_1',
                "command": 'mem_700C_and_const',
                "args": [0x00c0]
            },
            {
                "identifier": 'EVENT_351_action_queue_async_28_SUBSCRIPT_jmp_if_700C_equals_short_2',
                "command": 'jmp_if_700C_equals_short',
                "args": [64, 'EVENT_351_run_event_as_subroutine_29']
            },
            {
                "identifier": 'EVENT_351_action_queue_async_28_SUBSCRIPT_set_sprite_sequence_3',
                "command": 'set_sprite_sequence',
                "args": [1, 0, [_0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_351_action_queue_async_28_SUBSCRIPT_transfer_xyzf_pixels_4',
                "command": 'transfer_xyzf_pixels',
                "args": [4, 0, 0, RadialDirections.EAST]
            },
            {
                "identifier": 'EVENT_351_action_queue_async_28_SUBSCRIPT_jmp_5',
                "command": 'jmp',
                "args": ['EVENT_351_run_event_as_subroutine_29']
            }
        ]
    },
    {
        "identifier": 'EVENT_351_run_event_as_subroutine_29',
        "command": 'run_event_as_subroutine',
        "args": [3587]
    },
    {
        "identifier": 'EVENT_351_run_dialog_30',
        "command": 'run_dialog',
        "args": [3738, AreaObjects.MEM_70A8, [_0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]]
    },
    {
        "identifier": 'EVENT_351_jmp_if_dialog_option_b_31',
        "command": 'jmp_if_dialog_option_b',
        "args": ['EVENT_351_pause_52']
    },
    {
        "identifier": 'EVENT_351_pause_32',
        "command": 'pause',
        "args": [10]
    },
    {
        "identifier": 'EVENT_351_set_action_script_async_33',
        "command": 'set_action_script_async',
        "args": [AreaObjects.MARIO, 670]
    },
    {
        "identifier": 'EVENT_351_set_short_34',
        "command": 'set_short',
        "args": [0x7024, 0x01f4]
    },
    {
        "identifier": 'EVENT_351_run_event_as_subroutine_35',
        "command": 'run_event_as_subroutine',
        "args": [274]
    },
    {
        "identifier": 'EVENT_351_jmp_if_bit_set_36',
        "command": 'jmp_if_bit_set',
        "args": [0x7049, 3, 'EVENT_351_run_dialog_56']
    },
    {
        "identifier": 'EVENT_351_play_sound_37',
        "command": 'play_sound',
        "args": [Sounds._013_COIN, 6]
    },
    {
        "identifier": 'EVENT_351_set_38',
        "command": 'set',
        "args": [0x7000, 500]
    },
    {
        "identifier": 'EVENT_351_dec_coins_39',
        "command": 'dec_coins'
    },
    {
        "identifier": 'EVENT_351_set_bit_40',
        "command": 'set_bit',
        "args": [0x7062, 3]
    },
    {
        "identifier": 'EVENT_351_close_dialog_41',
        "command": 'close_dialog'
    },
    {
        "identifier": 'EVENT_351_run_dialog_42',
        "command": 'run_dialog',
        "args": [3742, AreaObjects.MEM_70A8, [_0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]]
    },
    {
        "identifier": 'EVENT_351_jmp_if_dialog_option_b_43',
        "command": 'jmp_if_dialog_option_b',
        "args": ['EVENT_351_pause_48']
    },
    {
        "identifier": 'EVENT_351_pause_44',
        "command": 'pause',
        "args": [10]
    },
    {
        "identifier": 'EVENT_351_set_action_script_async_45',
        "command": 'set_action_script_async',
        "args": [AreaObjects.MARIO, 670]
    },
    {
        "identifier": 'EVENT_351_run_dialog_46',
        "command": 'run_dialog',
        "args": [3744, AreaObjects.MEM_70A8, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]]
    },
    {
        "identifier": 'EVENT_351_jmp_47',
        "command": 'jmp',
        "args": ['EVENT_351_action_queue_async_58']
    },
    {
        "identifier": 'EVENT_351_pause_48',
        "command": 'pause',
        "args": [10]
    },
    {
        "identifier": 'EVENT_351_set_action_script_async_49',
        "command": 'set_action_script_async',
        "args": [AreaObjects.MARIO, 671]
    },
    {
        "identifier": 'EVENT_351_run_dialog_50',
        "command": 'run_dialog',
        "args": [3743, AreaObjects.MEM_70A8, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]]
    },
    {
        "identifier": 'EVENT_351_jmp_51',
        "command": 'jmp',
        "args": ['EVENT_351_action_queue_async_58']
    },
    {
        "identifier": 'EVENT_351_pause_52',
        "command": 'pause',
        "args": [10]
    },
    {
        "identifier": 'EVENT_351_set_action_script_async_53',
        "command": 'set_action_script_async',
        "args": [AreaObjects.MARIO, 671]
    },
    {
        "identifier": 'EVENT_351_run_dialog_54',
        "command": 'run_dialog',
        "args": [3739, AreaObjects.MEM_70A8, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]]
    },
    {
        "identifier": 'EVENT_351_jmp_55',
        "command": 'jmp',
        "args": ['EVENT_351_action_queue_async_58']
    },
    {
        "identifier": 'EVENT_351_run_dialog_56',
        "command": 'run_dialog',
        "args": [3741, AreaObjects.MEM_70A8, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]]
    },
    {
        "identifier": 'EVENT_351_jmp_57',
        "command": 'jmp',
        "args": ['EVENT_351_action_queue_async_58']
    },
    {
        "identifier": 'EVENT_351_action_queue_async_58',
        "command": 'action_queue_async',
        "args": [AreaObjects.MEM_70A8],
        "subscript": [
            {
                "identifier": 'EVENT_351_action_queue_async_58_SUBSCRIPT_set_sprite_sequence_0',
                "command": 'set_sprite_sequence',
                "args": [0, 0, [_0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_351_action_queue_async_58_SUBSCRIPT_clear_solidity_bits_1',
                "command": 'clear_solidity_bits',
                "args": [[_0x0AFlags.BIT_4, _0x0AFlags.CANT_PASS_NPCS, _0x0AFlags.CANT_WALK_THROUGH, _0x0AFlags.BIT_7]]
            },
            {
                "identifier": 'EVENT_351_action_queue_async_58_SUBSCRIPT_transfer_to_xyzf_2',
                "command": 'transfer_to_xyzf',
                "args": [9, 91, 0, RadialDirections.EAST]
            },
            {
                "identifier": 'EVENT_351_action_queue_async_58_SUBSCRIPT_set_solidity_bits_3',
                "command": 'set_solidity_bits',
                "args": [[_0x0AFlags.BIT_4, _0x0AFlags.CANT_PASS_NPCS, _0x0AFlags.CANT_WALK_THROUGH, _0x0AFlags.BIT_7]]
            }
        ]
    },
    {
        "identifier": 'EVENT_351_ret_59',
        "command": 'ret'
    }
]
