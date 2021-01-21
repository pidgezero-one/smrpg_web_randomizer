from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data import items
script = [
    {
        "identifier": 'EVENT_3806_freeze_camera_0',
        "command": 'freeze_camera'
    },
    {
        "identifier": 'EVENT_3806_run_background_event_1',
        "command": 'run_background_event',
        "args": [3808, [_0x40Flags.RETURN_ON_LEVEL_EXIT]]
    },
    {
        "identifier": 'EVENT_3806_action_queue_sync_2',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_7],
        "subscript": [
            {
                "identifier": 'EVENT_3806_action_queue_sync_2_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_SLOW, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_3806_action_queue_sync_2_SUBSCRIPT_set_animation_speed_1',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3806_action_queue_sync_2_SUBSCRIPT_shift_southwest_steps_2',
                "command": 'shift_southwest_steps',
                "args": [2]
            },
            {
                "identifier": 'EVENT_3806_action_queue_sync_2_SUBSCRIPT_shift_southwest_pixels_3',
                "command": 'shift_southwest_pixels',
                "args": [8]
            },
            {
                "identifier": 'EVENT_3806_action_queue_sync_2_SUBSCRIPT_face_southeast_4',
                "command": 'face_southeast'
            },
            {
                "identifier": 'EVENT_3806_action_queue_sync_2_SUBSCRIPT_pause_5',
                "command": 'pause',
                "args": [30]
            },
            {
                "identifier": 'EVENT_3806_action_queue_sync_2_SUBSCRIPT_face_northeast_6',
                "command": 'face_northeast'
            },
            {
                "identifier": 'EVENT_3806_action_queue_sync_2_SUBSCRIPT_set_animation_speed_7',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3806_action_queue_sync_2_SUBSCRIPT_set_sprite_sequence_8',
                "command": 'set_sprite_sequence',
                "args": [13, inc_sprite=1, flags=[_0x08Flags.LOOPING_OFF, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_3806_action_queue_sync_2_SUBSCRIPT_pause_9',
                "command": 'pause',
                "args": [68]
            },
            {
                "identifier": 'EVENT_3806_action_queue_sync_2_SUBSCRIPT_reset_properties_10',
                "command": 'reset_properties'
            },
            {
                "identifier": 'EVENT_3806_action_queue_sync_2_SUBSCRIPT_face_southeast_11',
                "command": 'face_southeast'
            },
            {
                "identifier": 'EVENT_3806_action_queue_sync_2_SUBSCRIPT_pause_12',
                "command": 'pause',
                "args": [2]
            },
            {
                "identifier": 'EVENT_3806_action_queue_sync_2_SUBSCRIPT_face_southwest_13',
                "command": 'face_southwest'
            },
            {
                "identifier": 'EVENT_3806_action_queue_sync_2_SUBSCRIPT_set_animation_speed_14',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_3806_action_queue_sync_2_SUBSCRIPT_set_animation_speed_15',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3806_action_queue_sync_2_SUBSCRIPT_sequence_looping_on_16',
                "command": 'sequence_looping_on'
            },
            {
                "identifier": 'EVENT_3806_action_queue_sync_2_SUBSCRIPT_pause_17',
                "command": 'pause',
                "args": [60]
            },
            {
                "identifier": 'EVENT_3806_action_queue_sync_2_SUBSCRIPT_shift_southwest_steps_18',
                "command": 'shift_southwest_steps',
                "args": [5]
            },
            {
                "identifier": 'EVENT_3806_action_queue_sync_2_SUBSCRIPT_shift_southwest_pixels_19',
                "command": 'shift_southwest_pixels',
                "args": [12]
            },
            {
                "identifier": 'EVENT_3806_action_queue_sync_2_SUBSCRIPT_set_animation_speed_20',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.SLOW, [_0x10Flags.SEQUENCE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_3806_action_queue_sync_3',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_10],
        "subscript": [
            {
                "identifier": 'EVENT_3806_action_queue_sync_3_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_SLOW, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_3806_action_queue_sync_3_SUBSCRIPT_set_animation_speed_1',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3806_action_queue_sync_3_SUBSCRIPT_walk_1_step_southwest_2',
                "command": 'walk_1_step_southwest'
            },
            {
                "identifier": 'EVENT_3806_action_queue_sync_3_SUBSCRIPT_set_sprite_sequence_3',
                "command": 'set_sprite_sequence',
                "args": [4, inc_sprite=0, flags=[_0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3806_action_queue_sync_3_SUBSCRIPT_pause_4',
                "command": 'pause',
                "args": [61]
            },
            {
                "identifier": 'EVENT_3806_action_queue_sync_3_SUBSCRIPT_reset_properties_5',
                "command": 'reset_properties'
            },
            {
                "identifier": 'EVENT_3806_action_queue_sync_3_SUBSCRIPT_face_northwest_6',
                "command": 'face_northwest'
            },
            {
                "identifier": 'EVENT_3806_action_queue_sync_3_SUBSCRIPT_pause_7',
                "command": 'pause',
                "args": [2]
            },
            {
                "identifier": 'EVENT_3806_action_queue_sync_3_SUBSCRIPT_face_northeast_8',
                "command": 'face_northeast'
            },
            {
                "identifier": 'EVENT_3806_action_queue_sync_3_SUBSCRIPT_pause_9',
                "command": 'pause',
                "args": [60]
            },
            {
                "identifier": 'EVENT_3806_action_queue_sync_3_SUBSCRIPT_face_northwest_10',
                "command": 'face_northwest'
            },
            {
                "identifier": 'EVENT_3806_action_queue_sync_3_SUBSCRIPT_pause_11',
                "command": 'pause',
                "args": [2]
            },
            {
                "identifier": 'EVENT_3806_action_queue_sync_3_SUBSCRIPT_face_southwest_12',
                "command": 'face_southwest'
            },
            {
                "identifier": 'EVENT_3806_action_queue_sync_3_SUBSCRIPT_set_animation_speed_13',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3806_action_queue_sync_3_SUBSCRIPT_sequence_looping_on_14',
                "command": 'sequence_looping_on'
            },
            {
                "identifier": 'EVENT_3806_action_queue_sync_3_SUBSCRIPT_set_animation_speed_15',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_SLOW, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_3806_action_queue_sync_3_SUBSCRIPT_shift_z_up_pixels_16',
                "command": 'shift_z_up_pixels',
                "args": [12]
            },
            {
                "identifier": 'EVENT_3806_action_queue_sync_3_SUBSCRIPT_shift_z_down_pixels_17',
                "command": 'shift_z_down_pixels',
                "args": [12]
            },
            {
                "identifier": 'EVENT_3806_action_queue_sync_3_SUBSCRIPT_set_animation_speed_18',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_3806_action_queue_sync_3_SUBSCRIPT_shift_southwest_steps_19',
                "command": 'shift_southwest_steps',
                "args": [4]
            },
            {
                "identifier": 'EVENT_3806_action_queue_sync_3_SUBSCRIPT_sequence_looping_off_20',
                "command": 'sequence_looping_off'
            },
            {
                "identifier": 'EVENT_3806_action_queue_sync_3_SUBSCRIPT_set_animation_speed_21',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.SEQUENCE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_3806_action_queue_sync_4',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_9],
        "subscript": [
            {
                "identifier": 'EVENT_3806_action_queue_sync_4_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [159]
            },
            {
                "identifier": 'EVENT_3806_action_queue_sync_4_SUBSCRIPT_set_sprite_sequence_1',
                "command": 'set_sprite_sequence',
                "args": [12, inc_sprite=0, flags=[_0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3806_action_queue_sync_4_SUBSCRIPT_visibility_off_2',
                "command": 'visibility_off'
            },
            {
                "identifier": 'EVENT_3806_action_queue_sync_4_SUBSCRIPT_transfer_to_object_xy_3',
                "command": 'transfer_to_object_xy',
                "args": [AreaObjects.NPC_10]
            },
            {
                "identifier": 'EVENT_3806_action_queue_sync_4_SUBSCRIPT_transfer_xyzf_pixels_4',
                "command": 'transfer_xyzf_pixels',
                "args": [4, 254, 0, RadialDirections.EAST]
            },
            {
                "identifier": 'EVENT_3806_action_queue_sync_4_SUBSCRIPT_set_vram_priority_5',
                "command": 'set_vram_priority',
                "args": [VramPriority.MARIO_OVERLAPS_ON_ALL_SIDES]
            },
            {
                "identifier": 'EVENT_3806_action_queue_sync_4_SUBSCRIPT_set_priority_6',
                "command": 'set_priority',
                "args": [3]
            },
            {
                "identifier": 'EVENT_3806_action_queue_sync_4_SUBSCRIPT_visibility_on_7',
                "command": 'visibility_on'
            },
            {
                "identifier": 'EVENT_3806_action_queue_sync_4_SUBSCRIPT_floating_on_8',
                "command": 'floating_on'
            },
            {
                "identifier": 'EVENT_3806_action_queue_sync_4_SUBSCRIPT_set_animation_speed_9',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_3806_action_queue_sync_4_SUBSCRIPT_shift_north_steps_10',
                "command": 'shift_north_steps',
                "args": [4]
            },
            {
                "identifier": 'EVENT_3806_action_queue_sync_4_SUBSCRIPT_set_animation_speed_11',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_3806_action_queue_sync_4_SUBSCRIPT_shift_north_pixels_12',
                "command": 'shift_north_pixels',
                "args": [8]
            },
            {
                "identifier": 'EVENT_3806_action_queue_sync_4_SUBSCRIPT_set_animation_speed_13',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_3806_action_queue_sync_4_SUBSCRIPT_shift_north_pixels_14',
                "command": 'shift_north_pixels',
                "args": [4]
            },
            {
                "identifier": 'EVENT_3806_action_queue_sync_4_SUBSCRIPT_set_animation_speed_15',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.SLOW, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_3806_action_queue_sync_4_SUBSCRIPT_shift_north_pixels_16',
                "command": 'shift_north_pixels',
                "args": [2]
            },
            {
                "identifier": 'EVENT_3806_action_queue_sync_4_SUBSCRIPT_shift_south_pixels_17',
                "command": 'shift_south_pixels',
                "args": [2]
            },
            {
                "identifier": 'EVENT_3806_action_queue_sync_4_SUBSCRIPT_set_animation_speed_18',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_3806_action_queue_sync_4_SUBSCRIPT_shift_south_pixels_19',
                "command": 'shift_south_pixels',
                "args": [4]
            },
            {
                "identifier": 'EVENT_3806_action_queue_sync_4_SUBSCRIPT_set_vram_priority_20',
                "command": 'set_vram_priority',
                "args": [VramPriority.NORMAL]
            },
            {
                "identifier": 'EVENT_3806_action_queue_sync_4_SUBSCRIPT_set_animation_speed_21',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_3806_action_queue_sync_4_SUBSCRIPT_walk_1_step_south_22',
                "command": 'walk_1_step_south'
            },
            {
                "identifier": 'EVENT_3806_action_queue_sync_4_SUBSCRIPT_set_animation_speed_23',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_3806_action_queue_sync_4_SUBSCRIPT_walk_1_step_south_24',
                "command": 'walk_1_step_south'
            },
            {
                "identifier": 'EVENT_3806_action_queue_sync_4_SUBSCRIPT_shift_south_pixels_25',
                "command": 'shift_south_pixels',
                "args": [2]
            },
            {
                "identifier": 'EVENT_3806_action_queue_sync_4_SUBSCRIPT_walk_1_step_southwest_26',
                "command": 'walk_1_step_southwest'
            },
            {
                "identifier": 'EVENT_3806_action_queue_sync_4_SUBSCRIPT_visibility_off_27',
                "command": 'visibility_off'
            }
        ]
    },
    {
        "identifier": 'EVENT_3806_action_queue_sync_5',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_5],
        "subscript": [
            {
                "identifier": 'EVENT_3806_action_queue_sync_5_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [300]
            },
            {
                "identifier": 'EVENT_3806_action_queue_sync_5_SUBSCRIPT_face_southwest_1',
                "command": 'face_southwest'
            }
        ]
    },
    {
        "identifier": 'EVENT_3806_action_queue_sync_6',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_6],
        "subscript": [
            {
                "identifier": 'EVENT_3806_action_queue_sync_6_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [300]
            },
            {
                "identifier": 'EVENT_3806_action_queue_sync_6_SUBSCRIPT_face_southwest_1',
                "command": 'face_southwest'
            }
        ]
    },
    {
        "identifier": 'EVENT_3806_star_mask_expand_from_screen_center_7',
        "command": 'star_mask_expand_from_screen_center'
    },
    {
        "identifier": 'EVENT_3806_remember_last_object_8',
        "command": 'remember_last_object'
    },
    {
        "identifier": 'EVENT_3806_action_queue_sync_9',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_3],
        "subscript": [
            {
                "identifier": 'EVENT_3806_action_queue_sync_9_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_3806_action_queue_sync_9_SUBSCRIPT_set_animation_speed_1',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3806_action_queue_sync_9_SUBSCRIPT_shift_southwest_steps_2',
                "command": 'shift_southwest_steps',
                "args": [3]
            },
            {
                "identifier": 'EVENT_3806_action_queue_sync_9_SUBSCRIPT_shift_northwest_steps_3',
                "command": 'shift_northwest_steps',
                "args": [5]
            },
            {
                "identifier": 'EVENT_3806_action_queue_sync_9_SUBSCRIPT_shift_northeast_steps_4',
                "command": 'shift_northeast_steps',
                "args": [1]
            },
            {
                "identifier": 'EVENT_3806_action_queue_sync_9_SUBSCRIPT_shift_northeast_pixels_5',
                "command": 'shift_northeast_pixels',
                "args": [12]
            },
            {
                "identifier": 'EVENT_3806_action_queue_sync_9_SUBSCRIPT_face_southeast_6',
                "command": 'face_southeast'
            },
            {
                "identifier": 'EVENT_3806_action_queue_sync_9_SUBSCRIPT_sequence_looping_off_7',
                "command": 'sequence_looping_off'
            }
        ]
    },
    {
        "identifier": 'EVENT_3806_action_queue_sync_10',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_4],
        "subscript": [
            {
                "identifier": 'EVENT_3806_action_queue_sync_10_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_3806_action_queue_sync_10_SUBSCRIPT_set_animation_speed_1',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3806_action_queue_sync_10_SUBSCRIPT_shift_southwest_steps_2',
                "command": 'shift_southwest_steps',
                "args": [4]
            },
            {
                "identifier": 'EVENT_3806_action_queue_sync_10_SUBSCRIPT_shift_southwest_pixels_3',
                "command": 'shift_southwest_pixels',
                "args": [4]
            },
            {
                "identifier": 'EVENT_3806_action_queue_sync_10_SUBSCRIPT_shift_northwest_steps_4',
                "command": 'shift_northwest_steps',
                "args": [4]
            },
            {
                "identifier": 'EVENT_3806_action_queue_sync_10_SUBSCRIPT_shift_northwest_pixels_5',
                "command": 'shift_northwest_pixels',
                "args": [4]
            },
            {
                "identifier": 'EVENT_3806_action_queue_sync_10_SUBSCRIPT_face_northeast_6',
                "command": 'face_northeast'
            },
            {
                "identifier": 'EVENT_3806_action_queue_sync_10_SUBSCRIPT_sequence_looping_off_7',
                "command": 'sequence_looping_off'
            }
        ]
    },
    {
        "identifier": 'EVENT_3806_action_queue_sync_11',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_2],
        "subscript": [
            {
                "identifier": 'EVENT_3806_action_queue_sync_11_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_3806_action_queue_sync_11_SUBSCRIPT_set_animation_speed_1',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3806_action_queue_sync_11_SUBSCRIPT_shift_southwest_steps_2',
                "command": 'shift_southwest_steps',
                "args": [5]
            },
            {
                "identifier": 'EVENT_3806_action_queue_sync_11_SUBSCRIPT_shift_southwest_pixels_3',
                "command": 'shift_southwest_pixels',
                "args": [6]
            },
            {
                "identifier": 'EVENT_3806_action_queue_sync_11_SUBSCRIPT_shift_northwest_steps_4',
                "command": 'shift_northwest_steps',
                "args": [2]
            },
            {
                "identifier": 'EVENT_3806_action_queue_sync_11_SUBSCRIPT_shift_northwest_pixels_5',
                "command": 'shift_northwest_pixels',
                "args": [12]
            },
            {
                "identifier": 'EVENT_3806_action_queue_sync_11_SUBSCRIPT_sequence_looping_off_6',
                "command": 'sequence_looping_off'
            }
        ]
    },
    {
        "identifier": 'EVENT_3806_set_action_script_sync_12',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_10, 239]
    },
    {
        "identifier": 'EVENT_3806_remember_last_object_13',
        "command": 'remember_last_object'
    },
    {
        "identifier": 'EVENT_3806_action_queue_async_14',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_7],
        "subscript": [
            {
                "identifier": 'EVENT_3806_action_queue_async_14_SUBSCRIPT_sequence_looping_off_0',
                "command": 'sequence_looping_off'
            }
        ]
    },
    {
        "identifier": 'EVENT_3806_set_action_script_sync_15',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_7, 677]
    },
    {
        "identifier": 'EVENT_3806_set_action_script_sync_16',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_2, 677]
    },
    {
        "identifier": 'EVENT_3806_set_action_script_sync_17',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_3, 677]
    },
    {
        "identifier": 'EVENT_3806_set_action_script_sync_18',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_4, 677]
    },
    {
        "identifier": 'EVENT_3806_action_queue_sync_19',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_0],
        "subscript": [
            {
                "identifier": 'EVENT_3806_action_queue_sync_19_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_3806_action_queue_sync_19_SUBSCRIPT_set_animation_speed_1',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3806_action_queue_sync_19_SUBSCRIPT_shift_southeast_steps_2',
                "command": 'shift_southeast_steps',
                "args": [4]
            },
            {
                "identifier": 'EVENT_3806_action_queue_sync_19_SUBSCRIPT_pause_3',
                "command": 'pause',
                "args": [134]
            },
            {
                "identifier": 'EVENT_3806_action_queue_sync_19_SUBSCRIPT_set_animation_speed_4',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_SLOW, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_3806_action_queue_sync_19_SUBSCRIPT_set_animation_speed_5',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3806_action_queue_sync_19_SUBSCRIPT_shift_northeast_steps_6',
                "command": 'shift_northeast_steps',
                "args": [12]
            }
        ]
    },
    {
        "identifier": 'EVENT_3806_set_action_script_sync_20',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_5, 208]
    },
    {
        "identifier": 'EVENT_3806_set_action_script_sync_21',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_6, 209]
    },
    {
        "identifier": 'EVENT_3806_pause_short_22',
        "command": 'pause_short',
        "args": [425]
    },
    {
        "identifier": 'EVENT_3806_pause_script_until_effect_done_23',
        "command": 'pause_script_until_effect_done'
    },
    {
        "identifier": 'EVENT_3806_star_mask_shrink_to_screen_center_24',
        "command": 'star_mask_shrink_to_screen_center'
    },
    {
        "identifier": 'EVENT_3806_pause_script_until_effect_done_25',
        "command": 'pause_script_until_effect_done'
    },
    {
        "identifier": 'EVENT_3806_jmp_to_event_26',
        "command": 'jmp_to_event',
        "args": [3800]
    }
]
