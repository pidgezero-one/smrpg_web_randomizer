from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data import items
script = [
    {
        "identifier": 'EVENT_1078_set_short_mem_0',
        "command": 'set_short_mem',
        "args": [0x7000, 0x7024]
    },
    {
        "identifier": 'EVENT_1078_set_short_mem_1',
        "command": 'set_short_mem',
        "args": [0x70f0, 0x7000]
    },
    {
        "identifier": 'EVENT_1078_set_short_mem_2',
        "command": 'set_short_mem',
        "args": [0x7000, 0x7026]
    },
    {
        "identifier": 'EVENT_1078_set_short_mem_3',
        "command": 'set_short_mem',
        "args": [0x70f1, 0x7000]
    },
    {
        "identifier": 'EVENT_1078_set_short_mem_4',
        "command": 'set_short_mem',
        "args": [0x7000, 0x7028]
    },
    {
        "identifier": 'EVENT_1078_set_short_mem_5',
        "command": 'set_short_mem',
        "args": [0x70f2, 0x7000]
    },
    {
        "identifier": 'EVENT_1078_set_short_mem_6',
        "command": 'set_short_mem',
        "args": [0x7000, 0x702a]
    },
    {
        "identifier": 'EVENT_1078_set_short_mem_7',
        "command": 'set_short_mem',
        "args": [0x70f3, 0x7000]
    },
    {
        "identifier": 'EVENT_1078_set_short_mem_8',
        "command": 'set_short_mem',
        "args": [0x7000, 0x702c]
    },
    {
        "identifier": 'EVENT_1078_set_short_mem_9',
        "command": 'set_short_mem',
        "args": [0x70f4, 0x7000]
    },
    {
        "identifier": 'EVENT_1078_set_short_mem_10',
        "command": 'set_short_mem',
        "args": [0x7000, 0x702e]
    },
    {
        "identifier": 'EVENT_1078_set_short_mem_11',
        "command": 'set_short_mem',
        "args": [0x70f5, 0x7000]
    },
    {
        "identifier": 'EVENT_1078_set_short_mem_12',
        "command": 'set_short_mem',
        "args": [0x7000, 0x7030]
    },
    {
        "identifier": 'EVENT_1078_set_short_mem_13',
        "command": 'set_short_mem',
        "args": [0x70f6, 0x7000]
    },
    {
        "identifier": 'EVENT_1078_set_short_mem_14',
        "command": 'set_short_mem',
        "args": [0x7000, 0x7032]
    },
    {
        "identifier": 'EVENT_1078_set_short_mem_15',
        "command": 'set_short_mem',
        "args": [0x70f7, 0x7000]
    },
    {
        "identifier": 'EVENT_1078_action_queue_async_16',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_8],
        "subscript": [
            {
                "identifier": 'EVENT_1078_action_queue_async_16_SUBSCRIPT_sequence_looping_off_0',
                "command": 'sequence_looping_off'
            },
            {
                "identifier": 'EVENT_1078_action_queue_async_16_SUBSCRIPT_face_southeast_1',
                "command": 'face_southeast'
            }
        ]
    },
    {
        "identifier": 'EVENT_1078_run_dialog_17',
        "command": 'run_dialog',
        "args": [3062, AreaObjects.MEM_70A8, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]]
    },
    {
        "identifier": 'EVENT_1078_pause_18',
        "command": 'pause',
        "args": [10]
    },
    {
        "identifier": 'EVENT_1078_set_bit_19',
        "command": 'set_bit',
        "args": [0x7044, 6]
    },
    {
        "identifier": 'EVENT_1078_set_action_script_sync_20',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_0, 157]
    },
    {
        "identifier": 'EVENT_1078_set_action_script_sync_21',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_1, 157]
    },
    {
        "identifier": 'EVENT_1078_set_action_script_sync_22',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_2, 157]
    },
    {
        "identifier": 'EVENT_1078_set_action_script_sync_23',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_3, 157]
    },
    {
        "identifier": 'EVENT_1078_set_action_script_sync_24',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_4, 157]
    },
    {
        "identifier": 'EVENT_1078_set_action_script_sync_25',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_5, 157]
    },
    {
        "identifier": 'EVENT_1078_set_action_script_sync_26',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_6, 157]
    },
    {
        "identifier": 'EVENT_1078_set_action_script_sync_27',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_7, 157]
    },
    {
        "identifier": 'EVENT_1078_clear_bit_28',
        "command": 'clear_bit',
        "args": [0x7044, 6]
    },
    {
        "identifier": 'EVENT_1078_pause_29',
        "command": 'pause',
        "args": [30]
    },
    {
        "identifier": 'EVENT_1078_action_queue_sync_30',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_8],
        "subscript": [
            {
                "identifier": 'EVENT_1078_action_queue_sync_30_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_SLOW, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_1078_action_queue_sync_30_SUBSCRIPT_set_sprite_sequence_1',
                "command": 'set_sprite_sequence',
                "args": [2, 0, [_0x08Flags.READ_AS_SEQUENCE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_1078_action_queue_async_31',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_1078_action_queue_async_31_SUBSCRIPT_clear_solidity_bits_0',
                "command": 'clear_solidity_bits',
                "args": [[_0x0AFlags.BIT_4, _0x0AFlags.CANT_PASS_NPCS, _0x0AFlags.CANT_WALK_THROUGH, _0x0AFlags.BIT_7]]
            },
            {
                "identifier": 'EVENT_1078_action_queue_async_31_SUBSCRIPT_clear_solidity_bits_1',
                "command": 'clear_solidity_bits',
                "args": [[_0x0AFlags.CANT_PASS_WALLS]]
            },
            {
                "identifier": 'EVENT_1078_action_queue_async_31_SUBSCRIPT_set_animation_speed_2',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_1078_action_queue_async_31_SUBSCRIPT_walk_to_xy_coords_3',
                "command": 'walk_to_xy_coords',
                "args": [16, 29]
            },
            {
                "identifier": 'EVENT_1078_action_queue_async_31_SUBSCRIPT_set_sprite_sequence_4',
                "command": 'set_sprite_sequence',
                "args": [9, 2, [_0x08Flags.READ_AS_SEQUENCE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_1078_pause_32',
        "command": 'pause',
        "args": [15]
    },
    {
        "identifier": 'EVENT_1078_deactivate_sound_channels_33',
        "command": 'deactivate_sound_channels',
        "args": [[0, 1, 2, 3, 4, 5, 6, 7]]
    },
    {
        "identifier": 'EVENT_1078_play_music_default_volume_34',
        "command": 'play_music_default_volume',
        "args": [Music._52_TOADOFSKY]
    },
    {
        "identifier": 'EVENT_1078_pause_35',
        "command": 'pause',
        "args": [120]
    },
    {
        "identifier": 'EVENT_1078_pause_36',
        "command": 'pause',
        "args": [120]
    },
    {
        "identifier": 'EVENT_1078_pause_37',
        "command": 'pause',
        "args": [120]
    },
    {
        "identifier": 'EVENT_1078_pause_38',
        "command": 'pause',
        "args": [120]
    },
    {
        "identifier": 'EVENT_1078_pause_39',
        "command": 'pause',
        "args": [120]
    },
    {
        "identifier": 'EVENT_1078_pause_40',
        "command": 'pause',
        "args": [120]
    },
    {
        "identifier": 'EVENT_1078_pause_41',
        "command": 'pause',
        "args": [120]
    },
    {
        "identifier": 'EVENT_1078_pause_42',
        "command": 'pause',
        "args": [120]
    },
    {
        "identifier": 'EVENT_1078_pause_43',
        "command": 'pause',
        "args": [75]
    },
    {
        "identifier": 'EVENT_1078_set_short_mem_44',
        "command": 'set_short_mem',
        "args": [0x7000, 0x70f0]
    },
    {
        "identifier": 'EVENT_1078_jmp_to_subroutine_45',
        "command": 'jmp_to_subroutine',
        "args": ['EVENT_1078_jmp_if_var_equals_short_119']
    },
    {
        "identifier": 'EVENT_1078_pause_46',
        "command": 'pause',
        "args": [25]
    },
    {
        "identifier": 'EVENT_1078_set_short_mem_47',
        "command": 'set_short_mem',
        "args": [0x7000, 0x70f1]
    },
    {
        "identifier": 'EVENT_1078_jmp_to_subroutine_48',
        "command": 'jmp_to_subroutine',
        "args": ['EVENT_1078_jmp_if_var_equals_short_119']
    },
    {
        "identifier": 'EVENT_1078_pause_49',
        "command": 'pause',
        "args": [25]
    },
    {
        "identifier": 'EVENT_1078_set_short_mem_50',
        "command": 'set_short_mem',
        "args": [0x7000, 0x70f2]
    },
    {
        "identifier": 'EVENT_1078_jmp_to_subroutine_51',
        "command": 'jmp_to_subroutine',
        "args": ['EVENT_1078_jmp_if_var_equals_short_119']
    },
    {
        "identifier": 'EVENT_1078_pause_52',
        "command": 'pause',
        "args": [25]
    },
    {
        "identifier": 'EVENT_1078_set_short_mem_53',
        "command": 'set_short_mem',
        "args": [0x7000, 0x70f3]
    },
    {
        "identifier": 'EVENT_1078_jmp_to_subroutine_54',
        "command": 'jmp_to_subroutine',
        "args": ['EVENT_1078_jmp_if_var_equals_short_119']
    },
    {
        "identifier": 'EVENT_1078_pause_55',
        "command": 'pause',
        "args": [26]
    },
    {
        "identifier": 'EVENT_1078_set_short_mem_56',
        "command": 'set_short_mem',
        "args": [0x7000, 0x70f4]
    },
    {
        "identifier": 'EVENT_1078_jmp_to_subroutine_57',
        "command": 'jmp_to_subroutine',
        "args": ['EVENT_1078_jmp_if_var_equals_short_119']
    },
    {
        "identifier": 'EVENT_1078_pause_58',
        "command": 'pause',
        "args": [26]
    },
    {
        "identifier": 'EVENT_1078_set_short_mem_59',
        "command": 'set_short_mem',
        "args": [0x7000, 0x70f5]
    },
    {
        "identifier": 'EVENT_1078_jmp_to_subroutine_60',
        "command": 'jmp_to_subroutine',
        "args": ['EVENT_1078_jmp_if_var_equals_short_119']
    },
    {
        "identifier": 'EVENT_1078_pause_61',
        "command": 'pause',
        "args": [27]
    },
    {
        "identifier": 'EVENT_1078_set_short_mem_62',
        "command": 'set_short_mem',
        "args": [0x7000, 0x70f6]
    },
    {
        "identifier": 'EVENT_1078_jmp_to_subroutine_63',
        "command": 'jmp_to_subroutine',
        "args": ['EVENT_1078_jmp_if_var_equals_short_119']
    },
    {
        "identifier": 'EVENT_1078_pause_64',
        "command": 'pause',
        "args": [27]
    },
    {
        "identifier": 'EVENT_1078_set_short_mem_65',
        "command": 'set_short_mem',
        "args": [0x7000, 0x70f7]
    },
    {
        "identifier": 'EVENT_1078_jmp_to_subroutine_66',
        "command": 'jmp_to_subroutine',
        "args": ['EVENT_1078_jmp_if_var_equals_short_119']
    },
    {
        "identifier": 'EVENT_1078_pause_67',
        "command": 'pause',
        "args": [18]
    },
    {
        "identifier": 'EVENT_1078_stop_sound_68',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_1078_pause_69',
        "command": 'pause',
        "args": [140]
    },
    {
        "identifier": 'EVENT_1078_set_action_script_async_70',
        "command": 'set_action_script_async',
        "args": [AreaObjects.MARIO, 395]
    },
    {
        "identifier": 'EVENT_1078_action_queue_sync_71',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_0],
        "subscript": [
            {
                "identifier": 'EVENT_1078_action_queue_sync_71_SUBSCRIPT_shirt_to_xy_coords_0',
                "command": 'shirt_to_xy_coords',
                "args": [14, 30]
            }
        ]
    },
    {
        "identifier": 'EVENT_1078_action_queue_sync_72',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_1],
        "subscript": [
            {
                "identifier": 'EVENT_1078_action_queue_sync_72_SUBSCRIPT_shirt_to_xy_coords_0',
                "command": 'shirt_to_xy_coords',
                "args": [13, 33]
            }
        ]
    },
    {
        "identifier": 'EVENT_1078_action_queue_sync_73',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_2],
        "subscript": [
            {
                "identifier": 'EVENT_1078_action_queue_sync_73_SUBSCRIPT_shirt_to_xy_coords_0',
                "command": 'shirt_to_xy_coords',
                "args": [14, 36]
            }
        ]
    },
    {
        "identifier": 'EVENT_1078_action_queue_sync_74',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_3],
        "subscript": [
            {
                "identifier": 'EVENT_1078_action_queue_sync_74_SUBSCRIPT_shirt_to_xy_coords_0',
                "command": 'shirt_to_xy_coords',
                "args": [12, 31]
            }
        ]
    },
    {
        "identifier": 'EVENT_1078_action_queue_sync_75',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_4],
        "subscript": [
            {
                "identifier": 'EVENT_1078_action_queue_sync_75_SUBSCRIPT_shirt_to_xy_coords_0',
                "command": 'shirt_to_xy_coords',
                "args": [15, 36]
            }
        ]
    },
    {
        "identifier": 'EVENT_1078_action_queue_sync_76',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_5],
        "subscript": [
            {
                "identifier": 'EVENT_1078_action_queue_sync_76_SUBSCRIPT_shirt_to_xy_coords_0',
                "command": 'shirt_to_xy_coords',
                "args": [14, 33]
            }
        ]
    },
    {
        "identifier": 'EVENT_1078_action_queue_sync_77',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_6],
        "subscript": [
            {
                "identifier": 'EVENT_1078_action_queue_sync_77_SUBSCRIPT_shirt_to_xy_coords_0',
                "command": 'shirt_to_xy_coords',
                "args": [16, 36]
            }
        ]
    },
    {
        "identifier": 'EVENT_1078_action_queue_async_78',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_7],
        "subscript": [
            {
                "identifier": 'EVENT_1078_action_queue_async_78_SUBSCRIPT_shirt_to_xy_coords_0',
                "command": 'shirt_to_xy_coords',
                "args": [15, 33]
            }
        ]
    },
    {
        "identifier": 'EVENT_1078_action_queue_async_79',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_1078_action_queue_async_79_SUBSCRIPT_face_southwest_0',
                "command": 'face_southwest'
            }
        ]
    },
    {
        "identifier": 'EVENT_1078_set_action_script_sync_80',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_0, 589]
    },
    {
        "identifier": 'EVENT_1078_pause_81',
        "command": 'pause',
        "args": [3]
    },
    {
        "identifier": 'EVENT_1078_set_action_script_sync_82',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_1, 589]
    },
    {
        "identifier": 'EVENT_1078_pause_83',
        "command": 'pause',
        "args": [3]
    },
    {
        "identifier": 'EVENT_1078_set_action_script_sync_84',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_2, 589]
    },
    {
        "identifier": 'EVENT_1078_pause_85',
        "command": 'pause',
        "args": [3]
    },
    {
        "identifier": 'EVENT_1078_set_action_script_sync_86',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_3, 589]
    },
    {
        "identifier": 'EVENT_1078_pause_87',
        "command": 'pause',
        "args": [3]
    },
    {
        "identifier": 'EVENT_1078_play_sound_88',
        "command": 'play_sound',
        "args": [Sounds._064_SPINNING_COPTERS, 6]
    },
    {
        "identifier": 'EVENT_1078_set_action_script_sync_89',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_4, 589]
    },
    {
        "identifier": 'EVENT_1078_pause_90',
        "command": 'pause',
        "args": [3]
    },
    {
        "identifier": 'EVENT_1078_set_action_script_sync_91',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_5, 589]
    },
    {
        "identifier": 'EVENT_1078_pause_92',
        "command": 'pause',
        "args": [3]
    },
    {
        "identifier": 'EVENT_1078_set_action_script_sync_93',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_6, 589]
    },
    {
        "identifier": 'EVENT_1078_pause_94',
        "command": 'pause',
        "args": [3]
    },
    {
        "identifier": 'EVENT_1078_set_action_script_sync_95',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_7, 589]
    },
    {
        "identifier": 'EVENT_1078_pause_96',
        "command": 'pause',
        "args": [120]
    },
    {
        "identifier": 'EVENT_1078_set_action_script_sync_97',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_0, 157]
    },
    {
        "identifier": 'EVENT_1078_set_action_script_sync_98',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_1, 157]
    },
    {
        "identifier": 'EVENT_1078_set_action_script_sync_99',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_2, 157]
    },
    {
        "identifier": 'EVENT_1078_set_action_script_sync_100',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_3, 157]
    },
    {
        "identifier": 'EVENT_1078_set_action_script_sync_101',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_4, 157]
    },
    {
        "identifier": 'EVENT_1078_set_action_script_sync_102',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_5, 157]
    },
    {
        "identifier": 'EVENT_1078_set_action_script_sync_103',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_6, 157]
    },
    {
        "identifier": 'EVENT_1078_set_action_script_async_104',
        "command": 'set_action_script_async',
        "args": [AreaObjects.NPC_7, 157]
    },
    {
        "identifier": 'EVENT_1078_action_queue_async_105',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_8],
        "subscript": [
            {
                "identifier": 'EVENT_1078_action_queue_async_105_SUBSCRIPT_reset_properties_0',
                "command": 'reset_properties'
            },
            {
                "identifier": 'EVENT_1078_action_queue_async_105_SUBSCRIPT_sequence_looping_off_1',
                "command": 'sequence_looping_off'
            },
            {
                "identifier": 'EVENT_1078_action_queue_async_105_SUBSCRIPT_set_animation_speed_2',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_1078_action_queue_async_105_SUBSCRIPT_face_southwest_3',
                "command": 'face_southwest'
            }
        ]
    },
    {
        "identifier": 'EVENT_1078_deactivate_sound_channels_106',
        "command": 'deactivate_sound_channels',
        "args": [[0, 1, 2, 3]]
    },
    {
        "identifier": 'EVENT_1078_play_music_default_volume_107',
        "command": 'play_music_default_volume',
        "args": [Music._17_TADPOLE_POND]
    },
    {
        "identifier": 'EVENT_1078_deactivate_sound_channels_108',
        "command": 'deactivate_sound_channels',
        "args": [[0, 1, 2, 3]]
    },
    {
        "identifier": 'EVENT_1078_clear_bit_109',
        "command": 'clear_bit',
        "args": [0x7093, 0]
    },
    {
        "identifier": 'EVENT_1078_clear_bit_110',
        "command": 'clear_bit',
        "args": [0x7043, 0]
    },
    {
        "identifier": 'EVENT_1078_clear_bit_111',
        "command": 'clear_bit',
        "args": [0x7043, 1]
    },
    {
        "identifier": 'EVENT_1078_clear_bit_112',
        "command": 'clear_bit',
        "args": [0x7043, 2]
    },
    {
        "identifier": 'EVENT_1078_clear_bit_113',
        "command": 'clear_bit',
        "args": [0x7043, 3]
    },
    {
        "identifier": 'EVENT_1078_clear_bit_114',
        "command": 'clear_bit',
        "args": [0x7043, 4]
    },
    {
        "identifier": 'EVENT_1078_clear_bit_115',
        "command": 'clear_bit',
        "args": [0x7043, 5]
    },
    {
        "identifier": 'EVENT_1078_clear_bit_116',
        "command": 'clear_bit',
        "args": [0x7043, 6]
    },
    {
        "identifier": 'EVENT_1078_clear_bit_117',
        "command": 'clear_bit',
        "args": [0x7043, 7]
    },
    {
        "identifier": 'EVENT_1078_ret_118',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_1078_jmp_if_var_equals_short_119',
        "command": 'jmp_if_var_equals_short',
        "args": [0x7000, 0, 'EVENT_1078_play_sound_126']
    },
    {
        "identifier": 'EVENT_1078_jmp_if_var_equals_short_120',
        "command": 'jmp_if_var_equals_short',
        "args": [0x7000, 1, 'EVENT_1078_play_sound_128']
    },
    {
        "identifier": 'EVENT_1078_jmp_if_var_equals_short_121',
        "command": 'jmp_if_var_equals_short',
        "args": [0x7000, 2, 'EVENT_1078_play_sound_130']
    },
    {
        "identifier": 'EVENT_1078_jmp_if_var_equals_short_122',
        "command": 'jmp_if_var_equals_short',
        "args": [0x7000, 3, 'EVENT_1078_play_sound_132']
    },
    {
        "identifier": 'EVENT_1078_jmp_if_var_equals_short_123',
        "command": 'jmp_if_var_equals_short',
        "args": [0x7000, 4, 'EVENT_1078_play_sound_134']
    },
    {
        "identifier": 'EVENT_1078_jmp_if_var_equals_short_124',
        "command": 'jmp_if_var_equals_short',
        "args": [0x7000, 5, 'EVENT_1078_play_sound_136']
    },
    {
        "identifier": 'EVENT_1078_jmp_if_var_equals_short_125',
        "command": 'jmp_if_var_equals_short',
        "args": [0x7000, 6, 'EVENT_1078_play_sound_138']
    },
    {
        "identifier": 'EVENT_1078_play_sound_126',
        "command": 'play_sound',
        "args": [Sounds._136_TOADOFSKY_COMPOSITION_DO, 6]
    },
    {
        "identifier": 'EVENT_1078_ret_127',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_1078_play_sound_128',
        "command": 'play_sound',
        "args": [Sounds._137_TOADOFSKY_COMPOSITION_RE, 6]
    },
    {
        "identifier": 'EVENT_1078_ret_129',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_1078_play_sound_130',
        "command": 'play_sound',
        "args": [Sounds._138_TOADOFSKY_COMPOSITION_MI, 6]
    },
    {
        "identifier": 'EVENT_1078_ret_131',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_1078_play_sound_132',
        "command": 'play_sound',
        "args": [Sounds._139_TOADOFSKY_COMPOSITION_FA, 6]
    },
    {
        "identifier": 'EVENT_1078_ret_133',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_1078_play_sound_134',
        "command": 'play_sound',
        "args": [Sounds._140_TOADOFSKY_COMPOSITION_SO, 6]
    },
    {
        "identifier": 'EVENT_1078_ret_135',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_1078_play_sound_136',
        "command": 'play_sound',
        "args": [Sounds._141_TOADOFSKY_COMPOSITION_LA, 6]
    },
    {
        "identifier": 'EVENT_1078_ret_137',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_1078_play_sound_138',
        "command": 'play_sound',
        "args": [Sounds._142_TOADOFSKY_COMPOSITION_TI, 6]
    },
    {
        "identifier": 'EVENT_1078_ret_139',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_1078_jmp_if_bit_clear_140',
        "command": 'jmp_if_bit_clear',
        "args": [0x7043, 0, 'EVENT_1078_jmp_if_bit_clear_143']
    },
    {
        "identifier": 'EVENT_1078_set_action_script_sync_141',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_0, 157]
    },
    {
        "identifier": 'EVENT_1078_pause_142',
        "command": 'pause',
        "args": [5]
    },
    {
        "identifier": 'EVENT_1078_jmp_if_bit_clear_143',
        "command": 'jmp_if_bit_clear',
        "args": [0x7043, 1, 'EVENT_1078_jmp_if_bit_clear_146']
    },
    {
        "identifier": 'EVENT_1078_set_action_script_sync_144',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_1, 157]
    },
    {
        "identifier": 'EVENT_1078_pause_145',
        "command": 'pause',
        "args": [5]
    },
    {
        "identifier": 'EVENT_1078_jmp_if_bit_clear_146',
        "command": 'jmp_if_bit_clear',
        "args": [0x7043, 2, 'EVENT_1078_jmp_if_bit_clear_149']
    },
    {
        "identifier": 'EVENT_1078_set_action_script_sync_147',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_2, 157]
    },
    {
        "identifier": 'EVENT_1078_pause_148',
        "command": 'pause',
        "args": [5]
    },
    {
        "identifier": 'EVENT_1078_jmp_if_bit_clear_149',
        "command": 'jmp_if_bit_clear',
        "args": [0x7043, 3, 'EVENT_1078_jmp_if_bit_clear_152']
    },
    {
        "identifier": 'EVENT_1078_set_action_script_sync_150',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_3, 157]
    },
    {
        "identifier": 'EVENT_1078_pause_151',
        "command": 'pause',
        "args": [5]
    },
    {
        "identifier": 'EVENT_1078_jmp_if_bit_clear_152',
        "command": 'jmp_if_bit_clear',
        "args": [0x7043, 4, 'EVENT_1078_jmp_if_bit_clear_155']
    },
    {
        "identifier": 'EVENT_1078_set_action_script_sync_153',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_4, 157]
    },
    {
        "identifier": 'EVENT_1078_pause_154',
        "command": 'pause',
        "args": [5]
    },
    {
        "identifier": 'EVENT_1078_jmp_if_bit_clear_155',
        "command": 'jmp_if_bit_clear',
        "args": [0x7043, 5, 'EVENT_1078_jmp_if_bit_clear_158']
    },
    {
        "identifier": 'EVENT_1078_set_action_script_sync_156',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_5, 157]
    },
    {
        "identifier": 'EVENT_1078_pause_157',
        "command": 'pause',
        "args": [5]
    },
    {
        "identifier": 'EVENT_1078_jmp_if_bit_clear_158',
        "command": 'jmp_if_bit_clear',
        "args": [0x7043, 6, 'EVENT_1078_jmp_if_bit_clear_161']
    },
    {
        "identifier": 'EVENT_1078_set_action_script_sync_159',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_6, 157]
    },
    {
        "identifier": 'EVENT_1078_pause_160',
        "command": 'pause',
        "args": [5]
    },
    {
        "identifier": 'EVENT_1078_jmp_if_bit_clear_161',
        "command": 'jmp_if_bit_clear',
        "args": [0x7043, 7, 'EVENT_1078_ret_164']
    },
    {
        "identifier": 'EVENT_1078_set_action_script_sync_162',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_7, 157]
    },
    {
        "identifier": 'EVENT_1078_pause_163',
        "command": 'pause',
        "args": [5]
    },
    {
        "identifier": 'EVENT_1078_ret_164',
        "command": 'ret'
    }
]
