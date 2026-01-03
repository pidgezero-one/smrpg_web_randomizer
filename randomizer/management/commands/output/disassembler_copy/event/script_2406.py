
from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data import items
script = [
    {
        "identifier": 'EVENT_2406_jmp_if_bit_set_0',
        "command": 'jmp_if_bit_set',
        "args": [0x708b, 5, 'EVENT_2406_ret_58']
    },
    {
        "identifier": 'EVENT_2406_set_bit_1',
        "command": 'set_bit',
        "args": [0x708b, 5]
    },
    {
        "identifier": 'EVENT_2406_remove_from_level_2',
        "command": 'remove_from_level',
        "args": [AreaObjects.NPC_9, Rooms._159_STAR_HILL_AREA_04]
    },
    {
        "identifier": 'EVENT_2406_fade_out_music_FDA3_3',
        "command": 'fade_out_music_FDA3'
    },
    {
        "identifier": 'EVENT_2406_action_queue_async_4',
        "command": 'action_queue_async',
        "args": [AreaObjects.SCREEN_FOCUS],
        "subscript": [
            {
                "identifier": 'EVENT_2406_action_queue_async_4_SUBSCRIPT_walk_to_xy_coords_0',
                "command": 'walk_to_xy_coords',
                "args": [23, 60]
            }
        ]
    },
    {
        "identifier": 'EVENT_2406_pause_5',
        "command": 'pause',
        "args": [16]
    },
    {
        "identifier": 'EVENT_2406_freeze_camera_6',
        "command": 'freeze_camera'
    },
    {
        "identifier": 'EVENT_2406_action_queue_async_7',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_2406_action_queue_async_7_SUBSCRIPT_floating_off_0',
                "command": 'floating_off'
            },
            {
                "identifier": 'EVENT_2406_action_queue_async_7_SUBSCRIPT_shadow_on_1',
                "command": 'shadow_on'
            },
            {
                "identifier": 'EVENT_2406_action_queue_async_7_SUBSCRIPT_overwrite_solidity_2',
                "command": 'overwrite_solidity',
                "args": [[]]
            },
            {
                "identifier": 'EVENT_2406_action_queue_async_7_SUBSCRIPT_walk_to_xy_coords_3',
                "command": 'walk_to_xy_coords',
                "args": [26, 77]
            },
            {
                "identifier": 'EVENT_2406_action_queue_async_7_SUBSCRIPT_face_northeast_4',
                "command": 'face_northeast'
            }
        ]
    },
    {
        "identifier": 'EVENT_2406_summon_to_current_level_at_marios_coords_8',
        "command": 'summon_to_current_level_at_marios_coords',
        "args": [AreaObjects.NPC_8]
    },
    {
        "identifier": 'EVENT_2406_pause_9',
        "command": 'pause',
        "args": [32]
    },
    {
        "identifier": 'EVENT_2406_action_queue_async_10',
        "command": 'action_queue_async',
        "args": [AreaObjects.SCREEN_FOCUS],
        "subscript": [
            {
                "identifier": 'EVENT_2406_action_queue_async_10_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.SLOW, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_2406_action_queue_async_10_SUBSCRIPT_shift_north_steps_1',
                "command": 'shift_north_steps',
                "args": [3]
            },
            {
                "identifier": 'EVENT_2406_action_queue_async_10_SUBSCRIPT_shift_north_pixels_2',
                "command": 'shift_north_pixels',
                "args": [8]
            },
            {
                "identifier": 'EVENT_2406_action_queue_async_10_SUBSCRIPT_pause_3',
                "command": 'pause',
                "args": [24]
            }
        ]
    },
    {
        "identifier": 'EVENT_2406_action_queue_sync_11',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_2406_action_queue_sync_11_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [112]
            },
            {
                "identifier": 'EVENT_2406_action_queue_sync_11_SUBSCRIPT_set_animation_speed_1',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FASTEST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_2406_action_queue_sync_11_SUBSCRIPT_set_sprite_sequence_2',
                "command": 'set_sprite_sequence',
                "args": [23, 2, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_2406_action_queue_sync_11_SUBSCRIPT_shift_west_pixels_3',
                "command": 'shift_west_pixels',
                "args": [2]
            }
        ]
    },
    {
        "identifier": 'EVENT_2406_play_music_default_volume_12',
        "command": 'play_music_default_volume',
        "args": [Music._23_GOT_A_STAR_PIECE_PART_1]
    },
    {
        "identifier": 'EVENT_2406_pause_13',
        "command": 'pause',
        "args": [68]
    },
    {
        "identifier": 'EVENT_2406_action_queue_async_14',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_9],
        "subscript": [
            {
                "identifier": 'EVENT_2406_action_queue_async_14_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_2406_action_queue_async_14_SUBSCRIPT_shift_z_up_pixels_1',
                "command": 'shift_z_up_pixels',
                "args": [80]
            },
            {
                "identifier": 'EVENT_2406_action_queue_async_14_SUBSCRIPT_pause_2',
                "command": 'pause',
                "args": [32]
            },
            {
                "identifier": 'EVENT_2406_action_queue_async_14_SUBSCRIPT_set_vram_priority_3',
                "command": 'set_vram_priority',
                "args": [VramPriority.OBJECT_OVERLAPS_MARIO_ON_ALL_SIDES]
            },
            {
                "identifier": 'EVENT_2406_action_queue_async_14_SUBSCRIPT_set_animation_speed_4',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_2406_action_queue_async_14_SUBSCRIPT_set_sprite_sequence_5',
                "command": 'set_sprite_sequence',
                "args": [0, 0, [_0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_2406_action_queue_async_14_SUBSCRIPT_pause_6',
                "command": 'pause',
                "args": [48]
            },
            {
                "identifier": 'EVENT_2406_action_queue_async_14_SUBSCRIPT_set_animation_speed_7',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FASTER, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_2406_action_queue_async_14_SUBSCRIPT_pause_8',
                "command": 'pause',
                "args": [48]
            },
            {
                "identifier": 'EVENT_2406_action_queue_async_14_SUBSCRIPT_set_animation_speed_9',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_2406_action_queue_async_14_SUBSCRIPT_pause_10',
                "command": 'pause',
                "args": [48]
            },
            {
                "identifier": 'EVENT_2406_action_queue_async_14_SUBSCRIPT_set_animation_speed_11',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FASTEST, [_0x10Flags.SEQUENCE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_2406_action_queue_async_15',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_8],
        "subscript": [
            {
                "identifier": 'EVENT_2406_action_queue_async_15_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_2406_action_queue_async_15_SUBSCRIPT_shift_z_up_pixels_1',
                "command": 'shift_z_up_pixels',
                "args": [80]
            }
        ]
    },
    {
        "identifier": 'EVENT_2406_pause_16',
        "command": 'pause',
        "args": [24]
    },
    {
        "identifier": 'EVENT_2406_set_action_script_sync_17',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_8, 394]
    },
    {
        "identifier": 'EVENT_2406_pause_18',
        "command": 'pause',
        "args": [1]
    },
    {
        "identifier": 'EVENT_2406_action_queue_sync_19',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_9],
        "subscript": [
            {
                "identifier": 'EVENT_2406_action_queue_sync_19_SUBSCRIPT_set_object_memory_bits_0',
                "command": 'set_object_memory_bits',
                "args": [0x0e, [0]]
            }
        ]
    },
    {
        "identifier": 'EVENT_2406_pause_short_20',
        "command": 'pause_short',
        "args": [544]
    },
    {
        "identifier": 'EVENT_2406_action_queue_async_21',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_2406_action_queue_async_21_SUBSCRIPT_shift_west_pixels_0',
                "command": 'shift_west_pixels',
                "args": [1]
            },
            {
                "identifier": 'EVENT_2406_action_queue_async_21_SUBSCRIPT_set_sprite_sequence_1',
                "command": 'set_sprite_sequence',
                "args": [12, 0, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_2406_action_queue_async_21_SUBSCRIPT_face_south_2',
                "command": 'face_south'
            }
        ]
    },
    {
        "identifier": 'EVENT_2406_pause_22',
        "command": 'pause',
        "args": [32]
    },
    {
        "identifier": 'EVENT_2406_action_queue_async_23',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_9],
        "subscript": [
            {
                "identifier": 'EVENT_2406_action_queue_async_23_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [16]
            },
            {
                "identifier": 'EVENT_2406_action_queue_async_23_SUBSCRIPT_set_animation_speed_1',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_2406_action_queue_async_23_SUBSCRIPT_pause_2',
                "command": 'pause',
                "args": [48]
            },
            {
                "identifier": 'EVENT_2406_action_queue_async_23_SUBSCRIPT_set_animation_speed_3',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FASTER, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_2406_action_queue_async_23_SUBSCRIPT_pause_4',
                "command": 'pause',
                "args": [48]
            },
            {
                "identifier": 'EVENT_2406_action_queue_async_23_SUBSCRIPT_set_animation_speed_5',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_2406_action_queue_async_23_SUBSCRIPT_pause_6',
                "command": 'pause',
                "args": [48]
            },
            {
                "identifier": 'EVENT_2406_action_queue_async_23_SUBSCRIPT_set_animation_speed_7',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_2406_action_queue_async_23_SUBSCRIPT_pause_8',
                "command": 'pause',
                "args": [68]
            },
            {
                "identifier": 'EVENT_2406_action_queue_async_23_SUBSCRIPT_set_sprite_sequence_9',
                "command": 'set_sprite_sequence',
                "args": [2, 0, [_0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_2406_action_queue_async_23_SUBSCRIPT_pause_10',
                "command": 'pause',
                "args": [96]
            },
            {
                "identifier": 'EVENT_2406_action_queue_async_23_SUBSCRIPT_set_animation_speed_11',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_2406_action_queue_async_23_SUBSCRIPT_pause_12',
                "command": 'pause',
                "args": [8]
            },
            {
                "identifier": 'EVENT_2406_action_queue_async_23_SUBSCRIPT_set_animation_speed_13',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_2406_action_queue_async_23_SUBSCRIPT_set_sprite_sequence_14',
                "command": 'set_sprite_sequence',
                "args": [0, 0, [_0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_2406_action_queue_async_23_SUBSCRIPT_pause_15',
                "command": 'pause',
                "args": [10]
            },
            {
                "identifier": 'EVENT_2406_action_queue_async_23_SUBSCRIPT_set_animation_speed_16',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FASTER, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_2406_action_queue_async_23_SUBSCRIPT_pause_17',
                "command": 'pause',
                "args": [10]
            },
            {
                "identifier": 'EVENT_2406_action_queue_async_23_SUBSCRIPT_set_animation_speed_18',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_2406_action_queue_async_23_SUBSCRIPT_pause_19',
                "command": 'pause',
                "args": [10]
            },
            {
                "identifier": 'EVENT_2406_action_queue_async_23_SUBSCRIPT_set_animation_speed_20',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FASTEST, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_2406_action_queue_async_23_SUBSCRIPT_pause_21',
                "command": 'pause',
                "args": [56]
            }
        ]
    },
    {
        "identifier": 'EVENT_2406_play_music_default_volume_24',
        "command": 'play_music_default_volume',
        "args": [Music._24_GOT_A_STAR_PIECE_PART_2]
    },
    {
        "identifier": 'EVENT_2406_pause_25',
        "command": 'pause',
        "args": [48]
    },
    {
        "identifier": 'EVENT_2406_action_queue_sync_26',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_9],
        "subscript": [
            {
                "identifier": 'EVENT_2406_action_queue_sync_26_SUBSCRIPT_set_vram_priority_0',
                "command": 'set_vram_priority',
                "args": [VramPriority.OBJECT_OVERLAPS_MARIO_ON_ALL_SIDES]
            },
            {
                "identifier": 'EVENT_2406_action_queue_sync_26_SUBSCRIPT_set_animation_speed_1',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_2406_action_queue_sync_26_SUBSCRIPT_shift_z_down_pixels_2',
                "command": 'shift_z_down_pixels',
                "args": [64]
            },
            {
                "identifier": 'EVENT_2406_action_queue_sync_26_SUBSCRIPT_set_sprite_sequence_3',
                "command": 'set_sprite_sequence',
                "args": [2, 0, [_0x08Flags.READ_AS_SEQUENCE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_2406_action_queue_sync_27',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_2406_action_queue_sync_27_SUBSCRIPT_set_sprite_sequence_0',
                "command": 'set_sprite_sequence',
                "args": [5, 0, [_0x08Flags.READ_AS_SEQUENCE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_2406_pause_short_28',
        "command": 'pause_short',
        "args": [464]
    },
    {
        "identifier": 'EVENT_2406_action_queue_sync_29',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_9],
        "subscript": [
            {
                "identifier": 'EVENT_2406_action_queue_sync_29_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_2406_action_queue_sync_29_SUBSCRIPT_shift_z_up_pixels_1',
                "command": 'shift_z_up_pixels',
                "args": [32]
            },
            {
                "identifier": 'EVENT_2406_action_queue_sync_29_SUBSCRIPT_pause_2',
                "command": 'pause',
                "args": [48]
            },
            {
                "identifier": 'EVENT_2406_action_queue_sync_29_SUBSCRIPT_set_animation_speed_3',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FASTEST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_2406_action_queue_sync_29_SUBSCRIPT_shift_z_up_steps_4',
                "command": 'shift_z_up_steps',
                "args": [16]
            }
        ]
    },
    {
        "identifier": 'EVENT_2406_action_queue_sync_30',
        "command": 'action_queue_sync',
        "args": [AreaObjects.SCREEN_FOCUS],
        "subscript": [
            {
                "identifier": 'EVENT_2406_action_queue_sync_30_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [67]
            },
            {
                "identifier": 'EVENT_2406_action_queue_sync_30_SUBSCRIPT_set_animation_speed_1',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_2406_action_queue_sync_30_SUBSCRIPT_shift_z_up_steps_2',
                "command": 'shift_z_up_steps',
                "args": [6]
            }
        ]
    },
    {
        "identifier": 'EVENT_2406_pause_31',
        "command": 'pause',
        "args": [73]
    },
    {
        "identifier": 'EVENT_2406_fade_out_to_black_async_duration_32',
        "command": 'fade_out_to_black_async_duration',
        "args": [32]
    },
    {
        "identifier": 'EVENT_2406_run_star_piece_sequence_33',
        "command": 'run_star_piece_sequence',
        "args": [4]
    },
    {
        "identifier": 'EVENT_2406_action_queue_async_34',
        "command": 'action_queue_async',
        "args": [AreaObjects.SCREEN_FOCUS],
        "subscript": [
            {
                "identifier": 'EVENT_2406_action_queue_async_34_SUBSCRIPT_shift_z_down_steps_0',
                "command": 'shift_z_down_steps',
                "args": [4]
            },
            {
                "identifier": 'EVENT_2406_action_queue_async_34_SUBSCRIPT_shift_south_steps_1',
                "command": 'shift_south_steps',
                "args": [5]
            }
        ]
    },
    {
        "identifier": 'EVENT_2406_set_action_script_async_35',
        "command": 'set_action_script_async',
        "args": [AreaObjects.MARIO, 395]
    },
    {
        "identifier": 'EVENT_2406_fade_in_from_black_async_36',
        "command": 'fade_in_from_black_async'
    },
    {
        "identifier": 'EVENT_2406_pause_37',
        "command": 'pause',
        "args": [16]
    },
    {
        "identifier": 'EVENT_2406_set_bit_7_offset_38',
        "command": 'set_bit_7_offset',
        "args": [0x0158, []]
    },
    {
        "identifier": 'EVENT_2406_set_bit_7_offset_39',
        "command": 'set_bit_7_offset',
        "args": [0x015a, []]
    },
    {
        "identifier": 'EVENT_2406_set_bit_7_offset_40',
        "command": 'set_bit_7_offset',
        "args": [0x015c, []]
    },
    {
        "identifier": 'EVENT_2406_db_41',
        "command": 'db',
        "args": [0xfd, 0x8e, 0x80, 0x07, 0x01]
    },
    {
        "identifier": 'EVENT_2406_pause_script_until_effect_done_42',
        "command": 'pause_script_until_effect_done'
    },
    {
        "identifier": 'EVENT_2406_run_dialog_43',
        "command": 'run_dialog',
        "args": [3442, AreaObjects.BOWSER, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_2406_pause_44',
        "command": 'pause',
        "args": [32]
    },
    {
        "identifier": 'EVENT_2406_set_action_script_sync_45',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.MARIO, 385]
    },
    {
        "identifier": 'EVENT_2406_pause_46',
        "command": 'pause',
        "args": [52]
    },
    {
        "identifier": 'EVENT_2406_play_sound_47',
        "command": 'play_sound',
        "args": [Sounds._013_COIN, 6]
    },
    {
        "identifier": 'EVENT_2406_pause_48',
        "command": 'pause',
        "args": [16]
    },
    {
        "identifier": 'EVENT_2406_db_49',
        "command": 'db',
        "args": [0xfd, 0x8e, 0xb2, 0x07, 0x01]
    },
    {
        "identifier": 'EVENT_2406_pause_script_until_effect_done_50',
        "command": 'pause_script_until_effect_done'
    },
    {
        "identifier": 'EVENT_2406_clear_bit_7_offset_51',
        "command": 'clear_bit_7_offset',
        "args": [0x0158, []]
    },
    {
        "identifier": 'EVENT_2406_clear_bit_7_offset_52',
        "command": 'clear_bit_7_offset',
        "args": [0x015a, []]
    },
    {
        "identifier": 'EVENT_2406_clear_bit_7_offset_53',
        "command": 'clear_bit_7_offset',
        "args": [0x015c, []]
    },
    {
        "identifier": 'EVENT_2406_set_action_script_sync_54',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.MARIO, 395]
    },
    {
        "identifier": 'EVENT_2406_pause_55',
        "command": 'pause',
        "args": [16]
    },
    {
        "identifier": 'EVENT_2406_play_music_default_volume_56',
        "command": 'play_music_default_volume',
        "args": [Music._34_STAR_HILL]
    },
    {
        "identifier": 'EVENT_2406_unfreeze_camera_57',
        "command": 'unfreeze_camera'
    },
    {
        "identifier": 'EVENT_2406_ret_58',
        "command": 'ret'
    }
]
