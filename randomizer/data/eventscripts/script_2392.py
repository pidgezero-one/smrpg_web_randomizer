from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data import items
script = [
    {
        "identifier": 'EVENT_2392_set_0',
        "command": 'set',
        "args": [0x70ae, 23]
    },
    {
        "identifier": 'EVENT_2392_store_item_amount_7000_1',
        "command": 'store_item_amount_7000',
        "args": [items.Seed]
    },
    {
        "identifier": 'EVENT_2392_jmp_if_var_equals_short_2',
        "command": 'jmp_if_var_equals_short',
        "args": [0x7000, 1, 'EVENT_2392_jmp_if_bit_set_11']
    },
    {
        "identifier": 'EVENT_2392_store_item_amount_7000_3',
        "command": 'store_item_amount_7000',
        "args": [items.Fertilizer]
    },
    {
        "identifier": 'EVENT_2392_jmp_if_var_equals_short_4',
        "command": 'jmp_if_var_equals_short',
        "args": [0x7000, 1, 'EVENT_2392_jmp_if_bit_set_144']
    },
    {
        "identifier": 'EVENT_2392_jmp_if_bit_set_5',
        "command": 'jmp_if_bit_set',
        "args": [0x708e, 7, 'EVENT_2392_run_dialog_9']
    },
    {
        "identifier": 'EVENT_2392_set_bit_6',
        "command": 'set_bit',
        "args": [0x708e, 2]
    },
    {
        "identifier": 'EVENT_2392_run_dialog_7',
        "command": 'run_dialog',
        "args": [3216, AreaObjects.MEM_70A8, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]]
    },
    {
        "identifier": 'EVENT_2392_ret_8',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_2392_run_dialog_9',
        "command": 'run_dialog',
        "args": [3103, AreaObjects.MEM_70A8, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]]
    },
    {
        "identifier": 'EVENT_2392_ret_10',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_2392_jmp_if_bit_set_11',
        "command": 'jmp_if_bit_set',
        "args": [0x708e, 2, 'EVENT_2392_jmp_if_bit_set_14']
    },
    {
        "identifier": 'EVENT_2392_set_bit_12',
        "command": 'set_bit',
        "args": [0x708e, 2]
    },
    {
        "identifier": 'EVENT_2392_run_dialog_13',
        "command": 'run_dialog',
        "args": [3216, AreaObjects.MEM_70A8, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]]
    },
    {
        "identifier": 'EVENT_2392_jmp_if_bit_set_14',
        "command": 'jmp_if_bit_set',
        "args": [0x708e, 3, 'EVENT_2392_run_dialog_40']
    },
    {
        "identifier": 'EVENT_2392_action_queue_sync_15',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_3],
        "subscript": [
            {
                "identifier": 'EVENT_2392_action_queue_sync_15_SUBSCRIPT_jump_to_height_0',
                "command": 'jump_to_height',
                "args": [108]
            },
            {
                "identifier": 'EVENT_2392_action_queue_sync_15_SUBSCRIPT_play_sound_1',
                "command": 'play_sound',
                "args": [Sounds._004_JUMP, 6]
            },
            {
                "identifier": 'EVENT_2392_action_queue_sync_15_SUBSCRIPT_pause_2',
                "command": 'pause',
                "args": [22]
            },
            {
                "identifier": 'EVENT_2392_action_queue_sync_15_SUBSCRIPT_set_animation_speed_3',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.SEQUENCE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_2392_pause_16',
        "command": 'pause',
        "args": [22]
    },
    {
        "identifier": 'EVENT_2392_adjust_music_tempo_17',
        "command": 'adjust_music_tempo',
        "args": [MusicDirections.SPEED_UP, 32, 0]
    },
    {
        "identifier": 'EVENT_2392_pause_18',
        "command": 'pause',
        "args": [2]
    },
    {
        "identifier": 'EVENT_2392_run_dialog_19',
        "command": 'run_dialog',
        "args": [3217, AreaObjects.MEM_70A8, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]]
    },
    {
        "identifier": 'EVENT_2392_freeze_camera_20',
        "command": 'freeze_camera'
    },
    {
        "identifier": 'EVENT_2392_pause_21',
        "command": 'pause',
        "args": [2]
    },
    {
        "identifier": 'EVENT_2392_adjust_music_tempo_22',
        "command": 'adjust_music_tempo',
        "args": [MusicDirections.SLOW_DOWN, 0, 0]
    },
    {
        "identifier": 'EVENT_2392_action_queue_sync_23',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_3],
        "subscript": [
            {
                "identifier": 'EVENT_2392_action_queue_sync_23_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_2392_action_queue_sync_23_SUBSCRIPT_pause_1',
                "command": 'pause',
                "args": [16]
            },
            {
                "identifier": 'EVENT_2392_action_queue_sync_23_SUBSCRIPT_face_southwest_2',
                "command": 'face_southwest'
            }
        ]
    },
    {
        "identifier": 'EVENT_2392_set_action_script_async_24',
        "command": 'set_action_script_async',
        "args": [AreaObjects.MARIO, 855]
    },
    {
        "identifier": 'EVENT_2392_set_action_script_sync_25',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.SCREEN_FOCUS, 391]
    },
    {
        "identifier": 'EVENT_2392_pause_26',
        "command": 'pause',
        "args": [32]
    },
    {
        "identifier": 'EVENT_2392_jmp_if_bit_set_27',
        "command": 'jmp_if_bit_set',
        "args": [0x708e, 4, 'EVENT_2392_run_dialog_30']
    },
    {
        "identifier": 'EVENT_2392_run_dialog_28',
        "command": 'run_dialog',
        "args": [3214, AreaObjects.MEM_70A8, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]]
    },
    {
        "identifier": 'EVENT_2392_jmp_29',
        "command": 'jmp',
        "args": ['EVENT_2392_pause_31']
    },
    {
        "identifier": 'EVENT_2392_run_dialog_30',
        "command": 'run_dialog',
        "args": [3215, AreaObjects.MEM_70A8, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]]
    },
    {
        "identifier": 'EVENT_2392_pause_31',
        "command": 'pause',
        "args": [16]
    },
    {
        "identifier": 'EVENT_2392_set_action_script_async_32',
        "command": 'set_action_script_async',
        "args": [AreaObjects.MARIO, 384]
    },
    {
        "identifier": 'EVENT_2392_set_action_script_async_33',
        "command": 'set_action_script_async',
        "args": [AreaObjects.MARIO, 395]
    },
    {
        "identifier": 'EVENT_2392_pause_34',
        "command": 'pause',
        "args": [16]
    },
    {
        "identifier": 'EVENT_2392_action_queue_async_35',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_2392_action_queue_async_35_SUBSCRIPT_face_northeast_0',
                "command": 'face_northeast'
            }
        ]
    },
    {
        "identifier": 'EVENT_2392_jmp_if_bit_set_36',
        "command": 'jmp_if_bit_set',
        "args": [0x708e, 3, 'EVENT_2392_run_dialog_40']
    },
    {
        "identifier": 'EVENT_2392_set_bit_37',
        "command": 'set_bit',
        "args": [0x708e, 3]
    },
    {
        "identifier": 'EVENT_2392_run_dialog_38',
        "command": 'run_dialog',
        "args": [3219, AreaObjects.MEM_70A8, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]]
    },
    {
        "identifier": 'EVENT_2392_jmp_39',
        "command": 'jmp',
        "args": ['EVENT_2392_jmp_if_dialog_option_b_41']
    },
    {
        "identifier": 'EVENT_2392_run_dialog_40',
        "command": 'run_dialog',
        "args": [3221, AreaObjects.MEM_70A8, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]]
    },
    {
        "identifier": 'EVENT_2392_jmp_if_dialog_option_b_41',
        "command": 'jmp_if_dialog_option_b',
        "args": ['EVENT_2392_pause_93']
    },
    {
        "identifier": 'EVENT_2392_pause_42',
        "command": 'pause',
        "args": [10]
    },
    {
        "identifier": 'EVENT_2392_set_action_script_async_43',
        "command": 'set_action_script_async',
        "args": [AreaObjects.MARIO, 670]
    },
    {
        "identifier": 'EVENT_2392_remove_one_from_inventory_44',
        "command": 'remove_one_from_inventory',
        "args": [items.Seed]
    },
    {
        "identifier": 'EVENT_2392_run_dialog_45',
        "command": 'run_dialog',
        "args": [3223, AreaObjects.MEM_70A8, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]]
    },
    {
        "identifier": 'EVENT_2392_set_bit_46',
        "command": 'set_bit',
        "args": [0x708e, 5]
    },
    {
        "identifier": 'EVENT_2392_jmp_if_bit_set_47',
        "command": 'jmp_if_bit_set',
        "args": [0x708e, 6, 'EVENT_2392_freeze_camera_191']
    },
    {
        "identifier": 'EVENT_2392_store_item_amount_7000_48',
        "command": 'store_item_amount_7000',
        "args": [items.Fertilizer]
    },
    {
        "identifier": 'EVENT_2392_jmp_if_var_equals_short_49',
        "command": 'jmp_if_var_equals_short',
        "args": [0x7000, 1, 'EVENT_2392_jmp_if_bit_set_52']
    },
    {
        "identifier": 'EVENT_2392_unfreeze_camera_50',
        "command": 'unfreeze_camera'
    },
    {
        "identifier": 'EVENT_2392_ret_51',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_2392_jmp_if_bit_set_52',
        "command": 'jmp_if_bit_set',
        "args": [0x708e, 4, 'EVENT_2392_run_dialog_85']
    },
    {
        "identifier": 'EVENT_2392_action_queue_sync_53',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_3],
        "subscript": [
            {
                "identifier": 'EVENT_2392_action_queue_sync_53_SUBSCRIPT_jump_to_height_0',
                "command": 'jump_to_height',
                "args": [108]
            },
            {
                "identifier": 'EVENT_2392_action_queue_sync_53_SUBSCRIPT_play_sound_1',
                "command": 'play_sound',
                "args": [Sounds._004_JUMP, 6]
            },
            {
                "identifier": 'EVENT_2392_action_queue_sync_53_SUBSCRIPT_pause_2',
                "command": 'pause',
                "args": [22]
            },
            {
                "identifier": 'EVENT_2392_action_queue_sync_53_SUBSCRIPT_set_animation_speed_3',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.SEQUENCE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_2392_pause_54',
        "command": 'pause',
        "args": [22]
    },
    {
        "identifier": 'EVENT_2392_adjust_music_tempo_55',
        "command": 'adjust_music_tempo',
        "args": [MusicDirections.SPEED_UP, 32, 0]
    },
    {
        "identifier": 'EVENT_2392_pause_56',
        "command": 'pause',
        "args": [2]
    },
    {
        "identifier": 'EVENT_2392_run_dialog_57',
        "command": 'run_dialog',
        "args": [3218, AreaObjects.MEM_70A8, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]]
    },
    {
        "identifier": 'EVENT_2392_freeze_camera_58',
        "command": 'freeze_camera'
    },
    {
        "identifier": 'EVENT_2392_pause_59',
        "command": 'pause',
        "args": [2]
    },
    {
        "identifier": 'EVENT_2392_adjust_music_tempo_60',
        "command": 'adjust_music_tempo',
        "args": [MusicDirections.SLOW_DOWN, 0, 0]
    },
    {
        "identifier": 'EVENT_2392_action_queue_sync_61',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_3],
        "subscript": [
            {
                "identifier": 'EVENT_2392_action_queue_sync_61_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_2392_action_queue_sync_61_SUBSCRIPT_pause_1',
                "command": 'pause',
                "args": [16]
            },
            {
                "identifier": 'EVENT_2392_action_queue_sync_61_SUBSCRIPT_face_southwest_2',
                "command": 'face_southwest'
            }
        ]
    },
    {
        "identifier": 'EVENT_2392_set_action_script_async_62',
        "command": 'set_action_script_async',
        "args": [AreaObjects.MARIO, 855]
    },
    {
        "identifier": 'EVENT_2392_set_action_script_sync_63',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.SCREEN_FOCUS, 391]
    },
    {
        "identifier": 'EVENT_2392_pause_64',
        "command": 'pause',
        "args": [32]
    },
    {
        "identifier": 'EVENT_2392_run_dialog_65',
        "command": 'run_dialog',
        "args": [3215, AreaObjects.MEM_70A8, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]]
    },
    {
        "identifier": 'EVENT_2392_pause_66',
        "command": 'pause',
        "args": [16]
    },
    {
        "identifier": 'EVENT_2392_set_action_script_async_67',
        "command": 'set_action_script_async',
        "args": [AreaObjects.MARIO, 384]
    },
    {
        "identifier": 'EVENT_2392_set_action_script_async_68',
        "command": 'set_action_script_async',
        "args": [AreaObjects.MARIO, 395]
    },
    {
        "identifier": 'EVENT_2392_pause_69',
        "command": 'pause',
        "args": [16]
    },
    {
        "identifier": 'EVENT_2392_action_queue_async_70',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_2392_action_queue_async_70_SUBSCRIPT_face_northeast_0',
                "command": 'face_northeast'
            }
        ]
    },
    {
        "identifier": 'EVENT_2392_set_bit_71',
        "command": 'set_bit',
        "args": [0x708e, 4]
    },
    {
        "identifier": 'EVENT_2392_run_dialog_72',
        "command": 'run_dialog',
        "args": [3220, AreaObjects.MEM_70A8, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]]
    },
    {
        "identifier": 'EVENT_2392_jmp_if_dialog_option_b_73',
        "command": 'jmp_if_dialog_option_b',
        "args": ['EVENT_2392_pause_80']
    },
    {
        "identifier": 'EVENT_2392_pause_74',
        "command": 'pause',
        "args": [10]
    },
    {
        "identifier": 'EVENT_2392_set_action_script_async_75',
        "command": 'set_action_script_async',
        "args": [AreaObjects.MARIO, 670]
    },
    {
        "identifier": 'EVENT_2392_remove_one_from_inventory_76',
        "command": 'remove_one_from_inventory',
        "args": [items.Fertilizer]
    },
    {
        "identifier": 'EVENT_2392_set_bit_77',
        "command": 'set_bit',
        "args": [0x708e, 6]
    },
    {
        "identifier": 'EVENT_2392_jmp_if_bit_set_78',
        "command": 'jmp_if_bit_set',
        "args": [0x708e, 5, 'EVENT_2392_freeze_camera_191']
    },
    {
        "identifier": 'EVENT_2392_jmp_79',
        "command": 'jmp',
        "args": ['EVENT_2392_freeze_camera_191']
    },
    {
        "identifier": 'EVENT_2392_pause_80',
        "command": 'pause',
        "args": [10]
    },
    {
        "identifier": 'EVENT_2392_set_action_script_async_81',
        "command": 'set_action_script_async',
        "args": [AreaObjects.MARIO, 671]
    },
    {
        "identifier": 'EVENT_2392_run_dialog_82',
        "command": 'run_dialog',
        "args": [3225, AreaObjects.MEM_70A8, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]]
    },
    {
        "identifier": 'EVENT_2392_unfreeze_camera_83',
        "command": 'unfreeze_camera'
    },
    {
        "identifier": 'EVENT_2392_ret_84',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_2392_run_dialog_85',
        "command": 'run_dialog',
        "args": [3224, AreaObjects.MEM_70A8, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]]
    },
    {
        "identifier": 'EVENT_2392_jmp_if_dialog_option_b_86',
        "command": 'jmp_if_dialog_option_b',
        "args": ['EVENT_2392_pause_80']
    },
    {
        "identifier": 'EVENT_2392_pause_87',
        "command": 'pause',
        "args": [10]
    },
    {
        "identifier": 'EVENT_2392_set_action_script_async_88',
        "command": 'set_action_script_async',
        "args": [AreaObjects.MARIO, 670]
    },
    {
        "identifier": 'EVENT_2392_remove_one_from_inventory_89',
        "command": 'remove_one_from_inventory',
        "args": [items.Fertilizer]
    },
    {
        "identifier": 'EVENT_2392_set_bit_90',
        "command": 'set_bit',
        "args": [0x708e, 6]
    },
    {
        "identifier": 'EVENT_2392_jmp_if_bit_set_91',
        "command": 'jmp_if_bit_set',
        "args": [0x708e, 5, 'EVENT_2392_freeze_camera_191']
    },
    {
        "identifier": 'EVENT_2392_jmp_92',
        "command": 'jmp',
        "args": ['EVENT_2392_freeze_camera_191']
    },
    {
        "identifier": 'EVENT_2392_pause_93',
        "command": 'pause',
        "args": [10]
    },
    {
        "identifier": 'EVENT_2392_set_action_script_async_94',
        "command": 'set_action_script_async',
        "args": [AreaObjects.MARIO, 671]
    },
    {
        "identifier": 'EVENT_2392_run_dialog_95',
        "command": 'run_dialog',
        "args": [3230, AreaObjects.MEM_70A8, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]]
    },
    {
        "identifier": 'EVENT_2392_store_item_amount_7000_96',
        "command": 'store_item_amount_7000',
        "args": [items.Fertilizer]
    },
    {
        "identifier": 'EVENT_2392_jmp_if_var_equals_short_97',
        "command": 'jmp_if_var_equals_short',
        "args": [0x7000, 1, 'EVENT_2392_jmp_if_bit_set_101']
    },
    {
        "identifier": 'EVENT_2392_run_dialog_98',
        "command": 'run_dialog',
        "args": [3225, AreaObjects.MEM_70A8, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]]
    },
    {
        "identifier": 'EVENT_2392_unfreeze_camera_99',
        "command": 'unfreeze_camera'
    },
    {
        "identifier": 'EVENT_2392_ret_100',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_2392_jmp_if_bit_set_101',
        "command": 'jmp_if_bit_set',
        "args": [0x708e, 4, 'EVENT_2392_jmp_if_bit_set_131']
    },
    {
        "identifier": 'EVENT_2392_action_queue_sync_102',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_3],
        "subscript": [
            {
                "identifier": 'EVENT_2392_action_queue_sync_102_SUBSCRIPT_jump_to_height_0',
                "command": 'jump_to_height',
                "args": [108]
            },
            {
                "identifier": 'EVENT_2392_action_queue_sync_102_SUBSCRIPT_play_sound_1',
                "command": 'play_sound',
                "args": [Sounds._004_JUMP, 6]
            },
            {
                "identifier": 'EVENT_2392_action_queue_sync_102_SUBSCRIPT_pause_2',
                "command": 'pause',
                "args": [22]
            },
            {
                "identifier": 'EVENT_2392_action_queue_sync_102_SUBSCRIPT_set_animation_speed_3',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.SEQUENCE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_2392_pause_103',
        "command": 'pause',
        "args": [22]
    },
    {
        "identifier": 'EVENT_2392_adjust_music_tempo_104',
        "command": 'adjust_music_tempo',
        "args": [MusicDirections.SPEED_UP, 32, 0]
    },
    {
        "identifier": 'EVENT_2392_pause_105',
        "command": 'pause',
        "args": [2]
    },
    {
        "identifier": 'EVENT_2392_run_dialog_106',
        "command": 'run_dialog',
        "args": [3218, AreaObjects.MEM_70A8, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]]
    },
    {
        "identifier": 'EVENT_2392_freeze_camera_107',
        "command": 'freeze_camera'
    },
    {
        "identifier": 'EVENT_2392_pause_108',
        "command": 'pause',
        "args": [2]
    },
    {
        "identifier": 'EVENT_2392_adjust_music_tempo_109',
        "command": 'adjust_music_tempo',
        "args": [MusicDirections.SLOW_DOWN, 0, 0]
    },
    {
        "identifier": 'EVENT_2392_action_queue_sync_110',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_3],
        "subscript": [
            {
                "identifier": 'EVENT_2392_action_queue_sync_110_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_2392_action_queue_sync_110_SUBSCRIPT_pause_1',
                "command": 'pause',
                "args": [16]
            },
            {
                "identifier": 'EVENT_2392_action_queue_sync_110_SUBSCRIPT_face_southwest_2',
                "command": 'face_southwest'
            }
        ]
    },
    {
        "identifier": 'EVENT_2392_set_action_script_async_111',
        "command": 'set_action_script_async',
        "args": [AreaObjects.MARIO, 855]
    },
    {
        "identifier": 'EVENT_2392_set_action_script_sync_112',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.SCREEN_FOCUS, 391]
    },
    {
        "identifier": 'EVENT_2392_pause_113',
        "command": 'pause',
        "args": [32]
    },
    {
        "identifier": 'EVENT_2392_run_dialog_114',
        "command": 'run_dialog',
        "args": [3215, AreaObjects.MEM_70A8, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]]
    },
    {
        "identifier": 'EVENT_2392_pause_115',
        "command": 'pause',
        "args": [16]
    },
    {
        "identifier": 'EVENT_2392_set_action_script_async_116',
        "command": 'set_action_script_async',
        "args": [AreaObjects.MARIO, 384]
    },
    {
        "identifier": 'EVENT_2392_set_action_script_async_117',
        "command": 'set_action_script_async',
        "args": [AreaObjects.MARIO, 395]
    },
    {
        "identifier": 'EVENT_2392_pause_118',
        "command": 'pause',
        "args": [16]
    },
    {
        "identifier": 'EVENT_2392_action_queue_async_119',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_2392_action_queue_async_119_SUBSCRIPT_face_northeast_0',
                "command": 'face_northeast'
            }
        ]
    },
    {
        "identifier": 'EVENT_2392_set_bit_120',
        "command": 'set_bit',
        "args": [0x708e, 4]
    },
    {
        "identifier": 'EVENT_2392_run_dialog_121',
        "command": 'run_dialog',
        "args": [3220, AreaObjects.MEM_70A8, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]]
    },
    {
        "identifier": 'EVENT_2392_jmp_if_dialog_option_b_122',
        "command": 'jmp_if_dialog_option_b',
        "args": ['EVENT_2392_pause_80']
    },
    {
        "identifier": 'EVENT_2392_pause_123',
        "command": 'pause',
        "args": [10]
    },
    {
        "identifier": 'EVENT_2392_set_action_script_async_124',
        "command": 'set_action_script_async',
        "args": [AreaObjects.MARIO, 670]
    },
    {
        "identifier": 'EVENT_2392_remove_one_from_inventory_125',
        "command": 'remove_one_from_inventory',
        "args": [items.Fertilizer]
    },
    {
        "identifier": 'EVENT_2392_set_bit_126',
        "command": 'set_bit',
        "args": [0x708e, 6]
    },
    {
        "identifier": 'EVENT_2392_jmp_if_bit_set_127',
        "command": 'jmp_if_bit_set',
        "args": [0x708e, 5, 'EVENT_2392_freeze_camera_191']
    },
    {
        "identifier": 'EVENT_2392_run_dialog_128',
        "command": 'run_dialog',
        "args": [3227, AreaObjects.MEM_70A8, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]]
    },
    {
        "identifier": 'EVENT_2392_unfreeze_camera_129',
        "command": 'unfreeze_camera'
    },
    {
        "identifier": 'EVENT_2392_ret_130',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_2392_jmp_if_bit_set_131',
        "command": 'jmp_if_bit_set',
        "args": [0x708e, 5, 'EVENT_2392_run_dialog_134']
    },
    {
        "identifier": 'EVENT_2392_run_dialog_132',
        "command": 'run_dialog',
        "args": [3224, AreaObjects.MEM_70A8, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]]
    },
    {
        "identifier": 'EVENT_2392_jmp_133',
        "command": 'jmp',
        "args": ['EVENT_2392_jmp_if_dialog_option_b_135']
    },
    {
        "identifier": 'EVENT_2392_run_dialog_134',
        "command": 'run_dialog',
        "args": [3229, AreaObjects.MEM_70A8, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]]
    },
    {
        "identifier": 'EVENT_2392_jmp_if_dialog_option_b_135',
        "command": 'jmp_if_dialog_option_b',
        "args": ['EVENT_2392_pause_80']
    },
    {
        "identifier": 'EVENT_2392_pause_136',
        "command": 'pause',
        "args": [10]
    },
    {
        "identifier": 'EVENT_2392_set_action_script_async_137',
        "command": 'set_action_script_async',
        "args": [AreaObjects.MARIO, 670]
    },
    {
        "identifier": 'EVENT_2392_remove_one_from_inventory_138',
        "command": 'remove_one_from_inventory',
        "args": [items.Fertilizer]
    },
    {
        "identifier": 'EVENT_2392_set_bit_139',
        "command": 'set_bit',
        "args": [0x708e, 6]
    },
    {
        "identifier": 'EVENT_2392_jmp_if_bit_set_140',
        "command": 'jmp_if_bit_set',
        "args": [0x708e, 5, 'EVENT_2392_freeze_camera_191']
    },
    {
        "identifier": 'EVENT_2392_run_dialog_141',
        "command": 'run_dialog',
        "args": [3227, AreaObjects.MEM_70A8, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]]
    },
    {
        "identifier": 'EVENT_2392_unfreeze_camera_142',
        "command": 'unfreeze_camera'
    },
    {
        "identifier": 'EVENT_2392_ret_143',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_2392_jmp_if_bit_set_144',
        "command": 'jmp_if_bit_set',
        "args": [0x708e, 4, 'EVENT_2392_run_dialog_183']
    },
    {
        "identifier": 'EVENT_2392_jmp_if_bit_set_145',
        "command": 'jmp_if_bit_set',
        "args": [0x708e, 2, 'EVENT_2392_action_queue_sync_148']
    },
    {
        "identifier": 'EVENT_2392_set_bit_146',
        "command": 'set_bit',
        "args": [0x708e, 2]
    },
    {
        "identifier": 'EVENT_2392_run_dialog_147',
        "command": 'run_dialog',
        "args": [3216, AreaObjects.MEM_70A8, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]]
    },
    {
        "identifier": 'EVENT_2392_action_queue_sync_148',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_3],
        "subscript": [
            {
                "identifier": 'EVENT_2392_action_queue_sync_148_SUBSCRIPT_jump_to_height_0',
                "command": 'jump_to_height',
                "args": [108]
            },
            {
                "identifier": 'EVENT_2392_action_queue_sync_148_SUBSCRIPT_play_sound_1',
                "command": 'play_sound',
                "args": [Sounds._004_JUMP, 6]
            },
            {
                "identifier": 'EVENT_2392_action_queue_sync_148_SUBSCRIPT_pause_2',
                "command": 'pause',
                "args": [22]
            },
            {
                "identifier": 'EVENT_2392_action_queue_sync_148_SUBSCRIPT_set_animation_speed_3',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.SEQUENCE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_2392_pause_149',
        "command": 'pause',
        "args": [24]
    },
    {
        "identifier": 'EVENT_2392_adjust_music_tempo_150',
        "command": 'adjust_music_tempo',
        "args": [MusicDirections.SPEED_UP, 32, 0]
    },
    {
        "identifier": 'EVENT_2392_pause_151',
        "command": 'pause',
        "args": [2]
    },
    {
        "identifier": 'EVENT_2392_run_dialog_152',
        "command": 'run_dialog',
        "args": [3218, AreaObjects.MEM_70A8, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]]
    },
    {
        "identifier": 'EVENT_2392_freeze_camera_153',
        "command": 'freeze_camera'
    },
    {
        "identifier": 'EVENT_2392_pause_154',
        "command": 'pause',
        "args": [2]
    },
    {
        "identifier": 'EVENT_2392_adjust_music_tempo_155',
        "command": 'adjust_music_tempo',
        "args": [MusicDirections.SLOW_DOWN, 0, 0]
    },
    {
        "identifier": 'EVENT_2392_action_queue_sync_156',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_3],
        "subscript": [
            {
                "identifier": 'EVENT_2392_action_queue_sync_156_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_2392_action_queue_sync_156_SUBSCRIPT_pause_1',
                "command": 'pause',
                "args": [16]
            },
            {
                "identifier": 'EVENT_2392_action_queue_sync_156_SUBSCRIPT_face_southwest_2',
                "command": 'face_southwest'
            }
        ]
    },
    {
        "identifier": 'EVENT_2392_set_action_script_async_157',
        "command": 'set_action_script_async',
        "args": [AreaObjects.MARIO, 855]
    },
    {
        "identifier": 'EVENT_2392_set_action_script_sync_158',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.SCREEN_FOCUS, 391]
    },
    {
        "identifier": 'EVENT_2392_pause_159',
        "command": 'pause',
        "args": [32]
    },
    {
        "identifier": 'EVENT_2392_jmp_if_bit_set_160',
        "command": 'jmp_if_bit_set',
        "args": [0x708e, 3, 'EVENT_2392_run_dialog_163']
    },
    {
        "identifier": 'EVENT_2392_run_dialog_161',
        "command": 'run_dialog',
        "args": [3214, AreaObjects.MEM_70A8, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]]
    },
    {
        "identifier": 'EVENT_2392_jmp_162',
        "command": 'jmp',
        "args": ['EVENT_2392_pause_164']
    },
    {
        "identifier": 'EVENT_2392_run_dialog_163',
        "command": 'run_dialog',
        "args": [3215, AreaObjects.MEM_70A8, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]]
    },
    {
        "identifier": 'EVENT_2392_pause_164',
        "command": 'pause',
        "args": [16]
    },
    {
        "identifier": 'EVENT_2392_set_action_script_async_165',
        "command": 'set_action_script_async',
        "args": [AreaObjects.MARIO, 384]
    },
    {
        "identifier": 'EVENT_2392_set_action_script_async_166',
        "command": 'set_action_script_async',
        "args": [AreaObjects.MARIO, 395]
    },
    {
        "identifier": 'EVENT_2392_pause_167',
        "command": 'pause',
        "args": [16]
    },
    {
        "identifier": 'EVENT_2392_action_queue_async_168',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_2392_action_queue_async_168_SUBSCRIPT_face_northeast_0',
                "command": 'face_northeast'
            }
        ]
    },
    {
        "identifier": 'EVENT_2392_jmp_if_bit_set_169',
        "command": 'jmp_if_bit_set',
        "args": [0x708e, 4, 'EVENT_2392_run_dialog_173']
    },
    {
        "identifier": 'EVENT_2392_set_bit_170',
        "command": 'set_bit',
        "args": [0x708e, 4]
    },
    {
        "identifier": 'EVENT_2392_run_dialog_171',
        "command": 'run_dialog',
        "args": [3220, AreaObjects.MEM_70A8, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]]
    },
    {
        "identifier": 'EVENT_2392_jmp_172',
        "command": 'jmp',
        "args": ['EVENT_2392_jmp_if_dialog_option_b_174']
    },
    {
        "identifier": 'EVENT_2392_run_dialog_173',
        "command": 'run_dialog',
        "args": [3222, AreaObjects.MEM_70A8, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]]
    },
    {
        "identifier": 'EVENT_2392_jmp_if_dialog_option_b_174',
        "command": 'jmp_if_dialog_option_b',
        "args": ['EVENT_2392_pause_80']
    },
    {
        "identifier": 'EVENT_2392_pause_175',
        "command": 'pause',
        "args": [10]
    },
    {
        "identifier": 'EVENT_2392_set_action_script_async_176',
        "command": 'set_action_script_async',
        "args": [AreaObjects.MARIO, 670]
    },
    {
        "identifier": 'EVENT_2392_remove_one_from_inventory_177',
        "command": 'remove_one_from_inventory',
        "args": [items.Fertilizer]
    },
    {
        "identifier": 'EVENT_2392_set_bit_178',
        "command": 'set_bit',
        "args": [0x708e, 6]
    },
    {
        "identifier": 'EVENT_2392_jmp_if_bit_set_179',
        "command": 'jmp_if_bit_set',
        "args": [0x708e, 5, 'EVENT_2392_freeze_camera_191']
    },
    {
        "identifier": 'EVENT_2392_run_dialog_180',
        "command": 'run_dialog',
        "args": [3228, AreaObjects.MEM_70A8, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]]
    },
    {
        "identifier": 'EVENT_2392_unfreeze_camera_181',
        "command": 'unfreeze_camera'
    },
    {
        "identifier": 'EVENT_2392_ret_182',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_2392_run_dialog_183',
        "command": 'run_dialog',
        "args": [3222, AreaObjects.MEM_70A8, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]]
    },
    {
        "identifier": 'EVENT_2392_jmp_if_dialog_option_b_184',
        "command": 'jmp_if_dialog_option_b',
        "args": ['EVENT_2392_pause_80']
    },
    {
        "identifier": 'EVENT_2392_remove_one_from_inventory_185',
        "command": 'remove_one_from_inventory',
        "args": [items.Fertilizer]
    },
    {
        "identifier": 'EVENT_2392_set_bit_186',
        "command": 'set_bit',
        "args": [0x708e, 6]
    },
    {
        "identifier": 'EVENT_2392_jmp_if_bit_set_187',
        "command": 'jmp_if_bit_set',
        "args": [0x708e, 5, 'EVENT_2392_freeze_camera_191']
    },
    {
        "identifier": 'EVENT_2392_run_dialog_188',
        "command": 'run_dialog',
        "args": [3228, AreaObjects.MEM_70A8, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]]
    },
    {
        "identifier": 'EVENT_2392_unfreeze_camera_189',
        "command": 'unfreeze_camera'
    },
    {
        "identifier": 'EVENT_2392_ret_190',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_2392_freeze_camera_191',
        "command": 'freeze_camera'
    },
    {
        "identifier": 'EVENT_2392_run_dialog_192',
        "command": 'run_dialog',
        "args": [3226, AreaObjects.MEM_70A8, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]]
    },
    {
        "identifier": 'EVENT_2392_set_bit_193',
        "command": 'set_bit',
        "args": [0x708e, 7]
    },
    {
        "identifier": 'EVENT_2392_summon_to_level_194',
        "command": 'summon_to_level',
        "args": [AreaObjects.NPC_0, Rooms._417_GARDENERS_HOUSE_OUTSIDE]
    },
    {
        "identifier": 'EVENT_2392_summon_to_level_195',
        "command": 'summon_to_level',
        "args": [AreaObjects.NPC_1, Rooms._417_GARDENERS_HOUSE_OUTSIDE]
    },
    {
        "identifier": 'EVENT_2392_summon_to_level_196',
        "command": 'summon_to_level',
        "args": [AreaObjects.NPC_0, Rooms._418_GARDENERS_HOUSE]
    },
    {
        "identifier": 'EVENT_2392_summon_to_level_197',
        "command": 'summon_to_level',
        "args": [AreaObjects.NPC_1, Rooms._418_GARDENERS_HOUSE]
    },
    {
        "identifier": 'EVENT_2392_action_queue_async_198',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_3],
        "subscript": [
            {
                "identifier": 'EVENT_2392_action_queue_async_198_SUBSCRIPT_shift_southeast_steps_0',
                "command": 'shift_southeast_steps',
                "args": [2]
            },
            {
                "identifier": 'EVENT_2392_action_queue_async_198_SUBSCRIPT_face_northeast_1',
                "command": 'face_northeast'
            },
            {
                "identifier": 'EVENT_2392_action_queue_async_198_SUBSCRIPT_pause_2',
                "command": 'pause',
                "args": [16]
            },
            {
                "identifier": 'EVENT_2392_action_queue_async_198_SUBSCRIPT_set_sprite_sequence_3',
                "command": 'set_sprite_sequence',
                "args": [1, inc_sprite=0, flags=[_0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_2392_action_queue_async_198_SUBSCRIPT_shift_southwest_pixels_4',
                "command": 'shift_southwest_pixels',
                "args": [10]
            },
            {
                "identifier": 'EVENT_2392_action_queue_async_198_SUBSCRIPT_face_northeast_5',
                "command": 'face_northeast'
            },
            {
                "identifier": 'EVENT_2392_action_queue_async_198_SUBSCRIPT_reset_properties_6',
                "command": 'reset_properties'
            },
            {
                "identifier": 'EVENT_2392_action_queue_async_198_SUBSCRIPT_sequence_looping_off_7',
                "command": 'sequence_looping_off'
            },
            {
                "identifier": 'EVENT_2392_action_queue_async_198_SUBSCRIPT_pause_8',
                "command": 'pause',
                "args": [32]
            },
            {
                "identifier": 'EVENT_2392_action_queue_async_198_SUBSCRIPT_set_vram_priority_9',
                "command": 'set_vram_priority',
                "args": [VramPriority.OBJECT_OVERLAPS_MARIO_ON_ALL_SIDES]
            },
            {
                "identifier": 'EVENT_2392_action_queue_async_198_SUBSCRIPT_overwrite_solidity_10',
                "command": 'overwrite_solidity',
                "args": [[]]
            },
            {
                "identifier": 'EVENT_2392_action_queue_async_198_SUBSCRIPT_sequence_looping_on_11',
                "command": 'sequence_looping_on'
            },
            {
                "identifier": 'EVENT_2392_action_queue_async_198_SUBSCRIPT_play_sound_12',
                "command": 'play_sound',
                "args": [Sounds._004_JUMP, 4]
            },
            {
                "identifier": 'EVENT_2392_action_queue_async_198_SUBSCRIPT_db_13',
                "command": 'db',
                "args": [0x20, 0x07]
            },
            {
                "identifier": 'EVENT_2392_action_queue_async_198_SUBSCRIPT_db_14',
                "command": 'db',
                "args": [0x24, 0x20, 0x01, 0xa0, 0xff]
            },
            {
                "identifier": 'EVENT_2392_action_queue_async_198_SUBSCRIPT_db_15',
                "command": 'db',
                "args": [0x25, 0xc0, 0x06, 0x80, 0xff]
            },
            {
                "identifier": 'EVENT_2392_action_queue_async_198_SUBSCRIPT_pause_16',
                "command": 'pause',
                "args": [25]
            },
            {
                "identifier": 'EVENT_2392_action_queue_async_198_SUBSCRIPT_bpl_26_27_28_17',
                "command": 'bpl_26_27_28'
            },
            {
                "identifier": 'EVENT_2392_action_queue_async_198_SUBSCRIPT_pause_18',
                "command": 'pause',
                "args": [10]
            },
            {
                "identifier": 'EVENT_2392_action_queue_async_198_SUBSCRIPT_sequence_looping_off_19',
                "command": 'sequence_looping_off'
            },
            {
                "identifier": 'EVENT_2392_action_queue_async_198_SUBSCRIPT_pause_20',
                "command": 'pause',
                "args": [48]
            },
            {
                "identifier": 'EVENT_2392_action_queue_async_198_SUBSCRIPT_play_sound_21',
                "command": 'play_sound',
                "args": [Sounds._024_TAPPING_FEET, 4]
            },
            {
                "identifier": 'EVENT_2392_action_queue_async_198_SUBSCRIPT_set_animation_speed_22',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FASTER, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_2392_action_queue_async_198_SUBSCRIPT_sequence_looping_on_23',
                "command": 'sequence_looping_on'
            },
            {
                "identifier": 'EVENT_2392_action_queue_async_198_SUBSCRIPT_pause_24',
                "command": 'pause',
                "args": [64]
            },
            {
                "identifier": 'EVENT_2392_action_queue_async_198_SUBSCRIPT_sequence_looping_off_25',
                "command": 'sequence_looping_off'
            },
            {
                "identifier": 'EVENT_2392_action_queue_async_198_SUBSCRIPT_set_animation_speed_26',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_2392_action_queue_async_198_SUBSCRIPT_play_sound_27',
                "command": 'play_sound',
                "args": [Sounds._000_SILENCE, 4]
            }
        ]
    },
    {
        "identifier": 'EVENT_2392_run_dialog_199',
        "command": 'run_dialog',
        "args": [3075, AreaObjects.MEM_70A8, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]]
    },
    {
        "identifier": 'EVENT_2392_action_queue_sync_200',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_2392_action_queue_sync_200_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_2392_action_queue_sync_200_SUBSCRIPT_walk_to_xy_coords_1',
                "command": 'walk_to_xy_coords',
                "args": [25, 14]
            },
            {
                "identifier": 'EVENT_2392_action_queue_sync_200_SUBSCRIPT_face_southeast_2',
                "command": 'face_southeast'
            }
        ]
    },
    {
        "identifier": 'EVENT_2392_pause_201',
        "command": 'pause',
        "args": [16]
    },
    {
        "identifier": 'EVENT_2392_action_queue_async_202',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_3],
        "subscript": [
            {
                "identifier": 'EVENT_2392_action_queue_async_202_SUBSCRIPT_play_sound_0',
                "command": 'play_sound',
                "args": [Sounds._024_TAPPING_FEET, 4]
            },
            {
                "identifier": 'EVENT_2392_action_queue_async_202_SUBSCRIPT_set_animation_speed_1',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FASTER, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_2392_action_queue_async_202_SUBSCRIPT_sequence_looping_on_2',
                "command": 'sequence_looping_on'
            },
            {
                "identifier": 'EVENT_2392_action_queue_async_202_SUBSCRIPT_pause_3',
                "command": 'pause',
                "args": [64]
            },
            {
                "identifier": 'EVENT_2392_action_queue_async_202_SUBSCRIPT_sequence_looping_off_4',
                "command": 'sequence_looping_off'
            },
            {
                "identifier": 'EVENT_2392_action_queue_async_202_SUBSCRIPT_set_animation_speed_5',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_2392_action_queue_async_202_SUBSCRIPT_play_sound_6',
                "command": 'play_sound',
                "args": [Sounds._000_SILENCE, 4]
            }
        ]
    },
    {
        "identifier": 'EVENT_2392_run_dialog_203',
        "command": 'run_dialog',
        "args": [3076, AreaObjects.MEM_70A8, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]]
    },
    {
        "identifier": 'EVENT_2392_pause_204',
        "command": 'pause',
        "args": [16]
    },
    {
        "identifier": 'EVENT_2392_action_queue_async_205',
        "command": 'action_queue_async',
        "args": [AreaObjects.SCREEN_FOCUS],
        "subscript": [
            {
                "identifier": 'EVENT_2392_action_queue_async_205_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.SLOW, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_2392_action_queue_async_205_SUBSCRIPT_walk_to_xy_coords_1',
                "command": 'walk_to_xy_coords',
                "args": [22, 0]
            }
        ]
    },
    {
        "identifier": 'EVENT_2392_pause_206',
        "command": 'pause',
        "args": [96]
    },
    {
        "identifier": 'EVENT_2392_run_dialog_207',
        "command": 'run_dialog',
        "args": [3085, AreaObjects.MEM_70A8, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]]
    },
    {
        "identifier": 'EVENT_2392_pause_208',
        "command": 'pause',
        "args": [32]
    },
    {
        "identifier": 'EVENT_2392_play_sound_209',
        "command": 'play_sound',
        "args": [Sounds._127_LIGHT_RATTLE, 6]
    },
    {
        "identifier": 'EVENT_2392_action_queue_async_210',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_0],
        "subscript": [
            {
                "identifier": 'EVENT_2392_action_queue_async_210_SUBSCRIPT_set_sprite_sequence_0',
                "command": 'set_sprite_sequence',
                "args": [0, inc_sprite=0, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_2392_action_queue_async_210_SUBSCRIPT_visibility_on_1',
                "command": 'visibility_on'
            }
        ]
    },
    {
        "identifier": 'EVENT_2392_action_queue_sync_211',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_2392_action_queue_sync_211_SUBSCRIPT_set_sprite_sequence_0',
                "command": 'set_sprite_sequence',
                "args": [0, inc_sprite=3, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_2392_action_queue_async_212',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_3],
        "subscript": [
            {
                "identifier": 'EVENT_2392_action_queue_async_212_SUBSCRIPT_db_0',
                "command": 'db',
                "args": [0x20, 0x07]
            },
            {
                "identifier": 'EVENT_2392_action_queue_async_212_SUBSCRIPT_db_1',
                "command": 'db',
                "args": [0x24, 0xe0, 0xfe, 0x60, 0x00]
            },
            {
                "identifier": 'EVENT_2392_action_queue_async_212_SUBSCRIPT_db_2',
                "command": 'db',
                "args": [0x25, 0xc0, 0x06, 0x80, 0xff]
            },
            {
                "identifier": 'EVENT_2392_action_queue_async_212_SUBSCRIPT_pause_3',
                "command": 'pause',
                "args": [32]
            },
            {
                "identifier": 'EVENT_2392_action_queue_async_212_SUBSCRIPT_bpl_26_27_28_4',
                "command": 'bpl_26_27_28'
            }
        ]
    },
    {
        "identifier": 'EVENT_2392_set_action_script_async_213',
        "command": 'set_action_script_async',
        "args": [AreaObjects.NPC_3, 395]
    },
    {
        "identifier": 'EVENT_2392_pause_214',
        "command": 'pause',
        "args": [24]
    },
    {
        "identifier": 'EVENT_2392_set_action_script_async_215',
        "command": 'set_action_script_async',
        "args": [AreaObjects.MARIO, 395]
    },
    {
        "identifier": 'EVENT_2392_pause_216',
        "command": 'pause',
        "args": [32]
    },
    {
        "identifier": 'EVENT_2392_action_queue_sync_217',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_2392_action_queue_sync_217_SUBSCRIPT_set_sprite_sequence_0',
                "command": 'set_sprite_sequence',
                "args": [0, inc_sprite=3, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_2392_play_sound_218',
        "command": 'play_sound',
        "args": [Sounds._128_FLOATING_HOVERING, 6]
    },
    {
        "identifier": 'EVENT_2392_action_queue_sync_219',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_0],
        "subscript": [
            {
                "identifier": 'EVENT_2392_action_queue_sync_219_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_2392_action_queue_sync_219_SUBSCRIPT_set_sprite_sequence_1',
                "command": 'set_sprite_sequence',
                "args": [0, inc_sprite=0, flags=[_0x08Flags.LOOPING_OFF]]
            },
            {
                "identifier": 'EVENT_2392_action_queue_sync_219_SUBSCRIPT_pause_2',
                "command": 'pause',
                "args": [64]
            },
            {
                "identifier": 'EVENT_2392_action_queue_sync_219_SUBSCRIPT_set_sprite_sequence_3',
                "command": 'set_sprite_sequence',
                "args": [14, inc_sprite=0, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_2392_pause_220',
        "command": 'pause',
        "args": [40]
    },
    {
        "identifier": 'EVENT_2392_summon_to_current_level_221',
        "command": 'summon_to_current_level',
        "args": [AreaObjects.NPC_1]
    },
    {
        "identifier": 'EVENT_2392_action_queue_async_222',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_1],
        "subscript": [
            {
                "identifier": 'EVENT_2392_action_queue_async_222_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_2392_action_queue_async_222_SUBSCRIPT_set_sprite_sequence_1',
                "command": 'set_sprite_sequence',
                "args": [0, inc_sprite=0, flags=[_0x08Flags.LOOPING_OFF]]
            },
            {
                "identifier": 'EVENT_2392_action_queue_async_222_SUBSCRIPT_pause_2',
                "command": 'pause',
                "args": [64]
            },
            {
                "identifier": 'EVENT_2392_action_queue_async_222_SUBSCRIPT_set_sprite_sequence_3',
                "command": 'set_sprite_sequence',
                "args": [14, inc_sprite=0, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_2392_play_sound_223',
        "command": 'play_sound',
        "args": [Sounds._000_SILENCE, 6]
    },
    {
        "identifier": 'EVENT_2392_pause_224',
        "command": 'pause',
        "args": [48]
    },
    {
        "identifier": 'EVENT_2392_run_dialog_225',
        "command": 'run_dialog',
        "args": [3098, AreaObjects.NPC_14, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_2392_pause_226',
        "command": 'pause',
        "args": [16]
    },
    {
        "identifier": 'EVENT_2392_set_action_script_async_227',
        "command": 'set_action_script_async',
        "args": [AreaObjects.MARIO, 395]
    },
    {
        "identifier": 'EVENT_2392_action_queue_sync_228',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_3],
        "subscript": [
            {
                "identifier": 'EVENT_2392_action_queue_sync_228_SUBSCRIPT_play_sound_0',
                "command": 'play_sound',
                "args": [Sounds._004_JUMP, 4]
            },
            {
                "identifier": 'EVENT_2392_action_queue_sync_228_SUBSCRIPT_jump_to_height_1',
                "command": 'jump_to_height',
                "args": [160]
            }
        ]
    },
    {
        "identifier": 'EVENT_2392_run_dialog_229',
        "command": 'run_dialog',
        "args": [3099, AreaObjects.NPC_14, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_2392_pause_230',
        "command": 'pause',
        "args": [24]
    },
    {
        "identifier": 'EVENT_2392_set_action_script_sync_231',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_3, 856]
    },
    {
        "identifier": 'EVENT_2392_adjust_music_tempo_232',
        "command": 'adjust_music_tempo',
        "args": [MusicDirections.SPEED_UP, 32, 0]
    },
    {
        "identifier": 'EVENT_2392_pause_233',
        "command": 'pause',
        "args": [2]
    },
    {
        "identifier": 'EVENT_2392_run_dialog_234',
        "command": 'run_dialog',
        "args": [3100, AreaObjects.MEM_70A8, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]]
    },
    {
        "identifier": 'EVENT_2392_set_bit_235',
        "command": 'set_bit',
        "args": [0x7043, 0]
    },
    {
        "identifier": 'EVENT_2392_pause_236',
        "command": 'pause',
        "args": [1]
    },
    {
        "identifier": 'EVENT_2392_jmp_if_bit_set_237',
        "command": 'jmp_if_bit_set',
        "args": [0x7043, 1, 'EVENT_2392_pause_239']
    },
    {
        "identifier": 'EVENT_2392_jmp_238',
        "command": 'jmp',
        "args": ['EVENT_2392_pause_236']
    },
    {
        "identifier": 'EVENT_2392_pause_239',
        "command": 'pause',
        "args": [4]
    },
    {
        "identifier": 'EVENT_2392_adjust_music_tempo_240',
        "command": 'adjust_music_tempo',
        "args": [MusicDirections.SLOW_DOWN, 0, 0]
    },
    {
        "identifier": 'EVENT_2392_pause_241',
        "command": 'pause',
        "args": [32]
    },
    {
        "identifier": 'EVENT_2392_run_dialog_242',
        "command": 'run_dialog',
        "args": [3101, AreaObjects.MEM_70A8, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]]
    },
    {
        "identifier": 'EVENT_2392_action_queue_sync_243',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_2392_action_queue_sync_243_SUBSCRIPT_set_sprite_sequence_0',
                "command": 'set_sprite_sequence',
                "args": [1, inc_sprite=3, flags=[_0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_2392_action_queue_sync_243_SUBSCRIPT_play_sound_1',
                "command": 'play_sound',
                "args": [Sounds._022_CLOSE_DOOR, 4]
            }
        ]
    },
    {
        "identifier": 'EVENT_2392_set_action_script_sync_244',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.SCREEN_FOCUS, 391]
    },
    {
        "identifier": 'EVENT_2392_pause_245',
        "command": 'pause',
        "args": [8]
    },
    {
        "identifier": 'EVENT_2392_run_dialog_246',
        "command": 'run_dialog',
        "args": [3102, AreaObjects.MEM_70A8, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]]
    },
    {
        "identifier": 'EVENT_2392_pause_247',
        "command": 'pause',
        "args": [8]
    },
    {
        "identifier": 'EVENT_2392_set_action_script_async_248',
        "command": 'set_action_script_async',
        "args": [AreaObjects.MARIO, 857]
    },
    {
        "identifier": 'EVENT_2392_set_action_script_async_249',
        "command": 'set_action_script_async',
        "args": [AreaObjects.MARIO, 395]
    },
    {
        "identifier": 'EVENT_2392_unfreeze_camera_250',
        "command": 'unfreeze_camera'
    },
    {
        "identifier": 'EVENT_2392_ret_251',
        "command": 'ret'
    }
]
