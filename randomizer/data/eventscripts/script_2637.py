from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data import items
script = [
    {
        "identifier": 'EVENT_2637_set_0',
        "command": 'set',
        "args": [0x70ae, 20]
    },
    {
        "identifier": 'EVENT_2637_jmp_if_bit_set_1',
        "command": 'jmp_if_bit_set',
        "args": [0x7044, 1, 'EVENT_2637_jmp_if_random_above_128_5']
    },
    {
        "identifier": 'EVENT_2637_run_dialog_2',
        "command": 'run_dialog',
        "args": [3318, AreaObjects.NPC_12, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_2637_set_bit_3',
        "command": 'set_bit',
        "args": [0x7044, 1]
    },
    {
        "identifier": 'EVENT_2637_ret_4',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_2637_jmp_if_random_above_128_5',
        "command": 'jmp_if_random_above_128',
        "args": ['EVENT_2637_run_dialog_8']
    },
    {
        "identifier": 'EVENT_2637_run_dialog_6',
        "command": 'run_dialog',
        "args": [3320, AreaObjects.NPC_12, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_2637_ret_7',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_2637_run_dialog_8',
        "command": 'run_dialog',
        "args": [3302, AreaObjects.NPC_12, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_2637_action_queue_sync_9',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_0],
        "subscript": [
            {
                "identifier": 'EVENT_2637_action_queue_sync_9_SUBSCRIPT_sequence_looping_off_0',
                "command": 'sequence_looping_off'
            }
        ]
    },
    {
        "identifier": 'EVENT_2637_action_queue_async_10',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_2637_action_queue_async_10_SUBSCRIPT_overwrite_solidity_0',
                "command": 'overwrite_solidity',
                "args": [[]]
            },
            {
                "identifier": 'EVENT_2637_action_queue_async_10_SUBSCRIPT_walk_to_xy_coords_1',
                "command": 'walk_to_xy_coords',
                "args": [4, 16]
            },
            {
                "identifier": 'EVENT_2637_action_queue_async_10_SUBSCRIPT_face_northeast_2',
                "command": 'face_northeast'
            }
        ]
    },
    {
        "identifier": 'EVENT_2637_run_dialog_11',
        "command": 'run_dialog',
        "args": [3303, AreaObjects.NPC_12, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_2637_run_dialog_12',
        "command": 'run_dialog',
        "args": [3304, AreaObjects.BOWSER, [_0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_2637_set_7000_to_pressed_button_13',
        "command": 'set_7000_to_pressed_button'
    },
    {
        "identifier": 'EVENT_2637_pause_14',
        "command": 'pause',
        "args": [1]
    },
    {
        "identifier": 'EVENT_2637_jmp_if_7000_equals_short_15',
        "command": 'jmp_if_7000_equals_short',
        "args": [1, 'EVENT_2637_close_dialog_18']
    },
    {
        "identifier": 'EVENT_2637_jmp_if_7000_equals_short_16',
        "command": 'jmp_if_7000_equals_short',
        "args": [2, 'EVENT_2637_close_dialog_29']
    },
    {
        "identifier": 'EVENT_2637_jmp_17',
        "command": 'jmp',
        "args": ['EVENT_2637_set_7000_to_pressed_button_13']
    },
    {
        "identifier": 'EVENT_2637_close_dialog_18',
        "command": 'close_dialog'
    },
    {
        "identifier": 'EVENT_2637_run_dialog_19',
        "command": 'run_dialog',
        "args": [3305, AreaObjects.NPC_12, [_0x60Flags.CLOSABLE, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_2637_pause_20',
        "command": 'pause',
        "args": [16]
    },
    {
        "identifier": 'EVENT_2637_action_queue_sync_21',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_2637_action_queue_sync_21_SUBSCRIPT_set_sprite_sequence_0',
                "command": 'set_sprite_sequence',
                "args": [11, 0, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_2637_jmp_if_random_above_128_22',
        "command": 'jmp_if_random_above_128',
        "args": ['EVENT_2637_action_queue_sync_26']
    },
    {
        "identifier": 'EVENT_2637_action_queue_sync_23',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_0],
        "subscript": [
            {
                "identifier": 'EVENT_2637_action_queue_sync_23_SUBSCRIPT_set_sprite_sequence_0',
                "command": 'set_sprite_sequence',
                "args": [3, 0, [_0x08Flags.READ_AS_SEQUENCE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_2637_unsync_dialog_24',
        "command": 'unsync_dialog'
    },
    {
        "identifier": 'EVENT_2637_jmp_25',
        "command": 'jmp',
        "args": ['EVENT_2637_play_sound_40']
    },
    {
        "identifier": 'EVENT_2637_action_queue_sync_26',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_0],
        "subscript": [
            {
                "identifier": 'EVENT_2637_action_queue_sync_26_SUBSCRIPT_set_sprite_sequence_0',
                "command": 'set_sprite_sequence',
                "args": [2, 0, [_0x08Flags.READ_AS_SEQUENCE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_2637_unsync_dialog_27',
        "command": 'unsync_dialog'
    },
    {
        "identifier": 'EVENT_2637_jmp_28',
        "command": 'jmp',
        "args": ['EVENT_2637_play_sound_49']
    },
    {
        "identifier": 'EVENT_2637_close_dialog_29',
        "command": 'close_dialog'
    },
    {
        "identifier": 'EVENT_2637_run_dialog_30',
        "command": 'run_dialog',
        "args": [3305, AreaObjects.NPC_12, [_0x60Flags.CLOSABLE, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_2637_pause_31',
        "command": 'pause',
        "args": [16]
    },
    {
        "identifier": 'EVENT_2637_action_queue_sync_32',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_2637_action_queue_sync_32_SUBSCRIPT_set_sprite_sequence_0',
                "command": 'set_sprite_sequence',
                "args": [10, 0, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_2637_jmp_if_random_above_128_33',
        "command": 'jmp_if_random_above_128',
        "args": ['EVENT_2637_action_queue_sync_37']
    },
    {
        "identifier": 'EVENT_2637_action_queue_sync_34',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_0],
        "subscript": [
            {
                "identifier": 'EVENT_2637_action_queue_sync_34_SUBSCRIPT_set_sprite_sequence_0',
                "command": 'set_sprite_sequence',
                "args": [3, 0, [_0x08Flags.READ_AS_SEQUENCE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_2637_unsync_dialog_35',
        "command": 'unsync_dialog'
    },
    {
        "identifier": 'EVENT_2637_jmp_36',
        "command": 'jmp',
        "args": ['EVENT_2637_play_sound_49']
    },
    {
        "identifier": 'EVENT_2637_action_queue_sync_37',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_0],
        "subscript": [
            {
                "identifier": 'EVENT_2637_action_queue_sync_37_SUBSCRIPT_set_sprite_sequence_0',
                "command": 'set_sprite_sequence',
                "args": [2, 0, [_0x08Flags.READ_AS_SEQUENCE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_2637_unsync_dialog_38',
        "command": 'unsync_dialog'
    },
    {
        "identifier": 'EVENT_2637_jmp_39',
        "command": 'jmp',
        "args": ['EVENT_2637_play_sound_40']
    },
    {
        "identifier": 'EVENT_2637_play_sound_40',
        "command": 'play_sound',
        "args": [Sounds._088_WRONG_SIGNAL, 6]
    },
    {
        "identifier": 'EVENT_2637_run_dialog_41',
        "command": 'run_dialog',
        "args": [3306, AreaObjects.NPC_12, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_2637_set_action_script_async_42',
        "command": 'set_action_script_async',
        "args": [AreaObjects.MARIO, 395]
    },
    {
        "identifier": 'EVENT_2637_action_queue_sync_43',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_0],
        "subscript": [
            {
                "identifier": 'EVENT_2637_action_queue_sync_43_SUBSCRIPT_reset_properties_0',
                "command": 'reset_properties'
            },
            {
                "identifier": 'EVENT_2637_action_queue_sync_43_SUBSCRIPT_sequence_looping_on_1',
                "command": 'sequence_looping_on'
            }
        ]
    },
    {
        "identifier": 'EVENT_2637_run_dialog_44',
        "command": 'run_dialog',
        "args": [3310, AreaObjects.NPC_12, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_2637_jmp_if_dialog_option_b_45',
        "command": 'jmp_if_dialog_option_b',
        "args": ['EVENT_2637_pause_138']
    },
    {
        "identifier": 'EVENT_2637_pause_46',
        "command": 'pause',
        "args": [10]
    },
    {
        "identifier": 'EVENT_2637_set_action_script_async_47',
        "command": 'set_action_script_async',
        "args": [AreaObjects.MARIO, 670]
    },
    {
        "identifier": 'EVENT_2637_jmp_48',
        "command": 'jmp',
        "args": ['EVENT_2637_action_queue_sync_9']
    },
    {
        "identifier": 'EVENT_2637_play_sound_49',
        "command": 'play_sound',
        "args": [Sounds._087_CORRECT_SIGNAL, 6]
    },
    {
        "identifier": 'EVENT_2637_run_dialog_50',
        "command": 'run_dialog',
        "args": [3307, AreaObjects.NPC_12, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_2637_set_action_script_async_51',
        "command": 'set_action_script_async',
        "args": [AreaObjects.MARIO, 395]
    },
    {
        "identifier": 'EVENT_2637_action_queue_sync_52',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_0],
        "subscript": [
            {
                "identifier": 'EVENT_2637_action_queue_sync_52_SUBSCRIPT_reset_properties_0',
                "command": 'reset_properties'
            },
            {
                "identifier": 'EVENT_2637_action_queue_sync_52_SUBSCRIPT_sequence_looping_on_1',
                "command": 'sequence_looping_on'
            }
        ]
    },
    {
        "identifier": 'EVENT_2637_jmp_if_bit_set_53',
        "command": 'jmp_if_bit_set',
        "args": [0x7059, 0, 'EVENT_2637_set_random_56']
    },
    {
        "identifier": 'EVENT_2637_inc_54',
        "command": 'inc',
        "args": [0x70ef]
    },
    {
        "identifier": 'EVENT_2637_jmp_if_var_equals_byte_55',
        "command": 'jmp_if_var_equals_byte',
        "args": [0x70ef, 100, 'EVENT_2637_run_dialog_132']
    },
    {
        "identifier": 'EVENT_2637_set_random_56',
        "command": 'set_random',
        "args": [0x7000, 255]
    },
    {
        "identifier": 'EVENT_2637_jmp_if_7000_equals_short_57',
        "command": 'jmp_if_7000_equals_short',
        "args": [0, 'EVENT_2637_run_dialog_84']
    },
    {
        "identifier": 'EVENT_2637_jmp_if_7000_equals_short_58',
        "command": 'jmp_if_7000_equals_short',
        "args": [1, 'EVENT_2637_run_dialog_90']
    },
    {
        "identifier": 'EVENT_2637_jmp_if_7000_equals_short_59',
        "command": 'jmp_if_7000_equals_short',
        "args": [2, 'EVENT_2637_run_dialog_90']
    },
    {
        "identifier": 'EVENT_2637_jmp_if_7000_equals_short_60',
        "command": 'jmp_if_7000_equals_short',
        "args": [3, 'EVENT_2637_run_dialog_96']
    },
    {
        "identifier": 'EVENT_2637_jmp_if_7000_equals_short_61',
        "command": 'jmp_if_7000_equals_short',
        "args": [4, 'EVENT_2637_run_dialog_96']
    },
    {
        "identifier": 'EVENT_2637_jmp_if_7000_equals_short_62',
        "command": 'jmp_if_7000_equals_short',
        "args": [5, 'EVENT_2637_run_dialog_96']
    },
    {
        "identifier": 'EVENT_2637_jmp_if_7000_equals_short_63',
        "command": 'jmp_if_7000_equals_short',
        "args": [6, 'EVENT_2637_run_dialog_102']
    },
    {
        "identifier": 'EVENT_2637_jmp_if_7000_equals_short_64',
        "command": 'jmp_if_7000_equals_short',
        "args": [7, 'EVENT_2637_run_dialog_102']
    },
    {
        "identifier": 'EVENT_2637_jmp_if_7000_equals_short_65',
        "command": 'jmp_if_7000_equals_short',
        "args": [8, 'EVENT_2637_run_dialog_102']
    },
    {
        "identifier": 'EVENT_2637_jmp_if_7000_equals_short_66',
        "command": 'jmp_if_7000_equals_short',
        "args": [9, 'EVENT_2637_run_dialog_102']
    },
    {
        "identifier": 'EVENT_2637_set_random_67',
        "command": 'set_random',
        "args": [0x7000, 10]
    },
    {
        "identifier": 'EVENT_2637_jmp_if_7000_equals_short_68',
        "command": 'jmp_if_7000_equals_short',
        "args": [0, 'EVENT_2637_run_dialog_108']
    },
    {
        "identifier": 'EVENT_2637_jmp_if_7000_equals_short_69',
        "command": 'jmp_if_7000_equals_short',
        "args": [1, 'EVENT_2637_run_dialog_114']
    },
    {
        "identifier": 'EVENT_2637_jmp_if_7000_equals_short_70',
        "command": 'jmp_if_7000_equals_short',
        "args": [2, 'EVENT_2637_run_dialog_114']
    },
    {
        "identifier": 'EVENT_2637_jmp_if_7000_equals_short_71',
        "command": 'jmp_if_7000_equals_short',
        "args": [3, 'EVENT_2637_run_dialog_114']
    },
    {
        "identifier": 'EVENT_2637_jmp_if_7000_equals_short_72',
        "command": 'jmp_if_7000_equals_short',
        "args": [4, 'EVENT_2637_run_dialog_120']
    },
    {
        "identifier": 'EVENT_2637_jmp_if_7000_equals_short_73',
        "command": 'jmp_if_7000_equals_short',
        "args": [5, 'EVENT_2637_run_dialog_120']
    },
    {
        "identifier": 'EVENT_2637_jmp_if_7000_equals_short_74',
        "command": 'jmp_if_7000_equals_short',
        "args": [6, 'EVENT_2637_run_dialog_120']
    },
    {
        "identifier": 'EVENT_2637_jmp_if_7000_equals_short_75',
        "command": 'jmp_if_7000_equals_short',
        "args": [7, 'EVENT_2637_run_dialog_126']
    },
    {
        "identifier": 'EVENT_2637_jmp_if_7000_equals_short_76',
        "command": 'jmp_if_7000_equals_short',
        "args": [8, 'EVENT_2637_run_dialog_126']
    },
    {
        "identifier": 'EVENT_2637_jmp_if_7000_equals_short_77',
        "command": 'jmp_if_7000_equals_short',
        "args": [9, 'EVENT_2637_run_dialog_126']
    },
    {
        "identifier": 'EVENT_2637_jmp_78',
        "command": 'jmp',
        "args": ['EVENT_2637_run_dialog_108']
    },
    {
        "identifier": 'EVENT_2637_run_dialog_79',
        "command": 'run_dialog',
        "args": [3310, AreaObjects.NPC_12, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_2637_jmp_if_dialog_option_b_80',
        "command": 'jmp_if_dialog_option_b',
        "args": ['EVENT_2637_pause_138']
    },
    {
        "identifier": 'EVENT_2637_pause_81',
        "command": 'pause',
        "args": [10]
    },
    {
        "identifier": 'EVENT_2637_set_action_script_async_82',
        "command": 'set_action_script_async',
        "args": [AreaObjects.MARIO, 670]
    },
    {
        "identifier": 'EVENT_2637_jmp_83',
        "command": 'jmp',
        "args": ['EVENT_2637_action_queue_sync_9']
    },
    {
        "identifier": 'EVENT_2637_run_dialog_84',
        "command": 'run_dialog',
        "args": [3183, AreaObjects.NPC_12, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_2637_set_85',
        "command": 'set',
        "args": [0x70a7, 131]
    },
    {
        "identifier": 'EVENT_2637_play_sound_86',
        "command": 'play_sound',
        "args": [Sounds._027_FOUND_AN_ITEM, 6]
    },
    {
        "identifier": 'EVENT_2637_run_dialog_87',
        "command": 'run_dialog',
        "args": [524, AreaObjects.BOWSER, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_2637_put_inventory_88',
        "command": 'put_inventory',
        "args": [items.RockCandy]
    },
    {
        "identifier": 'EVENT_2637_jmp_89',
        "command": 'jmp',
        "args": ['EVENT_2637_run_dialog_79']
    },
    {
        "identifier": 'EVENT_2637_run_dialog_90',
        "command": 'run_dialog',
        "args": [3183, AreaObjects.NPC_12, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_2637_set_91',
        "command": 'set',
        "args": [0x70a7, 101]
    },
    {
        "identifier": 'EVENT_2637_play_sound_92',
        "command": 'play_sound',
        "args": [Sounds._027_FOUND_AN_ITEM, 6]
    },
    {
        "identifier": 'EVENT_2637_run_dialog_93',
        "command": 'run_dialog',
        "args": [524, AreaObjects.BOWSER, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_2637_put_inventory_94',
        "command": 'put_inventory',
        "args": [items.RoyalSyrup]
    },
    {
        "identifier": 'EVENT_2637_jmp_95',
        "command": 'jmp',
        "args": ['EVENT_2637_run_dialog_79']
    },
    {
        "identifier": 'EVENT_2637_run_dialog_96',
        "command": 'run_dialog',
        "args": [3183, AreaObjects.NPC_12, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_2637_set_97',
        "command": 'set',
        "args": [0x70a7, 107]
    },
    {
        "identifier": 'EVENT_2637_play_sound_98',
        "command": 'play_sound',
        "args": [Sounds._027_FOUND_AN_ITEM, 6]
    },
    {
        "identifier": 'EVENT_2637_run_dialog_99',
        "command": 'run_dialog',
        "args": [524, AreaObjects.BOWSER, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_2637_put_inventory_100',
        "command": 'put_inventory',
        "args": [items.RedEssence]
    },
    {
        "identifier": 'EVENT_2637_jmp_101',
        "command": 'jmp',
        "args": ['EVENT_2637_run_dialog_79']
    },
    {
        "identifier": 'EVENT_2637_run_dialog_102',
        "command": 'run_dialog',
        "args": [3183, AreaObjects.NPC_12, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_2637_set_103',
        "command": 'set',
        "args": [0x70a7, 108]
    },
    {
        "identifier": 'EVENT_2637_play_sound_104',
        "command": 'play_sound',
        "args": [Sounds._027_FOUND_AN_ITEM, 6]
    },
    {
        "identifier": 'EVENT_2637_run_dialog_105',
        "command": 'run_dialog',
        "args": [524, AreaObjects.BOWSER, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_2637_put_inventory_106',
        "command": 'put_inventory',
        "args": [items.KerokeroCola]
    },
    {
        "identifier": 'EVENT_2637_jmp_107',
        "command": 'jmp',
        "args": ['EVENT_2637_run_dialog_79']
    },
    {
        "identifier": 'EVENT_2637_run_dialog_108',
        "command": 'run_dialog',
        "args": [3183, AreaObjects.NPC_12, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_2637_set_109',
        "command": 'set',
        "args": [0x70a7, 96]
    },
    {
        "identifier": 'EVENT_2637_play_sound_110',
        "command": 'play_sound',
        "args": [Sounds._027_FOUND_AN_ITEM, 6]
    },
    {
        "identifier": 'EVENT_2637_run_dialog_111',
        "command": 'run_dialog',
        "args": [524, AreaObjects.BOWSER, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_2637_put_inventory_112',
        "command": 'put_inventory',
        "args": [items.Mushroom]
    },
    {
        "identifier": 'EVENT_2637_jmp_113',
        "command": 'jmp',
        "args": ['EVENT_2637_run_dialog_79']
    },
    {
        "identifier": 'EVENT_2637_run_dialog_114',
        "command": 'run_dialog',
        "args": [3183, AreaObjects.NPC_12, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_2637_set_115',
        "command": 'set',
        "args": [0x70a7, 155]
    },
    {
        "identifier": 'EVENT_2637_play_sound_116',
        "command": 'play_sound',
        "args": [Sounds._027_FOUND_AN_ITEM, 6]
    },
    {
        "identifier": 'EVENT_2637_run_dialog_117',
        "command": 'run_dialog',
        "args": [524, AreaObjects.BOWSER, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_2637_put_inventory_118',
        "command": 'put_inventory',
        "args": [items.WiltShroom]
    },
    {
        "identifier": 'EVENT_2637_jmp_119',
        "command": 'jmp',
        "args": ['EVENT_2637_run_dialog_79']
    },
    {
        "identifier": 'EVENT_2637_run_dialog_120',
        "command": 'run_dialog',
        "args": [3183, AreaObjects.NPC_12, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_2637_set_121',
        "command": 'set',
        "args": [0x70a7, 156]
    },
    {
        "identifier": 'EVENT_2637_play_sound_122',
        "command": 'play_sound',
        "args": [Sounds._027_FOUND_AN_ITEM, 6]
    },
    {
        "identifier": 'EVENT_2637_run_dialog_123',
        "command": 'run_dialog',
        "args": [524, AreaObjects.BOWSER, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_2637_put_inventory_124',
        "command": 'put_inventory',
        "args": [items.RottenMush]
    },
    {
        "identifier": 'EVENT_2637_jmp_125',
        "command": 'jmp',
        "args": ['EVENT_2637_run_dialog_79']
    },
    {
        "identifier": 'EVENT_2637_run_dialog_126',
        "command": 'run_dialog',
        "args": [3183, AreaObjects.NPC_12, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_2637_set_127',
        "command": 'set',
        "args": [0x70a7, 157]
    },
    {
        "identifier": 'EVENT_2637_play_sound_128',
        "command": 'play_sound',
        "args": [Sounds._027_FOUND_AN_ITEM, 6]
    },
    {
        "identifier": 'EVENT_2637_run_dialog_129',
        "command": 'run_dialog',
        "args": [524, AreaObjects.BOWSER, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_2637_put_inventory_130',
        "command": 'put_inventory',
        "args": [items.MoldyMush]
    },
    {
        "identifier": 'EVENT_2637_jmp_131',
        "command": 'jmp',
        "args": ['EVENT_2637_run_dialog_79']
    },
    {
        "identifier": 'EVENT_2637_run_dialog_132',
        "command": 'run_dialog',
        "args": [3308, AreaObjects.NPC_12, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_2637_play_sound_133',
        "command": 'play_sound',
        "args": [Sounds._027_FOUND_AN_ITEM, 6]
    },
    {
        "identifier": 'EVENT_2637_set_bit_134',
        "command": 'set_bit',
        "args": [0x7059, 0]
    },
    {
        "identifier": 'EVENT_2637_run_dialog_135',
        "command": 'run_dialog',
        "args": [3309, AreaObjects.BOWSER, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_2637_put_inventory_136',
        "command": 'put_inventory',
        "args": [items.StarEgg]
    },
    {
        "identifier": 'EVENT_2637_jmp_137',
        "command": 'jmp',
        "args": ['EVENT_2637_run_dialog_79']
    },
    {
        "identifier": 'EVENT_2637_pause_138',
        "command": 'pause',
        "args": [10]
    },
    {
        "identifier": 'EVENT_2637_set_action_script_async_139',
        "command": 'set_action_script_async',
        "args": [AreaObjects.MARIO, 671]
    },
    {
        "identifier": 'EVENT_2637_run_dialog_140',
        "command": 'run_dialog',
        "args": [2408, AreaObjects.NPC_12, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_2637_ret_141',
        "command": 'ret'
    }
]
