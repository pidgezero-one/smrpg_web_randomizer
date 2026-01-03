
from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data import items
script = [
    {
        "identifier": 'EVENT_1342_pause_action_script_0',
        "command": 'pause_action_script',
        "args": [AreaObjects.NPC_0]
    },
    {
        "identifier": 'EVENT_1342_action_queue_sync_1',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_0],
        "subscript": [
            {
                "identifier": 'EVENT_1342_action_queue_sync_1_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_1342_action_queue_sync_1_SUBSCRIPT_set_sprite_sequence_1',
                "command": 'set_sprite_sequence',
                "args": [3, 0, [_0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_1342_action_queue_sync_1_SUBSCRIPT_play_sound_2',
                "command": 'play_sound',
                "args": [Sounds._160_CHOMP, 6]
            }
        ]
    },
    {
        "identifier": 'EVENT_1342_action_queue_async_2',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_1342_action_queue_async_2_SUBSCRIPT_clear_solidity_bits_0',
                "command": 'clear_solidity_bits',
                "args": [[_0x0AFlags.BIT_4, _0x0AFlags.CANT_PASS_NPCS, _0x0AFlags.CANT_WALK_THROUGH, _0x0AFlags.BIT_7]]
            },
            {
                "identifier": 'EVENT_1342_action_queue_async_2_SUBSCRIPT_face_northwest_1',
                "command": 'face_northwest'
            },
            {
                "identifier": 'EVENT_1342_action_queue_async_2_SUBSCRIPT_fixed_f_coord_on_2',
                "command": 'fixed_f_coord_on'
            },
            {
                "identifier": 'EVENT_1342_action_queue_async_2_SUBSCRIPT_set_animation_speed_3',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FASTER, [_0x10Flags.WALKING, _0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_1342_action_queue_async_2_SUBSCRIPT_jump_to_height_4',
                "command": 'jump_to_height',
                "args": [128]
            },
            {
                "identifier": 'EVENT_1342_action_queue_async_2_SUBSCRIPT_bounce_to_xy_with_height_5',
                "command": 'bounce_to_xy_with_height',
                "args": [25, 123, 4]
            },
            {
                "identifier": 'EVENT_1342_action_queue_async_2_SUBSCRIPT_fixed_f_coord_off_6',
                "command": 'fixed_f_coord_off'
            },
            {
                "identifier": 'EVENT_1342_action_queue_async_2_SUBSCRIPT_set_animation_speed_7',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_1342_action_queue_async_2_SUBSCRIPT_set_solidity_bits_8',
                "command": 'set_solidity_bits',
                "args": [[_0x0AFlags.BIT_4, _0x0AFlags.CANT_PASS_NPCS, _0x0AFlags.CANT_WALK_THROUGH, _0x0AFlags.BIT_7]]
            }
        ]
    },
    {
        "identifier": 'EVENT_1342_pause_3',
        "command": 'pause',
        "args": [80]
    },
    {
        "identifier": 'EVENT_1342_action_queue_async_4',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_1],
        "subscript": [
            {
                "identifier": 'EVENT_1342_action_queue_async_4_SUBSCRIPT_transfer_to_xyzf_0',
                "command": 'transfer_to_xyzf',
                "args": [26, 124, 4, RadialDirections.EAST]
            },
            {
                "identifier": 'EVENT_1342_action_queue_async_4_SUBSCRIPT_face_northwest_1',
                "command": 'face_northwest'
            },
            {
                "identifier": 'EVENT_1342_action_queue_async_4_SUBSCRIPT_visibility_on_2',
                "command": 'visibility_on'
            },
            {
                "identifier": 'EVENT_1342_action_queue_async_4_SUBSCRIPT_fixed_f_coord_on_3',
                "command": 'fixed_f_coord_on'
            },
            {
                "identifier": 'EVENT_1342_action_queue_async_4_SUBSCRIPT_shift_southwest_steps_4',
                "command": 'shift_southwest_steps',
                "args": [1]
            }
        ]
    },
    {
        "identifier": 'EVENT_1342_pause_5',
        "command": 'pause',
        "args": [30]
    },
    {
        "identifier": 'EVENT_1342_stop_sound_6',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_1342_action_queue_async_7',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_0],
        "subscript": [
            {
                "identifier": 'EVENT_1342_action_queue_async_7_SUBSCRIPT_set_sprite_sequence_0',
                "command": 'set_sprite_sequence',
                "args": [0, 0, [_0x08Flags.READ_AS_MOLD, _0x08Flags.MIRROR_SPRITE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_1342_pause_8',
        "command": 'pause',
        "args": [100]
    },
    {
        "identifier": 'EVENT_1342_run_dialog_9',
        "command": 'run_dialog',
        "args": [2768, AreaObjects.BOWSER, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC]]
    },
    {
        "identifier": 'EVENT_1342_pause_10',
        "command": 'pause',
        "args": [15]
    },
    {
        "identifier": 'EVENT_1342_action_queue_async_11',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_1],
        "subscript": [
            {
                "identifier": 'EVENT_1342_action_queue_async_11_SUBSCRIPT_fixed_f_coord_off_0',
                "command": 'fixed_f_coord_off'
            },
            {
                "identifier": 'EVENT_1342_action_queue_async_11_SUBSCRIPT_set_animation_speed_1',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_1342_action_queue_async_11_SUBSCRIPT_shift_northwest_steps_2',
                "command": 'shift_northwest_steps',
                "args": [1]
            },
            {
                "identifier": 'EVENT_1342_action_queue_async_11_SUBSCRIPT_jump_to_height_3',
                "command": 'jump_to_height',
                "args": [144]
            },
            {
                "identifier": 'EVENT_1342_action_queue_async_11_SUBSCRIPT_bounce_to_xy_with_height_4',
                "command": 'bounce_to_xy_with_height',
                "args": [23, 119, 8]
            },
            {
                "identifier": 'EVENT_1342_action_queue_async_11_SUBSCRIPT_face_southwest_5',
                "command": 'face_southwest'
            }
        ]
    },
    {
        "identifier": 'EVENT_1342_action_queue_async_12',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_0],
        "subscript": [
            {
                "identifier": 'EVENT_1342_action_queue_async_12_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.SLOW, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_1342_action_queue_async_12_SUBSCRIPT_set_sprite_sequence_1',
                "command": 'set_sprite_sequence',
                "args": [2, 0, [_0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_1342_pause_13',
        "command": 'pause',
        "args": [120]
    },
    {
        "identifier": 'EVENT_1342_freeze_camera_14',
        "command": 'freeze_camera'
    },
    {
        "identifier": 'EVENT_1342_action_queue_async_15',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_1],
        "subscript": [
            {
                "identifier": 'EVENT_1342_action_queue_async_15_SUBSCRIPT_face_southeast_0',
                "command": 'face_southeast'
            }
        ]
    },
    {
        "identifier": 'EVENT_1342_run_dialog_16',
        "command": 'run_dialog',
        "args": [2769, AreaObjects.NPC_14, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_1342_pause_17',
        "command": 'pause',
        "args": [15]
    },
    {
        "identifier": 'EVENT_1342_action_queue_sync_18',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_1342_action_queue_sync_18_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING, _0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_1342_action_queue_sync_18_SUBSCRIPT_shift_southeast_steps_1',
                "command": 'shift_southeast_steps',
                "args": [1]
            },
            {
                "identifier": 'EVENT_1342_action_queue_sync_18_SUBSCRIPT_face_east_2',
                "command": 'face_east'
            }
        ]
    },
    {
        "identifier": 'EVENT_1342_action_queue_async_19',
        "command": 'action_queue_async',
        "args": [AreaObjects.SCREEN_FOCUS],
        "subscript": [
            {
                "identifier": 'EVENT_1342_action_queue_async_19_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_1342_action_queue_async_19_SUBSCRIPT_shift_east_steps_1',
                "command": 'shift_east_steps',
                "args": [4]
            },
            {
                "identifier": 'EVENT_1342_action_queue_async_19_SUBSCRIPT_pause_2',
                "command": 'pause',
                "args": [20]
            }
        ]
    },
    {
        "identifier": 'EVENT_1342_remove_from_current_level_20',
        "command": 'remove_from_current_level',
        "args": [AreaObjects.NPC_0]
    },
    {
        "identifier": 'EVENT_1342_remove_from_level_21',
        "command": 'remove_from_level',
        "args": [AreaObjects.NPC_0, Rooms._200_BOOSTER_TOWER_6F_AREA_03_ELDERS_ROOM_WCHOMP]
    },
    {
        "identifier": 'EVENT_1342_action_queue_async_22',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_2],
        "subscript": [
            {
                "identifier": 'EVENT_1342_action_queue_async_22_SUBSCRIPT_transfer_to_xyzf_0',
                "command": 'transfer_to_xyzf',
                "args": [23, 120, 10, RadialDirections.EAST]
            },
            {
                "identifier": 'EVENT_1342_action_queue_async_22_SUBSCRIPT_shift_southwest_pixels_1',
                "command": 'shift_southwest_pixels',
                "args": [18]
            },
            {
                "identifier": 'EVENT_1342_action_queue_async_22_SUBSCRIPT_shift_southeast_pixels_2',
                "command": 'shift_southeast_pixels',
                "args": [2]
            }
        ]
    },
    {
        "identifier": 'EVENT_1342_run_dialog_23',
        "command": 'run_dialog',
        "args": [2816, AreaObjects.NPC_14, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_1342_action_queue_sync_24',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_1],
        "subscript": [
            {
                "identifier": 'EVENT_1342_action_queue_sync_24_SUBSCRIPT_shift_southeast_pixels_0',
                "command": 'shift_southeast_pixels',
                "args": [8]
            },
            {
                "identifier": 'EVENT_1342_action_queue_sync_24_SUBSCRIPT_shift_southwest_pixels_1',
                "command": 'shift_southwest_pixels',
                "args": [8]
            },
            {
                "identifier": 'EVENT_1342_action_queue_sync_24_SUBSCRIPT_face_southeast_2',
                "command": 'face_southeast'
            }
        ]
    },
    {
        "identifier": 'EVENT_1342_action_queue_sync_25',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_1342_action_queue_sync_25_SUBSCRIPT_face_northwest_0',
                "command": 'face_northwest'
            },
            {
                "identifier": 'EVENT_1342_action_queue_sync_25_SUBSCRIPT_set_animation_speed_1',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING, _0x10Flags.SEQUENCE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_1342_action_queue_async_26',
        "command": 'action_queue_async',
        "args": [AreaObjects.SCREEN_FOCUS],
        "subscript": [
            {
                "identifier": 'EVENT_1342_action_queue_async_26_SUBSCRIPT_shift_west_steps_0',
                "command": 'shift_west_steps',
                "args": [4]
            }
        ]
    },
    {
        "identifier": 'EVENT_1342_run_dialog_27',
        "command": 'run_dialog',
        "args": [2817, AreaObjects.NPC_14, [_0x60Flags.CLOSABLE, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_1342_pause_script_resume_on_next_dialog_page_a_FD61_28',
        "command": 'pause_script_resume_on_next_dialog_page_a_FD61'
    },
    {
        "identifier": 'EVENT_1342_play_sound_29',
        "command": 'play_sound',
        "args": [Sounds._104_DEEP_SCRAPING, 6]
    },
    {
        "identifier": 'EVENT_1342_action_queue_sync_30',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_1],
        "subscript": [
            {
                "identifier": 'EVENT_1342_action_queue_sync_30_SUBSCRIPT_set_sprite_sequence_0',
                "command": 'set_sprite_sequence',
                "args": [12, 3, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_1342_action_queue_async_31',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_2],
        "subscript": [
            {
                "identifier": 'EVENT_1342_action_queue_async_31_SUBSCRIPT_visibility_on_0',
                "command": 'visibility_on'
            },
            {
                "identifier": 'EVENT_1342_action_queue_async_31_SUBSCRIPT_set_sprite_sequence_1',
                "command": 'set_sprite_sequence',
                "args": [0, 0, [_0x08Flags.READ_AS_SEQUENCE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_1342_unsync_dialog_32',
        "command": 'unsync_dialog'
    },
    {
        "identifier": 'EVENT_1342_close_dialog_33',
        "command": 'close_dialog'
    },
    {
        "identifier": 'EVENT_1342_pause_34',
        "command": 'pause',
        "args": [30]
    },
    {
        "identifier": 'EVENT_1342_stop_sound_35',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_1342_remove_from_current_level_36',
        "command": 'remove_from_current_level',
        "args": [AreaObjects.NPC_2]
    },
    {
        "identifier": 'EVENT_1342_action_queue_async_37',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_1],
        "subscript": [
            {
                "identifier": 'EVENT_1342_action_queue_async_37_SUBSCRIPT_reset_properties_0',
                "command": 'reset_properties'
            },
            {
                "identifier": 'EVENT_1342_action_queue_async_37_SUBSCRIPT_pause_1',
                "command": 'pause',
                "args": [30]
            },
            {
                "identifier": 'EVENT_1342_action_queue_async_37_SUBSCRIPT_set_animation_speed_2',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_1342_action_queue_async_37_SUBSCRIPT_set_animation_speed_3',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_1342_action_queue_async_37_SUBSCRIPT_walk_1_step_southeast_4',
                "command": 'walk_1_step_southeast'
            },
            {
                "identifier": 'EVENT_1342_action_queue_async_37_SUBSCRIPT_jump_to_height_5',
                "command": 'jump_to_height',
                "args": [128]
            },
            {
                "identifier": 'EVENT_1342_action_queue_async_37_SUBSCRIPT_shift_southeast_steps_6',
                "command": 'shift_southeast_steps',
                "args": [3]
            },
            {
                "identifier": 'EVENT_1342_action_queue_async_37_SUBSCRIPT_pause_7',
                "command": 'pause',
                "args": [15]
            },
            {
                "identifier": 'EVENT_1342_action_queue_async_37_SUBSCRIPT_visibility_off_8',
                "command": 'visibility_off'
            }
        ]
    },
    {
        "identifier": 'EVENT_1342_remove_from_current_level_38',
        "command": 'remove_from_current_level',
        "args": [AreaObjects.NPC_1]
    },
    {
        "identifier": 'EVENT_1342_set_39',
        "command": 'set',
        "args": [0x70a7, 11]
    },
    {
        "identifier": 'EVENT_1342_set_40',
        "command": 'set',
        "args": [0x7000, 2754]
    },
    {
        "identifier": 'EVENT_1342_run_event_as_subroutine_41',
        "command": 'run_event_as_subroutine',
        "args": [3829]
    },
    {
        "identifier": 'EVENT_1342_unfreeze_camera_42',
        "command": 'unfreeze_camera'
    },
    {
        "identifier": 'EVENT_1342_ret_43',
        "command": 'ret'
    }
]
