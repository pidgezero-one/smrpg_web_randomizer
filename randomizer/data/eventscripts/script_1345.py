from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
script = [
    {
        "identifier": 'EVENT_1345_jmp_if_bit_set_0',
        "command": 'jmp_if_bit_set',
        "args": [0x7054, 1, 'EVENT_1345_ret_32'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1345_fade_out_music_to_volume_1',
        "command": 'fade_out_music_to_volume',
        "args": [0, 0],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1345_pause_2',
        "command": 'pause',
        "args": [30],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1345_play_sound_3',
        "command": 'play_sound',
        "args": [Sounds._076_BOOSTERS_TRAIN_HORN, 6],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1345_pause_4',
        "command": 'pause',
        "args": [60],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1345_run_dialog_5',
        "command": 'run_dialog',
        "args": [2568, AreaObjects.NPC_12, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1345_pause_6',
        "command": 'pause',
        "args": [1],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1345_freeze_camera_7',
        "command": 'freeze_camera',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1345_action_queue_sync_8',
        "command": 'action_queue_sync',
        "args": [AreaObjects.SCREEN_FOCUS],
        "subscript": [
            {
                "identifier": 'EVENT_1345_action_queue_sync_8_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING, _0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_1345_action_queue_sync_8_SUBSCRIPT_shift_north_steps_1',
                "command": 'shift_north_steps',
                "args": [2]
            }
        ]
    },
    {
        "identifier": 'EVENT_1345_action_queue_async_9',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_1345_action_queue_async_9_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING, _0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_1345_action_queue_async_9_SUBSCRIPT_walk_to_xy_coords_1',
                "command": 'walk_to_xy_coords',
                "args": [3, 113]
            },
            {
                "identifier": 'EVENT_1345_action_queue_async_9_SUBSCRIPT_face_north_2',
                "command": 'face_north',
                "args": []
            }
        ]
    },
    {
        "identifier": 'EVENT_1345_play_sound_10',
        "command": 'play_sound',
        "args": [Sounds._074_BOOSTERS_TRAIN, 6],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1345_action_queue_sync_11',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_0],
        "subscript": [
            {
                "identifier": 'EVENT_1345_action_queue_sync_11_SUBSCRIPT_shadow_off_0',
                "command": 'shadow_off',
                "args": []
            },
            {
                "identifier": 'EVENT_1345_action_queue_sync_11_SUBSCRIPT_set_animation_speed_1',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_1345_action_queue_sync_11_SUBSCRIPT_clear_solidity_bits_2',
                "command": 'clear_solidity_bits',
                "args": [[_0x0AFlags.CANT_PASS_WALLS]]
            },
            {
                "identifier": 'EVENT_1345_action_queue_sync_11_SUBSCRIPT_transfer_to_xyzf_3',
                "command": 'transfer_to_xyzf',
                "args": [1, 104, 8, RadialDirections.EAST]
            },
            {
                "identifier": 'EVENT_1345_action_queue_sync_11_SUBSCRIPT_shift_northwest_steps_4',
                "command": 'shift_northwest_steps',
                "args": [2]
            },
            {
                "identifier": 'EVENT_1345_action_queue_sync_11_SUBSCRIPT_shift_northwest_pixels_5',
                "command": 'shift_northwest_pixels',
                "args": [5]
            },
            {
                "identifier": 'EVENT_1345_action_queue_sync_11_SUBSCRIPT_shift_southwest_pixels_6',
                "command": 'shift_southwest_pixels',
                "args": [3]
            },
            {
                "identifier": 'EVENT_1345_action_queue_sync_11_SUBSCRIPT_reset_properties_7',
                "command": 'reset_properties',
                "args": []
            },
            {
                "identifier": 'EVENT_1345_action_queue_sync_11_SUBSCRIPT_face_southwest_8',
                "command": 'face_southwest',
                "args": []
            },
            {
                "identifier": 'EVENT_1345_action_queue_sync_11_SUBSCRIPT_fixed_f_coord_on_9',
                "command": 'fixed_f_coord_on',
                "args": []
            },
            {
                "identifier": 'EVENT_1345_action_queue_sync_11_SUBSCRIPT_set_sprite_sequence_10',
                "command": 'set_sprite_sequence',
                "args": [15, inc_sprite=0, flags=[_0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_1345_action_queue_sync_11_SUBSCRIPT_sequence_playback_off_11',
                "command": 'sequence_playback_off',
                "args": []
            },
            {
                "identifier": 'EVENT_1345_action_queue_sync_11_SUBSCRIPT_visibility_on_12',
                "command": 'visibility_on',
                "args": []
            }
        ]
    },
    {
        "identifier": 'EVENT_1345_action_queue_async_12',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_1],
        "subscript": [
            {
                "identifier": 'EVENT_1345_action_queue_async_12_SUBSCRIPT_shadow_off_0',
                "command": 'shadow_off',
                "args": []
            },
            {
                "identifier": 'EVENT_1345_action_queue_async_12_SUBSCRIPT_set_animation_speed_1',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_1345_action_queue_async_12_SUBSCRIPT_clear_solidity_bits_2',
                "command": 'clear_solidity_bits',
                "args": [[_0x0AFlags.CANT_PASS_WALLS]]
            },
            {
                "identifier": 'EVENT_1345_action_queue_async_12_SUBSCRIPT_transfer_to_xyzf_3',
                "command": 'transfer_to_xyzf',
                "args": [1, 104, 8, RadialDirections.EAST]
            },
            {
                "identifier": 'EVENT_1345_action_queue_async_12_SUBSCRIPT_set_vram_priority_4',
                "command": 'set_vram_priority',
                "args": [VramPriority.MARIO_OVERLAPS_ON_ALL_SIDES]
            },
            {
                "identifier": 'EVENT_1345_action_queue_async_12_SUBSCRIPT_set_priority_5',
                "command": 'set_priority',
                "args": [3]
            },
            {
                "identifier": 'EVENT_1345_action_queue_async_12_SUBSCRIPT_shift_northwest_steps_6',
                "command": 'shift_northwest_steps',
                "args": [1]
            },
            {
                "identifier": 'EVENT_1345_action_queue_async_12_SUBSCRIPT_shift_southwest_pixels_7',
                "command": 'shift_southwest_pixels',
                "args": [6]
            },
            {
                "identifier": 'EVENT_1345_action_queue_async_12_SUBSCRIPT_face_southeast_8',
                "command": 'face_southeast',
                "args": []
            },
            {
                "identifier": 'EVENT_1345_action_queue_async_12_SUBSCRIPT_set_sprite_sequence_9',
                "command": 'set_sprite_sequence',
                "args": [0, inc_sprite=0, flags=[_0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_1345_action_queue_async_12_SUBSCRIPT_visibility_on_10',
                "command": 'visibility_on',
                "args": []
            }
        ]
    },
    {
        "identifier": 'EVENT_1345_action_queue_sync_13',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_0],
        "subscript": [
            {
                "identifier": 'EVENT_1345_action_queue_sync_13_SUBSCRIPT_clear_solidity_bits_0',
                "command": 'clear_solidity_bits',
                "args": [[_0x0AFlags.CANT_PASS_WALLS]]
            },
            {
                "identifier": 'EVENT_1345_action_queue_sync_13_SUBSCRIPT_set_animation_speed_1',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.SLOW, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_1345_action_queue_sync_13_SUBSCRIPT_shift_southeast_steps_2',
                "command": 'shift_southeast_steps',
                "args": [7]
            },
            {
                "identifier": 'EVENT_1345_action_queue_sync_13_SUBSCRIPT_set_vram_priority_3',
                "command": 'set_vram_priority',
                "args": [VramPriority.OBJECT_OVERLAPS_MARIO_ON_ALL_SIDES]
            },
            {
                "identifier": 'EVENT_1345_action_queue_sync_13_SUBSCRIPT_shift_southeast_steps_4',
                "command": 'shift_southeast_steps',
                "args": [1]
            }
        ]
    },
    {
        "identifier": 'EVENT_1345_action_queue_async_14',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_1],
        "subscript": [
            {
                "identifier": 'EVENT_1345_action_queue_async_14_SUBSCRIPT_clear_solidity_bits_0',
                "command": 'clear_solidity_bits',
                "args": [[_0x0AFlags.CANT_PASS_WALLS]]
            },
            {
                "identifier": 'EVENT_1345_action_queue_async_14_SUBSCRIPT_set_animation_speed_1',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.SLOW, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_1345_action_queue_async_14_SUBSCRIPT_shift_southeast_steps_2',
                "command": 'shift_southeast_steps',
                "args": [7]
            },
            {
                "identifier": 'EVENT_1345_action_queue_async_14_SUBSCRIPT_object_memory_modify_bits_3',
                "command": 'object_memory_modify_bits',
                "args": [0x09, [5], [4, 6]]
            },
            {
                "identifier": 'EVENT_1345_action_queue_async_14_SUBSCRIPT_set_vram_priority_4',
                "command": 'set_vram_priority',
                "args": [VramPriority.NORMAL]
            },
            {
                "identifier": 'EVENT_1345_action_queue_async_14_SUBSCRIPT_shift_southeast_steps_5',
                "command": 'shift_southeast_steps',
                "args": [1]
            }
        ]
    },
    {
        "identifier": 'EVENT_1345_action_queue_sync_15',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_1345_action_queue_sync_15_SUBSCRIPT_face_northeast_0',
                "command": 'face_northeast',
                "args": []
            },
            {
                "identifier": 'EVENT_1345_action_queue_sync_15_SUBSCRIPT_set_animation_speed_1',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING, _0x10Flags.SEQUENCE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_1345_action_queue_sync_16',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_0],
        "subscript": [
            {
                "identifier": 'EVENT_1345_action_queue_sync_16_SUBSCRIPT_shift_southeast_steps_0',
                "command": 'shift_southeast_steps',
                "args": [1]
            },
            {
                "identifier": 'EVENT_1345_action_queue_sync_16_SUBSCRIPT_set_animation_speed_1',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_SLOW, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_1345_action_queue_sync_16_SUBSCRIPT_shift_southeast_steps_2',
                "command": 'shift_southeast_steps',
                "args": [1]
            }
        ]
    },
    {
        "identifier": 'EVENT_1345_action_queue_async_17',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_1],
        "subscript": [
            {
                "identifier": 'EVENT_1345_action_queue_async_17_SUBSCRIPT_shift_southeast_steps_0',
                "command": 'shift_southeast_steps',
                "args": [1]
            },
            {
                "identifier": 'EVENT_1345_action_queue_async_17_SUBSCRIPT_set_animation_speed_1',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_SLOW, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_1345_action_queue_async_17_SUBSCRIPT_set_animation_speed_2',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.SLOW, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_1345_action_queue_async_17_SUBSCRIPT_shift_southeast_pixels_3',
                "command": 'shift_southeast_pixels',
                "args": [8]
            },
            {
                "identifier": 'EVENT_1345_action_queue_async_17_SUBSCRIPT_set_animation_speed_4',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_SLOW, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_1345_action_queue_async_17_SUBSCRIPT_shift_southeast_pixels_5',
                "command": 'shift_southeast_pixels',
                "args": [8]
            },
            {
                "identifier": 'EVENT_1345_action_queue_async_17_SUBSCRIPT_reset_properties_6',
                "command": 'reset_properties',
                "args": []
            },
            {
                "identifier": 'EVENT_1345_action_queue_async_17_SUBSCRIPT_face_southwest_7',
                "command": 'face_southwest',
                "args": []
            }
        ]
    },
    {
        "identifier": 'EVENT_1345_play_sound_18',
        "command": 'play_sound',
        "args": [Sounds._000_SILENCE, 6],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1345_pause_19',
        "command": 'pause',
        "args": [80],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1345_run_dialog_20',
        "command": 'run_dialog',
        "args": [2569, AreaObjects.NPC_12, [_0x60Flags.CLOSABLE, _0x60Flags.MULTILINE]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1345_pause_script_resume_on_next_dialog_page_a_21',
        "command": 'pause_script_resume_on_next_dialog_page_a',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1345_action_queue_async_22',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_0],
        "subscript": [
            {
                "identifier": 'EVENT_1345_action_queue_async_22_SUBSCRIPT_reset_properties_0',
                "command": 'reset_properties',
                "args": []
            }
        ]
    },
    {
        "identifier": 'EVENT_1345_pause_script_resume_on_next_dialog_page_a_23',
        "command": 'pause_script_resume_on_next_dialog_page_a',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1345_pause_script_resume_on_next_dialog_page_a_24',
        "command": 'pause_script_resume_on_next_dialog_page_a',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1345_unsync_dialog_25',
        "command": 'unsync_dialog',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1345_close_dialog_26',
        "command": 'close_dialog',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1345_play_music_default_volume_27',
        "command": 'play_music_default_volume',
        "args": [Music._32_AND_MY_NAMES_BOOSTER],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1345_set_action_script_sync_28',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_0, 525],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1345_set_action_script_sync_29',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_1, 526],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1345_unfreeze_camera_30',
        "command": 'unfreeze_camera',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1345_set_bit_31',
        "command": 'set_bit',
        "args": [0x7054, 1],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1345_ret_32',
        "command": 'ret',
        "args": [],
        "subscript": []
    }
]
