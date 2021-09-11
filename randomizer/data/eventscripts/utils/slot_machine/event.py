from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data import items
script = [
    {
        "identifier": 'jmp_if_bit_set_0',
        "command": 'jmp_if_bit_set',
        "args": [0x7044, 2, 'jmp_if_bit_set_15']
    },
    {
        "identifier": 'set_bit_1',
        "command": 'set_bit',
        "args": [0x7044, 2]
    },
    #{
    #    "identifier": 'run_background_event_12',
    #    "command": 'run_background_event',
    #    "args": [93, [_0x40Flags.RETURN_ON_LEVEL_EXIT]]
    #}, # background event disables non-jump controls to make you finish the slot machine chest - decided not to do this since it has too much potential for softlocking
    {
        "identifier": 'pause_action_script_2',
        "command": 'pause_action_script',
        "args": [AreaObjects.MEM_70A8]
    },
    {
        "identifier": 'set_7016_to_object_xyz_2',
        "command": 'set_7016_to_object_xyz',
        "args": [AreaObjects.MEM_70A8]
    },
    {
        "identifier": 'add_short_14',
        "command": 'add_short',
        "args": [0x701A, 304]
    },
    {
        "identifier": 'action_queue_async_3',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MEM_70A8],
        "subscript": [
            {
                "identifier": 'action_queue_sync_3_SUBSCRIPT_sequence_looping_on_0',
                "command": 'sequence_looping_on'
            },
            {
                "identifier": 'action_queue_sync_3_SUBSCRIPT_set_sprite_sequence_1',
                "command": 'set_sprite_sequence',
                "args": [1, 0, [_0x08Flags.LOOPING_OFF]]
            },
            {
                "identifier": 'action_queue_sync_3_SUBSCRIPT_pause_2',
                "command": 'pause',
                "args": [6]
            },
            {
                "identifier": 'action_queue_sync_3_SUBSCRIPT_set_sprite_sequence_3',
                "command": 'set_sprite_sequence',
                "args": [2, 0, [_0x08Flags.READ_AS_SEQUENCE]]
            }
        ]
    },
    {
        "identifier": 'action_queue_move_slot_NPC_3',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_2],
        "subscript": [
            {
                "identifier": 'EVENT_2549_action_queue_sync_11_SUBSCRIPT_shift_south_pixels_1',
                "command": 'transfer_to_7016_7018_701A'
            }
        ]
    },
    {
        "identifier": 'action_queue_move_slot_NPC_4',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_3],
        "subscript": [
            {
                "identifier": 'EVENT_2549_action_queue_sync_11_SUBSCRIPT_shift_south_pixels_1',
                "command": 'transfer_to_7016_7018_701A'
            }
        ]
    },
    {
        "identifier": 'action_queue_move_slot_NPC_5',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_4],
        "subscript": [
            {
                "identifier": 'EVENT_2549_action_queue_sync_11_SUBSCRIPT_shift_south_pixels_1',
                "command": 'transfer_to_7016_7018_701A'
            }
        ]
    },
    {
        "identifier": 'action_queue_move_slot_NPC_6',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_5],
        "subscript": [
            {
                "identifier": 'EVENT_2549_action_queue_sync_11_SUBSCRIPT_shift_south_pixels_1',
                "command": 'transfer_to_7016_7018_701A'
            }
        ]
    },
    {
        "identifier": 'action_queue_move_slot_NPC_7',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_6],
        "subscript": [
            {
                "identifier": 'EVENT_2549_action_queue_sync_11_SUBSCRIPT_shift_south_pixels_1',
                "command": 'transfer_to_7016_7018_701A'
            }
        ]
    },
    {
        "identifier": 'pause_4',
        "command": 'pause',
        "args": [6]
    },
    {
        "identifier": 'summon_to_current_level_5',
        "command": 'summon_to_current_level',
        "args": [AreaObjects.NPC_2]
    },
    {
        "identifier": 'summon_to_current_level_6',
        "command": 'summon_to_current_level',
        "args": [AreaObjects.NPC_3]
    },
    {
        "identifier": 'summon_to_current_level_7',
        "command": 'summon_to_current_level',
        "args": [AreaObjects.NPC_4]
    },
    {
        "identifier": 'pause_8',
        "command": 'pause',
        "args": [1]
    },
    {
        "identifier": 'action_queue_sync_9',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_3],
        "subscript": [
            {
                "identifier": 'action_queue_sync_9_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FASTEST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'action_queue_sync_9_SUBSCRIPT_shift_east_pixels_1',
                "command": 'shift_east_pixels',
                "args": [17]
            }
        ]
    },
    {
        "identifier": 'action_queue_async_10',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_4],
        "subscript": [
            {
                "identifier": 'action_queue_async_10_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FASTEST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'action_queue_async_10_SUBSCRIPT_shift_west_pixels_1',
                "command": 'shift_west_pixels',
                "args": [17]
            }
        ]
    },
    {
        "identifier": 'set_action_script_sync_11',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_2, 185]
    },
    {
        "identifier": 'set_action_script_sync_12',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_3, 186]
    },
    {
        "identifier": 'set_action_script_sync_13',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_4, 184]
    },
    {
        "identifier": 'ret_14',
        "command": 'ret'
    },
    {
        "identifier": 'jmp_if_bit_set_15',
        "command": 'jmp_if_bit_set',
        "args": [0x7044, 3, 'jmp_if_bit_set_19']
    },
    {
        "identifier": 'set_bit_16',
        "command": 'set_bit',
        "args": [0x7044, 3]
    },
    {
        "identifier": 'pause_action_script_17',
        "command": 'pause_action_script',
        "args": [AreaObjects.NPC_4]
    },
    {
        "identifier": 'ret_18',
        "command": 'ret'
    },
    {
        "identifier": 'jmp_if_bit_set_19',
        "command": 'jmp_if_bit_set',
        "args": [0x7044, 4, 'disable_trigger_23']
    },
    {
        "identifier": 'set_bit_20',
        "command": 'set_bit',
        "args": [0x7044, 4]
    },
    {
        "identifier": 'pause_action_script_21',
        "command": 'pause_action_script',
        "args": [AreaObjects.NPC_2]
    },
    {
        "identifier": 'ret_22',
        "command": 'ret'
    },
    {
        "identifier": 'disable_trigger_23',
        "command": 'disable_trigger',
        "args": [AreaObjects.MEM_70A8]
    },
    {
        "identifier": 'pause_action_script_24',
        "command": 'pause_action_script',
        "args": [AreaObjects.NPC_3]
    },
    {
        "identifier": 'pause_25',
        "command": 'pause',
        "args": [16]
    },
    {
        "identifier": 'action_queue_sync_26',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_4],
        "subscript": [
            {
                "identifier": 'action_queue_sync_26_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'action_queue_sync_26_SUBSCRIPT_shift_east_pixels_1',
                "command": 'shift_east_pixels',
                "args": [8]
            }
        ]
    },
    {
        "identifier": 'action_queue_sync_27',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_3],
        "subscript": [
            {
                "identifier": 'action_queue_sync_27_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'action_queue_sync_27_SUBSCRIPT_shift_west_pixels_1',
                "command": 'shift_west_pixels',
                "args": [8]
            }
        ]
    },
    {
        "identifier": 'stop_embedded_action_script_28',
        "command": 'stop_embedded_action_script',
        "args": [AreaObjects.NPC_3]
    },
    {
        "identifier": 'stop_embedded_action_script_29',
        "command": 'stop_embedded_action_script',
        "args": [AreaObjects.NPC_4]
    },
    {
        "identifier": 'remove_from_current_level_30',
        "command": 'remove_from_current_level',
        "args": [AreaObjects.NPC_2]
    },
    {
        "identifier": 'remove_from_current_level_31',
        "command": 'remove_from_current_level',
        "args": [AreaObjects.NPC_3]
    },
    {
        "identifier": 'remove_from_current_level_32',
        "command": 'remove_from_current_level',
        "args": [AreaObjects.NPC_4]
    },
    {
        "identifier": 'summon_to_current_level_33',
        "command": 'summon_to_current_level',
        "args": [AreaObjects.NPC_6]
    },
    {
        "identifier": 'action_queue_async_34',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_6],
        "subscript": [
            {
                "identifier": 'action_queue_async_34_SUBSCRIPT_set_vram_priority_0',
                "command": 'set_vram_priority',
                "args": [VramPriority.OBJECT_OVERLAPS_MARIO_ON_ALL_SIDES]
            },
            {
                "identifier": 'action_queue_async_34_SUBSCRIPT_set_sprite_sequence_1',
                "command": 'set_sprite_sequence',
                "args": [1, 0, [_0x08Flags.LOOPING_OFF]]
            },
            {
                "identifier": 'action_queue_async_34_SUBSCRIPT_pause_2',
                "command": 'pause',
                "args": [16]
            },
            {
                "identifier": 'action_queue_async_34_SUBSCRIPT_visibility_off_3',
                "command": 'visibility_off'
            }
        ]
    },
    {
        "identifier": 'jmp_if_var_equals_byte_35',
        "command": 'jmp_if_var_equals_byte',
        "args": [0x70c0, 0, 'jmp_if_var_equals_byte_38']
    },
    {
        "identifier": 'jmp_if_var_equals_byte_36',
        "command": 'jmp_if_var_equals_byte',
        "args": [0x70c0, 1, 'jmp_if_var_equals_byte_41']
    },
    {
        "identifier": 'jmp_if_var_equals_byte_37',
        "command": 'jmp_if_var_equals_byte',
        "args": [0x70c0, 2, 'jmp_if_var_equals_byte_44']
    },
    {
        "identifier": 'jmp_if_var_equals_byte_38',
        "command": 'jmp_if_var_equals_byte',
        "args": [0x70c1, 0, 'jmp_if_var_equals_byte_47']
    },
    {
        "identifier": 'jmp_if_var_equals_byte_39',
        "command": 'jmp_if_var_equals_byte',
        "args": [0x70c1, 1, 'jmp_if_var_equals_byte_49']
    },
    {
        "identifier": 'jmp_40',
        "command": 'jmp',
        "args": ['jmp_if_var_equals_byte_52']
    },
    {
        "identifier": 'jmp_if_var_equals_byte_41',
        "command": 'jmp_if_var_equals_byte',
        "args": [0x70c1, 0, 'jmp_if_var_equals_byte_55']
    },
    {
        "identifier": 'jmp_if_var_equals_byte_42',
        "command": 'jmp_if_var_equals_byte',
        "args": [0x70c1, 1, 'jmp_if_var_equals_byte_58']
    },
    {
        "identifier": 'jmp_43',
        "command": 'jmp',
        "args": ['jmp_if_var_equals_byte_60']
    },
    {
        "identifier": 'jmp_if_var_equals_byte_44',
        "command": 'jmp_if_var_equals_byte',
        "args": [0x70c1, 0, 'jmp_if_var_equals_byte_63']
    },
    {
        "identifier": 'jmp_if_var_equals_byte_45',
        "command": 'jmp_if_var_equals_byte',
        "args": [0x70c1, 1, 'jmp_if_var_equals_byte_66']
    },
    {
        "identifier": 'jmp_46',
        "command": 'jmp',
        "args": ['jmp_if_var_equals_byte_69']
    },
    {
        "identifier": 'jmp_if_var_equals_byte_47',
        "command": 'jmp_if_var_equals_byte',
        "args": [0x70c2, 0, 'summon_to_current_level_71']
    },
    {
        "identifier": 'jmp_48',
        "command": 'jmp',
        "args": ['play_sound_76']
    },
    {
        "identifier": 'jmp_if_var_equals_byte_49',
        "command": 'jmp_if_var_equals_byte',
        "args": [0x70c2, 0, 'play_sound_76']
    },
    {
        "identifier": 'jmp_if_var_equals_byte_50',
        "command": 'jmp_if_var_equals_byte',
        "args": [0x70c2, 1, 'play_sound_81']
    },
    {
        "identifier": 'jmp_51',
        "command": 'jmp',
        "args": ['action_queue_async_92']
    },
    {
        "identifier": 'jmp_if_var_equals_byte_52',
        "command": 'jmp_if_var_equals_byte',
        "args": [0x70c2, 0, 'play_sound_76']
    },
    {
        "identifier": 'jmp_if_var_equals_byte_53',
        "command": 'jmp_if_var_equals_byte',
        "args": [0x70c2, 1, 'action_queue_async_92']
    },
    {
        "identifier": 'jmp_54',
        "command": 'jmp',
        "args": ['play_sound_88']
    },
    {
        "identifier": 'jmp_if_var_equals_byte_55',
        "command": 'jmp_if_var_equals_byte',
        "args": [0x70c2, 0, 'play_sound_76']
    },
    {
        "identifier": 'jmp_if_var_equals_byte_56',
        "command": 'jmp_if_var_equals_byte',
        "args": [0x70c2, 1, 'play_sound_81']
    },
    {
        "identifier": 'jmp_57',
        "command": 'jmp',
        "args": ['action_queue_async_92']
    },
    {
        "identifier": 'jmp_if_var_equals_byte_58',
        "command": 'jmp_if_var_equals_byte',
        "args": [0x70c2, 1, 'summon_to_current_level_71']
    },
    {
        "identifier": 'jmp_59',
        "command": 'jmp',
        "args": ['play_sound_81']
    },
    {
        "identifier": 'jmp_if_var_equals_byte_60',
        "command": 'jmp_if_var_equals_byte',
        "args": [0x70c2, 0, 'action_queue_async_92']
    },
    {
        "identifier": 'jmp_if_var_equals_byte_61',
        "command": 'jmp_if_var_equals_byte',
        "args": [0x70c2, 1, 'play_sound_81']
    },
    {
        "identifier": 'jmp_62',
        "command": 'jmp',
        "args": ['play_sound_88']
    },
    {
        "identifier": 'jmp_if_var_equals_byte_63',
        "command": 'jmp_if_var_equals_byte',
        "args": [0x70c2, 0, 'play_sound_76']
    },
    {
        "identifier": 'jmp_if_var_equals_byte_64',
        "command": 'jmp_if_var_equals_byte',
        "args": [0x70c2, 1, 'action_queue_async_92']
    },
    {
        "identifier": 'jmp_65',
        "command": 'jmp',
        "args": ['play_sound_88']
    },
    {
        "identifier": 'jmp_if_var_equals_byte_66',
        "command": 'jmp_if_var_equals_byte',
        "args": [0x70c2, 0, 'action_queue_async_92']
    },
    {
        "identifier": 'jmp_if_var_equals_byte_67',
        "command": 'jmp_if_var_equals_byte',
        "args": [0x70c2, 1, 'play_sound_81']
    },
    {
        "identifier": 'jmp_68',
        "command": 'jmp',
        "args": ['play_sound_88']
    },
    {
        "identifier": 'jmp_if_var_equals_byte_69',
        "command": 'jmp_if_var_equals_byte',
        "args": [0x70c2, 2, 'summon_to_current_level_71']
    },
    {
        "identifier": 'jmp_70',
        "command": 'jmp',
        "args": ['play_sound_88']
    },
    {
        "identifier": 'summon_to_current_level_71',
        "command": 'summon_to_current_level',
        "args": [AreaObjects.NPC_5]
    },
    {
        "identifier": 'play_sound_72',
        "command": 'play_sound',
        "args": [Sounds._094_FROG_COIN, 6]
    },
    {
        "identifier": 'action_queue_sync_73',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_5],
        "subscript": [
            {
                "identifier": 'action_queue_sync_73_SUBSCRIPT_set_vram_priority_0',
                "command": 'set_vram_priority',
                "args": [VramPriority.OBJECT_OVERLAPS_MARIO_ON_ALL_SIDES]
            },
            {
                "identifier": 'action_queue_sync_73_SUBSCRIPT_set_priority_1',
                "command": 'set_priority',
                "args": [3]
            },
            {
                "identifier": 'action_queue_sync_73_SUBSCRIPT_set_sprite_sequence_2',
                "command": 'set_sprite_sequence',
                "args": [1, 0, [_0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'action_queue_sync_73_SUBSCRIPT_pause_3',
                "command": 'pause',
                "args": [32]
            },
            {
                "identifier": 'action_queue_sync_73_SUBSCRIPT_visibility_off_4',
                "command": 'visibility_off'
            }
        ]
    },
    {
        "identifier": 'add_frog_coins_74',
        "command": 'add_frog_coins',
        "args": [1]
    },
    {
        "identifier": 'jmp_75',
        "command": 'jmp',
        "args": ['action_queue_sync_99']
    },
    {
        "identifier": 'play_sound_76',
        "command": 'play_sound',
        "args": [Sounds._014_FLOWER, 6]
    },
    {
        "identifier": 'action_queue_sync_77',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_2],
        "subscript": [
            {
                "identifier": 'action_queue_sync_77_SUBSCRIPT_visibility_on_0',
                "command": 'visibility_on'
            },
            {
                "identifier": 'action_queue_sync_77_SUBSCRIPT_set_sprite_sequence_1',
                "command": 'set_sprite_sequence',
                "args": [0, 0, [_0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'action_queue_sync_77_SUBSCRIPT_pause_2',
                "command": 'pause',
                "args": [32]
            },
            {
                "identifier": 'action_queue_sync_77_SUBSCRIPT_visibility_off_3',
                "command": 'visibility_off'
            }
        ]
    },
    {
        "identifier": 'set_78',
        "command": 'set',
        "args": [0x7000, 1]
    },
    {
        "identifier": 'add_max_FP_7000_79',
        "command": 'add_max_FP_7000'
    },
    {
        "identifier": 'jmp_80',
        "command": 'jmp',
        "args": ['action_queue_sync_99']
    },
    {
        "identifier": 'play_sound_81',
        "command": 'play_sound',
        "args": [Sounds._071_MUSHROOM_CURE, 6]
    },
    {
        "identifier": 'action_queue_sync_82',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_2],
        "subscript": [
            {
                "identifier": 'action_queue_sync_82_SUBSCRIPT_visibility_on_0',
                "command": 'visibility_on'
            },
            {
                "identifier": 'action_queue_sync_82_SUBSCRIPT_set_sprite_sequence_1',
                "command": 'set_sprite_sequence',
                "args": [1, 0, [_0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'action_queue_sync_82_SUBSCRIPT_pause_2',
                "command": 'pause',
                "args": [32]
            },
            {
                "identifier": 'action_queue_sync_82_SUBSCRIPT_visibility_off_3',
                "command": 'visibility_off'
            }
        ]
    },
    {
        "identifier": 'restore_all_hp_83',
        "command": 'restore_all_hp'
    },
    {
        "identifier": 'restore_all_fp_84',
        "command": 'restore_all_fp'
    },
    {
        "identifier": 'tint_layers_85',
        "command": 'tint_layers',
        "args": [0x40, 0xa0, 0x40, 3, [_0x81Flags.LAYER_1, _0x81Flags.LAYER_2, _0x81Flags.LAYER_3, _0x81Flags.LAYER_4, _0x81Flags.NPC_SPRITES, _0x81Flags.BACKGROUND], [7]]
    },
    {
        "identifier": 'tint_layers_86',
        "command": 'tint_layers',
        "args": [0x00, 0x00, 0x00, 3, [_0x81Flags.LAYER_1, _0x81Flags.LAYER_2, _0x81Flags.LAYER_3, _0x81Flags.LAYER_4, _0x81Flags.NPC_SPRITES, _0x81Flags.BACKGROUND], [7]]
    },
    {
        "identifier": 'jmp_87',
        "command": 'jmp',
        "args": ['action_queue_sync_99']
    },
    {
        "identifier": 'play_sound_88',
        "command": 'play_sound',
        "args": [Sounds._027_FOUND_AN_ITEM, 6]
    },
    {
        "identifier": 'action_queue_sync_89',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_2],
        "subscript": [
            {
                "identifier": 'action_queue_sync_89_SUBSCRIPT_visibility_on_0',
                "command": 'visibility_on'
            },
            {
                "identifier": 'action_queue_sync_89_SUBSCRIPT_set_sprite_sequence_1',
                "command": 'set_sprite_sequence',
                "args": [3, 0, [_0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'action_queue_sync_89_SUBSCRIPT_pause_2',
                "command": 'pause',
                "args": [32]
            },
            {
                "identifier": 'action_queue_sync_89_SUBSCRIPT_visibility_off_3',
                "command": 'visibility_off'
            }
        ]
    },
    {
        "identifier": 'put_inventory_90',
        "command": 'put_inventory',
        "args": [items.RockCandy]
    },
    {
        "identifier": 'jmp_91',
        "command": 'jmp',
        "args": ['action_queue_sync_99']
    },
    {
        "identifier": 'action_queue_async_92',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_2],
        "subscript": [
            {
                "identifier": 'action_queue_async_92_SUBSCRIPT_visibility_on_0',
                "command": 'visibility_on'
            },
            {
                "identifier": 'action_queue_async_92_SUBSCRIPT_set_sprite_sequence_1',
                "command": 'set_sprite_sequence',
                "args": [4, 0, [_0x08Flags.READ_AS_SEQUENCE]]
            }
        ]
    },
    {
        "identifier": 'pause_93',
        "command": 'pause',
        "args": [32]
    },
    {
        "identifier": 'set_7K',
        "command": 'start_battle',
        "args": [518, 0x31]
    },
    {
        "identifier": 'jmp_if_bit_clear_47',
        "command": 'jmp_if_bit_set',
        "args": [0x7040, 0, 'reset_and_choose_game_48']
    },
    {
        "identifier": 'remove_from_current_level_97',
        "command": 'remove_from_current_level',
        "args": [AreaObjects.NPC_2]
    },
    {
        "identifier": 'jmp_if_bit_set_351',
        "command": 'jmp_if_bit_clear',
        "args": [0x7086, 7, 'fade_in_from_black_async_98']
    },
    {
        "identifier": 'start_battle_94_',
        "command": 'run_event_as_subroutine',
        "args": [171]
    },
    {
        "identifier": 'fade_in_from_black_async_98',
        "command": 'fade_in_from_black_async'
    },
    {
        "identifier": 'action_queue_sync_99',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MEM_70A8],
        "subscript": [
            {
                "identifier": 'action_queue_sync_99_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [32]
            },
            {
                "identifier": 'action_queue_sync_99_SUBSCRIPT_set_animation_speed_1',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'action_queue_sync_99_SUBSCRIPT_set_sprite_sequence_2',
                "command": 'set_sprite_sequence',
                "args": [3, 0, [_0x08Flags.LOOPING_OFF]]
            },
            {
                "identifier": 'action_queue_sync_99_SUBSCRIPT_pause_3',
                "command": 'pause',
                "args": [10]
            },
            {
                "identifier": 'action_queue_sync_99_SUBSCRIPT_set_sprite_sequence_4',
                "command": 'set_sprite_sequence',
                "args": [4, 0, [_0x08Flags.READ_AS_SEQUENCE]]
            }
        ]
    },
    {
        "identifier": 'disable_99',
        "command": 'disable_trigger',
        "args": [AreaObjects.MEM_70A8]
    },
    {
        "identifier": 'disable_event_trigger_for_object_at_70A8_2',
        "command": 'disable_event_trigger_for_object_at_70A8'
    },
    {
        "identifier": 'clear_bit_1',
        "command": 'clear_bit',
        "args": [0x7044, 2]
    },
    {
        "identifier": 'clear_bit_2',
        "command": 'clear_bit',
        "args": [0x7044, 3]
    },
    {
        "identifier": 'clear_bit_3',
        "command": 'clear_bit',
        "args": [0x7044, 4]
    },
    {
        "identifier": 'ret_100',
        "command": 'ret'
    },
    {
        "identifier": 'reset_and_choose_game_48',
        "command": 'reset_and_choose_game'
    },
    {
        "identifier": 'ret_100_',
        "command": 'ret'
    },
]
