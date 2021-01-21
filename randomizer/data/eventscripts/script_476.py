from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data import items
script = [
    {
        "identifier": 'EVENT_476_circle_mask_static_0',
        "command": 'circle_mask_static',
        "args": [AreaObjects.MARIO, 0, 3]
    },
    {
        "identifier": 'EVENT_476_pause_script_until_effect_done_1',
        "command": 'pause_script_until_effect_done'
    },
    {
        "identifier": 'EVENT_476_pause_action_script_2',
        "command": 'pause_action_script',
        "args": [AreaObjects.NPC_0]
    },
    {
        "identifier": 'EVENT_476_pause_action_script_3',
        "command": 'pause_action_script',
        "args": [AreaObjects.NPC_2]
    },
    {
        "identifier": 'EVENT_476_pause_action_script_4',
        "command": 'pause_action_script',
        "args": [AreaObjects.NPC_1]
    },
    {
        "identifier": 'EVENT_476_pause_action_script_5',
        "command": 'pause_action_script',
        "args": [AreaObjects.NPC_3]
    },
    {
        "identifier": 'EVENT_476_pause_action_script_6',
        "command": 'pause_action_script',
        "args": [AreaObjects.NPC_5]
    },
    {
        "identifier": 'EVENT_476_pause_action_script_7',
        "command": 'pause_action_script',
        "args": [AreaObjects.NPC_9]
    },
    {
        "identifier": 'EVENT_476_pause_action_script_8',
        "command": 'pause_action_script',
        "args": [AreaObjects.NPC_10]
    },
    {
        "identifier": 'EVENT_476_start_embedded_action_script_async_9',
        "command": 'start_embedded_action_script_async',
        "args": [AreaObjects.NPC_0],
        "subscript": [
            {
                "identifier": 'EVENT_476_start_embedded_action_script_async_9_SUBSCRIPT_transfer_to_xyzf_0',
                "command": 'transfer_to_xyzf',
                "args": [16, 77, 0, RadialDirections.EAST]
            },
            {
                "identifier": 'EVENT_476_start_embedded_action_script_async_9_SUBSCRIPT_face_northwest_1',
                "command": 'face_northwest'
            },
            {
                "identifier": 'EVENT_476_start_embedded_action_script_async_9_SUBSCRIPT_object_memory_set_bit_2',
                "command": 'object_memory_set_bit',
                "args": [0x30, [4]]
            }
        ]
    },
    {
        "identifier": 'EVENT_476_start_embedded_action_script_async_10',
        "command": 'start_embedded_action_script_async',
        "args": [AreaObjects.NPC_9],
        "subscript": [
            {
                "identifier": 'EVENT_476_start_embedded_action_script_async_10_SUBSCRIPT_transfer_to_xyzf_0',
                "command": 'transfer_to_xyzf',
                "args": [10, 81, 0, RadialDirections.EAST]
            },
            {
                "identifier": 'EVENT_476_start_embedded_action_script_async_10_SUBSCRIPT_face_southeast_1',
                "command": 'face_southeast'
            },
            {
                "identifier": 'EVENT_476_start_embedded_action_script_async_10_SUBSCRIPT_sequence_looping_off_2',
                "command": 'sequence_looping_off'
            }
        ]
    },
    {
        "identifier": 'EVENT_476_action_queue_sync_11',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_10],
        "subscript": [
            {
                "identifier": 'EVENT_476_action_queue_sync_11_SUBSCRIPT_transfer_to_xyzf_0',
                "command": 'transfer_to_xyzf',
                "args": [11, 83, 0, RadialDirections.EAST]
            },
            {
                "identifier": 'EVENT_476_action_queue_sync_11_SUBSCRIPT_face_northeast_1',
                "command": 'face_northeast'
            },
            {
                "identifier": 'EVENT_476_action_queue_sync_11_SUBSCRIPT_visibility_off_2',
                "command": 'visibility_off'
            }
        ]
    },
    {
        "identifier": 'EVENT_476_start_embedded_action_script_async_12',
        "command": 'start_embedded_action_script_async',
        "args": [AreaObjects.NPC_2],
        "subscript": [
            {
                "identifier": 'EVENT_476_start_embedded_action_script_async_12_SUBSCRIPT_transfer_to_xyzf_0',
                "command": 'transfer_to_xyzf',
                "args": [11, 75, 0, RadialDirections.EAST]
            },
            {
                "identifier": 'EVENT_476_start_embedded_action_script_async_12_SUBSCRIPT_object_memory_set_bit_1',
                "command": 'object_memory_set_bit',
                "args": [0x30, [4]]
            },
            {
                "identifier": 'EVENT_476_start_embedded_action_script_async_12_SUBSCRIPT_face_southeast_2',
                "command": 'face_southeast'
            }
        ]
    },
    {
        "identifier": 'EVENT_476_start_embedded_action_script_async_13',
        "command": 'start_embedded_action_script_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_476_start_embedded_action_script_async_13_SUBSCRIPT_transfer_to_xyzf_0',
                "command": 'transfer_to_xyzf',
                "args": [10, 81, 0, RadialDirections.EAST]
            },
            {
                "identifier": 'EVENT_476_start_embedded_action_script_async_13_SUBSCRIPT_set_sprite_sequence_1',
                "command": 'set_sprite_sequence',
                "args": [5, inc_sprite=6, flags=[_0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_476_start_embedded_action_script_async_14',
        "command": 'start_embedded_action_script_async',
        "args": [AreaObjects.NPC_1],
        "subscript": [
            {
                "identifier": 'EVENT_476_start_embedded_action_script_async_14_SUBSCRIPT_transfer_to_xyzf_0',
                "command": 'transfer_to_xyzf',
                "args": [20, 69, 0, RadialDirections.EAST]
            },
            {
                "identifier": 'EVENT_476_start_embedded_action_script_async_14_SUBSCRIPT_face_northwest_1',
                "command": 'face_northwest'
            }
        ]
    },
    {
        "identifier": 'EVENT_476_start_embedded_action_script_async_15',
        "command": 'start_embedded_action_script_async',
        "args": [AreaObjects.NPC_3],
        "subscript": [
            {
                "identifier": 'EVENT_476_start_embedded_action_script_async_15_SUBSCRIPT_transfer_to_xyzf_0',
                "command": 'transfer_to_xyzf',
                "args": [15, 67, 0, RadialDirections.EAST]
            },
            {
                "identifier": 'EVENT_476_start_embedded_action_script_async_15_SUBSCRIPT_face_southeast_1',
                "command": 'face_southeast'
            }
        ]
    },
    {
        "identifier": 'EVENT_476_start_embedded_action_script_async_16',
        "command": 'start_embedded_action_script_async',
        "args": [AreaObjects.NPC_5],
        "subscript": [
            {
                "identifier": 'EVENT_476_start_embedded_action_script_async_16_SUBSCRIPT_transfer_to_xyzf_0',
                "command": 'transfer_to_xyzf',
                "args": [19, 60, 0, RadialDirections.EAST]
            },
            {
                "identifier": 'EVENT_476_start_embedded_action_script_async_16_SUBSCRIPT_transfer_xyzf_pixels_1',
                "command": 'transfer_xyzf_pixels',
                "args": [8, 252, 0, RadialDirections.EAST]
            },
            {
                "identifier": 'EVENT_476_start_embedded_action_script_async_16_SUBSCRIPT_object_memory_set_bit_2',
                "command": 'object_memory_set_bit',
                "args": [0x30, [4]]
            },
            {
                "identifier": 'EVENT_476_start_embedded_action_script_async_16_SUBSCRIPT_face_southeast_3',
                "command": 'face_southeast'
            }
        ]
    },
    {
        "identifier": 'EVENT_476_remember_last_object_17',
        "command": 'remember_last_object'
    },
    {
        "identifier": 'EVENT_476_remove_from_current_level_18',
        "command": 'remove_from_current_level',
        "args": [AreaObjects.NPC_13]
    },
    {
        "identifier": 'EVENT_476_set_bit_19',
        "command": 'set_bit',
        "args": [0x7049, 6]
    },
    {
        "identifier": 'EVENT_476_run_event_as_subroutine_20',
        "command": 'run_event_as_subroutine',
        "args": [276]
    },
    {
        "identifier": 'EVENT_476_db_21',
        "command": 'db',
        "args": [0xfd, 0x8e, 0x40, 0x00, 0xb1]
    },
    {
        "identifier": 'EVENT_476_pause_script_until_effect_done_22',
        "command": 'pause_script_until_effect_done'
    },
    {
        "identifier": 'EVENT_476_fade_in_from_black_async_23',
        "command": 'fade_in_from_black_async'
    },
    {
        "identifier": 'EVENT_476_action_queue_async_24',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_8],
        "subscript": [
            {
                "identifier": 'EVENT_476_action_queue_async_24_SUBSCRIPT_shadow_off_0',
                "command": 'shadow_off'
            },
            {
                "identifier": 'EVENT_476_action_queue_async_24_SUBSCRIPT_transfer_to_xyzf_1',
                "command": 'transfer_to_xyzf',
                "args": [14, 75, 0, RadialDirections.EAST]
            },
            {
                "identifier": 'EVENT_476_action_queue_async_24_SUBSCRIPT_set_priority_2',
                "command": 'set_priority',
                "args": [3]
            },
            {
                "identifier": 'EVENT_476_action_queue_async_24_SUBSCRIPT_set_vram_priority_3',
                "command": 'set_vram_priority',
                "args": [VramPriority.OBJECT_OVERLAPS_MARIO_ON_ALL_SIDES]
            },
            {
                "identifier": 'EVENT_476_action_queue_async_24_SUBSCRIPT_set_animation_speed_4',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_476_action_queue_async_24_SUBSCRIPT_set_animation_speed_5',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_476_action_queue_async_24_SUBSCRIPT_set_sprite_sequence_6',
                "command": 'set_sprite_sequence',
                "args": [12, inc_sprite=0, flags=[_0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_476_action_queue_async_24_SUBSCRIPT_shift_west_steps_7',
                "command": 'shift_west_steps',
                "args": [3]
            },
            {
                "identifier": 'EVENT_476_action_queue_async_24_SUBSCRIPT_set_sprite_sequence_8',
                "command": 'set_sprite_sequence',
                "args": [10, inc_sprite=0, flags=[_0x08Flags.READ_AS_SEQUENCE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_476_play_sound_25',
        "command": 'play_sound',
        "args": [Sounds._087_CORRECT_SIGNAL, 6]
    },
    {
        "identifier": 'EVENT_476_run_dialog_26',
        "command": 'run_dialog',
        "args": [922, AreaObjects.NPC_14, [_0x60Flags.ASYNC, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_476_jmp_if_dialog_option_b_27',
        "command": 'jmp_if_dialog_option_b',
        "args": ['EVENT_476_clear_bit_183']
    },
    {
        "identifier": 'EVENT_476_pause_28',
        "command": 'pause',
        "args": [30]
    },
    {
        "identifier": 'EVENT_476_set_action_script_async_29',
        "command": 'set_action_script_async',
        "args": [AreaObjects.NPC_8, 636]
    },
    {
        "identifier": 'EVENT_476_pause_action_script_30',
        "command": 'pause_action_script',
        "args": [AreaObjects.NPC_8]
    },
    {
        "identifier": 'EVENT_476_unsync_dialog_31',
        "command": 'unsync_dialog'
    },
    {
        "identifier": 'EVENT_476_run_dialog_32',
        "command": 'run_dialog',
        "args": [2555, AreaObjects.NPC_14, [_0x60Flags.ASYNC, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_476_pause_33',
        "command": 'pause',
        "args": [10]
    },
    {
        "identifier": 'EVENT_476_set_action_script_async_34',
        "command": 'set_action_script_async',
        "args": [AreaObjects.NPC_9, 678]
    },
    {
        "identifier": 'EVENT_476_set_action_script_async_35',
        "command": 'set_action_script_async',
        "args": [AreaObjects.NPC_9, 678]
    },
    {
        "identifier": 'EVENT_476_action_queue_async_36',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_9],
        "subscript": [
            {
                "identifier": 'EVENT_476_action_queue_async_36_SUBSCRIPT_sequence_looping_off_0',
                "command": 'sequence_looping_off'
            }
        ]
    },
    {
        "identifier": 'EVENT_476_run_dialog_37',
        "command": 'run_dialog',
        "args": [2556, AreaObjects.NPC_14, [_0x60Flags.ASYNC, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_476_pause_38',
        "command": 'pause',
        "args": [10]
    },
    {
        "identifier": 'EVENT_476_set_action_script_async_39',
        "command": 'set_action_script_async',
        "args": [AreaObjects.NPC_9, 679]
    },
    {
        "identifier": 'EVENT_476_set_action_script_async_40',
        "command": 'set_action_script_async',
        "args": [AreaObjects.NPC_9, 679]
    },
    {
        "identifier": 'EVENT_476_action_queue_async_41',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_9],
        "subscript": [
            {
                "identifier": 'EVENT_476_action_queue_async_41_SUBSCRIPT_sequence_looping_off_0',
                "command": 'sequence_looping_off'
            }
        ]
    },
    {
        "identifier": 'EVENT_476_run_dialog_42',
        "command": 'run_dialog',
        "args": [2557, AreaObjects.NPC_14, [_0x60Flags.ASYNC, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_476_jmp_if_dialog_option_b_43',
        "command": 'jmp_if_dialog_option_b',
        "args": ['EVENT_476_run_dialog_45']
    },
    {
        "identifier": 'EVENT_476_jmp_44',
        "command": 'jmp',
        "args": ['EVENT_476_run_dialog_32']
    },
    {
        "identifier": 'EVENT_476_run_dialog_45',
        "command": 'run_dialog',
        "args": [924, AreaObjects.NPC_14, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_476_jmp_if_bit_set_46',
        "command": 'jmp_if_bit_set',
        "args": [0x7043, 2, 'EVENT_476_play_music_default_volume_49']
    },
    {
        "identifier": 'EVENT_476_fade_out_music_to_volume_47',
        "command": 'fade_out_music_to_volume',
        "args": [3, 0]
    },
    {
        "identifier": 'EVENT_476_pause_48',
        "command": 'pause',
        "args": [120]
    },
    {
        "identifier": 'EVENT_476_play_music_default_volume_49',
        "command": 'play_music_default_volume',
        "args": [Music._19_RACE_TRAINING]
    },
    {
        "identifier": 'EVENT_476_adjust_music_tempo_50',
        "command": 'adjust_music_tempo',
        "args": [MusicDirections.SLOW_DOWN, 2, 0]
    },
    {
        "identifier": 'EVENT_476_clear_bit_51',
        "command": 'clear_bit',
        "args": [0x7043, 2]
    },
    {
        "identifier": 'EVENT_476_clear_bit_52',
        "command": 'clear_bit',
        "args": [0x7043, 0]
    },
    {
        "identifier": 'EVENT_476_pause_53',
        "command": 'pause',
        "args": [1]
    },
    {
        "identifier": 'EVENT_476_jmp_if_audio_memory_equals_54',
        "command": 'jmp_if_audio_memory_equals',
        "args": [4, 'EVENT_476_pause_53']
    },
    {
        "identifier": 'EVENT_476_run_dialog_55',
        "command": 'run_dialog',
        "args": [925, AreaObjects.NPC_14, [_0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_476_set_action_script_sync_56',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_8, 636]
    },
    {
        "identifier": 'EVENT_476_pause_57',
        "command": 'pause',
        "args": [1]
    },
    {
        "identifier": 'EVENT_476_jmp_if_audio_memory_equals_58',
        "command": 'jmp_if_audio_memory_equals',
        "args": [5, 'EVENT_476_pause_57']
    },
    {
        "identifier": 'EVENT_476_run_dialog_59',
        "command": 'run_dialog',
        "args": [929, AreaObjects.NPC_14, [_0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_476_set_action_script_sync_60',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_8, 636]
    },
    {
        "identifier": 'EVENT_476_pause_61',
        "command": 'pause',
        "args": [1]
    },
    {
        "identifier": 'EVENT_476_jmp_if_audio_memory_equals_62',
        "command": 'jmp_if_audio_memory_equals',
        "args": [6, 'EVENT_476_pause_61']
    },
    {
        "identifier": 'EVENT_476_run_dialog_63',
        "command": 'run_dialog',
        "args": [925, AreaObjects.NPC_14, [_0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_476_set_action_script_sync_64',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_8, 636]
    },
    {
        "identifier": 'EVENT_476_pause_65',
        "command": 'pause',
        "args": [1]
    },
    {
        "identifier": 'EVENT_476_jmp_if_audio_memory_equals_66',
        "command": 'jmp_if_audio_memory_equals',
        "args": [7, 'EVENT_476_pause_65']
    },
    {
        "identifier": 'EVENT_476_run_dialog_67',
        "command": 'run_dialog',
        "args": [926, AreaObjects.NPC_14, [_0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_476_set_action_script_sync_68',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_8, 636]
    },
    {
        "identifier": 'EVENT_476_pause_69',
        "command": 'pause',
        "args": [1]
    },
    {
        "identifier": 'EVENT_476_jmp_if_audio_memory_equals_70',
        "command": 'jmp_if_audio_memory_equals',
        "args": [8, 'EVENT_476_pause_69']
    },
    {
        "identifier": 'EVENT_476_run_dialog_71',
        "command": 'run_dialog',
        "args": [925, AreaObjects.NPC_14, [_0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_476_set_action_script_sync_72',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_8, 636]
    },
    {
        "identifier": 'EVENT_476_pause_73',
        "command": 'pause',
        "args": [1]
    },
    {
        "identifier": 'EVENT_476_jmp_if_audio_memory_equals_74',
        "command": 'jmp_if_audio_memory_equals',
        "args": [9, 'EVENT_476_pause_73']
    },
    {
        "identifier": 'EVENT_476_run_dialog_75',
        "command": 'run_dialog',
        "args": [926, AreaObjects.NPC_14, [_0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_476_set_action_script_sync_76',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_8, 636]
    },
    {
        "identifier": 'EVENT_476_pause_77',
        "command": 'pause',
        "args": [1]
    },
    {
        "identifier": 'EVENT_476_jmp_if_audio_memory_equals_78',
        "command": 'jmp_if_audio_memory_equals',
        "args": [10, 'EVENT_476_pause_77']
    },
    {
        "identifier": 'EVENT_476_run_dialog_79',
        "command": 'run_dialog',
        "args": [927, AreaObjects.NPC_14, [_0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_476_set_action_script_sync_80',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_8, 636]
    },
    {
        "identifier": 'EVENT_476_pause_81',
        "command": 'pause',
        "args": [1]
    },
    {
        "identifier": 'EVENT_476_jmp_if_audio_memory_equals_82',
        "command": 'jmp_if_audio_memory_equals',
        "args": [11, 'EVENT_476_pause_81']
    },
    {
        "identifier": 'EVENT_476_run_dialog_83',
        "command": 'run_dialog',
        "args": [928, AreaObjects.NPC_14, [_0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_476_set_action_script_sync_84',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_8, 636]
    },
    {
        "identifier": 'EVENT_476_set_action_script_sync_85',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_9, 119]
    },
    {
        "identifier": 'EVENT_476_set_86',
        "command": 'set',
        "args": [0x70ae, 0]
    },
    {
        "identifier": 'EVENT_476_set_short_87',
        "command": 'set_short',
        "args": [0x7032, 0x0000]
    },
    {
        "identifier": 'EVENT_476_set_short_88',
        "command": 'set_short',
        "args": [0x7038, 0x0078]
    },
    {
        "identifier": 'EVENT_476_set_7000_to_tapped_button_89',
        "command": 'set_7000_to_tapped_button'
    },
    {
        "identifier": 'EVENT_476_pause_90',
        "command": 'pause',
        "args": [1]
    },
    {
        "identifier": 'EVENT_476_jmp_if_7000_any_bits_set_91',
        "command": 'jmp_if_7000_any_bits_set',
        "args": [[5], 'EVENT_476_clear_bit_130']
    },
    {
        "identifier": 'EVENT_476_jmp_if_7000_any_bits_set_92',
        "command": 'jmp_if_7000_any_bits_set',
        "args": [[7], 'EVENT_476_clear_bit_130']
    },
    {
        "identifier": 'EVENT_476_jmp_if_audio_memory_equals_93',
        "command": 'jmp_if_audio_memory_equals',
        "args": [1, 'EVENT_476_set_7000_to_tapped_button_89']
    },
    {
        "identifier": 'EVENT_476_jmp_if_bit_set_94',
        "command": 'jmp_if_bit_set',
        "args": [0x7043, 0, 'EVENT_476_clear_bit_99']
    },
    {
        "identifier": 'EVENT_476_set_bit_95',
        "command": 'set_bit',
        "args": [0x7043, 0]
    },
    {
        "identifier": 'EVENT_476_run_dialog_96',
        "command": 'run_dialog',
        "args": [947, AreaObjects.NPC_14, [_0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_476_set_action_script_sync_97',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_8, 636]
    },
    {
        "identifier": 'EVENT_476_jmp_98',
        "command": 'jmp',
        "args": ['EVENT_476_set_7000_to_tapped_button_102']
    },
    {
        "identifier": 'EVENT_476_clear_bit_99',
        "command": 'clear_bit',
        "args": [0x7043, 0]
    },
    {
        "identifier": 'EVENT_476_run_dialog_100',
        "command": 'run_dialog',
        "args": [948, AreaObjects.NPC_14, [_0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_476_set_action_script_sync_101',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_8, 636]
    },
    {
        "identifier": 'EVENT_476_set_7000_to_tapped_button_102',
        "command": 'set_7000_to_tapped_button'
    },
    {
        "identifier": 'EVENT_476_pause_103',
        "command": 'pause',
        "args": [1]
    },
    {
        "identifier": 'EVENT_476_jmp_if_7000_any_bits_set_104',
        "command": 'jmp_if_7000_any_bits_set',
        "args": [[5], 'EVENT_476_set_bit_144']
    },
    {
        "identifier": 'EVENT_476_jmp_if_7000_any_bits_set_105',
        "command": 'jmp_if_7000_any_bits_set',
        "args": [[7], 'EVENT_476_set_bit_148']
    },
    {
        "identifier": 'EVENT_476_jmp_if_audio_memory_equals_106',
        "command": 'jmp_if_audio_memory_equals',
        "args": [2, 'EVENT_476_set_7000_to_tapped_button_102']
    },
    {
        "identifier": 'EVENT_476_pause_107',
        "command": 'pause',
        "args": [1]
    },
    {
        "identifier": 'EVENT_476_jmp_if_7000_any_bits_set_108',
        "command": 'jmp_if_7000_any_bits_set',
        "args": [[5], 'EVENT_476_clear_bit_130']
    },
    {
        "identifier": 'EVENT_476_jmp_if_7000_any_bits_set_109',
        "command": 'jmp_if_7000_any_bits_set',
        "args": [[7], 'EVENT_476_clear_bit_130']
    },
    {
        "identifier": 'EVENT_476_jmp_if_audio_memory_equals_110',
        "command": 'jmp_if_audio_memory_equals',
        "args": [1, 'EVENT_476_pause_107']
    },
    {
        "identifier": 'EVENT_476_jmp_if_bit_clear_111',
        "command": 'jmp_if_bit_clear',
        "args": [0x7043, 0, 'EVENT_476_set_bit_116']
    },
    {
        "identifier": 'EVENT_476_clear_bit_112',
        "command": 'clear_bit',
        "args": [0x7043, 0]
    },
    {
        "identifier": 'EVENT_476_run_dialog_113',
        "command": 'run_dialog',
        "args": [948, AreaObjects.NPC_14, [_0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_476_set_action_script_sync_114',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_8, 636]
    },
    {
        "identifier": 'EVENT_476_jmp_115',
        "command": 'jmp',
        "args": ['EVENT_476_set_7000_to_tapped_button_119']
    },
    {
        "identifier": 'EVENT_476_set_bit_116',
        "command": 'set_bit',
        "args": [0x7043, 0]
    },
    {
        "identifier": 'EVENT_476_run_dialog_117',
        "command": 'run_dialog',
        "args": [947, AreaObjects.NPC_14, [_0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_476_set_action_script_sync_118',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_8, 636]
    },
    {
        "identifier": 'EVENT_476_set_7000_to_tapped_button_119',
        "command": 'set_7000_to_tapped_button'
    },
    {
        "identifier": 'EVENT_476_pause_120',
        "command": 'pause',
        "args": [1]
    },
    {
        "identifier": 'EVENT_476_jmp_if_7000_any_bits_set_121',
        "command": 'jmp_if_7000_any_bits_set',
        "args": [[5], 'EVENT_476_jmp_if_bit_set_134']
    },
    {
        "identifier": 'EVENT_476_jmp_if_7000_any_bits_set_122',
        "command": 'jmp_if_7000_any_bits_set',
        "args": [[7], 'EVENT_476_jmp_if_bit_set_139']
    },
    {
        "identifier": 'EVENT_476_jmp_if_audio_memory_equals_123',
        "command": 'jmp_if_audio_memory_equals',
        "args": [2, 'EVENT_476_set_7000_to_tapped_button_119']
    },
    {
        "identifier": 'EVENT_476_clear_bit_124',
        "command": 'clear_bit',
        "args": [0x704a, 0]
    },
    {
        "identifier": 'EVENT_476_clear_bit_125',
        "command": 'clear_bit',
        "args": [0x704a, 1]
    },
    {
        "identifier": 'EVENT_476_add_126',
        "command": 'add',
        "args": [0x70ae, 0x01]
    },
    {
        "identifier": 'EVENT_476_set_short_mem_127',
        "command": 'set_short_mem',
        "args": [0x7000, 0x70ae]
    },
    {
        "identifier": 'EVENT_476_jmp_if_var_equals_short_128',
        "command": 'jmp_if_var_equals_short',
        "args": [0x7000, 10, 'EVENT_476_fade_out_music_to_volume_172']
    },
    {
        "identifier": 'EVENT_476_jmp_129',
        "command": 'jmp',
        "args": ['EVENT_476_set_7000_to_tapped_button_89']
    },
    {
        "identifier": 'EVENT_476_clear_bit_130',
        "command": 'clear_bit',
        "args": [0x704a, 0]
    },
    {
        "identifier": 'EVENT_476_clear_bit_131',
        "command": 'clear_bit',
        "args": [0x704a, 1]
    },
    {
        "identifier": 'EVENT_476_set_short_132',
        "command": 'set_short',
        "args": [0x7032, 0x0000]
    },
    {
        "identifier": 'EVENT_476_jmp_133',
        "command": 'jmp',
        "args": ['EVENT_476_set_7000_to_tapped_button_89']
    },
    {
        "identifier": 'EVENT_476_jmp_if_bit_set_134',
        "command": 'jmp_if_bit_set',
        "args": [0x704a, 0, 'EVENT_476_set_short_152']
    },
    {
        "identifier": 'EVENT_476_jmp_if_bit_set_135',
        "command": 'jmp_if_bit_set',
        "args": [0x704a, 1, 'EVENT_476_set_bit_154']
    },
    {
        "identifier": 'EVENT_476_set_bit_136',
        "command": 'set_bit',
        "args": [0x704a, 0]
    },
    {
        "identifier": 'EVENT_476_clear_bit_137',
        "command": 'clear_bit',
        "args": [0x704a, 1]
    },
    {
        "identifier": 'EVENT_476_jmp_138',
        "command": 'jmp',
        "args": ['EVENT_476_set_7000_to_tapped_button_102']
    },
    {
        "identifier": 'EVENT_476_jmp_if_bit_set_139',
        "command": 'jmp_if_bit_set',
        "args": [0x704a, 1, 'EVENT_476_set_short_152']
    },
    {
        "identifier": 'EVENT_476_jmp_if_bit_set_140',
        "command": 'jmp_if_bit_set',
        "args": [0x704a, 0, 'EVENT_476_set_bit_161']
    },
    {
        "identifier": 'EVENT_476_set_bit_141',
        "command": 'set_bit',
        "args": [0x704a, 1]
    },
    {
        "identifier": 'EVENT_476_clear_bit_142',
        "command": 'clear_bit',
        "args": [0x704a, 0]
    },
    {
        "identifier": 'EVENT_476_jmp_143',
        "command": 'jmp',
        "args": ['EVENT_476_set_7000_to_tapped_button_102']
    },
    {
        "identifier": 'EVENT_476_set_bit_144',
        "command": 'set_bit',
        "args": [0x704a, 0]
    },
    {
        "identifier": 'EVENT_476_clear_bit_145',
        "command": 'clear_bit',
        "args": [0x704a, 1]
    },
    {
        "identifier": 'EVENT_476_set_action_script_sync_146',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_9, 678]
    },
    {
        "identifier": 'EVENT_476_jmp_147',
        "command": 'jmp',
        "args": ['EVENT_476_set_7000_to_tapped_button_102']
    },
    {
        "identifier": 'EVENT_476_set_bit_148',
        "command": 'set_bit',
        "args": [0x704a, 1]
    },
    {
        "identifier": 'EVENT_476_clear_bit_149',
        "command": 'clear_bit',
        "args": [0x704a, 0]
    },
    {
        "identifier": 'EVENT_476_set_action_script_sync_150',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_9, 678]
    },
    {
        "identifier": 'EVENT_476_jmp_151',
        "command": 'jmp',
        "args": ['EVENT_476_set_7000_to_tapped_button_102']
    },
    {
        "identifier": 'EVENT_476_set_short_152',
        "command": 'set_short',
        "args": [0x7032, 0x0000]
    },
    {
        "identifier": 'EVENT_476_jmp_153',
        "command": 'jmp',
        "args": ['EVENT_476_set_7000_to_tapped_button_102']
    },
    {
        "identifier": 'EVENT_476_set_bit_154',
        "command": 'set_bit',
        "args": [0x704a, 0]
    },
    {
        "identifier": 'EVENT_476_clear_bit_155',
        "command": 'clear_bit',
        "args": [0x704a, 1]
    },
    {
        "identifier": 'EVENT_476_add_short_156',
        "command": 'add_short',
        "args": [0x7032, 0x01]
    },
    {
        "identifier": 'EVENT_476_mem_compare_157',
        "command": 'mem_compare',
        "args": [0x7032, 4]
    },
    {
        "identifier": 'EVENT_476_jmp_if_comparison_result_is_greater_or_equal_158',
        "command": 'jmp_if_comparison_result_is_greater_or_equal',
        "args": ['EVENT_476_mem_compare_168']
    },
    {
        "identifier": 'EVENT_476_set_action_script_sync_159',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_9, 678]
    },
    {
        "identifier": 'EVENT_476_jmp_160',
        "command": 'jmp',
        "args": ['EVENT_476_set_7000_to_tapped_button_102']
    },
    {
        "identifier": 'EVENT_476_set_bit_161',
        "command": 'set_bit',
        "args": [0x704a, 1]
    },
    {
        "identifier": 'EVENT_476_clear_bit_162',
        "command": 'clear_bit',
        "args": [0x704a, 0]
    },
    {
        "identifier": 'EVENT_476_add_short_163',
        "command": 'add_short',
        "args": [0x7032, 0x01]
    },
    {
        "identifier": 'EVENT_476_mem_compare_164',
        "command": 'mem_compare',
        "args": [0x7032, 4]
    },
    {
        "identifier": 'EVENT_476_jmp_if_comparison_result_is_greater_or_equal_165',
        "command": 'jmp_if_comparison_result_is_greater_or_equal',
        "args": ['EVENT_476_mem_compare_168']
    },
    {
        "identifier": 'EVENT_476_set_action_script_sync_166',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_9, 678]
    },
    {
        "identifier": 'EVENT_476_jmp_167',
        "command": 'jmp',
        "args": ['EVENT_476_set_7000_to_tapped_button_102']
    },
    {
        "identifier": 'EVENT_476_mem_compare_168',
        "command": 'mem_compare',
        "args": [0x7032, 8]
    },
    {
        "identifier": 'EVENT_476_jmp_if_comparison_result_is_greater_or_equal_169',
        "command": 'jmp_if_comparison_result_is_greater_or_equal',
        "args": ['EVENT_476_fade_out_music_to_volume_172']
    },
    {
        "identifier": 'EVENT_476_set_action_script_sync_170',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_9, 679]
    },
    {
        "identifier": 'EVENT_476_jmp_171',
        "command": 'jmp',
        "args": ['EVENT_476_set_7000_to_tapped_button_102']
    },
    {
        "identifier": 'EVENT_476_fade_out_music_to_volume_172',
        "command": 'fade_out_music_to_volume',
        "args": [3, 0]
    },
    {
        "identifier": 'EVENT_476_pause_173',
        "command": 'pause',
        "args": [120]
    },
    {
        "identifier": 'EVENT_476_stop_music_174',
        "command": 'stop_music'
    },
    {
        "identifier": 'EVENT_476_mem_compare_175',
        "command": 'mem_compare',
        "args": [0x7032, 6]
    },
    {
        "identifier": 'EVENT_476_jmp_if_comparison_result_is_greater_or_equal_176',
        "command": 'jmp_if_comparison_result_is_greater_or_equal',
        "args": ['EVENT_476_run_dialog_182']
    },
    {
        "identifier": 'EVENT_476_jmp_if_var_equals_short_177',
        "command": 'jmp_if_var_equals_short',
        "args": [0x7032, 0, 'EVENT_476_set_bit_207']
    },
    {
        "identifier": 'EVENT_476_set_bit_178',
        "command": 'set_bit',
        "args": [0x7043, 2]
    },
    {
        "identifier": 'EVENT_476_run_dialog_179',
        "command": 'run_dialog',
        "args": [931, AreaObjects.NPC_14, [_0x60Flags.ASYNC, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_476_jmp_if_dialog_option_b_180',
        "command": 'jmp_if_dialog_option_b',
        "args": ['EVENT_476_clear_bit_183']
    },
    {
        "identifier": 'EVENT_476_jmp_181',
        "command": 'jmp',
        "args": ['EVENT_476_run_dialog_45']
    },
    {
        "identifier": 'EVENT_476_run_dialog_182',
        "command": 'run_dialog',
        "args": [932, AreaObjects.NPC_14, [_0x60Flags.ASYNC, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_476_clear_bit_183',
        "command": 'clear_bit',
        "args": [0x7043, 2]
    },
    {
        "identifier": 'EVENT_476_set_action_script_async_184',
        "command": 'set_action_script_async',
        "args": [AreaObjects.NPC_8, 636]
    },
    {
        "identifier": 'EVENT_476_run_dialog_185',
        "command": 'run_dialog',
        "args": [933, AreaObjects.NPC_14, [_0x60Flags.ASYNC, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_476_action_queue_async_186',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_8],
        "subscript": [
            {
                "identifier": 'EVENT_476_action_queue_async_186_SUBSCRIPT_set_sprite_sequence_0',
                "command": 'set_sprite_sequence',
                "args": [12, inc_sprite=0, flags=[_0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_476_action_queue_async_186_SUBSCRIPT_shift_east_steps_1',
                "command": 'shift_east_steps',
                "args": [3]
            },
            {
                "identifier": 'EVENT_476_action_queue_async_186_SUBSCRIPT_shift_east_pixels_2',
                "command": 'shift_east_pixels',
                "args": [16]
            },
            {
                "identifier": 'EVENT_476_action_queue_async_186_SUBSCRIPT_sequence_playback_off_3',
                "command": 'sequence_playback_off'
            },
            {
                "identifier": 'EVENT_476_action_queue_async_186_SUBSCRIPT_visibility_off_4',
                "command": 'visibility_off'
            }
        ]
    },
    {
        "identifier": 'EVENT_476_close_dialog_187',
        "command": 'close_dialog'
    },
    {
        "identifier": 'EVENT_476_jmp_if_bit_clear_188',
        "command": 'jmp_if_bit_clear',
        "args": [0x704c, 6, 'EVENT_476_db_190']
    },
    {
        "identifier": 'EVENT_476_summon_to_current_level_189',
        "command": 'summon_to_current_level',
        "args": [AreaObjects.NPC_13]
    },
    {
        "identifier": 'EVENT_476_db_190',
        "command": 'db',
        "args": [0xfd, 0x8e, 0xb2, 0x07, 0xb1]
    },
    {
        "identifier": 'EVENT_476_action_queue_sync_191',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_10],
        "subscript": [
            {
                "identifier": 'EVENT_476_action_queue_sync_191_SUBSCRIPT_face_northwest_0',
                "command": 'face_northwest'
            },
            {
                "identifier": 'EVENT_476_action_queue_sync_191_SUBSCRIPT_visibility_on_1',
                "command": 'visibility_on'
            }
        ]
    },
    {
        "identifier": 'EVENT_476_action_queue_sync_192',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_9],
        "subscript": [
            {
                "identifier": 'EVENT_476_action_queue_sync_192_SUBSCRIPT_face_southeast_0',
                "command": 'face_southeast'
            },
            {
                "identifier": 'EVENT_476_action_queue_sync_192_SUBSCRIPT_set_animation_speed_1',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.SLOW, [_0x10Flags.SEQUENCE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_476_action_queue_async_193',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_476_action_queue_async_193_SUBSCRIPT_set_sprite_sequence_0',
                "command": 'set_sprite_sequence',
                "args": [5, inc_sprite=6, flags=[_0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_476_pause_script_until_effect_done_194',
        "command": 'pause_script_until_effect_done'
    },
    {
        "identifier": 'EVENT_476_pause_195',
        "command": 'pause',
        "args": [30]
    },
    {
        "identifier": 'EVENT_476_play_sound_196',
        "command": 'play_sound',
        "args": [Sounds._062_BIG_YOSHI_TALK, 6]
    },
    {
        "identifier": 'EVENT_476_run_dialog_197',
        "command": 'run_dialog',
        "args": [908, AreaObjects.NPC_10, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]]
    },
    {
        "identifier": 'EVENT_476_pause_198',
        "command": 'pause',
        "args": [10]
    },
    {
        "identifier": 'EVENT_476_action_queue_sync_199',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_10],
        "subscript": [
            {
                "identifier": 'EVENT_476_action_queue_sync_199_SUBSCRIPT_face_northeast_0',
                "command": 'face_northeast'
            }
        ]
    },
    {
        "identifier": 'EVENT_476_action_queue_sync_200',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_476_action_queue_sync_200_SUBSCRIPT_set_sprite_sequence_0',
                "command": 'set_sprite_sequence',
                "args": [6, inc_sprite=6, flags=[_0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_476_action_queue_async_201',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_9],
        "subscript": [
            {
                "identifier": 'EVENT_476_action_queue_async_201_SUBSCRIPT_face_northeast_0',
                "command": 'face_northeast'
            }
        ]
    },
    {
        "identifier": 'EVENT_476_pause_202',
        "command": 'pause',
        "args": [60]
    },
    {
        "identifier": 'EVENT_476_jmp_to_subroutine_203',
        "command": 'jmp_to_subroutine',
        "args": [0x42a2]
    },
    {
        "identifier": 'EVENT_476_run_background_event_204',
        "command": 'run_background_event',
        "args": [465, [_0x40Flags.RETURN_ON_LEVEL_EXIT, _0x40Flags.BIT_7]]
    },
    {
        "identifier": 'EVENT_476_enable_controls_205',
        "command": 'enable_controls',
        "args": [[]]
    },
    {
        "identifier": 'EVENT_476_ret_206',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_476_set_bit_207',
        "command": 'set_bit',
        "args": [0x7043, 2]
    },
    {
        "identifier": 'EVENT_476_run_dialog_208',
        "command": 'run_dialog',
        "args": [930, AreaObjects.NPC_14, [_0x60Flags.ASYNC, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_476_jmp_if_dialog_option_b_209',
        "command": 'jmp_if_dialog_option_b',
        "args": ['EVENT_476_clear_bit_183']
    },
    {
        "identifier": 'EVENT_476_jmp_210',
        "command": 'jmp',
        "args": ['EVENT_476_run_dialog_45']
    }
]
