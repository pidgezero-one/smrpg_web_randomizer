from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
script = [
    {
        "identifier": 'EVENT_3640_jmp_if_bit_set_0',
        "command": 'jmp_if_bit_set',
        "args": [0x7092, 5, 'EVENT_3640_ret_370'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3640_fade_out_to_black_sync_duration_1',
        "command": 'fade_out_to_black_sync_duration',
        "args": [60],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3640_pause_script_until_effect_done_2',
        "command": 'pause_script_until_effect_done',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3640_remove_from_level_3',
        "command": 'remove_from_level',
        "args": [AreaObjects.NPC_6, Rooms._109_NIMBUS_CASTLE_AREA_01_ENTRANCE_HALL],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3640_clear_bit_4',
        "command": 'clear_bit',
        "args": [0x704c, 0],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3640_enter_area_5',
        "command": 'enter_area',
        "args": [Rooms._110_NIMBUS_CASTLE_AREA_18_DODOS_STATUEPOLISHING_ROOM, RadialDirections.NORTHEAST, 6, 68, 1, []],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3640_palette_set_6',
        "command": 'palette_set',
        "args": [111, 1],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3640_set_action_script_sync_7',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.MARIO, 395],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3640_action_queue_async_8',
        "command": 'action_queue_async',
        "args": [AreaObjects.SCREEN_FOCUS],
        "subscript": [
            {
                "identifier": 'EVENT_3640_action_queue_async_8_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_3640_action_queue_async_8_SUBSCRIPT_walk_to_xy_coords_1',
                "command": 'walk_to_xy_coords',
                "args": [1, 49]
            },
            {
                "identifier": 'EVENT_3640_action_queue_async_8_SUBSCRIPT_shift_northwest_steps_2',
                "command": 'shift_northwest_steps',
                "args": [1]
            },
            {
                "identifier": 'EVENT_3640_action_queue_async_8_SUBSCRIPT_shift_east_pixels_3',
                "command": 'shift_east_pixels',
                "args": [13]
            }
        ]
    },
    {
        "identifier": 'EVENT_3640_jmp_if_bit_set_9',
        "command": 'jmp_if_bit_set',
        "args": [0x705f, 4, 'EVENT_3640_action_queue_sync_18'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3640_jmp_10',
        "command": 'jmp',
        "args": ['EVENT_3640_action_queue_sync_12'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3640_ret_11',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3640_action_queue_sync_12',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_0],
        "subscript": [
            {
                "identifier": 'EVENT_3640_action_queue_sync_12_SUBSCRIPT_shift_southwest_pixels_0',
                "command": 'shift_southwest_pixels',
                "args": [3]
            },
            {
                "identifier": 'EVENT_3640_action_queue_sync_12_SUBSCRIPT_shift_northwest_pixels_1',
                "command": 'shift_northwest_pixels',
                "args": [3]
            },
            {
                "identifier": 'EVENT_3640_action_queue_sync_12_SUBSCRIPT_face_northeast_2',
                "command": 'face_northeast',
                "args": []
            }
        ]
    },
    {
        "identifier": 'EVENT_3640_action_queue_sync_13',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_1],
        "subscript": [
            {
                "identifier": 'EVENT_3640_action_queue_sync_13_SUBSCRIPT_shift_southwest_pixels_0',
                "command": 'shift_southwest_pixels',
                "args": [3]
            },
            {
                "identifier": 'EVENT_3640_action_queue_sync_13_SUBSCRIPT_shift_northwest_pixels_1',
                "command": 'shift_northwest_pixels',
                "args": [3]
            },
            {
                "identifier": 'EVENT_3640_action_queue_sync_13_SUBSCRIPT_face_northeast_2',
                "command": 'face_northeast',
                "args": []
            }
        ]
    },
    {
        "identifier": 'EVENT_3640_action_queue_async_14',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_2],
        "subscript": [
            {
                "identifier": 'EVENT_3640_action_queue_async_14_SUBSCRIPT_shift_southwest_pixels_0',
                "command": 'shift_southwest_pixels',
                "args": [3]
            },
            {
                "identifier": 'EVENT_3640_action_queue_async_14_SUBSCRIPT_shift_northwest_pixels_1',
                "command": 'shift_northwest_pixels',
                "args": [3]
            },
            {
                "identifier": 'EVENT_3640_action_queue_async_14_SUBSCRIPT_face_northeast_2',
                "command": 'face_northeast',
                "args": []
            }
        ]
    },
    {
        "identifier": 'EVENT_3640_fade_in_from_black_async_15',
        "command": 'fade_in_from_black_async',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3640_jmp_16',
        "command": 'jmp',
        "args": ['EVENT_3640_fade_out_music_to_volume_24'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3640_ret_17',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3640_action_queue_sync_18',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_0],
        "subscript": [
            {
                "identifier": 'EVENT_3640_action_queue_sync_18_SUBSCRIPT_shift_southwest_pixels_0',
                "command": 'shift_southwest_pixels',
                "args": [5]
            },
            {
                "identifier": 'EVENT_3640_action_queue_sync_18_SUBSCRIPT_shift_northwest_pixels_1',
                "command": 'shift_northwest_pixels',
                "args": [1]
            },
            {
                "identifier": 'EVENT_3640_action_queue_sync_18_SUBSCRIPT_set_sprite_sequence_2',
                "command": 'set_sprite_sequence',
                "args": [3, inc_sprite=0, flags=[_0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_3640_action_queue_sync_18_SUBSCRIPT_shadow_off_3',
                "command": 'shadow_off',
                "args": []
            }
        ]
    },
    {
        "identifier": 'EVENT_3640_action_queue_sync_19',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_1],
        "subscript": [
            {
                "identifier": 'EVENT_3640_action_queue_sync_19_SUBSCRIPT_shift_southwest_pixels_0',
                "command": 'shift_southwest_pixels',
                "args": [5]
            },
            {
                "identifier": 'EVENT_3640_action_queue_sync_19_SUBSCRIPT_shift_northwest_pixels_1',
                "command": 'shift_northwest_pixels',
                "args": [1]
            },
            {
                "identifier": 'EVENT_3640_action_queue_sync_19_SUBSCRIPT_set_sprite_sequence_2',
                "command": 'set_sprite_sequence',
                "args": [3, inc_sprite=0, flags=[_0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_3640_action_queue_sync_19_SUBSCRIPT_shadow_off_3',
                "command": 'shadow_off',
                "args": []
            }
        ]
    },
    {
        "identifier": 'EVENT_3640_action_queue_async_20',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_2],
        "subscript": [
            {
                "identifier": 'EVENT_3640_action_queue_async_20_SUBSCRIPT_shift_southwest_pixels_0',
                "command": 'shift_southwest_pixels',
                "args": [5]
            },
            {
                "identifier": 'EVENT_3640_action_queue_async_20_SUBSCRIPT_shift_northwest_pixels_1',
                "command": 'shift_northwest_pixels',
                "args": [1]
            },
            {
                "identifier": 'EVENT_3640_action_queue_async_20_SUBSCRIPT_set_sprite_sequence_2',
                "command": 'set_sprite_sequence',
                "args": [3, inc_sprite=0, flags=[_0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_3640_action_queue_async_20_SUBSCRIPT_shadow_off_3',
                "command": 'shadow_off',
                "args": []
            }
        ]
    },
    {
        "identifier": 'EVENT_3640_fade_in_from_black_async_21',
        "command": 'fade_in_from_black_async',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3640_jmp_22',
        "command": 'jmp',
        "args": ['EVENT_3640_fade_out_music_to_volume_24'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3640_ret_23',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3640_fade_out_music_to_volume_24',
        "command": 'fade_out_music_to_volume',
        "args": [0, 0],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3640_play_music_default_volume_25',
        "command": 'play_music_default_volume',
        "args": [Music._01_DODOS_COMING],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3640_stop_music_26',
        "command": 'stop_music',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3640_pause_27',
        "command": 'pause',
        "args": [30],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3640_enable_controls_until_return_28',
        "command": 'enable_controls_until_return',
        "args": [[]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3640_pause_29',
        "command": 'pause',
        "args": [1],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3640_pause_30',
        "command": 'pause',
        "args": [10],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3640_play_sound_31',
        "command": 'play_sound',
        "args": [Sounds._016_OPEN_DOOR, 6],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3640_pause_32',
        "command": 'pause',
        "args": [60],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3640_enable_controls_until_return_33',
        "command": 'enable_controls_until_return',
        "args": [[ControllerDirections.B]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3640_pause_34',
        "command": 'pause',
        "args": [1],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3640_play_music_default_volume_35',
        "command": 'play_music_default_volume',
        "args": [Music._01_DODOS_COMING],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3640_pause_36',
        "command": 'pause',
        "args": [143],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3640_pause_37',
        "command": 'pause',
        "args": [235],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3640_pause_38',
        "command": 'pause',
        "args": [118],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3640_action_queue_async_39',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_3],
        "subscript": [
            {
                "identifier": 'EVENT_3640_action_queue_async_39_SUBSCRIPT_shirt_to_xy_coords_0',
                "command": 'shirt_to_xy_coords',
                "args": [2, 56]
            },
            {
                "identifier": 'EVENT_3640_action_queue_async_39_SUBSCRIPT_shift_southwest_pixels_1',
                "command": 'shift_southwest_pixels',
                "args": [5]
            },
            {
                "identifier": 'EVENT_3640_action_queue_async_39_SUBSCRIPT_shift_southeast_pixels_2',
                "command": 'shift_southeast_pixels',
                "args": [16]
            },
            {
                "identifier": 'EVENT_3640_action_queue_async_39_SUBSCRIPT_sequence_playback_off_3',
                "command": 'sequence_playback_off',
                "args": []
            },
            {
                "identifier": 'EVENT_3640_action_queue_async_39_SUBSCRIPT_set_sprite_sequence_4',
                "command": 'set_sprite_sequence',
                "args": [0, inc_sprite=0, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_3640_action_queue_async_39_SUBSCRIPT_visibility_on_5',
                "command": 'visibility_on',
                "args": []
            },
            {
                "identifier": 'EVENT_3640_action_queue_async_39_SUBSCRIPT_pause_6',
                "command": 'pause',
                "args": [31]
            },
            {
                "identifier": 'EVENT_3640_action_queue_async_39_SUBSCRIPT_set_sprite_sequence_7',
                "command": 'set_sprite_sequence',
                "args": [5, inc_sprite=0, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_3640_action_queue_async_39_SUBSCRIPT_pause_8',
                "command": 'pause',
                "args": [31]
            },
            {
                "identifier": 'EVENT_3640_action_queue_async_39_SUBSCRIPT_set_animation_speed_9',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.SLOW, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3640_action_queue_async_39_SUBSCRIPT_sequence_playback_on_10',
                "command": 'sequence_playback_on',
                "args": []
            },
            {
                "identifier": 'EVENT_3640_action_queue_async_39_SUBSCRIPT_sequence_looping_on_11',
                "command": 'sequence_looping_on',
                "args": []
            },
            {
                "identifier": 'EVENT_3640_action_queue_async_39_SUBSCRIPT_set_sprite_sequence_12',
                "command": 'set_sprite_sequence',
                "args": [4, inc_sprite=0, flags=[_0x08Flags.LOOPING_OFF, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_3640_action_queue_async_39_SUBSCRIPT_pause_13',
                "command": 'pause',
                "args": [66]
            },
            {
                "identifier": 'EVENT_3640_action_queue_async_39_SUBSCRIPT_sequence_looping_off_14',
                "command": 'sequence_looping_off',
                "args": []
            },
            {
                "identifier": 'EVENT_3640_action_queue_async_39_SUBSCRIPT_set_sprite_sequence_15',
                "command": 'set_sprite_sequence',
                "args": [0, inc_sprite=0, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_3640_action_queue_async_39_SUBSCRIPT_pause_16',
                "command": 'pause',
                "args": [17]
            }
        ]
    },
    {
        "identifier": 'EVENT_3640_jmp_to_subroutine_40',
        "command": 'jmp_to_subroutine',
        "args": [0x946f],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3640_pause_41',
        "command": 'pause',
        "args": [13],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3640_jmp_to_subroutine_42',
        "command": 'jmp_to_subroutine',
        "args": [0x9480],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3640_pause_43',
        "command": 'pause',
        "args": [13],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3640_jmp_to_subroutine_44',
        "command": 'jmp_to_subroutine',
        "args": [0x946f],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3640_jmp_to_subroutine_45',
        "command": 'jmp_to_subroutine',
        "args": [0x9491],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3640_jmp_to_subroutine_46',
        "command": 'jmp_to_subroutine',
        "args": [0x94a8],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3640_pause_47',
        "command": 'pause',
        "args": [12],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3640_jmp_to_subroutine_48',
        "command": 'jmp_to_subroutine',
        "args": [0x946f],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3640_pause_49',
        "command": 'pause',
        "args": [13],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3640_jmp_to_subroutine_50',
        "command": 'jmp_to_subroutine',
        "args": [0x9480],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3640_pause_51',
        "command": 'pause',
        "args": [12],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3640_jmp_to_subroutine_52',
        "command": 'jmp_to_subroutine',
        "args": [0x946f],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3640_jmp_to_subroutine_53',
        "command": 'jmp_to_subroutine',
        "args": [0x9491],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3640_jmp_to_subroutine_54',
        "command": 'jmp_to_subroutine',
        "args": [0x94b6],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3640_pause_55',
        "command": 'pause',
        "args": [12],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3640_jmp_to_subroutine_56',
        "command": 'jmp_to_subroutine',
        "args": [0x946f],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3640_pause_57',
        "command": 'pause',
        "args": [13],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3640_jmp_to_subroutine_58',
        "command": 'jmp_to_subroutine',
        "args": [0x9480],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3640_pause_59',
        "command": 'pause',
        "args": [12],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3640_jmp_to_subroutine_60',
        "command": 'jmp_to_subroutine',
        "args": [0x946f],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3640_action_queue_async_61',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_3],
        "subscript": [
            {
                "identifier": 'EVENT_3640_action_queue_async_61_SUBSCRIPT_set_sprite_sequence_0',
                "command": 'set_sprite_sequence',
                "args": [0, inc_sprite=0, flags=[_0x08Flags.READ_AS_MOLD]]
            },
            {
                "identifier": 'EVENT_3640_action_queue_async_61_SUBSCRIPT_face_southwest_1',
                "command": 'face_southwest',
                "args": []
            }
        ]
    },
    {
        "identifier": 'EVENT_3640_set_short_62',
        "command": 'set_short',
        "args": [0x7000, 0x0000],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3640_clear_bit_63',
        "command": 'clear_bit',
        "args": [0x708a, 7],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3640_start_loop_n_times_64',
        "command": 'start_loop_n_times',
        "args": [18],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3640_pause_65',
        "command": 'pause',
        "args": [1],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3640_set_7000_to_tapped_button_66',
        "command": 'set_7000_to_tapped_button',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3640_jmp_if_7000_all_bits_clear_67',
        "command": 'jmp_if_7000_all_bits_clear',
        "args": [[7], 'EVENT_3640_end_loop_69'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3640_set_bit_68',
        "command": 'set_bit',
        "args": [0x708a, 7],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3640_end_loop_69',
        "command": 'end_loop',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3640_jmp_if_bit_set_70',
        "command": 'jmp_if_bit_set',
        "args": [0x708a, 7, 'EVENT_3640_stop_music_227'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3640_action_queue_sync_71',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_3],
        "subscript": [
            {
                "identifier": 'EVENT_3640_action_queue_sync_71_SUBSCRIPT_sequence_playback_on_0',
                "command": 'sequence_playback_on',
                "args": []
            },
            {
                "identifier": 'EVENT_3640_action_queue_sync_71_SUBSCRIPT_sequence_looping_on_1',
                "command": 'sequence_looping_on',
                "args": []
            },
            {
                "identifier": 'EVENT_3640_action_queue_sync_71_SUBSCRIPT_set_animation_speed_2',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3640_action_queue_sync_71_SUBSCRIPT_set_sprite_sequence_3',
                "command": 'set_sprite_sequence',
                "args": [3, inc_sprite=0, flags=[_0x08Flags.LOOPING_OFF, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3640_action_queue_sync_71_SUBSCRIPT_pause_4',
                "command": 'pause',
                "args": [20]
            },
            {
                "identifier": 'EVENT_3640_action_queue_sync_71_SUBSCRIPT_sequence_looping_off_5',
                "command": 'sequence_looping_off',
                "args": []
            }
        ]
    },
    {
        "identifier": 'EVENT_3640_clear_bit_72',
        "command": 'clear_bit',
        "args": [0x708a, 7],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3640_set_short_73',
        "command": 'set_short',
        "args": [0x7000, 0x0000],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3640_start_loop_n_times_74',
        "command": 'start_loop_n_times',
        "args": [22],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3640_pause_75',
        "command": 'pause',
        "args": [1],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3640_set_7000_to_tapped_button_76',
        "command": 'set_7000_to_tapped_button',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3640_jmp_if_7000_all_bits_clear_77',
        "command": 'jmp_if_7000_all_bits_clear',
        "args": [[7], 'EVENT_3640_end_loop_79'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3640_set_bit_78',
        "command": 'set_bit',
        "args": [0x708a, 7],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3640_end_loop_79',
        "command": 'end_loop',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3640_jmp_if_bit_clear_80',
        "command": 'jmp_if_bit_clear',
        "args": [0x708a, 7, 'EVENT_3640_stop_music_316'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3640_set_short_81',
        "command": 'set_short',
        "args": [0x7000, 0x0000],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3640_pause_82',
        "command": 'pause',
        "args": [17],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3640_jmp_to_subroutine_83',
        "command": 'jmp_to_subroutine',
        "args": [0x946f],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3640_pause_84',
        "command": 'pause',
        "args": [13],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3640_jmp_to_subroutine_85',
        "command": 'jmp_to_subroutine',
        "args": [0x9480],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3640_pause_86',
        "command": 'pause',
        "args": [12],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3640_jmp_to_subroutine_87',
        "command": 'jmp_to_subroutine',
        "args": [0x946f],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3640_pause_88',
        "command": 'pause',
        "args": [74],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3640_action_queue_async_89',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_3],
        "subscript": [
            {
                "identifier": 'EVENT_3640_action_queue_async_89_SUBSCRIPT_sequence_playback_on_0',
                "command": 'sequence_playback_on',
                "args": []
            },
            {
                "identifier": 'EVENT_3640_action_queue_async_89_SUBSCRIPT_set_animation_speed_1',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_3640_action_queue_async_89_SUBSCRIPT_set_animation_speed_2',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FASTER, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3640_action_queue_async_89_SUBSCRIPT_fixed_f_coord_on_3',
                "command": 'fixed_f_coord_on',
                "args": []
            },
            {
                "identifier": 'EVENT_3640_action_queue_async_89_SUBSCRIPT_set_sprite_sequence_4',
                "command": 'set_sprite_sequence',
                "args": [0, inc_sprite=0, flags=[_0x08Flags.LOOPING_OFF, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_3640_action_queue_async_89_SUBSCRIPT_shift_northwest_steps_5',
                "command": 'shift_northwest_steps',
                "args": [3]
            },
            {
                "identifier": 'EVENT_3640_action_queue_async_89_SUBSCRIPT_pause_6',
                "command": 'pause',
                "args": [25]
            },
            {
                "identifier": 'EVENT_3640_action_queue_async_89_SUBSCRIPT_face_southwest_7',
                "command": 'face_southwest',
                "args": []
            },
            {
                "identifier": 'EVENT_3640_action_queue_async_89_SUBSCRIPT_set_animation_speed_8',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FASTER, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_3640_action_queue_async_89_SUBSCRIPT_set_animation_speed_9',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3640_action_queue_async_89_SUBSCRIPT_set_sprite_sequence_10',
                "command": 'set_sprite_sequence',
                "args": [0, inc_sprite=0, flags=[_0x08Flags.READ_AS_MOLD]]
            },
            {
                "identifier": 'EVENT_3640_action_queue_async_89_SUBSCRIPT_pause_11',
                "command": 'pause',
                "args": [36]
            },
            {
                "identifier": 'EVENT_3640_action_queue_async_89_SUBSCRIPT_sequence_looping_on_12',
                "command": 'sequence_looping_on',
                "args": []
            },
            {
                "identifier": 'EVENT_3640_action_queue_async_89_SUBSCRIPT_start_loop_n_times_13',
                "command": 'start_loop_n_times',
                "args": [8]
            },
            {
                "identifier": 'EVENT_3640_action_queue_async_89_SUBSCRIPT_set_sprite_sequence_14',
                "command": 'set_sprite_sequence',
                "args": [5, inc_sprite=0, flags=[_0x08Flags.LOOPING_OFF]]
            },
            {
                "identifier": 'EVENT_3640_action_queue_async_89_SUBSCRIPT_pause_15',
                "command": 'pause',
                "args": [2]
            },
            {
                "identifier": 'EVENT_3640_action_queue_async_89_SUBSCRIPT_set_sprite_sequence_16',
                "command": 'set_sprite_sequence',
                "args": [0, inc_sprite=0, flags=[_0x08Flags.LOOPING_OFF]]
            },
            {
                "identifier": 'EVENT_3640_action_queue_async_89_SUBSCRIPT_pause_17',
                "command": 'pause',
                "args": [2]
            },
            {
                "identifier": 'EVENT_3640_action_queue_async_89_SUBSCRIPT_end_loop_18',
                "command": 'end_loop',
                "args": []
            },
            {
                "identifier": 'EVENT_3640_action_queue_async_89_SUBSCRIPT_set_sprite_sequence_19',
                "command": 'set_sprite_sequence',
                "args": [5, inc_sprite=0, flags=[_0x08Flags.LOOPING_OFF, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3640_action_queue_async_89_SUBSCRIPT_pause_20',
                "command": 'pause',
                "args": [50]
            },
            {
                "identifier": 'EVENT_3640_action_queue_async_89_SUBSCRIPT_set_sprite_sequence_21',
                "command": 'set_sprite_sequence',
                "args": [0, inc_sprite=0, flags=[_0x08Flags.READ_AS_MOLD]]
            },
            {
                "identifier": 'EVENT_3640_action_queue_async_89_SUBSCRIPT_sequence_looping_off_22',
                "command": 'sequence_looping_off',
                "args": []
            }
        ]
    },
    {
        "identifier": 'EVENT_3640_pause_90',
        "command": 'pause',
        "args": [5],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3640_set_short_91',
        "command": 'set_short',
        "args": [0x7024, 0x0000],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3640_set_short_92',
        "command": 'set_short',
        "args": [0x7000, 0x0000],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3640_clear_bit_93',
        "command": 'clear_bit',
        "args": [0x708a, 7],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3640_start_loop_n_times_94',
        "command": 'start_loop_n_times',
        "args": [17],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3640_pause_95',
        "command": 'pause',
        "args": [1],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3640_set_7000_to_tapped_button_96',
        "command": 'set_7000_to_tapped_button',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3640_jmp_if_7000_all_bits_clear_97',
        "command": 'jmp_if_7000_all_bits_clear',
        "args": [[7], 'EVENT_3640_end_loop_99'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3640_set_bit_98',
        "command": 'set_bit',
        "args": [0x708a, 7],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3640_end_loop_99',
        "command": 'end_loop',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3640_jmp_if_bit_set_100',
        "command": 'jmp_if_bit_set',
        "args": [0x708a, 7, 'EVENT_3640_stop_music_227'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3640_add_short_101',
        "command": 'add_short',
        "args": [0x7024, 0x01],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3640_jmp_if_var_not_equals_short_102',
        "command": 'jmp_if_var_not_equals_short',
        "args": [0x7024, 7, 'EVENT_3640_set_short_92'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3640_action_queue_async_103',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_3],
        "subscript": [
            {
                "identifier": 'EVENT_3640_action_queue_async_103_SUBSCRIPT_set_sprite_sequence_0',
                "command": 'set_sprite_sequence',
                "args": [0, inc_sprite=0, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_3640_action_queue_async_103_SUBSCRIPT_face_southeast_1',
                "command": 'face_southeast',
                "args": []
            }
        ]
    },
    {
        "identifier": 'EVENT_3640_pause_104',
        "command": 'pause',
        "args": [18],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3640_jmp_to_subroutine_105',
        "command": 'jmp_to_subroutine',
        "args": [0x946f],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3640_pause_106',
        "command": 'pause',
        "args": [13],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3640_jmp_to_subroutine_107',
        "command": 'jmp_to_subroutine',
        "args": [0x9480],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3640_pause_108',
        "command": 'pause',
        "args": [12],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3640_jmp_to_subroutine_109',
        "command": 'jmp_to_subroutine',
        "args": [0x946f],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3640_jmp_to_subroutine_110',
        "command": 'jmp_to_subroutine',
        "args": [0x9491],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3640_jmp_to_subroutine_111',
        "command": 'jmp_to_subroutine',
        "args": [0x953c],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3640_pause_112',
        "command": 'pause',
        "args": [12],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3640_jmp_to_subroutine_113',
        "command": 'jmp_to_subroutine',
        "args": [0x954a],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3640_pause_114',
        "command": 'pause',
        "args": [13],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3640_jmp_to_subroutine_115',
        "command": 'jmp_to_subroutine',
        "args": [0x955b],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3640_pause_116',
        "command": 'pause',
        "args": [12],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3640_jmp_to_subroutine_117',
        "command": 'jmp_to_subroutine',
        "args": [0x954a],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3640_action_queue_async_118',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_3],
        "subscript": [
            {
                "identifier": 'EVENT_3640_action_queue_async_118_SUBSCRIPT_set_sprite_sequence_0',
                "command": 'set_sprite_sequence',
                "args": [0, inc_sprite=0, flags=[_0x08Flags.READ_AS_MOLD]]
            },
            {
                "identifier": 'EVENT_3640_action_queue_async_118_SUBSCRIPT_face_southwest_1',
                "command": 'face_southwest',
                "args": []
            }
        ]
    },
    {
        "identifier": 'EVENT_3640_set_short_119',
        "command": 'set_short',
        "args": [0x7000, 0x0000],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3640_clear_bit_120',
        "command": 'clear_bit',
        "args": [0x708a, 7],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3640_start_loop_n_times_121',
        "command": 'start_loop_n_times',
        "args": [18],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3640_pause_122',
        "command": 'pause',
        "args": [1],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3640_set_7000_to_tapped_button_123',
        "command": 'set_7000_to_tapped_button',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3640_jmp_if_7000_all_bits_clear_124',
        "command": 'jmp_if_7000_all_bits_clear',
        "args": [[7], 'EVENT_3640_end_loop_126'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3640_set_bit_125',
        "command": 'set_bit',
        "args": [0x708a, 7],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3640_end_loop_126',
        "command": 'end_loop',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3640_jmp_if_bit_set_127',
        "command": 'jmp_if_bit_set',
        "args": [0x708a, 7, 'EVENT_3640_stop_music_227'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3640_action_queue_sync_128',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_3],
        "subscript": [
            {
                "identifier": 'EVENT_3640_action_queue_sync_128_SUBSCRIPT_sequence_playback_on_0',
                "command": 'sequence_playback_on',
                "args": []
            },
            {
                "identifier": 'EVENT_3640_action_queue_sync_128_SUBSCRIPT_sequence_looping_on_1',
                "command": 'sequence_looping_on',
                "args": []
            },
            {
                "identifier": 'EVENT_3640_action_queue_sync_128_SUBSCRIPT_set_animation_speed_2',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3640_action_queue_sync_128_SUBSCRIPT_set_sprite_sequence_3',
                "command": 'set_sprite_sequence',
                "args": [3, inc_sprite=0, flags=[_0x08Flags.LOOPING_OFF, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3640_action_queue_sync_128_SUBSCRIPT_pause_4',
                "command": 'pause',
                "args": [20]
            },
            {
                "identifier": 'EVENT_3640_action_queue_sync_128_SUBSCRIPT_sequence_looping_off_5',
                "command": 'sequence_looping_off',
                "args": []
            }
        ]
    },
    {
        "identifier": 'EVENT_3640_clear_bit_129',
        "command": 'clear_bit',
        "args": [0x708a, 7],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3640_set_short_130',
        "command": 'set_short',
        "args": [0x7000, 0x0000],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3640_start_loop_n_times_131',
        "command": 'start_loop_n_times',
        "args": [22],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3640_pause_132',
        "command": 'pause',
        "args": [1],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3640_set_7000_to_tapped_button_133',
        "command": 'set_7000_to_tapped_button',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3640_jmp_if_7000_all_bits_clear_134',
        "command": 'jmp_if_7000_all_bits_clear',
        "args": [[7], 'EVENT_3640_end_loop_136'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3640_set_bit_135',
        "command": 'set_bit',
        "args": [0x708a, 7],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3640_end_loop_136',
        "command": 'end_loop',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3640_jmp_if_bit_clear_137',
        "command": 'jmp_if_bit_clear',
        "args": [0x708a, 7, 'EVENT_3640_stop_music_316'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3640_set_short_138',
        "command": 'set_short',
        "args": [0x7000, 0x0000],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3640_pause_139',
        "command": 'pause',
        "args": [18],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3640_jmp_to_subroutine_140',
        "command": 'jmp_to_subroutine',
        "args": [0x955b],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3640_pause_141',
        "command": 'pause',
        "args": [13],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3640_jmp_to_subroutine_142',
        "command": 'jmp_to_subroutine',
        "args": [0x954a],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3640_pause_143',
        "command": 'pause',
        "args": [13],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3640_jmp_to_subroutine_144',
        "command": 'jmp_to_subroutine',
        "args": [0x955b],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3640_jmp_to_subroutine_145',
        "command": 'jmp_to_subroutine',
        "args": [0x9491],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3640_jmp_to_subroutine_146',
        "command": 'jmp_to_subroutine',
        "args": [0x94b6],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3640_action_queue_async_147',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_3],
        "subscript": [
            {
                "identifier": 'EVENT_3640_action_queue_async_147_SUBSCRIPT_set_sprite_sequence_0',
                "command": 'set_sprite_sequence',
                "args": [0, inc_sprite=0, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3640_action_queue_async_147_SUBSCRIPT_pause_1',
                "command": 'pause',
                "args": [23]
            },
            {
                "identifier": 'EVENT_3640_action_queue_async_147_SUBSCRIPT_set_sprite_sequence_2',
                "command": 'set_sprite_sequence',
                "args": [0, inc_sprite=0, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_3640_action_queue_async_147_SUBSCRIPT_pause_3',
                "command": 'pause',
                "args": [45]
            },
            {
                "identifier": 'EVENT_3640_action_queue_async_147_SUBSCRIPT_set_sprite_sequence_4',
                "command": 'set_sprite_sequence',
                "args": [0, inc_sprite=0, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3640_action_queue_async_147_SUBSCRIPT_pause_5',
                "command": 'pause',
                "args": [45]
            },
            {
                "identifier": 'EVENT_3640_action_queue_async_147_SUBSCRIPT_set_animation_speed_6',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_3640_action_queue_async_147_SUBSCRIPT_set_animation_speed_7',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3640_action_queue_async_147_SUBSCRIPT_set_sprite_sequence_8',
                "command": 'set_sprite_sequence',
                "args": [0, inc_sprite=0, flags=[_0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_3640_action_queue_async_147_SUBSCRIPT_shift_southeast_steps_9',
                "command": 'shift_southeast_steps',
                "args": [3]
            },
            {
                "identifier": 'EVENT_3640_action_queue_async_147_SUBSCRIPT_ret_10',
                "command": 'ret',
                "args": []
            }
        ]
    },
    {
        "identifier": 'EVENT_3640_action_queue_async_148',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_3],
        "subscript": [
            {
                "identifier": 'EVENT_3640_action_queue_async_148_SUBSCRIPT_set_sprite_sequence_0',
                "command": 'set_sprite_sequence',
                "args": [0, inc_sprite=0, flags=[_0x08Flags.READ_AS_MOLD]]
            },
            {
                "identifier": 'EVENT_3640_action_queue_async_148_SUBSCRIPT_face_southwest_1',
                "command": 'face_southwest',
                "args": []
            }
        ]
    },
    {
        "identifier": 'EVENT_3640_set_short_149',
        "command": 'set_short',
        "args": [0x7000, 0x0000],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3640_clear_bit_150',
        "command": 'clear_bit',
        "args": [0x708a, 7],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3640_start_loop_n_times_151',
        "command": 'start_loop_n_times',
        "args": [3],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3640_pause_152',
        "command": 'pause',
        "args": [1],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3640_set_7000_to_tapped_button_153',
        "command": 'set_7000_to_tapped_button',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3640_jmp_if_7000_all_bits_clear_154',
        "command": 'jmp_if_7000_all_bits_clear',
        "args": [[7], 'EVENT_3640_end_loop_156'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3640_set_bit_155',
        "command": 'set_bit',
        "args": [0x708a, 7],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3640_end_loop_156',
        "command": 'end_loop',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3640_jmp_if_bit_set_157',
        "command": 'jmp_if_bit_set',
        "args": [0x708a, 7, 'EVENT_3640_stop_music_227'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3640_action_queue_sync_158',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_3],
        "subscript": [
            {
                "identifier": 'EVENT_3640_action_queue_sync_158_SUBSCRIPT_sequence_playback_on_0',
                "command": 'sequence_playback_on',
                "args": []
            },
            {
                "identifier": 'EVENT_3640_action_queue_sync_158_SUBSCRIPT_sequence_looping_on_1',
                "command": 'sequence_looping_on',
                "args": []
            },
            {
                "identifier": 'EVENT_3640_action_queue_sync_158_SUBSCRIPT_set_animation_speed_2',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3640_action_queue_sync_158_SUBSCRIPT_set_sprite_sequence_3',
                "command": 'set_sprite_sequence',
                "args": [3, inc_sprite=0, flags=[_0x08Flags.LOOPING_OFF, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3640_action_queue_sync_158_SUBSCRIPT_pause_4',
                "command": 'pause',
                "args": [20]
            },
            {
                "identifier": 'EVENT_3640_action_queue_sync_158_SUBSCRIPT_sequence_looping_off_5',
                "command": 'sequence_looping_off',
                "args": []
            }
        ]
    },
    {
        "identifier": 'EVENT_3640_clear_bit_159',
        "command": 'clear_bit',
        "args": [0x708a, 7],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3640_set_short_160',
        "command": 'set_short',
        "args": [0x7000, 0x0000],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3640_start_loop_n_times_161',
        "command": 'start_loop_n_times',
        "args": [22],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3640_pause_162',
        "command": 'pause',
        "args": [1],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3640_set_7000_to_tapped_button_163',
        "command": 'set_7000_to_tapped_button',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3640_jmp_if_7000_all_bits_clear_164',
        "command": 'jmp_if_7000_all_bits_clear',
        "args": [[7], 'EVENT_3640_end_loop_166'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3640_set_bit_165',
        "command": 'set_bit',
        "args": [0x708a, 7],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3640_end_loop_166',
        "command": 'end_loop',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3640_jmp_if_bit_clear_167',
        "command": 'jmp_if_bit_clear',
        "args": [0x708a, 7, 'EVENT_3640_stop_music_316'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3640_set_short_168',
        "command": 'set_short',
        "args": [0x7000, 0x0000],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3640_pause_169',
        "command": 'pause',
        "args": [17],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3640_jmp_to_subroutine_170',
        "command": 'jmp_to_subroutine',
        "args": [0x946f],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3640_pause_171',
        "command": 'pause',
        "args": [13],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3640_jmp_to_subroutine_172',
        "command": 'jmp_to_subroutine',
        "args": [0x9480],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3640_pause_173',
        "command": 'pause',
        "args": [13],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3640_jmp_to_subroutine_174',
        "command": 'jmp_to_subroutine',
        "args": [0x946f],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3640_jmp_to_subroutine_175',
        "command": 'jmp_to_subroutine',
        "args": [0x9491],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3640_jmp_to_subroutine_176',
        "command": 'jmp_to_subroutine',
        "args": [0x953c],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3640_pause_177',
        "command": 'pause',
        "args": [12],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3640_jmp_to_subroutine_178',
        "command": 'jmp_to_subroutine',
        "args": [0x954a],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3640_pause_179',
        "command": 'pause',
        "args": [13],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3640_jmp_to_subroutine_180',
        "command": 'jmp_to_subroutine',
        "args": [0x955b],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3640_pause_181',
        "command": 'pause',
        "args": [12],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3640_jmp_to_subroutine_182',
        "command": 'jmp_to_subroutine',
        "args": [0x954a],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3640_action_queue_async_183',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_3],
        "subscript": [
            {
                "identifier": 'EVENT_3640_action_queue_async_183_SUBSCRIPT_set_sprite_sequence_0',
                "command": 'set_sprite_sequence',
                "args": [0, inc_sprite=0, flags=[_0x08Flags.READ_AS_MOLD]]
            },
            {
                "identifier": 'EVENT_3640_action_queue_async_183_SUBSCRIPT_sequence_playback_on_1',
                "command": 'sequence_playback_on',
                "args": []
            },
            {
                "identifier": 'EVENT_3640_action_queue_async_183_SUBSCRIPT_face_southwest_2',
                "command": 'face_southwest',
                "args": []
            },
            {
                "identifier": 'EVENT_3640_action_queue_async_183_SUBSCRIPT_pause_3',
                "command": 'pause',
                "args": [16]
            },
            {
                "identifier": 'EVENT_3640_action_queue_async_183_SUBSCRIPT_sequence_looping_on_4',
                "command": 'sequence_looping_on',
                "args": []
            },
            {
                "identifier": 'EVENT_3640_action_queue_async_183_SUBSCRIPT_set_animation_speed_5',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3640_action_queue_async_183_SUBSCRIPT_set_sprite_sequence_6',
                "command": 'set_sprite_sequence',
                "args": [3, inc_sprite=0, flags=[_0x08Flags.LOOPING_OFF, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3640_action_queue_async_183_SUBSCRIPT_pause_7',
                "command": 'pause',
                "args": [9]
            },
            {
                "identifier": 'EVENT_3640_action_queue_async_183_SUBSCRIPT_sequence_playback_off_8',
                "command": 'sequence_playback_off',
                "args": []
            },
            {
                "identifier": 'EVENT_3640_action_queue_async_183_SUBSCRIPT_pause_9',
                "command": 'pause',
                "args": [8]
            },
            {
                "identifier": 'EVENT_3640_action_queue_async_183_SUBSCRIPT_sequence_looping_off_10',
                "command": 'sequence_looping_off',
                "args": []
            },
            {
                "identifier": 'EVENT_3640_action_queue_async_183_SUBSCRIPT_face_northwest_11',
                "command": 'face_northwest',
                "args": []
            },
            {
                "identifier": 'EVENT_3640_action_queue_async_183_SUBSCRIPT_set_sprite_sequence_12',
                "command": 'set_sprite_sequence',
                "args": [4, inc_sprite=0, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_3640_action_queue_async_183_SUBSCRIPT_pause_13',
                "command": 'pause',
                "args": [45]
            },
            {
                "identifier": 'EVENT_3640_action_queue_async_183_SUBSCRIPT_set_animation_speed_14',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_3640_action_queue_async_183_SUBSCRIPT_set_animation_speed_15',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3640_action_queue_async_183_SUBSCRIPT_sequence_playback_on_16',
                "command": 'sequence_playback_on',
                "args": []
            },
            {
                "identifier": 'EVENT_3640_action_queue_async_183_SUBSCRIPT_pause_17',
                "command": 'pause',
                "args": [20]
            },
            {
                "identifier": 'EVENT_3640_action_queue_async_183_SUBSCRIPT_set_sprite_sequence_18',
                "command": 'set_sprite_sequence',
                "args": [1, inc_sprite=0, flags=[_0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_3640_action_queue_async_183_SUBSCRIPT_shift_northwest_steps_19',
                "command": 'shift_northwest_steps',
                "args": [9]
            },
            {
                "identifier": 'EVENT_3640_action_queue_async_183_SUBSCRIPT_set_animation_speed_20',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_3640_action_queue_async_183_SUBSCRIPT_set_animation_speed_21',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3640_action_queue_async_183_SUBSCRIPT_shift_northwest_steps_22',
                "command": 'shift_northwest_steps',
                "args": [3]
            },
            {
                "identifier": 'EVENT_3640_action_queue_async_183_SUBSCRIPT_visibility_off_23',
                "command": 'visibility_off',
                "args": []
            },
            {
                "identifier": 'EVENT_3640_action_queue_async_183_SUBSCRIPT_sequence_looping_off_24',
                "command": 'sequence_looping_off',
                "args": []
            },
            {
                "identifier": 'EVENT_3640_action_queue_async_183_SUBSCRIPT_pause_25',
                "command": 'pause',
                "args": [9]
            },
            {
                "identifier": 'EVENT_3640_action_queue_async_183_SUBSCRIPT_clear_solidity_bits_26',
                "command": 'clear_solidity_bits',
                "args": [[_0x0AFlags.CANT_PASS_WALLS]]
            },
            {
                "identifier": 'EVENT_3640_action_queue_async_183_SUBSCRIPT_pause_27',
                "command": 'pause',
                "args": [38]
            },
            {
                "identifier": 'EVENT_3640_action_queue_async_183_SUBSCRIPT_shirt_to_xy_coords_28',
                "command": 'shirt_to_xy_coords',
                "args": [127, 66]
            },
            {
                "identifier": 'EVENT_3640_action_queue_async_183_SUBSCRIPT_visibility_on_29',
                "command": 'visibility_on',
                "args": []
            },
            {
                "identifier": 'EVENT_3640_action_queue_async_183_SUBSCRIPT_set_sprite_sequence_30',
                "command": 'set_sprite_sequence',
                "args": [0, inc_sprite=0, flags=[_0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_3640_action_queue_async_183_SUBSCRIPT_shift_southeast_steps_31',
                "command": 'shift_southeast_steps',
                "args": [14]
            },
            {
                "identifier": 'EVENT_3640_action_queue_async_183_SUBSCRIPT_pause_32',
                "command": 'pause',
                "args": [20]
            },
            {
                "identifier": 'EVENT_3640_action_queue_async_183_SUBSCRIPT_shirt_to_xy_coords_33',
                "command": 'shirt_to_xy_coords',
                "args": [11, 75]
            },
            {
                "identifier": 'EVENT_3640_action_queue_async_183_SUBSCRIPT_shift_southwest_pixels_34',
                "command": 'shift_southwest_pixels',
                "args": [5]
            },
            {
                "identifier": 'EVENT_3640_action_queue_async_183_SUBSCRIPT_set_sprite_sequence_35',
                "command": 'set_sprite_sequence',
                "args": [1, inc_sprite=0, flags=[_0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_3640_action_queue_async_183_SUBSCRIPT_face_northwest_36',
                "command": 'face_northwest',
                "args": []
            },
            {
                "identifier": 'EVENT_3640_action_queue_async_183_SUBSCRIPT_visibility_on_37',
                "command": 'visibility_on',
                "args": []
            },
            {
                "identifier": 'EVENT_3640_action_queue_async_183_SUBSCRIPT_shift_northwest_steps_38',
                "command": 'shift_northwest_steps',
                "args": [9]
            },
            {
                "identifier": 'EVENT_3640_action_queue_async_183_SUBSCRIPT_face_southwest_39',
                "command": 'face_southwest',
                "args": []
            },
            {
                "identifier": 'EVENT_3640_action_queue_async_183_SUBSCRIPT_set_sprite_sequence_40',
                "command": 'set_sprite_sequence',
                "args": [0, inc_sprite=0, flags=[]]
            },
            {
                "identifier": 'EVENT_3640_action_queue_async_183_SUBSCRIPT_sequence_looping_off_41',
                "command": 'sequence_looping_off',
                "args": []
            }
        ]
    },
    {
        "identifier": 'EVENT_3640_pause_184',
        "command": 'pause',
        "args": [25],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3640_action_queue_sync_185',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_3],
        "subscript": [
            {
                "identifier": 'EVENT_3640_action_queue_sync_185_SUBSCRIPT_sequence_playback_on_0',
                "command": 'sequence_playback_on',
                "args": []
            },
            {
                "identifier": 'EVENT_3640_action_queue_sync_185_SUBSCRIPT_sequence_looping_on_1',
                "command": 'sequence_looping_on',
                "args": []
            },
            {
                "identifier": 'EVENT_3640_action_queue_sync_185_SUBSCRIPT_set_animation_speed_2',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3640_action_queue_sync_185_SUBSCRIPT_set_sprite_sequence_3',
                "command": 'set_sprite_sequence',
                "args": [3, inc_sprite=0, flags=[_0x08Flags.LOOPING_OFF, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3640_action_queue_sync_185_SUBSCRIPT_pause_4',
                "command": 'pause',
                "args": [20]
            },
            {
                "identifier": 'EVENT_3640_action_queue_sync_185_SUBSCRIPT_sequence_looping_off_5',
                "command": 'sequence_looping_off',
                "args": []
            }
        ]
    },
    {
        "identifier": 'EVENT_3640_clear_bit_186',
        "command": 'clear_bit',
        "args": [0x708a, 7],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3640_set_short_187',
        "command": 'set_short',
        "args": [0x7000, 0x0000],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3640_start_loop_n_times_188',
        "command": 'start_loop_n_times',
        "args": [22],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3640_pause_189',
        "command": 'pause',
        "args": [1],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3640_set_7000_to_tapped_button_190',
        "command": 'set_7000_to_tapped_button',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3640_jmp_if_7000_all_bits_clear_191',
        "command": 'jmp_if_7000_all_bits_clear',
        "args": [[7], 'EVENT_3640_end_loop_193'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3640_set_bit_192',
        "command": 'set_bit',
        "args": [0x708a, 7],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3640_end_loop_193',
        "command": 'end_loop',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3640_jmp_if_bit_clear_194',
        "command": 'jmp_if_bit_clear',
        "args": [0x708a, 7, 'EVENT_3640_stop_music_316'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3640_set_short_195',
        "command": 'set_short',
        "args": [0x7000, 0x0000],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3640_pause_196',
        "command": 'pause',
        "args": [30],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3640_enable_controls_until_return_197',
        "command": 'enable_controls_until_return',
        "args": [[]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3640_clear_bit_198',
        "command": 'clear_bit',
        "args": [0x7043, 0],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3640_clear_bit_199',
        "command": 'clear_bit',
        "args": [0x7043, 1],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3640_action_queue_async_200',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_3],
        "subscript": [
            {
                "identifier": 'EVENT_3640_action_queue_async_200_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.SLOW, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3640_action_queue_async_200_SUBSCRIPT_set_sprite_sequence_1',
                "command": 'set_sprite_sequence',
                "args": [6, inc_sprite=0, flags=[_0x08Flags.LOOPING_OFF, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3640_action_queue_async_200_SUBSCRIPT_pause_2',
                "command": 'pause',
                "args": [90]
            },
            {
                "identifier": 'EVENT_3640_action_queue_async_200_SUBSCRIPT_sequence_looping_off_3',
                "command": 'sequence_looping_off',
                "args": []
            }
        ]
    },
    {
        "identifier": 'EVENT_3640_pause_201',
        "command": 'pause',
        "args": [20],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3640_action_queue_async_202',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_3],
        "subscript": [
            {
                "identifier": 'EVENT_3640_action_queue_async_202_SUBSCRIPT_fixed_f_coord_off_0',
                "command": 'fixed_f_coord_off',
                "args": []
            },
            {
                "identifier": 'EVENT_3640_action_queue_async_202_SUBSCRIPT_face_northwest_1',
                "command": 'face_northwest',
                "args": []
            },
            {
                "identifier": 'EVENT_3640_action_queue_async_202_SUBSCRIPT_set_sprite_sequence_2',
                "command": 'set_sprite_sequence',
                "args": [1, inc_sprite=0, flags=[_0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_3640_action_queue_async_202_SUBSCRIPT_set_animation_speed_3',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING, _0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3640_action_queue_async_202_SUBSCRIPT_shift_northwest_steps_4',
                "command": 'shift_northwest_steps',
                "args": [11]
            },
            {
                "identifier": 'EVENT_3640_action_queue_async_202_SUBSCRIPT_visibility_off_5',
                "command": 'visibility_off',
                "args": []
            },
            {
                "identifier": 'EVENT_3640_action_queue_async_202_SUBSCRIPT_sequence_looping_off_6',
                "command": 'sequence_looping_off',
                "args": []
            },
            {
                "identifier": 'EVENT_3640_action_queue_async_202_SUBSCRIPT_stop_sound_7',
                "command": 'stop_sound',
                "args": []
            }
        ]
    },
    {
        "identifier": 'EVENT_3640_set_bit_203',
        "command": 'set_bit',
        "args": [0x7092, 7],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3640_stop_sound_204',
        "command": 'stop_sound',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3640_stop_sound_205',
        "command": 'stop_sound',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3640_stop_sound_206',
        "command": 'stop_sound',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3640_stop_sound_207',
        "command": 'stop_sound',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3640_stop_sound_208',
        "command": 'stop_sound',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3640_stop_sound_209',
        "command": 'stop_sound',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3640_pause_210',
        "command": 'pause',
        "args": [60],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3640_play_sound_211',
        "command": 'play_sound',
        "args": [Sounds._000_SILENCE, 6],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3640_pause_212',
        "command": 'pause',
        "args": [30],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3640_action_queue_async_213',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_3640_action_queue_async_213_SUBSCRIPT_jump_to_height_0',
                "command": 'jump_to_height',
                "args": [96]
            },
            {
                "identifier": 'EVENT_3640_action_queue_async_213_SUBSCRIPT_shift_northeast_steps_1',
                "command": 'shift_northeast_steps',
                "args": [2]
            },
            {
                "identifier": 'EVENT_3640_action_queue_async_213_SUBSCRIPT_face_south_2',
                "command": 'face_south',
                "args": []
            },
            {
                "identifier": 'EVENT_3640_action_queue_async_213_SUBSCRIPT_set_sprite_sequence_3',
                "command": 'set_sprite_sequence',
                "args": [10, inc_sprite=2, flags=[_0x08Flags.LOOPING_OFF, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3640_action_queue_async_213_SUBSCRIPT_pause_4',
                "command": 'pause',
                "args": [60]
            }
        ]
    },
    {
        "identifier": 'EVENT_3640_set_action_script_async_214',
        "command": 'set_action_script_async',
        "args": [AreaObjects.MARIO, 395],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3640_set_bit_215',
        "command": 'set_bit',
        "args": [0x7092, 5],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3640_remove_from_level_216',
        "command": 'remove_from_level',
        "args": [AreaObjects.NPC_1, Rooms._112_NIMBUS_CASTLE_AREA_17_RIGHT_OF_4WAY_PATH_SAVE_POINT],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3640_unfreeze_camera_217',
        "command": 'unfreeze_camera',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3640_set_218',
        "command": 'set',
        "args": [0x70a7, 91],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3640_set_219',
        "command": 'set',
        "args": [0x7000, 524],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3640_run_event_as_subroutine_220',
        "command": 'run_event_as_subroutine',
        "args": [3828],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3640_stop_sound_221',
        "command": 'stop_sound',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3640_stop_sound_222',
        "command": 'stop_sound',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3640_stop_sound_223',
        "command": 'stop_sound',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3640_stop_sound_224',
        "command": 'stop_sound',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3640_stop_sound_225',
        "command": 'stop_sound',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3640_ret_226',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3640_stop_music_227',
        "command": 'stop_music',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3640_action_queue_async_228',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_3],
        "subscript": [
            {
                "identifier": 'EVENT_3640_action_queue_async_228_SUBSCRIPT_set_sprite_sequence_0',
                "command": 'set_sprite_sequence',
                "args": [0, inc_sprite=0, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3640_action_queue_async_228_SUBSCRIPT_pause_1',
                "command": 'pause',
                "args": [20]
            },
            {
                "identifier": 'EVENT_3640_action_queue_async_228_SUBSCRIPT_set_animation_speed_2',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3640_action_queue_async_228_SUBSCRIPT_set_sprite_sequence_3',
                "command": 'set_sprite_sequence',
                "args": [4, inc_sprite=0, flags=[_0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3640_action_queue_async_228_SUBSCRIPT_pause_4',
                "command": 'pause',
                "args": [45]
            }
        ]
    },
    {
        "identifier": 'EVENT_3640_action_queue_sync_229',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_3],
        "subscript": [
            {
                "identifier": 'EVENT_3640_action_queue_sync_229_SUBSCRIPT_sequence_looping_on_0',
                "command": 'sequence_looping_on',
                "args": []
            },
            {
                "identifier": 'EVENT_3640_action_queue_sync_229_SUBSCRIPT_sequence_playback_on_1',
                "command": 'sequence_playback_on',
                "args": []
            },
            {
                "identifier": 'EVENT_3640_action_queue_sync_229_SUBSCRIPT_set_animation_speed_2',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.WALKING, _0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3640_action_queue_sync_229_SUBSCRIPT_set_sprite_sequence_3',
                "command": 'set_sprite_sequence',
                "args": [1, inc_sprite=0, flags=[_0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_3640_action_queue_sync_229_SUBSCRIPT_shift_northwest_steps_4',
                "command": 'shift_northwest_steps',
                "args": [9]
            },
            {
                "identifier": 'EVENT_3640_action_queue_sync_229_SUBSCRIPT_shift_northwest_steps_5',
                "command": 'shift_northwest_steps',
                "args": [2]
            },
            {
                "identifier": 'EVENT_3640_action_queue_sync_229_SUBSCRIPT_visibility_off_6',
                "command": 'visibility_off',
                "args": []
            },
            {
                "identifier": 'EVENT_3640_action_queue_sync_229_SUBSCRIPT_sequence_looping_off_7',
                "command": 'sequence_looping_off',
                "args": []
            },
            {
                "identifier": 'EVENT_3640_action_queue_sync_229_SUBSCRIPT_pause_8',
                "command": 'pause',
                "args": [40]
            }
        ]
    },
    {
        "identifier": 'EVENT_3640_action_queue_async_230',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_3640_action_queue_async_230_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [60]
            },
            {
                "identifier": 'EVENT_3640_action_queue_async_230_SUBSCRIPT_set_sprite_sequence_1',
                "command": 'set_sprite_sequence',
                "args": [10, inc_sprite=0, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_3640_pause_231',
        "command": 'pause',
        "args": [60],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3640_play_sound_232',
        "command": 'play_sound',
        "args": [Sounds._016_OPEN_DOOR, 6],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3640_pause_233',
        "command": 'pause',
        "args": [60],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3640_jmp_if_bit_set_234',
        "command": 'jmp_if_bit_set',
        "args": [0x7044, 2, 'EVENT_3640_action_queue_async_242'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3640_action_queue_async_235',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_3640_action_queue_async_235_SUBSCRIPT_reset_properties_0',
                "command": 'reset_properties',
                "args": []
            }
        ]
    },
    {
        "identifier": 'EVENT_3640_clear_bit_236',
        "command": 'clear_bit',
        "args": [0x7043, 0],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3640_clear_bit_237',
        "command": 'clear_bit',
        "args": [0x7043, 1],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3640_set_bit_238',
        "command": 'set_bit',
        "args": [0x7044, 2],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3640_pause_239',
        "command": 'pause',
        "args": [30],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3640_jmp_240',
        "command": 'jmp',
        "args": ['EVENT_3640_pause_277'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3640_ret_241',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3640_action_queue_async_242',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_3640_action_queue_async_242_SUBSCRIPT_reset_properties_0',
                "command": 'reset_properties',
                "args": []
            }
        ]
    },
    {
        "identifier": 'EVENT_3640_enable_controls_until_return_243',
        "command": 'enable_controls_until_return',
        "args": [[]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3640_pause_244',
        "command": 'pause',
        "args": [60],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3640_fade_out_music_to_volume_245',
        "command": 'fade_out_music_to_volume',
        "args": [5, 0],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3640_action_queue_async_246',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_3],
        "subscript": [
            {
                "identifier": 'EVENT_3640_action_queue_async_246_SUBSCRIPT_shirt_to_xy_coords_0',
                "command": 'shirt_to_xy_coords',
                "args": [2, 56]
            },
            {
                "identifier": 'EVENT_3640_action_queue_async_246_SUBSCRIPT_shift_southwest_pixels_1',
                "command": 'shift_southwest_pixels',
                "args": [5]
            },
            {
                "identifier": 'EVENT_3640_action_queue_async_246_SUBSCRIPT_shift_southeast_pixels_2',
                "command": 'shift_southeast_pixels',
                "args": [16]
            },
            {
                "identifier": 'EVENT_3640_action_queue_async_246_SUBSCRIPT_set_sprite_sequence_3',
                "command": 'set_sprite_sequence',
                "args": [0, inc_sprite=0, flags=[_0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_3640_action_queue_async_246_SUBSCRIPT_set_animation_speed_4',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3640_action_queue_async_246_SUBSCRIPT_set_animation_speed_5',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_3640_action_queue_async_246_SUBSCRIPT_visibility_on_6',
                "command": 'visibility_on',
                "args": []
            },
            {
                "identifier": 'EVENT_3640_action_queue_async_246_SUBSCRIPT_shift_southeast_steps_7',
                "command": 'shift_southeast_steps',
                "args": [9]
            },
            {
                "identifier": 'EVENT_3640_action_queue_async_246_SUBSCRIPT_set_sprite_sequence_8',
                "command": 'set_sprite_sequence',
                "args": [0, inc_sprite=0, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3640_action_queue_async_246_SUBSCRIPT_pause_9',
                "command": 'pause',
                "args": [30]
            },
            {
                "identifier": 'EVENT_3640_action_queue_async_246_SUBSCRIPT_set_animation_speed_10',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.SLOW, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3640_action_queue_async_246_SUBSCRIPT_set_sprite_sequence_11',
                "command": 'set_sprite_sequence',
                "args": [6, inc_sprite=0, flags=[_0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3640_action_queue_async_246_SUBSCRIPT_pause_12',
                "command": 'pause',
                "args": [120]
            }
        ]
    },
    {
        "identifier": 'EVENT_3640_action_queue_sync_247',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_3],
        "subscript": [
            {
                "identifier": 'EVENT_3640_action_queue_sync_247_SUBSCRIPT_set_sprite_sequence_0',
                "command": 'set_sprite_sequence',
                "args": [9, inc_sprite=0, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3640_action_queue_sync_247_SUBSCRIPT_pause_1',
                "command": 'pause',
                "args": [40]
            },
            {
                "identifier": 'EVENT_3640_action_queue_sync_247_SUBSCRIPT_set_sprite_sequence_2',
                "command": 'set_sprite_sequence',
                "args": [10, inc_sprite=0, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3640_action_queue_sync_247_SUBSCRIPT_pause_3',
                "command": 'pause',
                "args": [40]
            },
            {
                "identifier": 'EVENT_3640_action_queue_sync_247_SUBSCRIPT_set_sprite_sequence_4',
                "command": 'set_sprite_sequence',
                "args": [11, inc_sprite=0, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3640_action_queue_sync_247_SUBSCRIPT_pause_5',
                "command": 'pause',
                "args": [40]
            },
            {
                "identifier": 'EVENT_3640_action_queue_sync_247_SUBSCRIPT_set_sprite_sequence_6',
                "command": 'set_sprite_sequence',
                "args": [12, inc_sprite=0, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3640_action_queue_sync_247_SUBSCRIPT_pause_7',
                "command": 'pause',
                "args": [40]
            }
        ]
    },
    {
        "identifier": 'EVENT_3640_action_queue_async_248',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_3640_action_queue_async_248_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [40]
            },
            {
                "identifier": 'EVENT_3640_action_queue_async_248_SUBSCRIPT_pause_1',
                "command": 'pause',
                "args": [40]
            },
            {
                "identifier": 'EVENT_3640_action_queue_async_248_SUBSCRIPT_pause_2',
                "command": 'pause',
                "args": [30]
            },
            {
                "identifier": 'EVENT_3640_action_queue_async_248_SUBSCRIPT_set_animation_speed_3',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3640_action_queue_async_248_SUBSCRIPT_set_sprite_sequence_4',
                "command": 'set_sprite_sequence',
                "args": [9, inc_sprite=0, flags=[_0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_3640_action_queue_async_248_SUBSCRIPT_pause_5',
                "command": 'pause',
                "args": [50]
            }
        ]
    },
    {
        "identifier": 'EVENT_3640_start_battle_249',
        "command": 'start_battle',
        "args": [0x00d0, 22],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3640_jmp_if_bit_clear_250',
        "command": 'jmp_if_bit_clear',
        "args": [0x7040, 0, 'EVENT_3640_unfreeze_camera_252'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3640_reset_and_choose_game_251',
        "command": 'reset_and_choose_game',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3640_unfreeze_camera_252',
        "command": 'unfreeze_camera',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3640_palette_set_253',
        "command": 'palette_set',
        "args": [84, 1],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3640_action_queue_sync_254',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_3],
        "subscript": [
            {
                "identifier": 'EVENT_3640_action_queue_sync_254_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3640_action_queue_sync_254_SUBSCRIPT_set_sprite_sequence_1',
                "command": 'set_sprite_sequence',
                "args": [6, inc_sprite=0, flags=[_0x08Flags.READ_AS_SEQUENCE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_3640_action_queue_async_255',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_3640_action_queue_async_255_SUBSCRIPT_reset_properties_0',
                "command": 'reset_properties',
                "args": []
            },
            {
                "identifier": 'EVENT_3640_action_queue_async_255_SUBSCRIPT_face_northeast_1',
                "command": 'face_northeast',
                "args": []
            }
        ]
    },
    {
        "identifier": 'EVENT_3640_fade_in_from_black_async_256',
        "command": 'fade_in_from_black_async',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3640_action_queue_async_257',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_3],
        "subscript": [
            {
                "identifier": 'EVENT_3640_action_queue_async_257_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [60]
            },
            {
                "identifier": 'EVENT_3640_action_queue_async_257_SUBSCRIPT_face_northwest_1',
                "command": 'face_northwest',
                "args": []
            },
            {
                "identifier": 'EVENT_3640_action_queue_async_257_SUBSCRIPT_set_sprite_sequence_2',
                "command": 'set_sprite_sequence',
                "args": [1, inc_sprite=0, flags=[_0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_3640_action_queue_async_257_SUBSCRIPT_set_animation_speed_3',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.WALKING, _0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3640_action_queue_async_257_SUBSCRIPT_shift_northwest_steps_4',
                "command": 'shift_northwest_steps',
                "args": [11]
            },
            {
                "identifier": 'EVENT_3640_action_queue_async_257_SUBSCRIPT_visibility_off_5',
                "command": 'visibility_off',
                "args": []
            }
        ]
    },
    {
        "identifier": 'EVENT_3640_pause_258',
        "command": 'pause',
        "args": [35],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3640_play_sound_259',
        "command": 'play_sound',
        "args": [Sounds._016_OPEN_DOOR, 6],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3640_pause_260',
        "command": 'pause',
        "args": [10],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3640_stop_sound_261',
        "command": 'stop_sound',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3640_stop_sound_262',
        "command": 'stop_sound',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3640_remove_from_level_263',
        "command": 'remove_from_level',
        "args": [AreaObjects.NPC_1, Rooms._112_NIMBUS_CASTLE_AREA_17_RIGHT_OF_4WAY_PATH_SAVE_POINT],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3640_set_action_script_async_264',
        "command": 'set_action_script_async',
        "args": [AreaObjects.MARIO, 395],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3640_enable_controls_until_return_265',
        "command": 'enable_controls_until_return',
        "args": [[ControllerDirections.LEFT, ControllerDirections.RIGHT, ControllerDirections.DOWN, ControllerDirections.UP, ControllerDirections.X, ControllerDirections.A, ControllerDirections.Y, ControllerDirections.B]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3640_restore_all_hp_266',
        "command": 'restore_all_hp',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3640_restore_all_fp_267',
        "command": 'restore_all_fp',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3640_jmp_if_bit_set_268',
        "command": 'jmp_if_bit_set',
        "args": [0x705f, 4, 'EVENT_3640_play_music_default_volume_273'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3640_play_music_default_volume_269',
        "command": 'play_music_default_volume',
        "args": [Music._61_VALENTINA],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3640_set_short_270',
        "command": 'set_short',
        "args": [0x700a, 0x00db],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3640_jmp_to_event_271',
        "command": 'jmp_to_event',
        "args": [720],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3640_ret_272',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3640_play_music_default_volume_273',
        "command": 'play_music_default_volume',
        "args": [Music._50_NIMBUS_LAND],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3640_set_short_274',
        "command": 'set_short',
        "args": [0x700a, 0x00db],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3640_jmp_to_event_275',
        "command": 'jmp_to_event',
        "args": [720],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3640_ret_276',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3640_pause_277',
        "command": 'pause',
        "args": [10],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3640_play_sound_278',
        "command": 'play_sound',
        "args": [Sounds._016_OPEN_DOOR, 6],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3640_pause_279',
        "command": 'pause',
        "args": [60],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3640_enable_controls_until_return_280',
        "command": 'enable_controls_until_return',
        "args": [[ControllerDirections.B]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3640_pause_281',
        "command": 'pause',
        "args": [1],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3640_play_music_default_volume_282',
        "command": 'play_music_default_volume',
        "args": [Music._01_DODOS_COMING],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3640_pause_283',
        "command": 'pause',
        "args": [143],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3640_pause_284',
        "command": 'pause',
        "args": [235],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3640_pause_285',
        "command": 'pause',
        "args": [131],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3640_jmp_286',
        "command": 'jmp',
        "args": ['EVENT_3640_action_queue_async_39'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3640_ret_287',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3640_action_queue_async_288',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_3],
        "subscript": [
            {
                "identifier": 'EVENT_3640_action_queue_async_288_SUBSCRIPT_sequence_playback_off_0',
                "command": 'sequence_playback_off',
                "args": []
            },
            {
                "identifier": 'EVENT_3640_action_queue_async_288_SUBSCRIPT_set_animation_speed_1',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING, _0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3640_action_queue_async_288_SUBSCRIPT_set_animation_speed_2',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.SLOW, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3640_action_queue_async_288_SUBSCRIPT_set_sprite_sequence_3',
                "command": 'set_sprite_sequence',
                "args": [0, inc_sprite=0, flags=[_0x08Flags.LOOPING_OFF, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_3640_action_queue_async_288_SUBSCRIPT_pause_4',
                "command": 'pause',
                "args": [12]
            },
            {
                "identifier": 'EVENT_3640_action_queue_async_288_SUBSCRIPT_set_sprite_sequence_5',
                "command": 'set_sprite_sequence',
                "args": [8, inc_sprite=0, flags=[_0x08Flags.LOOPING_OFF, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_3640_action_queue_async_288_SUBSCRIPT_walk_1_step_southeast_6',
                "command": 'walk_1_step_southeast',
                "args": []
            }
        ]
    },
    {
        "identifier": 'EVENT_3640_ret_289',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3640_action_queue_async_290',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_3],
        "subscript": [
            {
                "identifier": 'EVENT_3640_action_queue_async_290_SUBSCRIPT_sequence_playback_off_0',
                "command": 'sequence_playback_off',
                "args": []
            },
            {
                "identifier": 'EVENT_3640_action_queue_async_290_SUBSCRIPT_set_animation_speed_1',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING, _0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3640_action_queue_async_290_SUBSCRIPT_set_animation_speed_2',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.SLOW, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3640_action_queue_async_290_SUBSCRIPT_set_sprite_sequence_3',
                "command": 'set_sprite_sequence',
                "args": [0, inc_sprite=0, flags=[_0x08Flags.LOOPING_OFF, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_3640_action_queue_async_290_SUBSCRIPT_pause_4',
                "command": 'pause',
                "args": [12]
            },
            {
                "identifier": 'EVENT_3640_action_queue_async_290_SUBSCRIPT_set_sprite_sequence_5',
                "command": 'set_sprite_sequence',
                "args": [9, inc_sprite=0, flags=[_0x08Flags.LOOPING_OFF, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_3640_action_queue_async_290_SUBSCRIPT_walk_1_step_southeast_6',
                "command": 'walk_1_step_southeast',
                "args": []
            }
        ]
    },
    {
        "identifier": 'EVENT_3640_ret_291',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3640_action_queue_async_292',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_3],
        "subscript": [
            {
                "identifier": 'EVENT_3640_action_queue_async_292_SUBSCRIPT_sequence_playback_on_0',
                "command": 'sequence_playback_on',
                "args": []
            },
            {
                "identifier": 'EVENT_3640_action_queue_async_292_SUBSCRIPT_set_animation_speed_1',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING, _0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3640_action_queue_async_292_SUBSCRIPT_pause_2',
                "command": 'pause',
                "args": [3]
            },
            {
                "identifier": 'EVENT_3640_action_queue_async_292_SUBSCRIPT_face_southwest_3',
                "command": 'face_southwest',
                "args": []
            },
            {
                "identifier": 'EVENT_3640_action_queue_async_292_SUBSCRIPT_set_sprite_sequence_4',
                "command": 'set_sprite_sequence',
                "args": [0, inc_sprite=0, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3640_action_queue_async_292_SUBSCRIPT_pause_5',
                "command": 'pause',
                "args": [15]
            },
            {
                "identifier": 'EVENT_3640_action_queue_async_292_SUBSCRIPT_sequence_looping_on_6',
                "command": 'sequence_looping_on',
                "args": []
            },
            {
                "identifier": 'EVENT_3640_action_queue_async_292_SUBSCRIPT_set_sprite_sequence_7',
                "command": 'set_sprite_sequence',
                "args": [3, inc_sprite=0, flags=[_0x08Flags.LOOPING_OFF]]
            },
            {
                "identifier": 'EVENT_3640_action_queue_async_292_SUBSCRIPT_pause_8',
                "command": 'pause',
                "args": [19]
            },
            {
                "identifier": 'EVENT_3640_action_queue_async_292_SUBSCRIPT_set_sprite_sequence_9',
                "command": 'set_sprite_sequence',
                "args": [0, inc_sprite=0, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_3640_ret_293',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3640_set_temp_action_script_async_294',
        "command": 'set_temp_action_script_async',
        "args": [AreaObjects.NPC_0, 333],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3640_stop_sound_295',
        "command": 'stop_sound',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3640_stop_sound_296',
        "command": 'stop_sound',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3640_stop_sound_297',
        "command": 'stop_sound',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3640_stop_sound_298',
        "command": 'stop_sound',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3640_stop_sound_299',
        "command": 'stop_sound',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3640_stop_sound_300',
        "command": 'stop_sound',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3640_stop_sound_301',
        "command": 'stop_sound',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3640_stop_sound_302',
        "command": 'stop_sound',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3640_stop_sound_303',
        "command": 'stop_sound',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3640_ret_304',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3640_set_temp_action_script_async_305',
        "command": 'set_temp_action_script_async',
        "args": [AreaObjects.NPC_1, 333],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3640_stop_sound_306',
        "command": 'stop_sound',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3640_stop_sound_307',
        "command": 'stop_sound',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3640_stop_sound_308',
        "command": 'stop_sound',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3640_stop_sound_309',
        "command": 'stop_sound',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3640_stop_sound_310',
        "command": 'stop_sound',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3640_stop_sound_311',
        "command": 'stop_sound',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3640_stop_sound_312',
        "command": 'stop_sound',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3640_stop_sound_313',
        "command": 'stop_sound',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3640_stop_sound_314',
        "command": 'stop_sound',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3640_ret_315',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3640_stop_music_316',
        "command": 'stop_music',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3640_enable_controls_until_return_317',
        "command": 'enable_controls_until_return',
        "args": [[]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3640_freeze_camera_318',
        "command": 'freeze_camera',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3640_action_queue_sync_319',
        "command": 'action_queue_sync',
        "args": [AreaObjects.SCREEN_FOCUS],
        "subscript": [
            {
                "identifier": 'EVENT_3640_action_queue_sync_319_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [15]
            },
            {
                "identifier": 'EVENT_3640_action_queue_sync_319_SUBSCRIPT_play_sound_1',
                "command": 'play_sound',
                "args": [Sounds._022_CLOSE_DOOR, 6]
            },
            {
                "identifier": 'EVENT_3640_action_queue_sync_319_SUBSCRIPT_shift_northeast_pixels_2',
                "command": 'shift_northeast_pixels',
                "args": [4]
            },
            {
                "identifier": 'EVENT_3640_action_queue_sync_319_SUBSCRIPT_shift_southwest_pixels_3',
                "command": 'shift_southwest_pixels',
                "args": [4]
            },
            {
                "identifier": 'EVENT_3640_action_queue_sync_319_SUBSCRIPT_shift_northeast_pixels_4',
                "command": 'shift_northeast_pixels',
                "args": [2]
            },
            {
                "identifier": 'EVENT_3640_action_queue_sync_319_SUBSCRIPT_shift_southwest_pixels_5',
                "command": 'shift_southwest_pixels',
                "args": [2]
            }
        ]
    },
    {
        "identifier": 'EVENT_3640_action_queue_sync_320',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_3],
        "subscript": [
            {
                "identifier": 'EVENT_3640_action_queue_sync_320_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [50]
            },
            {
                "identifier": 'EVENT_3640_action_queue_sync_320_SUBSCRIPT_set_sprite_sequence_1',
                "command": 'set_sprite_sequence',
                "args": [0, inc_sprite=0, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_3640_action_queue_async_321',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_3640_action_queue_async_321_SUBSCRIPT_fixed_f_coord_on_0',
                "command": 'fixed_f_coord_on',
                "args": []
            },
            {
                "identifier": 'EVENT_3640_action_queue_async_321_SUBSCRIPT_sequence_playback_on_1',
                "command": 'sequence_playback_on',
                "args": []
            },
            {
                "identifier": 'EVENT_3640_action_queue_async_321_SUBSCRIPT_sequence_looping_on_2',
                "command": 'sequence_looping_on',
                "args": []
            },
            {
                "identifier": 'EVENT_3640_action_queue_async_321_SUBSCRIPT_set_animation_speed_3',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3640_action_queue_async_321_SUBSCRIPT_set_sprite_sequence_4',
                "command": 'set_sprite_sequence',
                "args": [7, inc_sprite=2, flags=[_0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3640_action_queue_async_321_SUBSCRIPT_pause_5',
                "command": 'pause',
                "args": [5]
            },
            {
                "identifier": 'EVENT_3640_action_queue_async_321_SUBSCRIPT_sequence_playback_off_6',
                "command": 'sequence_playback_off',
                "args": []
            },
            {
                "identifier": 'EVENT_3640_action_queue_async_321_SUBSCRIPT_set_animation_speed_7',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_3640_action_queue_async_321_SUBSCRIPT_set_sprite_sequence_8',
                "command": 'set_sprite_sequence',
                "args": [3, inc_sprite=2, flags=[_0x08Flags.LOOPING_OFF, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3640_action_queue_async_321_SUBSCRIPT_shift_southwest_steps_9',
                "command": 'shift_southwest_steps',
                "args": [1]
            },
            {
                "identifier": 'EVENT_3640_action_queue_async_321_SUBSCRIPT_pause_10',
                "command": 'pause',
                "args": [25]
            },
            {
                "identifier": 'EVENT_3640_action_queue_async_321_SUBSCRIPT_sequence_playback_on_11',
                "command": 'sequence_playback_on',
                "args": []
            },
            {
                "identifier": 'EVENT_3640_action_queue_async_321_SUBSCRIPT_set_animation_speed_12',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3640_action_queue_async_321_SUBSCRIPT_set_sprite_sequence_13',
                "command": 'set_sprite_sequence',
                "args": [9, inc_sprite=0, flags=[_0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_3640_action_queue_async_321_SUBSCRIPT_pause_14',
                "command": 'pause',
                "args": [20]
            },
            {
                "identifier": 'EVENT_3640_action_queue_async_321_SUBSCRIPT_reset_properties_15',
                "command": 'reset_properties',
                "args": []
            },
            {
                "identifier": 'EVENT_3640_action_queue_async_321_SUBSCRIPT_sequence_looping_off_16',
                "command": 'sequence_looping_off',
                "args": []
            },
            {
                "identifier": 'EVENT_3640_action_queue_async_321_SUBSCRIPT_set_animation_speed_17',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING, _0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3640_action_queue_async_321_SUBSCRIPT_set_animation_speed_18',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_3640_action_queue_async_321_SUBSCRIPT_jump_to_height_19',
                "command": 'jump_to_height',
                "args": [108]
            },
            {
                "identifier": 'EVENT_3640_action_queue_async_321_SUBSCRIPT_shift_northeast_steps_20',
                "command": 'shift_northeast_steps',
                "args": [1]
            }
        ]
    },
    {
        "identifier": 'EVENT_3640_pause_322',
        "command": 'pause',
        "args": [40],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3640_action_queue_async_323',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_3],
        "subscript": [
            {
                "identifier": 'EVENT_3640_action_queue_async_323_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3640_action_queue_async_323_SUBSCRIPT_set_sprite_sequence_1',
                "command": 'set_sprite_sequence',
                "args": [7, inc_sprite=0, flags=[_0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3640_action_queue_async_323_SUBSCRIPT_pause_2',
                "command": 'pause',
                "args": [60]
            }
        ]
    },
    {
        "identifier": 'EVENT_3640_action_queue_sync_324',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_3],
        "subscript": [
            {
                "identifier": 'EVENT_3640_action_queue_sync_324_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.WALKING, _0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3640_action_queue_sync_324_SUBSCRIPT_set_sprite_sequence_1',
                "command": 'set_sprite_sequence',
                "args": [1, inc_sprite=0, flags=[_0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_3640_action_queue_sync_324_SUBSCRIPT_shift_northwest_steps_2',
                "command": 'shift_northwest_steps',
                "args": [11]
            },
            {
                "identifier": 'EVENT_3640_action_queue_sync_324_SUBSCRIPT_visibility_off_3',
                "command": 'visibility_off',
                "args": []
            }
        ]
    },
    {
        "identifier": 'EVENT_3640_action_queue_async_325',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_3640_action_queue_async_325_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [60]
            },
            {
                "identifier": 'EVENT_3640_action_queue_async_325_SUBSCRIPT_set_sprite_sequence_1',
                "command": 'set_sprite_sequence',
                "args": [10, inc_sprite=0, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_3640_pause_326',
        "command": 'pause',
        "args": [60],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3640_play_sound_327',
        "command": 'play_sound',
        "args": [Sounds._016_OPEN_DOOR, 6],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3640_pause_328',
        "command": 'pause',
        "args": [60],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3640_jmp_if_bit_set_329',
        "command": 'jmp_if_bit_set',
        "args": [0x7044, 2, 'EVENT_3640_action_queue_async_242'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3640_action_queue_async_330',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_3640_action_queue_async_330_SUBSCRIPT_reset_properties_0',
                "command": 'reset_properties',
                "args": []
            }
        ]
    },
    {
        "identifier": 'EVENT_3640_clear_bit_331',
        "command": 'clear_bit',
        "args": [0x7043, 0],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3640_clear_bit_332',
        "command": 'clear_bit',
        "args": [0x7043, 1],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3640_set_bit_333',
        "command": 'set_bit',
        "args": [0x7044, 2],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3640_pause_334',
        "command": 'pause',
        "args": [30],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3640_jmp_335',
        "command": 'jmp',
        "args": ['EVENT_3640_pause_277'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3640_ret_336',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3640_set_temp_action_script_async_337',
        "command": 'set_temp_action_script_async',
        "args": [AreaObjects.NPC_2, 333],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3640_stop_sound_338',
        "command": 'stop_sound',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3640_stop_sound_339',
        "command": 'stop_sound',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3640_stop_sound_340',
        "command": 'stop_sound',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3640_stop_sound_341',
        "command": 'stop_sound',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3640_stop_sound_342',
        "command": 'stop_sound',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3640_stop_sound_343',
        "command": 'stop_sound',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3640_stop_sound_344',
        "command": 'stop_sound',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3640_stop_sound_345',
        "command": 'stop_sound',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3640_stop_sound_346',
        "command": 'stop_sound',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3640_ret_347',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3640_action_queue_async_348',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_3],
        "subscript": [
            {
                "identifier": 'EVENT_3640_action_queue_async_348_SUBSCRIPT_sequence_playback_off_0',
                "command": 'sequence_playback_off',
                "args": []
            },
            {
                "identifier": 'EVENT_3640_action_queue_async_348_SUBSCRIPT_set_animation_speed_1',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING, _0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3640_action_queue_async_348_SUBSCRIPT_set_animation_speed_2',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.SLOW, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3640_action_queue_async_348_SUBSCRIPT_set_sprite_sequence_3',
                "command": 'set_sprite_sequence',
                "args": [1, inc_sprite=0, flags=[_0x08Flags.LOOPING_OFF, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_3640_action_queue_async_348_SUBSCRIPT_pause_4',
                "command": 'pause',
                "args": [12]
            },
            {
                "identifier": 'EVENT_3640_action_queue_async_348_SUBSCRIPT_set_sprite_sequence_5',
                "command": 'set_sprite_sequence',
                "args": [10, inc_sprite=0, flags=[_0x08Flags.LOOPING_OFF, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_3640_action_queue_async_348_SUBSCRIPT_walk_1_step_northwest_6',
                "command": 'walk_1_step_northwest',
                "args": []
            }
        ]
    },
    {
        "identifier": 'EVENT_3640_ret_349',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3640_action_queue_async_350',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_3],
        "subscript": [
            {
                "identifier": 'EVENT_3640_action_queue_async_350_SUBSCRIPT_sequence_playback_off_0',
                "command": 'sequence_playback_off',
                "args": []
            },
            {
                "identifier": 'EVENT_3640_action_queue_async_350_SUBSCRIPT_set_animation_speed_1',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING, _0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3640_action_queue_async_350_SUBSCRIPT_set_animation_speed_2',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.SLOW, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3640_action_queue_async_350_SUBSCRIPT_set_sprite_sequence_3',
                "command": 'set_sprite_sequence',
                "args": [1, inc_sprite=0, flags=[_0x08Flags.LOOPING_OFF, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_3640_action_queue_async_350_SUBSCRIPT_pause_4',
                "command": 'pause',
                "args": [12]
            },
            {
                "identifier": 'EVENT_3640_action_queue_async_350_SUBSCRIPT_set_sprite_sequence_5',
                "command": 'set_sprite_sequence',
                "args": [11, inc_sprite=0, flags=[_0x08Flags.LOOPING_OFF, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_3640_action_queue_async_350_SUBSCRIPT_walk_1_step_northwest_6',
                "command": 'walk_1_step_northwest',
                "args": []
            }
        ]
    },
    {
        "identifier": 'EVENT_3640_ret_351',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3640_create_packet_event_at_coords_jmp_if_null_352',
        "command": 'create_packet_event_at_coords_jmp_if_null',
        "args": [NPCPackets._000_FLOWER, 0x0000],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3640_create_packet_event_at_coords_jmp_if_null_353',
        "command": 'create_packet_event_at_coords_jmp_if_null',
        "args": [NPCPackets._000_FLOWER, 0x0000, 'EVENT_3622_ret_9'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3640_create_packet_event_at_coords_jmp_if_null_354',
        "command": 'create_packet_event_at_coords_jmp_if_null',
        "args": [NPCPackets._000_FLOWER, 0x0000],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3640_create_packet_event_at_coords_jmp_if_null_355',
        "command": 'create_packet_event_at_coords_jmp_if_null',
        "args": [NPCPackets._000_FLOWER, 0x0000, 'EVENT_3372_action_queue_sync_10'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3640_create_packet_event_at_coords_jmp_if_null_356',
        "command": 'create_packet_event_at_coords_jmp_if_null',
        "args": [NPCPackets._000_FLOWER, 0x0000],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3640_create_packet_event_at_coords_jmp_if_null_357',
        "command": 'create_packet_event_at_coords_jmp_if_null',
        "args": [NPCPackets._000_FLOWER, 0x0000],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3640_create_packet_event_at_coords_jmp_if_null_358',
        "command": 'create_packet_event_at_coords_jmp_if_null',
        "args": [NPCPackets._000_FLOWER, 0x0000],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3640_create_packet_event_at_coords_jmp_if_null_359',
        "command": 'create_packet_event_at_coords_jmp_if_null',
        "args": [NPCPackets._000_FLOWER, 0x0000],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3640_create_packet_event_at_coords_jmp_if_null_360',
        "command": 'create_packet_event_at_coords_jmp_if_null',
        "args": [NPCPackets._000_FLOWER, 0x0000, 'EVENT_3820_set_short_2'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3640_create_packet_event_at_coords_jmp_if_null_361',
        "command": 'create_packet_event_at_coords_jmp_if_null',
        "args": [NPCPackets._000_FLOWER, 0x0000],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3640_ret_362',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3640_ret_363',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3640_ret_364',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3640_ret_365',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3640_ret_366',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3640_ret_367',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3640_ret_368',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3640_ret_369',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3640_ret_370',
        "command": 'ret',
        "args": [],
        "subscript": []
    }
]
