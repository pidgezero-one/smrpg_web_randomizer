from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data import items
script = [
    {
        "identifier": 'EVENT_1364_jmp_if_bit_set_0',
        "command": 'jmp_if_bit_set',
        "args": [0x708b, 5, 'EVENT_1364_jmp_if_bit_clear_73']
    },
    {
        "identifier": 'EVENT_1364_jmp_if_bit_set_1',
        "command": 'jmp_if_bit_set',
        "args": [0x7053, 5, 'EVENT_1364_fade_out_to_black_async_44']
    },
    {
        "identifier": 'EVENT_1364_jmp_if_bit_set_2',
        "command": 'jmp_if_bit_set',
        "args": [0x7053, 4, 'EVENT_1364_fade_out_to_black_async_44']
    },
    {
        "identifier": 'EVENT_1364_fade_out_to_black_async_3',
        "command": 'fade_out_to_black_async'
    },
    {
        "identifier": 'EVENT_1364_pause_4',
        "command": 'pause',
        "args": [5]
    },
    {
        "identifier": 'EVENT_1364_jmp_5',
        "command": 'jmp',
        "args": ['EVENT_1281_enter_area_0']
    },
    {
        "identifier": 'EVENT_1364_freeze_camera_6',
        "command": 'freeze_camera'
    },
    {
        "identifier": 'EVENT_1364_apply_solidity_mod_7',
        "command": 'apply_solidity_mod',
        "args": [Rooms._192_BOOSTER_TOWER_9F_AREA_02_BOOSTERS_CURTAIN_GAME_ROOM, 3, [_0x6BFlags.PERMANENT]]
    },
    {
        "identifier": 'EVENT_1364_action_queue_sync_8',
        "command": 'action_queue_sync',
        "args": [AreaObjects.SCREEN_FOCUS],
        "subscript": [
            {
                "identifier": 'EVENT_1364_action_queue_sync_8_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_1364_action_queue_sync_8_SUBSCRIPT_bounce_to_xy_with_height_1',
                "command": 'bounce_to_xy_with_height',
                "args": [0, 3, 0]
            }
        ]
    },
    {
        "identifier": 'EVENT_1364_action_queue_async_9',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_1364_action_queue_async_9_SUBSCRIPT_shirt_to_xy_coords_0',
                "command": 'shirt_to_xy_coords',
                "args": [3, 26]
            },
            {
                "identifier": 'EVENT_1364_action_queue_async_9_SUBSCRIPT_set_animation_speed_1',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FASTEST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_1364_action_queue_async_9_SUBSCRIPT_shift_northwest_pixels_2',
                "command": 'shift_northwest_pixels',
                "args": [8]
            },
            {
                "identifier": 'EVENT_1364_action_queue_async_9_SUBSCRIPT_set_sprite_sequence_3',
                "command": 'set_sprite_sequence',
                "args": [3, 3, [_0x08Flags.READ_AS_SEQUENCE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_1364_fade_in_from_black_async_10',
        "command": 'fade_in_from_black_async'
    },
    {
        "identifier": 'EVENT_1364_jmp_11',
        "command": 'jmp',
        "args": ['EVENT_1364_play_music_default_volume_14']
    },
    {
        "identifier": 'EVENT_1364_pause_12',
        "command": 'pause',
        "args": [80]
    },
    {
        "identifier": 'EVENT_1364_fade_out_music_to_volume_13',
        "command": 'fade_out_music_to_volume',
        "args": [0, 100]
    },
    {
        "identifier": 'EVENT_1364_play_music_default_volume_14',
        "command": 'play_music_default_volume',
        "args": [Music._32_AND_MY_NAMES_BOOSTER]
    },
    {
        "identifier": 'EVENT_1364_pause_15',
        "command": 'pause',
        "args": [1]
    },
    {
        "identifier": 'EVENT_1364_jmp_16',
        "command": 'jmp',
        "args": ['EVENT_1364_action_queue_async_24']
    },
    {
        "identifier": 'EVENT_1364_unsync_dialog_17',
        "command": 'unsync_dialog'
    },
    {
        "identifier": 'EVENT_1364_action_queue_async_18',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_1364_action_queue_async_18_SUBSCRIPT_reset_properties_0',
                "command": 'reset_properties'
            },
            {
                "identifier": 'EVENT_1364_action_queue_async_18_SUBSCRIPT_face_northeast_1',
                "command": 'face_northeast'
            },
            {
                "identifier": 'EVENT_1364_action_queue_async_18_SUBSCRIPT_jump_to_height_2',
                "command": 'jump_to_height',
                "args": [96]
            }
        ]
    },
    {
        "identifier": 'EVENT_1364_pause_19',
        "command": 'pause',
        "args": [60]
    },
    {
        "identifier": 'EVENT_1364_pause_script_resume_on_next_dialog_page_a_FD61_20',
        "command": 'pause_script_resume_on_next_dialog_page_a_FD61'
    },
    {
        "identifier": 'EVENT_1364_action_queue_async_21',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_1364_action_queue_async_21_SUBSCRIPT_face_southwest_0',
                "command": 'face_southwest'
            }
        ]
    },
    {
        "identifier": 'EVENT_1364_unsync_dialog_22',
        "command": 'unsync_dialog'
    },
    {
        "identifier": 'EVENT_1364_close_dialog_23',
        "command": 'close_dialog'
    },
    {
        "identifier": 'EVENT_1364_action_queue_async_24',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_1364_action_queue_async_24_SUBSCRIPT_reset_properties_0',
                "command": 'reset_properties'
            },
            {
                "identifier": 'EVENT_1364_action_queue_async_24_SUBSCRIPT_set_animation_speed_1',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_1364_action_queue_async_24_SUBSCRIPT_set_animation_speed_2',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_1364_action_queue_async_24_SUBSCRIPT_pause_3',
                "command": 'pause',
                "args": [15]
            },
            {
                "identifier": 'EVENT_1364_action_queue_async_24_SUBSCRIPT_face_northeast_4',
                "command": 'face_northeast'
            },
            {
                "identifier": 'EVENT_1364_action_queue_async_24_SUBSCRIPT_pause_5',
                "command": 'pause',
                "args": [15]
            },
            {
                "identifier": 'EVENT_1364_action_queue_async_24_SUBSCRIPT_shift_northeast_steps_6',
                "command": 'shift_northeast_steps',
                "args": [3]
            },
            {
                "identifier": 'EVENT_1364_action_queue_async_24_SUBSCRIPT_shift_northeast_pixels_7',
                "command": 'shift_northeast_pixels',
                "args": [8]
            },
            {
                "identifier": 'EVENT_1364_action_queue_async_24_SUBSCRIPT_pause_8',
                "command": 'pause',
                "args": [7]
            },
            {
                "identifier": 'EVENT_1364_action_queue_async_24_SUBSCRIPT_set_sprite_sequence_9',
                "command": 'set_sprite_sequence',
                "args": [10, 0, [_0x08Flags.READ_AS_MOLD, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_1364_action_queue_async_24_SUBSCRIPT_pause_10',
                "command": 'pause',
                "args": [7]
            },
            {
                "identifier": 'EVENT_1364_action_queue_async_24_SUBSCRIPT_set_sprite_sequence_11',
                "command": 'set_sprite_sequence',
                "args": [11, 0, [_0x08Flags.READ_AS_MOLD, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_1364_action_queue_async_24_SUBSCRIPT_pause_12',
                "command": 'pause',
                "args": [15]
            },
            {
                "identifier": 'EVENT_1364_action_queue_async_24_SUBSCRIPT_set_sprite_sequence_13',
                "command": 'set_sprite_sequence',
                "args": [9, 0, [_0x08Flags.READ_AS_MOLD]]
            },
            {
                "identifier": 'EVENT_1364_action_queue_async_24_SUBSCRIPT_pause_14',
                "command": 'pause',
                "args": [7]
            },
            {
                "identifier": 'EVENT_1364_action_queue_async_24_SUBSCRIPT_set_sprite_sequence_15',
                "command": 'set_sprite_sequence',
                "args": [8, 0, [_0x08Flags.READ_AS_MOLD]]
            },
            {
                "identifier": 'EVENT_1364_action_queue_async_24_SUBSCRIPT_pause_16',
                "command": 'pause',
                "args": [30]
            },
            {
                "identifier": 'EVENT_1364_action_queue_async_24_SUBSCRIPT_reset_properties_17',
                "command": 'reset_properties'
            },
            {
                "identifier": 'EVENT_1364_action_queue_async_24_SUBSCRIPT_face_northwest_18',
                "command": 'face_northwest'
            },
            {
                "identifier": 'EVENT_1364_action_queue_async_24_SUBSCRIPT_pause_19',
                "command": 'pause',
                "args": [20]
            },
            {
                "identifier": 'EVENT_1364_action_queue_async_24_SUBSCRIPT_set_priority_20',
                "command": 'set_priority',
                "args": [3]
            },
            {
                "identifier": 'EVENT_1364_action_queue_async_24_SUBSCRIPT_clear_solidity_bits_21',
                "command": 'clear_solidity_bits',
                "args": [[_0x0AFlags.CANT_PASS_WALLS]]
            },
            {
                "identifier": 'EVENT_1364_action_queue_async_24_SUBSCRIPT_shift_northwest_steps_22',
                "command": 'shift_northwest_steps',
                "args": [3]
            },
            {
                "identifier": 'EVENT_1364_action_queue_async_24_SUBSCRIPT_shift_northwest_pixels_23',
                "command": 'shift_northwest_pixels',
                "args": [7]
            }
        ]
    },
    {
        "identifier": 'EVENT_1364_pause_25',
        "command": 'pause',
        "args": [20]
    },
    {
        "identifier": 'EVENT_1364_play_sound_26',
        "command": 'play_sound',
        "args": [Sounds._090_CURTAIN, 6]
    },
    {
        "identifier": 'EVENT_1364_apply_tile_mod_27',
        "command": 'apply_tile_mod',
        "args": [Rooms._192_BOOSTER_TOWER_9F_AREA_02_BOOSTERS_CURTAIN_GAME_ROOM, 37, [_0x6AFlags.USE_ALTERNATE]]
    },
    {
        "identifier": 'EVENT_1364_pause_28',
        "command": 'pause',
        "args": [2]
    },
    {
        "identifier": 'EVENT_1364_apply_tile_mod_29',
        "command": 'apply_tile_mod',
        "args": [Rooms._192_BOOSTER_TOWER_9F_AREA_02_BOOSTERS_CURTAIN_GAME_ROOM, 38, [_0x6AFlags.USE_ALTERNATE]]
    },
    {
        "identifier": 'EVENT_1364_pause_30',
        "command": 'pause',
        "args": [2]
    },
    {
        "identifier": 'EVENT_1364_apply_tile_mod_31',
        "command": 'apply_tile_mod',
        "args": [Rooms._192_BOOSTER_TOWER_9F_AREA_02_BOOSTERS_CURTAIN_GAME_ROOM, 39, [_0x6AFlags.USE_ALTERNATE]]
    },
    {
        "identifier": 'EVENT_1364_pause_32',
        "command": 'pause',
        "args": [2]
    },
    {
        "identifier": 'EVENT_1364_pause_33',
        "command": 'pause',
        "args": [15]
    },
    {
        "identifier": 'EVENT_1364_action_queue_async_34',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_1364_action_queue_async_34_SUBSCRIPT_shift_northwest_pixels_0',
                "command": 'shift_northwest_pixels',
                "args": [20]
            },
            {
                "identifier": 'EVENT_1364_action_queue_async_34_SUBSCRIPT_set_priority_1',
                "command": 'set_priority',
                "args": [2]
            },
            {
                "identifier": 'EVENT_1364_action_queue_async_34_SUBSCRIPT_pause_2',
                "command": 'pause',
                "args": [15]
            },
            {
                "identifier": 'EVENT_1364_action_queue_async_34_SUBSCRIPT_face_southeast_3',
                "command": 'face_southeast'
            },
            {
                "identifier": 'EVENT_1364_action_queue_async_34_SUBSCRIPT_pause_4',
                "command": 'pause',
                "args": [10]
            },
            {
                "identifier": 'EVENT_1364_action_queue_async_34_SUBSCRIPT_set_solidity_bits_5',
                "command": 'set_solidity_bits',
                "args": [[_0x0AFlags.CANT_PASS_WALLS]]
            },
            {
                "identifier": 'EVENT_1364_action_queue_async_34_SUBSCRIPT_set_animation_speed_6',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING, _0x10Flags.SEQUENCE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_1364_play_sound_35',
        "command": 'play_sound',
        "args": [Sounds._090_CURTAIN, 6]
    },
    {
        "identifier": 'EVENT_1364_apply_tile_mod_36',
        "command": 'apply_tile_mod',
        "args": [Rooms._192_BOOSTER_TOWER_9F_AREA_02_BOOSTERS_CURTAIN_GAME_ROOM, 38, [_0x6AFlags.USE_ALTERNATE]]
    },
    {
        "identifier": 'EVENT_1364_pause_37',
        "command": 'pause',
        "args": [2]
    },
    {
        "identifier": 'EVENT_1364_apply_tile_mod_38',
        "command": 'apply_tile_mod',
        "args": [Rooms._192_BOOSTER_TOWER_9F_AREA_02_BOOSTERS_CURTAIN_GAME_ROOM, 37, [_0x6AFlags.USE_ALTERNATE]]
    },
    {
        "identifier": 'EVENT_1364_pause_39',
        "command": 'pause',
        "args": [2]
    },
    {
        "identifier": 'EVENT_1364_apply_tile_mod_40',
        "command": 'apply_tile_mod',
        "args": [Rooms._192_BOOSTER_TOWER_9F_AREA_02_BOOSTERS_CURTAIN_GAME_ROOM, 36, [_0x6AFlags.USE_ALTERNATE]]
    },
    {
        "identifier": 'EVENT_1364_pause_41',
        "command": 'pause',
        "args": [2]
    },
    {
        "identifier": 'EVENT_1364_jmp_42',
        "command": 'jmp',
        "args": ['EVENT_1358_remove_from_level_0']
    },
    {
        "identifier": 'EVENT_1364_ret_43',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_1364_fade_out_to_black_async_44',
        "command": 'fade_out_to_black_async'
    },
    {
        "identifier": 'EVENT_1364_fade_out_music_to_volume_45',
        "command": 'fade_out_music_to_volume',
        "args": [0, 0]
    },
    {
        "identifier": 'EVENT_1364_start_battle_46',
        "command": 'start_battle',
        "args": [0x00b1, 17]
    },
    {
        "identifier": 'EVENT_1364_jmp_if_bit_clear_47',
        "command": 'jmp_if_bit_clear',
        "args": [0x7040, 0, 'EVENT_1364_fade_out_music_to_volume_49']
    },
    {
        "identifier": 'EVENT_1364_reset_and_choose_game_48',
        "command": 'reset_and_choose_game'
    },
    {
        "identifier": 'EVENT_1364_fade_out_music_to_volume_49',
        "command": 'fade_out_music_to_volume',
        "args": [0, 0]
    },
    {
        "identifier": 'EVENT_1364_remove_from_level_50',
        "command": 'remove_from_level',
        "args": [AreaObjects.NPC_4, Rooms._039_BOOSTER_TOWER_5F_KNIFE_GUYS_JUGGLING_ROOM]
    },
    {
        "identifier": 'EVENT_1364_set_bit_51',
        "command": 'set_bit',
        "args": [0x7048, 6]
    },
    {
        "identifier": 'EVENT_1364_set_bit_52',
        "command": 'set_bit',
        "args": [0x7053, 7]
    },
    {
        "identifier": 'EVENT_1364_set_bit_53',
        "command": 'set_bit',
        "args": [0x7089, 2]
    },
    {
        "identifier": 'EVENT_1364_enter_area_54',
        "command": 'enter_area',
        "args": [Rooms._202_BOOSTER_TOWER_ENTRANCE, RadialDirections.SOUTHWEST, 5, 114, 0, [_0x68Flags.RUN_ENTRANCE_EVENT]]
    },
    {
        "identifier": 'EVENT_1364_stop_sound_55',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_1364_set_short_56',
        "command": 'set_short',
        "args": [0x700a, 0x00d0]
    },
    {
        "identifier": 'EVENT_1364_run_event_as_subroutine_57',
        "command": 'run_event_as_subroutine',
        "args": [720]
    },
    {
        "identifier": 'EVENT_1364_restore_all_hp_58',
        "command": 'restore_all_hp'
    },
    {
        "identifier": 'EVENT_1364_restore_all_fp_59',
        "command": 'restore_all_fp'
    },
    {
        "identifier": 'EVENT_1364_set_bit_60',
        "command": 'set_bit',
        "args": [0x708b, 5]
    },
    {
        "identifier": 'EVENT_1364_ret_61',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_1364_play_music_default_volume_62',
        "command": 'play_music_default_volume',
        "args": [Music._37_BOOSTER_HILL_START]
    },
    {
        "identifier": 'EVENT_1364_jmp_63',
        "command": 'jmp',
        "args": ['EVENT_1364_restore_all_hp_58']
    },
    {
        "identifier": 'EVENT_1364_remove_from_current_level_64',
        "command": 'remove_from_current_level',
        "args": [AreaObjects.NPC_0]
    },
    {
        "identifier": 'EVENT_1364_fade_in_from_black_async_65',
        "command": 'fade_in_from_black_async'
    },
    {
        "identifier": 'EVENT_1364_play_sound_66',
        "command": 'play_sound',
        "args": [Sounds._019_LONG_FALL, 6]
    },
    {
        "identifier": 'EVENT_1364_pause_67',
        "command": 'pause',
        "args": [50]
    },
    {
        "identifier": 'EVENT_1364_freeze_camera_68',
        "command": 'freeze_camera'
    },
    {
        "identifier": 'EVENT_1364_action_queue_async_69',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_1364_action_queue_async_69_SUBSCRIPT_play_sound_0',
                "command": 'play_sound',
                "args": [Sounds._058_INSERT, 6]
            },
            {
                "identifier": 'EVENT_1364_action_queue_async_69_SUBSCRIPT_pause_1',
                "command": 'pause',
                "args": [45]
            },
            {
                "identifier": 'EVENT_1364_action_queue_async_69_SUBSCRIPT_set_sprite_sequence_2',
                "command": 'set_sprite_sequence',
                "args": [8, 0, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_1364_action_queue_async_69_SUBSCRIPT_pause_3',
                "command": 'pause',
                "args": [10]
            },
            {
                "identifier": 'EVENT_1364_action_queue_async_69_SUBSCRIPT_set_sprite_sequence_4',
                "command": 'set_sprite_sequence',
                "args": [9, 0, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_1364_action_queue_async_69_SUBSCRIPT_pause_5',
                "command": 'pause',
                "args": [10]
            },
            {
                "identifier": 'EVENT_1364_action_queue_async_69_SUBSCRIPT_set_sprite_sequence_6',
                "command": 'set_sprite_sequence',
                "args": [8, 0, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_1364_action_queue_async_69_SUBSCRIPT_pause_7',
                "command": 'pause',
                "args": [25]
            },
            {
                "identifier": 'EVENT_1364_action_queue_async_69_SUBSCRIPT_reset_properties_8',
                "command": 'reset_properties'
            },
            {
                "identifier": 'EVENT_1364_action_queue_async_69_SUBSCRIPT_pause_9',
                "command": 'pause',
                "args": [30]
            },
            {
                "identifier": 'EVENT_1364_action_queue_async_69_SUBSCRIPT_set_animation_speed_10',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_1364_action_queue_async_69_SUBSCRIPT_sequence_looping_on_11',
                "command": 'sequence_looping_on'
            },
            {
                "identifier": 'EVENT_1364_action_queue_async_69_SUBSCRIPT_play_sound_12',
                "command": 'play_sound',
                "args": [Sounds._024_TAPPING_FEET, 6]
            },
            {
                "identifier": 'EVENT_1364_action_queue_async_69_SUBSCRIPT_shift_northeast_pixels_13',
                "command": 'shift_northeast_pixels',
                "args": [24]
            },
            {
                "identifier": 'EVENT_1364_action_queue_async_69_SUBSCRIPT_jump_to_height_silent_14',
                "command": 'jump_to_height_silent',
                "args": [69]
            },
            {
                "identifier": 'EVENT_1364_action_queue_async_69_SUBSCRIPT_play_sound_15',
                "command": 'play_sound',
                "args": [Sounds._011_WHOOSH_AWAY, 6]
            },
            {
                "identifier": 'EVENT_1364_action_queue_async_69_SUBSCRIPT_set_animation_speed_16',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FASTEST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_1364_action_queue_async_69_SUBSCRIPT_set_animation_speed_17',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_1364_action_queue_async_69_SUBSCRIPT_shift_southwest_steps_18',
                "command": 'shift_southwest_steps',
                "args": [8]
            },
            {
                "identifier": 'EVENT_1364_action_queue_async_69_SUBSCRIPT_visibility_off_19',
                "command": 'visibility_off'
            }
        ]
    },
    {
        "identifier": 'EVENT_1364_pause_70',
        "command": 'pause',
        "args": [15]
    },
    {
        "identifier": 'EVENT_1364_enter_area_71',
        "command": 'enter_area',
        "args": [Rooms._054_BOOSTER_HILL_____DUMMY, RadialDirections.NORTHWEST, 7, 57, 0, [_0x68Flags.RUN_ENTRANCE_EVENT]]
    },
    {
        "identifier": 'EVENT_1364_ret_72',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_1364_jmp_if_bit_clear_73',
        "command": 'jmp_if_bit_clear',
        "args": [0x704c, 6, 'EVENT_1283_enter_area_0']
    },
    {
        "identifier": 'EVENT_1364_jmp_74',
        "command": 'jmp',
        "args": ['EVENT_1282_enter_area_0']
    }
]
