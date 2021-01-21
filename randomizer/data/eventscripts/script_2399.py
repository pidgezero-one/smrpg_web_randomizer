from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data import items
script = [
    {
        "identifier": 'EVENT_2399_set_0',
        "command": 'set',
        "args": [0x70df, 55]
    },
    {
        "identifier": 'EVENT_2399_action_queue_async_1',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_2],
        "subscript": [
            {
                "identifier": 'EVENT_2399_action_queue_async_1_SUBSCRIPT_set_sprite_sequence_0',
                "command": 'set_sprite_sequence',
                "args": [28, 1, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_2399_action_queue_async_1_SUBSCRIPT_pause_1',
                "command": 'pause',
                "args": [2]
            },
            {
                "identifier": 'EVENT_2399_action_queue_async_1_SUBSCRIPT_reset_properties_2',
                "command": 'reset_properties'
            }
        ]
    },
    {
        "identifier": 'EVENT_2399_set_2',
        "command": 'set',
        "args": [0x70c0, 219]
    },
    {
        "identifier": 'EVENT_2399_action_queue_async_3',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_0],
        "subscript": [
            {
                "identifier": 'EVENT_2399_action_queue_async_3_SUBSCRIPT_shift_northwest_pixels_0',
                "command": 'shift_northwest_pixels',
                "args": [12]
            }
        ]
    },
    {
        "identifier": 'EVENT_2399_jmp_if_bit_clear_4',
        "command": 'jmp_if_bit_clear',
        "args": [0x708f, 3, 'EVENT_2399_fade_in_music_8']
    },
    {
        "identifier": 'EVENT_2399_clear_bit_5',
        "command": 'clear_bit',
        "args": [0x708f, 3]
    },
    {
        "identifier": 'EVENT_2399_fade_in_from_black_async_6',
        "command": 'fade_in_from_black_async'
    },
    {
        "identifier": 'EVENT_2399_ret_7',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_2399_fade_in_music_8',
        "command": 'fade_in_music',
        "args": [Music._65_GATE]
    },
    {
        "identifier": 'EVENT_2399_jmp_9',
        "command": 'jmp',
        "args": ['EVENT_2399_freeze_camera_11']
    },
    {
        "identifier": 'EVENT_2399_fade_in_music_10',
        "command": 'fade_in_music',
        "args": [Music._67_WEAPONS_FACTORY]
    },
    {
        "identifier": 'EVENT_2399_freeze_camera_11',
        "command": 'freeze_camera'
    },
    {
        "identifier": 'EVENT_2399_play_sound_12',
        "command": 'play_sound',
        "args": [Sounds._019_LONG_FALL, 6]
    },
    {
        "identifier": 'EVENT_2399_action_queue_sync_13',
        "command": 'action_queue_sync',
        "args": [AreaObjects.SCREEN_FOCUS],
        "subscript": [
            {
                "identifier": 'EVENT_2399_action_queue_sync_13_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FASTEST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_2399_action_queue_sync_13_SUBSCRIPT_walk_to_xy_coords_1',
                "command": 'walk_to_xy_coords',
                "args": [2, 10]
            }
        ]
    },
    {
        "identifier": 'EVENT_2399_action_queue_async_14',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_2399_action_queue_async_14_SUBSCRIPT_floating_off_0',
                "command": 'floating_off'
            },
            {
                "identifier": 'EVENT_2399_action_queue_async_14_SUBSCRIPT_transfer_to_xyzf_1',
                "command": 'transfer_to_xyzf',
                "args": [4, 25, 21, RadialDirections.EAST]
            },
            {
                "identifier": 'EVENT_2399_action_queue_async_14_SUBSCRIPT_shift_south_pixels_2',
                "command": 'shift_south_pixels',
                "args": [8]
            }
        ]
    },
    {
        "identifier": 'EVENT_2399_fade_in_from_black_async_15',
        "command": 'fade_in_from_black_async'
    },
    {
        "identifier": 'EVENT_2399_action_queue_async_16',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_2399_action_queue_async_16_SUBSCRIPT_floating_on_0',
                "command": 'floating_on'
            },
            {
                "identifier": 'EVENT_2399_action_queue_async_16_SUBSCRIPT_jump_to_height_silent_1',
                "command": 'jump_to_height_silent',
                "args": [0]
            },
            {
                "identifier": 'EVENT_2399_action_queue_async_16_SUBSCRIPT_set_sprite_sequence_2',
                "command": 'set_sprite_sequence',
                "args": [0, 1, [_0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_2399_action_queue_async_16_SUBSCRIPT_pause_3',
                "command": 'pause',
                "args": [1]
            },
            {
                "identifier": 'EVENT_2399_action_queue_async_16_SUBSCRIPT_jmp_if_mario_in_air_4',
                "command": 'jmp_if_mario_in_air',
                "args": ['EVENT_2399_action_queue_async_16_SUBSCRIPT_pause_3']
            },
            {
                "identifier": 'EVENT_2399_action_queue_async_16_SUBSCRIPT_play_sound_5',
                "command": 'play_sound',
                "args": [Sounds._058_INSERT, 4]
            }
        ]
    },
    {
        "identifier": 'EVENT_2399_set_action_script_async_17',
        "command": 'set_action_script_async',
        "args": [AreaObjects.MARIO, 395]
    },
    {
        "identifier": 'EVENT_2399_jmp_18',
        "command": 'jmp',
        "args": ['EVENT_2399_unfreeze_camera_109']
    },
    {
        "identifier": 'EVENT_2399_pause_19',
        "command": 'pause',
        "args": [24]
    },
    {
        "identifier": 'EVENT_2399_summon_to_current_level_at_marios_coords_20',
        "command": 'summon_to_current_level_at_marios_coords',
        "args": [AreaObjects.NPC_2]
    },
    {
        "identifier": 'EVENT_2399_action_queue_sync_21',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_2399_action_queue_sync_21_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [24]
            },
            {
                "identifier": 'EVENT_2399_action_queue_sync_21_SUBSCRIPT_face_northeast_1',
                "command": 'face_northeast'
            }
        ]
    },
    {
        "identifier": 'EVENT_2399_action_queue_async_22',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_2],
        "subscript": [
            {
                "identifier": 'EVENT_2399_action_queue_async_22_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.SLOW, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_2399_action_queue_async_22_SUBSCRIPT_shift_northeast_steps_1',
                "command": 'shift_northeast_steps',
                "args": [2]
            },
            {
                "identifier": 'EVENT_2399_action_queue_async_22_SUBSCRIPT_shift_northeast_pixels_2',
                "command": 'shift_northeast_pixels',
                "args": [8]
            },
            {
                "identifier": 'EVENT_2399_action_queue_async_22_SUBSCRIPT_pause_3',
                "command": 'pause',
                "args": [10]
            },
            {
                "identifier": 'EVENT_2399_action_queue_async_22_SUBSCRIPT_set_animation_speed_4',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.SLOW, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_2399_action_queue_async_22_SUBSCRIPT_set_sprite_sequence_5',
                "command": 'set_sprite_sequence',
                "args": [9, 0, [_0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_2399_pause_23',
        "command": 'pause',
        "args": [8]
    },
    {
        "identifier": 'EVENT_2399_run_dialog_24',
        "command": 'run_dialog',
        "args": [3128, AreaObjects.NPC_12, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_2399_pause_25',
        "command": 'pause',
        "args": [16]
    },
    {
        "identifier": 'EVENT_2399_action_queue_async_26',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_2],
        "subscript": [
            {
                "identifier": 'EVENT_2399_action_queue_async_26_SUBSCRIPT_reset_properties_0',
                "command": 'reset_properties'
            },
            {
                "identifier": 'EVENT_2399_action_queue_async_26_SUBSCRIPT_pause_1',
                "command": 'pause',
                "args": [24]
            },
            {
                "identifier": 'EVENT_2399_action_queue_async_26_SUBSCRIPT_face_southwest_2',
                "command": 'face_southwest'
            }
        ]
    },
    {
        "identifier": 'EVENT_2399_run_dialog_27',
        "command": 'run_dialog',
        "args": [3129, AreaObjects.NPC_12, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_2399_set_action_script_async_28',
        "command": 'set_action_script_async',
        "args": [AreaObjects.NPC_2, 854]
    },
    {
        "identifier": 'EVENT_2399_run_dialog_29',
        "command": 'run_dialog',
        "args": [3130, AreaObjects.NPC_12, [_0x60Flags.CLOSABLE, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_2399_pause_script_resume_on_next_dialog_page_a_30',
        "command": 'pause_script_resume_on_next_dialog_page_a'
    },
    {
        "identifier": 'EVENT_2399_action_queue_async_31',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_2],
        "subscript": [
            {
                "identifier": 'EVENT_2399_action_queue_async_31_SUBSCRIPT_set_sprite_sequence_0',
                "command": 'set_sprite_sequence',
                "args": [16, 0, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_2399_unsync_dialog_32',
        "command": 'unsync_dialog'
    },
    {
        "identifier": 'EVENT_2399_play_sound_33',
        "command": 'play_sound',
        "args": [Sounds._026_LAUGHING_BOWSER, 6]
    },
    {
        "identifier": 'EVENT_2399_run_dialog_34',
        "command": 'run_dialog',
        "args": [3131, AreaObjects.NPC_12, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_2399_summon_to_current_level_at_marios_coords_35',
        "command": 'summon_to_current_level_at_marios_coords',
        "args": [AreaObjects.NPC_1]
    },
    {
        "identifier": 'EVENT_2399_action_queue_sync_36',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_2399_action_queue_sync_36_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [16]
            },
            {
                "identifier": 'EVENT_2399_action_queue_sync_36_SUBSCRIPT_face_southeast_1',
                "command": 'face_southeast'
            }
        ]
    },
    {
        "identifier": 'EVENT_2399_action_queue_sync_37',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_2],
        "subscript": [
            {
                "identifier": 'EVENT_2399_action_queue_sync_37_SUBSCRIPT_reset_properties_0',
                "command": 'reset_properties'
            }
        ]
    },
    {
        "identifier": 'EVENT_2399_action_queue_async_38',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_1],
        "subscript": [
            {
                "identifier": 'EVENT_2399_action_queue_async_38_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.SLOW, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_2399_action_queue_async_38_SUBSCRIPT_walk_1_step_southeast_1',
                "command": 'walk_1_step_southeast'
            },
            {
                "identifier": 'EVENT_2399_action_queue_async_38_SUBSCRIPT_shift_southeast_pixels_2',
                "command": 'shift_southeast_pixels',
                "args": [12]
            },
            {
                "identifier": 'EVENT_2399_action_queue_async_38_SUBSCRIPT_face_northeast_3',
                "command": 'face_northeast'
            },
            {
                "identifier": 'EVENT_2399_action_queue_async_38_SUBSCRIPT_set_sprite_sequence_4',
                "command": 'set_sprite_sequence',
                "args": [5, 0, [_0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_2399_run_dialog_39',
        "command": 'run_dialog',
        "args": [3132, AreaObjects.NPC_12, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_2399_action_queue_async_40',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_1],
        "subscript": [
            {
                "identifier": 'EVENT_2399_action_queue_async_40_SUBSCRIPT_reset_properties_0',
                "command": 'reset_properties'
            },
            {
                "identifier": 'EVENT_2399_action_queue_async_40_SUBSCRIPT_face_east_1',
                "command": 'face_east'
            },
            {
                "identifier": 'EVENT_2399_action_queue_async_40_SUBSCRIPT_pause_2',
                "command": 'pause',
                "args": [4]
            },
            {
                "identifier": 'EVENT_2399_action_queue_async_40_SUBSCRIPT_face_southeast_3',
                "command": 'face_southeast'
            },
            {
                "identifier": 'EVENT_2399_action_queue_async_40_SUBSCRIPT_pause_4',
                "command": 'pause',
                "args": [4]
            },
            {
                "identifier": 'EVENT_2399_action_queue_async_40_SUBSCRIPT_face_south_5',
                "command": 'face_south'
            },
            {
                "identifier": 'EVENT_2399_action_queue_async_40_SUBSCRIPT_pause_6',
                "command": 'pause',
                "args": [4]
            },
            {
                "identifier": 'EVENT_2399_action_queue_async_40_SUBSCRIPT_face_southwest_7',
                "command": 'face_southwest'
            }
        ]
    },
    {
        "identifier": 'EVENT_2399_run_dialog_41',
        "command": 'run_dialog',
        "args": [3133, AreaObjects.NPC_12, [_0x60Flags.CLOSABLE, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_2399_pause_script_resume_on_next_dialog_page_a_42',
        "command": 'pause_script_resume_on_next_dialog_page_a'
    },
    {
        "identifier": 'EVENT_2399_action_queue_async_43',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_1],
        "subscript": [
            {
                "identifier": 'EVENT_2399_action_queue_async_43_SUBSCRIPT_set_sprite_sequence_0',
                "command": 'set_sprite_sequence',
                "args": [16, 0, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_2399_unsync_dialog_44',
        "command": 'unsync_dialog'
    },
    {
        "identifier": 'EVENT_2399_action_queue_async_45',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_1],
        "subscript": [
            {
                "identifier": 'EVENT_2399_action_queue_async_45_SUBSCRIPT_set_sprite_sequence_0',
                "command": 'set_sprite_sequence',
                "args": [5, 0, [_0x08Flags.READ_AS_SEQUENCE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_2399_action_queue_sync_46',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_2399_action_queue_sync_46_SUBSCRIPT_set_sprite_sequence_0',
                "command": 'set_sprite_sequence',
                "args": [0, 3, [_0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_2399_run_dialog_47',
        "command": 'run_dialog',
        "args": [3134, AreaObjects.NPC_12, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_2399_pause_48',
        "command": 'pause',
        "args": [8]
    },
    {
        "identifier": 'EVENT_2399_action_queue_async_49',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_2],
        "subscript": [
            {
                "identifier": 'EVENT_2399_action_queue_async_49_SUBSCRIPT_set_sprite_sequence_0',
                "command": 'set_sprite_sequence',
                "args": [2, 0, [_0x08Flags.READ_AS_SEQUENCE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_2399_run_dialog_50',
        "command": 'run_dialog',
        "args": [3135, AreaObjects.NPC_12, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_2399_action_queue_async_51',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_1],
        "subscript": [
            {
                "identifier": 'EVENT_2399_action_queue_async_51_SUBSCRIPT_set_sprite_sequence_0',
                "command": 'set_sprite_sequence',
                "args": [12, 0, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_2399_action_queue_sync_52',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_2399_action_queue_sync_52_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [48]
            },
            {
                "identifier": 'EVENT_2399_action_queue_sync_52_SUBSCRIPT_face_northeast_1',
                "command": 'face_northeast'
            },
            {
                "identifier": 'EVENT_2399_action_queue_sync_52_SUBSCRIPT_reset_properties_2',
                "command": 'reset_properties'
            }
        ]
    },
    {
        "identifier": 'EVENT_2399_run_dialog_53',
        "command": 'run_dialog',
        "args": [3136, AreaObjects.NPC_12, [_0x60Flags.CLOSABLE, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_2399_pause_script_resume_on_next_dialog_page_a_54',
        "command": 'pause_script_resume_on_next_dialog_page_a'
    },
    {
        "identifier": 'EVENT_2399_action_queue_async_55',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_1],
        "subscript": [
            {
                "identifier": 'EVENT_2399_action_queue_async_55_SUBSCRIPT_face_northeast_0',
                "command": 'face_northeast'
            },
            {
                "identifier": 'EVENT_2399_action_queue_async_55_SUBSCRIPT_reset_properties_1',
                "command": 'reset_properties'
            }
        ]
    },
    {
        "identifier": 'EVENT_2399_unsync_dialog_56',
        "command": 'unsync_dialog'
    },
    {
        "identifier": 'EVENT_2399_pause_57',
        "command": 'pause',
        "args": [8]
    },
    {
        "identifier": 'EVENT_2399_action_queue_async_58',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_2],
        "subscript": [
            {
                "identifier": 'EVENT_2399_action_queue_async_58_SUBSCRIPT_reset_properties_0',
                "command": 'reset_properties'
            }
        ]
    },
    {
        "identifier": 'EVENT_2399_run_dialog_59',
        "command": 'run_dialog',
        "args": [3137, AreaObjects.NPC_12, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_2399_action_queue_sync_60',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_1],
        "subscript": [
            {
                "identifier": 'EVENT_2399_action_queue_sync_60_SUBSCRIPT_set_sprite_sequence_0',
                "command": 'set_sprite_sequence',
                "args": [7, 1, [_0x08Flags.READ_AS_SEQUENCE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_2399_run_dialog_61',
        "command": 'run_dialog',
        "args": [3138, AreaObjects.NPC_12, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_2399_action_queue_sync_62',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_1],
        "subscript": [
            {
                "identifier": 'EVENT_2399_action_queue_sync_62_SUBSCRIPT_reset_properties_0',
                "command": 'reset_properties'
            }
        ]
    },
    {
        "identifier": 'EVENT_2399_pause_63',
        "command": 'pause',
        "args": [8]
    },
    {
        "identifier": 'EVENT_2399_action_queue_sync_64',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_2],
        "subscript": [
            {
                "identifier": 'EVENT_2399_action_queue_sync_64_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [16]
            },
            {
                "identifier": 'EVENT_2399_action_queue_sync_64_SUBSCRIPT_set_sprite_sequence_1',
                "command": 'set_sprite_sequence',
                "args": [6, 0, [_0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_2399_action_queue_sync_64_SUBSCRIPT_pause_2',
                "command": 'pause',
                "args": [64]
            },
            {
                "identifier": 'EVENT_2399_action_queue_sync_64_SUBSCRIPT_reset_properties_3',
                "command": 'reset_properties'
            }
        ]
    },
    {
        "identifier": 'EVENT_2399_run_dialog_65',
        "command": 'run_dialog',
        "args": [3139, AreaObjects.NPC_12, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_2399_set_action_script_sync_66',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_2, 854]
    },
    {
        "identifier": 'EVENT_2399_run_dialog_67',
        "command": 'run_dialog',
        "args": [3140, AreaObjects.NPC_12, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_2399_pause_68',
        "command": 'pause',
        "args": [16]
    },
    {
        "identifier": 'EVENT_2399_action_queue_async_69',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_2],
        "subscript": [
            {
                "identifier": 'EVENT_2399_action_queue_async_69_SUBSCRIPT_face_southwest_0',
                "command": 'face_southwest'
            },
            {
                "identifier": 'EVENT_2399_action_queue_async_69_SUBSCRIPT_reset_properties_1',
                "command": 'reset_properties'
            }
        ]
    },
    {
        "identifier": 'EVENT_2399_run_dialog_70',
        "command": 'run_dialog',
        "args": [3141, AreaObjects.NPC_12, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_2399_action_queue_async_71',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_2399_action_queue_async_71_SUBSCRIPT_face_southeast_0',
                "command": 'face_southeast'
            }
        ]
    },
    {
        "identifier": 'EVENT_2399_run_dialog_72',
        "command": 'run_dialog',
        "args": [3142, AreaObjects.NPC_12, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_2399_pause_73',
        "command": 'pause',
        "args": [16]
    },
    {
        "identifier": 'EVENT_2399_action_queue_async_74',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_1],
        "subscript": [
            {
                "identifier": 'EVENT_2399_action_queue_async_74_SUBSCRIPT_set_sprite_sequence_0',
                "command": 'set_sprite_sequence',
                "args": [10, 0, [_0x08Flags.READ_AS_SEQUENCE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_2399_run_dialog_75',
        "command": 'run_dialog',
        "args": [3142, AreaObjects.NPC_12, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_2399_pause_76',
        "command": 'pause',
        "args": [24]
    },
    {
        "identifier": 'EVENT_2399_run_dialog_77',
        "command": 'run_dialog',
        "args": [3146, AreaObjects.NPC_12, [_0x60Flags.CLOSABLE, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_2399_pause_script_resume_on_next_dialog_page_a_78',
        "command": 'pause_script_resume_on_next_dialog_page_a'
    },
    {
        "identifier": 'EVENT_2399_pause_script_resume_on_next_dialog_page_a_79',
        "command": 'pause_script_resume_on_next_dialog_page_a'
    },
    {
        "identifier": 'EVENT_2399_action_queue_sync_80',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_1],
        "subscript": [
            {
                "identifier": 'EVENT_2399_action_queue_sync_80_SUBSCRIPT_set_sprite_sequence_0',
                "command": 'set_sprite_sequence',
                "args": [13, 0, [_0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_2399_unsync_dialog_81',
        "command": 'unsync_dialog'
    },
    {
        "identifier": 'EVENT_2399_pause_82',
        "command": 'pause',
        "args": [16]
    },
    {
        "identifier": 'EVENT_2399_action_queue_async_83',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_1],
        "subscript": [
            {
                "identifier": 'EVENT_2399_action_queue_async_83_SUBSCRIPT_face_southeast_0',
                "command": 'face_southeast'
            },
            {
                "identifier": 'EVENT_2399_action_queue_async_83_SUBSCRIPT_reset_properties_1',
                "command": 'reset_properties'
            }
        ]
    },
    {
        "identifier": 'EVENT_2399_run_dialog_84',
        "command": 'run_dialog',
        "args": [3147, AreaObjects.NPC_12, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_2399_pause_85',
        "command": 'pause',
        "args": [16]
    },
    {
        "identifier": 'EVENT_2399_run_dialog_86',
        "command": 'run_dialog',
        "args": [3142, AreaObjects.NPC_12, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_2399_run_dialog_87',
        "command": 'run_dialog',
        "args": [3148, AreaObjects.NPC_12, [_0x60Flags.CLOSABLE, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_2399_action_queue_async_88',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_1],
        "subscript": [
            {
                "identifier": 'EVENT_2399_action_queue_async_88_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [8]
            },
            {
                "identifier": 'EVENT_2399_action_queue_async_88_SUBSCRIPT_set_sprite_sequence_1',
                "command": 'set_sprite_sequence',
                "args": [0, 2, [_0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_2399_action_queue_async_88_SUBSCRIPT_pause_2',
                "command": 'pause',
                "args": [32]
            },
            {
                "identifier": 'EVENT_2399_action_queue_async_88_SUBSCRIPT_reset_properties_3',
                "command": 'reset_properties'
            }
        ]
    },
    {
        "identifier": 'EVENT_2399_unsync_dialog_89',
        "command": 'unsync_dialog'
    },
    {
        "identifier": 'EVENT_2399_pause_90',
        "command": 'pause',
        "args": [32]
    },
    {
        "identifier": 'EVENT_2399_action_queue_sync_91',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_1],
        "subscript": [
            {
                "identifier": 'EVENT_2399_action_queue_sync_91_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.SLOW, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_2399_action_queue_sync_91_SUBSCRIPT_set_sprite_sequence_1',
                "command": 'set_sprite_sequence',
                "args": [10, 1, [_0x08Flags.LOOPING_OFF]]
            },
            {
                "identifier": 'EVENT_2399_action_queue_sync_91_SUBSCRIPT_pause_2',
                "command": 'pause',
                "args": [54]
            },
            {
                "identifier": 'EVENT_2399_action_queue_sync_91_SUBSCRIPT_set_sprite_sequence_3',
                "command": 'set_sprite_sequence',
                "args": [30, 1, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_2399_run_dialog_92',
        "command": 'run_dialog',
        "args": [3143, AreaObjects.NPC_12, [_0x60Flags.CLOSABLE, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_2399_pause_script_resume_on_next_dialog_page_a_93',
        "command": 'pause_script_resume_on_next_dialog_page_a'
    },
    {
        "identifier": 'EVENT_2399_action_queue_sync_94',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_1],
        "subscript": [
            {
                "identifier": 'EVENT_2399_action_queue_sync_94_SUBSCRIPT_set_sprite_sequence_0',
                "command": 'set_sprite_sequence',
                "args": [10, 0, [_0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_2399_action_queue_sync_94_SUBSCRIPT_pause_1',
                "command": 'pause',
                "args": [8]
            },
            {
                "identifier": 'EVENT_2399_action_queue_sync_94_SUBSCRIPT_set_sprite_sequence_2',
                "command": 'set_sprite_sequence',
                "args": [16, 0, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_2399_unsync_dialog_95',
        "command": 'unsync_dialog'
    },
    {
        "identifier": 'EVENT_2399_action_queue_async_96',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_1],
        "subscript": [
            {
                "identifier": 'EVENT_2399_action_queue_async_96_SUBSCRIPT_face_northwest_0',
                "command": 'face_northwest'
            },
            {
                "identifier": 'EVENT_2399_action_queue_async_96_SUBSCRIPT_reset_properties_1',
                "command": 'reset_properties'
            },
            {
                "identifier": 'EVENT_2399_action_queue_async_96_SUBSCRIPT_pause_2',
                "command": 'pause',
                "args": [8]
            }
        ]
    },
    {
        "identifier": 'EVENT_2399_run_dialog_97',
        "command": 'run_dialog',
        "args": [3144, AreaObjects.NPC_12, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_2399_action_queue_async_98',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_1],
        "subscript": [
            {
                "identifier": 'EVENT_2399_action_queue_async_98_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_2399_action_queue_async_98_SUBSCRIPT_walk_1_step_northwest_1',
                "command": 'walk_1_step_northwest'
            },
            {
                "identifier": 'EVENT_2399_action_queue_async_98_SUBSCRIPT_shift_northwest_pixels_2',
                "command": 'shift_northwest_pixels',
                "args": [10]
            },
            {
                "identifier": 'EVENT_2399_action_queue_async_98_SUBSCRIPT_visibility_off_3',
                "command": 'visibility_off'
            }
        ]
    },
    {
        "identifier": 'EVENT_2399_pause_99',
        "command": 'pause',
        "args": [32]
    },
    {
        "identifier": 'EVENT_2399_run_dialog_100',
        "command": 'run_dialog',
        "args": [3149, AreaObjects.NPC_12, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_2399_pause_101',
        "command": 'pause',
        "args": [16]
    },
    {
        "identifier": 'EVENT_2399_action_queue_async_102',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_2399_action_queue_async_102_SUBSCRIPT_face_northeast_0',
                "command": 'face_northeast'
            }
        ]
    },
    {
        "identifier": 'EVENT_2399_action_queue_sync_103',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_2],
        "subscript": [
            {
                "identifier": 'EVENT_2399_action_queue_sync_103_SUBSCRIPT_set_sprite_sequence_0',
                "command": 'set_sprite_sequence',
                "args": [2, 0, [_0x08Flags.READ_AS_SEQUENCE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_2399_run_dialog_104',
        "command": 'run_dialog',
        "args": [3145, AreaObjects.NPC_12, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_2399_pause_105',
        "command": 'pause',
        "args": [8]
    },
    {
        "identifier": 'EVENT_2399_action_queue_async_106',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_2],
        "subscript": [
            {
                "identifier": 'EVENT_2399_action_queue_async_106_SUBSCRIPT_reset_properties_0',
                "command": 'reset_properties'
            },
            {
                "identifier": 'EVENT_2399_action_queue_async_106_SUBSCRIPT_set_animation_speed_1',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_2399_action_queue_async_106_SUBSCRIPT_shift_southwest_steps_2',
                "command": 'shift_southwest_steps',
                "args": [2]
            },
            {
                "identifier": 'EVENT_2399_action_queue_async_106_SUBSCRIPT_shift_southwest_pixels_3',
                "command": 'shift_southwest_pixels',
                "args": [4]
            },
            {
                "identifier": 'EVENT_2399_action_queue_async_106_SUBSCRIPT_visibility_off_4',
                "command": 'visibility_off'
            }
        ]
    },
    {
        "identifier": 'EVENT_2399_set_action_script_async_107',
        "command": 'set_action_script_async',
        "args": [AreaObjects.MARIO, 395]
    },
    {
        "identifier": 'EVENT_2399_action_queue_async_108',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_2399_action_queue_async_108_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [16]
            },
            {
                "identifier": 'EVENT_2399_action_queue_async_108_SUBSCRIPT_face_south_1',
                "command": 'face_south'
            }
        ]
    },
    {
        "identifier": 'EVENT_2399_unfreeze_camera_109',
        "command": 'unfreeze_camera'
    },
    {
        "identifier": 'EVENT_2399_ret_110',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_2399_ret_111',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_2399_ret_112',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_2399_ret_113',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_2399_ret_114',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_2399_ret_115',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_2399_ret_116',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_2399_ret_117',
        "command": 'ret'
    }
]
