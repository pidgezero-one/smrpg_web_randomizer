from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data import items
script = [
    {
        "identifier": 'EVENT_1794_set_short_mem_0',
        "command": 'set_short_mem',
        "args": [0x7000, 0x70a8]
    },
    {
        "identifier": 'EVENT_1794_set_short_mem_1',
        "command": 'set_short_mem',
        "args": [0x70ae, 0x7000]
    },
    {
        "identifier": 'EVENT_1794_jmp_if_bit_set_2',
        "command": 'jmp_if_bit_set',
        "args": [0x7076, 0, 'EVENT_1794_action_queue_sync_77']
    },
    {
        "identifier": 'EVENT_1794_jmp_if_object_trigger_enabled_3',
        "command": 'jmp_if_object_trigger_enabled',
        "args": [AreaObjects.NPC_5, Rooms._263_LANDS_END_UNDERGROUND_AREA_01, 'EVENT_1794_run_dialog_75']
    },
    {
        "identifier": 'EVENT_1794_jmp_if_bit_set_4',
        "command": 'jmp_if_bit_set',
        "args": [0x7050, 0, 'EVENT_1794_jmp_if_bit_set_26']
    },
    {
        "identifier": 'EVENT_1794_store_coin_amount_7000_5',
        "command": 'store_coin_amount_7000'
    },
    {
        "identifier": 'EVENT_1794_mem_compare_6',
        "command": 'mem_compare',
        "args": [0x7000, 400]
    },
    {
        "identifier": 'EVENT_1794_jmp_if_comparison_result_is_lesser_7',
        "command": 'jmp_if_comparison_result_is_lesser',
        "args": ['EVENT_1794_run_dialog_70']
    },
    {
        "identifier": 'EVENT_1794_run_dialog_8',
        "command": 'run_dialog',
        "args": [1223, AreaObjects.MEM_70A8, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]]
    },
    {
        "identifier": 'EVENT_1794_jmp_if_dialog_option_b_9',
        "command": 'jmp_if_dialog_option_b',
        "args": ['EVENT_1794_pause_20']
    },
    {
        "identifier": 'EVENT_1794_pause_10',
        "command": 'pause',
        "args": [10]
    },
    {
        "identifier": 'EVENT_1794_set_action_script_async_11',
        "command": 'set_action_script_async',
        "args": [AreaObjects.MARIO, 670]
    },
    {
        "identifier": 'EVENT_1794_action_queue_async_12',
        "command": 'action_queue_async',
        "args": [AreaObjects.MEM_70A8],
        "subscript": [
            {
                "identifier": 'EVENT_1794_action_queue_async_12_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_1794_action_queue_async_12_SUBSCRIPT_sequence_looping_on_1',
                "command": 'sequence_looping_on'
            },
            {
                "identifier": 'EVENT_1794_action_queue_async_12_SUBSCRIPT_pause_2',
                "command": 'pause',
                "args": [30]
            },
            {
                "identifier": 'EVENT_1794_action_queue_async_12_SUBSCRIPT_set_animation_speed_3',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_SLOW, [_0x10Flags.SEQUENCE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_1794_set_13',
        "command": 'set',
        "args": [0x7000, 400]
    },
    {
        "identifier": 'EVENT_1794_dec_coins_14',
        "command": 'dec_coins'
    },
    {
        "identifier": 'EVENT_1794_play_sound_15',
        "command": 'play_sound',
        "args": [Sounds._055_LOSE_COINS_COIN_FOUNTAIN, 6]
    },
    {
        "identifier": 'EVENT_1794_set_16',
        "command": 'set',
        "args": [0x70aa, 38]
    },
    {
        "identifier": 'EVENT_1794_jmp_to_subroutine_17',
        "command": 'jmp_to_subroutine',
        "args": [0x4e23]
    },
    {
        "identifier": 'EVENT_1794_set_bit_18',
        "command": 'set_bit',
        "args": [0x704f, 7]
    },
    {
        "identifier": 'EVENT_1794_ret_19',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_1794_pause_20',
        "command": 'pause',
        "args": [10]
    },
    {
        "identifier": 'EVENT_1794_set_action_script_async_21',
        "command": 'set_action_script_async',
        "args": [AreaObjects.MARIO, 671]
    },
    {
        "identifier": 'EVENT_1794_run_dialog_22',
        "command": 'run_dialog',
        "args": [1225, AreaObjects.MEM_70A8, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]]
    },
    {
        "identifier": 'EVENT_1794_jmp_to_subroutine_23',
        "command": 'jmp_to_subroutine',
        "args": [0x4e6f]
    },
    {
        "identifier": 'EVENT_1794_remove_from_level_24',
        "command": 'remove_from_level',
        "args": [AreaObjects.NPC_16, Rooms._262_LANDS_END_UNDERGROUND_AREA_04_BUY_SUPER_STARS]
    },
    {
        "identifier": 'EVENT_1794_ret_25',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_1794_jmp_if_bit_set_26',
        "command": 'jmp_if_bit_set',
        "args": [0x7050, 3, 'EVENT_1794_store_coin_amount_7000_36']
    },
    {
        "identifier": 'EVENT_1794_run_dialog_27',
        "command": 'run_dialog',
        "args": [1224, AreaObjects.MEM_70A8, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]]
    },
    {
        "identifier": 'EVENT_1794_jmp_if_dialog_option_b_28',
        "command": 'jmp_if_dialog_option_b',
        "args": ['EVENT_1794_pause_20']
    },
    {
        "identifier": 'EVENT_1794_pause_29',
        "command": 'pause',
        "args": [10]
    },
    {
        "identifier": 'EVENT_1794_set_action_script_async_30',
        "command": 'set_action_script_async',
        "args": [AreaObjects.MARIO, 670]
    },
    {
        "identifier": 'EVENT_1794_run_dialog_31',
        "command": 'run_dialog',
        "args": [1226, AreaObjects.MEM_70A8, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]]
    },
    {
        "identifier": 'EVENT_1794_set_bit_32',
        "command": 'set_bit',
        "args": [0x7050, 3]
    },
    {
        "identifier": 'EVENT_1794_jmp_to_subroutine_33',
        "command": 'jmp_to_subroutine',
        "args": [0x4e6f]
    },
    {
        "identifier": 'EVENT_1794_remove_from_level_34',
        "command": 'remove_from_level',
        "args": [AreaObjects.NPC_16, Rooms._262_LANDS_END_UNDERGROUND_AREA_04_BUY_SUPER_STARS]
    },
    {
        "identifier": 'EVENT_1794_ret_35',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_1794_store_coin_amount_7000_36',
        "command": 'store_coin_amount_7000'
    },
    {
        "identifier": 'EVENT_1794_mem_compare_37',
        "command": 'mem_compare',
        "args": [0x7000, 800]
    },
    {
        "identifier": 'EVENT_1794_jmp_if_comparison_result_is_lesser_38',
        "command": 'jmp_if_comparison_result_is_lesser',
        "args": ['EVENT_1794_run_dialog_70']
    },
    {
        "identifier": 'EVENT_1794_run_dialog_39',
        "command": 'run_dialog',
        "args": [1227, AreaObjects.MEM_70A8, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]]
    },
    {
        "identifier": 'EVENT_1794_jmp_if_dialog_option_b_40',
        "command": 'jmp_if_dialog_option_b',
        "args": ['EVENT_1794_clear_bit_53']
    },
    {
        "identifier": 'EVENT_1794_pause_41',
        "command": 'pause',
        "args": [10]
    },
    {
        "identifier": 'EVENT_1794_set_action_script_async_42',
        "command": 'set_action_script_async',
        "args": [AreaObjects.MARIO, 670]
    },
    {
        "identifier": 'EVENT_1794_action_queue_async_43',
        "command": 'action_queue_async',
        "args": [AreaObjects.MEM_70A8],
        "subscript": [
            {
                "identifier": 'EVENT_1794_action_queue_async_43_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_1794_action_queue_async_43_SUBSCRIPT_sequence_looping_on_1',
                "command": 'sequence_looping_on'
            },
            {
                "identifier": 'EVENT_1794_action_queue_async_43_SUBSCRIPT_pause_2',
                "command": 'pause',
                "args": [30]
            },
            {
                "identifier": 'EVENT_1794_action_queue_async_43_SUBSCRIPT_set_animation_speed_3',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_SLOW, [_0x10Flags.SEQUENCE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_1794_set_44',
        "command": 'set',
        "args": [0x7000, 800]
    },
    {
        "identifier": 'EVENT_1794_dec_coins_45',
        "command": 'dec_coins'
    },
    {
        "identifier": 'EVENT_1794_play_sound_46',
        "command": 'play_sound',
        "args": [Sounds._055_LOSE_COINS_COIN_FOUNTAIN, 6]
    },
    {
        "identifier": 'EVENT_1794_set_47',
        "command": 'set',
        "args": [0x70aa, 39]
    },
    {
        "identifier": 'EVENT_1794_jmp_to_subroutine_48',
        "command": 'jmp_to_subroutine',
        "args": [0x4e23]
    },
    {
        "identifier": 'EVENT_1794_set_bit_49',
        "command": 'set_bit',
        "args": [0x7050, 1]
    },
    {
        "identifier": 'EVENT_1794_clear_bit_50',
        "command": 'clear_bit',
        "args": [0x7050, 3]
    },
    {
        "identifier": 'EVENT_1794_remove_from_level_51',
        "command": 'remove_from_level',
        "args": [AreaObjects.NPC_16, Rooms._262_LANDS_END_UNDERGROUND_AREA_04_BUY_SUPER_STARS]
    },
    {
        "identifier": 'EVENT_1794_ret_52',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_1794_clear_bit_53',
        "command": 'clear_bit',
        "args": [0x7050, 3]
    },
    {
        "identifier": 'EVENT_1794_jmp_54',
        "command": 'jmp',
        "args": ['EVENT_1794_pause_20']
    },
    {
        "identifier": 'EVENT_1794_action_queue_sync_55',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_16],
        "subscript": [
            {
                "identifier": 'EVENT_1794_action_queue_sync_55_SUBSCRIPT_play_sound_0',
                "command": 'play_sound',
                "args": [Sounds._033_JUMPING_BOUNCING_FISH, 4]
            },
            {
                "identifier": 'EVENT_1794_action_queue_sync_55_SUBSCRIPT_jump_to_height_1',
                "command": 'jump_to_height',
                "args": [112]
            },
            {
                "identifier": 'EVENT_1794_action_queue_sync_55_SUBSCRIPT_start_loop_n_times_2',
                "command": 'start_loop_n_times',
                "args": [11]
            },
            {
                "identifier": 'EVENT_1794_action_queue_sync_55_SUBSCRIPT_turn_clockwise_45_degrees_n_times_3',
                "command": 'turn_clockwise_45_degrees_n_times',
                "args": [6]
            },
            {
                "identifier": 'EVENT_1794_action_queue_sync_55_SUBSCRIPT_pause_4',
                "command": 'pause',
                "args": [1]
            },
            {
                "identifier": 'EVENT_1794_action_queue_sync_55_SUBSCRIPT_end_loop_5',
                "command": 'end_loop'
            }
        ]
    },
    {
        "identifier": 'EVENT_1794_pause_56',
        "command": 'pause',
        "args": [20]
    },
    {
        "identifier": 'EVENT_1794_set_short_57',
        "command": 'set_short',
        "args": [0x7034, 0x0006]
    },
    {
        "identifier": 'EVENT_1794_set_7010_to_object_xyz_58',
        "command": 'set_7010_to_object_xyz',
        "args": [AreaObjects.MEM_70AA]
    },
    {
        "identifier": 'EVENT_1794_play_sound_59',
        "command": 'play_sound',
        "args": [Sounds._060_DYNAMITE_BOMB_EXPLOSION, 6]
    },
    {
        "identifier": 'EVENT_1794_start_loop_n_times_60',
        "command": 'start_loop_n_times',
        "args": [8]
    },
    {
        "identifier": 'EVENT_1794_pause_61',
        "command": 'pause',
        "args": [1]
    },
    {
        "identifier": 'EVENT_1794_create_packet_at_7010_coords_jmp_if_null_62',
        "command": 'create_packet_at_7010_coords_jmp_if_null',
        "args": [NPCPackets._032_BLUE_CLOUD, 'EVENT_1794_pause_61']
    },
    {
        "identifier": 'EVENT_1794_pause_63',
        "command": 'pause',
        "args": [5]
    },
    {
        "identifier": 'EVENT_1794_add_short_64',
        "command": 'add_short',
        "args": [0x7034, 0x0003]
    },
    {
        "identifier": 'EVENT_1794_add_short_65',
        "command": 'add_short',
        "args": [0x7014, 0x0040]
    },
    {
        "identifier": 'EVENT_1794_end_loop_66',
        "command": 'end_loop'
    },
    {
        "identifier": 'EVENT_1794_action_queue_async_67',
        "command": 'action_queue_async',
        "args": [AreaObjects.MEM_70AA],
        "subscript": [
            {
                "identifier": 'EVENT_1794_action_queue_async_67_SUBSCRIPT_start_loop_n_times_0',
                "command": 'start_loop_n_times',
                "args": [4]
            },
            {
                "identifier": 'EVENT_1794_action_queue_async_67_SUBSCRIPT_visibility_off_1',
                "command": 'visibility_off'
            },
            {
                "identifier": 'EVENT_1794_action_queue_async_67_SUBSCRIPT_pause_2',
                "command": 'pause',
                "args": [2]
            },
            {
                "identifier": 'EVENT_1794_action_queue_async_67_SUBSCRIPT_visibility_on_3',
                "command": 'visibility_on'
            },
            {
                "identifier": 'EVENT_1794_action_queue_async_67_SUBSCRIPT_pause_4',
                "command": 'pause',
                "args": [4]
            },
            {
                "identifier": 'EVENT_1794_action_queue_async_67_SUBSCRIPT_end_loop_5',
                "command": 'end_loop'
            },
            {
                "identifier": 'EVENT_1794_action_queue_async_67_SUBSCRIPT_start_loop_n_times_6',
                "command": 'start_loop_n_times',
                "args": [2]
            },
            {
                "identifier": 'EVENT_1794_action_queue_async_67_SUBSCRIPT_visibility_off_7',
                "command": 'visibility_off'
            },
            {
                "identifier": 'EVENT_1794_action_queue_async_67_SUBSCRIPT_pause_8',
                "command": 'pause',
                "args": [2]
            },
            {
                "identifier": 'EVENT_1794_action_queue_async_67_SUBSCRIPT_visibility_on_9',
                "command": 'visibility_on'
            },
            {
                "identifier": 'EVENT_1794_action_queue_async_67_SUBSCRIPT_pause_10',
                "command": 'pause',
                "args": [8]
            },
            {
                "identifier": 'EVENT_1794_action_queue_async_67_SUBSCRIPT_end_loop_11',
                "command": 'end_loop'
            }
        ]
    },
    {
        "identifier": 'EVENT_1794_set_action_script_sync_68',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.MEM_70AA, 14]
    },
    {
        "identifier": 'EVENT_1794_jmp_69',
        "command": 'jmp',
        "args": ['EVENT_1794_set_72']
    },
    {
        "identifier": 'EVENT_1794_run_dialog_70',
        "command": 'run_dialog',
        "args": [1222, AreaObjects.MEM_70A8, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]]
    },
    {
        "identifier": 'EVENT_1794_ret_71',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_1794_set_72',
        "command": 'set',
        "args": [0x70aa, 36]
    },
    {
        "identifier": 'EVENT_1794_action_queue_async_73',
        "command": 'action_queue_async',
        "args": [AreaObjects.MEM_70AA],
        "subscript": [
            {
                "identifier": 'EVENT_1794_action_queue_async_73_SUBSCRIPT_play_sound_0',
                "command": 'play_sound',
                "args": [Sounds._059_HOVERING_FROGFUCIUS, 4]
            },
            {
                "identifier": 'EVENT_1794_action_queue_async_73_SUBSCRIPT_sequence_playback_off_1',
                "command": 'sequence_playback_off'
            },
            {
                "identifier": 'EVENT_1794_action_queue_async_73_SUBSCRIPT_clear_solidity_bits_2',
                "command": 'clear_solidity_bits',
                "args": [[_0x0AFlags.BIT_4, _0x0AFlags.CANT_PASS_NPCS, _0x0AFlags.CANT_WALK_THROUGH, _0x0AFlags.BIT_7]]
            },
            {
                "identifier": 'EVENT_1794_action_queue_async_73_SUBSCRIPT_set_animation_speed_3',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.SLOW, [_0x10Flags.WALKING, _0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_1794_action_queue_async_73_SUBSCRIPT_shift_z_up_steps_4',
                "command": 'shift_z_up_steps',
                "args": [2]
            },
            {
                "identifier": 'EVENT_1794_action_queue_async_73_SUBSCRIPT_start_loop_n_times_5',
                "command": 'start_loop_n_times',
                "args": [3]
            },
            {
                "identifier": 'EVENT_1794_action_queue_async_73_SUBSCRIPT_pause_6',
                "command": 'pause',
                "args": [1]
            },
            {
                "identifier": 'EVENT_1794_action_queue_async_73_SUBSCRIPT_visibility_on_7',
                "command": 'visibility_on'
            },
            {
                "identifier": 'EVENT_1794_action_queue_async_73_SUBSCRIPT_pause_8',
                "command": 'pause',
                "args": [6]
            },
            {
                "identifier": 'EVENT_1794_action_queue_async_73_SUBSCRIPT_visibility_off_9',
                "command": 'visibility_off'
            },
            {
                "identifier": 'EVENT_1794_action_queue_async_73_SUBSCRIPT_end_loop_10',
                "command": 'end_loop'
            },
            {
                "identifier": 'EVENT_1794_action_queue_async_73_SUBSCRIPT_pause_11',
                "command": 'pause',
                "args": [1]
            },
            {
                "identifier": 'EVENT_1794_action_queue_async_73_SUBSCRIPT_set_short_12',
                "command": 'set_short',
                "args": [0x7034, 0xffff]
            },
            {
                "identifier": 'EVENT_1794_action_queue_async_73_SUBSCRIPT_create_packet_at_object_coords_jmp_if_null_13',
                "command": 'create_packet_at_object_coords_jmp_if_null',
                "args": [NPCPackets._032_BLUE_CLOUD, AreaObjects.MEM_70AA, 'EVENT_1794_action_queue_async_73_SUBSCRIPT_pause_11']
            },
            {
                "identifier": 'EVENT_1794_action_queue_async_73_SUBSCRIPT_play_sound_14',
                "command": 'play_sound',
                "args": [Sounds._161_GHOST, 4]
            }
        ]
    },
    {
        "identifier": 'EVENT_1794_ret_74',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_1794_run_dialog_75',
        "command": 'run_dialog',
        "args": [1221, AreaObjects.MEM_70A8, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]]
    },
    {
        "identifier": 'EVENT_1794_ret_76',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_1794_action_queue_sync_77',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_16],
        "subscript": [
            {
                "identifier": 'EVENT_1794_action_queue_sync_77_SUBSCRIPT_clear_solidity_bits_0',
                "command": 'clear_solidity_bits',
                "args": [[_0x0AFlags.BIT_4, _0x0AFlags.CANT_PASS_NPCS, _0x0AFlags.CANT_WALK_THROUGH, _0x0AFlags.BIT_7]]
            },
            {
                "identifier": 'EVENT_1794_action_queue_sync_77_SUBSCRIPT_play_sound_1',
                "command": 'play_sound',
                "args": [Sounds._066_KICK_BALL_SHELL, 4]
            },
            {
                "identifier": 'EVENT_1794_action_queue_sync_77_SUBSCRIPT_jump_to_height_2',
                "command": 'jump_to_height',
                "args": [128]
            },
            {
                "identifier": 'EVENT_1794_action_queue_sync_77_SUBSCRIPT_start_loop_n_times_3',
                "command": 'start_loop_n_times',
                "args": [11]
            },
            {
                "identifier": 'EVENT_1794_action_queue_sync_77_SUBSCRIPT_pause_4',
                "command": 'pause',
                "args": [4]
            },
            {
                "identifier": 'EVENT_1794_action_queue_sync_77_SUBSCRIPT_turn_clockwise_45_degrees_n_times_5',
                "command": 'turn_clockwise_45_degrees_n_times',
                "args": [2]
            },
            {
                "identifier": 'EVENT_1794_action_queue_sync_77_SUBSCRIPT_end_loop_6',
                "command": 'end_loop'
            },
            {
                "identifier": 'EVENT_1794_action_queue_sync_77_SUBSCRIPT_set_solidity_bits_7',
                "command": 'set_solidity_bits',
                "args": [[_0x0AFlags.BIT_4, _0x0AFlags.CANT_WALK_THROUGH]]
            }
        ]
    },
    {
        "identifier": 'EVENT_1794_ret_78',
        "command": 'ret'
    }
]
