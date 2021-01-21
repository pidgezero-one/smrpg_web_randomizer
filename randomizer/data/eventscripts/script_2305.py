from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data import items
script = [
    {
        "identifier": 'EVENT_2305_jmp_if_bit_set_0',
        "command": 'jmp_if_bit_set',
        "args": [0x7044, 2, 'EVENT_2305_jmp_if_bit_set_15']
    },
    {
        "identifier": 'EVENT_2305_set_bit_1',
        "command": 'set_bit',
        "args": [0x7044, 2]
    },
    {
        "identifier": 'EVENT_2305_pause_action_script_2',
        "command": 'pause_action_script',
        "args": [AreaObjects.NPC_0]
    },
    {
        "identifier": 'EVENT_2305_action_queue_sync_3',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_0],
        "subscript": [
            {
                "identifier": 'EVENT_2305_action_queue_sync_3_SUBSCRIPT_sequence_looping_on_0',
                "command": 'sequence_looping_on'
            },
            {
                "identifier": 'EVENT_2305_action_queue_sync_3_SUBSCRIPT_set_sprite_sequence_1',
                "command": 'set_sprite_sequence',
                "args": [1, inc_sprite=0, flags=[_0x08Flags.LOOPING_OFF]]
            },
            {
                "identifier": 'EVENT_2305_action_queue_sync_3_SUBSCRIPT_pause_2',
                "command": 'pause',
                "args": [6]
            },
            {
                "identifier": 'EVENT_2305_action_queue_sync_3_SUBSCRIPT_set_sprite_sequence_3',
                "command": 'set_sprite_sequence',
                "args": [2, inc_sprite=0, flags=[_0x08Flags.READ_AS_SEQUENCE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_2305_pause_4',
        "command": 'pause',
        "args": [6]
    },
    {
        "identifier": 'EVENT_2305_summon_to_current_level_5',
        "command": 'summon_to_current_level',
        "args": [AreaObjects.NPC_1]
    },
    {
        "identifier": 'EVENT_2305_summon_to_current_level_6',
        "command": 'summon_to_current_level',
        "args": [AreaObjects.NPC_2]
    },
    {
        "identifier": 'EVENT_2305_summon_to_current_level_7',
        "command": 'summon_to_current_level',
        "args": [AreaObjects.NPC_3]
    },
    {
        "identifier": 'EVENT_2305_pause_8',
        "command": 'pause',
        "args": [1]
    },
    {
        "identifier": 'EVENT_2305_action_queue_sync_9',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_2],
        "subscript": [
            {
                "identifier": 'EVENT_2305_action_queue_sync_9_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FASTEST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_2305_action_queue_sync_9_SUBSCRIPT_shift_east_pixels_1',
                "command": 'shift_east_pixels',
                "args": [17]
            }
        ]
    },
    {
        "identifier": 'EVENT_2305_action_queue_async_10',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_3],
        "subscript": [
            {
                "identifier": 'EVENT_2305_action_queue_async_10_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FASTEST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_2305_action_queue_async_10_SUBSCRIPT_shift_west_pixels_1',
                "command": 'shift_west_pixels',
                "args": [17]
            }
        ]
    },
    {
        "identifier": 'EVENT_2305_set_action_script_sync_11',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_1, 185]
    },
    {
        "identifier": 'EVENT_2305_set_action_script_sync_12',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_2, 186]
    },
    {
        "identifier": 'EVENT_2305_set_action_script_sync_13',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_3, 184]
    },
    {
        "identifier": 'EVENT_2305_ret_14',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_2305_jmp_if_bit_set_15',
        "command": 'jmp_if_bit_set',
        "args": [0x7044, 3, 'EVENT_2305_jmp_if_bit_set_19']
    },
    {
        "identifier": 'EVENT_2305_set_bit_16',
        "command": 'set_bit',
        "args": [0x7044, 3]
    },
    {
        "identifier": 'EVENT_2305_pause_action_script_17',
        "command": 'pause_action_script',
        "args": [AreaObjects.NPC_3]
    },
    {
        "identifier": 'EVENT_2305_ret_18',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_2305_jmp_if_bit_set_19',
        "command": 'jmp_if_bit_set',
        "args": [0x7044, 4, 'EVENT_2305_disable_trigger_23']
    },
    {
        "identifier": 'EVENT_2305_set_bit_20',
        "command": 'set_bit',
        "args": [0x7044, 4]
    },
    {
        "identifier": 'EVENT_2305_pause_action_script_21',
        "command": 'pause_action_script',
        "args": [AreaObjects.NPC_1]
    },
    {
        "identifier": 'EVENT_2305_ret_22',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_2305_disable_trigger_23',
        "command": 'disable_trigger',
        "args": [AreaObjects.MEM_70A8]
    },
    {
        "identifier": 'EVENT_2305_pause_action_script_24',
        "command": 'pause_action_script',
        "args": [AreaObjects.NPC_2]
    },
    {
        "identifier": 'EVENT_2305_pause_25',
        "command": 'pause',
        "args": [16]
    },
    {
        "identifier": 'EVENT_2305_action_queue_sync_26',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_3],
        "subscript": [
            {
                "identifier": 'EVENT_2305_action_queue_sync_26_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_2305_action_queue_sync_26_SUBSCRIPT_shift_east_pixels_1',
                "command": 'shift_east_pixels',
                "args": [8]
            }
        ]
    },
    {
        "identifier": 'EVENT_2305_action_queue_sync_27',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_2],
        "subscript": [
            {
                "identifier": 'EVENT_2305_action_queue_sync_27_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_2305_action_queue_sync_27_SUBSCRIPT_shift_west_pixels_1',
                "command": 'shift_west_pixels',
                "args": [8]
            }
        ]
    },
    {
        "identifier": 'EVENT_2305_stop_embedded_action_script_28',
        "command": 'stop_embedded_action_script',
        "args": [AreaObjects.NPC_2]
    },
    {
        "identifier": 'EVENT_2305_stop_embedded_action_script_29',
        "command": 'stop_embedded_action_script',
        "args": [AreaObjects.NPC_3]
    },
    {
        "identifier": 'EVENT_2305_remove_from_current_level_30',
        "command": 'remove_from_current_level',
        "args": [AreaObjects.NPC_1]
    },
    {
        "identifier": 'EVENT_2305_remove_from_current_level_31',
        "command": 'remove_from_current_level',
        "args": [AreaObjects.NPC_2]
    },
    {
        "identifier": 'EVENT_2305_remove_from_current_level_32',
        "command": 'remove_from_current_level',
        "args": [AreaObjects.NPC_3]
    },
    {
        "identifier": 'EVENT_2305_summon_to_current_level_33',
        "command": 'summon_to_current_level',
        "args": [AreaObjects.NPC_5]
    },
    {
        "identifier": 'EVENT_2305_action_queue_async_34',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_5],
        "subscript": [
            {
                "identifier": 'EVENT_2305_action_queue_async_34_SUBSCRIPT_set_vram_priority_0',
                "command": 'set_vram_priority',
                "args": [VramPriority.OBJECT_OVERLAPS_MARIO_ON_ALL_SIDES]
            },
            {
                "identifier": 'EVENT_2305_action_queue_async_34_SUBSCRIPT_set_sprite_sequence_1',
                "command": 'set_sprite_sequence',
                "args": [1, inc_sprite=0, flags=[_0x08Flags.LOOPING_OFF]]
            },
            {
                "identifier": 'EVENT_2305_action_queue_async_34_SUBSCRIPT_pause_2',
                "command": 'pause',
                "args": [16]
            },
            {
                "identifier": 'EVENT_2305_action_queue_async_34_SUBSCRIPT_visibility_off_3',
                "command": 'visibility_off'
            }
        ]
    },
    {
        "identifier": 'EVENT_2305_jmp_if_var_equals_byte_35',
        "command": 'jmp_if_var_equals_byte',
        "args": [0x70c0, 0, 'EVENT_2305_jmp_if_var_equals_byte_38']
    },
    {
        "identifier": 'EVENT_2305_jmp_if_var_equals_byte_36',
        "command": 'jmp_if_var_equals_byte',
        "args": [0x70c0, 1, 'EVENT_2305_jmp_if_var_equals_byte_41']
    },
    {
        "identifier": 'EVENT_2305_jmp_if_var_equals_byte_37',
        "command": 'jmp_if_var_equals_byte',
        "args": [0x70c0, 2, 'EVENT_2305_jmp_if_var_equals_byte_44']
    },
    {
        "identifier": 'EVENT_2305_jmp_if_var_equals_byte_38',
        "command": 'jmp_if_var_equals_byte',
        "args": [0x70c1, 0, 'EVENT_2305_jmp_if_var_equals_byte_47']
    },
    {
        "identifier": 'EVENT_2305_jmp_if_var_equals_byte_39',
        "command": 'jmp_if_var_equals_byte',
        "args": [0x70c1, 1, 'EVENT_2305_jmp_if_var_equals_byte_49']
    },
    {
        "identifier": 'EVENT_2305_jmp_40',
        "command": 'jmp',
        "args": ['EVENT_2305_jmp_if_var_equals_byte_52']
    },
    {
        "identifier": 'EVENT_2305_jmp_if_var_equals_byte_41',
        "command": 'jmp_if_var_equals_byte',
        "args": [0x70c1, 0, 'EVENT_2305_jmp_if_var_equals_byte_55']
    },
    {
        "identifier": 'EVENT_2305_jmp_if_var_equals_byte_42',
        "command": 'jmp_if_var_equals_byte',
        "args": [0x70c1, 1, 'EVENT_2305_jmp_if_var_equals_byte_58']
    },
    {
        "identifier": 'EVENT_2305_jmp_43',
        "command": 'jmp',
        "args": ['EVENT_2305_jmp_if_var_equals_byte_60']
    },
    {
        "identifier": 'EVENT_2305_jmp_if_var_equals_byte_44',
        "command": 'jmp_if_var_equals_byte',
        "args": [0x70c1, 0, 'EVENT_2305_jmp_if_var_equals_byte_63']
    },
    {
        "identifier": 'EVENT_2305_jmp_if_var_equals_byte_45',
        "command": 'jmp_if_var_equals_byte',
        "args": [0x70c1, 1, 'EVENT_2305_jmp_if_var_equals_byte_66']
    },
    {
        "identifier": 'EVENT_2305_jmp_46',
        "command": 'jmp',
        "args": ['EVENT_2305_jmp_if_var_equals_byte_69']
    },
    {
        "identifier": 'EVENT_2305_jmp_if_var_equals_byte_47',
        "command": 'jmp_if_var_equals_byte',
        "args": [0x70c2, 0, 'EVENT_2305_summon_to_current_level_71']
    },
    {
        "identifier": 'EVENT_2305_jmp_48',
        "command": 'jmp',
        "args": ['EVENT_2305_play_sound_76']
    },
    {
        "identifier": 'EVENT_2305_jmp_if_var_equals_byte_49',
        "command": 'jmp_if_var_equals_byte',
        "args": [0x70c2, 0, 'EVENT_2305_play_sound_76']
    },
    {
        "identifier": 'EVENT_2305_jmp_if_var_equals_byte_50',
        "command": 'jmp_if_var_equals_byte',
        "args": [0x70c2, 1, 'EVENT_2305_play_sound_81']
    },
    {
        "identifier": 'EVENT_2305_jmp_51',
        "command": 'jmp',
        "args": ['EVENT_2305_action_queue_async_92']
    },
    {
        "identifier": 'EVENT_2305_jmp_if_var_equals_byte_52',
        "command": 'jmp_if_var_equals_byte',
        "args": [0x70c2, 0, 'EVENT_2305_play_sound_76']
    },
    {
        "identifier": 'EVENT_2305_jmp_if_var_equals_byte_53',
        "command": 'jmp_if_var_equals_byte',
        "args": [0x70c2, 1, 'EVENT_2305_action_queue_async_92']
    },
    {
        "identifier": 'EVENT_2305_jmp_54',
        "command": 'jmp',
        "args": ['EVENT_2305_play_sound_88']
    },
    {
        "identifier": 'EVENT_2305_jmp_if_var_equals_byte_55',
        "command": 'jmp_if_var_equals_byte',
        "args": [0x70c2, 0, 'EVENT_2305_play_sound_76']
    },
    {
        "identifier": 'EVENT_2305_jmp_if_var_equals_byte_56',
        "command": 'jmp_if_var_equals_byte',
        "args": [0x70c2, 1, 'EVENT_2305_play_sound_81']
    },
    {
        "identifier": 'EVENT_2305_jmp_57',
        "command": 'jmp',
        "args": ['EVENT_2305_action_queue_async_92']
    },
    {
        "identifier": 'EVENT_2305_jmp_if_var_equals_byte_58',
        "command": 'jmp_if_var_equals_byte',
        "args": [0x70c2, 1, 'EVENT_2305_summon_to_current_level_71']
    },
    {
        "identifier": 'EVENT_2305_jmp_59',
        "command": 'jmp',
        "args": ['EVENT_2305_play_sound_81']
    },
    {
        "identifier": 'EVENT_2305_jmp_if_var_equals_byte_60',
        "command": 'jmp_if_var_equals_byte',
        "args": [0x70c2, 0, 'EVENT_2305_action_queue_async_92']
    },
    {
        "identifier": 'EVENT_2305_jmp_if_var_equals_byte_61',
        "command": 'jmp_if_var_equals_byte',
        "args": [0x70c2, 1, 'EVENT_2305_play_sound_81']
    },
    {
        "identifier": 'EVENT_2305_jmp_62',
        "command": 'jmp',
        "args": ['EVENT_2305_play_sound_88']
    },
    {
        "identifier": 'EVENT_2305_jmp_if_var_equals_byte_63',
        "command": 'jmp_if_var_equals_byte',
        "args": [0x70c2, 0, 'EVENT_2305_play_sound_76']
    },
    {
        "identifier": 'EVENT_2305_jmp_if_var_equals_byte_64',
        "command": 'jmp_if_var_equals_byte',
        "args": [0x70c2, 1, 'EVENT_2305_action_queue_async_92']
    },
    {
        "identifier": 'EVENT_2305_jmp_65',
        "command": 'jmp',
        "args": ['EVENT_2305_play_sound_88']
    },
    {
        "identifier": 'EVENT_2305_jmp_if_var_equals_byte_66',
        "command": 'jmp_if_var_equals_byte',
        "args": [0x70c2, 0, 'EVENT_2305_action_queue_async_92']
    },
    {
        "identifier": 'EVENT_2305_jmp_if_var_equals_byte_67',
        "command": 'jmp_if_var_equals_byte',
        "args": [0x70c2, 1, 'EVENT_2305_play_sound_81']
    },
    {
        "identifier": 'EVENT_2305_jmp_68',
        "command": 'jmp',
        "args": ['EVENT_2305_play_sound_88']
    },
    {
        "identifier": 'EVENT_2305_jmp_if_var_equals_byte_69',
        "command": 'jmp_if_var_equals_byte',
        "args": [0x70c2, 2, 'EVENT_2305_summon_to_current_level_71']
    },
    {
        "identifier": 'EVENT_2305_jmp_70',
        "command": 'jmp',
        "args": ['EVENT_2305_play_sound_88']
    },
    {
        "identifier": 'EVENT_2305_summon_to_current_level_71',
        "command": 'summon_to_current_level',
        "args": [AreaObjects.NPC_4]
    },
    {
        "identifier": 'EVENT_2305_play_sound_72',
        "command": 'play_sound',
        "args": [Sounds._094_FROG_COIN, 6]
    },
    {
        "identifier": 'EVENT_2305_action_queue_sync_73',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_4],
        "subscript": [
            {
                "identifier": 'EVENT_2305_action_queue_sync_73_SUBSCRIPT_set_vram_priority_0',
                "command": 'set_vram_priority',
                "args": [VramPriority.OBJECT_OVERLAPS_MARIO_ON_ALL_SIDES]
            },
            {
                "identifier": 'EVENT_2305_action_queue_sync_73_SUBSCRIPT_set_priority_1',
                "command": 'set_priority',
                "args": [3]
            },
            {
                "identifier": 'EVENT_2305_action_queue_sync_73_SUBSCRIPT_set_sprite_sequence_2',
                "command": 'set_sprite_sequence',
                "args": [1, inc_sprite=0, flags=[_0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_2305_action_queue_sync_73_SUBSCRIPT_pause_3',
                "command": 'pause',
                "args": [32]
            },
            {
                "identifier": 'EVENT_2305_action_queue_sync_73_SUBSCRIPT_visibility_off_4',
                "command": 'visibility_off'
            }
        ]
    },
    {
        "identifier": 'EVENT_2305_add_frog_coins_74',
        "command": 'add_frog_coins',
        "args": [1]
    },
    {
        "identifier": 'EVENT_2305_jmp_75',
        "command": 'jmp',
        "args": ['EVENT_2305_action_queue_sync_99']
    },
    {
        "identifier": 'EVENT_2305_play_sound_76',
        "command": 'play_sound',
        "args": [Sounds._014_FLOWER, 6]
    },
    {
        "identifier": 'EVENT_2305_action_queue_sync_77',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_1],
        "subscript": [
            {
                "identifier": 'EVENT_2305_action_queue_sync_77_SUBSCRIPT_visibility_on_0',
                "command": 'visibility_on'
            },
            {
                "identifier": 'EVENT_2305_action_queue_sync_77_SUBSCRIPT_set_sprite_sequence_1',
                "command": 'set_sprite_sequence',
                "args": [0, inc_sprite=0, flags=[_0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_2305_action_queue_sync_77_SUBSCRIPT_pause_2',
                "command": 'pause',
                "args": [32]
            },
            {
                "identifier": 'EVENT_2305_action_queue_sync_77_SUBSCRIPT_visibility_off_3',
                "command": 'visibility_off'
            }
        ]
    },
    {
        "identifier": 'EVENT_2305_set_78',
        "command": 'set',
        "args": [0x7000, 1]
    },
    {
        "identifier": 'EVENT_2305_add_max_FP_7000_79',
        "command": 'add_max_FP_7000'
    },
    {
        "identifier": 'EVENT_2305_jmp_80',
        "command": 'jmp',
        "args": ['EVENT_2305_action_queue_sync_99']
    },
    {
        "identifier": 'EVENT_2305_play_sound_81',
        "command": 'play_sound',
        "args": [Sounds._071_MUSHROOM_CURE, 6]
    },
    {
        "identifier": 'EVENT_2305_action_queue_sync_82',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_1],
        "subscript": [
            {
                "identifier": 'EVENT_2305_action_queue_sync_82_SUBSCRIPT_visibility_on_0',
                "command": 'visibility_on'
            },
            {
                "identifier": 'EVENT_2305_action_queue_sync_82_SUBSCRIPT_set_sprite_sequence_1',
                "command": 'set_sprite_sequence',
                "args": [1, inc_sprite=0, flags=[_0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_2305_action_queue_sync_82_SUBSCRIPT_pause_2',
                "command": 'pause',
                "args": [32]
            },
            {
                "identifier": 'EVENT_2305_action_queue_sync_82_SUBSCRIPT_visibility_off_3',
                "command": 'visibility_off'
            }
        ]
    },
    {
        "identifier": 'EVENT_2305_restore_all_hp_83',
        "command": 'restore_all_hp'
    },
    {
        "identifier": 'EVENT_2305_restore_all_fp_84',
        "command": 'restore_all_fp'
    },
    {
        "identifier": 'EVENT_2305_tint_layers_85',
        "command": 'tint_layers',
        "args": [0x40, 0xa0, 0x40, 3, [_0x81Flags.LAYER_1, _0x81Flags.LAYER_2, _0x81Flags.LAYER_3, _0x81Flags.NPC_SPRITES, _0x81Flags.BACKGROUND]]
    },
    {
        "identifier": 'EVENT_2305_tint_layers_86',
        "command": 'tint_layers',
        "args": [0x00, 0x00, 0x00, 3, [_0x81Flags.LAYER_1, _0x81Flags.LAYER_2, _0x81Flags.LAYER_3, _0x81Flags.NPC_SPRITES, _0x81Flags.BACKGROUND]]
    },
    {
        "identifier": 'EVENT_2305_jmp_87',
        "command": 'jmp',
        "args": ['EVENT_2305_action_queue_sync_99']
    },
    {
        "identifier": 'EVENT_2305_play_sound_88',
        "command": 'play_sound',
        "args": [Sounds._027_FOUND_AN_ITEM, 6]
    },
    {
        "identifier": 'EVENT_2305_action_queue_sync_89',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_1],
        "subscript": [
            {
                "identifier": 'EVENT_2305_action_queue_sync_89_SUBSCRIPT_visibility_on_0',
                "command": 'visibility_on'
            },
            {
                "identifier": 'EVENT_2305_action_queue_sync_89_SUBSCRIPT_set_sprite_sequence_1',
                "command": 'set_sprite_sequence',
                "args": [3, inc_sprite=0, flags=[_0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_2305_action_queue_sync_89_SUBSCRIPT_pause_2',
                "command": 'pause',
                "args": [32]
            },
            {
                "identifier": 'EVENT_2305_action_queue_sync_89_SUBSCRIPT_visibility_off_3',
                "command": 'visibility_off'
            }
        ]
    },
    {
        "identifier": 'EVENT_2305_put_inventory_90',
        "command": 'put_inventory',
        "args": [items.RockCandy]
    },
    {
        "identifier": 'EVENT_2305_jmp_91',
        "command": 'jmp',
        "args": ['EVENT_2305_action_queue_sync_99']
    },
    {
        "identifier": 'EVENT_2305_action_queue_async_92',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_1],
        "subscript": [
            {
                "identifier": 'EVENT_2305_action_queue_async_92_SUBSCRIPT_visibility_on_0',
                "command": 'visibility_on'
            },
            {
                "identifier": 'EVENT_2305_action_queue_async_92_SUBSCRIPT_set_sprite_sequence_1',
                "command": 'set_sprite_sequence',
                "args": [4, inc_sprite=0, flags=[_0x08Flags.READ_AS_SEQUENCE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_2305_pause_93',
        "command": 'pause',
        "args": [32]
    },
    {
        "identifier": 'EVENT_2305_start_battle_94',
        "command": 'start_battle',
        "args": [0x009e, 21]
    },
    {
        "identifier": 'EVENT_2305_jmp_if_bit_clear_95',
        "command": 'jmp_if_bit_clear',
        "args": [0x7040, 0, 'EVENT_2305_remove_from_current_level_97']
    },
    {
        "identifier": 'EVENT_2305_reset_and_choose_game_96',
        "command": 'reset_and_choose_game'
    },
    {
        "identifier": 'EVENT_2305_remove_from_current_level_97',
        "command": 'remove_from_current_level',
        "args": [AreaObjects.NPC_1]
    },
    {
        "identifier": 'EVENT_2305_fade_in_from_black_async_98',
        "command": 'fade_in_from_black_async'
    },
    {
        "identifier": 'EVENT_2305_action_queue_sync_99',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_0],
        "subscript": [
            {
                "identifier": 'EVENT_2305_action_queue_sync_99_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [32]
            },
            {
                "identifier": 'EVENT_2305_action_queue_sync_99_SUBSCRIPT_set_animation_speed_1',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_2305_action_queue_sync_99_SUBSCRIPT_set_sprite_sequence_2',
                "command": 'set_sprite_sequence',
                "args": [3, inc_sprite=0, flags=[_0x08Flags.LOOPING_OFF]]
            },
            {
                "identifier": 'EVENT_2305_action_queue_sync_99_SUBSCRIPT_pause_3',
                "command": 'pause',
                "args": [10]
            },
            {
                "identifier": 'EVENT_2305_action_queue_sync_99_SUBSCRIPT_set_sprite_sequence_4',
                "command": 'set_sprite_sequence',
                "args": [4, inc_sprite=0, flags=[_0x08Flags.READ_AS_SEQUENCE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_2305_ret_100',
        "command": 'ret'
    }
]
