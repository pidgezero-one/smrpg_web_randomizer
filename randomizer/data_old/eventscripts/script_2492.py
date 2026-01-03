
from randomizer.helpers.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.helpers.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data import items
script = [
    {
        "identifier": 'EVENT_2492_jmp_if_bit_set_0',
        "command": 'jmp_if_bit_set',
        "args": [0x7044, 2, 'EVENT_2492_jmp_if_bit_set_15']
    },
    {
        "identifier": 'EVENT_2492_set_bit_1',
        "command": 'set_bit',
        "args": [0x7044, 2]
    },
    {
        "identifier": 'EVENT_2492_pause_action_script_2',
        "command": 'pause_action_script',
        "args": [AreaObjects.MEM_70A8]
    },
    {
        "identifier": 'EVENT_2492_set_7016_to_object_xyz_2',
        "command": 'set_7016_to_object_xyz',
        "args": [AreaObjects.MEM_70A8]
    },
    {
        "identifier": 'EVENT_2492_add_short_14',
        "command": "add_const_to_var",
        "args": [0x701A, 304]
    },
    {
        "identifier": 'EVENT_2492_action_queue_async_3',
        "command": 'action_queue',
        'args': [AreaObjects.MEM_70A8, True],
        "subscript": [
            {
                "identifier": 'EVENT_2492_action_queue_sync_3_SUBSCRIPT_sequence_looping_on_0',
                "command": 'sequence_looping_on'
            },
            {
                "identifier": 'EVENT_2492_action_queue_sync_3_SUBSCRIPT_set_sprite_sequence_1',
                "command": 'set_sprite_sequence',
                "args": [1, 0, [_0x08Flags.LOOPING_OFF]]
            },
            {
                "identifier": 'EVENT_2492_action_queue_sync_3_SUBSCRIPT_pause_2',
                "command": 'pause',
                "args": [6]
            },
            {
                "identifier": 'EVENT_2492_action_queue_sync_3_SUBSCRIPT_set_sprite_sequence_3',
                "command": 'set_sprite_sequence',
                "args": [2, 0, [_0x08Flags.READ_AS_SEQUENCE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_2492_action_queue_move_slot_NPC_3',
        "command": 'action_queue',
        'args': [AreaObjects.NPC_3, True],
        "subscript": [
            {
                "identifier": 'EVENT_2549_action_queue_sync_11_SUBSCRIPT_shift_south_pixels_1',
                "command": 'transfer_to_7016_7018_701A'
            }
        ]
    },
    {
        "identifier": 'EVENT_2492_action_queue_move_slot_NPC_4',
        "command": 'action_queue',
        'args': [AreaObjects.NPC_4, True],
        "subscript": [
            {
                "identifier": 'EVENT_2549_action_queue_sync_11_SUBSCRIPT_shift_south_pixels_1',
                "command": 'transfer_to_7016_7018_701A'
            }
        ]
    },
    {
        "identifier": 'EVENT_2492_action_queue_move_slot_NPC_5',
        "command": 'action_queue',
        'args': [AreaObjects.NPC_5, True],
        "subscript": [
            {
                "identifier": 'EVENT_2549_action_queue_sync_11_SUBSCRIPT_shift_south_pixels_1',
                "command": 'transfer_to_7016_7018_701A'
            }
        ]
    },
    {
        "identifier": 'EVENT_2492_action_queue_move_slot_NPC_6',
        "command": 'action_queue',
        'args': [AreaObjects.NPC_6, True],
        "subscript": [
            {
                "identifier": 'EVENT_2549_action_queue_sync_11_SUBSCRIPT_shift_south_pixels_1',
                "command": 'transfer_to_7016_7018_701A'
            }
        ]
    },
    {
        "identifier": 'EVENT_2492_action_queue_move_slot_NPC_7',
        "command": 'action_queue',
        'args': [AreaObjects.NPC_7, False],
        "subscript": [
            {
                "identifier": 'EVENT_2549_action_queue_sync_11_SUBSCRIPT_shift_south_pixels_1',
                "command": 'transfer_to_7016_7018_701A'
            }
        ]
    },
    {
        "identifier": 'EVENT_2492_pause_4',
        "command": 'pause',
        "args": [6]
    },
    {
        "identifier": 'EVENT_2492_summon_to_current_level_5',
        "command": 'summon_to_current_level',
        "args": [AreaObjects.NPC_3]
    },
    {
        "identifier": 'EVENT_2492_summon_to_current_level_6',
        "command": 'summon_to_current_level',
        "args": [AreaObjects.NPC_4]
    },
    {
        "identifier": 'EVENT_2492_summon_to_current_level_7',
        "command": 'summon_to_current_level',
        "args": [AreaObjects.NPC_5]
    },
    {
        "identifier": 'EVENT_2492_pause_8',
        "command": 'pause',
        "args": [1]
    },
    {
        "identifier": 'EVENT_2492_action_queue_sync_9',
        "command": 'action_queue',
        'args': [AreaObjects.NPC_4, True],
        "subscript": [
            {
                "identifier": 'EVENT_2492_action_queue_sync_9_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FASTEST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_2492_action_queue_sync_9_SUBSCRIPT_shift_east_pixels_1',
                "command": 'shift_east_pixels',
                "args": [17]
            }
        ]
    },
    {
        "identifier": 'EVENT_2492_action_queue_async_10',
        "command": 'action_queue',
        'args': [AreaObjects.NPC_5, False],
        "subscript": [
            {
                "identifier": 'EVENT_2492_action_queue_async_10_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FASTEST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_2492_action_queue_async_10_SUBSCRIPT_shift_west_pixels_1',
                "command": 'shift_west_pixels',
                "args": [17]
            }
        ]
    },
    {
        "identifier": 'EVENT_2492_set_action_script_sync_11',
        "command": 'set_action_script',
        'args': [AreaObjects.NPC_3, True, 185]
    },
    {
        "identifier": 'EVENT_2492_set_action_script_sync_12',
        "command": 'set_action_script',
        'args': [AreaObjects.NPC_4, True, 186]
    },
    {
        "identifier": 'EVENT_2492_set_action_script_sync_13',
        "command": 'set_action_script',
        'args': [AreaObjects.NPC_5, True, 184]
    },
    {
        "identifier": 'EVENT_2492_ret_14',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_2492_jmp_if_bit_set_15',
        "command": 'jmp_if_bit_set',
        "args": [0x7044, 3, 'EVENT_2492_jmp_if_bit_set_19']
    },
    {
        "identifier": 'EVENT_2492_set_bit_16',
        "command": 'set_bit',
        "args": [0x7044, 3]
    },
    {
        "identifier": 'EVENT_2492_pause_action_script_17',
        "command": 'pause_action_script',
        "args": [AreaObjects.NPC_5]
    },
    {
        "identifier": 'EVENT_2492_ret_18',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_2492_jmp_if_bit_set_19',
        "command": 'jmp_if_bit_set',
        "args": [0x7044, 4, 'EVENT_2492_disable_trigger_23']
    },
    {
        "identifier": 'EVENT_2492_set_bit_20',
        "command": 'set_bit',
        "args": [0x7044, 4]
    },
    {
        "identifier": 'EVENT_2492_pause_action_script_21',
        "command": 'pause_action_script',
        "args": [AreaObjects.NPC_3]
    },
    {
        "identifier": 'EVENT_2492_ret_22',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_2492_disable_trigger_23',
        "command": 'disable_trigger',
        "args": [AreaObjects.MEM_70A8]
    },
    {
        "identifier": 'EVENT_2492_pause_action_script_24',
        "command": 'pause_action_script',
        "args": [AreaObjects.NPC_4]
    },
    {
        "identifier": 'EVENT_2492_pause_25',
        "command": 'pause',
        "args": [16]
    },
    {
        "identifier": 'EVENT_2492_action_queue_sync_26',
        "command": 'action_queue',
        'args': [AreaObjects.NPC_5, True],
        "subscript": [
            {
                "identifier": 'EVENT_2492_action_queue_sync_26_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_2492_action_queue_sync_26_SUBSCRIPT_shift_east_pixels_1',
                "command": 'shift_east_pixels',
                "args": [8]
            }
        ]
    },
    {
        "identifier": 'EVENT_2492_action_queue_sync_27',
        "command": 'action_queue',
        'args': [AreaObjects.NPC_4, True],
        "subscript": [
            {
                "identifier": 'EVENT_2492_action_queue_sync_27_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_2492_action_queue_sync_27_SUBSCRIPT_shift_west_pixels_1',
                "command": 'shift_west_pixels',
                "args": [8]
            }
        ]
    },
    {
        "identifier": 'EVENT_2492_stop_embedded_action_script_28',
        "command": 'stop_embedded_action_script',
        "args": [AreaObjects.NPC_4]
    },
    {
        "identifier": 'EVENT_2492_stop_embedded_action_script_29',
        "command": 'stop_embedded_action_script',
        "args": [AreaObjects.NPC_5]
    },
    {
        "identifier": 'EVENT_2492_remove_from_current_level_30',
        "command": 'remove_from_current_level',
        "args": [AreaObjects.NPC_3]
    },
    {
        "identifier": 'EVENT_2492_remove_from_current_level_31',
        "command": 'remove_from_current_level',
        "args": [AreaObjects.NPC_4]
    },
    {
        "identifier": 'EVENT_2492_remove_from_current_level_32',
        "command": 'remove_from_current_level',
        "args": [AreaObjects.NPC_5]
    },
    {
        "identifier": 'EVENT_2492_summon_to_current_level_33',
        "command": 'summon_to_current_level',
        "args": [AreaObjects.NPC_7]
    },
    {
        "identifier": 'EVENT_2492_action_queue_async_34',
        "command": 'action_queue',
        'args': [AreaObjects.NPC_7, False],
        "subscript": [
            {
                "identifier": 'EVENT_2492_action_queue_async_34_SUBSCRIPT_set_vram_priority_0',
                "command": 'set_vram_priority',
                "args": [VramPriority.OBJECT_OVERLAPS_MARIO_ON_ALL_SIDES]
            },
            {
                "identifier": 'EVENT_2492_action_queue_async_34_SUBSCRIPT_set_sprite_sequence_1',
                "command": 'set_sprite_sequence',
                "args": [1, 0, [_0x08Flags.LOOPING_OFF]]
            },
            {
                "identifier": 'EVENT_2492_action_queue_async_34_SUBSCRIPT_pause_2',
                "command": 'pause',
                "args": [16]
            },
            {
                "identifier": 'EVENT_2492_action_queue_async_34_SUBSCRIPT_visibility_off_3',
                "command": 'visibility_off'
            }
        ]
    },
    {
        "identifier": 'EVENT_2492_jmp_if_var_equals_const_35',
        "command": 'jmp_if_var_equals_const',
        "args": [0x70c0, 0, 'EVENT_2492_jmp_if_var_equals_const_38']
    },
    {
        "identifier": 'EVENT_2492_jmp_if_var_equals_const_36',
        "command": 'jmp_if_var_equals_const',
        "args": [0x70c0, 1, 'EVENT_2492_jmp_if_var_equals_const_41']
    },
    {
        "identifier": 'EVENT_2492_jmp_if_var_equals_const_37',
        "command": 'jmp_if_var_equals_const',
        "args": [0x70c0, 2, 'EVENT_2492_jmp_if_var_equals_const_44']
    },
    {
        "identifier": 'EVENT_2492_jmp_if_var_equals_const_38',
        "command": 'jmp_if_var_equals_const',
        "args": [0x70c1, 0, 'EVENT_2492_jmp_if_var_equals_const_47']
    },
    {
        "identifier": 'EVENT_2492_jmp_if_var_equals_const_39',
        "command": 'jmp_if_var_equals_const',
        "args": [0x70c1, 1, 'EVENT_2492_jmp_if_var_equals_const_49']
    },
    {
        "identifier": 'EVENT_2492_jmp_40',
        "command": 'jmp',
        "args": ['EVENT_2492_jmp_if_var_equals_const_52']
    },
    {
        "identifier": 'EVENT_2492_jmp_if_var_equals_const_41',
        "command": 'jmp_if_var_equals_const',
        "args": [0x70c1, 0, 'EVENT_2492_jmp_if_var_equals_const_55']
    },
    {
        "identifier": 'EVENT_2492_jmp_if_var_equals_const_42',
        "command": 'jmp_if_var_equals_const',
        "args": [0x70c1, 1, 'EVENT_2492_jmp_if_var_equals_const_58']
    },
    {
        "identifier": 'EVENT_2492_jmp_43',
        "command": 'jmp',
        "args": ['EVENT_2492_jmp_if_var_equals_const_60']
    },
    {
        "identifier": 'EVENT_2492_jmp_if_var_equals_const_44',
        "command": 'jmp_if_var_equals_const',
        "args": [0x70c1, 0, 'EVENT_2492_jmp_if_var_equals_const_63']
    },
    {
        "identifier": 'EVENT_2492_jmp_if_var_equals_const_45',
        "command": 'jmp_if_var_equals_const',
        "args": [0x70c1, 1, 'EVENT_2492_jmp_if_var_equals_const_66']
    },
    {
        "identifier": 'EVENT_2492_jmp_46',
        "command": 'jmp',
        "args": ['EVENT_2492_jmp_if_var_equals_const_69']
    },
    {
        "identifier": 'EVENT_2492_jmp_if_var_equals_const_47',
        "command": 'jmp_if_var_equals_const',
        "args": [0x70c2, 0, 'EVENT_2492_summon_to_current_level_71']
    },
    {
        "identifier": 'EVENT_2492_jmp_48',
        "command": 'jmp',
        "args": ['EVENT_2492_play_sound_76']
    },
    {
        "identifier": 'EVENT_2492_jmp_if_var_equals_const_49',
        "command": 'jmp_if_var_equals_const',
        "args": [0x70c2, 0, 'EVENT_2492_play_sound_76']
    },
    {
        "identifier": 'EVENT_2492_jmp_if_var_equals_const_50',
        "command": 'jmp_if_var_equals_const',
        "args": [0x70c2, 1, 'EVENT_2492_play_sound_81']
    },
    {
        "identifier": 'EVENT_2492_jmp_51',
        "command": 'jmp',
        "args": ['EVENT_2492_action_queue_async_92']
    },
    {
        "identifier": 'EVENT_2492_jmp_if_var_equals_const_52',
        "command": 'jmp_if_var_equals_const',
        "args": [0x70c2, 0, 'EVENT_2492_play_sound_76']
    },
    {
        "identifier": 'EVENT_2492_jmp_if_var_equals_const_53',
        "command": 'jmp_if_var_equals_const',
        "args": [0x70c2, 1, 'EVENT_2492_action_queue_async_92']
    },
    {
        "identifier": 'EVENT_2492_jmp_54',
        "command": 'jmp',
        "args": ['EVENT_2492_play_sound_88']
    },
    {
        "identifier": 'EVENT_2492_jmp_if_var_equals_const_55',
        "command": 'jmp_if_var_equals_const',
        "args": [0x70c2, 0, 'EVENT_2492_play_sound_76']
    },
    {
        "identifier": 'EVENT_2492_jmp_if_var_equals_const_56',
        "command": 'jmp_if_var_equals_const',
        "args": [0x70c2, 1, 'EVENT_2492_play_sound_81']
    },
    {
        "identifier": 'EVENT_2492_jmp_57',
        "command": 'jmp',
        "args": ['EVENT_2492_action_queue_async_92']
    },
    {
        "identifier": 'EVENT_2492_jmp_if_var_equals_const_58',
        "command": 'jmp_if_var_equals_const',
        "args": [0x70c2, 1, 'EVENT_2492_summon_to_current_level_71']
    },
    {
        "identifier": 'EVENT_2492_jmp_59',
        "command": 'jmp',
        "args": ['EVENT_2492_play_sound_81']
    },
    {
        "identifier": 'EVENT_2492_jmp_if_var_equals_const_60',
        "command": 'jmp_if_var_equals_const',
        "args": [0x70c2, 0, 'EVENT_2492_action_queue_async_92']
    },
    {
        "identifier": 'EVENT_2492_jmp_if_var_equals_const_61',
        "command": 'jmp_if_var_equals_const',
        "args": [0x70c2, 1, 'EVENT_2492_play_sound_81']
    },
    {
        "identifier": 'EVENT_2492_jmp_62',
        "command": 'jmp',
        "args": ['EVENT_2492_play_sound_88']
    },
    {
        "identifier": 'EVENT_2492_jmp_if_var_equals_const_63',
        "command": 'jmp_if_var_equals_const',
        "args": [0x70c2, 0, 'EVENT_2492_play_sound_76']
    },
    {
        "identifier": 'EVENT_2492_jmp_if_var_equals_const_64',
        "command": 'jmp_if_var_equals_const',
        "args": [0x70c2, 1, 'EVENT_2492_action_queue_async_92']
    },
    {
        "identifier": 'EVENT_2492_jmp_65',
        "command": 'jmp',
        "args": ['EVENT_2492_play_sound_88']
    },
    {
        "identifier": 'EVENT_2492_jmp_if_var_equals_const_66',
        "command": 'jmp_if_var_equals_const',
        "args": [0x70c2, 0, 'EVENT_2492_action_queue_async_92']
    },
    {
        "identifier": 'EVENT_2492_jmp_if_var_equals_const_67',
        "command": 'jmp_if_var_equals_const',
        "args": [0x70c2, 1, 'EVENT_2492_play_sound_81']
    },
    {
        "identifier": 'EVENT_2492_jmp_68',
        "command": 'jmp',
        "args": ['EVENT_2492_play_sound_88']
    },
    {
        "identifier": 'EVENT_2492_jmp_if_var_equals_const_69',
        "command": 'jmp_if_var_equals_const',
        "args": [0x70c2, 2, 'EVENT_2492_summon_to_current_level_71']
    },
    {
        "identifier": 'EVENT_2492_jmp_70',
        "command": 'jmp',
        "args": ['EVENT_2492_play_sound_88']
    },
    {
        "identifier": 'EVENT_2492_summon_to_current_level_71',
        "command": 'summon_to_current_level',
        "args": [AreaObjects.NPC_6]
    },
    {
        "identifier": 'EVENT_2492_play_sound_72',
        "command": 'play_sound',
        "args": [Sounds._094_FROG_COIN, 6]
    },
    {
        "identifier": 'EVENT_2492_action_queue_sync_73',
        "command": 'action_queue',
        'args': [AreaObjects.NPC_6, True],
        "subscript": [
            {
                "identifier": 'EVENT_2492_action_queue_sync_73_SUBSCRIPT_set_vram_priority_0',
                "command": 'set_vram_priority',
                "args": [VramPriority.OBJECT_OVERLAPS_MARIO_ON_ALL_SIDES]
            },
            {
                "identifier": 'EVENT_2492_action_queue_sync_73_SUBSCRIPT_set_priority_1',
                "command": 'set_priority',
                "args": [3]
            },
            {
                "identifier": 'EVENT_2492_action_queue_sync_73_SUBSCRIPT_set_sprite_sequence_2',
                "command": 'set_sprite_sequence',
                "args": [1, 0, [_0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_2492_action_queue_sync_73_SUBSCRIPT_pause_3',
                "command": 'pause',
                "args": [32]
            },
            {
                "identifier": 'EVENT_2492_action_queue_sync_73_SUBSCRIPT_visibility_off_4',
                "command": 'visibility_off'
            }
        ]
    },
    {
        "identifier": 'EVENT_2492_add_frog_coins_74',
        "command": 'add_frog_coins',
        "args": [1]
    },
    {
        "identifier": 'EVENT_2492_jmp_75',
        "command": 'jmp',
        "args": ['EVENT_2492_action_queue_sync_99']
    },
    {
        "identifier": 'EVENT_2492_play_sound_76',
        "command": 'play_sound',
        "args": [Sounds._014_FLOWER, 6]
    },
    {
        "identifier": 'EVENT_2492_action_queue_sync_77',
        "command": 'action_queue',
        'args': [AreaObjects.NPC_3, True],
        "subscript": [
            {
                "identifier": 'EVENT_2492_action_queue_sync_77_SUBSCRIPT_visibility_on_0',
                "command": 'visibility_on'
            },
            {
                "identifier": 'EVENT_2492_action_queue_sync_77_SUBSCRIPT_set_sprite_sequence_1',
                "command": 'set_sprite_sequence',
                "args": [0, 0, [_0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_2492_action_queue_sync_77_SUBSCRIPT_pause_2',
                "command": 'pause',
                "args": [32]
            },
            {
                "identifier": 'EVENT_2492_action_queue_sync_77_SUBSCRIPT_visibility_off_3',
                "command": 'visibility_off'
            }
        ]
    },
    {
        "identifier": 'EVENT_2492_set_78',
        "command": "set_var_to_const",
        "args": [0x7000, 1]
    },
    {
        "identifier": 'EVENT_2492_add_7000_to_max_FP_79',
        "command": 'add_7000_to_max_FP'
    },
    {
        "identifier": 'EVENT_2492_jmp_80',
        "command": 'jmp',
        "args": ['EVENT_2492_action_queue_sync_99']
    },
    {
        "identifier": 'EVENT_2492_play_sound_81',
        "command": 'play_sound',
        "args": [Sounds._071_MUSHROOM_CURE, 6]
    },
    {
        "identifier": 'EVENT_2492_action_queue_sync_82',
        "command": 'action_queue',
        'args': [AreaObjects.NPC_3, True],
        "subscript": [
            {
                "identifier": 'EVENT_2492_action_queue_sync_82_SUBSCRIPT_visibility_on_0',
                "command": 'visibility_on'
            },
            {
                "identifier": 'EVENT_2492_action_queue_sync_82_SUBSCRIPT_set_sprite_sequence_1',
                "command": 'set_sprite_sequence',
                "args": [1, 0, [_0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_2492_action_queue_sync_82_SUBSCRIPT_pause_2',
                "command": 'pause',
                "args": [32]
            },
            {
                "identifier": 'EVENT_2492_action_queue_sync_82_SUBSCRIPT_visibility_off_3',
                "command": 'visibility_off'
            }
        ]
    },
    {
        "identifier": 'EVENT_2492_restore_all_hp_83',
        "command": 'restore_all_hp'
    },
    {
        "identifier": 'EVENT_2492_restore_all_fp_84',
        "command": 'restore_all_fp'
    },
    {
        "identifier": 'EVENT_2492_tint_layers_85',
        "command": 'tint_layers',
        "args": [0x40, 0xa0, 0x40, 3, [_0x81Flags.LAYER_1, _0x81Flags.LAYER_2, _0x81Flags.LAYER_3, _0x81Flags.LAYER_4, _0x81Flags.NPC_SPRITES, _0x81Flags.BACKGROUND], [7]]
    },
    {
        "identifier": 'EVENT_2492_tint_layers_86',
        "command": 'tint_layers',
        "args": [0x00, 0x00, 0x00, 3, [_0x81Flags.LAYER_1, _0x81Flags.LAYER_2, _0x81Flags.LAYER_3, _0x81Flags.LAYER_4, _0x81Flags.NPC_SPRITES, _0x81Flags.BACKGROUND], [7]]
    },
    {
        "identifier": 'EVENT_2492_jmp_87',
        "command": 'jmp',
        "args": ['EVENT_2492_action_queue_sync_99']
    },
    {
        "identifier": 'EVENT_2492_play_sound_88',
        "command": 'play_sound',
        "args": [Sounds._027_FOUND_AN_ITEM, 6]
    },
    {
        "identifier": 'EVENT_2492_action_queue_sync_89',
        "command": 'action_queue',
        'args': [AreaObjects.NPC_3, True],
        "subscript": [
            {
                "identifier": 'EVENT_2492_action_queue_sync_89_SUBSCRIPT_visibility_on_0',
                "command": 'visibility_on'
            },
            {
                "identifier": 'EVENT_2492_action_queue_sync_89_SUBSCRIPT_set_sprite_sequence_1',
                "command": 'set_sprite_sequence',
                "args": [3, 0, [_0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_2492_action_queue_sync_89_SUBSCRIPT_pause_2',
                "command": 'pause',
                "args": [32]
            },
            {
                "identifier": 'EVENT_2492_action_queue_sync_89_SUBSCRIPT_visibility_off_3',
                "command": 'visibility_off'
            }
        ]
    },
    {
        "identifier": 'EVENT_2492_put_inventory_90',
        "command": 'put_inventory',
        "args": [items.RockCandy]
    },
    {
        "identifier": 'EVENT_2492_jmp_91',
        "command": 'jmp',
        "args": ['EVENT_2492_action_queue_sync_99']
    },
    {
        "identifier": 'EVENT_2492_action_queue_async_92',
        "command": 'action_queue',
        'args': [AreaObjects.NPC_3, False],
        "subscript": [
            {
                "identifier": 'EVENT_2492_action_queue_async_92_SUBSCRIPT_visibility_on_0',
                "command": 'visibility_on'
            },
            {
                "identifier": 'EVENT_2492_action_queue_async_92_SUBSCRIPT_set_sprite_sequence_1',
                "command": 'set_sprite_sequence',
                "args": [4, 0, [_0x08Flags.READ_AS_SEQUENCE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_2492_pause_93',
        "command": 'pause',
        "args": [32]
    },
    {
        "identifier": 'EVENT_2492_jmp_if_bit_set_351',
        "command": 'jmp_if_bit_set',
        "args": [0x7086, 7, 'EVENT_2492_start_battle_94_']
    },
    {
        "identifier": 'EVENT_2492_start_battle_94',
        "command": 'run_event_as_subroutine',
        "args": [1931]
    },
    {
        "identifier": 'EVENT_2492_jmp_if_bit_set_351_',
        "command": 'jmp',
        "args": ['EVENT_2492_remove_from_current_level_97']
    },
    {
        "identifier": 'EVENT_2492_start_battle_94_',
        "command": "set_var_to_const",
        "args": [0x7000, 514]
    },
    {
        "identifier": 'EVENT_2492_fight',
        "command": 'run_event_as_subroutine',
        "args": [353]
    },
    {
        "identifier": 'EVENT_2492_start_battle_350',
        "command": 'run_event_as_subroutine',
        "args": [171]
    },
    {
        "identifier": 'EVENT_2492_remove_from_current_level_97',
        "command": 'remove_from_current_level',
        "args": [AreaObjects.NPC_3]
    },
    {
        "identifier": 'EVENT_2492_fade_in_from_black_async_98',
        "command": 'fade_in_from_black_async'
    },
    {
        "identifier": 'EVENT_2492_action_queue_sync_99',
        "command": 'action_queue',
        'args': [AreaObjects.MEM_70A8, True],
        "subscript": [
            {
                "identifier": 'EVENT_2492_action_queue_sync_99_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [32]
            },
            {
                "identifier": 'EVENT_2492_action_queue_sync_99_SUBSCRIPT_set_animation_speed_1',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_2492_action_queue_sync_99_SUBSCRIPT_set_sprite_sequence_2',
                "command": 'set_sprite_sequence',
                "args": [3, 0, [_0x08Flags.LOOPING_OFF]]
            },
            {
                "identifier": 'EVENT_2492_action_queue_sync_99_SUBSCRIPT_pause_3',
                "command": 'pause',
                "args": [10]
            },
            {
                "identifier": 'EVENT_2492_action_queue_sync_99_SUBSCRIPT_set_sprite_sequence_4',
                "command": 'set_sprite_sequence',
                "args": [4, 0, [_0x08Flags.READ_AS_SEQUENCE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_2492_disable_99',
        "command": 'disable_trigger',
        "args": [AreaObjects.MEM_70A8]
    },
    {
        "identifier": 'EVENT_2492_clear_bit_1',
        "command": 'clear_bit',
        "args": [0x7044, 2]
    },
    {
        "identifier": 'EVENT_2492_clear_bit_2',
        "command": 'clear_bit',
        "args": [0x7044, 3]
    },
    {
        "identifier": 'EVENT_2492_clear_bit_3',
        "command": 'clear_bit',
        "args": [0x7044, 4]
    },
    {
        "identifier": 'EVENT_2492_ret_100',
        "command": 'ret'
    }
]
