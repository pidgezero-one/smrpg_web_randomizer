from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data import items
script = [
    {
        "identifier": 'EVENT_1329_fade_in_from_black_async_0',
        "command": 'fade_in_from_black_async'
    },
    {
        "identifier": 'EVENT_1329_freeze_camera_1',
        "command": 'freeze_camera'
    },
    {
        "identifier": 'EVENT_1329_action_queue_async_2',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_1329_action_queue_async_2_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING, _0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_1329_action_queue_async_2_SUBSCRIPT_shift_northeast_pixels_1',
                "command": 'shift_northeast_pixels',
                "args": [4]
            },
            {
                "identifier": 'EVENT_1329_action_queue_async_2_SUBSCRIPT_set_animation_speed_2',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.SLOW, [_0x10Flags.WALKING, _0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_1329_action_queue_async_2_SUBSCRIPT_shift_northeast_pixels_3',
                "command": 'shift_northeast_pixels',
                "args": [4]
            }
        ]
    },
    {
        "identifier": 'EVENT_1329_pause_3',
        "command": 'pause',
        "args": [30]
    },
    {
        "identifier": 'EVENT_1329_action_queue_async_4',
        "command": 'action_queue_async',
        "args": [AreaObjects.SCREEN_FOCUS],
        "subscript": [
            {
                "identifier": 'EVENT_1329_action_queue_async_4_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_1329_action_queue_async_4_SUBSCRIPT_shift_north_steps_1',
                "command": 'shift_north_steps',
                "args": [3]
            }
        ]
    },
    {
        "identifier": 'EVENT_1329_pause_5',
        "command": 'pause',
        "args": [20]
    },
    {
        "identifier": 'EVENT_1329_run_dialog_6',
        "command": 'run_dialog',
        "args": [2806, AreaObjects.NPC_12, [_0x60Flags.CLOSABLE, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_1329_pause_script_resume_on_next_dialog_page_a_7',
        "command": 'pause_script_resume_on_next_dialog_page_a'
    },
    {
        "identifier": 'EVENT_1329_pause_script_resume_on_next_dialog_page_a_8',
        "command": 'pause_script_resume_on_next_dialog_page_a'
    },
    {
        "identifier": 'EVENT_1329_action_queue_async_9',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_0],
        "subscript": [
            {
                "identifier": 'EVENT_1329_action_queue_async_9_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_1329_action_queue_async_9_SUBSCRIPT_set_sprite_sequence_1',
                "command": 'set_sprite_sequence',
                "args": [14, 0, [_0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_1329_unsync_dialog_10',
        "command": 'unsync_dialog'
    },
    {
        "identifier": 'EVENT_1329_close_dialog_11',
        "command": 'close_dialog'
    },
    {
        "identifier": 'EVENT_1329_pause_12',
        "command": 'pause',
        "args": [60]
    },
    {
        "identifier": 'EVENT_1329_action_queue_async_13',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_0],
        "subscript": [
            {
                "identifier": 'EVENT_1329_action_queue_async_13_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_1329_action_queue_async_13_SUBSCRIPT_set_sprite_sequence_1',
                "command": 'set_sprite_sequence',
                "args": [13, 0, [_0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_1329_action_queue_async_13_SUBSCRIPT_pause_2',
                "command": 'pause',
                "args": [55]
            },
            {
                "identifier": 'EVENT_1329_action_queue_async_13_SUBSCRIPT_set_sprite_sequence_3',
                "command": 'set_sprite_sequence',
                "args": [21, 0, [_0x08Flags.READ_AS_MOLD]]
            },
            {
                "identifier": 'EVENT_1329_action_queue_async_13_SUBSCRIPT_pause_4',
                "command": 'pause',
                "args": [40]
            },
            {
                "identifier": 'EVENT_1329_action_queue_async_13_SUBSCRIPT_set_sprite_sequence_5',
                "command": 'set_sprite_sequence',
                "args": [0, 2, [_0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_1329_action_queue_async_13_SUBSCRIPT_jump_to_height_silent_6',
                "command": 'jump_to_height_silent',
                "args": [48]
            },
            {
                "identifier": 'EVENT_1329_action_queue_async_13_SUBSCRIPT_pause_7',
                "command": 'pause',
                "args": [30]
            }
        ]
    },
    {
        "identifier": 'EVENT_1329_run_dialog_14',
        "command": 'run_dialog',
        "args": [2807, AreaObjects.NPC_12, [_0x60Flags.CLOSABLE, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_1329_pause_script_resume_on_next_dialog_page_a_15',
        "command": 'pause_script_resume_on_next_dialog_page_a'
    },
    {
        "identifier": 'EVENT_1329_action_queue_async_16',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_0],
        "subscript": [
            {
                "identifier": 'EVENT_1329_action_queue_async_16_SUBSCRIPT_reset_properties_0',
                "command": 'reset_properties'
            },
            {
                "identifier": 'EVENT_1329_action_queue_async_16_SUBSCRIPT_face_northeast_1',
                "command": 'face_northeast'
            }
        ]
    },
    {
        "identifier": 'EVENT_1329_pause_script_resume_on_next_dialog_page_a_17',
        "command": 'pause_script_resume_on_next_dialog_page_a'
    },
    {
        "identifier": 'EVENT_1329_action_queue_async_18',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_0],
        "subscript": [
            {
                "identifier": 'EVENT_1329_action_queue_async_18_SUBSCRIPT_face_southwest_0',
                "command": 'face_southwest'
            }
        ]
    },
    {
        "identifier": 'EVENT_1329_pause_script_resume_on_next_dialog_page_a_19',
        "command": 'pause_script_resume_on_next_dialog_page_a'
    },
    {
        "identifier": 'EVENT_1329_action_queue_async_20',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_0],
        "subscript": [
            {
                "identifier": 'EVENT_1329_action_queue_async_20_SUBSCRIPT_face_northeast_0',
                "command": 'face_northeast'
            }
        ]
    },
    {
        "identifier": 'EVENT_1329_unsync_dialog_21',
        "command": 'unsync_dialog'
    },
    {
        "identifier": 'EVENT_1329_close_dialog_22',
        "command": 'close_dialog'
    },
    {
        "identifier": 'EVENT_1329_action_queue_async_23',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_0],
        "subscript": [
            {
                "identifier": 'EVENT_1329_action_queue_async_23_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [10]
            },
            {
                "identifier": 'EVENT_1329_action_queue_async_23_SUBSCRIPT_set_animation_speed_1',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_1329_action_queue_async_23_SUBSCRIPT_play_sound_2',
                "command": 'play_sound',
                "args": [Sounds._056_SHAKE_HEAD, 4]
            },
            {
                "identifier": 'EVENT_1329_action_queue_async_23_SUBSCRIPT_set_sprite_sequence_3',
                "command": 'set_sprite_sequence',
                "args": [9, 0, [_0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_1329_action_queue_async_23_SUBSCRIPT_pause_4',
                "command": 'pause',
                "args": [30]
            },
            {
                "identifier": 'EVENT_1329_action_queue_async_23_SUBSCRIPT_stop_sound_5',
                "command": 'stop_sound'
            },
            {
                "identifier": 'EVENT_1329_action_queue_async_23_SUBSCRIPT_reset_properties_6',
                "command": 'reset_properties'
            },
            {
                "identifier": 'EVENT_1329_action_queue_async_23_SUBSCRIPT_pause_7',
                "command": 'pause',
                "args": [30]
            },
            {
                "identifier": 'EVENT_1329_action_queue_async_23_SUBSCRIPT_face_southwest_8',
                "command": 'face_southwest'
            }
        ]
    },
    {
        "identifier": 'EVENT_1329_run_dialog_24',
        "command": 'run_dialog',
        "args": [2809, AreaObjects.NPC_12, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_1329_pause_25',
        "command": 'pause',
        "args": [20]
    },
    {
        "identifier": 'EVENT_1329_action_queue_sync_26',
        "command": 'action_queue_sync',
        "args": [AreaObjects.SCREEN_FOCUS],
        "subscript": [
            {
                "identifier": 'EVENT_1329_action_queue_sync_26_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_1329_action_queue_sync_26_SUBSCRIPT_shift_north_steps_1',
                "command": 'shift_north_steps',
                "args": [3]
            },
            {
                "identifier": 'EVENT_1329_action_queue_sync_26_SUBSCRIPT_set_animation_speed_2',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_1329_action_queue_sync_26_SUBSCRIPT_shift_north_steps_3',
                "command": 'shift_north_steps',
                "args": [3]
            },
            {
                "identifier": 'EVENT_1329_action_queue_sync_26_SUBSCRIPT_set_animation_speed_4',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FASTER, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_1329_action_queue_sync_26_SUBSCRIPT_shift_north_steps_5',
                "command": 'shift_north_steps',
                "args": [3]
            },
            {
                "identifier": 'EVENT_1329_action_queue_sync_26_SUBSCRIPT_set_animation_speed_6',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_1329_action_queue_sync_26_SUBSCRIPT_shift_north_steps_7',
                "command": 'shift_north_steps',
                "args": [28]
            }
        ]
    },
    {
        "identifier": 'EVENT_1329_pause_27',
        "command": 'pause',
        "args": [145]
    },
    {
        "identifier": 'EVENT_1329_fade_out_to_black_async_duration_28',
        "command": 'fade_out_to_black_async_duration',
        "args": [50]
    },
    {
        "identifier": 'EVENT_1329_jmp_29',
        "command": 'jmp',
        "args": ['EVENT_1280_enter_area_0']
    },
    {
        "identifier": 'EVENT_1329_action_queue_sync_30',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_0],
        "subscript": [
            {
                "identifier": 'EVENT_1329_action_queue_sync_30_SUBSCRIPT_set_sprite_sequence_0',
                "command": 'set_sprite_sequence',
                "args": [25, 1, [_0x08Flags.READ_AS_MOLD]]
            }
        ]
    },
    {
        "identifier": 'EVENT_1329_action_queue_async_31',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_1329_action_queue_async_31_SUBSCRIPT_set_sprite_sequence_0',
                "command": 'set_sprite_sequence',
                "args": [24, 2, [_0x08Flags.READ_AS_MOLD]]
            }
        ]
    },
    {
        "identifier": 'EVENT_1329_action_queue_sync_32',
        "command": 'action_queue_sync',
        "args": [AreaObjects.SCREEN_FOCUS],
        "subscript": [
            {
                "identifier": 'EVENT_1329_action_queue_sync_32_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FASTEST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_1329_action_queue_sync_32_SUBSCRIPT_shift_south_steps_1',
                "command": 'shift_south_steps',
                "args": [31]
            },
            {
                "identifier": 'EVENT_1329_action_queue_sync_32_SUBSCRIPT_set_animation_speed_2',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_1329_action_queue_sync_32_SUBSCRIPT_shift_south_steps_3',
                "command": 'shift_south_steps',
                "args": [3]
            },
            {
                "identifier": 'EVENT_1329_action_queue_sync_32_SUBSCRIPT_set_animation_speed_4',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_1329_action_queue_sync_32_SUBSCRIPT_shift_south_steps_5',
                "command": 'shift_south_steps',
                "args": [2]
            },
            {
                "identifier": 'EVENT_1329_action_queue_sync_32_SUBSCRIPT_set_animation_speed_6',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_1329_action_queue_sync_32_SUBSCRIPT_shift_south_steps_7',
                "command": 'shift_south_steps',
                "args": [1]
            }
        ]
    },
    {
        "identifier": 'EVENT_1329_fade_in_from_black_async_duration_33',
        "command": 'fade_in_from_black_async_duration',
        "args": [50]
    },
    {
        "identifier": 'EVENT_1329_pause_34',
        "command": 'pause',
        "args": [120]
    },
    {
        "identifier": 'EVENT_1329_pause_35',
        "command": 'pause',
        "args": [25]
    },
    {
        "identifier": 'EVENT_1329_action_queue_sync_36',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_0],
        "subscript": [
            {
                "identifier": 'EVENT_1329_action_queue_sync_36_SUBSCRIPT_set_sprite_sequence_0',
                "command": 'set_sprite_sequence',
                "args": [10, 0, [_0x08Flags.READ_AS_SEQUENCE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_1329_action_queue_async_37',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_1329_action_queue_async_37_SUBSCRIPT_reset_properties_0',
                "command": 'reset_properties'
            }
        ]
    },
    {
        "identifier": 'EVENT_1329_run_dialog_38',
        "command": 'run_dialog',
        "args": [2808, AreaObjects.NPC_12, [_0x60Flags.CLOSABLE, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_1329_pause_script_resume_on_next_dialog_page_a_39',
        "command": 'pause_script_resume_on_next_dialog_page_a'
    },
    {
        "identifier": 'EVENT_1329_action_queue_async_40',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_0],
        "subscript": [
            {
                "identifier": 'EVENT_1329_action_queue_async_40_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_1329_action_queue_async_40_SUBSCRIPT_set_sprite_sequence_1',
                "command": 'set_sprite_sequence',
                "args": [5, 0, [_0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_1329_pause_script_resume_on_next_dialog_page_a_41',
        "command": 'pause_script_resume_on_next_dialog_page_a'
    },
    {
        "identifier": 'EVENT_1329_action_queue_async_42',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_0],
        "subscript": [
            {
                "identifier": 'EVENT_1329_action_queue_async_42_SUBSCRIPT_reset_properties_0',
                "command": 'reset_properties'
            }
        ]
    },
    {
        "identifier": 'EVENT_1329_unsync_dialog_43',
        "command": 'unsync_dialog'
    },
    {
        "identifier": 'EVENT_1329_close_dialog_44',
        "command": 'close_dialog'
    },
    {
        "identifier": 'EVENT_1329_action_queue_async_45',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_0],
        "subscript": [
            {
                "identifier": 'EVENT_1329_action_queue_async_45_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_1329_action_queue_async_45_SUBSCRIPT_set_animation_speed_1',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_1329_action_queue_async_45_SUBSCRIPT_shift_southwest_steps_2',
                "command": 'shift_southwest_steps',
                "args": [3]
            },
            {
                "identifier": 'EVENT_1329_action_queue_async_45_SUBSCRIPT_shift_southeast_steps_3',
                "command": 'shift_southeast_steps',
                "args": [3]
            },
            {
                "identifier": 'EVENT_1329_action_queue_async_45_SUBSCRIPT_shift_southwest_steps_4',
                "command": 'shift_southwest_steps',
                "args": [2]
            }
        ]
    },
    {
        "identifier": 'EVENT_1329_run_dialog_46',
        "command": 'run_dialog',
        "args": [2810, AreaObjects.NPC_12, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_1329_set_bit_47',
        "command": 'set_bit',
        "args": [0x7053, 7]
    },
    {
        "identifier": 'EVENT_1329_action_queue_sync_48',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_0],
        "subscript": [
            {
                "identifier": 'EVENT_1329_action_queue_sync_48_SUBSCRIPT_jump_to_height_0',
                "command": 'jump_to_height',
                "args": [80]
            }
        ]
    },
    {
        "identifier": 'EVENT_1329_action_queue_sync_49',
        "command": 'action_queue_sync',
        "args": [AreaObjects.SCREEN_FOCUS],
        "subscript": [
            {
                "identifier": 'EVENT_1329_action_queue_sync_49_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [20]
            },
            {
                "identifier": 'EVENT_1329_action_queue_sync_49_SUBSCRIPT_set_animation_speed_1',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_1329_action_queue_sync_49_SUBSCRIPT_play_sound_2',
                "command": 'play_sound',
                "args": [Sounds._022_CLOSE_DOOR, 6]
            },
            {
                "identifier": 'EVENT_1329_action_queue_sync_49_SUBSCRIPT_shift_south_pixels_3',
                "command": 'shift_south_pixels',
                "args": [12]
            },
            {
                "identifier": 'EVENT_1329_action_queue_sync_49_SUBSCRIPT_shift_north_pixels_4',
                "command": 'shift_north_pixels',
                "args": [12]
            },
            {
                "identifier": 'EVENT_1329_action_queue_sync_49_SUBSCRIPT_shift_south_pixels_5',
                "command": 'shift_south_pixels',
                "args": [8]
            },
            {
                "identifier": 'EVENT_1329_action_queue_sync_49_SUBSCRIPT_shift_north_pixels_6',
                "command": 'shift_north_pixels',
                "args": [8]
            },
            {
                "identifier": 'EVENT_1329_action_queue_sync_49_SUBSCRIPT_shift_south_pixels_7',
                "command": 'shift_south_pixels',
                "args": [5]
            },
            {
                "identifier": 'EVENT_1329_action_queue_sync_49_SUBSCRIPT_shift_north_pixels_8',
                "command": 'shift_north_pixels',
                "args": [5]
            }
        ]
    },
    {
        "identifier": 'EVENT_1329_action_queue_async_50',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_1329_action_queue_async_50_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [25]
            },
            {
                "identifier": 'EVENT_1329_action_queue_async_50_SUBSCRIPT_set_animation_speed_1',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING, _0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_1329_action_queue_async_50_SUBSCRIPT_face_southeast_2',
                "command": 'face_southeast'
            },
            {
                "identifier": 'EVENT_1329_action_queue_async_50_SUBSCRIPT_fixed_f_coord_on_3',
                "command": 'fixed_f_coord_on'
            },
            {
                "identifier": 'EVENT_1329_action_queue_async_50_SUBSCRIPT_jump_to_height_silent_4',
                "command": 'jump_to_height_silent',
                "args": [96]
            },
            {
                "identifier": 'EVENT_1329_action_queue_async_50_SUBSCRIPT_shift_northwest_steps_5',
                "command": 'shift_northwest_steps',
                "args": [2]
            },
            {
                "identifier": 'EVENT_1329_action_queue_async_50_SUBSCRIPT_fixed_f_coord_off_6',
                "command": 'fixed_f_coord_off'
            }
        ]
    },
    {
        "identifier": 'EVENT_1329_action_queue_async_51',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_0],
        "subscript": [
            {
                "identifier": 'EVENT_1329_action_queue_async_51_SUBSCRIPT_shift_southwest_steps_0',
                "command": 'shift_southwest_steps',
                "args": [2]
            },
            {
                "identifier": 'EVENT_1329_action_queue_async_51_SUBSCRIPT_visibility_off_1',
                "command": 'visibility_off'
            }
        ]
    },
    {
        "identifier": 'EVENT_1329_remove_from_current_level_52',
        "command": 'remove_from_current_level',
        "args": [AreaObjects.NPC_0]
    },
    {
        "identifier": 'EVENT_1329_unfreeze_camera_53',
        "command": 'unfreeze_camera'
    },
    {
        "identifier": 'EVENT_1329_set_bit_54',
        "command": 'set_bit',
        "args": [0x7053, 7]
    },
    {
        "identifier": 'EVENT_1329_ret_55',
        "command": 'ret'
    }
]
