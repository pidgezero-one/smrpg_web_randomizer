from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data import items
script = [
    {
        "identifier": 'EVENT_1571_clear_bit_0',
        "command": 'clear_bit',
        "args": [0x7078, 2]
    },
    {
        "identifier": 'EVENT_1571_set_short_1',
        "command": 'set_short',
        "args": [0x7024, 0x0000]
    },
    {
        "identifier": 'EVENT_1571_set_short_2',
        "command": 'set_short',
        "args": [0x7026, 0x0016]
    },
    {
        "identifier": 'EVENT_1571_set_short_3',
        "command": 'set_short',
        "args": [0x7028, 0x0015]
    },
    {
        "identifier": 'EVENT_1571_run_background_event_4',
        "command": 'run_background_event',
        "args": [1585, [_0x40Flags.RETURN_ON_LEVEL_EXIT]]
    },
    {
        "identifier": 'EVENT_1571_enable_controls_5',
        "command": 'enable_controls',
        "args": [[ControllerDirections.LEFT, ControllerDirections.RIGHT, ControllerDirections.DOWN, ControllerDirections.UP, ControllerDirections.X, ControllerDirections.A, ControllerDirections.Y, ControllerDirections.B]]
    },
    {
        "identifier": 'EVENT_1571_enable_controls_until_return_6',
        "command": 'enable_controls_until_return',
        "args": [[]]
    },
    {
        "identifier": 'EVENT_1571_action_queue_async_7',
        "command": 'action_queue_async',
        "args": [AreaObjects.SCREEN_FOCUS],
        "subscript": [
            {
                "identifier": 'EVENT_1571_action_queue_async_7_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FASTEST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_1571_action_queue_async_7_SUBSCRIPT_shift_south_steps_1',
                "command": 'shift_south_steps',
                "args": [4]
            }
        ]
    },
    {
        "identifier": 'EVENT_1571_freeze_camera_8',
        "command": 'freeze_camera'
    },
    {
        "identifier": 'EVENT_1571_set_7016_to_object_xyz_9',
        "command": 'set_7016_to_object_xyz',
        "args": [0x95]
    },
    {
        "identifier": 'EVENT_1571_set_action_script_async_10',
        "command": 'set_action_script_async',
        "args": [AreaObjects.NPC_9, 170]
    },
    {
        "identifier": 'EVENT_1571_action_queue_sync_11',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_1],
        "subscript": [
            {
                "identifier": 'EVENT_1571_action_queue_sync_11_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FASTEST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_1571_action_queue_sync_11_SUBSCRIPT_object_memory_set_bit_1',
                "command": 'object_memory_set_bit',
                "args": [0x30, [4]]
            },
            {
                "identifier": 'EVENT_1571_action_queue_sync_11_SUBSCRIPT_set_sprite_sequence_2',
                "command": 'set_sprite_sequence',
                "args": [0, 0, [_0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_1571_action_queue_sync_11_SUBSCRIPT_shift_southwest_pixels_3',
                "command": 'shift_southwest_pixels',
                "args": [4]
            },
            {
                "identifier": 'EVENT_1571_action_queue_sync_11_SUBSCRIPT_shift_northeast_steps_4',
                "command": 'shift_northeast_steps',
                "args": [2]
            }
        ]
    },
    {
        "identifier": 'EVENT_1571_action_queue_async_12',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_2],
        "subscript": [
            {
                "identifier": 'EVENT_1571_action_queue_async_12_SUBSCRIPT_object_memory_set_bit_0',
                "command": 'object_memory_set_bit',
                "args": [0x30, [4]]
            },
            {
                "identifier": 'EVENT_1571_action_queue_async_12_SUBSCRIPT_set_sprite_sequence_1',
                "command": 'set_sprite_sequence',
                "args": [0, 0, [_0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_1571_fade_in_from_black_sync_13',
        "command": 'fade_in_from_black_sync'
    },
    {
        "identifier": 'EVENT_1571_action_queue_sync_14',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_1571_action_queue_sync_14_SUBSCRIPT_floating_off_0',
                "command": 'floating_off'
            },
            {
                "identifier": 'EVENT_1571_action_queue_sync_14_SUBSCRIPT_transfer_to_xyzf_1',
                "command": 'transfer_to_xyzf',
                "args": [13, 16, 17, RadialDirections.EAST]
            },
            {
                "identifier": 'EVENT_1571_action_queue_sync_14_SUBSCRIPT_face_southwest_2',
                "command": 'face_southwest'
            },
            {
                "identifier": 'EVENT_1571_action_queue_sync_14_SUBSCRIPT_pause_3',
                "command": 'pause',
                "args": [9]
            },
            {
                "identifier": 'EVENT_1571_action_queue_sync_14_SUBSCRIPT_set_vram_priority_4',
                "command": 'set_vram_priority',
                "args": [VramPriority.OBJECT_OVERLAPS_MARIO_ON_ALL_SIDES]
            },
            {
                "identifier": 'EVENT_1571_action_queue_sync_14_SUBSCRIPT_set_sprite_sequence_5',
                "command": 'set_sprite_sequence',
                "args": [8, 3, [_0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_1571_action_queue_sync_14_SUBSCRIPT_jump_to_height_silent_6',
                "command": 'jump_to_height_silent',
                "args": [0]
            },
            {
                "identifier": 'EVENT_1571_action_queue_sync_14_SUBSCRIPT_floating_on_7',
                "command": 'floating_on'
            }
        ]
    },
    {
        "identifier": 'EVENT_1571_action_queue_async_15',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_1],
        "subscript": [
            {
                "identifier": 'EVENT_1571_action_queue_async_15_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_1571_action_queue_async_15_SUBSCRIPT_shift_southwest_steps_1',
                "command": 'shift_southwest_steps',
                "args": [2]
            },
            {
                "identifier": 'EVENT_1571_action_queue_async_15_SUBSCRIPT_play_sound_2',
                "command": 'play_sound',
                "args": [Sounds._022_CLOSE_DOOR, 4]
            }
        ]
    },
    {
        "identifier": 'EVENT_1571_action_queue_sync_16',
        "command": 'action_queue_sync',
        "args": [AreaObjects.SCREEN_FOCUS],
        "subscript": [
            {
                "identifier": 'EVENT_1571_action_queue_sync_16_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_1571_action_queue_sync_16_SUBSCRIPT_shift_south_pixels_1',
                "command": 'shift_south_pixels',
                "args": [4]
            },
            {
                "identifier": 'EVENT_1571_action_queue_sync_16_SUBSCRIPT_shift_north_pixels_2',
                "command": 'shift_north_pixels',
                "args": [8]
            },
            {
                "identifier": 'EVENT_1571_action_queue_sync_16_SUBSCRIPT_shift_south_pixels_3',
                "command": 'shift_south_pixels',
                "args": [8]
            },
            {
                "identifier": 'EVENT_1571_action_queue_sync_16_SUBSCRIPT_shift_north_pixels_4',
                "command": 'shift_north_pixels',
                "args": [8]
            },
            {
                "identifier": 'EVENT_1571_action_queue_sync_16_SUBSCRIPT_shift_south_pixels_5',
                "command": 'shift_south_pixels',
                "args": [4]
            },
            {
                "identifier": 'EVENT_1571_action_queue_sync_16_SUBSCRIPT_set_animation_speed_6',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING]]
            }
        ]
    },
    {
        "identifier": 'EVENT_1571_action_queue_async_17',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_1571_action_queue_async_17_SUBSCRIPT_floating_off_0',
                "command": 'floating_off'
            },
            {
                "identifier": 'EVENT_1571_action_queue_async_17_SUBSCRIPT_jump_to_height_silent_1',
                "command": 'jump_to_height_silent',
                "args": [64]
            },
            {
                "identifier": 'EVENT_1571_action_queue_async_17_SUBSCRIPT_set_animation_speed_2',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_1571_action_queue_async_17_SUBSCRIPT_set_sprite_sequence_3',
                "command": 'set_sprite_sequence',
                "args": [6, 3, [_0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_1571_action_queue_async_17_SUBSCRIPT_pause_4',
                "command": 'pause',
                "args": [20]
            },
            {
                "identifier": 'EVENT_1571_action_queue_async_17_SUBSCRIPT_reset_properties_5',
                "command": 'reset_properties'
            },
            {
                "identifier": 'EVENT_1571_action_queue_async_17_SUBSCRIPT_set_animation_speed_6',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_1571_action_queue_async_17_SUBSCRIPT_sequence_looping_on_7',
                "command": 'sequence_looping_on'
            },
            {
                "identifier": 'EVENT_1571_action_queue_async_17_SUBSCRIPT_floating_on_8',
                "command": 'floating_on'
            },
            {
                "identifier": 'EVENT_1571_action_queue_async_17_SUBSCRIPT_shadow_off_9',
                "command": 'shadow_off'
            }
        ]
    },
    {
        "identifier": 'EVENT_1571_jmp_18',
        "command": 'jmp',
        "args": ['EVENT_1571_pause_65']
    },
    {
        "identifier": 'EVENT_1571_palette_set_morphs_19',
        "command": 'palette_set_morphs',
        "args": [PaletteSetTypes.FADE_TO, 10, 26, 1]
    },
    {
        "identifier": 'EVENT_1571_palette_set_morphs_20',
        "command": 'palette_set_morphs',
        "args": [PaletteSetTypes.FADE_TO, 10, 26, 2]
    },
    {
        "identifier": 'EVENT_1571_palette_set_morphs_21',
        "command": 'palette_set_morphs',
        "args": [PaletteSetTypes.FADE_TO, 10, 26, 3]
    },
    {
        "identifier": 'EVENT_1571_palette_set_morphs_22',
        "command": 'palette_set_morphs',
        "args": [PaletteSetTypes.FADE_TO, 10, 26, 4]
    },
    {
        "identifier": 'EVENT_1571_palette_set_morphs_23',
        "command": 'palette_set_morphs',
        "args": [PaletteSetTypes.FADE_TO, 10, 26, 5]
    },
    {
        "identifier": 'EVENT_1571_palette_set_morphs_24',
        "command": 'palette_set_morphs',
        "args": [PaletteSetTypes.FADE_TO, 10, 26, 6]
    },
    {
        "identifier": 'EVENT_1571_palette_set_morphs_25',
        "command": 'palette_set_morphs',
        "args": [PaletteSetTypes.FADE_TO, 10, 26, 7]
    },
    {
        "identifier": 'EVENT_1571_pause_26',
        "command": 'pause',
        "args": [16]
    },
    {
        "identifier": 'EVENT_1571_action_queue_async_27',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_12],
        "subscript": [
            {
                "identifier": 'EVENT_1571_action_queue_async_27_SUBSCRIPT_set_priority_0',
                "command": 'set_priority',
                "args": [3]
            },
            {
                "identifier": 'EVENT_1571_action_queue_async_27_SUBSCRIPT_transfer_to_xyzf_1',
                "command": 'transfer_to_xyzf',
                "args": [8, 4, 0, RadialDirections.EAST]
            },
            {
                "identifier": 'EVENT_1571_action_queue_async_27_SUBSCRIPT_visibility_on_2',
                "command": 'visibility_on'
            },
            {
                "identifier": 'EVENT_1571_action_queue_async_27_SUBSCRIPT_set_animation_speed_3',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING, _0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_1571_action_queue_async_27_SUBSCRIPT_shift_southeast_steps_4',
                "command": 'shift_southeast_steps',
                "args": [8]
            },
            {
                "identifier": 'EVENT_1571_action_queue_async_27_SUBSCRIPT_set_sprite_sequence_5',
                "command": 'set_sprite_sequence',
                "args": [10, 0, [_0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_1571_action_queue_async_27_SUBSCRIPT_jump_to_height_6',
                "command": 'jump_to_height',
                "args": [64]
            }
        ]
    },
    {
        "identifier": 'EVENT_1571_play_sound_28',
        "command": 'play_sound',
        "args": [Sounds._087_CORRECT_SIGNAL, 6]
    },
    {
        "identifier": 'EVENT_1571_run_dialog_29',
        "command": 'run_dialog',
        "args": [1050, AreaObjects.NPC_14, [_0x60Flags.ASYNC, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_1571_jmp_if_dialog_option_b_30',
        "command": 'jmp_if_dialog_option_b',
        "args": ['EVENT_1571_run_dialog_duration_52']
    },
    {
        "identifier": 'EVENT_1571_set_bit_31',
        "command": 'set_bit',
        "args": [0x7044, 0]
    },
    {
        "identifier": 'EVENT_1571_run_dialog_32',
        "command": 'run_dialog',
        "args": [1051, AreaObjects.NPC_14, [_0x60Flags.ASYNC, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_1571_move_script_to_background_thread_2_33',
        "command": 'move_script_to_background_thread_2'
    },
    {
        "identifier": 'EVENT_1571_action_queue_sync_34',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_3],
        "subscript": [
            {
                "identifier": 'EVENT_1571_action_queue_sync_34_SUBSCRIPT_transfer_to_xyzf_0',
                "command": 'transfer_to_xyzf',
                "args": [11, 19, 10, RadialDirections.EAST]
            },
            {
                "identifier": 'EVENT_1571_action_queue_sync_34_SUBSCRIPT_set_vram_priority_1',
                "command": 'set_vram_priority',
                "args": [VramPriority.PRIORITY_3]
            },
            {
                "identifier": 'EVENT_1571_action_queue_sync_34_SUBSCRIPT_sequence_looping_on_2',
                "command": 'sequence_looping_on'
            },
            {
                "identifier": 'EVENT_1571_action_queue_sync_34_SUBSCRIPT_visibility_on_3',
                "command": 'visibility_on'
            },
            {
                "identifier": 'EVENT_1571_action_queue_sync_34_SUBSCRIPT_set_animation_speed_4',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING, _0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_1571_action_queue_sync_34_SUBSCRIPT_shift_northeast_steps_5',
                "command": 'shift_northeast_steps',
                "args": [3]
            }
        ]
    },
    {
        "identifier": 'EVENT_1571_action_queue_sync_35',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_4],
        "subscript": [
            {
                "identifier": 'EVENT_1571_action_queue_sync_35_SUBSCRIPT_transfer_to_xyzf_0',
                "command": 'transfer_to_xyzf',
                "args": [10, 21, 10, RadialDirections.EAST]
            },
            {
                "identifier": 'EVENT_1571_action_queue_sync_35_SUBSCRIPT_set_vram_priority_1',
                "command": 'set_vram_priority',
                "args": [VramPriority.PRIORITY_3]
            },
            {
                "identifier": 'EVENT_1571_action_queue_sync_35_SUBSCRIPT_sequence_looping_on_2',
                "command": 'sequence_looping_on'
            },
            {
                "identifier": 'EVENT_1571_action_queue_sync_35_SUBSCRIPT_visibility_on_3',
                "command": 'visibility_on'
            },
            {
                "identifier": 'EVENT_1571_action_queue_sync_35_SUBSCRIPT_set_animation_speed_4',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING, _0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_1571_action_queue_sync_35_SUBSCRIPT_shift_northeast_steps_5',
                "command": 'shift_northeast_steps',
                "args": [5]
            }
        ]
    },
    {
        "identifier": 'EVENT_1571_action_queue_async_36',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_1571_action_queue_async_36_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [40]
            },
            {
                "identifier": 'EVENT_1571_action_queue_async_36_SUBSCRIPT_start_loop_n_times_1',
                "command": 'start_loop_n_times',
                "args": [1]
            },
            {
                "identifier": 'EVENT_1571_action_queue_async_36_SUBSCRIPT_jump_to_height_2',
                "command": 'jump_to_height',
                "args": [108]
            },
            {
                "identifier": 'EVENT_1571_action_queue_async_36_SUBSCRIPT_pause_3',
                "command": 'pause',
                "args": [32]
            },
            {
                "identifier": 'EVENT_1571_action_queue_async_36_SUBSCRIPT_end_loop_4',
                "command": 'end_loop'
            }
        ]
    },
    {
        "identifier": 'EVENT_1571_move_script_to_main_thread_37',
        "command": 'move_script_to_main_thread'
    },
    {
        "identifier": 'EVENT_1571_dec_short_38',
        "command": 'dec_short',
        "args": [0x702a]
    },
    {
        "identifier": 'EVENT_1571_dec_short_39',
        "command": 'dec_short',
        "args": [0x702a]
    },
    {
        "identifier": 'EVENT_1571_run_dialog_duration_40',
        "command": 'run_dialog_duration',
        "args": [1052, DialogDurations.FOREVER, [_0x60Flags.ASYNC]]
    },
    {
        "identifier": 'EVENT_1571_action_queue_sync_41',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_2],
        "subscript": [
            {
                "identifier": 'EVENT_1571_action_queue_sync_41_SUBSCRIPT_set_short_0',
                "command": 'set_short',
                "args": [0x7016, 0x0009]
            },
            {
                "identifier": 'EVENT_1571_action_queue_sync_41_SUBSCRIPT_set_short_1',
                "command": 'set_short',
                "args": [0x7018, 0x0017]
            },
            {
                "identifier": 'EVENT_1571_action_queue_sync_41_SUBSCRIPT_set_short_2',
                "command": 'set_short',
                "args": [0x701a, 0x0000]
            },
            {
                "identifier": 'EVENT_1571_action_queue_sync_41_SUBSCRIPT_db_3',
                "command": 'db',
                "args": [0x9a]
            },
            {
                "identifier": 'EVENT_1571_action_queue_sync_41_SUBSCRIPT_set_animation_speed_4',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_1571_action_queue_sync_41_SUBSCRIPT_shift_northeast_steps_5',
                "command": 'shift_northeast_steps',
                "args": [5]
            },
            {
                "identifier": 'EVENT_1571_action_queue_sync_41_SUBSCRIPT_shift_northeast_pixels_6',
                "command": 'shift_northeast_pixels',
                "args": [4]
            }
        ]
    },
    {
        "identifier": 'EVENT_1571_set_action_script_sync_42',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_10, 170]
    },
    {
        "identifier": 'EVENT_1571_pause_43',
        "command": 'pause',
        "args": [87]
    },
    {
        "identifier": 'EVENT_1571_action_queue_sync_44',
        "command": 'action_queue_sync',
        "args": [AreaObjects.SCREEN_FOCUS],
        "subscript": [
            {
                "identifier": 'EVENT_1571_action_queue_sync_44_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_1571_action_queue_sync_44_SUBSCRIPT_shift_south_pixels_1',
                "command": 'shift_south_pixels',
                "args": [4]
            },
            {
                "identifier": 'EVENT_1571_action_queue_sync_44_SUBSCRIPT_shift_north_pixels_2',
                "command": 'shift_north_pixels',
                "args": [8]
            },
            {
                "identifier": 'EVENT_1571_action_queue_sync_44_SUBSCRIPT_shift_south_pixels_3',
                "command": 'shift_south_pixels',
                "args": [4]
            },
            {
                "identifier": 'EVENT_1571_action_queue_sync_44_SUBSCRIPT_set_animation_speed_4',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING]]
            }
        ]
    },
    {
        "identifier": 'EVENT_1571_action_queue_sync_45',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_1571_action_queue_sync_45_SUBSCRIPT_play_sound_0',
                "command": 'play_sound',
                "args": [Sounds._049_BIG_SHELL_HIT, 4]
            },
            {
                "identifier": 'EVENT_1571_action_queue_sync_45_SUBSCRIPT_jump_to_height_silent_1',
                "command": 'jump_to_height_silent',
                "args": [64]
            },
            {
                "identifier": 'EVENT_1571_action_queue_sync_45_SUBSCRIPT_set_animation_speed_2',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_1571_action_queue_sync_45_SUBSCRIPT_set_sprite_sequence_3',
                "command": 'set_sprite_sequence',
                "args": [6, 3, [_0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_1571_action_queue_sync_45_SUBSCRIPT_set_animation_speed_4',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_1571_action_queue_sync_45_SUBSCRIPT_shift_southeast_steps_5',
                "command": 'shift_southeast_steps',
                "args": [2]
            },
            {
                "identifier": 'EVENT_1571_action_queue_sync_45_SUBSCRIPT_face_southwest_6',
                "command": 'face_southwest'
            },
            {
                "identifier": 'EVENT_1571_action_queue_sync_45_SUBSCRIPT_reset_properties_7',
                "command": 'reset_properties'
            }
        ]
    },
    {
        "identifier": 'EVENT_1571_action_queue_async_46',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_1],
        "subscript": [
            {
                "identifier": 'EVENT_1571_action_queue_async_46_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_1571_action_queue_async_46_SUBSCRIPT_shift_southeast_steps_1',
                "command": 'shift_southeast_steps',
                "args": [2]
            }
        ]
    },
    {
        "identifier": 'EVENT_1571_action_queue_async_47',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_2],
        "subscript": [
            {
                "identifier": 'EVENT_1571_action_queue_async_47_SUBSCRIPT_shift_northeast_steps_0',
                "command": 'shift_northeast_steps',
                "args": [4]
            },
            {
                "identifier": 'EVENT_1571_action_queue_async_47_SUBSCRIPT_visibility_off_1',
                "command": 'visibility_off'
            }
        ]
    },
    {
        "identifier": 'EVENT_1571_remove_from_current_level_48',
        "command": 'remove_from_current_level',
        "args": [AreaObjects.NPC_10]
    },
    {
        "identifier": 'EVENT_1571_run_dialog_duration_49',
        "command": 'run_dialog_duration',
        "args": [1053, DialogDurations.FOREVER, [_0x60Flags.ASYNC]]
    },
    {
        "identifier": 'EVENT_1571_action_queue_sync_50',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_1571_action_queue_sync_50_SUBSCRIPT_fixed_f_coord_on_0',
                "command": 'fixed_f_coord_on'
            },
            {
                "identifier": 'EVENT_1571_action_queue_sync_50_SUBSCRIPT_shift_northwest_steps_1',
                "command": 'shift_northwest_steps',
                "args": [2]
            },
            {
                "identifier": 'EVENT_1571_action_queue_sync_50_SUBSCRIPT_face_southwest_2',
                "command": 'face_southwest'
            },
            {
                "identifier": 'EVENT_1571_action_queue_sync_50_SUBSCRIPT_fixed_f_coord_off_3',
                "command": 'fixed_f_coord_off'
            }
        ]
    },
    {
        "identifier": 'EVENT_1571_action_queue_async_51',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_1],
        "subscript": [
            {
                "identifier": 'EVENT_1571_action_queue_async_51_SUBSCRIPT_shift_northwest_steps_0',
                "command": 'shift_northwest_steps',
                "args": [2]
            }
        ]
    },
    {
        "identifier": 'EVENT_1571_run_dialog_duration_52',
        "command": 'run_dialog_duration',
        "args": [1054, DialogDurations.SHORT, [_0x60Flags.ASYNC]]
    },
    {
        "identifier": 'EVENT_1571_play_sound_53',
        "command": 'play_sound',
        "args": [Sounds._087_CORRECT_SIGNAL, 6]
    },
    {
        "identifier": 'EVENT_1571_jmp_if_bit_clear_54',
        "command": 'jmp_if_bit_clear',
        "args": [0x7044, 0, 'EVENT_1571_action_queue_async_57']
    },
    {
        "identifier": 'EVENT_1571_action_queue_async_55',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_12],
        "subscript": [
            {
                "identifier": 'EVENT_1571_action_queue_async_55_SUBSCRIPT_reset_properties_0',
                "command": 'reset_properties'
            },
            {
                "identifier": 'EVENT_1571_action_queue_async_55_SUBSCRIPT_face_southwest_1',
                "command": 'face_southwest'
            },
            {
                "identifier": 'EVENT_1571_action_queue_async_55_SUBSCRIPT_pause_2',
                "command": 'pause',
                "args": [5]
            },
            {
                "identifier": 'EVENT_1571_action_queue_async_55_SUBSCRIPT_shift_northwest_steps_3',
                "command": 'shift_northwest_steps',
                "args": [3]
            },
            {
                "identifier": 'EVENT_1571_action_queue_async_55_SUBSCRIPT_pause_4',
                "command": 'pause',
                "args": [20]
            },
            {
                "identifier": 'EVENT_1571_action_queue_async_55_SUBSCRIPT_pause_5',
                "command": 'pause',
                "args": [20]
            },
            {
                "identifier": 'EVENT_1571_action_queue_async_55_SUBSCRIPT_shift_southeast_steps_6',
                "command": 'shift_southeast_steps',
                "args": [3]
            },
            {
                "identifier": 'EVENT_1571_action_queue_async_55_SUBSCRIPT_set_sprite_sequence_7',
                "command": 'set_sprite_sequence',
                "args": [10, 0, [_0x08Flags.READ_AS_SEQUENCE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_1571_run_dialog_56',
        "command": 'run_dialog',
        "args": [1055, AreaObjects.NPC_14, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_1571_action_queue_async_57',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_12],
        "subscript": [
            {
                "identifier": 'EVENT_1571_action_queue_async_57_SUBSCRIPT_reset_properties_0',
                "command": 'reset_properties'
            },
            {
                "identifier": 'EVENT_1571_action_queue_async_57_SUBSCRIPT_shift_northwest_steps_1',
                "command": 'shift_northwest_steps',
                "args": [5]
            },
            {
                "identifier": 'EVENT_1571_action_queue_async_57_SUBSCRIPT_visibility_off_2',
                "command": 'visibility_off'
            }
        ]
    },
    {
        "identifier": 'EVENT_1571_palette_set_morphs_58',
        "command": 'palette_set_morphs',
        "args": [PaletteSetTypes.FADE_TO, 10, 49, 1]
    },
    {
        "identifier": 'EVENT_1571_palette_set_morphs_59',
        "command": 'palette_set_morphs',
        "args": [PaletteSetTypes.FADE_TO, 10, 50, 2]
    },
    {
        "identifier": 'EVENT_1571_palette_set_morphs_60',
        "command": 'palette_set_morphs',
        "args": [PaletteSetTypes.FADE_TO, 10, 51, 3]
    },
    {
        "identifier": 'EVENT_1571_palette_set_morphs_61',
        "command": 'palette_set_morphs',
        "args": [PaletteSetTypes.FADE_TO, 10, 52, 4]
    },
    {
        "identifier": 'EVENT_1571_palette_set_morphs_62',
        "command": 'palette_set_morphs',
        "args": [PaletteSetTypes.FADE_TO, 10, 53, 5]
    },
    {
        "identifier": 'EVENT_1571_palette_set_morphs_63',
        "command": 'palette_set_morphs',
        "args": [PaletteSetTypes.FADE_TO, 10, 54, 6]
    },
    {
        "identifier": 'EVENT_1571_palette_set_morphs_64',
        "command": 'palette_set_morphs',
        "args": [PaletteSetTypes.FADE_TO, 10, 55, 7]
    },
    {
        "identifier": 'EVENT_1571_pause_65',
        "command": 'pause',
        "args": [16]
    },
    {
        "identifier": 'EVENT_1571_set_action_script_sync_66',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_1, 593]
    },
    {
        "identifier": 'EVENT_1571_set_action_script_sync_67',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.MARIO, 593]
    },
    {
        "identifier": 'EVENT_1571_set_action_script_sync_68',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.SCREEN_FOCUS, 592]
    },
    {
        "identifier": 'EVENT_1571_move_script_to_background_thread_2_69',
        "command": 'move_script_to_background_thread_2'
    },
    {
        "identifier": 'EVENT_1571_enable_controls_until_return_70',
        "command": 'enable_controls_until_return',
        "args": [[ControllerDirections.A, ControllerDirections.B]]
    },
    {
        "identifier": 'EVENT_1571_pause_71',
        "command": 'pause',
        "args": [1]
    },
    {
        "identifier": 'EVENT_1571_jmp_if_bit_set_72',
        "command": 'jmp_if_bit_set',
        "args": [0x7044, 7, 'EVENT_1571_clear_bit_82']
    },
    {
        "identifier": 'EVENT_1571_jmp_if_bit_set_73',
        "command": 'jmp_if_bit_set',
        "args": [0x7078, 2, 'EVENT_1571_adjust_music_tempo_132']
    },
    {
        "identifier": 'EVENT_1571_set_7000_to_tapped_button_74',
        "command": 'set_7000_to_tapped_button'
    },
    {
        "identifier": 'EVENT_1571_jmp_if_7000_any_bits_set_75',
        "command": 'jmp_if_7000_any_bits_set',
        "args": [[7], 'EVENT_1571_jmp_if_mario_in_air_77']
    },
    {
        "identifier": 'EVENT_1571_jmp_76',
        "command": 'jmp',
        "args": ['EVENT_1571_pause_71']
    },
    {
        "identifier": 'EVENT_1571_jmp_if_mario_in_air_77',
        "command": 'jmp_if_mario_in_air',
        "args": ['EVENT_1571_pause_71']
    },
    {
        "identifier": 'EVENT_1571_clear_bit_78',
        "command": 'clear_bit',
        "args": [0x7044, 4]
    },
    {
        "identifier": 'EVENT_1571_jmp_if_bit_clear_79',
        "command": 'jmp_if_bit_clear',
        "args": [0x7044, 5, 'EVENT_1571_pause_71']
    },
    {
        "identifier": 'EVENT_1571_set_bit_80',
        "command": 'set_bit',
        "args": [0x7044, 4]
    },
    {
        "identifier": 'EVENT_1571_jmp_81',
        "command": 'jmp',
        "args": ['EVENT_1571_pause_71']
    },
    {
        "identifier": 'EVENT_1571_clear_bit_82',
        "command": 'clear_bit',
        "args": [0x7044, 7]
    },
    {
        "identifier": 'EVENT_1571_pause_action_script_83',
        "command": 'pause_action_script',
        "args": [AreaObjects.MARIO]
    },
    {
        "identifier": 'EVENT_1571_pause_action_script_84',
        "command": 'pause_action_script',
        "args": [AreaObjects.SCREEN_FOCUS]
    },
    {
        "identifier": 'EVENT_1571_set_short_mem_85',
        "command": 'set_short_mem',
        "args": [0x7000, 0x7026]
    },
    {
        "identifier": 'EVENT_1571_set_short_mem_86',
        "command": 'set_short_mem',
        "args": [0x70a9, 0x7000]
    },
    {
        "identifier": 'EVENT_1571_jmp_if_mario_in_air_87',
        "command": 'jmp_if_mario_in_air',
        "args": ['EVENT_1571_set_short_mem_100']
    },
    {
        "identifier": 'EVENT_1571_enable_controls_until_return_88',
        "command": 'enable_controls_until_return',
        "args": [[]]
    },
    {
        "identifier": 'EVENT_1571_action_queue_sync_89',
        "command": 'action_queue_sync',
        "args": [AreaObjects.SCREEN_FOCUS],
        "subscript": [
            {
                "identifier": 'EVENT_1571_action_queue_sync_89_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_1571_action_queue_sync_89_SUBSCRIPT_shift_south_pixels_1',
                "command": 'shift_south_pixels',
                "args": [4]
            },
            {
                "identifier": 'EVENT_1571_action_queue_sync_89_SUBSCRIPT_shift_north_pixels_2',
                "command": 'shift_north_pixels',
                "args": [8]
            },
            {
                "identifier": 'EVENT_1571_action_queue_sync_89_SUBSCRIPT_shift_south_pixels_3',
                "command": 'shift_south_pixels',
                "args": [4]
            },
            {
                "identifier": 'EVENT_1571_action_queue_sync_89_SUBSCRIPT_set_animation_speed_4',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING]]
            }
        ]
    },
    {
        "identifier": 'EVENT_1571_pause_action_script_90',
        "command": 'pause_action_script',
        "args": [AreaObjects.MEM_70A9]
    },
    {
        "identifier": 'EVENT_1571_action_queue_sync_91',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_1571_action_queue_sync_91_SUBSCRIPT_play_sound_0',
                "command": 'play_sound',
                "args": [Sounds._049_BIG_SHELL_HIT, 4]
            },
            {
                "identifier": 'EVENT_1571_action_queue_sync_91_SUBSCRIPT_jump_to_height_silent_1',
                "command": 'jump_to_height_silent',
                "args": [64]
            },
            {
                "identifier": 'EVENT_1571_action_queue_sync_91_SUBSCRIPT_set_animation_speed_2',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_1571_action_queue_sync_91_SUBSCRIPT_set_sprite_sequence_3',
                "command": 'set_sprite_sequence',
                "args": [6, 3, [_0x08Flags.READ_AS_SEQUENCE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_1571_resume_action_script_92',
        "command": 'resume_action_script',
        "args": [AreaObjects.MARIO]
    },
    {
        "identifier": 'EVENT_1571_store_set_bits_93',
        "command": 'store_set_bits',
        "args": [0x7044, 6]
    },
    {
        "identifier": 'EVENT_1571_pause_94',
        "command": 'pause',
        "args": [19]
    },
    {
        "identifier": 'EVENT_1571_resume_action_script_95',
        "command": 'resume_action_script',
        "args": [AreaObjects.SCREEN_FOCUS]
    },
    {
        "identifier": 'EVENT_1571_pause_96',
        "command": 'pause',
        "args": [1]
    },
    {
        "identifier": 'EVENT_1571_action_queue_sync_97',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_1571_action_queue_sync_97_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_1571_action_queue_sync_97_SUBSCRIPT_reset_properties_1',
                "command": 'reset_properties'
            }
        ]
    },
    {
        "identifier": 'EVENT_1571_add_short_98',
        "command": 'add_short',
        "args": [0x702c, 0xfff6]
    },
    {
        "identifier": 'EVENT_1571_jmp_99',
        "command": 'jmp',
        "args": ['EVENT_1571_enable_controls_until_return_70']
    },
    {
        "identifier": 'EVENT_1571_set_short_mem_100',
        "command": 'set_short_mem',
        "args": [0x7000, 0x7028]
    },
    {
        "identifier": 'EVENT_1571_set_short_mem_101',
        "command": 'set_short_mem',
        "args": [0x70a8, 0x7000]
    },
    {
        "identifier": 'EVENT_1571_pause_action_script_102',
        "command": 'pause_action_script',
        "args": [AreaObjects.MEM_70A8]
    },
    {
        "identifier": 'EVENT_1571_jmp_if_bit_set_103',
        "command": 'jmp_if_bit_set',
        "args": [0x7044, 4, 'EVENT_1571_action_queue_sync_122']
    },
    {
        "identifier": 'EVENT_1571_enable_controls_until_return_104',
        "command": 'enable_controls_until_return',
        "args": [[]]
    },
    {
        "identifier": 'EVENT_1571_pause_action_script_105',
        "command": 'pause_action_script',
        "args": [AreaObjects.MEM_70A9]
    },
    {
        "identifier": 'EVENT_1571_pause_106',
        "command": 'pause',
        "args": [1]
    },
    {
        "identifier": 'EVENT_1571_jmp_if_mario_in_air_107',
        "command": 'jmp_if_mario_in_air',
        "args": ['EVENT_1571_pause_106']
    },
    {
        "identifier": 'EVENT_1571_action_queue_async_108',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_1571_action_queue_async_108_SUBSCRIPT_play_sound_0',
                "command": 'play_sound',
                "args": [Sounds._043_POP_UP_FROM_WATER, 4]
            },
            {
                "identifier": 'EVENT_1571_action_queue_async_108_SUBSCRIPT_set_sprite_sequence_1',
                "command": 'set_sprite_sequence',
                "args": [4, 0, [_0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_1571_action_queue_async_108_SUBSCRIPT_shift_southwest_pixels_2',
                "command": 'shift_southwest_pixels',
                "args": [8]
            }
        ]
    },
    {
        "identifier": 'EVENT_1571_store_set_bits_109',
        "command": 'store_set_bits',
        "args": [0x7044, 6]
    },
    {
        "identifier": 'EVENT_1571_resume_action_script_110',
        "command": 'resume_action_script',
        "args": [AreaObjects.MEM_70A8]
    },
    {
        "identifier": 'EVENT_1571_resume_action_script_111',
        "command": 'resume_action_script',
        "args": [AreaObjects.MARIO]
    },
    {
        "identifier": 'EVENT_1571_pause_112',
        "command": 'pause',
        "args": [9]
    },
    {
        "identifier": 'EVENT_1571_play_sound_113',
        "command": 'play_sound',
        "args": [Sounds._043_POP_UP_FROM_WATER, 6]
    },
    {
        "identifier": 'EVENT_1571_pause_114',
        "command": 'pause',
        "args": [10]
    },
    {
        "identifier": 'EVENT_1571_resume_action_script_115',
        "command": 'resume_action_script',
        "args": [AreaObjects.SCREEN_FOCUS]
    },
    {
        "identifier": 'EVENT_1571_start_loop_n_times_116',
        "command": 'start_loop_n_times',
        "args": [2]
    },
    {
        "identifier": 'EVENT_1571_play_sound_117',
        "command": 'play_sound',
        "args": [Sounds._043_POP_UP_FROM_WATER, 6]
    },
    {
        "identifier": 'EVENT_1571_pause_118',
        "command": 'pause',
        "args": [10]
    },
    {
        "identifier": 'EVENT_1571_end_loop_119',
        "command": 'end_loop'
    },
    {
        "identifier": 'EVENT_1571_action_queue_async_120',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_1571_action_queue_async_120_SUBSCRIPT_jump_to_height_0',
                "command": 'jump_to_height',
                "args": [48]
            },
            {
                "identifier": 'EVENT_1571_action_queue_async_120_SUBSCRIPT_shift_northeast_pixels_1',
                "command": 'shift_northeast_pixels',
                "args": [4]
            },
            {
                "identifier": 'EVENT_1571_action_queue_async_120_SUBSCRIPT_reset_properties_2',
                "command": 'reset_properties'
            }
        ]
    },
    {
        "identifier": 'EVENT_1571_jmp_121',
        "command": 'jmp',
        "args": ['EVENT_1571_enable_controls_until_return_70']
    },
    {
        "identifier": 'EVENT_1571_action_queue_sync_122',
        "command": 'action_queue_sync',
        "args": [AreaObjects.SCREEN_FOCUS],
        "subscript": [
            {
                "identifier": 'EVENT_1571_action_queue_sync_122_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [3]
            }
        ]
    },
    {
        "identifier": 'EVENT_1571_resume_action_script_123',
        "command": 'resume_action_script',
        "args": [AreaObjects.SCREEN_FOCUS]
    },
    {
        "identifier": 'EVENT_1571_reset_coords_124',
        "command": 'reset_coords',
        "args": [AreaObjects.MARIO]
    },
    {
        "identifier": 'EVENT_1571_action_queue_async_125',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_1571_action_queue_async_125_SUBSCRIPT_walk_1_step_southwest_0',
                "command": 'walk_1_step_southwest'
            },
            {
                "identifier": 'EVENT_1571_action_queue_async_125_SUBSCRIPT_walk_1_step_southwest_1',
                "command": 'walk_1_step_southwest'
            }
        ]
    },
    {
        "identifier": 'EVENT_1571_set_action_script_sync_126',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.MARIO, 592]
    },
    {
        "identifier": 'EVENT_1571_action_queue_sync_127',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MEM_70A9],
        "subscript": [
            {
                "identifier": 'EVENT_1571_action_queue_sync_127_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING, _0x10Flags.SEQUENCE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_1571_swap_short_mem_128',
        "command": 'swap_short_mem',
        "args": [0x7000, 0x7028]
    },
    {
        "identifier": 'EVENT_1571_swap_short_mem_129',
        "command": 'swap_short_mem',
        "args": [0x7000, 0x7026]
    },
    {
        "identifier": 'EVENT_1571_swap_short_mem_130',
        "command": 'swap_short_mem',
        "args": [0x7000, 0x7028]
    },
    {
        "identifier": 'EVENT_1571_jmp_131',
        "command": 'jmp',
        "args": ['EVENT_1571_pause_71']
    },
    {
        "identifier": 'EVENT_1571_adjust_music_tempo_132',
        "command": 'adjust_music_tempo',
        "args": [MusicDirections.SLOW_DOWN, 0, 30]
    },
    {
        "identifier": 'EVENT_1571_set_short_mem_133',
        "command": 'set_short_mem',
        "args": [0x7000, 0x7028]
    },
    {
        "identifier": 'EVENT_1571_set_short_mem_134',
        "command": 'set_short_mem',
        "args": [0x70a9, 0x7000]
    },
    {
        "identifier": 'EVENT_1571_set_action_script_sync_135',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.MEM_70A9, 592]
    },
    {
        "identifier": 'EVENT_1571_set_action_script_sync_136',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.MARIO, 592]
    },
    {
        "identifier": 'EVENT_1571_pause_action_script_137',
        "command": 'pause_action_script',
        "args": [AreaObjects.SCREEN_FOCUS]
    },
    {
        "identifier": 'EVENT_1571_action_queue_async_138',
        "command": 'action_queue_async',
        "args": [AreaObjects.SCREEN_FOCUS],
        "subscript": [
            {
                "identifier": 'EVENT_1571_action_queue_async_138_SUBSCRIPT_shift_southwest_steps_0',
                "command": 'shift_southwest_steps',
                "args": [14]
            }
        ]
    },
    {
        "identifier": 'EVENT_1571_fade_out_to_black_async_duration_139',
        "command": 'fade_out_to_black_async_duration',
        "args": [32]
    },
    {
        "identifier": 'EVENT_1571_enter_area_140',
        "command": 'enter_area',
        "args": [Rooms._067_MIDAS_RIVER_BUSINESS_TRANSACTION_AREA, RadialDirections.SOUTH, 20, 21, 0, []]
    },
    {
        "identifier": 'EVENT_1571_clear_bit_141',
        "command": 'clear_bit',
        "args": [0x7079, 1]
    },
    {
        "identifier": 'EVENT_1571_set_bit_142',
        "command": 'set_bit',
        "args": [0x7043, 1]
    },
    {
        "identifier": 'EVENT_1571_jmp_to_event_143',
        "command": 'jmp_to_event',
        "args": [3486]
    },
    {
        "identifier": 'EVENT_1571_ret_144',
        "command": 'ret'
    }
]
