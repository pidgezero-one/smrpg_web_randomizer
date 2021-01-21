from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data import items
script = [
    {
        "identifier": 'EVENT_2081_set_short_0',
        "command": 'set_short',
        "args": [0x7022, 0x0008]
    },
    {
        "identifier": 'EVENT_2081_run_background_event_with_pause_1',
        "command": 'run_background_event_with_pause',
        "args": [3075, 0x7022, [12, 13]]
    },
    {
        "identifier": 'EVENT_2081_play_sound_2',
        "command": 'play_sound',
        "args": [Sounds._071_MUSHROOM_CURE, 6]
    },
    {
        "identifier": 'EVENT_2081_restore_all_hp_3',
        "command": 'restore_all_hp'
    },
    {
        "identifier": 'EVENT_2081_restore_all_fp_4',
        "command": 'restore_all_fp'
    },
    {
        "identifier": 'EVENT_2081_set_5',
        "command": 'set',
        "args": [0x70a7, 161]
    },
    {
        "identifier": 'EVENT_2081_store_7000_item_quantity_to_70A7_6',
        "command": 'store_7000_item_quantity_to_70A7'
    },
    {
        "identifier": 'EVENT_2081_jmp_if_var_equals_short_7',
        "command": 'jmp_if_var_equals_short',
        "args": [0x7000, 0, 'EVENT_2081_ret_21']
    },
    {
        "identifier": 'EVENT_2081_set_8',
        "command": 'set',
        "args": [0x70a7, 162]
    },
    {
        "identifier": 'EVENT_2081_store_7000_item_quantity_to_70A7_9',
        "command": 'store_7000_item_quantity_to_70A7'
    },
    {
        "identifier": 'EVENT_2081_jmp_if_var_equals_short_10',
        "command": 'jmp_if_var_equals_short',
        "args": [0x7000, 0, 'EVENT_2081_ret_21']
    },
    {
        "identifier": 'EVENT_2081_set_11',
        "command": 'set',
        "args": [0x70a7, 163]
    },
    {
        "identifier": 'EVENT_2081_store_7000_item_quantity_to_70A7_12',
        "command": 'store_7000_item_quantity_to_70A7'
    },
    {
        "identifier": 'EVENT_2081_jmp_if_var_equals_short_13',
        "command": 'jmp_if_var_equals_short',
        "args": [0x7000, 0, 'EVENT_2081_ret_21']
    },
    {
        "identifier": 'EVENT_2081_set_14',
        "command": 'set',
        "args": [0x70a7, 0]
    },
    {
        "identifier": 'EVENT_2081_set_15',
        "command": 'set',
        "args": [0x70a7, 89]
    },
    {
        "identifier": 'EVENT_2081_set_16',
        "command": 'set',
        "args": [0x7000, 524]
    },
    {
        "identifier": 'EVENT_2081_run_event_as_subroutine_17',
        "command": 'run_event_as_subroutine',
        "args": [3828]
    },
    {
        "identifier": 'EVENT_2081_remove_one_from_inventory_18',
        "command": 'remove_one_from_inventory',
        "args": [items.BigBooFlag]
    },
    {
        "identifier": 'EVENT_2081_remove_one_from_inventory_19',
        "command": 'remove_one_from_inventory',
        "args": [items.DryBonesFlag]
    },
    {
        "identifier": 'EVENT_2081_remove_one_from_inventory_20',
        "command": 'remove_one_from_inventory',
        "args": [items.GreaperFlag]
    },
    {
        "identifier": 'EVENT_2081_ret_21',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_2081_move_script_to_main_thread_22',
        "command": 'move_script_to_main_thread'
    },
    {
        "identifier": 'EVENT_2081_set_bit_23',
        "command": 'set_bit',
        "args": [0x7049, 5]
    },
    {
        "identifier": 'EVENT_2081_action_queue_async_24',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_3],
        "subscript": [
            {
                "identifier": 'EVENT_2081_action_queue_async_24_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [2]
            },
            {
                "identifier": 'EVENT_2081_action_queue_async_24_SUBSCRIPT_set_sprite_sequence_1',
                "command": 'set_sprite_sequence',
                "args": [12, 0, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_2081_action_queue_async_24_SUBSCRIPT_pause_2',
                "command": 'pause',
                "args": [4]
            },
            {
                "identifier": 'EVENT_2081_action_queue_async_24_SUBSCRIPT_set_sprite_sequence_3',
                "command": 'set_sprite_sequence',
                "args": [13, 0, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_2081_apply_tile_mod_25',
        "command": 'apply_tile_mod',
        "args": [Rooms._399_MONSTRO_TOWN_3_MUSTY_FEARS_INN, 32, [_0x6AFlags.USE_ALTERNATE]]
    },
    {
        "identifier": 'EVENT_2081_action_queue_async_26',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_2081_action_queue_async_26_SUBSCRIPT_shift_northeast_pixels_0',
                "command": 'shift_northeast_pixels',
                "args": [16]
            },
            {
                "identifier": 'EVENT_2081_action_queue_async_26_SUBSCRIPT_shift_south_pixels_1',
                "command": 'shift_south_pixels',
                "args": [2]
            },
            {
                "identifier": 'EVENT_2081_action_queue_async_26_SUBSCRIPT_set_animation_speed_2',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.SLOW, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_2081_action_queue_async_26_SUBSCRIPT_set_sprite_sequence_3',
                "command": 'set_sprite_sequence',
                "args": [13, 0, [_0x08Flags.READ_AS_SEQUENCE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_2081_set_action_script_sync_27',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_0, 568]
    },
    {
        "identifier": 'EVENT_2081_pause_28',
        "command": 'pause',
        "args": [60]
    },
    {
        "identifier": 'EVENT_2081_run_dialog_29',
        "command": 'run_dialog',
        "args": [2966, AreaObjects.MARIO, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_2081_pause_30',
        "command": 'pause',
        "args": [20]
    },
    {
        "identifier": 'EVENT_2081_set_action_script_sync_31',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_1, 568]
    },
    {
        "identifier": 'EVENT_2081_pause_32',
        "command": 'pause',
        "args": [60]
    },
    {
        "identifier": 'EVENT_2081_run_dialog_33',
        "command": 'run_dialog',
        "args": [2964, AreaObjects.MARIO, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_2081_pause_34',
        "command": 'pause',
        "args": [20]
    },
    {
        "identifier": 'EVENT_2081_set_action_script_sync_35',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_2, 568]
    },
    {
        "identifier": 'EVENT_2081_pause_36',
        "command": 'pause',
        "args": [60]
    },
    {
        "identifier": 'EVENT_2081_run_dialog_37',
        "command": 'run_dialog',
        "args": [2965, AreaObjects.MARIO, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_2081_pause_38',
        "command": 'pause',
        "args": [20]
    },
    {
        "identifier": 'EVENT_2081_run_dialog_39',
        "command": 'run_dialog',
        "args": [2967, AreaObjects.MARIO, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_2081_pause_40',
        "command": 'pause',
        "args": [60]
    },
    {
        "identifier": 'EVENT_2081_action_queue_async_41',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_0],
        "subscript": [
            {
                "identifier": 'EVENT_2081_action_queue_async_41_SUBSCRIPT_face_southeast_0',
                "command": 'face_southeast'
            },
            {
                "identifier": 'EVENT_2081_action_queue_async_41_SUBSCRIPT_pause_1',
                "command": 'pause',
                "args": [30]
            }
        ]
    },
    {
        "identifier": 'EVENT_2081_run_dialog_42',
        "command": 'run_dialog',
        "args": [2968, AreaObjects.MARIO, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_2081_pause_43',
        "command": 'pause',
        "args": [15]
    },
    {
        "identifier": 'EVENT_2081_action_queue_async_44',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_2],
        "subscript": [
            {
                "identifier": 'EVENT_2081_action_queue_async_44_SUBSCRIPT_face_northwest_0',
                "command": 'face_northwest'
            },
            {
                "identifier": 'EVENT_2081_action_queue_async_44_SUBSCRIPT_pause_1',
                "command": 'pause',
                "args": [30]
            }
        ]
    },
    {
        "identifier": 'EVENT_2081_run_dialog_45',
        "command": 'run_dialog',
        "args": [2969, AreaObjects.MARIO, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_2081_pause_46',
        "command": 'pause',
        "args": [30]
    },
    {
        "identifier": 'EVENT_2081_run_dialog_47',
        "command": 'run_dialog',
        "args": [2970, AreaObjects.MARIO, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_2081_pause_48',
        "command": 'pause',
        "args": [20]
    },
    {
        "identifier": 'EVENT_2081_action_queue_sync_49',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_0],
        "subscript": [
            {
                "identifier": 'EVENT_2081_action_queue_sync_49_SUBSCRIPT_face_southwest_0',
                "command": 'face_southwest'
            }
        ]
    },
    {
        "identifier": 'EVENT_2081_action_queue_async_50',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_2],
        "subscript": [
            {
                "identifier": 'EVENT_2081_action_queue_async_50_SUBSCRIPT_face_southwest_0',
                "command": 'face_southwest'
            }
        ]
    },
    {
        "identifier": 'EVENT_2081_pause_51',
        "command": 'pause',
        "args": [20]
    },
    {
        "identifier": 'EVENT_2081_action_queue_sync_52',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_0],
        "subscript": [
            {
                "identifier": 'EVENT_2081_action_queue_sync_52_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.SLOW, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_2081_action_queue_sync_52_SUBSCRIPT_shift_z_down_steps_1',
                "command": 'shift_z_down_steps',
                "args": [1]
            }
        ]
    },
    {
        "identifier": 'EVENT_2081_action_queue_sync_53',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_1],
        "subscript": [
            {
                "identifier": 'EVENT_2081_action_queue_sync_53_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.SLOW, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_2081_action_queue_sync_53_SUBSCRIPT_shift_z_down_steps_1',
                "command": 'shift_z_down_steps',
                "args": [1]
            }
        ]
    },
    {
        "identifier": 'EVENT_2081_action_queue_async_54',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_2],
        "subscript": [
            {
                "identifier": 'EVENT_2081_action_queue_async_54_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.SLOW, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_2081_action_queue_async_54_SUBSCRIPT_shift_z_down_steps_1',
                "command": 'shift_z_down_steps',
                "args": [1]
            }
        ]
    },
    {
        "identifier": 'EVENT_2081_pause_55',
        "command": 'pause',
        "args": [10]
    },
    {
        "identifier": 'EVENT_2081_action_queue_sync_56',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_0],
        "subscript": [
            {
                "identifier": 'EVENT_2081_action_queue_sync_56_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.SLOW, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_2081_action_queue_sync_56_SUBSCRIPT_shift_southwest_steps_1',
                "command": 'shift_southwest_steps',
                "args": [2]
            },
            {
                "identifier": 'EVENT_2081_action_queue_sync_56_SUBSCRIPT_face_southeast_2',
                "command": 'face_southeast'
            }
        ]
    },
    {
        "identifier": 'EVENT_2081_action_queue_async_57',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_2],
        "subscript": [
            {
                "identifier": 'EVENT_2081_action_queue_async_57_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.SLOW, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_2081_action_queue_async_57_SUBSCRIPT_shift_southwest_steps_1',
                "command": 'shift_southwest_steps',
                "args": [2]
            },
            {
                "identifier": 'EVENT_2081_action_queue_async_57_SUBSCRIPT_face_northwest_2',
                "command": 'face_northwest'
            }
        ]
    },
    {
        "identifier": 'EVENT_2081_pause_58',
        "command": 'pause',
        "args": [45]
    },
    {
        "identifier": 'EVENT_2081_set_action_script_sync_59',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_1, 870]
    },
    {
        "identifier": 'EVENT_2081_run_dialog_60',
        "command": 'run_dialog',
        "args": [2989, AreaObjects.MARIO, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_2081_set_action_script_sync_61',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_1, 871]
    },
    {
        "identifier": 'EVENT_2081_pause_62',
        "command": 'pause',
        "args": [20]
    },
    {
        "identifier": 'EVENT_2081_set_action_script_sync_63',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_0, 872]
    },
    {
        "identifier": 'EVENT_2081_run_dialog_64',
        "command": 'run_dialog',
        "args": [2990, AreaObjects.MARIO, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_2081_set_action_script_sync_65',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_0, 873]
    },
    {
        "identifier": 'EVENT_2081_pause_66',
        "command": 'pause',
        "args": [20]
    },
    {
        "identifier": 'EVENT_2081_set_action_script_sync_67',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_2, 874]
    },
    {
        "identifier": 'EVENT_2081_run_dialog_68',
        "command": 'run_dialog',
        "args": [2991, AreaObjects.MARIO, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_2081_set_action_script_sync_69',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_2, 875]
    },
    {
        "identifier": 'EVENT_2081_pause_70',
        "command": 'pause',
        "args": [20]
    },
    {
        "identifier": 'EVENT_2081_run_dialog_71',
        "command": 'run_dialog',
        "args": [2992, AreaObjects.MARIO, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_2081_pause_72',
        "command": 'pause',
        "args": [10]
    },
    {
        "identifier": 'EVENT_2081_set_action_script_sync_73',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_0, 569]
    },
    {
        "identifier": 'EVENT_2081_set_action_script_sync_74',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_1, 569]
    },
    {
        "identifier": 'EVENT_2081_set_action_script_sync_75',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_2, 569]
    },
    {
        "identifier": 'EVENT_2081_pause_76',
        "command": 'pause',
        "args": [110]
    },
    {
        "identifier": 'EVENT_2081_action_queue_async_77',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_3],
        "subscript": [
            {
                "identifier": 'EVENT_2081_action_queue_async_77_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.SLOW, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_2081_action_queue_async_77_SUBSCRIPT_reset_properties_1',
                "command": 'reset_properties'
            },
            {
                "identifier": 'EVENT_2081_action_queue_async_77_SUBSCRIPT_sequence_looping_on_2',
                "command": 'sequence_looping_on'
            },
            {
                "identifier": 'EVENT_2081_action_queue_async_77_SUBSCRIPT_pause_3',
                "command": 'pause',
                "args": [20]
            },
            {
                "identifier": 'EVENT_2081_action_queue_async_77_SUBSCRIPT_set_animation_speed_4',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_2081_action_queue_async_77_SUBSCRIPT_walk_to_xy_coords_5',
                "command": 'walk_to_xy_coords',
                "args": [5, 47]
            }
        ]
    },
    {
        "identifier": 'EVENT_2081_run_dialog_78',
        "command": 'run_dialog',
        "args": [2993, AreaObjects.MARIO, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_2081_action_queue_async_79',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_3],
        "subscript": [
            {
                "identifier": 'EVENT_2081_action_queue_async_79_SUBSCRIPT_walk_to_xy_coords_0',
                "command": 'walk_to_xy_coords',
                "args": [8, 46]
            },
            {
                "identifier": 'EVENT_2081_action_queue_async_79_SUBSCRIPT_pause_1',
                "command": 'pause',
                "args": [2]
            },
            {
                "identifier": 'EVENT_2081_action_queue_async_79_SUBSCRIPT_set_sprite_sequence_2',
                "command": 'set_sprite_sequence',
                "args": [12, 0, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_2081_action_queue_async_79_SUBSCRIPT_pause_3',
                "command": 'pause',
                "args": [4]
            },
            {
                "identifier": 'EVENT_2081_action_queue_async_79_SUBSCRIPT_set_sprite_sequence_4',
                "command": 'set_sprite_sequence',
                "args": [13, 0, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_2081_pause_80',
        "command": 'pause',
        "args": [110]
    },
    {
        "identifier": 'EVENT_2081_set_action_script_sync_81',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_0, 568]
    },
    {
        "identifier": 'EVENT_2081_pause_82',
        "command": 'pause',
        "args": [45]
    },
    {
        "identifier": 'EVENT_2081_run_dialog_83',
        "command": 'run_dialog',
        "args": [2994, AreaObjects.MARIO, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_2081_pause_84',
        "command": 'pause',
        "args": [30]
    },
    {
        "identifier": 'EVENT_2081_set_action_script_sync_85',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_2, 568]
    },
    {
        "identifier": 'EVENT_2081_pause_86',
        "command": 'pause',
        "args": [45]
    },
    {
        "identifier": 'EVENT_2081_run_dialog_87',
        "command": 'run_dialog',
        "args": [2995, AreaObjects.MARIO, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_2081_pause_88',
        "command": 'pause',
        "args": [30]
    },
    {
        "identifier": 'EVENT_2081_set_action_script_sync_89',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_1, 568]
    },
    {
        "identifier": 'EVENT_2081_pause_90',
        "command": 'pause',
        "args": [45]
    },
    {
        "identifier": 'EVENT_2081_run_dialog_91',
        "command": 'run_dialog',
        "args": [2996, AreaObjects.MARIO, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_2081_pause_92',
        "command": 'pause',
        "args": [30]
    },
    {
        "identifier": 'EVENT_2081_run_dialog_93',
        "command": 'run_dialog',
        "args": [2997, AreaObjects.MARIO, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_2081_set_action_script_sync_94',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_0, 569]
    },
    {
        "identifier": 'EVENT_2081_set_action_script_sync_95',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_1, 569]
    },
    {
        "identifier": 'EVENT_2081_set_action_script_sync_96',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_2, 569]
    },
    {
        "identifier": 'EVENT_2081_pause_97',
        "command": 'pause',
        "args": [60]
    },
    {
        "identifier": 'EVENT_2081_tint_layers_98',
        "command": 'tint_layers',
        "args": [0x00, 0x00, 0x00, 0, [_0x81Flags.LAYER_1, _0x81Flags.LAYER_2, _0x81Flags.NPC_SPRITES, _0x81Flags.MINUS_SUB]]
    },
    {
        "identifier": 'EVENT_2081_reset_priority_set_99',
        "command": 'reset_priority_set'
    },
    {
        "identifier": 'EVENT_2081_fade_out_music_to_volume_100',
        "command": 'fade_out_music_to_volume',
        "args": [0, 100]
    },
    {
        "identifier": 'EVENT_2081_action_queue_sync_101',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_3],
        "subscript": [
            {
                "identifier": 'EVENT_2081_action_queue_sync_101_SUBSCRIPT_set_sprite_sequence_0',
                "command": 'set_sprite_sequence',
                "args": [0, 0, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_2081_action_queue_async_102',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_2081_action_queue_async_102_SUBSCRIPT_play_sound_0',
                "command": 'play_sound',
                "args": [Sounds._030_SURPRISED_MONSTER, 6]
            },
            {
                "identifier": 'EVENT_2081_action_queue_async_102_SUBSCRIPT_set_animation_speed_1',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_2081_action_queue_async_102_SUBSCRIPT_set_sprite_sequence_2',
                "command": 'set_sprite_sequence',
                "args": [14, 0, [_0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_2081_action_queue_async_102_SUBSCRIPT_pause_3',
                "command": 'pause',
                "args": [15]
            },
            {
                "identifier": 'EVENT_2081_action_queue_async_102_SUBSCRIPT_set_animation_speed_4',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.SEQUENCE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_2081_fade_out_music_to_volume_103',
        "command": 'fade_out_music_to_volume',
        "args": [6, 100]
    },
    {
        "identifier": 'EVENT_2081_set_7000_to_tapped_button_104',
        "command": 'set_7000_to_tapped_button'
    },
    {
        "identifier": 'EVENT_2081_pause_105',
        "command": 'pause',
        "args": [1]
    },
    {
        "identifier": 'EVENT_2081_mem_7000_and_const_106',
        "command": 'mem_7000_and_const',
        "args": [0x0080]
    },
    {
        "identifier": 'EVENT_2081_jmp_if_var_equals_short_107',
        "command": 'jmp_if_var_equals_short',
        "args": [0x7000, 128, 'EVENT_2081_apply_tile_mod_109']
    },
    {
        "identifier": 'EVENT_2081_jmp_108',
        "command": 'jmp',
        "args": ['EVENT_2081_set_7000_to_tapped_button_104']
    },
    {
        "identifier": 'EVENT_2081_apply_tile_mod_109',
        "command": 'apply_tile_mod',
        "args": [Rooms._399_MONSTRO_TOWN_3_MUSTY_FEARS_INN, 32, []]
    },
    {
        "identifier": 'EVENT_2081_action_queue_async_110',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_2081_action_queue_async_110_SUBSCRIPT_reset_properties_0',
                "command": 'reset_properties'
            },
            {
                "identifier": 'EVENT_2081_action_queue_async_110_SUBSCRIPT_set_animation_speed_1',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_2081_action_queue_async_110_SUBSCRIPT_jump_to_height_2',
                "command": 'jump_to_height',
                "args": [120]
            },
            {
                "identifier": 'EVENT_2081_action_queue_async_110_SUBSCRIPT_shift_south_pixels_3',
                "command": 'shift_south_pixels',
                "args": [32]
            },
            {
                "identifier": 'EVENT_2081_action_queue_async_110_SUBSCRIPT_set_animation_speed_4',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING, _0x10Flags.SEQUENCE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_2081_pause_111',
        "command": 'pause',
        "args": [1]
    },
    {
        "identifier": 'EVENT_2081_play_sound_112',
        "command": 'play_sound',
        "args": [Sounds._058_INSERT, 6]
    },
    {
        "identifier": 'EVENT_2081_clear_bit_113',
        "command": 'clear_bit',
        "args": [0x7049, 5]
    },
    {
        "identifier": 'EVENT_2081_ret_114',
        "command": 'ret'
    }
]
