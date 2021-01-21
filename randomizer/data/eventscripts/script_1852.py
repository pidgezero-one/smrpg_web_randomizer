from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data import items
script = [
    {
        "identifier": 'EVENT_1852_set_short_mem_0',
        "command": 'set_short_mem',
        "args": [0x7000, 0x70a8]
    },
    {
        "identifier": 'EVENT_1852_set_short_mem_1',
        "command": 'set_short_mem',
        "args": [0x70ae, 0x7000]
    },
    {
        "identifier": 'EVENT_1852_jmp_fork_mario_on_object_2',
        "command": 'jmp_fork_mario_on_object',
        "args": ['EVENT_1852_run_dialog_111', 'EVENT_1852_set_action_script_sync_68']
    },
    {
        "identifier": 'EVENT_1852_jmp_if_bit_set_3',
        "command": 'jmp_if_bit_set',
        "args": [0x7043, 2, 'EVENT_1852_stop_all_background_events_70']
    },
    {
        "identifier": 'EVENT_1852_jmp_if_bit_set_4',
        "command": 'jmp_if_bit_set',
        "args": [0x707b, 6, 'EVENT_1852_run_dialog_14']
    },
    {
        "identifier": 'EVENT_1852_set_bit_5',
        "command": 'set_bit',
        "args": [0x707b, 6]
    },
    {
        "identifier": 'EVENT_1852_run_dialog_6',
        "command": 'run_dialog',
        "args": [1312, AreaObjects.MEM_70A8, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]]
    },
    {
        "identifier": 'EVENT_1852_set_bit_7',
        "command": 'set_bit',
        "args": [0x7094, 4]
    },
    {
        "identifier": 'EVENT_1852_set_8',
        "command": 'set',
        "args": [0x70ab, 35]
    },
    {
        "identifier": 'EVENT_1852_run_event_as_subroutine_9',
        "command": 'run_event_as_subroutine',
        "args": [1739]
    },
    {
        "identifier": 'EVENT_1852_pause_10',
        "command": 'pause',
        "args": [20]
    },
    {
        "identifier": 'EVENT_1852_set_11',
        "command": 'set',
        "args": [0x70ab, 0]
    },
    {
        "identifier": 'EVENT_1852_run_event_as_subroutine_12',
        "command": 'run_event_as_subroutine',
        "args": [1739]
    },
    {
        "identifier": 'EVENT_1852_clear_bit_13',
        "command": 'clear_bit',
        "args": [0x7094, 4]
    },
    {
        "identifier": 'EVENT_1852_run_dialog_14',
        "command": 'run_dialog',
        "args": [1300, AreaObjects.MEM_70A8, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]]
    },
    {
        "identifier": 'EVENT_1852_jmp_if_dialog_option_b_15',
        "command": 'jmp_if_dialog_option_b',
        "args": ['EVENT_1852_pause_17']
    },
    {
        "identifier": 'EVENT_1852_jmp_16',
        "command": 'jmp',
        "args": ['EVENT_1852_pause_23']
    },
    {
        "identifier": 'EVENT_1852_pause_17',
        "command": 'pause',
        "args": [10]
    },
    {
        "identifier": 'EVENT_1852_set_action_script_async_18',
        "command": 'set_action_script_async',
        "args": [AreaObjects.MARIO, 671]
    },
    {
        "identifier": 'EVENT_1852_clear_bit_19',
        "command": 'clear_bit',
        "args": [0x7044, 7]
    },
    {
        "identifier": 'EVENT_1852_run_dialog_20',
        "command": 'run_dialog',
        "args": [1301, AreaObjects.MEM_70A8, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]]
    },
    {
        "identifier": 'EVENT_1852_set_action_script_sync_21',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.MARIO, 823]
    },
    {
        "identifier": 'EVENT_1852_ret_22',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_1852_pause_23',
        "command": 'pause',
        "args": [10]
    },
    {
        "identifier": 'EVENT_1852_set_action_script_async_24',
        "command": 'set_action_script_async',
        "args": [AreaObjects.MARIO, 670]
    },
    {
        "identifier": 'EVENT_1852_clear_bit_25',
        "command": 'clear_bit',
        "args": [0x7044, 7]
    },
    {
        "identifier": 'EVENT_1852_run_dialog_26',
        "command": 'run_dialog',
        "args": [1305, AreaObjects.NPC_17, [_0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]]
    },
    {
        "identifier": 'EVENT_1852_store_coin_amount_7000_27',
        "command": 'store_coin_amount_7000'
    },
    {
        "identifier": 'EVENT_1852_mem_compare_28',
        "command": 'mem_compare',
        "args": [0x7000, 5]
    },
    {
        "identifier": 'EVENT_1852_jmp_if_comparison_result_is_greater_or_equal_29',
        "command": 'jmp_if_comparison_result_is_greater_or_equal',
        "args": ['EVENT_1852_play_sound_33']
    },
    {
        "identifier": 'EVENT_1852_run_dialog_duration_30',
        "command": 'run_dialog_duration',
        "args": [1306, DialogDurations.SHORT, [_0x60Flags.ASYNC]]
    },
    {
        "identifier": 'EVENT_1852_set_action_script_sync_31',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.MARIO, 823]
    },
    {
        "identifier": 'EVENT_1852_ret_32',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_1852_play_sound_33',
        "command": 'play_sound',
        "args": [Sounds._055_LOSE_COINS_COIN_FOUNTAIN, 6]
    },
    {
        "identifier": 'EVENT_1852_set_34',
        "command": 'set',
        "args": [0x7000, 5]
    },
    {
        "identifier": 'EVENT_1852_dec_coins_35',
        "command": 'dec_coins'
    },
    {
        "identifier": 'EVENT_1852_jmp_if_bit_set_36',
        "command": 'jmp_if_bit_set',
        "args": [0x7094, 1, 'EVENT_1852_run_dialog_48']
    },
    {
        "identifier": 'EVENT_1852_run_dialog_37',
        "command": 'run_dialog',
        "args": [1302, AreaObjects.MEM_70A8, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]]
    },
    {
        "identifier": 'EVENT_1852_jmp_if_dialog_option_b_38',
        "command": 'jmp_if_dialog_option_b',
        "args": ['EVENT_1852_pause_45']
    },
    {
        "identifier": 'EVENT_1852_pause_39',
        "command": 'pause',
        "args": [10]
    },
    {
        "identifier": 'EVENT_1852_set_action_script_async_40',
        "command": 'set_action_script_async',
        "args": [AreaObjects.MARIO, 670]
    },
    {
        "identifier": 'EVENT_1852_clear_bit_41',
        "command": 'clear_bit',
        "args": [0x7044, 7]
    },
    {
        "identifier": 'EVENT_1852_set_bit_42',
        "command": 'set_bit',
        "args": [0x7094, 1]
    },
    {
        "identifier": 'EVENT_1852_run_dialog_43',
        "command": 'run_dialog',
        "args": [1303, AreaObjects.NPC_17, [_0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]]
    },
    {
        "identifier": 'EVENT_1852_jmp_44',
        "command": 'jmp',
        "args": ['EVENT_1852_run_dialog_48']
    },
    {
        "identifier": 'EVENT_1852_pause_45',
        "command": 'pause',
        "args": [10]
    },
    {
        "identifier": 'EVENT_1852_set_action_script_async_46',
        "command": 'set_action_script_async',
        "args": [AreaObjects.MARIO, 671]
    },
    {
        "identifier": 'EVENT_1852_clear_bit_47',
        "command": 'clear_bit',
        "args": [0x7044, 7]
    },
    {
        "identifier": 'EVENT_1852_run_dialog_48',
        "command": 'run_dialog',
        "args": [1304, AreaObjects.MEM_70A8, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]]
    },
    {
        "identifier": 'EVENT_1852_jmp_if_dialog_option_b_or_c_49',
        "command": 'jmp_if_dialog_option_b_or_c',
        "args": ['EVENT_1852_set_short_54', 'EVENT_1852_set_short_58']
    },
    {
        "identifier": 'EVENT_1852_set_short_50',
        "command": 'set_short',
        "args": [0x7026, 0x0005]
    },
    {
        "identifier": 'EVENT_1852_set_bit_51',
        "command": 'set_bit',
        "args": [0x7094, 3]
    },
    {
        "identifier": 'EVENT_1852_set_bit_52',
        "command": 'set_bit',
        "args": [0x707b, 7]
    },
    {
        "identifier": 'EVENT_1852_jmp_53',
        "command": 'jmp',
        "args": ['EVENT_1852_set_short_61']
    },
    {
        "identifier": 'EVENT_1852_set_short_54',
        "command": 'set_short',
        "args": [0x7026, 0x0008]
    },
    {
        "identifier": 'EVENT_1852_set_bit_55',
        "command": 'set_bit',
        "args": [0x7094, 3]
    },
    {
        "identifier": 'EVENT_1852_clear_bit_56',
        "command": 'clear_bit',
        "args": [0x707b, 7]
    },
    {
        "identifier": 'EVENT_1852_jmp_57',
        "command": 'jmp',
        "args": ['EVENT_1852_set_short_61']
    },
    {
        "identifier": 'EVENT_1852_set_short_58',
        "command": 'set_short',
        "args": [0x7026, 0x0001]
    },
    {
        "identifier": 'EVENT_1852_clear_bit_59',
        "command": 'clear_bit',
        "args": [0x7094, 3]
    },
    {
        "identifier": 'EVENT_1852_clear_bit_60',
        "command": 'clear_bit',
        "args": [0x707b, 7]
    },
    {
        "identifier": 'EVENT_1852_set_short_61',
        "command": 'set_short',
        "args": [0x702e, 0x0030]
    },
    {
        "identifier": 'EVENT_1852_set_short_62',
        "command": 'set_short',
        "args": [0x702c, 0x0064]
    },
    {
        "identifier": 'EVENT_1852_run_dialog_63',
        "command": 'run_dialog',
        "args": [1314, AreaObjects.MEM_70A8, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]]
    },
    {
        "identifier": 'EVENT_1852_set_bit_64',
        "command": 'set_bit',
        "args": [0x7043, 2]
    },
    {
        "identifier": 'EVENT_1852_set_short_65',
        "command": 'set_short',
        "args": [0x7028, 0x0001]
    },
    {
        "identifier": 'EVENT_1852_action_queue_async_66',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_17],
        "subscript": [
            {
                "identifier": 'EVENT_1852_action_queue_async_66_SUBSCRIPT_clear_solidity_bits_0',
                "command": 'clear_solidity_bits',
                "args": [[_0x0AFlags.BIT_4, _0x0AFlags.CANT_PASS_NPCS, _0x0AFlags.CANT_WALK_THROUGH, _0x0AFlags.BIT_7]]
            },
            {
                "identifier": 'EVENT_1852_action_queue_async_66_SUBSCRIPT_play_sound_1',
                "command": 'play_sound',
                "args": [Sounds._161_GHOST, 4]
            },
            {
                "identifier": 'EVENT_1852_action_queue_async_66_SUBSCRIPT_jump_to_height_2',
                "command": 'jump_to_height',
                "args": [128]
            },
            {
                "identifier": 'EVENT_1852_action_queue_async_66_SUBSCRIPT_start_loop_n_times_3',
                "command": 'start_loop_n_times',
                "args": [4]
            },
            {
                "identifier": 'EVENT_1852_action_queue_async_66_SUBSCRIPT_visibility_off_4',
                "command": 'visibility_off'
            },
            {
                "identifier": 'EVENT_1852_action_queue_async_66_SUBSCRIPT_pause_5',
                "command": 'pause',
                "args": [1]
            },
            {
                "identifier": 'EVENT_1852_action_queue_async_66_SUBSCRIPT_visibility_on_6',
                "command": 'visibility_on'
            },
            {
                "identifier": 'EVENT_1852_action_queue_async_66_SUBSCRIPT_pause_7',
                "command": 'pause',
                "args": [2]
            },
            {
                "identifier": 'EVENT_1852_action_queue_async_66_SUBSCRIPT_end_loop_8',
                "command": 'end_loop'
            },
            {
                "identifier": 'EVENT_1852_action_queue_async_66_SUBSCRIPT_floating_off_9',
                "command": 'floating_off'
            },
            {
                "identifier": 'EVENT_1852_action_queue_async_66_SUBSCRIPT_set_solidity_bits_10',
                "command": 'set_solidity_bits',
                "args": [[_0x0AFlags.BIT_4, _0x0AFlags.CANT_WALK_THROUGH]]
            },
            {
                "identifier": 'EVENT_1852_action_queue_async_66_SUBSCRIPT_transfer_to_xyzf_11',
                "command": 'transfer_to_xyzf',
                "args": [10, 76, 19, RadialDirections.EAST]
            },
            {
                "identifier": 'EVENT_1852_action_queue_async_66_SUBSCRIPT_face_southwest_12',
                "command": 'face_southwest'
            }
        ]
    },
    {
        "identifier": 'EVENT_1852_run_background_event_67',
        "command": 'run_background_event',
        "args": [1732, [_0x40Flags.RETURN_ON_LEVEL_EXIT]]
    },
    {
        "identifier": 'EVENT_1852_set_action_script_sync_68',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.MARIO, 823]
    },
    {
        "identifier": 'EVENT_1852_ret_69',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_1852_stop_all_background_events_70',
        "command": 'stop_all_background_events'
    },
    {
        "identifier": 'EVENT_1852_clear_bit_71',
        "command": 'clear_bit',
        "args": [0x7043, 0]
    },
    {
        "identifier": 'EVENT_1852_clear_bit_72',
        "command": 'clear_bit',
        "args": [0x7044, 3]
    },
    {
        "identifier": 'EVENT_1852_jmp_if_var_not_equals_short_73',
        "command": 'jmp_if_var_not_equals_short',
        "args": [0x7028, 3, 'EVENT_1852_run_dialog_76']
    },
    {
        "identifier": 'EVENT_1852_run_dialog_74',
        "command": 'run_dialog',
        "args": [1308, AreaObjects.NPC_17, [_0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]]
    },
    {
        "identifier": 'EVENT_1852_jmp_75',
        "command": 'jmp',
        "args": ['EVENT_1852_run_dialog_94']
    },
    {
        "identifier": 'EVENT_1852_run_dialog_76',
        "command": 'run_dialog',
        "args": [1307, AreaObjects.MEM_70A8, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]]
    },
    {
        "identifier": 'EVENT_1852_jmp_if_dialog_option_b_77',
        "command": 'jmp_if_dialog_option_b',
        "args": ['EVENT_1852_pause_91']
    },
    {
        "identifier": 'EVENT_1852_pause_78',
        "command": 'pause',
        "args": [10]
    },
    {
        "identifier": 'EVENT_1852_set_action_script_async_79',
        "command": 'set_action_script_async',
        "args": [AreaObjects.MARIO, 670]
    },
    {
        "identifier": 'EVENT_1852_clear_bit_80',
        "command": 'clear_bit',
        "args": [0x7044, 7]
    },
    {
        "identifier": 'EVENT_1852_add_short_81',
        "command": 'add_short',
        "args": [0x7028, 0x01]
    },
    {
        "identifier": 'EVENT_1852_mem_7000_shift_left_82',
        "command": 'mem_7000_shift_left',
        "args": [0x7026, 255]
    },
    {
        "identifier": 'EVENT_1852_add_short_83',
        "command": 'add_short',
        "args": [0x702e, 0xfff0]
    },
    {
        "identifier": 'EVENT_1852_add_short_84',
        "command": 'add_short',
        "args": [0x702c, 0xffec]
    },
    {
        "identifier": 'EVENT_1852_action_queue_async_85',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_1852_action_queue_async_85_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_1852_action_queue_async_85_SUBSCRIPT_clear_solidity_bits_1',
                "command": 'clear_solidity_bits',
                "args": [[_0x0AFlags.CANT_PASS_WALLS]]
            },
            {
                "identifier": 'EVENT_1852_action_queue_async_85_SUBSCRIPT_jump_to_height_2',
                "command": 'jump_to_height',
                "args": [108]
            },
            {
                "identifier": 'EVENT_1852_action_queue_async_85_SUBSCRIPT_walk_to_xy_coords_3',
                "command": 'walk_to_xy_coords',
                "args": [10, 76]
            },
            {
                "identifier": 'EVENT_1852_action_queue_async_85_SUBSCRIPT_pause_4',
                "command": 'pause',
                "args": [1]
            },
            {
                "identifier": 'EVENT_1852_action_queue_async_85_SUBSCRIPT_jmp_if_mario_in_air_5',
                "command": 'jmp_if_mario_in_air',
                "args": ['EVENT_1852_action_queue_async_85_SUBSCRIPT_pause_4']
            }
        ]
    },
    {
        "identifier": 'EVENT_1852_pause_86',
        "command": 'pause',
        "args": [1]
    },
    {
        "identifier": 'EVENT_1852_action_queue_sync_87',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_1852_action_queue_sync_87_SUBSCRIPT_floating_off_0',
                "command": 'floating_off'
            },
            {
                "identifier": 'EVENT_1852_action_queue_sync_87_SUBSCRIPT_sequence_playback_off_1',
                "command": 'sequence_playback_off'
            },
            {
                "identifier": 'EVENT_1852_action_queue_sync_87_SUBSCRIPT_set_animation_speed_2',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.SLOW, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_1852_action_queue_sync_87_SUBSCRIPT_add_z_coord_1_step_3',
                "command": 'add_z_coord_1_step'
            },
            {
                "identifier": 'EVENT_1852_action_queue_sync_87_SUBSCRIPT_set_animation_speed_4',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_1852_action_queue_sync_87_SUBSCRIPT_walk_to_xy_coords_5',
                "command": 'walk_to_xy_coords',
                "args": [20, 104]
            }
        ]
    },
    {
        "identifier": 'EVENT_1852_action_queue_async_88',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_17],
        "subscript": [
            {
                "identifier": 'EVENT_1852_action_queue_async_88_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.SLOW, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_1852_action_queue_async_88_SUBSCRIPT_add_z_coord_1_step_1',
                "command": 'add_z_coord_1_step'
            },
            {
                "identifier": 'EVENT_1852_action_queue_async_88_SUBSCRIPT_set_animation_speed_2',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_1852_action_queue_async_88_SUBSCRIPT_walk_to_xy_coords_3',
                "command": 'walk_to_xy_coords',
                "args": [20, 104]
            }
        ]
    },
    {
        "identifier": 'EVENT_1852_action_queue_async_89',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_1852_action_queue_async_89_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING, _0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_1852_action_queue_async_89_SUBSCRIPT_floating_on_1',
                "command": 'floating_on'
            },
            {
                "identifier": 'EVENT_1852_action_queue_async_89_SUBSCRIPT_sequence_playback_on_2',
                "command": 'sequence_playback_on'
            },
            {
                "identifier": 'EVENT_1852_action_queue_async_89_SUBSCRIPT_set_solidity_bits_3',
                "command": 'set_solidity_bits',
                "args": [[_0x0AFlags.CANT_PASS_WALLS]]
            }
        ]
    },
    {
        "identifier": 'EVENT_1852_jmp_90',
        "command": 'jmp',
        "args": ['EVENT_1852_action_queue_async_66']
    },
    {
        "identifier": 'EVENT_1852_pause_91',
        "command": 'pause',
        "args": [10]
    },
    {
        "identifier": 'EVENT_1852_set_action_script_async_92',
        "command": 'set_action_script_async',
        "args": [AreaObjects.MARIO, 671]
    },
    {
        "identifier": 'EVENT_1852_clear_bit_93',
        "command": 'clear_bit',
        "args": [0x7044, 7]
    },
    {
        "identifier": 'EVENT_1852_run_dialog_94',
        "command": 'run_dialog',
        "args": [1309, AreaObjects.MEM_70A8, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]]
    },
    {
        "identifier": 'EVENT_1852_action_queue_async_95',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_17],
        "subscript": [
            {
                "identifier": 'EVENT_1852_action_queue_async_95_SUBSCRIPT_set_sprite_sequence_0',
                "command": 'set_sprite_sequence',
                "args": [4, 0, [_0x08Flags.LOOPING_OFF]]
            },
            {
                "identifier": 'EVENT_1852_action_queue_async_95_SUBSCRIPT_pause_1',
                "command": 'pause',
                "args": [40]
            }
        ]
    },
    {
        "identifier": 'EVENT_1852_jmp_if_bit_set_96',
        "command": 'jmp_if_bit_set',
        "args": [0x7094, 3, 'EVENT_1852_play_sound_102']
    },
    {
        "identifier": 'EVENT_1852_play_sound_97',
        "command": 'play_sound',
        "args": [Sounds._094_FROG_COIN, 6]
    },
    {
        "identifier": 'EVENT_1852_set_short_mem_98',
        "command": 'set_short_mem',
        "args": [0x7000, 0x7026]
    },
    {
        "identifier": 'EVENT_1852_add_frog_coins_99',
        "command": 'add_frog_coins',
        "args": [0x7000]
    },
    {
        "identifier": 'EVENT_1852_run_dialog_100',
        "command": 'run_dialog',
        "args": [1310, AreaObjects.TOADSTOOL, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_1852_jmp_101',
        "command": 'jmp',
        "args": ['EVENT_1852_action_queue_sync_106']
    },
    {
        "identifier": 'EVENT_1852_play_sound_102',
        "command": 'play_sound',
        "args": [Sounds._013_COIN, 6]
    },
    {
        "identifier": 'EVENT_1852_set_short_mem_103',
        "command": 'set_short_mem',
        "args": [0x7000, 0x7026]
    },
    {
        "identifier": 'EVENT_1852_add_coins_104',
        "command": 'add_coins',
        "args": [0x7000]
    },
    {
        "identifier": 'EVENT_1852_run_dialog_105',
        "command": 'run_dialog',
        "args": [1311, AreaObjects.TOADSTOOL, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_1852_action_queue_sync_106',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_18],
        "subscript": [
            {
                "identifier": 'EVENT_1852_action_queue_sync_106_SUBSCRIPT_start_loop_n_times_0',
                "command": 'start_loop_n_times',
                "args": [3]
            },
            {
                "identifier": 'EVENT_1852_action_queue_sync_106_SUBSCRIPT_turn_clockwise_45_degrees_n_times_1',
                "command": 'turn_clockwise_45_degrees_n_times',
                "args": [2]
            },
            {
                "identifier": 'EVENT_1852_action_queue_sync_106_SUBSCRIPT_pause_2',
                "command": 'pause',
                "args": [1]
            },
            {
                "identifier": 'EVENT_1852_action_queue_sync_106_SUBSCRIPT_end_loop_3',
                "command": 'end_loop'
            }
        ]
    },
    {
        "identifier": 'EVENT_1852_action_queue_async_107',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_17],
        "subscript": [
            {
                "identifier": 'EVENT_1852_action_queue_async_107_SUBSCRIPT_clear_solidity_bits_0',
                "command": 'clear_solidity_bits',
                "args": [[_0x0AFlags.BIT_4, _0x0AFlags.CANT_PASS_NPCS, _0x0AFlags.CANT_WALK_THROUGH, _0x0AFlags.BIT_7]]
            },
            {
                "identifier": 'EVENT_1852_action_queue_async_107_SUBSCRIPT_play_sound_1',
                "command": 'play_sound',
                "args": [Sounds._161_GHOST, 4]
            },
            {
                "identifier": 'EVENT_1852_action_queue_async_107_SUBSCRIPT_jump_to_height_2',
                "command": 'jump_to_height',
                "args": [128]
            },
            {
                "identifier": 'EVENT_1852_action_queue_async_107_SUBSCRIPT_start_loop_n_times_3',
                "command": 'start_loop_n_times',
                "args": [4]
            },
            {
                "identifier": 'EVENT_1852_action_queue_async_107_SUBSCRIPT_visibility_off_4',
                "command": 'visibility_off'
            },
            {
                "identifier": 'EVENT_1852_action_queue_async_107_SUBSCRIPT_pause_5',
                "command": 'pause',
                "args": [1]
            },
            {
                "identifier": 'EVENT_1852_action_queue_async_107_SUBSCRIPT_visibility_on_6',
                "command": 'visibility_on'
            },
            {
                "identifier": 'EVENT_1852_action_queue_async_107_SUBSCRIPT_pause_7',
                "command": 'pause',
                "args": [2]
            },
            {
                "identifier": 'EVENT_1852_action_queue_async_107_SUBSCRIPT_end_loop_8',
                "command": 'end_loop'
            },
            {
                "identifier": 'EVENT_1852_action_queue_async_107_SUBSCRIPT_floating_off_9',
                "command": 'floating_off'
            },
            {
                "identifier": 'EVENT_1852_action_queue_async_107_SUBSCRIPT_set_solidity_bits_10',
                "command": 'set_solidity_bits',
                "args": [[_0x0AFlags.BIT_4, _0x0AFlags.CANT_WALK_THROUGH]]
            },
            {
                "identifier": 'EVENT_1852_action_queue_async_107_SUBSCRIPT_transfer_to_xyzf_11',
                "command": 'transfer_to_xyzf',
                "args": [20, 104, 18, RadialDirections.EAST]
            },
            {
                "identifier": 'EVENT_1852_action_queue_async_107_SUBSCRIPT_face_southwest_12',
                "command": 'face_southwest'
            }
        ]
    },
    {
        "identifier": 'EVENT_1852_clear_bit_108',
        "command": 'clear_bit',
        "args": [0x7043, 2]
    },
    {
        "identifier": 'EVENT_1852_set_action_script_sync_109',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.MARIO, 823]
    },
    {
        "identifier": 'EVENT_1852_ret_110',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_1852_run_dialog_111',
        "command": 'run_dialog',
        "args": [1312, AreaObjects.MEM_70A8, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]]
    },
    {
        "identifier": 'EVENT_1852_ret_112',
        "command": 'ret'
    }
]
