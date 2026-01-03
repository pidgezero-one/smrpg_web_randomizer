
from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data import items
script = [
    {
        "identifier": 'EVENT_1364_jmp_if_bit_set_0',
        "command": 'jmp_if_bit_set',
        "args": [0x704d, 7, 'EVENT_1364_jmp_if_bit_clear_72']
    },
    {
        "identifier": 'EVENT_1364_jmp_if_bit_set_1',
        "command": 'jmp_if_bit_set',
        "args": [0x7053, 5, 'EVENT_1364_fade_out_to_black_async_49']
    },
    {
        "identifier": 'EVENT_1364_jmp_if_bit_set_2',
        "command": 'jmp_if_bit_set',
        "args": [0x7053, 4, 'EVENT_1364_fade_out_to_black_async_49']
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
        "identifier": 'EVENT_1364_pause_11',
        "command": 'pause',
        "args": [80]
    },
    {
        "identifier": 'EVENT_1364_stop_music_12',
        "command": 'stop_music'
    },
    {
        "identifier": 'EVENT_1364_fade_out_music_to_volume_13',
        "command": 'fade_out_music_to_volume',
        "args": [0, 100]
    },
    {
        "identifier": 'EVENT_1364_pause_14',
        "command": 'pause',
        "args": [10]
    },
    {
        "identifier": 'EVENT_1364_run_dialog_15',
        "command": 'run_dialog',
        "args": [2770, AreaObjects.NPC_12, [_0x60Flags.CLOSABLE, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_1364_pause_16',
        "command": 'pause',
        "args": [25]
    },
    {
        "identifier": 'EVENT_1364_play_music_default_volume_17',
        "command": 'play_music_default_volume',
        "args": [Music._32_AND_MY_NAMES_BOOSTER]
    },
    {
        "identifier": 'EVENT_1364_pause_18',
        "command": 'pause',
        "args": [10]
    },
    {
        "identifier": 'EVENT_1364_unsync_dialog_19',
        "command": 'unsync_dialog'
    },
    {
        "identifier": 'EVENT_1364_close_dialog_20',
        "command": 'close_dialog'
    },
    {
        "identifier": 'EVENT_1364_pause_21',
        "command": 'pause',
        "args": [15]
    },
    {
        "identifier": 'EVENT_1364_action_queue_async_22',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_1364_action_queue_async_22_SUBSCRIPT_reset_properties_0',
                "command": 'reset_properties'
            },
            {
                "identifier": 'EVENT_1364_action_queue_async_22_SUBSCRIPT_face_northeast_1',
                "command": 'face_northeast'
            },
            {
                "identifier": 'EVENT_1364_action_queue_async_22_SUBSCRIPT_jump_to_height_2',
                "command": 'jump_to_height',
                "args": [96]
            }
        ]
    },
    {
        "identifier": 'EVENT_1364_pause_23',
        "command": 'pause',
        "args": [60]
    },
    {
        "identifier": 'EVENT_1364_run_dialog_24',
        "command": 'run_dialog',
        "args": [2771, AreaObjects.NPC_12, [_0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_1364_pause_script_resume_on_next_dialog_page_a_FD61_25',
        "command": 'pause_script_resume_on_next_dialog_page_a_FD61'
    },
    {
        "identifier": 'EVENT_1364_action_queue_async_26',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_1364_action_queue_async_26_SUBSCRIPT_face_southwest_0',
                "command": 'face_southwest'
            }
        ]
    },
    {
        "identifier": 'EVENT_1364_unsync_dialog_27',
        "command": 'unsync_dialog'
    },
    {
        "identifier": 'EVENT_1364_close_dialog_28',
        "command": 'close_dialog'
    },
    {
        "identifier": 'EVENT_1364_action_queue_async_29',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_1364_action_queue_async_29_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_1364_action_queue_async_29_SUBSCRIPT_set_animation_speed_1',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_1364_action_queue_async_29_SUBSCRIPT_pause_2',
                "command": 'pause',
                "args": [15]
            },
            {
                "identifier": 'EVENT_1364_action_queue_async_29_SUBSCRIPT_face_northeast_3',
                "command": 'face_northeast'
            },
            {
                "identifier": 'EVENT_1364_action_queue_async_29_SUBSCRIPT_pause_4',
                "command": 'pause',
                "args": [15]
            },
            {
                "identifier": 'EVENT_1364_action_queue_async_29_SUBSCRIPT_shift_northeast_steps_5',
                "command": 'shift_northeast_steps',
                "args": [3]
            },
            {
                "identifier": 'EVENT_1364_action_queue_async_29_SUBSCRIPT_shift_northeast_pixels_6',
                "command": 'shift_northeast_pixels',
                "args": [8]
            },
            {
                "identifier": 'EVENT_1364_action_queue_async_29_SUBSCRIPT_pause_7',
                "command": 'pause',
                "args": [7]
            },
            {
                "identifier": 'EVENT_1364_action_queue_async_29_SUBSCRIPT_set_sprite_sequence_8',
                "command": 'set_sprite_sequence',
                "args": [10, 0, [_0x08Flags.READ_AS_MOLD, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_1364_action_queue_async_29_SUBSCRIPT_pause_9',
                "command": 'pause',
                "args": [7]
            },
            {
                "identifier": 'EVENT_1364_action_queue_async_29_SUBSCRIPT_set_sprite_sequence_10',
                "command": 'set_sprite_sequence',
                "args": [11, 0, [_0x08Flags.READ_AS_MOLD, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_1364_action_queue_async_29_SUBSCRIPT_pause_11',
                "command": 'pause',
                "args": [15]
            },
            {
                "identifier": 'EVENT_1364_action_queue_async_29_SUBSCRIPT_set_sprite_sequence_12',
                "command": 'set_sprite_sequence',
                "args": [9, 0, [_0x08Flags.READ_AS_MOLD]]
            },
            {
                "identifier": 'EVENT_1364_action_queue_async_29_SUBSCRIPT_pause_13',
                "command": 'pause',
                "args": [7]
            },
            {
                "identifier": 'EVENT_1364_action_queue_async_29_SUBSCRIPT_set_sprite_sequence_14',
                "command": 'set_sprite_sequence',
                "args": [8, 0, [_0x08Flags.READ_AS_MOLD]]
            },
            {
                "identifier": 'EVENT_1364_action_queue_async_29_SUBSCRIPT_pause_15',
                "command": 'pause',
                "args": [30]
            },
            {
                "identifier": 'EVENT_1364_action_queue_async_29_SUBSCRIPT_reset_properties_16',
                "command": 'reset_properties'
            },
            {
                "identifier": 'EVENT_1364_action_queue_async_29_SUBSCRIPT_face_northwest_17',
                "command": 'face_northwest'
            },
            {
                "identifier": 'EVENT_1364_action_queue_async_29_SUBSCRIPT_pause_18',
                "command": 'pause',
                "args": [20]
            },
            {
                "identifier": 'EVENT_1364_action_queue_async_29_SUBSCRIPT_set_priority_19',
                "command": 'set_priority',
                "args": [3]
            },
            {
                "identifier": 'EVENT_1364_action_queue_async_29_SUBSCRIPT_clear_solidity_bits_20',
                "command": 'clear_solidity_bits',
                "args": [[_0x0AFlags.CANT_PASS_WALLS]]
            },
            {
                "identifier": 'EVENT_1364_action_queue_async_29_SUBSCRIPT_shift_northwest_steps_21',
                "command": 'shift_northwest_steps',
                "args": [3]
            },
            {
                "identifier": 'EVENT_1364_action_queue_async_29_SUBSCRIPT_shift_northwest_pixels_22',
                "command": 'shift_northwest_pixels',
                "args": [7]
            }
        ]
    },
    {
        "identifier": 'EVENT_1364_pause_30',
        "command": 'pause',
        "args": [20]
    },
    {
        "identifier": 'EVENT_1364_play_sound_31',
        "command": 'play_sound',
        "args": [Sounds._090_CURTAIN, 6]
    },
    {
        "identifier": 'EVENT_1364_apply_tile_mod_32',
        "command": 'apply_tile_mod',
        "args": [Rooms._192_BOOSTER_TOWER_9F_AREA_02_BOOSTERS_CURTAIN_GAME_ROOM, 37, [_0x6AFlags.USE_ALTERNATE]]
    },
    {
        "identifier": 'EVENT_1364_pause_33',
        "command": 'pause',
        "args": [2]
    },
    {
        "identifier": 'EVENT_1364_apply_tile_mod_34',
        "command": 'apply_tile_mod',
        "args": [Rooms._192_BOOSTER_TOWER_9F_AREA_02_BOOSTERS_CURTAIN_GAME_ROOM, 38, [_0x6AFlags.USE_ALTERNATE]]
    },
    {
        "identifier": 'EVENT_1364_pause_35',
        "command": 'pause',
        "args": [2]
    },
    {
        "identifier": 'EVENT_1364_apply_tile_mod_36',
        "command": 'apply_tile_mod',
        "args": [Rooms._192_BOOSTER_TOWER_9F_AREA_02_BOOSTERS_CURTAIN_GAME_ROOM, 39, [_0x6AFlags.USE_ALTERNATE]]
    },
    {
        "identifier": 'EVENT_1364_pause_37',
        "command": 'pause',
        "args": [2]
    },
    {
        "identifier": 'EVENT_1364_pause_38',
        "command": 'pause',
        "args": [15]
    },
    {
        "identifier": 'EVENT_1364_action_queue_async_39',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_1364_action_queue_async_39_SUBSCRIPT_shift_northwest_pixels_0',
                "command": 'shift_northwest_pixels',
                "args": [20]
            },
            {
                "identifier": 'EVENT_1364_action_queue_async_39_SUBSCRIPT_set_priority_1',
                "command": 'set_priority',
                "args": [2]
            },
            {
                "identifier": 'EVENT_1364_action_queue_async_39_SUBSCRIPT_pause_2',
                "command": 'pause',
                "args": [15]
            },
            {
                "identifier": 'EVENT_1364_action_queue_async_39_SUBSCRIPT_face_southeast_3',
                "command": 'face_southeast'
            },
            {
                "identifier": 'EVENT_1364_action_queue_async_39_SUBSCRIPT_pause_4',
                "command": 'pause',
                "args": [10]
            },
            {
                "identifier": 'EVENT_1364_action_queue_async_39_SUBSCRIPT_set_solidity_bits_5',
                "command": 'set_solidity_bits',
                "args": [[_0x0AFlags.CANT_PASS_WALLS]]
            },
            {
                "identifier": 'EVENT_1364_action_queue_async_39_SUBSCRIPT_set_animation_speed_6',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING, _0x10Flags.SEQUENCE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_1364_play_sound_40',
        "command": 'play_sound',
        "args": [Sounds._090_CURTAIN, 6]
    },
    {
        "identifier": 'EVENT_1364_apply_tile_mod_41',
        "command": 'apply_tile_mod',
        "args": [Rooms._192_BOOSTER_TOWER_9F_AREA_02_BOOSTERS_CURTAIN_GAME_ROOM, 38, [_0x6AFlags.USE_ALTERNATE]]
    },
    {
        "identifier": 'EVENT_1364_pause_42',
        "command": 'pause',
        "args": [2]
    },
    {
        "identifier": 'EVENT_1364_apply_tile_mod_43',
        "command": 'apply_tile_mod',
        "args": [Rooms._192_BOOSTER_TOWER_9F_AREA_02_BOOSTERS_CURTAIN_GAME_ROOM, 37, [_0x6AFlags.USE_ALTERNATE]]
    },
    {
        "identifier": 'EVENT_1364_pause_44',
        "command": 'pause',
        "args": [2]
    },
    {
        "identifier": 'EVENT_1364_apply_tile_mod_45',
        "command": 'apply_tile_mod',
        "args": [Rooms._192_BOOSTER_TOWER_9F_AREA_02_BOOSTERS_CURTAIN_GAME_ROOM, 36, [_0x6AFlags.USE_ALTERNATE]]
    },
    {
        "identifier": 'EVENT_1364_pause_46',
        "command": 'pause',
        "args": [2]
    },
    {
        "identifier": 'EVENT_1364_jmp_47',
        "command": 'jmp',
        "args": ['EVENT_1358_remove_from_level_0']
    },
    {
        "identifier": 'EVENT_1364_ret_48',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_1364_fade_out_to_black_async_49',
        "command": 'fade_out_to_black_async'
    },
    {
        "identifier": 'EVENT_1364_fade_out_music_to_volume_50',
        "command": 'fade_out_music_to_volume',
        "args": [0, 0]
    },
    {
        "identifier": 'EVENT_1364_start_battle_51',
        "command": 'start_battle',
        "args": [0x00b1, 17]
    },
    {
        "identifier": 'EVENT_1364_jmp_if_bit_clear_52',
        "command": 'jmp_if_bit_clear',
        "args": [0x7040, 0, 'EVENT_1364_fade_out_music_to_volume_54']
    },
    {
        "identifier": 'EVENT_1364_reset_and_choose_game_53',
        "command": 'reset_and_choose_game'
    },
    {
        "identifier": 'EVENT_1364_fade_out_music_to_volume_54',
        "command": 'fade_out_music_to_volume',
        "args": [0, 0]
    },
    {
        "identifier": 'EVENT_1364_remove_from_level_55',
        "command": 'remove_from_level',
        "args": [AreaObjects.NPC_4, Rooms._039_BOOSTER_TOWER_5F_KNIFE_GUYS_JUGGLING_ROOM]
    },
    {
        "identifier": 'EVENT_1364_set_bit_56',
        "command": 'set_bit',
        "args": [0x7048, 6]
    },
    {
        "identifier": 'EVENT_1364_set_bit_57',
        "command": 'set_bit',
        "args": [0x7053, 7]
    },
    {
        "identifier": 'EVENT_1364_set_bit_58',
        "command": 'set_bit',
        "args": [0x7089, 2]
    },
    {
        "identifier": 'EVENT_1364_enter_area_59',
        "command": 'enter_area',
        "args": [Rooms._202_BOOSTER_TOWER_ENTRANCE, RadialDirections.SOUTHWEST, 5, 114, 23, []]
    },
    {
        "identifier": 'EVENT_1364_play_music_default_volume_60',
        "command": 'play_music_default_volume',
        "args": [Music._37_BOOSTER_HILL_START]
    },
    {
        "identifier": 'EVENT_1364_remove_from_current_level_61',
        "command": 'remove_from_current_level',
        "args": [AreaObjects.NPC_0]
    },
    {
        "identifier": 'EVENT_1364_fade_in_from_black_async_62',
        "command": 'fade_in_from_black_async'
    },
    {
        "identifier": 'EVENT_1364_play_sound_63',
        "command": 'play_sound',
        "args": [Sounds._019_LONG_FALL, 6]
    },
    {
        "identifier": 'EVENT_1364_pause_64',
        "command": 'pause',
        "args": [50]
    },
    {
        "identifier": 'EVENT_1364_freeze_camera_65',
        "command": 'freeze_camera'
    },
    {
        "identifier": 'EVENT_1364_action_queue_async_66',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_1364_action_queue_async_66_SUBSCRIPT_play_sound_0',
                "command": 'play_sound',
                "args": [Sounds._058_INSERT, 6]
            },
            {
                "identifier": 'EVENT_1364_action_queue_async_66_SUBSCRIPT_pause_1',
                "command": 'pause',
                "args": [45]
            },
            {
                "identifier": 'EVENT_1364_action_queue_async_66_SUBSCRIPT_set_sprite_sequence_2',
                "command": 'set_sprite_sequence',
                "args": [8, 0, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_1364_action_queue_async_66_SUBSCRIPT_pause_3',
                "command": 'pause',
                "args": [10]
            },
            {
                "identifier": 'EVENT_1364_action_queue_async_66_SUBSCRIPT_set_sprite_sequence_4',
                "command": 'set_sprite_sequence',
                "args": [9, 0, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_1364_action_queue_async_66_SUBSCRIPT_pause_5',
                "command": 'pause',
                "args": [10]
            },
            {
                "identifier": 'EVENT_1364_action_queue_async_66_SUBSCRIPT_set_sprite_sequence_6',
                "command": 'set_sprite_sequence',
                "args": [8, 0, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_1364_action_queue_async_66_SUBSCRIPT_pause_7',
                "command": 'pause',
                "args": [25]
            },
            {
                "identifier": 'EVENT_1364_action_queue_async_66_SUBSCRIPT_reset_properties_8',
                "command": 'reset_properties'
            },
            {
                "identifier": 'EVENT_1364_action_queue_async_66_SUBSCRIPT_pause_9',
                "command": 'pause',
                "args": [30]
            },
            {
                "identifier": 'EVENT_1364_action_queue_async_66_SUBSCRIPT_set_animation_speed_10',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_1364_action_queue_async_66_SUBSCRIPT_sequence_looping_on_11',
                "command": 'sequence_looping_on'
            },
            {
                "identifier": 'EVENT_1364_action_queue_async_66_SUBSCRIPT_fixed_f_coord_on_12',
                "command": 'fixed_f_coord_on'
            },
            {
                "identifier": 'EVENT_1364_action_queue_async_66_SUBSCRIPT_set_animation_speed_13',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.SLOW, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_1364_action_queue_async_66_SUBSCRIPT_play_sound_14',
                "command": 'play_sound',
                "args": [Sounds._024_TAPPING_FEET, 6]
            },
            {
                "identifier": 'EVENT_1364_action_queue_async_66_SUBSCRIPT_shift_northeast_pixels_15',
                "command": 'shift_northeast_pixels',
                "args": [24]
            },
            {
                "identifier": 'EVENT_1364_action_queue_async_66_SUBSCRIPT_jump_to_height_silent_16',
                "command": 'jump_to_height_silent',
                "args": [69]
            },
            {
                "identifier": 'EVENT_1364_action_queue_async_66_SUBSCRIPT_pause_17',
                "command": 'pause',
                "args": [15]
            },
            {
                "identifier": 'EVENT_1364_action_queue_async_66_SUBSCRIPT_play_sound_18',
                "command": 'play_sound',
                "args": [Sounds._011_WHOOSH_AWAY, 6]
            },
            {
                "identifier": 'EVENT_1364_action_queue_async_66_SUBSCRIPT_set_animation_speed_19',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FASTEST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_1364_action_queue_async_66_SUBSCRIPT_set_animation_speed_20',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_1364_action_queue_async_66_SUBSCRIPT_shift_southwest_steps_21',
                "command": 'shift_southwest_steps',
                "args": [8]
            },
            {
                "identifier": 'EVENT_1364_action_queue_async_66_SUBSCRIPT_visibility_off_22',
                "command": 'visibility_off'
            }
        ]
    },
    {
        "identifier": 'EVENT_1364_pause_67',
        "command": 'pause',
        "args": [15]
    },
    {
        "identifier": 'EVENT_1364_restore_all_hp_68',
        "command": 'restore_all_hp'
    },
    {
        "identifier": 'EVENT_1364_restore_all_fp_69',
        "command": 'restore_all_fp'
    },
    {
        "identifier": 'EVENT_1364_enter_area_70',
        "command": 'enter_area',
        "args": [Rooms._054_BOOSTER_HILL_____DUMMY, RadialDirections.NORTHWEST, 7, 57, 0, [_0x68Flags.RUN_ENTRANCE_EVENT]]
    },
    {
        "identifier": 'EVENT_1364_ret_71',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_1364_jmp_if_bit_clear_72',
        "command": 'jmp_if_bit_clear',
        "args": [0x704c, 6, 'EVENT_1283_enter_area_0']
    },
    {
        "identifier": 'EVENT_1364_jmp_73',
        "command": 'jmp',
        "args": ['EVENT_1282_enter_area_0']
    }
]
