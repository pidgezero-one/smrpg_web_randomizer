
from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data import items
script = [
    {
        "identifier": 'EVENT_3794_set_action_script_sync_0',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_9, 991]
    },
    {
        "identifier": 'EVENT_3794_set_action_script_sync_1',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_4, 240]
    },
    {
        "identifier": 'EVENT_3794_set_action_script_sync_2',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_8, 990]
    },
    {
        "identifier": 'EVENT_3794_set_action_script_sync_3',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_5, 241]
    },
    {
        "identifier": 'EVENT_3794_set_bit_4',
        "command": 'set_bit',
        "args": [0x7044, 0]
    },
    {
        "identifier": 'EVENT_3794_run_background_event_5',
        "command": 'run_background_event',
        "args": [3793, [_0x40Flags.RETURN_ON_LEVEL_EXIT]]
    },
    {
        "identifier": 'EVENT_3794_action_queue_sync_6',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_3794_action_queue_sync_6_SUBSCRIPT_set_vram_priority_0',
                "command": 'set_vram_priority',
                "args": [VramPriority.OBJECT_OVERLAPS_MARIO_ON_ALL_SIDES]
            },
            {
                "identifier": 'EVENT_3794_action_queue_sync_6_SUBSCRIPT_floating_on_1',
                "command": 'floating_on'
            },
            {
                "identifier": 'EVENT_3794_action_queue_sync_6_SUBSCRIPT_pause_2',
                "command": 'pause',
                "args": [1]
            },
            {
                "identifier": 'EVENT_3794_action_queue_sync_6_SUBSCRIPT_jmp_if_mario_in_air_3',
                "command": 'jmp_if_mario_in_air',
                "args": ['EVENT_3794_action_queue_sync_6_SUBSCRIPT_pause_2']
            },
            {
                "identifier": 'EVENT_3794_action_queue_sync_6_SUBSCRIPT_play_sound_4',
                "command": 'play_sound',
                "args": [Sounds._058_INSERT, 4]
            },
            {
                "identifier": 'EVENT_3794_action_queue_sync_6_SUBSCRIPT_set_sprite_sequence_5',
                "command": 'set_sprite_sequence',
                "args": [0, 6, [_0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3794_action_queue_sync_6_SUBSCRIPT_set_vram_priority_6',
                "command": 'set_vram_priority',
                "args": [VramPriority.NORMAL]
            },
            {
                "identifier": 'EVENT_3794_action_queue_sync_6_SUBSCRIPT_pause_7',
                "command": 'pause',
                "args": [30]
            },
            {
                "identifier": 'EVENT_3794_action_queue_sync_6_SUBSCRIPT_reset_properties_8',
                "command": 'reset_properties'
            }
        ]
    },
    {
        "identifier": 'EVENT_3794_action_queue_sync_7',
        "command": 'action_queue_sync',
        "args": [AreaObjects.SCREEN_FOCUS],
        "subscript": [
            {
                "identifier": 'EVENT_3794_action_queue_sync_7_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [30]
            },
            {
                "identifier": 'EVENT_3794_action_queue_sync_7_SUBSCRIPT_set_animation_speed_1',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_3794_action_queue_sync_7_SUBSCRIPT_walk_1_step_south_2',
                "command": 'walk_1_step_south'
            }
        ]
    },
    {
        "identifier": 'EVENT_3794_remember_last_object_8',
        "command": 'remember_last_object'
    },
    {
        "identifier": 'EVENT_3794_pause_9',
        "command": 'pause',
        "args": [10]
    },
    {
        "identifier": 'EVENT_3794_run_dialog_10',
        "command": 'run_dialog',
        "args": [3888, AreaObjects.NPC_12, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_3794_pause_11',
        "command": 'pause',
        "args": [10]
    },
    {
        "identifier": 'EVENT_3794_action_queue_sync_12',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_3794_action_queue_sync_12_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [8]
            },
            {
                "identifier": 'EVENT_3794_action_queue_sync_12_SUBSCRIPT_face_east_1',
                "command": 'face_east'
            },
            {
                "identifier": 'EVENT_3794_action_queue_sync_12_SUBSCRIPT_pause_2',
                "command": 'pause',
                "args": [2]
            },
            {
                "identifier": 'EVENT_3794_action_queue_sync_12_SUBSCRIPT_face_southeast_3',
                "command": 'face_southeast'
            }
        ]
    },
    {
        "identifier": 'EVENT_3794_action_queue_async_13',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_1],
        "subscript": [
            {
                "identifier": 'EVENT_3794_action_queue_async_13_SUBSCRIPT_visibility_off_0',
                "command": 'visibility_off'
            },
            {
                "identifier": 'EVENT_3794_action_queue_async_13_SUBSCRIPT_transfer_to_xyzf_1',
                "command": 'transfer_to_xyzf',
                "args": [3, 23, 0, RadialDirections.EAST]
            },
            {
                "identifier": 'EVENT_3794_action_queue_async_13_SUBSCRIPT_transfer_xyzf_pixels_2',
                "command": 'transfer_xyzf_pixels',
                "args": [4, 2, 0, RadialDirections.EAST]
            },
            {
                "identifier": 'EVENT_3794_action_queue_async_13_SUBSCRIPT_set_animation_speed_3',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3794_action_queue_async_13_SUBSCRIPT_set_animation_speed_4',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.SLOW, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_3794_action_queue_async_13_SUBSCRIPT_face_southeast_5',
                "command": 'face_southeast'
            },
            {
                "identifier": 'EVENT_3794_action_queue_async_13_SUBSCRIPT_visibility_on_6',
                "command": 'visibility_on'
            },
            {
                "identifier": 'EVENT_3794_action_queue_async_13_SUBSCRIPT_shift_southeast_pixels_7',
                "command": 'shift_southeast_pixels',
                "args": [14]
            },
            {
                "identifier": 'EVENT_3794_action_queue_async_13_SUBSCRIPT_face_northeast_8',
                "command": 'face_northeast'
            },
            {
                "identifier": 'EVENT_3794_action_queue_async_13_SUBSCRIPT_set_animation_speed_9',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3794_action_queue_async_13_SUBSCRIPT_set_sprite_sequence_10',
                "command": 'set_sprite_sequence',
                "args": [5, 0, [_0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_3794_pause_14',
        "command": 'pause',
        "args": [10]
    },
    {
        "identifier": 'EVENT_3794_run_dialog_15',
        "command": 'run_dialog',
        "args": [3889, AreaObjects.NPC_12, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_3794_action_queue_sync_16',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_3794_action_queue_sync_16_SUBSCRIPT_face_east_0',
                "command": 'face_east'
            },
            {
                "identifier": 'EVENT_3794_action_queue_sync_16_SUBSCRIPT_pause_1',
                "command": 'pause',
                "args": [2]
            },
            {
                "identifier": 'EVENT_3794_action_queue_sync_16_SUBSCRIPT_face_northeast_2',
                "command": 'face_northeast'
            }
        ]
    },
    {
        "identifier": 'EVENT_3794_action_queue_async_17',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_1],
        "subscript": [
            {
                "identifier": 'EVENT_3794_action_queue_async_17_SUBSCRIPT_reset_properties_0',
                "command": 'reset_properties'
            }
        ]
    },
    {
        "identifier": 'EVENT_3794_unsync_action_script_18',
        "command": 'unsync_action_script',
        "args": [AreaObjects.NPC_9]
    },
    {
        "identifier": 'EVENT_3794_unsync_action_script_19',
        "command": 'unsync_action_script',
        "args": [AreaObjects.NPC_4]
    },
    {
        "identifier": 'EVENT_3794_unsync_action_script_20',
        "command": 'unsync_action_script',
        "args": [AreaObjects.NPC_5]
    },
    {
        "identifier": 'EVENT_3794_unsync_action_script_21',
        "command": 'unsync_action_script',
        "args": [AreaObjects.NPC_8]
    },
    {
        "identifier": 'EVENT_3794_pause_22',
        "command": 'pause',
        "args": [1]
    },
    {
        "identifier": 'EVENT_3794_jmp_if_bit_clear_23',
        "command": 'jmp_if_bit_clear',
        "args": [0x704c, 0, 'EVENT_3794_pause_22']
    },
    {
        "identifier": 'EVENT_3794_clear_bit_24',
        "command": 'clear_bit',
        "args": [0x704c, 0]
    },
    {
        "identifier": 'EVENT_3794_stop_all_background_events_25',
        "command": 'stop_all_background_events'
    },
    {
        "identifier": 'EVENT_3794_set_bit_26',
        "command": 'set_bit',
        "args": [0x7043, 2]
    },
    {
        "identifier": 'EVENT_3794_set_action_script_sync_27',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_4, 989]
    },
    {
        "identifier": 'EVENT_3794_set_action_script_sync_28',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_9, 988]
    },
    {
        "identifier": 'EVENT_3794_jmp_to_subroutine_29',
        "command": 'jmp_to_subroutine',
        "args": ['EVENT_3794_set_bit_143']
    },
    {
        "identifier": 'EVENT_3794_pause_30',
        "command": 'pause',
        "args": [10]
    },
    {
        "identifier": 'EVENT_3794_run_dialog_31',
        "command": 'run_dialog',
        "args": [3890, AreaObjects.NPC_14, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_3794_jmp_to_subroutine_32',
        "command": 'jmp_to_subroutine',
        "args": ['EVENT_3794_set_bit_148']
    },
    {
        "identifier": 'EVENT_3794_set_bit_33',
        "command": 'set_bit',
        "args": [0x7043, 5]
    },
    {
        "identifier": 'EVENT_3794_set_bit_34',
        "command": 'set_bit',
        "args": [0x7043, 1]
    },
    {
        "identifier": 'EVENT_3794_run_background_event_35',
        "command": 'run_background_event',
        "args": [3793, [_0x40Flags.RETURN_ON_LEVEL_EXIT]]
    },
    {
        "identifier": 'EVENT_3794_pause_36',
        "command": 'pause',
        "args": [90]
    },
    {
        "identifier": 'EVENT_3794_action_queue_sync_37',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_3794_action_queue_sync_37_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3794_action_queue_sync_37_SUBSCRIPT_set_sprite_sequence_1',
                "command": 'set_sprite_sequence',
                "args": [3, 2, [_0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3794_action_queue_sync_37_SUBSCRIPT_pause_2',
                "command": 'pause',
                "args": [30]
            },
            {
                "identifier": 'EVENT_3794_action_queue_sync_37_SUBSCRIPT_reset_properties_3',
                "command": 'reset_properties'
            },
            {
                "identifier": 'EVENT_3794_action_queue_sync_37_SUBSCRIPT_set_animation_speed_4',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.SEQUENCE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_3794_action_queue_sync_38',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_1],
        "subscript": [
            {
                "identifier": 'EVENT_3794_action_queue_sync_38_SUBSCRIPT_set_sprite_sequence_0',
                "command": 'set_sprite_sequence',
                "args": [3, 1, [_0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3794_action_queue_sync_38_SUBSCRIPT_pause_1',
                "command": 'pause',
                "args": [30]
            },
            {
                "identifier": 'EVENT_3794_action_queue_sync_38_SUBSCRIPT_reset_properties_2',
                "command": 'reset_properties'
            }
        ]
    },
    {
        "identifier": 'EVENT_3794_pause_39',
        "command": 'pause',
        "args": [90]
    },
    {
        "identifier": 'EVENT_3794_run_dialog_40',
        "command": 'run_dialog',
        "args": [3891, AreaObjects.NPC_12, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_3794_pause_41',
        "command": 'pause',
        "args": [60]
    },
    {
        "identifier": 'EVENT_3794_action_queue_sync_42',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_3794_action_queue_sync_42_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [8]
            },
            {
                "identifier": 'EVENT_3794_action_queue_sync_42_SUBSCRIPT_face_north_1',
                "command": 'face_north'
            },
            {
                "identifier": 'EVENT_3794_action_queue_sync_42_SUBSCRIPT_pause_2',
                "command": 'pause',
                "args": [2]
            },
            {
                "identifier": 'EVENT_3794_action_queue_sync_42_SUBSCRIPT_face_northwest_3',
                "command": 'face_northwest'
            }
        ]
    },
    {
        "identifier": 'EVENT_3794_action_queue_sync_43',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_1],
        "subscript": [
            {
                "identifier": 'EVENT_3794_action_queue_sync_43_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [10]
            },
            {
                "identifier": 'EVENT_3794_action_queue_sync_43_SUBSCRIPT_face_northwest_1',
                "command": 'face_northwest'
            }
        ]
    },
    {
        "identifier": 'EVENT_3794_action_queue_async_44',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_2],
        "subscript": [
            {
                "identifier": 'EVENT_3794_action_queue_async_44_SUBSCRIPT_visibility_off_0',
                "command": 'visibility_off'
            },
            {
                "identifier": 'EVENT_3794_action_queue_async_44_SUBSCRIPT_transfer_to_xyzf_1',
                "command": 'transfer_to_xyzf',
                "args": [3, 23, 0, RadialDirections.EAST]
            },
            {
                "identifier": 'EVENT_3794_action_queue_async_44_SUBSCRIPT_transfer_xyzf_pixels_2',
                "command": 'transfer_xyzf_pixels',
                "args": [252, 254, 0, RadialDirections.EAST]
            },
            {
                "identifier": 'EVENT_3794_action_queue_async_44_SUBSCRIPT_set_animation_speed_3',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3794_action_queue_async_44_SUBSCRIPT_set_animation_speed_4',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.SLOW, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_3794_action_queue_async_44_SUBSCRIPT_face_northwest_5',
                "command": 'face_northwest'
            },
            {
                "identifier": 'EVENT_3794_action_queue_async_44_SUBSCRIPT_visibility_on_6',
                "command": 'visibility_on'
            },
            {
                "identifier": 'EVENT_3794_action_queue_async_44_SUBSCRIPT_shift_northwest_pixels_7',
                "command": 'shift_northwest_pixels',
                "args": [14]
            },
            {
                "identifier": 'EVENT_3794_action_queue_async_44_SUBSCRIPT_face_northeast_8',
                "command": 'face_northeast'
            },
            {
                "identifier": 'EVENT_3794_action_queue_async_44_SUBSCRIPT_pause_9',
                "command": 'pause',
                "args": [30]
            },
            {
                "identifier": 'EVENT_3794_action_queue_async_44_SUBSCRIPT_set_animation_speed_10',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3794_action_queue_async_44_SUBSCRIPT_set_sprite_sequence_11',
                "command": 'set_sprite_sequence',
                "args": [5, 0, [_0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_3794_run_dialog_45',
        "command": 'run_dialog',
        "args": [3892, AreaObjects.NPC_12, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_3794_action_queue_sync_46',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_3794_action_queue_sync_46_SUBSCRIPT_face_north_0',
                "command": 'face_north'
            },
            {
                "identifier": 'EVENT_3794_action_queue_sync_46_SUBSCRIPT_pause_1',
                "command": 'pause',
                "args": [2]
            },
            {
                "identifier": 'EVENT_3794_action_queue_sync_46_SUBSCRIPT_face_northeast_2',
                "command": 'face_northeast'
            }
        ]
    },
    {
        "identifier": 'EVENT_3794_action_queue_sync_47',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_1],
        "subscript": [
            {
                "identifier": 'EVENT_3794_action_queue_sync_47_SUBSCRIPT_face_northeast_0',
                "command": 'face_northeast'
            }
        ]
    },
    {
        "identifier": 'EVENT_3794_action_queue_async_48',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_2],
        "subscript": [
            {
                "identifier": 'EVENT_3794_action_queue_async_48_SUBSCRIPT_reset_properties_0',
                "command": 'reset_properties'
            },
            {
                "identifier": 'EVENT_3794_action_queue_async_48_SUBSCRIPT_set_animation_speed_1',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.SEQUENCE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_3794_pause_49',
        "command": 'pause',
        "args": [30]
    },
    {
        "identifier": 'EVENT_3794_action_queue_async_50',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_3794_action_queue_async_50_SUBSCRIPT_jump_to_height_0',
                "command": 'jump_to_height',
                "args": [80]
            },
            {
                "identifier": 'EVENT_3794_action_queue_async_50_SUBSCRIPT_pause_1',
                "command": 'pause',
                "args": [1]
            },
            {
                "identifier": 'EVENT_3794_action_queue_async_50_SUBSCRIPT_jmp_if_mario_in_air_2',
                "command": 'jmp_if_mario_in_air',
                "args": ['EVENT_3794_action_queue_async_50_SUBSCRIPT_pause_1']
            },
            {
                "identifier": 'EVENT_3794_action_queue_async_50_SUBSCRIPT_jump_to_height_3',
                "command": 'jump_to_height',
                "args": [80]
            },
            {
                "identifier": 'EVENT_3794_action_queue_async_50_SUBSCRIPT_pause_4',
                "command": 'pause',
                "args": [1]
            },
            {
                "identifier": 'EVENT_3794_action_queue_async_50_SUBSCRIPT_jmp_if_mario_in_air_5',
                "command": 'jmp_if_mario_in_air',
                "args": ['EVENT_3794_action_queue_async_50_SUBSCRIPT_pause_4']
            }
        ]
    },
    {
        "identifier": 'EVENT_3794_pause_51',
        "command": 'pause',
        "args": [60]
    },
    {
        "identifier": 'EVENT_3794_unsync_action_script_52',
        "command": 'unsync_action_script',
        "args": [AreaObjects.NPC_9]
    },
    {
        "identifier": 'EVENT_3794_unsync_action_script_53',
        "command": 'unsync_action_script',
        "args": [AreaObjects.NPC_4]
    },
    {
        "identifier": 'EVENT_3794_unsync_action_script_54',
        "command": 'unsync_action_script',
        "args": [AreaObjects.NPC_5]
    },
    {
        "identifier": 'EVENT_3794_unsync_action_script_55',
        "command": 'unsync_action_script',
        "args": [AreaObjects.NPC_8]
    },
    {
        "identifier": 'EVENT_3794_pause_56',
        "command": 'pause',
        "args": [1]
    },
    {
        "identifier": 'EVENT_3794_jmp_if_bit_clear_57',
        "command": 'jmp_if_bit_clear',
        "args": [0x704c, 0, 'EVENT_3794_pause_56']
    },
    {
        "identifier": 'EVENT_3794_clear_bit_58',
        "command": 'clear_bit',
        "args": [0x704c, 0]
    },
    {
        "identifier": 'EVENT_3794_stop_all_background_events_59',
        "command": 'stop_all_background_events'
    },
    {
        "identifier": 'EVENT_3794_clear_bit_60',
        "command": 'clear_bit',
        "args": [0x7043, 1]
    },
    {
        "identifier": 'EVENT_3794_clear_bit_61',
        "command": 'clear_bit',
        "args": [0x7043, 5]
    },
    {
        "identifier": 'EVENT_3794_set_action_script_sync_62',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_4, 989]
    },
    {
        "identifier": 'EVENT_3794_set_action_script_sync_63',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_9, 988]
    },
    {
        "identifier": 'EVENT_3794_jmp_to_subroutine_64',
        "command": 'jmp_to_subroutine',
        "args": ['EVENT_3794_set_bit_143']
    },
    {
        "identifier": 'EVENT_3794_pause_65',
        "command": 'pause',
        "args": [10]
    },
    {
        "identifier": 'EVENT_3794_run_dialog_66',
        "command": 'run_dialog',
        "args": [3893, AreaObjects.NPC_14, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_3794_jmp_to_subroutine_67',
        "command": 'jmp_to_subroutine',
        "args": ['EVENT_3794_set_bit_148']
    },
    {
        "identifier": 'EVENT_3794_pause_68',
        "command": 'pause',
        "args": [30]
    },
    {
        "identifier": 'EVENT_3794_play_sound_69',
        "command": 'play_sound',
        "args": [Sounds._026_LAUGHING_BOWSER, 6]
    },
    {
        "identifier": 'EVENT_3794_pause_70',
        "command": 'pause',
        "args": [30]
    },
    {
        "identifier": 'EVENT_3794_action_queue_sync_71',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_3794_action_queue_sync_71_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [10]
            },
            {
                "identifier": 'EVENT_3794_action_queue_sync_71_SUBSCRIPT_face_north_1',
                "command": 'face_north'
            },
            {
                "identifier": 'EVENT_3794_action_queue_sync_71_SUBSCRIPT_pause_2',
                "command": 'pause',
                "args": [2]
            },
            {
                "identifier": 'EVENT_3794_action_queue_sync_71_SUBSCRIPT_face_northwest_3',
                "command": 'face_northwest'
            },
            {
                "identifier": 'EVENT_3794_action_queue_sync_71_SUBSCRIPT_pause_4',
                "command": 'pause',
                "args": [2]
            },
            {
                "identifier": 'EVENT_3794_action_queue_sync_71_SUBSCRIPT_face_west_5',
                "command": 'face_west'
            }
        ]
    },
    {
        "identifier": 'EVENT_3794_action_queue_sync_72',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_2],
        "subscript": [
            {
                "identifier": 'EVENT_3794_action_queue_sync_72_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [10]
            },
            {
                "identifier": 'EVENT_3794_action_queue_sync_72_SUBSCRIPT_face_southeast_1',
                "command": 'face_southeast'
            },
            {
                "identifier": 'EVENT_3794_action_queue_sync_72_SUBSCRIPT_pause_2',
                "command": 'pause',
                "args": [2]
            },
            {
                "identifier": 'EVENT_3794_action_queue_sync_72_SUBSCRIPT_face_southwest_3',
                "command": 'face_southwest'
            }
        ]
    },
    {
        "identifier": 'EVENT_3794_action_queue_sync_73',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_1],
        "subscript": [
            {
                "identifier": 'EVENT_3794_action_queue_sync_73_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [10]
            },
            {
                "identifier": 'EVENT_3794_action_queue_sync_73_SUBSCRIPT_face_northwest_1',
                "command": 'face_northwest'
            },
            {
                "identifier": 'EVENT_3794_action_queue_sync_73_SUBSCRIPT_pause_2',
                "command": 'pause',
                "args": [2]
            },
            {
                "identifier": 'EVENT_3794_action_queue_sync_73_SUBSCRIPT_set_sprite_sequence_3',
                "command": 'set_sprite_sequence',
                "args": [19, 0, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_3794_action_queue_async_74',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_3],
        "subscript": [
            {
                "identifier": 'EVENT_3794_action_queue_async_74_SUBSCRIPT_visibility_off_0',
                "command": 'visibility_off'
            },
            {
                "identifier": 'EVENT_3794_action_queue_async_74_SUBSCRIPT_transfer_to_xyzf_1',
                "command": 'transfer_to_xyzf',
                "args": [3, 23, 0, RadialDirections.EAST]
            },
            {
                "identifier": 'EVENT_3794_action_queue_async_74_SUBSCRIPT_transfer_xyzf_pixels_2',
                "command": 'transfer_xyzf_pixels',
                "args": [248, 0, 0, RadialDirections.EAST]
            },
            {
                "identifier": 'EVENT_3794_action_queue_async_74_SUBSCRIPT_set_animation_speed_3',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3794_action_queue_async_74_SUBSCRIPT_set_animation_speed_4',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_3794_action_queue_async_74_SUBSCRIPT_face_southwest_5',
                "command": 'face_southwest'
            },
            {
                "identifier": 'EVENT_3794_action_queue_async_74_SUBSCRIPT_visibility_on_6',
                "command": 'visibility_on'
            },
            {
                "identifier": 'EVENT_3794_action_queue_async_74_SUBSCRIPT_shift_west_pixels_7',
                "command": 'shift_west_pixels',
                "args": [24]
            },
            {
                "identifier": 'EVENT_3794_action_queue_async_74_SUBSCRIPT_face_northwest_8',
                "command": 'face_northwest'
            },
            {
                "identifier": 'EVENT_3794_action_queue_async_74_SUBSCRIPT_pause_9',
                "command": 'pause',
                "args": [2]
            },
            {
                "identifier": 'EVENT_3794_action_queue_async_74_SUBSCRIPT_face_northeast_10',
                "command": 'face_northeast'
            },
            {
                "identifier": 'EVENT_3794_action_queue_async_74_SUBSCRIPT_pause_11',
                "command": 'pause',
                "args": [30]
            },
            {
                "identifier": 'EVENT_3794_action_queue_async_74_SUBSCRIPT_set_animation_speed_12',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3794_action_queue_async_74_SUBSCRIPT_set_sprite_sequence_13',
                "command": 'set_sprite_sequence',
                "args": [5, 0, [_0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_3794_pause_75',
        "command": 'pause',
        "args": [10]
    },
    {
        "identifier": 'EVENT_3794_run_dialog_76',
        "command": 'run_dialog',
        "args": [3894, AreaObjects.NPC_12, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_3794_action_queue_sync_77',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_3794_action_queue_sync_77_SUBSCRIPT_start_loop_n_times_0',
                "command": 'start_loop_n_times',
                "args": [2]
            },
            {
                "identifier": 'EVENT_3794_action_queue_sync_77_SUBSCRIPT_turn_clockwise_45_degrees_n_times_1',
                "command": 'turn_clockwise_45_degrees_n_times',
                "args": [1]
            },
            {
                "identifier": 'EVENT_3794_action_queue_sync_77_SUBSCRIPT_pause_2',
                "command": 'pause',
                "args": [2]
            },
            {
                "identifier": 'EVENT_3794_action_queue_sync_77_SUBSCRIPT_end_loop_3',
                "command": 'end_loop'
            }
        ]
    },
    {
        "identifier": 'EVENT_3794_action_queue_sync_78',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_3],
        "subscript": [
            {
                "identifier": 'EVENT_3794_action_queue_sync_78_SUBSCRIPT_reset_properties_0',
                "command": 'reset_properties'
            }
        ]
    },
    {
        "identifier": 'EVENT_3794_action_queue_sync_79',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_1],
        "subscript": [
            {
                "identifier": 'EVENT_3794_action_queue_sync_79_SUBSCRIPT_reset_properties_0',
                "command": 'reset_properties'
            },
            {
                "identifier": 'EVENT_3794_action_queue_sync_79_SUBSCRIPT_face_northeast_1',
                "command": 'face_northeast'
            }
        ]
    },
    {
        "identifier": 'EVENT_3794_action_queue_sync_80',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_2],
        "subscript": [
            {
                "identifier": 'EVENT_3794_action_queue_sync_80_SUBSCRIPT_face_southeast_0',
                "command": 'face_southeast'
            },
            {
                "identifier": 'EVENT_3794_action_queue_sync_80_SUBSCRIPT_pause_1',
                "command": 'pause',
                "args": [2]
            },
            {
                "identifier": 'EVENT_3794_action_queue_sync_80_SUBSCRIPT_face_northeast_2',
                "command": 'face_northeast'
            }
        ]
    },
    {
        "identifier": 'EVENT_3794_remember_last_object_81',
        "command": 'remember_last_object'
    },
    {
        "identifier": 'EVENT_3794_pause_82',
        "command": 'pause',
        "args": [30]
    },
    {
        "identifier": 'EVENT_3794_jmp_to_subroutine_83',
        "command": 'jmp_to_subroutine',
        "args": ['EVENT_3794_set_bit_143']
    },
    {
        "identifier": 'EVENT_3794_pause_84',
        "command": 'pause',
        "args": [10]
    },
    {
        "identifier": 'EVENT_3794_run_dialog_85',
        "command": 'run_dialog',
        "args": [3895, AreaObjects.NPC_14, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_3794_jmp_to_subroutine_86',
        "command": 'jmp_to_subroutine',
        "args": ['EVENT_3794_set_bit_148']
    },
    {
        "identifier": 'EVENT_3794_pause_87',
        "command": 'pause',
        "args": [30]
    },
    {
        "identifier": 'EVENT_3794_action_queue_sync_88',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_0],
        "subscript": [
            {
                "identifier": 'EVENT_3794_action_queue_sync_88_SUBSCRIPT_visibility_off_0',
                "command": 'visibility_off'
            },
            {
                "identifier": 'EVENT_3794_action_queue_sync_88_SUBSCRIPT_transfer_to_xyzf_1',
                "command": 'transfer_to_xyzf',
                "args": [3, 23, 0, RadialDirections.EAST]
            },
            {
                "identifier": 'EVENT_3794_action_queue_sync_88_SUBSCRIPT_transfer_xyzf_pixels_2',
                "command": 'transfer_xyzf_pixels',
                "args": [4, 2, 0, RadialDirections.EAST]
            },
            {
                "identifier": 'EVENT_3794_action_queue_sync_88_SUBSCRIPT_set_animation_speed_3',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.SLOW, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_3794_action_queue_sync_88_SUBSCRIPT_set_animation_speed_4',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3794_action_queue_sync_88_SUBSCRIPT_visibility_on_5',
                "command": 'visibility_on'
            },
            {
                "identifier": 'EVENT_3794_action_queue_sync_88_SUBSCRIPT_shift_southeast_pixels_6',
                "command": 'shift_southeast_pixels',
                "args": [14]
            },
            {
                "identifier": 'EVENT_3794_action_queue_sync_88_SUBSCRIPT_face_northeast_7',
                "command": 'face_northeast'
            }
        ]
    },
    {
        "identifier": 'EVENT_3794_action_queue_sync_89',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_1],
        "subscript": [
            {
                "identifier": 'EVENT_3794_action_queue_sync_89_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [4]
            },
            {
                "identifier": 'EVENT_3794_action_queue_sync_89_SUBSCRIPT_reset_properties_1',
                "command": 'reset_properties'
            },
            {
                "identifier": 'EVENT_3794_action_queue_sync_89_SUBSCRIPT_pause_2',
                "command": 'pause',
                "args": [2]
            },
            {
                "identifier": 'EVENT_3794_action_queue_sync_89_SUBSCRIPT_set_animation_speed_3',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3794_action_queue_sync_89_SUBSCRIPT_walk_1_step_southwest_4',
                "command": 'walk_1_step_southwest'
            },
            {
                "identifier": 'EVENT_3794_action_queue_sync_89_SUBSCRIPT_face_northwest_5',
                "command": 'face_northwest'
            },
            {
                "identifier": 'EVENT_3794_action_queue_sync_89_SUBSCRIPT_pause_6',
                "command": 'pause',
                "args": [2]
            },
            {
                "identifier": 'EVENT_3794_action_queue_sync_89_SUBSCRIPT_face_northeast_7',
                "command": 'face_northeast'
            }
        ]
    },
    {
        "identifier": 'EVENT_3794_action_queue_sync_90',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_3794_action_queue_sync_90_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [20]
            },
            {
                "identifier": 'EVENT_3794_action_queue_sync_90_SUBSCRIPT_face_east_1',
                "command": 'face_east'
            },
            {
                "identifier": 'EVENT_3794_action_queue_sync_90_SUBSCRIPT_pause_2',
                "command": 'pause',
                "args": [2]
            },
            {
                "identifier": 'EVENT_3794_action_queue_sync_90_SUBSCRIPT_face_southeast_3',
                "command": 'face_southeast'
            }
        ]
    },
    {
        "identifier": 'EVENT_3794_action_queue_sync_91',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_2],
        "subscript": [
            {
                "identifier": 'EVENT_3794_action_queue_sync_91_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [20]
            },
            {
                "identifier": 'EVENT_3794_action_queue_sync_91_SUBSCRIPT_face_southeast_1',
                "command": 'face_southeast'
            }
        ]
    },
    {
        "identifier": 'EVENT_3794_action_queue_sync_92',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_3],
        "subscript": [
            {
                "identifier": 'EVENT_3794_action_queue_sync_92_SUBSCRIPT_set_sprite_sequence_0',
                "command": 'set_sprite_sequence',
                "args": [19, 0, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_3794_remember_last_object_93',
        "command": 'remember_last_object'
    },
    {
        "identifier": 'EVENT_3794_action_queue_async_94',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_0],
        "subscript": [
            {
                "identifier": 'EVENT_3794_action_queue_async_94_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3794_action_queue_async_94_SUBSCRIPT_set_sprite_sequence_1',
                "command": 'set_sprite_sequence',
                "args": [5, 0, [_0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_3794_pause_95',
        "command": 'pause',
        "args": [10]
    },
    {
        "identifier": 'EVENT_3794_run_dialog_96',
        "command": 'run_dialog',
        "args": [3896, AreaObjects.NPC_12, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_3794_pause_97',
        "command": 'pause',
        "args": [10]
    },
    {
        "identifier": 'EVENT_3794_action_queue_sync_98',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_3794_action_queue_sync_98_SUBSCRIPT_face_east_0',
                "command": 'face_east'
            },
            {
                "identifier": 'EVENT_3794_action_queue_sync_98_SUBSCRIPT_pause_1',
                "command": 'pause',
                "args": [2]
            },
            {
                "identifier": 'EVENT_3794_action_queue_sync_98_SUBSCRIPT_face_northeast_2',
                "command": 'face_northeast'
            }
        ]
    },
    {
        "identifier": 'EVENT_3794_action_queue_sync_99',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_3],
        "subscript": [
            {
                "identifier": 'EVENT_3794_action_queue_sync_99_SUBSCRIPT_reset_properties_0',
                "command": 'reset_properties'
            }
        ]
    },
    {
        "identifier": 'EVENT_3794_action_queue_sync_100',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_2],
        "subscript": [
            {
                "identifier": 'EVENT_3794_action_queue_sync_100_SUBSCRIPT_face_northeast_0',
                "command": 'face_northeast'
            }
        ]
    },
    {
        "identifier": 'EVENT_3794_action_queue_sync_101',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_0],
        "subscript": [
            {
                "identifier": 'EVENT_3794_action_queue_sync_101_SUBSCRIPT_reset_properties_0',
                "command": 'reset_properties'
            }
        ]
    },
    {
        "identifier": 'EVENT_3794_jmp_to_subroutine_102',
        "command": 'jmp_to_subroutine',
        "args": ['EVENT_3794_set_bit_143']
    },
    {
        "identifier": 'EVENT_3794_pause_103',
        "command": 'pause',
        "args": [10]
    },
    {
        "identifier": 'EVENT_3794_run_dialog_104',
        "command": 'run_dialog',
        "args": [3897, AreaObjects.NPC_14, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_3794_jmp_to_subroutine_105',
        "command": 'jmp_to_subroutine',
        "args": ['EVENT_3794_set_bit_148']
    },
    {
        "identifier": 'EVENT_3794_action_queue_async_106',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_3794_action_queue_async_106_SUBSCRIPT_start_loop_n_times_0',
                "command": 'start_loop_n_times',
                "args": [3]
            },
            {
                "identifier": 'EVENT_3794_action_queue_async_106_SUBSCRIPT_turn_clockwise_45_degrees_n_times_1',
                "command": 'turn_clockwise_45_degrees_n_times',
                "args": [1]
            },
            {
                "identifier": 'EVENT_3794_action_queue_async_106_SUBSCRIPT_pause_2',
                "command": 'pause',
                "args": [2]
            },
            {
                "identifier": 'EVENT_3794_action_queue_async_106_SUBSCRIPT_end_loop_3',
                "command": 'end_loop'
            }
        ]
    },
    {
        "identifier": 'EVENT_3794_action_queue_sync_107',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_0],
        "subscript": [
            {
                "identifier": 'EVENT_3794_action_queue_sync_107_SUBSCRIPT_face_northwest_0',
                "command": 'face_northwest'
            }
        ]
    },
    {
        "identifier": 'EVENT_3794_action_queue_sync_108',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_1],
        "subscript": [
            {
                "identifier": 'EVENT_3794_action_queue_sync_108_SUBSCRIPT_set_sprite_sequence_0',
                "command": 'set_sprite_sequence',
                "args": [18, 0, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_3794_action_queue_sync_109',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_2],
        "subscript": [
            {
                "identifier": 'EVENT_3794_action_queue_sync_109_SUBSCRIPT_face_southeast_0',
                "command": 'face_southeast'
            }
        ]
    },
    {
        "identifier": 'EVENT_3794_action_queue_sync_110',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_3],
        "subscript": [
            {
                "identifier": 'EVENT_3794_action_queue_sync_110_SUBSCRIPT_set_sprite_sequence_0',
                "command": 'set_sprite_sequence',
                "args": [19, 0, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_3794_remember_last_object_111',
        "command": 'remember_last_object'
    },
    {
        "identifier": 'EVENT_3794_pause_112',
        "command": 'pause',
        "args": [30]
    },
    {
        "identifier": 'EVENT_3794_action_queue_async_113',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_3794_action_queue_async_113_SUBSCRIPT_jump_to_height_0',
                "command": 'jump_to_height',
                "args": [80]
            },
            {
                "identifier": 'EVENT_3794_action_queue_async_113_SUBSCRIPT_pause_1',
                "command": 'pause',
                "args": [1]
            },
            {
                "identifier": 'EVENT_3794_action_queue_async_113_SUBSCRIPT_jmp_if_mario_in_air_2',
                "command": 'jmp_if_mario_in_air',
                "args": ['EVENT_3794_action_queue_async_113_SUBSCRIPT_pause_1']
            },
            {
                "identifier": 'EVENT_3794_action_queue_async_113_SUBSCRIPT_jump_to_height_3',
                "command": 'jump_to_height',
                "args": [80]
            },
            {
                "identifier": 'EVENT_3794_action_queue_async_113_SUBSCRIPT_pause_4',
                "command": 'pause',
                "args": [1]
            },
            {
                "identifier": 'EVENT_3794_action_queue_async_113_SUBSCRIPT_jmp_if_mario_in_air_5',
                "command": 'jmp_if_mario_in_air',
                "args": ['EVENT_3794_action_queue_async_113_SUBSCRIPT_pause_4']
            }
        ]
    },
    {
        "identifier": 'EVENT_3794_pause_114',
        "command": 'pause',
        "args": [20]
    },
    {
        "identifier": 'EVENT_3794_action_queue_sync_115',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_0],
        "subscript": [
            {
                "identifier": 'EVENT_3794_action_queue_sync_115_SUBSCRIPT_set_sprite_sequence_0',
                "command": 'set_sprite_sequence',
                "args": [15, 0, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3794_action_queue_sync_115_SUBSCRIPT_pause_1',
                "command": 'pause',
                "args": [8]
            },
            {
                "identifier": 'EVENT_3794_action_queue_sync_115_SUBSCRIPT_reset_properties_2',
                "command": 'reset_properties'
            },
            {
                "identifier": 'EVENT_3794_action_queue_sync_115_SUBSCRIPT_pause_3',
                "command": 'pause',
                "args": [40]
            },
            {
                "identifier": 'EVENT_3794_action_queue_sync_115_SUBSCRIPT_set_animation_speed_4',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3794_action_queue_sync_115_SUBSCRIPT_set_animation_speed_5',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.SLOW, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_3794_action_queue_sync_115_SUBSCRIPT_shift_northwest_pixels_6',
                "command": 'shift_northwest_pixels',
                "args": [14]
            },
            {
                "identifier": 'EVENT_3794_action_queue_sync_115_SUBSCRIPT_transfer_to_xyzf_7',
                "command": 'transfer_to_xyzf',
                "args": [7, 65, 0, RadialDirections.EAST]
            }
        ]
    },
    {
        "identifier": 'EVENT_3794_action_queue_sync_116',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_2],
        "subscript": [
            {
                "identifier": 'EVENT_3794_action_queue_sync_116_SUBSCRIPT_set_sprite_sequence_0',
                "command": 'set_sprite_sequence',
                "args": [14, 0, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_3794_action_queue_sync_116_SUBSCRIPT_pause_1',
                "command": 'pause',
                "args": [8]
            },
            {
                "identifier": 'EVENT_3794_action_queue_sync_116_SUBSCRIPT_reset_properties_2',
                "command": 'reset_properties'
            },
            {
                "identifier": 'EVENT_3794_action_queue_sync_116_SUBSCRIPT_pause_3',
                "command": 'pause',
                "args": [40]
            },
            {
                "identifier": 'EVENT_3794_action_queue_sync_116_SUBSCRIPT_set_animation_speed_4',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3794_action_queue_sync_116_SUBSCRIPT_set_animation_speed_5',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.SLOW, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_3794_action_queue_sync_116_SUBSCRIPT_shift_southeast_pixels_6',
                "command": 'shift_southeast_pixels',
                "args": [14]
            },
            {
                "identifier": 'EVENT_3794_action_queue_sync_116_SUBSCRIPT_transfer_to_xyzf_7',
                "command": 'transfer_to_xyzf',
                "args": [7, 69, 0, RadialDirections.EAST]
            }
        ]
    },
    {
        "identifier": 'EVENT_3794_action_queue_sync_117',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_1],
        "subscript": [
            {
                "identifier": 'EVENT_3794_action_queue_sync_117_SUBSCRIPT_set_sprite_sequence_0',
                "command": 'set_sprite_sequence',
                "args": [15, 0, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_3794_action_queue_sync_117_SUBSCRIPT_pause_1',
                "command": 'pause',
                "args": [8]
            },
            {
                "identifier": 'EVENT_3794_action_queue_sync_117_SUBSCRIPT_reset_properties_2',
                "command": 'reset_properties'
            },
            {
                "identifier": 'EVENT_3794_action_queue_sync_117_SUBSCRIPT_pause_3',
                "command": 'pause',
                "args": [40]
            },
            {
                "identifier": 'EVENT_3794_action_queue_sync_117_SUBSCRIPT_set_animation_speed_4',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3794_action_queue_sync_117_SUBSCRIPT_set_animation_speed_5',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.SLOW, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_3794_action_queue_sync_117_SUBSCRIPT_shift_north_pixels_6',
                "command": 'shift_north_pixels',
                "args": [14]
            },
            {
                "identifier": 'EVENT_3794_action_queue_sync_117_SUBSCRIPT_transfer_to_xyzf_7',
                "command": 'transfer_to_xyzf',
                "args": [7, 67, 0, RadialDirections.EAST]
            }
        ]
    },
    {
        "identifier": 'EVENT_3794_action_queue_sync_118',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_3],
        "subscript": [
            {
                "identifier": 'EVENT_3794_action_queue_sync_118_SUBSCRIPT_set_sprite_sequence_0',
                "command": 'set_sprite_sequence',
                "args": [15, 0, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_3794_action_queue_sync_118_SUBSCRIPT_pause_1',
                "command": 'pause',
                "args": [8]
            },
            {
                "identifier": 'EVENT_3794_action_queue_sync_118_SUBSCRIPT_reset_properties_2',
                "command": 'reset_properties'
            },
            {
                "identifier": 'EVENT_3794_action_queue_sync_118_SUBSCRIPT_pause_3',
                "command": 'pause',
                "args": [40]
            },
            {
                "identifier": 'EVENT_3794_action_queue_sync_118_SUBSCRIPT_set_animation_speed_4',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3794_action_queue_sync_118_SUBSCRIPT_set_animation_speed_5',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_3794_action_queue_sync_118_SUBSCRIPT_shift_east_pixels_6',
                "command": 'shift_east_pixels',
                "args": [24]
            },
            {
                "identifier": 'EVENT_3794_action_queue_sync_118_SUBSCRIPT_transfer_to_xyzf_7',
                "command": 'transfer_to_xyzf',
                "args": [9, 69, 0, RadialDirections.EAST]
            }
        ]
    },
    {
        "identifier": 'EVENT_3794_remember_last_object_119',
        "command": 'remember_last_object'
    },
    {
        "identifier": 'EVENT_3794_pause_120',
        "command": 'pause',
        "args": [10]
    },
    {
        "identifier": 'EVENT_3794_action_queue_async_121',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_3794_action_queue_async_121_SUBSCRIPT_start_loop_n_times_0',
                "command": 'start_loop_n_times',
                "args": [3]
            },
            {
                "identifier": 'EVENT_3794_action_queue_async_121_SUBSCRIPT_turn_clockwise_45_degrees_n_times_1',
                "command": 'turn_clockwise_45_degrees_n_times',
                "args": [1]
            },
            {
                "identifier": 'EVENT_3794_action_queue_async_121_SUBSCRIPT_pause_2',
                "command": 'pause',
                "args": [2]
            },
            {
                "identifier": 'EVENT_3794_action_queue_async_121_SUBSCRIPT_end_loop_3',
                "command": 'end_loop'
            },
            {
                "identifier": 'EVENT_3794_action_queue_async_121_SUBSCRIPT_set_sprite_sequence_4',
                "command": 'set_sprite_sequence',
                "args": [0, 6, [_0x08Flags.READ_AS_SEQUENCE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_3794_jmp_to_subroutine_122',
        "command": 'jmp_to_subroutine',
        "args": ['EVENT_3794_set_bit_143']
    },
    {
        "identifier": 'EVENT_3794_pause_123',
        "command": 'pause',
        "args": [10]
    },
    {
        "identifier": 'EVENT_3794_run_dialog_124',
        "command": 'run_dialog',
        "args": [3898, AreaObjects.NPC_14, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_3794_jmp_to_subroutine_125',
        "command": 'jmp_to_subroutine',
        "args": ['EVENT_3794_set_bit_148']
    },
    {
        "identifier": 'EVENT_3794_pause_126',
        "command": 'pause',
        "args": [30]
    },
    {
        "identifier": 'EVENT_3794_unfreeze_camera_127',
        "command": 'unfreeze_camera'
    },
    {
        "identifier": 'EVENT_3794_set_bit_128',
        "command": 'set_bit',
        "args": [0x7043, 5]
    },
    {
        "identifier": 'EVENT_3794_unsync_action_script_129',
        "command": 'unsync_action_script',
        "args": [AreaObjects.NPC_9]
    },
    {
        "identifier": 'EVENT_3794_unsync_action_script_130',
        "command": 'unsync_action_script',
        "args": [AreaObjects.NPC_4]
    },
    {
        "identifier": 'EVENT_3794_action_queue_sync_131',
        "command": 'action_queue_sync',
        "args": [AreaObjects.SCREEN_FOCUS],
        "subscript": [
            {
                "identifier": 'EVENT_3794_action_queue_sync_131_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [20]
            },
            {
                "identifier": 'EVENT_3794_action_queue_sync_131_SUBSCRIPT_set_animation_speed_1',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_3794_action_queue_sync_131_SUBSCRIPT_walk_1_step_northeast_2',
                "command": 'walk_1_step_northeast'
            }
        ]
    },
    {
        "identifier": 'EVENT_3794_action_queue_sync_132',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_3794_action_queue_sync_132_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [20]
            },
            {
                "identifier": 'EVENT_3794_action_queue_sync_132_SUBSCRIPT_reset_properties_1',
                "command": 'reset_properties'
            },
            {
                "identifier": 'EVENT_3794_action_queue_sync_132_SUBSCRIPT_set_animation_speed_2',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_3794_action_queue_sync_132_SUBSCRIPT_set_vram_priority_3',
                "command": 'set_vram_priority',
                "args": [VramPriority.OBJECT_OVERLAPS_MARIO_ON_ALL_SIDES]
            },
            {
                "identifier": 'EVENT_3794_action_queue_sync_132_SUBSCRIPT_jump_to_height_4',
                "command": 'jump_to_height',
                "args": [152]
            },
            {
                "identifier": 'EVENT_3794_action_queue_sync_132_SUBSCRIPT_shift_northeast_steps_5',
                "command": 'shift_northeast_steps',
                "args": [2]
            },
            {
                "identifier": 'EVENT_3794_action_queue_sync_132_SUBSCRIPT_set_sprite_sequence_6',
                "command": 'set_sprite_sequence',
                "args": [9, 1, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_3794_action_queue_sync_132_SUBSCRIPT_shift_northeast_steps_7',
                "command": 'shift_northeast_steps',
                "args": [2]
            },
            {
                "identifier": 'EVENT_3794_action_queue_sync_132_SUBSCRIPT_floating_off_8',
                "command": 'floating_off'
            },
            {
                "identifier": 'EVENT_3794_action_queue_sync_132_SUBSCRIPT_set_sprite_sequence_9',
                "command": 'set_sprite_sequence',
                "args": [9, 1, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_3794_pause_133',
        "command": 'pause',
        "args": [10]
    },
    {
        "identifier": 'EVENT_3794_pause_action_script_134',
        "command": 'pause_action_script',
        "args": [AreaObjects.NPC_8]
    },
    {
        "identifier": 'EVENT_3794_action_queue_sync_135',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_9],
        "subscript": [
            {
                "identifier": 'EVENT_3794_action_queue_sync_135_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_3794_action_queue_sync_135_SUBSCRIPT_shift_northeast_pixels_1',
                "command": 'shift_northeast_pixels',
                "args": [2]
            },
            {
                "identifier": 'EVENT_3794_action_queue_sync_135_SUBSCRIPT_set_animation_speed_2',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_SLOW, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_3794_action_queue_sync_135_SUBSCRIPT_shift_south_pixels_3',
                "command": 'shift_south_pixels',
                "args": [4]
            },
            {
                "identifier": 'EVENT_3794_action_queue_sync_135_SUBSCRIPT_shift_southwest_pixels_4',
                "command": 'shift_southwest_pixels',
                "args": [6]
            }
        ]
    },
    {
        "identifier": 'EVENT_3794_action_queue_sync_136',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_4],
        "subscript": [
            {
                "identifier": 'EVENT_3794_action_queue_sync_136_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.SLOW, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3794_action_queue_sync_136_SUBSCRIPT_set_sprite_sequence_1',
                "command": 'set_sprite_sequence',
                "args": [2, 0, [_0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3794_action_queue_sync_136_SUBSCRIPT_pause_2',
                "command": 'pause',
                "args": [40]
            },
            {
                "identifier": 'EVENT_3794_action_queue_sync_136_SUBSCRIPT_set_sprite_sequence_3',
                "command": 'set_sprite_sequence',
                "args": [12, 0, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_3794_action_queue_sync_137',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_8],
        "subscript": [
            {
                "identifier": 'EVENT_3794_action_queue_sync_137_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_3794_action_queue_sync_137_SUBSCRIPT_shift_northeast_pixels_1',
                "command": 'shift_northeast_pixels',
                "args": [2]
            },
            {
                "identifier": 'EVENT_3794_action_queue_sync_137_SUBSCRIPT_set_animation_speed_2',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.SLOW, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_3794_action_queue_sync_137_SUBSCRIPT_shift_southwest_pixels_3',
                "command": 'shift_southwest_pixels',
                "args": [2]
            },
            {
                "identifier": 'EVENT_3794_action_queue_sync_137_SUBSCRIPT_set_animation_speed_4',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_SLOW, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_3794_action_queue_sync_137_SUBSCRIPT_shift_z_down_pixels_5',
                "command": 'shift_z_down_pixels',
                "args": [4]
            }
        ]
    },
    {
        "identifier": 'EVENT_3794_action_queue_sync_138',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_5],
        "subscript": [
            {
                "identifier": 'EVENT_3794_action_queue_sync_138_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [10]
            },
            {
                "identifier": 'EVENT_3794_action_queue_sync_138_SUBSCRIPT_set_animation_speed_1',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_3794_action_queue_sync_138_SUBSCRIPT_shift_southwest_pixels_2',
                "command": 'shift_southwest_pixels',
                "args": [2]
            },
            {
                "identifier": 'EVENT_3794_action_queue_sync_138_SUBSCRIPT_set_animation_speed_3',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.SLOW, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_3794_action_queue_sync_138_SUBSCRIPT_shift_northeast_pixels_4',
                "command": 'shift_northeast_pixels',
                "args": [2]
            },
            {
                "identifier": 'EVENT_3794_action_queue_sync_138_SUBSCRIPT_set_animation_speed_5',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_SLOW, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_3794_action_queue_sync_138_SUBSCRIPT_shift_northeast_pixels_6',
                "command": 'shift_northeast_pixels',
                "args": [1]
            },
            {
                "identifier": 'EVENT_3794_action_queue_sync_138_SUBSCRIPT_shift_north_pixels_7',
                "command": 'shift_north_pixels',
                "args": [2]
            },
            {
                "identifier": 'EVENT_3794_action_queue_sync_138_SUBSCRIPT_set_sprite_sequence_8',
                "command": 'set_sprite_sequence',
                "args": [4, 0, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_3794_pause_139',
        "command": 'pause',
        "args": [55]
    },
    {
        "identifier": 'EVENT_3794_initiate_battle_mask_140',
        "command": 'initiate_battle_mask'
    },
    {
        "identifier": 'EVENT_3794_enter_area_141',
        "command": 'enter_area',
        "args": [Rooms._496_FACTORY_GROUNDS_FIGHT_WITH_SMITHY_USES_SLEDGE, RadialDirections.NORTHEAST, 4, 51, 0, [_0x68Flags.RUN_ENTRANCE_EVENT]]
    },
    {
        "identifier": 'EVENT_3794_ret_142',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_3794_set_bit_143',
        "command": 'set_bit',
        "args": [0x7043, 1]
    },
    {
        "identifier": 'EVENT_3794_unsync_action_script_144',
        "command": 'unsync_action_script',
        "args": [AreaObjects.NPC_8]
    },
    {
        "identifier": 'EVENT_3794_clear_bit_145',
        "command": 'clear_bit',
        "args": [0x7043, 1]
    },
    {
        "identifier": 'EVENT_3794_set_action_script_sync_146',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_8, 242]
    },
    {
        "identifier": 'EVENT_3794_ret_147',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_3794_set_bit_148',
        "command": 'set_bit',
        "args": [0x7043, 1]
    },
    {
        "identifier": 'EVENT_3794_clear_bit_149',
        "command": 'clear_bit',
        "args": [0x7043, 3]
    },
    {
        "identifier": 'EVENT_3794_unsync_action_script_150',
        "command": 'unsync_action_script',
        "args": [AreaObjects.NPC_8]
    },
    {
        "identifier": 'EVENT_3794_clear_bit_151',
        "command": 'clear_bit',
        "args": [0x7043, 1]
    },
    {
        "identifier": 'EVENT_3794_set_action_script_sync_152',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_8, 987]
    },
    {
        "identifier": 'EVENT_3794_ret_153',
        "command": 'ret'
    }
]
