from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data import items
script = [
    {
        "identifier": 'EVENT_2634_jmp_if_bit_clear_0',
        "command": 'jmp_if_bit_clear',
        "args": [0x7043, 0, 'EVENT_2634_ret_112']
    },
    {
        "identifier": 'EVENT_2634_jmp_if_bit_set_1',
        "command": 'jmp_if_bit_set',
        "args": [0x7043, 1, 'EVENT_2634_jmp_if_bit_set_38']
    },
    {
        "identifier": 'EVENT_2634_set_bit_2',
        "command": 'set_bit',
        "args": [0x7043, 1]
    },
    {
        "identifier": 'EVENT_2634_clear_bit_3',
        "command": 'clear_bit',
        "args": [0x7045, 0]
    },
    {
        "identifier": 'EVENT_2634_clear_bit_4',
        "command": 'clear_bit',
        "args": [0x7045, 1]
    },
    {
        "identifier": 'EVENT_2634_clear_bit_5',
        "command": 'clear_bit',
        "args": [0x7045, 2]
    },
    {
        "identifier": 'EVENT_2634_clear_bit_6',
        "command": 'clear_bit',
        "args": [0x7045, 3]
    },
    {
        "identifier": 'EVENT_2634_clear_bit_7',
        "command": 'clear_bit',
        "args": [0x7045, 4]
    },
    {
        "identifier": 'EVENT_2634_clear_bit_8',
        "command": 'clear_bit',
        "args": [0x7045, 5]
    },
    {
        "identifier": 'EVENT_2634_jmp_if_random_above_66_9',
        "command": 'jmp_if_random_above_66',
        "args": ['EVENT_2634_set_bit_11']
    },
    {
        "identifier": 'EVENT_2634_jmp_10',
        "command": 'jmp',
        "args": ['EVENT_2634_jmp_if_random_above_66_14']
    },
    {
        "identifier": 'EVENT_2634_set_bit_11',
        "command": 'set_bit',
        "args": [0x7045, 0]
    },
    {
        "identifier": 'EVENT_2634_jmp_12',
        "command": 'jmp',
        "args": ['EVENT_2634_jmp_if_random_above_66_14']
    },
    {
        "identifier": 'EVENT_2634_set_bit_13',
        "command": 'set_bit',
        "args": [0x7045, 1]
    },
    {
        "identifier": 'EVENT_2634_jmp_if_random_above_66_14',
        "command": 'jmp_if_random_above_66',
        "args": ['EVENT_2634_set_bit_16']
    },
    {
        "identifier": 'EVENT_2634_jmp_15',
        "command": 'jmp',
        "args": ['EVENT_2634_jmp_if_random_above_66_19']
    },
    {
        "identifier": 'EVENT_2634_set_bit_16',
        "command": 'set_bit',
        "args": [0x7045, 2]
    },
    {
        "identifier": 'EVENT_2634_jmp_17',
        "command": 'jmp',
        "args": ['EVENT_2634_jmp_if_random_above_66_19']
    },
    {
        "identifier": 'EVENT_2634_set_bit_18',
        "command": 'set_bit',
        "args": [0x7045, 3]
    },
    {
        "identifier": 'EVENT_2634_jmp_if_random_above_66_19',
        "command": 'jmp_if_random_above_66',
        "args": ['EVENT_2634_set_bit_21']
    },
    {
        "identifier": 'EVENT_2634_jmp_20',
        "command": 'jmp',
        "args": ['EVENT_2634_pause_action_script_24']
    },
    {
        "identifier": 'EVENT_2634_set_bit_21',
        "command": 'set_bit',
        "args": [0x7045, 4]
    },
    {
        "identifier": 'EVENT_2634_jmp_22',
        "command": 'jmp',
        "args": ['EVENT_2634_pause_action_script_24']
    },
    {
        "identifier": 'EVENT_2634_set_bit_23',
        "command": 'set_bit',
        "args": [0x7045, 5]
    },
    {
        "identifier": 'EVENT_2634_pause_action_script_24',
        "command": 'pause_action_script',
        "args": [AreaObjects.NPC_3]
    },
    {
        "identifier": 'EVENT_2634_action_queue_sync_25',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_3],
        "subscript": [
            {
                "identifier": 'EVENT_2634_action_queue_sync_25_SUBSCRIPT_sequence_looping_on_0',
                "command": 'sequence_looping_on'
            },
            {
                "identifier": 'EVENT_2634_action_queue_sync_25_SUBSCRIPT_set_sprite_sequence_1',
                "command": 'set_sprite_sequence',
                "args": [1, 0, [_0x08Flags.LOOPING_OFF]]
            },
            {
                "identifier": 'EVENT_2634_action_queue_sync_25_SUBSCRIPT_pause_2',
                "command": 'pause',
                "args": [6]
            },
            {
                "identifier": 'EVENT_2634_action_queue_sync_25_SUBSCRIPT_set_sprite_sequence_3',
                "command": 'set_sprite_sequence',
                "args": [2, 0, [_0x08Flags.READ_AS_SEQUENCE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_2634_pause_26',
        "command": 'pause',
        "args": [6]
    },
    {
        "identifier": 'EVENT_2634_summon_to_current_level_27',
        "command": 'summon_to_current_level',
        "args": [AreaObjects.NPC_4]
    },
    {
        "identifier": 'EVENT_2634_summon_to_current_level_28',
        "command": 'summon_to_current_level',
        "args": [AreaObjects.NPC_5]
    },
    {
        "identifier": 'EVENT_2634_summon_to_current_level_29',
        "command": 'summon_to_current_level',
        "args": [AreaObjects.NPC_6]
    },
    {
        "identifier": 'EVENT_2634_pause_30',
        "command": 'pause',
        "args": [1]
    },
    {
        "identifier": 'EVENT_2634_action_queue_sync_31',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_4],
        "subscript": [
            {
                "identifier": 'EVENT_2634_action_queue_sync_31_SUBSCRIPT_shadow_off_0',
                "command": 'shadow_off'
            },
            {
                "identifier": 'EVENT_2634_action_queue_sync_31_SUBSCRIPT_set_animation_speed_1',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FASTEST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_2634_action_queue_sync_31_SUBSCRIPT_shift_west_pixels_2',
                "command": 'shift_west_pixels',
                "args": [17]
            }
        ]
    },
    {
        "identifier": 'EVENT_2634_action_queue_async_32',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_6],
        "subscript": [
            {
                "identifier": 'EVENT_2634_action_queue_async_32_SUBSCRIPT_shadow_off_0',
                "command": 'shadow_off'
            },
            {
                "identifier": 'EVENT_2634_action_queue_async_32_SUBSCRIPT_set_animation_speed_1',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FASTEST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_2634_action_queue_async_32_SUBSCRIPT_shift_east_pixels_2',
                "command": 'shift_east_pixels',
                "args": [17]
            }
        ]
    },
    {
        "identifier": 'EVENT_2634_play_sound_33',
        "command": 'play_sound',
        "args": [Sounds._153_SLOT_MACHINES, 6]
    },
    {
        "identifier": 'EVENT_2634_set_action_script_sync_34',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_4, 205]
    },
    {
        "identifier": 'EVENT_2634_set_action_script_sync_35',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_5, 206]
    },
    {
        "identifier": 'EVENT_2634_set_action_script_sync_36',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_6, 207]
    },
    {
        "identifier": 'EVENT_2634_ret_37',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_2634_jmp_if_bit_set_38',
        "command": 'jmp_if_bit_set',
        "args": [0x7043, 2, 'EVENT_2634_jmp_if_bit_set_44']
    },
    {
        "identifier": 'EVENT_2634_set_bit_39',
        "command": 'set_bit',
        "args": [0x7043, 2]
    },
    {
        "identifier": 'EVENT_2634_pause_action_script_40',
        "command": 'pause_action_script',
        "args": [AreaObjects.NPC_4]
    },
    {
        "identifier": 'EVENT_2634_pause_41',
        "command": 'pause',
        "args": [12]
    },
    {
        "identifier": 'EVENT_2634_play_sound_42',
        "command": 'play_sound',
        "args": [Sounds._153_SLOT_MACHINES, 6]
    },
    {
        "identifier": 'EVENT_2634_ret_43',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_2634_jmp_if_bit_set_44',
        "command": 'jmp_if_bit_set',
        "args": [0x7043, 3, 'EVENT_2634_pause_action_script_50']
    },
    {
        "identifier": 'EVENT_2634_set_bit_45',
        "command": 'set_bit',
        "args": [0x7043, 3]
    },
    {
        "identifier": 'EVENT_2634_pause_action_script_46',
        "command": 'pause_action_script',
        "args": [AreaObjects.NPC_5]
    },
    {
        "identifier": 'EVENT_2634_pause_47',
        "command": 'pause',
        "args": [12]
    },
    {
        "identifier": 'EVENT_2634_play_sound_48',
        "command": 'play_sound',
        "args": [Sounds._153_SLOT_MACHINES, 6]
    },
    {
        "identifier": 'EVENT_2634_ret_49',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_2634_pause_action_script_50',
        "command": 'pause_action_script',
        "args": [AreaObjects.NPC_6]
    },
    {
        "identifier": 'EVENT_2634_pause_51',
        "command": 'pause',
        "args": [16]
    },
    {
        "identifier": 'EVENT_2634_action_queue_sync_52',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_4],
        "subscript": [
            {
                "identifier": 'EVENT_2634_action_queue_sync_52_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_2634_action_queue_sync_52_SUBSCRIPT_shift_east_pixels_1',
                "command": 'shift_east_pixels',
                "args": [17]
            }
        ]
    },
    {
        "identifier": 'EVENT_2634_action_queue_async_53',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_6],
        "subscript": [
            {
                "identifier": 'EVENT_2634_action_queue_async_53_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_2634_action_queue_async_53_SUBSCRIPT_shift_west_pixels_1',
                "command": 'shift_west_pixels',
                "args": [17]
            }
        ]
    },
    {
        "identifier": 'EVENT_2634_remove_from_current_level_54',
        "command": 'remove_from_current_level',
        "args": [AreaObjects.NPC_4]
    },
    {
        "identifier": 'EVENT_2634_remove_from_current_level_55',
        "command": 'remove_from_current_level',
        "args": [AreaObjects.NPC_5]
    },
    {
        "identifier": 'EVENT_2634_remove_from_current_level_56',
        "command": 'remove_from_current_level',
        "args": [AreaObjects.NPC_6]
    },
    {
        "identifier": 'EVENT_2634_set_7010_to_object_xyz_57',
        "command": 'set_7010_to_object_xyz',
        "args": [AreaObjects.NPC_3]
    },
    {
        "identifier": 'EVENT_2634_set_short_mem_58',
        "command": 'set_short_mem',
        "args": [0x7000, 0x7014]
    },
    {
        "identifier": 'EVENT_2634_add_59',
        "command": 'add',
        "args": [0x7000, 256]
    },
    {
        "identifier": 'EVENT_2634_set_short_mem_60',
        "command": 'set_short_mem',
        "args": [0x7014, 0x7000]
    },
    {
        "identifier": 'EVENT_2634_create_packet_at_7010_coords_jmp_if_null_61',
        "command": 'create_packet_at_7010_coords_jmp_if_null',
        "args": [NPCPackets._052_BOMB_EXPLOSION_FASTER, 'EVENT_2634_pause_62']
    },
    {
        "identifier": 'EVENT_2634_pause_62',
        "command": 'pause',
        "args": [16]
    },
    {
        "identifier": 'EVENT_2634_jmp_if_var_equals_byte_63',
        "command": 'jmp_if_var_equals_byte',
        "args": [0x70c0, 0, 'EVENT_2634_jmp_if_var_equals_byte_66']
    },
    {
        "identifier": 'EVENT_2634_jmp_if_var_equals_byte_64',
        "command": 'jmp_if_var_equals_byte',
        "args": [0x70c0, 1, 'EVENT_2634_jmp_if_var_equals_byte_68']
    },
    {
        "identifier": 'EVENT_2634_jmp_if_var_equals_byte_65',
        "command": 'jmp_if_var_equals_byte',
        "args": [0x70c0, 2, 'EVENT_2634_jmp_if_var_equals_byte_70']
    },
    {
        "identifier": 'EVENT_2634_jmp_if_var_equals_byte_66',
        "command": 'jmp_if_var_equals_byte',
        "args": [0x70c1, 0, 'EVENT_2634_jmp_if_var_equals_byte_72']
    },
    {
        "identifier": 'EVENT_2634_jmp_67',
        "command": 'jmp',
        "args": ['EVENT_2634_play_sound_86']
    },
    {
        "identifier": 'EVENT_2634_jmp_if_var_equals_byte_68',
        "command": 'jmp_if_var_equals_byte',
        "args": [0x70c1, 1, 'EVENT_2634_jmp_if_var_equals_byte_74']
    },
    {
        "identifier": 'EVENT_2634_jmp_69',
        "command": 'jmp',
        "args": ['EVENT_2634_play_sound_86']
    },
    {
        "identifier": 'EVENT_2634_jmp_if_var_equals_byte_70',
        "command": 'jmp_if_var_equals_byte',
        "args": [0x70c1, 2, 'EVENT_2634_jmp_if_var_equals_byte_76']
    },
    {
        "identifier": 'EVENT_2634_jmp_71',
        "command": 'jmp',
        "args": ['EVENT_2634_play_sound_86']
    },
    {
        "identifier": 'EVENT_2634_jmp_if_var_equals_byte_72',
        "command": 'jmp_if_var_equals_byte',
        "args": [0x70c2, 0, 'EVENT_2634_set_7010_to_object_xyz_78']
    },
    {
        "identifier": 'EVENT_2634_jmp_73',
        "command": 'jmp',
        "args": ['EVENT_2634_play_sound_86']
    },
    {
        "identifier": 'EVENT_2634_jmp_if_var_equals_byte_74',
        "command": 'jmp_if_var_equals_byte',
        "args": [0x70c2, 1, 'EVENT_2634_set_7010_to_object_xyz_78']
    },
    {
        "identifier": 'EVENT_2634_jmp_75',
        "command": 'jmp',
        "args": ['EVENT_2634_play_sound_86']
    },
    {
        "identifier": 'EVENT_2634_jmp_if_var_equals_byte_76',
        "command": 'jmp_if_var_equals_byte',
        "args": [0x70c2, 2, 'EVENT_2634_set_7010_to_object_xyz_78']
    },
    {
        "identifier": 'EVENT_2634_jmp_77',
        "command": 'jmp',
        "args": ['EVENT_2634_play_sound_86']
    },
    {
        "identifier": 'EVENT_2634_set_7010_to_object_xyz_78',
        "command": 'set_7010_to_object_xyz',
        "args": [AreaObjects.NPC_3]
    },
    {
        "identifier": 'EVENT_2634_set_short_mem_79',
        "command": 'set_short_mem',
        "args": [0x7000, 0x7014]
    },
    {
        "identifier": 'EVENT_2634_add_80',
        "command": 'add',
        "args": [0x7000, 256]
    },
    {
        "identifier": 'EVENT_2634_set_short_mem_81',
        "command": 'set_short_mem',
        "args": [0x7014, 0x7000]
    },
    {
        "identifier": 'EVENT_2634_play_sound_82',
        "command": 'play_sound',
        "args": [Sounds._094_FROG_COIN, 6]
    },
    {
        "identifier": 'EVENT_2634_create_packet_at_7010_coords_jmp_if_null_83',
        "command": 'create_packet_at_7010_coords_jmp_if_null',
        "args": [NPCPackets._019_FROG_COIN, 'EVENT_2634_jmp_85']
    },
    {
        "identifier": 'EVENT_2634_add_frog_coins_84',
        "command": 'add_frog_coins',
        "args": [1]
    },
    {
        "identifier": 'EVENT_2634_jmp_85',
        "command": 'jmp',
        "args": ['EVENT_2634_action_queue_async_88']
    },
    {
        "identifier": 'EVENT_2634_play_sound_86',
        "command": 'play_sound',
        "args": [Sounds._105_SURPRISE, 6]
    },
    {
        "identifier": 'EVENT_2634_action_queue_async_87',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_5],
        "subscript": [
            {
                "identifier": 'EVENT_2634_action_queue_async_87_SUBSCRIPT_visibility_on_0',
                "command": 'visibility_on'
            },
            {
                "identifier": 'EVENT_2634_action_queue_async_87_SUBSCRIPT_set_sprite_sequence_1',
                "command": 'set_sprite_sequence',
                "args": [4, 0, [_0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_2634_action_queue_async_87_SUBSCRIPT_pause_2',
                "command": 'pause',
                "args": [24]
            },
            {
                "identifier": 'EVENT_2634_action_queue_async_87_SUBSCRIPT_visibility_off_3',
                "command": 'visibility_off'
            }
        ]
    },
    {
        "identifier": 'EVENT_2634_action_queue_async_88',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_3],
        "subscript": [
            {
                "identifier": 'EVENT_2634_action_queue_async_88_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [16]
            },
            {
                "identifier": 'EVENT_2634_action_queue_async_88_SUBSCRIPT_set_animation_speed_1',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_2634_action_queue_async_88_SUBSCRIPT_set_sprite_sequence_2',
                "command": 'set_sprite_sequence',
                "args": [3, 0, [_0x08Flags.LOOPING_OFF]]
            }
        ]
    },
    {
        "identifier": 'EVENT_2634_clear_bit_89',
        "command": 'clear_bit',
        "args": [0x7043, 0]
    },
    {
        "identifier": 'EVENT_2634_clear_bit_90',
        "command": 'clear_bit',
        "args": [0x7043, 1]
    },
    {
        "identifier": 'EVENT_2634_clear_bit_91',
        "command": 'clear_bit',
        "args": [0x7043, 2]
    },
    {
        "identifier": 'EVENT_2634_clear_bit_92',
        "command": 'clear_bit',
        "args": [0x7043, 3]
    },
    {
        "identifier": 'EVENT_2634_set_93',
        "command": 'set',
        "args": [0x70c0, 0]
    },
    {
        "identifier": 'EVENT_2634_set_94',
        "command": 'set',
        "args": [0x70c1, 0]
    },
    {
        "identifier": 'EVENT_2634_set_95',
        "command": 'set',
        "args": [0x70c2, 0]
    },
    {
        "identifier": 'EVENT_2634_pause_96',
        "command": 'pause',
        "args": [32]
    },
    {
        "identifier": 'EVENT_2634_run_dialog_97',
        "command": 'run_dialog',
        "args": [3294, AreaObjects.NPC_12, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_2634_jmp_if_dialog_option_b_98',
        "command": 'jmp_if_dialog_option_b',
        "args": ['EVENT_2634_pause_113']
    },
    {
        "identifier": 'EVENT_2634_pause_99',
        "command": 'pause',
        "args": [10]
    },
    {
        "identifier": 'EVENT_2634_set_action_script_async_100',
        "command": 'set_action_script_async',
        "args": [AreaObjects.MARIO, 670]
    },
    {
        "identifier": 'EVENT_2634_store_coin_amount_7000_101',
        "command": 'store_coin_amount_7000'
    },
    {
        "identifier": 'EVENT_2634_mem_compare_102',
        "command": 'mem_compare',
        "args": [0x7000, 10]
    },
    {
        "identifier": 'EVENT_2634_jmp_if_comparison_result_is_greater_or_equal_103',
        "command": 'jmp_if_comparison_result_is_greater_or_equal',
        "args": ['EVENT_2634_set_bit_108']
    },
    {
        "identifier": 'EVENT_2634_run_dialog_104',
        "command": 'run_dialog',
        "args": [3316, AreaObjects.NPC_12, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_2634_action_queue_sync_105',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_2],
        "subscript": [
            {
                "identifier": 'EVENT_2634_action_queue_sync_105_SUBSCRIPT_set_sprite_sequence_0',
                "command": 'set_sprite_sequence',
                "args": [10, 0, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_2634_enable_controls_106',
        "command": 'enable_controls',
        "args": [[ControllerDirections.LEFT, ControllerDirections.RIGHT, ControllerDirections.DOWN, ControllerDirections.UP, ControllerDirections.X, ControllerDirections.A, ControllerDirections.Y, ControllerDirections.B]]
    },
    {
        "identifier": 'EVENT_2634_ret_107',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_2634_set_bit_108',
        "command": 'set_bit',
        "args": [0x7043, 0]
    },
    {
        "identifier": 'EVENT_2634_set_109',
        "command": 'set',
        "args": [0x7000, 10]
    },
    {
        "identifier": 'EVENT_2634_dec_coins_110',
        "command": 'dec_coins'
    },
    {
        "identifier": 'EVENT_2634_jmp_111',
        "command": 'jmp',
        "args": ['EVENT_2634_set_bit_2']
    },
    {
        "identifier": 'EVENT_2634_ret_112',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_2634_pause_113',
        "command": 'pause',
        "args": [10]
    },
    {
        "identifier": 'EVENT_2634_set_action_script_async_114',
        "command": 'set_action_script_async',
        "args": [AreaObjects.MARIO, 671]
    },
    {
        "identifier": 'EVENT_2634_run_dialog_115',
        "command": 'run_dialog',
        "args": [3313, AreaObjects.NPC_12, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_2634_set_action_script_async_116',
        "command": 'set_action_script_async',
        "args": [AreaObjects.MARIO, 395]
    },
    {
        "identifier": 'EVENT_2634_action_queue_sync_117',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_2],
        "subscript": [
            {
                "identifier": 'EVENT_2634_action_queue_sync_117_SUBSCRIPT_set_sprite_sequence_0',
                "command": 'set_sprite_sequence',
                "args": [10, 0, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_2634_enable_controls_118',
        "command": 'enable_controls',
        "args": [[ControllerDirections.LEFT, ControllerDirections.RIGHT, ControllerDirections.DOWN, ControllerDirections.UP, ControllerDirections.X, ControllerDirections.A, ControllerDirections.Y, ControllerDirections.B]]
    },
    {
        "identifier": 'EVENT_2634_ret_119',
        "command": 'ret'
    }
]
