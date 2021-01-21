from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data import items
script = [
    {
        "identifier": 'EVENT_3729_fade_in_from_black_async_0',
        "command": 'fade_in_from_black_async'
    },
    {
        "identifier": 'EVENT_3729_jmp_1',
        "command": 'jmp',
        "args": ['EVENT_3729_set_bit_158']
    },
    {
        "identifier": 'EVENT_3729_ret_2',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_3729_reset_game_3',
        "command": 'reset_game'
    },
    {
        "identifier": 'EVENT_3729_enable_event_trigger_for_object_at_70A8_4',
        "command": 'enable_event_trigger_for_object_at_70A8'
    },
    {
        "identifier": 'EVENT_3729_add_short_5',
        "command": 'add_short',
        "args": [0x71b4, 0x01]
    },
    {
        "identifier": 'EVENT_3729_reset_priority_set_6',
        "command": 'reset_priority_set'
    },
    {
        "identifier": 'EVENT_3729_fade_out_music_to_volume_7',
        "command": 'fade_out_music_to_volume',
        "args": [117, 253]
    },
    {
        "identifier": 'EVENT_3729_unfreeze_all_npcs_8',
        "command": 'unfreeze_all_npcs'
    },
    {
        "identifier": 'EVENT_3729_action_queue_sync_9',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_8],
        "subscript": [
            {
                "identifier": 'EVENT_3729_action_queue_sync_9_SUBSCRIPT_shadow_off_0',
                "command": 'shadow_off'
            }
        ]
    },
    {
        "identifier": 'EVENT_3729_action_queue_sync_10',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_3729_action_queue_sync_10_SUBSCRIPT_set_sprite_sequence_0',
                "command": 'set_sprite_sequence',
                "args": [5, 6, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_3729_action_queue_sync_10_SUBSCRIPT_pause_1',
                "command": 'pause',
                "args": [1]
            },
            {
                "identifier": 'EVENT_3729_action_queue_sync_10_SUBSCRIPT_reset_properties_2',
                "command": 'reset_properties'
            }
        ]
    },
    {
        "identifier": 'EVENT_3729_action_queue_sync_11',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_9],
        "subscript": [
            {
                "identifier": 'EVENT_3729_action_queue_sync_11_SUBSCRIPT_transfer_xyzf_pixels_0',
                "command": 'transfer_xyzf_pixels',
                "args": [8, 4, 0, RadialDirections.EAST]
            }
        ]
    },
    {
        "identifier": 'EVENT_3729_action_queue_async_12',
        "command": 'action_queue_async',
        "args": [AreaObjects.SCREEN_FOCUS],
        "subscript": [
            {
                "identifier": 'EVENT_3729_action_queue_async_12_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FASTEST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_3729_action_queue_async_12_SUBSCRIPT_walk_1_step_northeast_1',
                "command": 'walk_1_step_northeast'
            },
            {
                "identifier": 'EVENT_3729_action_queue_async_12_SUBSCRIPT_walk_1_step_north_2',
                "command": 'walk_1_step_north'
            }
        ]
    },
    {
        "identifier": 'EVENT_3729_fade_in_from_black_sync_duration_13',
        "command": 'fade_in_from_black_sync_duration',
        "args": [60]
    },
    {
        "identifier": 'EVENT_3729_action_queue_sync_14',
        "command": 'action_queue_sync',
        "args": [AreaObjects.SCREEN_FOCUS],
        "subscript": [
            {
                "identifier": 'EVENT_3729_action_queue_sync_14_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_3729_action_queue_sync_14_SUBSCRIPT_shift_northeast_steps_1',
                "command": 'shift_northeast_steps',
                "args": [10]
            }
        ]
    },
    {
        "identifier": 'EVENT_3729_action_queue_sync_15',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_8],
        "subscript": [
            {
                "identifier": 'EVENT_3729_action_queue_sync_15_SUBSCRIPT_face_northeast_0',
                "command": 'face_northeast'
            },
            {
                "identifier": 'EVENT_3729_action_queue_sync_15_SUBSCRIPT_transfer_to_xyzf_1',
                "command": 'transfer_to_xyzf',
                "args": [4, 57, 6, RadialDirections.EAST]
            },
            {
                "identifier": 'EVENT_3729_action_queue_sync_15_SUBSCRIPT_set_animation_speed_2',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_SLOW, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_3729_action_queue_sync_15_SUBSCRIPT_shift_northeast_steps_3',
                "command": 'shift_northeast_steps',
                "args": [3]
            },
            {
                "identifier": 'EVENT_3729_action_queue_sync_15_SUBSCRIPT_set_animation_speed_4',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.SLOW, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3729_action_queue_sync_15_SUBSCRIPT_sequence_looping_on_5',
                "command": 'sequence_looping_on'
            }
        ]
    },
    {
        "identifier": 'EVENT_3729_action_queue_sync_16',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_7],
        "subscript": [
            {
                "identifier": 'EVENT_3729_action_queue_sync_16_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [60]
            },
            {
                "identifier": 'EVENT_3729_action_queue_sync_16_SUBSCRIPT_add_z_coord_1_step_1',
                "command": 'add_z_coord_1_step'
            },
            {
                "identifier": 'EVENT_3729_action_queue_sync_16_SUBSCRIPT_set_animation_speed_2',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_3729_action_queue_sync_16_SUBSCRIPT_shift_z_down_pixels_3',
                "command": 'shift_z_down_pixels',
                "args": [6]
            },
            {
                "identifier": 'EVENT_3729_action_queue_sync_16_SUBSCRIPT_set_animation_speed_4',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_3729_action_queue_sync_16_SUBSCRIPT_shift_z_down_pixels_5',
                "command": 'shift_z_down_pixels',
                "args": [10]
            },
            {
                "identifier": 'EVENT_3729_action_queue_sync_16_SUBSCRIPT_sequence_playback_on_6',
                "command": 'sequence_playback_on'
            },
            {
                "identifier": 'EVENT_3729_action_queue_sync_16_SUBSCRIPT_pause_7',
                "command": 'pause',
                "args": [60]
            },
            {
                "identifier": 'EVENT_3729_action_queue_sync_16_SUBSCRIPT_set_animation_speed_8',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.SLOW, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_3729_action_queue_sync_16_SUBSCRIPT_set_animation_speed_9',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3729_action_queue_sync_16_SUBSCRIPT_walk_1_step_southeast_10',
                "command": 'walk_1_step_southeast'
            },
            {
                "identifier": 'EVENT_3729_action_queue_sync_16_SUBSCRIPT_face_southwest_11',
                "command": 'face_southwest'
            }
        ]
    },
    {
        "identifier": 'EVENT_3729_action_queue_sync_17',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_9],
        "subscript": [
            {
                "identifier": 'EVENT_3729_action_queue_sync_17_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [80]
            },
            {
                "identifier": 'EVENT_3729_action_queue_sync_17_SUBSCRIPT_set_sprite_sequence_1',
                "command": 'set_sprite_sequence',
                "args": [22, 0, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_3729_action_queue_sync_17_SUBSCRIPT_pause_2',
                "command": 'pause',
                "args": [4]
            },
            {
                "identifier": 'EVENT_3729_action_queue_sync_17_SUBSCRIPT_set_sprite_sequence_3',
                "command": 'set_sprite_sequence',
                "args": [23, 0, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_3729_action_queue_sync_17_SUBSCRIPT_pause_4',
                "command": 'pause',
                "args": [2]
            },
            {
                "identifier": 'EVENT_3729_action_queue_sync_17_SUBSCRIPT_set_sprite_sequence_5',
                "command": 'set_sprite_sequence',
                "args": [24, 0, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_3729_action_queue_sync_17_SUBSCRIPT_pause_6',
                "command": 'pause',
                "args": [4]
            },
            {
                "identifier": 'EVENT_3729_action_queue_sync_17_SUBSCRIPT_start_loop_n_times_7',
                "command": 'start_loop_n_times',
                "args": [1]
            },
            {
                "identifier": 'EVENT_3729_action_queue_sync_17_SUBSCRIPT_set_sprite_sequence_8',
                "command": 'set_sprite_sequence',
                "args": [22, 0, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_3729_action_queue_sync_17_SUBSCRIPT_pause_9',
                "command": 'pause',
                "args": [2]
            },
            {
                "identifier": 'EVENT_3729_action_queue_sync_17_SUBSCRIPT_set_sprite_sequence_10',
                "command": 'set_sprite_sequence',
                "args": [23, 0, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_3729_action_queue_sync_17_SUBSCRIPT_pause_11',
                "command": 'pause',
                "args": [2]
            },
            {
                "identifier": 'EVENT_3729_action_queue_sync_17_SUBSCRIPT_set_sprite_sequence_12',
                "command": 'set_sprite_sequence',
                "args": [24, 0, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_3729_action_queue_sync_17_SUBSCRIPT_pause_13',
                "command": 'pause',
                "args": [4]
            },
            {
                "identifier": 'EVENT_3729_action_queue_sync_17_SUBSCRIPT_end_loop_14',
                "command": 'end_loop'
            },
            {
                "identifier": 'EVENT_3729_action_queue_sync_17_SUBSCRIPT_set_sprite_sequence_15',
                "command": 'set_sprite_sequence',
                "args": [0, 0, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_3729_pause_script_until_effect_done_18',
        "command": 'pause_script_until_effect_done'
    },
    {
        "identifier": 'EVENT_3729_pause_19',
        "command": 'pause',
        "args": [60]
    },
    {
        "identifier": 'EVENT_3729_run_dialog_20',
        "command": 'run_dialog',
        "args": [3616, AreaObjects.NPC_14, [_0x60Flags.ASYNC, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_3729_remember_last_object_21',
        "command": 'remember_last_object'
    },
    {
        "identifier": 'EVENT_3729_run_dialog_22',
        "command": 'run_dialog',
        "args": [3617, AreaObjects.NPC_14, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_3729_pause_23',
        "command": 'pause',
        "args": [10]
    },
    {
        "identifier": 'EVENT_3729_run_dialog_24',
        "command": 'run_dialog',
        "args": [3618, AreaObjects.NPC_12, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_3729_pause_25',
        "command": 'pause',
        "args": [10]
    },
    {
        "identifier": 'EVENT_3729_run_dialog_26',
        "command": 'run_dialog',
        "args": [3619, AreaObjects.NPC_14, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_3729_pause_27',
        "command": 'pause',
        "args": [10]
    },
    {
        "identifier": 'EVENT_3729_action_queue_async_28',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_7],
        "subscript": [
            {
                "identifier": 'EVENT_3729_action_queue_async_28_SUBSCRIPT_face_northwest_0',
                "command": 'face_northwest'
            },
            {
                "identifier": 'EVENT_3729_action_queue_async_28_SUBSCRIPT_pause_1',
                "command": 'pause',
                "args": [2]
            },
            {
                "identifier": 'EVENT_3729_action_queue_async_28_SUBSCRIPT_face_northeast_2',
                "command": 'face_northeast'
            }
        ]
    },
    {
        "identifier": 'EVENT_3729_pause_29',
        "command": 'pause',
        "args": [30]
    },
    {
        "identifier": 'EVENT_3729_run_dialog_30',
        "command": 'run_dialog',
        "args": [3620, AreaObjects.NPC_12, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_3729_pause_31',
        "command": 'pause',
        "args": [30]
    },
    {
        "identifier": 'EVENT_3729_palette_set_32',
        "command": 'palette_set',
        "args": [111, 1]
    },
    {
        "identifier": 'EVENT_3729_action_queue_async_33',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_3729_action_queue_async_33_SUBSCRIPT_visibility_off_0',
                "command": 'visibility_off'
            },
            {
                "identifier": 'EVENT_3729_action_queue_async_33_SUBSCRIPT_transfer_to_xyzf_1',
                "command": 'transfer_to_xyzf',
                "args": [8, 52, 4, RadialDirections.EAST]
            },
            {
                "identifier": 'EVENT_3729_action_queue_async_33_SUBSCRIPT_transfer_xyzf_pixels_2',
                "command": 'transfer_xyzf_pixels',
                "args": [8, 252, 0, RadialDirections.EAST]
            },
            {
                "identifier": 'EVENT_3729_action_queue_async_33_SUBSCRIPT_face_southwest_3',
                "command": 'face_southwest'
            },
            {
                "identifier": 'EVENT_3729_action_queue_async_33_SUBSCRIPT_visibility_on_4',
                "command": 'visibility_on'
            },
            {
                "identifier": 'EVENT_3729_action_queue_async_33_SUBSCRIPT_pause_5',
                "command": 'pause',
                "args": [1]
            },
            {
                "identifier": 'EVENT_3729_action_queue_async_33_SUBSCRIPT_start_loop_n_times_6',
                "command": 'start_loop_n_times',
                "args": [7]
            },
            {
                "identifier": 'EVENT_3729_action_queue_async_33_SUBSCRIPT_visibility_off_7',
                "command": 'visibility_off'
            },
            {
                "identifier": 'EVENT_3729_action_queue_async_33_SUBSCRIPT_pause_8',
                "command": 'pause',
                "args": [1]
            },
            {
                "identifier": 'EVENT_3729_action_queue_async_33_SUBSCRIPT_visibility_on_9',
                "command": 'visibility_on'
            },
            {
                "identifier": 'EVENT_3729_action_queue_async_33_SUBSCRIPT_pause_10',
                "command": 'pause',
                "args": [1]
            },
            {
                "identifier": 'EVENT_3729_action_queue_async_33_SUBSCRIPT_end_loop_11',
                "command": 'end_loop'
            },
            {
                "identifier": 'EVENT_3729_action_queue_async_33_SUBSCRIPT_start_loop_n_times_12',
                "command": 'start_loop_n_times',
                "args": [7]
            },
            {
                "identifier": 'EVENT_3729_action_queue_async_33_SUBSCRIPT_visibility_off_13',
                "command": 'visibility_off'
            },
            {
                "identifier": 'EVENT_3729_action_queue_async_33_SUBSCRIPT_pause_14',
                "command": 'pause',
                "args": [2]
            },
            {
                "identifier": 'EVENT_3729_action_queue_async_33_SUBSCRIPT_visibility_on_15',
                "command": 'visibility_on'
            },
            {
                "identifier": 'EVENT_3729_action_queue_async_33_SUBSCRIPT_pause_16',
                "command": 'pause',
                "args": [2]
            },
            {
                "identifier": 'EVENT_3729_action_queue_async_33_SUBSCRIPT_end_loop_17',
                "command": 'end_loop'
            },
            {
                "identifier": 'EVENT_3729_action_queue_async_33_SUBSCRIPT_start_loop_n_times_18',
                "command": 'start_loop_n_times',
                "args": [1]
            },
            {
                "identifier": 'EVENT_3729_action_queue_async_33_SUBSCRIPT_visibility_off_19',
                "command": 'visibility_off'
            },
            {
                "identifier": 'EVENT_3729_action_queue_async_33_SUBSCRIPT_pause_20',
                "command": 'pause',
                "args": [4]
            },
            {
                "identifier": 'EVENT_3729_action_queue_async_33_SUBSCRIPT_visibility_on_21',
                "command": 'visibility_on'
            },
            {
                "identifier": 'EVENT_3729_action_queue_async_33_SUBSCRIPT_pause_22',
                "command": 'pause',
                "args": [4]
            },
            {
                "identifier": 'EVENT_3729_action_queue_async_33_SUBSCRIPT_end_loop_23',
                "command": 'end_loop'
            },
            {
                "identifier": 'EVENT_3729_action_queue_async_33_SUBSCRIPT_pause_24',
                "command": 'pause',
                "args": [90]
            },
            {
                "identifier": 'EVENT_3729_action_queue_async_33_SUBSCRIPT_set_sprite_sequence_25',
                "command": 'set_sprite_sequence',
                "args": [30, 2, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3729_action_queue_async_33_SUBSCRIPT_pause_26',
                "command": 'pause',
                "args": [30]
            },
            {
                "identifier": 'EVENT_3729_action_queue_async_33_SUBSCRIPT_reset_properties_27',
                "command": 'reset_properties'
            },
            {
                "identifier": 'EVENT_3729_action_queue_async_33_SUBSCRIPT_pause_28',
                "command": 'pause',
                "args": [30]
            },
            {
                "identifier": 'EVENT_3729_action_queue_async_33_SUBSCRIPT_start_loop_n_times_29',
                "command": 'start_loop_n_times',
                "args": [1]
            },
            {
                "identifier": 'EVENT_3729_action_queue_async_33_SUBSCRIPT_visibility_off_30',
                "command": 'visibility_off'
            },
            {
                "identifier": 'EVENT_3729_action_queue_async_33_SUBSCRIPT_pause_31',
                "command": 'pause',
                "args": [4]
            },
            {
                "identifier": 'EVENT_3729_action_queue_async_33_SUBSCRIPT_visibility_on_32',
                "command": 'visibility_on'
            },
            {
                "identifier": 'EVENT_3729_action_queue_async_33_SUBSCRIPT_pause_33',
                "command": 'pause',
                "args": [4]
            },
            {
                "identifier": 'EVENT_3729_action_queue_async_33_SUBSCRIPT_end_loop_34',
                "command": 'end_loop'
            },
            {
                "identifier": 'EVENT_3729_action_queue_async_33_SUBSCRIPT_start_loop_n_times_35',
                "command": 'start_loop_n_times',
                "args": [7]
            },
            {
                "identifier": 'EVENT_3729_action_queue_async_33_SUBSCRIPT_visibility_off_36',
                "command": 'visibility_off'
            },
            {
                "identifier": 'EVENT_3729_action_queue_async_33_SUBSCRIPT_pause_37',
                "command": 'pause',
                "args": [2]
            },
            {
                "identifier": 'EVENT_3729_action_queue_async_33_SUBSCRIPT_visibility_on_38',
                "command": 'visibility_on'
            },
            {
                "identifier": 'EVENT_3729_action_queue_async_33_SUBSCRIPT_pause_39',
                "command": 'pause',
                "args": [2]
            },
            {
                "identifier": 'EVENT_3729_action_queue_async_33_SUBSCRIPT_end_loop_40',
                "command": 'end_loop'
            },
            {
                "identifier": 'EVENT_3729_action_queue_async_33_SUBSCRIPT_start_loop_n_times_41',
                "command": 'start_loop_n_times',
                "args": [7]
            },
            {
                "identifier": 'EVENT_3729_action_queue_async_33_SUBSCRIPT_visibility_off_42',
                "command": 'visibility_off'
            },
            {
                "identifier": 'EVENT_3729_action_queue_async_33_SUBSCRIPT_pause_43',
                "command": 'pause',
                "args": [1]
            },
            {
                "identifier": 'EVENT_3729_action_queue_async_33_SUBSCRIPT_visibility_on_44',
                "command": 'visibility_on'
            },
            {
                "identifier": 'EVENT_3729_action_queue_async_33_SUBSCRIPT_pause_45',
                "command": 'pause',
                "args": [1]
            },
            {
                "identifier": 'EVENT_3729_action_queue_async_33_SUBSCRIPT_end_loop_46',
                "command": 'end_loop'
            },
            {
                "identifier": 'EVENT_3729_action_queue_async_33_SUBSCRIPT_visibility_off_47',
                "command": 'visibility_off'
            },
            {
                "identifier": 'EVENT_3729_action_queue_async_33_SUBSCRIPT_reset_properties_48',
                "command": 'reset_properties'
            },
            {
                "identifier": 'EVENT_3729_action_queue_async_33_SUBSCRIPT_face_northeast_49',
                "command": 'face_northeast'
            },
            {
                "identifier": 'EVENT_3729_action_queue_async_33_SUBSCRIPT_transfer_to_xyzf_50',
                "command": 'transfer_to_xyzf',
                "args": [1, 63, 0, RadialDirections.EAST]
            },
            {
                "identifier": 'EVENT_3729_action_queue_async_33_SUBSCRIPT_visibility_on_51',
                "command": 'visibility_on'
            }
        ]
    },
    {
        "identifier": 'EVENT_3729_palette_set_34',
        "command": 'palette_set',
        "args": [84, 1]
    },
    {
        "identifier": 'EVENT_3729_pause_35',
        "command": 'pause',
        "args": [30]
    },
    {
        "identifier": 'EVENT_3729_action_queue_async_36',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_7],
        "subscript": [
            {
                "identifier": 'EVENT_3729_action_queue_async_36_SUBSCRIPT_fixed_f_coord_on_0',
                "command": 'fixed_f_coord_on'
            },
            {
                "identifier": 'EVENT_3729_action_queue_async_36_SUBSCRIPT_sequence_playback_off_1',
                "command": 'sequence_playback_off'
            },
            {
                "identifier": 'EVENT_3729_action_queue_async_36_SUBSCRIPT_set_animation_speed_2',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_3729_action_queue_async_36_SUBSCRIPT_shift_southwest_pixels_3',
                "command": 'shift_southwest_pixels',
                "args": [6]
            },
            {
                "identifier": 'EVENT_3729_action_queue_async_36_SUBSCRIPT_set_animation_speed_4',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3729_action_queue_async_36_SUBSCRIPT_sequence_looping_on_5',
                "command": 'sequence_looping_on'
            },
            {
                "identifier": 'EVENT_3729_action_queue_async_36_SUBSCRIPT_pause_6',
                "command": 'pause',
                "args": [60]
            },
            {
                "identifier": 'EVENT_3729_action_queue_async_36_SUBSCRIPT_sequence_looping_off_7',
                "command": 'sequence_looping_off'
            },
            {
                "identifier": 'EVENT_3729_action_queue_async_36_SUBSCRIPT_shift_northeast_pixels_8',
                "command": 'shift_northeast_pixels',
                "args": [6]
            },
            {
                "identifier": 'EVENT_3729_action_queue_async_36_SUBSCRIPT_pause_9',
                "command": 'pause',
                "args": [10]
            },
            {
                "identifier": 'EVENT_3729_action_queue_async_36_SUBSCRIPT_pause_10',
                "command": 'pause',
                "args": [20]
            },
            {
                "identifier": 'EVENT_3729_action_queue_async_36_SUBSCRIPT_fixed_f_coord_off_11',
                "command": 'fixed_f_coord_off'
            },
            {
                "identifier": 'EVENT_3729_action_queue_async_36_SUBSCRIPT_sequence_playback_on_12',
                "command": 'sequence_playback_on'
            },
            {
                "identifier": 'EVENT_3729_action_queue_async_36_SUBSCRIPT_face_northwest_13',
                "command": 'face_northwest'
            },
            {
                "identifier": 'EVENT_3729_action_queue_async_36_SUBSCRIPT_pause_14',
                "command": 'pause',
                "args": [2]
            },
            {
                "identifier": 'EVENT_3729_action_queue_async_36_SUBSCRIPT_face_southwest_15',
                "command": 'face_southwest'
            }
        ]
    },
    {
        "identifier": 'EVENT_3729_pause_37',
        "command": 'pause',
        "args": [10]
    },
    {
        "identifier": 'EVENT_3729_run_dialog_38',
        "command": 'run_dialog',
        "args": [3621, AreaObjects.NPC_12, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_3729_pause_39',
        "command": 'pause',
        "args": [30]
    },
    {
        "identifier": 'EVENT_3729_action_queue_sync_40',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_8],
        "subscript": [
            {
                "identifier": 'EVENT_3729_action_queue_sync_40_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3729_action_queue_sync_40_SUBSCRIPT_set_animation_speed_1',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_3729_action_queue_sync_40_SUBSCRIPT_set_sprite_sequence_2',
                "command": 'set_sprite_sequence',
                "args": [6, 0, [_0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_3729_action_queue_sync_40_SUBSCRIPT_walk_1_step_southeast_3',
                "command": 'walk_1_step_southeast'
            },
            {
                "identifier": 'EVENT_3729_action_queue_sync_40_SUBSCRIPT_start_loop_n_times_4',
                "command": 'start_loop_n_times',
                "args": [1]
            },
            {
                "identifier": 'EVENT_3729_action_queue_sync_40_SUBSCRIPT_reset_properties_5',
                "command": 'reset_properties'
            },
            {
                "identifier": 'EVENT_3729_action_queue_sync_40_SUBSCRIPT_shift_northwest_steps_6',
                "command": 'shift_northwest_steps',
                "args": [2]
            },
            {
                "identifier": 'EVENT_3729_action_queue_sync_40_SUBSCRIPT_set_sprite_sequence_7',
                "command": 'set_sprite_sequence',
                "args": [6, 0, [_0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_3729_action_queue_sync_40_SUBSCRIPT_shift_southeast_steps_8',
                "command": 'shift_southeast_steps',
                "args": [2]
            },
            {
                "identifier": 'EVENT_3729_action_queue_sync_40_SUBSCRIPT_end_loop_9',
                "command": 'end_loop'
            },
            {
                "identifier": 'EVENT_3729_action_queue_sync_40_SUBSCRIPT_reset_properties_10',
                "command": 'reset_properties'
            },
            {
                "identifier": 'EVENT_3729_action_queue_sync_40_SUBSCRIPT_walk_1_step_northwest_11',
                "command": 'walk_1_step_northwest'
            },
            {
                "identifier": 'EVENT_3729_action_queue_sync_40_SUBSCRIPT_face_northeast_12',
                "command": 'face_northeast'
            }
        ]
    },
    {
        "identifier": 'EVENT_3729_pause_41',
        "command": 'pause',
        "args": [10]
    },
    {
        "identifier": 'EVENT_3729_run_dialog_42',
        "command": 'run_dialog',
        "args": [3622, AreaObjects.NPC_14, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_3729_remember_last_object_43',
        "command": 'remember_last_object'
    },
    {
        "identifier": 'EVENT_3729_action_queue_async_44',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_8],
        "subscript": [
            {
                "identifier": 'EVENT_3729_action_queue_async_44_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.SLOW, [_0x10Flags.SEQUENCE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_3729_pause_45',
        "command": 'pause',
        "args": [10]
    },
    {
        "identifier": 'EVENT_3729_run_dialog_46',
        "command": 'run_dialog',
        "args": [3623, AreaObjects.NPC_12, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_3729_action_queue_async_47',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_7],
        "subscript": [
            {
                "identifier": 'EVENT_3729_action_queue_async_47_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3729_action_queue_async_47_SUBSCRIPT_set_sprite_sequence_1',
                "command": 'set_sprite_sequence',
                "args": [2, 0, [_0x08Flags.READ_AS_SEQUENCE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_3729_pause_48',
        "command": 'pause',
        "args": [30]
    },
    {
        "identifier": 'EVENT_3729_action_queue_async_49',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_9],
        "subscript": [
            {
                "identifier": 'EVENT_3729_action_queue_async_49_SUBSCRIPT_set_sprite_sequence_0',
                "command": 'set_sprite_sequence',
                "args": [25, 0, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_3729_action_queue_async_49_SUBSCRIPT_pause_1',
                "command": 'pause',
                "args": [30]
            },
            {
                "identifier": 'EVENT_3729_action_queue_async_49_SUBSCRIPT_reset_properties_2',
                "command": 'reset_properties'
            },
            {
                "identifier": 'EVENT_3729_action_queue_async_49_SUBSCRIPT_pause_3',
                "command": 'pause',
                "args": [60]
            },
            {
                "identifier": 'EVENT_3729_action_queue_async_49_SUBSCRIPT_set_sprite_sequence_4',
                "command": 'set_sprite_sequence',
                "args": [25, 0, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_3729_action_queue_async_49_SUBSCRIPT_pause_5',
                "command": 'pause',
                "args": [30]
            },
            {
                "identifier": 'EVENT_3729_action_queue_async_49_SUBSCRIPT_reset_properties_6',
                "command": 'reset_properties'
            },
            {
                "identifier": 'EVENT_3729_action_queue_async_49_SUBSCRIPT_set_sprite_sequence_7',
                "command": 'set_sprite_sequence',
                "args": [25, 0, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_3729_action_queue_async_49_SUBSCRIPT_pause_8',
                "command": 'pause',
                "args": [10]
            },
            {
                "identifier": 'EVENT_3729_action_queue_async_49_SUBSCRIPT_reset_properties_9',
                "command": 'reset_properties'
            },
            {
                "identifier": 'EVENT_3729_action_queue_async_49_SUBSCRIPT_pause_10',
                "command": 'pause',
                "args": [20]
            },
            {
                "identifier": 'EVENT_3729_action_queue_async_49_SUBSCRIPT_set_sprite_sequence_11',
                "command": 'set_sprite_sequence',
                "args": [25, 0, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_3729_action_queue_async_49_SUBSCRIPT_pause_12',
                "command": 'pause',
                "args": [10]
            },
            {
                "identifier": 'EVENT_3729_action_queue_async_49_SUBSCRIPT_reset_properties_13',
                "command": 'reset_properties'
            },
            {
                "identifier": 'EVENT_3729_action_queue_async_49_SUBSCRIPT_pause_14',
                "command": 'pause',
                "args": [8]
            },
            {
                "identifier": 'EVENT_3729_action_queue_async_49_SUBSCRIPT_set_sprite_sequence_15',
                "command": 'set_sprite_sequence',
                "args": [25, 0, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_3729_action_queue_async_49_SUBSCRIPT_pause_16',
                "command": 'pause',
                "args": [8]
            },
            {
                "identifier": 'EVENT_3729_action_queue_async_49_SUBSCRIPT_reset_properties_17',
                "command": 'reset_properties'
            },
            {
                "identifier": 'EVENT_3729_action_queue_async_49_SUBSCRIPT_pause_18',
                "command": 'pause',
                "args": [4]
            },
            {
                "identifier": 'EVENT_3729_action_queue_async_49_SUBSCRIPT_set_sprite_sequence_19',
                "command": 'set_sprite_sequence',
                "args": [0, 0, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3729_action_queue_async_49_SUBSCRIPT_pause_20',
                "command": 'pause',
                "args": [4]
            },
            {
                "identifier": 'EVENT_3729_action_queue_async_49_SUBSCRIPT_set_sprite_sequence_21',
                "command": 'set_sprite_sequence',
                "args": [7, 0, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3729_action_queue_async_49_SUBSCRIPT_pause_22',
                "command": 'pause',
                "args": [50]
            },
            {
                "identifier": 'EVENT_3729_action_queue_async_49_SUBSCRIPT_set_sprite_sequence_23',
                "command": 'set_sprite_sequence',
                "args": [9, 0, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3729_action_queue_async_49_SUBSCRIPT_pause_24',
                "command": 'pause',
                "args": [4]
            },
            {
                "identifier": 'EVENT_3729_action_queue_async_49_SUBSCRIPT_set_sprite_sequence_25',
                "command": 'set_sprite_sequence',
                "args": [8, 0, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3729_action_queue_async_49_SUBSCRIPT_pause_26',
                "command": 'pause',
                "args": [2]
            },
            {
                "identifier": 'EVENT_3729_action_queue_async_49_SUBSCRIPT_reset_properties_27',
                "command": 'reset_properties'
            },
            {
                "identifier": 'EVENT_3729_action_queue_async_49_SUBSCRIPT_set_animation_speed_28',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.SLOW, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_3729_action_queue_async_49_SUBSCRIPT_set_animation_speed_29',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3729_action_queue_async_49_SUBSCRIPT_sequence_looping_on_30',
                "command": 'sequence_looping_on'
            },
            {
                "identifier": 'EVENT_3729_action_queue_async_49_SUBSCRIPT_walk_1_step_southeast_31',
                "command": 'walk_1_step_southeast'
            },
            {
                "identifier": 'EVENT_3729_action_queue_async_49_SUBSCRIPT_sequence_looping_off_32',
                "command": 'sequence_looping_off'
            },
            {
                "identifier": 'EVENT_3729_action_queue_async_49_SUBSCRIPT_set_sprite_sequence_33',
                "command": 'set_sprite_sequence',
                "args": [13, 0, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_3729_action_queue_async_49_SUBSCRIPT_pause_34',
                "command": 'pause',
                "args": [8]
            },
            {
                "identifier": 'EVENT_3729_action_queue_async_49_SUBSCRIPT_reset_properties_35',
                "command": 'reset_properties'
            }
        ]
    },
    {
        "identifier": 'EVENT_3729_pause_50',
        "command": 'pause',
        "args": [30]
    },
    {
        "identifier": 'EVENT_3729_action_queue_sync_51',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_7],
        "subscript": [
            {
                "identifier": 'EVENT_3729_action_queue_sync_51_SUBSCRIPT_reset_properties_0',
                "command": 'reset_properties'
            },
            {
                "identifier": 'EVENT_3729_action_queue_sync_51_SUBSCRIPT_pause_1',
                "command": 'pause',
                "args": [4]
            },
            {
                "identifier": 'EVENT_3729_action_queue_sync_51_SUBSCRIPT_face_northwest_2',
                "command": 'face_northwest'
            },
            {
                "identifier": 'EVENT_3729_action_queue_sync_51_SUBSCRIPT_pause_3',
                "command": 'pause',
                "args": [60]
            },
            {
                "identifier": 'EVENT_3729_action_queue_sync_51_SUBSCRIPT_add_z_coord_1_step_4',
                "command": 'add_z_coord_1_step'
            },
            {
                "identifier": 'EVENT_3729_action_queue_sync_51_SUBSCRIPT_set_animation_speed_5',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_3729_action_queue_sync_51_SUBSCRIPT_shift_z_down_pixels_6',
                "command": 'shift_z_down_pixels',
                "args": [6]
            },
            {
                "identifier": 'EVENT_3729_action_queue_sync_51_SUBSCRIPT_set_animation_speed_7',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_3729_action_queue_sync_51_SUBSCRIPT_shift_z_down_pixels_8',
                "command": 'shift_z_down_pixels',
                "args": [10]
            },
            {
                "identifier": 'EVENT_3729_action_queue_sync_51_SUBSCRIPT_sequence_playback_on_9',
                "command": 'sequence_playback_on'
            },
            {
                "identifier": 'EVENT_3729_action_queue_sync_51_SUBSCRIPT_pause_10',
                "command": 'pause',
                "args": [60]
            },
            {
                "identifier": 'EVENT_3729_action_queue_sync_51_SUBSCRIPT_face_southwest_11',
                "command": 'face_southwest'
            },
            {
                "identifier": 'EVENT_3729_action_queue_sync_51_SUBSCRIPT_pause_12',
                "command": 'pause',
                "args": [2]
            },
            {
                "identifier": 'EVENT_3729_action_queue_sync_51_SUBSCRIPT_set_sprite_sequence_13',
                "command": 'set_sprite_sequence',
                "args": [2, 0, [_0x08Flags.READ_AS_SEQUENCE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_3729_action_queue_sync_52',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_9],
        "subscript": [
            {
                "identifier": 'EVENT_3729_action_queue_sync_52_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [84]
            },
            {
                "identifier": 'EVENT_3729_action_queue_sync_52_SUBSCRIPT_set_sprite_sequence_1',
                "command": 'set_sprite_sequence',
                "args": [22, 0, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_3729_action_queue_sync_52_SUBSCRIPT_pause_2',
                "command": 'pause',
                "args": [4]
            },
            {
                "identifier": 'EVENT_3729_action_queue_sync_52_SUBSCRIPT_set_sprite_sequence_3',
                "command": 'set_sprite_sequence',
                "args": [23, 0, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_3729_action_queue_sync_52_SUBSCRIPT_pause_4',
                "command": 'pause',
                "args": [2]
            },
            {
                "identifier": 'EVENT_3729_action_queue_sync_52_SUBSCRIPT_set_sprite_sequence_5',
                "command": 'set_sprite_sequence',
                "args": [24, 0, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_3729_action_queue_sync_52_SUBSCRIPT_pause_6',
                "command": 'pause',
                "args": [4]
            },
            {
                "identifier": 'EVENT_3729_action_queue_sync_52_SUBSCRIPT_start_loop_n_times_7',
                "command": 'start_loop_n_times',
                "args": [1]
            },
            {
                "identifier": 'EVENT_3729_action_queue_sync_52_SUBSCRIPT_set_sprite_sequence_8',
                "command": 'set_sprite_sequence',
                "args": [22, 0, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_3729_action_queue_sync_52_SUBSCRIPT_pause_9',
                "command": 'pause',
                "args": [2]
            },
            {
                "identifier": 'EVENT_3729_action_queue_sync_52_SUBSCRIPT_set_sprite_sequence_10',
                "command": 'set_sprite_sequence',
                "args": [23, 0, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_3729_action_queue_sync_52_SUBSCRIPT_pause_11',
                "command": 'pause',
                "args": [2]
            },
            {
                "identifier": 'EVENT_3729_action_queue_sync_52_SUBSCRIPT_set_sprite_sequence_12',
                "command": 'set_sprite_sequence',
                "args": [24, 0, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_3729_action_queue_sync_52_SUBSCRIPT_pause_13',
                "command": 'pause',
                "args": [4]
            },
            {
                "identifier": 'EVENT_3729_action_queue_sync_52_SUBSCRIPT_end_loop_14',
                "command": 'end_loop'
            },
            {
                "identifier": 'EVENT_3729_action_queue_sync_52_SUBSCRIPT_set_sprite_sequence_15',
                "command": 'set_sprite_sequence',
                "args": [0, 0, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_3729_pause_53',
        "command": 'pause',
        "args": [30]
    },
    {
        "identifier": 'EVENT_3729_run_dialog_54',
        "command": 'run_dialog',
        "args": [3624, AreaObjects.NPC_14, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_3729_remember_last_object_55',
        "command": 'remember_last_object'
    },
    {
        "identifier": 'EVENT_3729_pause_56',
        "command": 'pause',
        "args": [120]
    },
    {
        "identifier": 'EVENT_3729_action_queue_sync_57',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_9],
        "subscript": [
            {
                "identifier": 'EVENT_3729_action_queue_sync_57_SUBSCRIPT_set_sprite_sequence_0',
                "command": 'set_sprite_sequence',
                "args": [13, 0, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_3729_action_queue_sync_57_SUBSCRIPT_pause_1',
                "command": 'pause',
                "args": [8]
            },
            {
                "identifier": 'EVENT_3729_action_queue_sync_57_SUBSCRIPT_reset_properties_2',
                "command": 'reset_properties'
            },
            {
                "identifier": 'EVENT_3729_action_queue_sync_57_SUBSCRIPT_pause_3',
                "command": 'pause',
                "args": [20]
            },
            {
                "identifier": 'EVENT_3729_action_queue_sync_57_SUBSCRIPT_set_sprite_sequence_4',
                "command": 'set_sprite_sequence',
                "args": [13, 0, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_3729_action_queue_sync_57_SUBSCRIPT_pause_5',
                "command": 'pause',
                "args": [8]
            },
            {
                "identifier": 'EVENT_3729_action_queue_sync_57_SUBSCRIPT_reset_properties_6',
                "command": 'reset_properties'
            }
        ]
    },
    {
        "identifier": 'EVENT_3729_remember_last_object_58',
        "command": 'remember_last_object'
    },
    {
        "identifier": 'EVENT_3729_action_queue_async_59',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_7],
        "subscript": [
            {
                "identifier": 'EVENT_3729_action_queue_async_59_SUBSCRIPT_reset_properties_0',
                "command": 'reset_properties'
            },
            {
                "identifier": 'EVENT_3729_action_queue_async_59_SUBSCRIPT_pause_1',
                "command": 'pause',
                "args": [4]
            },
            {
                "identifier": 'EVENT_3729_action_queue_async_59_SUBSCRIPT_face_northwest_2',
                "command": 'face_northwest'
            }
        ]
    },
    {
        "identifier": 'EVENT_3729_run_dialog_60',
        "command": 'run_dialog',
        "args": [3625, AreaObjects.NPC_14, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_3729_action_queue_async_61',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_9],
        "subscript": [
            {
                "identifier": 'EVENT_3729_action_queue_async_61_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [30]
            },
            {
                "identifier": 'EVENT_3729_action_queue_async_61_SUBSCRIPT_set_sprite_sequence_1',
                "command": 'set_sprite_sequence',
                "args": [25, 0, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_3729_pause_62',
        "command": 'pause',
        "args": [60]
    },
    {
        "identifier": 'EVENT_3729_action_queue_sync_63',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_7],
        "subscript": [
            {
                "identifier": 'EVENT_3729_action_queue_sync_63_SUBSCRIPT_face_southwest_0',
                "command": 'face_southwest'
            }
        ]
    },
    {
        "identifier": 'EVENT_3729_action_queue_sync_64',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_8],
        "subscript": [
            {
                "identifier": 'EVENT_3729_action_queue_sync_64_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [30]
            },
            {
                "identifier": 'EVENT_3729_action_queue_sync_64_SUBSCRIPT_set_sprite_sequence_1',
                "command": 'set_sprite_sequence',
                "args": [6, 0, [_0x08Flags.READ_AS_SEQUENCE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_3729_action_queue_sync_65',
        "command": 'action_queue_sync',
        "args": [AreaObjects.SCREEN_FOCUS],
        "subscript": [
            {
                "identifier": 'EVENT_3729_action_queue_sync_65_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_3729_action_queue_sync_65_SUBSCRIPT_shift_southwest_steps_1',
                "command": 'shift_southwest_steps',
                "args": [11]
            }
        ]
    },
    {
        "identifier": 'EVENT_3729_pause_66',
        "command": 'pause',
        "args": [30]
    },
    {
        "identifier": 'EVENT_3729_run_dialog_67',
        "command": 'run_dialog',
        "args": [3626, AreaObjects.NPC_14, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_3729_remember_last_object_68',
        "command": 'remember_last_object'
    },
    {
        "identifier": 'EVENT_3729_pause_69',
        "command": 'pause',
        "args": [10]
    },
    {
        "identifier": 'EVENT_3729_action_queue_sync_70',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_3729_action_queue_sync_70_SUBSCRIPT_walk_1_step_southeast_0',
                "command": 'walk_1_step_southeast'
            },
            {
                "identifier": 'EVENT_3729_action_queue_sync_70_SUBSCRIPT_face_northeast_1',
                "command": 'face_northeast'
            }
        ]
    },
    {
        "identifier": 'EVENT_3729_action_queue_async_71',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_6],
        "subscript": [
            {
                "identifier": 'EVENT_3729_action_queue_async_71_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [12]
            },
            {
                "identifier": 'EVENT_3729_action_queue_async_71_SUBSCRIPT_visibility_off_1',
                "command": 'visibility_off'
            },
            {
                "identifier": 'EVENT_3729_action_queue_async_71_SUBSCRIPT_transfer_to_xyzf_2',
                "command": 'transfer_to_xyzf',
                "args": [1, 63, 0, RadialDirections.EAST]
            },
            {
                "identifier": 'EVENT_3729_action_queue_async_71_SUBSCRIPT_transfer_xyzf_pixels_3',
                "command": 'transfer_xyzf_pixels',
                "args": [8, 4, 0, RadialDirections.EAST]
            },
            {
                "identifier": 'EVENT_3729_action_queue_async_71_SUBSCRIPT_set_animation_speed_4',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3729_action_queue_async_71_SUBSCRIPT_face_northwest_5',
                "command": 'face_northwest'
            },
            {
                "identifier": 'EVENT_3729_action_queue_async_71_SUBSCRIPT_visibility_on_6',
                "command": 'visibility_on'
            },
            {
                "identifier": 'EVENT_3729_action_queue_async_71_SUBSCRIPT_shift_northwest_pixels_7',
                "command": 'shift_northwest_pixels',
                "args": [12]
            },
            {
                "identifier": 'EVENT_3729_action_queue_async_71_SUBSCRIPT_face_northeast_8',
                "command": 'face_northeast'
            },
            {
                "identifier": 'EVENT_3729_action_queue_async_71_SUBSCRIPT_set_animation_speed_9',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3729_action_queue_async_71_SUBSCRIPT_set_sprite_sequence_10',
                "command": 'set_sprite_sequence',
                "args": [5, 0, [_0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_3729_pause_72',
        "command": 'pause',
        "args": [10]
    },
    {
        "identifier": 'EVENT_3729_run_dialog_73',
        "command": 'run_dialog',
        "args": [3627, AreaObjects.NPC_12, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_3729_pause_74',
        "command": 'pause',
        "args": [10]
    },
    {
        "identifier": 'EVENT_3729_action_queue_sync_75',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_6],
        "subscript": [
            {
                "identifier": 'EVENT_3729_action_queue_sync_75_SUBSCRIPT_set_sprite_sequence_0',
                "command": 'set_sprite_sequence',
                "args": [12, 0, [_0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_3729_action_queue_sync_75_SUBSCRIPT_shift_northeast_steps_1',
                "command": 'shift_northeast_steps',
                "args": [3]
            },
            {
                "identifier": 'EVENT_3729_action_queue_sync_75_SUBSCRIPT_set_solidity_bits_2',
                "command": 'set_solidity_bits',
                "args": [[_0x0AFlags.CANT_PASS_WALLS]]
            },
            {
                "identifier": 'EVENT_3729_action_queue_sync_75_SUBSCRIPT_floating_on_3',
                "command": 'floating_on'
            },
            {
                "identifier": 'EVENT_3729_action_queue_sync_75_SUBSCRIPT_shift_northeast_steps_4',
                "command": 'shift_northeast_steps',
                "args": [2]
            },
            {
                "identifier": 'EVENT_3729_action_queue_sync_75_SUBSCRIPT_shift_northeast_pixels_5',
                "command": 'shift_northeast_pixels',
                "args": [8]
            },
            {
                "identifier": 'EVENT_3729_action_queue_sync_75_SUBSCRIPT_set_sprite_sequence_6',
                "command": 'set_sprite_sequence',
                "args": [8, 1, [_0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3729_action_queue_sync_75_SUBSCRIPT_play_sound_7',
                "command": 'play_sound',
                "args": [Sounds._022_CLOSE_DOOR, 4]
            },
            {
                "identifier": 'EVENT_3729_action_queue_sync_75_SUBSCRIPT_set_animation_speed_8',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.SLOW, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_3729_action_queue_sync_75_SUBSCRIPT_shift_northeast_pixels_9',
                "command": 'shift_northeast_pixels',
                "args": [4]
            },
            {
                "identifier": 'EVENT_3729_action_queue_sync_75_SUBSCRIPT_set_animation_speed_10',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_SLOW, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_3729_action_queue_sync_75_SUBSCRIPT_shift_northeast_pixels_11',
                "command": 'shift_northeast_pixels',
                "args": [4]
            },
            {
                "identifier": 'EVENT_3729_action_queue_sync_75_SUBSCRIPT_pause_12',
                "command": 'pause',
                "args": [60]
            },
            {
                "identifier": 'EVENT_3729_action_queue_sync_75_SUBSCRIPT_set_sprite_sequence_13',
                "command": 'set_sprite_sequence',
                "args": [15, 1, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3729_action_queue_sync_75_SUBSCRIPT_pause_14',
                "command": 'pause',
                "args": [60]
            },
            {
                "identifier": 'EVENT_3729_action_queue_sync_75_SUBSCRIPT_reset_properties_15',
                "command": 'reset_properties'
            }
        ]
    },
    {
        "identifier": 'EVENT_3729_action_queue_sync_76',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_3729_action_queue_sync_76_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [88]
            },
            {
                "identifier": 'EVENT_3729_action_queue_sync_76_SUBSCRIPT_shift_northeast_steps_1',
                "command": 'shift_northeast_steps',
                "args": [6]
            },
            {
                "identifier": 'EVENT_3729_action_queue_sync_76_SUBSCRIPT_face_northwest_2',
                "command": 'face_northwest'
            },
            {
                "identifier": 'EVENT_3729_action_queue_sync_76_SUBSCRIPT_set_sprite_sequence_3',
                "command": 'set_sprite_sequence',
                "args": [0, 6, [_0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_3729_action_queue_sync_76_SUBSCRIPT_pause_4',
                "command": 'pause',
                "args": [60]
            },
            {
                "identifier": 'EVENT_3729_action_queue_sync_76_SUBSCRIPT_reset_properties_5',
                "command": 'reset_properties'
            }
        ]
    },
    {
        "identifier": 'EVENT_3729_action_queue_sync_77',
        "command": 'action_queue_sync',
        "args": [AreaObjects.SCREEN_FOCUS],
        "subscript": [
            {
                "identifier": 'EVENT_3729_action_queue_sync_77_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.SLOW, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_3729_action_queue_sync_77_SUBSCRIPT_shift_northeast_steps_1',
                "command": 'shift_northeast_steps',
                "args": [8]
            }
        ]
    },
    {
        "identifier": 'EVENT_3729_pause_78',
        "command": 'pause',
        "args": [88]
    },
    {
        "identifier": 'EVENT_3729_run_dialog_79',
        "command": 'run_dialog',
        "args": [2530, AreaObjects.NPC_14, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_3729_remember_last_object_80',
        "command": 'remember_last_object'
    },
    {
        "identifier": 'EVENT_3729_action_queue_sync_81',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_8],
        "subscript": [
            {
                "identifier": 'EVENT_3729_action_queue_sync_81_SUBSCRIPT_set_sprite_sequence_0',
                "command": 'set_sprite_sequence',
                "args": [6, 0, [_0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_3729_action_queue_sync_81_SUBSCRIPT_set_animation_speed_1',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.SLOW, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_3729_action_queue_sync_81_SUBSCRIPT_walk_1_step_northwest_2',
                "command": 'walk_1_step_northwest'
            }
        ]
    },
    {
        "identifier": 'EVENT_3729_action_queue_async_82',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_7],
        "subscript": [
            {
                "identifier": 'EVENT_3729_action_queue_async_82_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.SLOW, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_3729_action_queue_async_82_SUBSCRIPT_set_animation_speed_1',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3729_action_queue_async_82_SUBSCRIPT_walk_1_step_southwest_2',
                "command": 'walk_1_step_southwest'
            }
        ]
    },
    {
        "identifier": 'EVENT_3729_pause_83',
        "command": 'pause',
        "args": [10]
    },
    {
        "identifier": 'EVENT_3729_action_queue_sync_84',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_3729_action_queue_sync_84_SUBSCRIPT_face_northeast_0',
                "command": 'face_northeast'
            }
        ]
    },
    {
        "identifier": 'EVENT_3729_run_dialog_85',
        "command": 'run_dialog',
        "args": [3628, AreaObjects.NPC_12, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_3729_pause_86',
        "command": 'pause',
        "args": [10]
    },
    {
        "identifier": 'EVENT_3729_action_queue_async_87',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_6],
        "subscript": [
            {
                "identifier": 'EVENT_3729_action_queue_async_87_SUBSCRIPT_set_sprite_sequence_0',
                "command": 'set_sprite_sequence',
                "args": [5, 0, [_0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_3729_pause_88',
        "command": 'pause',
        "args": [10]
    },
    {
        "identifier": 'EVENT_3729_run_dialog_89',
        "command": 'run_dialog',
        "args": [3629, AreaObjects.NPC_14, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_3729_pause_90',
        "command": 'pause',
        "args": [10]
    },
    {
        "identifier": 'EVENT_3729_action_queue_sync_91',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_6],
        "subscript": [
            {
                "identifier": 'EVENT_3729_action_queue_sync_91_SUBSCRIPT_reset_properties_0',
                "command": 'reset_properties'
            }
        ]
    },
    {
        "identifier": 'EVENT_3729_pause_92',
        "command": 'pause',
        "args": [30]
    },
    {
        "identifier": 'EVENT_3729_action_queue_async_93',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_7],
        "subscript": [
            {
                "identifier": 'EVENT_3729_action_queue_async_93_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_3729_action_queue_async_93_SUBSCRIPT_fixed_f_coord_on_1',
                "command": 'fixed_f_coord_on'
            },
            {
                "identifier": 'EVENT_3729_action_queue_async_93_SUBSCRIPT_sequence_playback_off_2',
                "command": 'sequence_playback_off'
            },
            {
                "identifier": 'EVENT_3729_action_queue_async_93_SUBSCRIPT_shift_northeast_pixels_3',
                "command": 'shift_northeast_pixels',
                "args": [6]
            },
            {
                "identifier": 'EVENT_3729_action_queue_async_93_SUBSCRIPT_shift_southwest_pixels_4',
                "command": 'shift_southwest_pixels',
                "args": [6]
            },
            {
                "identifier": 'EVENT_3729_action_queue_async_93_SUBSCRIPT_fixed_f_coord_off_5',
                "command": 'fixed_f_coord_off'
            },
            {
                "identifier": 'EVENT_3729_action_queue_async_93_SUBSCRIPT_sequence_playback_on_6',
                "command": 'sequence_playback_on'
            }
        ]
    },
    {
        "identifier": 'EVENT_3729_pause_94',
        "command": 'pause',
        "args": [10]
    },
    {
        "identifier": 'EVENT_3729_run_dialog_95',
        "command": 'run_dialog',
        "args": [3630, AreaObjects.NPC_12, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_3729_pause_96',
        "command": 'pause',
        "args": [10]
    },
    {
        "identifier": 'EVENT_3729_action_queue_sync_97',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_3729_action_queue_sync_97_SUBSCRIPT_face_north_0',
                "command": 'face_north'
            },
            {
                "identifier": 'EVENT_3729_action_queue_sync_97_SUBSCRIPT_pause_1',
                "command": 'pause',
                "args": [2]
            },
            {
                "identifier": 'EVENT_3729_action_queue_sync_97_SUBSCRIPT_face_northwest_2',
                "command": 'face_northwest'
            },
            {
                "identifier": 'EVENT_3729_action_queue_sync_97_SUBSCRIPT_pause_3',
                "command": 'pause',
                "args": [2]
            },
            {
                "identifier": 'EVENT_3729_action_queue_sync_97_SUBSCRIPT_face_west_4',
                "command": 'face_west'
            },
            {
                "identifier": 'EVENT_3729_action_queue_sync_97_SUBSCRIPT_pause_5',
                "command": 'pause',
                "args": [2]
            },
            {
                "identifier": 'EVENT_3729_action_queue_sync_97_SUBSCRIPT_face_southwest_6',
                "command": 'face_southwest'
            }
        ]
    },
    {
        "identifier": 'EVENT_3729_action_queue_async_98',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_6],
        "subscript": [
            {
                "identifier": 'EVENT_3729_action_queue_async_98_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [4]
            },
            {
                "identifier": 'EVENT_3729_action_queue_async_98_SUBSCRIPT_face_southeast_1',
                "command": 'face_southeast'
            },
            {
                "identifier": 'EVENT_3729_action_queue_async_98_SUBSCRIPT_pause_2',
                "command": 'pause',
                "args": [2]
            },
            {
                "identifier": 'EVENT_3729_action_queue_async_98_SUBSCRIPT_set_sprite_sequence_3',
                "command": 'set_sprite_sequence',
                "args": [6, 2, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_3729_pause_99',
        "command": 'pause',
        "args": [10]
    },
    {
        "identifier": 'EVENT_3729_run_dialog_100',
        "command": 'run_dialog',
        "args": [3631, AreaObjects.NPC_12, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_3729_pause_101',
        "command": 'pause',
        "args": [10]
    },
    {
        "identifier": 'EVENT_3729_set_action_script_async_102',
        "command": 'set_action_script_async',
        "args": [AreaObjects.MARIO, 670]
    },
    {
        "identifier": 'EVENT_3729_pause_103',
        "command": 'pause',
        "args": [10]
    },
    {
        "identifier": 'EVENT_3729_action_queue_sync_104',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_6],
        "subscript": [
            {
                "identifier": 'EVENT_3729_action_queue_sync_104_SUBSCRIPT_reset_properties_0',
                "command": 'reset_properties'
            },
            {
                "identifier": 'EVENT_3729_action_queue_sync_104_SUBSCRIPT_pause_1',
                "command": 'pause',
                "args": [2]
            },
            {
                "identifier": 'EVENT_3729_action_queue_sync_104_SUBSCRIPT_face_northeast_2',
                "command": 'face_northeast'
            }
        ]
    },
    {
        "identifier": 'EVENT_3729_action_queue_sync_105',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_3729_action_queue_sync_105_SUBSCRIPT_face_west_0',
                "command": 'face_west'
            },
            {
                "identifier": 'EVENT_3729_action_queue_sync_105_SUBSCRIPT_pause_1',
                "command": 'pause',
                "args": [2]
            },
            {
                "identifier": 'EVENT_3729_action_queue_sync_105_SUBSCRIPT_face_northwest_2',
                "command": 'face_northwest'
            },
            {
                "identifier": 'EVENT_3729_action_queue_sync_105_SUBSCRIPT_pause_3',
                "command": 'pause',
                "args": [2]
            },
            {
                "identifier": 'EVENT_3729_action_queue_sync_105_SUBSCRIPT_face_north_4',
                "command": 'face_north'
            },
            {
                "identifier": 'EVENT_3729_action_queue_sync_105_SUBSCRIPT_pause_5',
                "command": 'pause',
                "args": [2]
            },
            {
                "identifier": 'EVENT_3729_action_queue_sync_105_SUBSCRIPT_face_northeast_6',
                "command": 'face_northeast'
            }
        ]
    },
    {
        "identifier": 'EVENT_3729_remember_last_object_106',
        "command": 'remember_last_object'
    },
    {
        "identifier": 'EVENT_3729_pause_107',
        "command": 'pause',
        "args": [10]
    },
    {
        "identifier": 'EVENT_3729_run_dialog_108',
        "command": 'run_dialog',
        "args": [3632, AreaObjects.NPC_14, [_0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_3729_action_queue_async_109',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_7],
        "subscript": [
            {
                "identifier": 'EVENT_3729_action_queue_async_109_SUBSCRIPT_fixed_f_coord_on_0',
                "command": 'fixed_f_coord_on'
            },
            {
                "identifier": 'EVENT_3729_action_queue_async_109_SUBSCRIPT_sequence_looping_on_1',
                "command": 'sequence_looping_on'
            },
            {
                "identifier": 'EVENT_3729_action_queue_async_109_SUBSCRIPT_set_animation_speed_2',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_SLOW, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_3729_action_queue_async_109_SUBSCRIPT_shift_northeast_pixels_3',
                "command": 'shift_northeast_pixels',
                "args": [8]
            },
            {
                "identifier": 'EVENT_3729_action_queue_async_109_SUBSCRIPT_sequence_looping_off_4',
                "command": 'sequence_looping_off'
            },
            {
                "identifier": 'EVENT_3729_action_queue_async_109_SUBSCRIPT_pause_5',
                "command": 'pause',
                "args": [30]
            },
            {
                "identifier": 'EVENT_3729_action_queue_async_109_SUBSCRIPT_set_animation_speed_6',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.SLOW, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_3729_action_queue_async_109_SUBSCRIPT_sequence_looping_on_7',
                "command": 'sequence_looping_on'
            },
            {
                "identifier": 'EVENT_3729_action_queue_async_109_SUBSCRIPT_shift_northeast_pixels_8',
                "command": 'shift_northeast_pixels',
                "args": [8]
            },
            {
                "identifier": 'EVENT_3729_action_queue_async_109_SUBSCRIPT_sequence_looping_off_9',
                "command": 'sequence_looping_off'
            }
        ]
    },
    {
        "identifier": 'EVENT_3729_action_queue_async_110',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_9],
        "subscript": [
            {
                "identifier": 'EVENT_3729_action_queue_async_110_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [60]
            },
            {
                "identifier": 'EVENT_3729_action_queue_async_110_SUBSCRIPT_set_sprite_sequence_1',
                "command": 'set_sprite_sequence',
                "args": [0, 0, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_3729_unsync_dialog_111',
        "command": 'unsync_dialog'
    },
    {
        "identifier": 'EVENT_3729_action_queue_sync_112',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_7],
        "subscript": [
            {
                "identifier": 'EVENT_3729_action_queue_sync_112_SUBSCRIPT_fixed_f_coord_off_0',
                "command": 'fixed_f_coord_off'
            },
            {
                "identifier": 'EVENT_3729_action_queue_sync_112_SUBSCRIPT_set_animation_speed_1',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_3729_action_queue_sync_112_SUBSCRIPT_set_animation_speed_2',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3729_action_queue_sync_112_SUBSCRIPT_shift_northeast_steps_3',
                "command": 'shift_northeast_steps',
                "args": [4]
            },
            {
                "identifier": 'EVENT_3729_action_queue_sync_112_SUBSCRIPT_shift_northwest_steps_4',
                "command": 'shift_northwest_steps',
                "args": [2]
            }
        ]
    },
    {
        "identifier": 'EVENT_3729_action_queue_sync_113',
        "command": 'action_queue_sync',
        "args": [AreaObjects.SCREEN_FOCUS],
        "subscript": [
            {
                "identifier": 'EVENT_3729_action_queue_sync_113_SUBSCRIPT_shift_northeast_steps_0',
                "command": 'shift_northeast_steps',
                "args": [3]
            }
        ]
    },
    {
        "identifier": 'EVENT_3729_action_queue_sync_114',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_9],
        "subscript": [
            {
                "identifier": 'EVENT_3729_action_queue_sync_114_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [30]
            },
            {
                "identifier": 'EVENT_3729_action_queue_sync_114_SUBSCRIPT_set_sprite_sequence_1',
                "command": 'set_sprite_sequence',
                "args": [3, 0, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_3729_action_queue_sync_115',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_8],
        "subscript": [
            {
                "identifier": 'EVENT_3729_action_queue_sync_115_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [30]
            },
            {
                "identifier": 'EVENT_3729_action_queue_sync_115_SUBSCRIPT_set_sprite_sequence_1',
                "command": 'set_sprite_sequence',
                "args": [1, 0, [_0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_3729_run_dialog_116',
        "command": 'run_dialog',
        "args": [3633, AreaObjects.NPC_14, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_3729_remember_last_object_117',
        "command": 'remember_last_object'
    },
    {
        "identifier": 'EVENT_3729_play_sound_118',
        "command": 'play_sound',
        "args": [Sounds._016_OPEN_DOOR, 6]
    },
    {
        "identifier": 'EVENT_3729_apply_tile_mod_119',
        "command": 'apply_tile_mod',
        "args": [Rooms._120_NIMBUS_CASTLE_AREA_13_THRONE_ROOM_DURING_VALENTINA, 0, [_0x6AFlags.USE_ALTERNATE]]
    },
    {
        "identifier": 'EVENT_3729_apply_solidity_mod_120',
        "command": 'apply_solidity_mod',
        "args": [Rooms._120_NIMBUS_CASTLE_AREA_13_THRONE_ROOM_DURING_VALENTINA, 0, [_0x6BFlags.PERMANENT]]
    },
    {
        "identifier": 'EVENT_3729_action_queue_async_121',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_7],
        "subscript": [
            {
                "identifier": 'EVENT_3729_action_queue_async_121_SUBSCRIPT_walk_1_step_northwest_0',
                "command": 'walk_1_step_northwest'
            }
        ]
    },
    {
        "identifier": 'EVENT_3729_remove_from_current_level_122',
        "command": 'remove_from_current_level',
        "args": [AreaObjects.NPC_7]
    },
    {
        "identifier": 'EVENT_3729_remove_from_level_123',
        "command": 'remove_from_level',
        "args": [AreaObjects.NPC_7, Rooms._120_NIMBUS_CASTLE_AREA_13_THRONE_ROOM_DURING_VALENTINA]
    },
    {
        "identifier": 'EVENT_3729_pause_124',
        "command": 'pause',
        "args": [30]
    },
    {
        "identifier": 'EVENT_3729_run_dialog_125',
        "command": 'run_dialog',
        "args": [3635, AreaObjects.NPC_14, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_3729_pause_126',
        "command": 'pause',
        "args": [10]
    },
    {
        "identifier": 'EVENT_3729_run_dialog_127',
        "command": 'run_dialog',
        "args": [3636, AreaObjects.NPC_14, [_0x60Flags.CLOSABLE, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_3729_action_queue_sync_128',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_8],
        "subscript": [
            {
                "identifier": 'EVENT_3729_action_queue_sync_128_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING, _0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3729_action_queue_sync_128_SUBSCRIPT_set_sprite_sequence_1',
                "command": 'set_sprite_sequence',
                "args": [1, 0, [_0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_3729_action_queue_sync_128_SUBSCRIPT_shift_northeast_steps_2',
                "command": 'shift_northeast_steps',
                "args": [1]
            },
            {
                "identifier": 'EVENT_3729_action_queue_sync_128_SUBSCRIPT_set_vram_priority_3',
                "command": 'set_vram_priority',
                "args": [VramPriority.PRIORITY_3]
            },
            {
                "identifier": 'EVENT_3729_action_queue_sync_128_SUBSCRIPT_shift_northeast_steps_4',
                "command": 'shift_northeast_steps',
                "args": [5]
            },
            {
                "identifier": 'EVENT_3729_action_queue_sync_128_SUBSCRIPT_set_vram_priority_5',
                "command": 'set_vram_priority',
                "args": [VramPriority.NORMAL]
            },
            {
                "identifier": 'EVENT_3729_action_queue_sync_128_SUBSCRIPT_set_sprite_sequence_6',
                "command": 'set_sprite_sequence',
                "args": [1, 0, [_0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3729_action_queue_sync_128_SUBSCRIPT_walk_1_step_northwest_7',
                "command": 'walk_1_step_northwest'
            },
            {
                "identifier": 'EVENT_3729_action_queue_sync_128_SUBSCRIPT_shift_northwest_pixels_8',
                "command": 'shift_northwest_pixels',
                "args": [8]
            },
            {
                "identifier": 'EVENT_3729_action_queue_sync_128_SUBSCRIPT_visibility_off_9',
                "command": 'visibility_off'
            }
        ]
    },
    {
        "identifier": 'EVENT_3729_action_queue_sync_129',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_9],
        "subscript": [
            {
                "identifier": 'EVENT_3729_action_queue_sync_129_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [30]
            },
            {
                "identifier": 'EVENT_3729_action_queue_sync_129_SUBSCRIPT_set_sprite_sequence_1',
                "command": 'set_sprite_sequence',
                "args": [30, 0, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3729_action_queue_sync_129_SUBSCRIPT_pause_2',
                "command": 'pause',
                "args": [32]
            },
            {
                "identifier": 'EVENT_3729_action_queue_sync_129_SUBSCRIPT_set_sprite_sequence_3',
                "command": 'set_sprite_sequence',
                "args": [3, 0, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_3729_remember_last_object_130',
        "command": 'remember_last_object'
    },
    {
        "identifier": 'EVENT_3729_remove_from_current_level_131',
        "command": 'remove_from_current_level',
        "args": [AreaObjects.NPC_8]
    },
    {
        "identifier": 'EVENT_3729_remove_from_level_132',
        "command": 'remove_from_level',
        "args": [AreaObjects.NPC_8, Rooms._120_NIMBUS_CASTLE_AREA_13_THRONE_ROOM_DURING_VALENTINA]
    },
    {
        "identifier": 'EVENT_3729_pause_133',
        "command": 'pause',
        "args": [30]
    },
    {
        "identifier": 'EVENT_3729_close_dialog_134',
        "command": 'close_dialog'
    },
    {
        "identifier": 'EVENT_3729_action_queue_async_135',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_9],
        "subscript": [
            {
                "identifier": 'EVENT_3729_action_queue_async_135_SUBSCRIPT_set_sprite_sequence_0',
                "command": 'set_sprite_sequence',
                "args": [0, 0, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_3729_action_queue_async_135_SUBSCRIPT_pause_1',
                "command": 'pause',
                "args": [2]
            },
            {
                "identifier": 'EVENT_3729_action_queue_async_135_SUBSCRIPT_set_sprite_sequence_2',
                "command": 'set_sprite_sequence',
                "args": [0, 0, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3729_action_queue_async_135_SUBSCRIPT_pause_3',
                "command": 'pause',
                "args": [60]
            },
            {
                "identifier": 'EVENT_3729_action_queue_async_135_SUBSCRIPT_set_animation_speed_4',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3729_action_queue_async_135_SUBSCRIPT_set_animation_speed_5',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.SLOW, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_3729_action_queue_async_135_SUBSCRIPT_set_sprite_sequence_6',
                "command": 'set_sprite_sequence',
                "args": [0, 0, [_0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3729_action_queue_async_135_SUBSCRIPT_walk_1_step_northeast_7',
                "command": 'walk_1_step_northeast'
            },
            {
                "identifier": 'EVENT_3729_action_queue_async_135_SUBSCRIPT_set_sprite_sequence_8',
                "command": 'set_sprite_sequence',
                "args": [0, 0, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3729_action_queue_async_135_SUBSCRIPT_pause_9',
                "command": 'pause',
                "args": [30]
            },
            {
                "identifier": 'EVENT_3729_action_queue_async_135_SUBSCRIPT_set_animation_speed_10',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_3729_action_queue_async_135_SUBSCRIPT_set_sprite_sequence_11',
                "command": 'set_sprite_sequence',
                "args": [0, 0, [_0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3729_action_queue_async_135_SUBSCRIPT_walk_1_step_northeast_12',
                "command": 'walk_1_step_northeast'
            },
            {
                "identifier": 'EVENT_3729_action_queue_async_135_SUBSCRIPT_set_sprite_sequence_13',
                "command": 'set_sprite_sequence',
                "args": [0, 0, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3729_action_queue_async_135_SUBSCRIPT_set_animation_speed_14',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING, _0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3729_action_queue_async_135_SUBSCRIPT_set_sprite_sequence_15',
                "command": 'set_sprite_sequence',
                "args": [0, 0, [_0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3729_action_queue_async_135_SUBSCRIPT_shift_northeast_steps_16',
                "command": 'shift_northeast_steps',
                "args": [3]
            },
            {
                "identifier": 'EVENT_3729_action_queue_async_135_SUBSCRIPT_jmp_17',
                "command": 'jmp',
                "args": ['EVENT_3729_non_embedded_action_queue_137']
            }
        ]
    },
    {
        "identifier": 'EVENT_3729_jmp_136',
        "command": 'jmp',
        "args": ['EVENT_3729_remove_from_current_level_138']
    },
    {
        "identifier": 'EVENT_3729_non_embedded_action_queue_137',
        "command": 'non_embedded_action_queue',
        "subscript": [
            {
                "identifier": 'EVENT_3729_non_embedded_action_queue_137_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_3729_non_embedded_action_queue_137_SUBSCRIPT_set_sprite_sequence_1',
                "command": 'set_sprite_sequence',
                "args": [14, 0, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3729_non_embedded_action_queue_137_SUBSCRIPT_shift_southwest_pixels_2',
                "command": 'shift_southwest_pixels',
                "args": [2]
            },
            {
                "identifier": 'EVENT_3729_non_embedded_action_queue_137_SUBSCRIPT_set_sprite_sequence_3',
                "command": 'set_sprite_sequence',
                "args": [15, 0, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3729_non_embedded_action_queue_137_SUBSCRIPT_shift_southwest_pixels_4',
                "command": 'shift_southwest_pixels',
                "args": [2]
            },
            {
                "identifier": 'EVENT_3729_non_embedded_action_queue_137_SUBSCRIPT_set_sprite_sequence_5',
                "command": 'set_sprite_sequence',
                "args": [16, 0, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3729_non_embedded_action_queue_137_SUBSCRIPT_shift_southwest_pixels_6',
                "command": 'shift_southwest_pixels',
                "args": [2]
            },
            {
                "identifier": 'EVENT_3729_non_embedded_action_queue_137_SUBSCRIPT_set_sprite_sequence_7',
                "command": 'set_sprite_sequence',
                "args": [17, 0, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3729_non_embedded_action_queue_137_SUBSCRIPT_shift_southwest_pixels_8',
                "command": 'shift_southwest_pixels',
                "args": [2]
            },
            {
                "identifier": 'EVENT_3729_non_embedded_action_queue_137_SUBSCRIPT_set_sprite_sequence_9',
                "command": 'set_sprite_sequence',
                "args": [18, 0, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3729_non_embedded_action_queue_137_SUBSCRIPT_shift_southwest_pixels_10',
                "command": 'shift_southwest_pixels',
                "args": [2]
            },
            {
                "identifier": 'EVENT_3729_non_embedded_action_queue_137_SUBSCRIPT_set_sprite_sequence_11',
                "command": 'set_sprite_sequence',
                "args": [19, 0, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3729_non_embedded_action_queue_137_SUBSCRIPT_shift_southwest_pixels_12',
                "command": 'shift_southwest_pixels',
                "args": [2]
            },
            {
                "identifier": 'EVENT_3729_non_embedded_action_queue_137_SUBSCRIPT_set_animation_speed_13',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.SLOW, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_3729_non_embedded_action_queue_137_SUBSCRIPT_start_loop_n_times_14',
                "command": 'start_loop_n_times',
                "args": [3]
            },
            {
                "identifier": 'EVENT_3729_non_embedded_action_queue_137_SUBSCRIPT_set_sprite_sequence_15',
                "command": 'set_sprite_sequence',
                "args": [20, 0, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3729_non_embedded_action_queue_137_SUBSCRIPT_shift_southwest_pixels_16',
                "command": 'shift_southwest_pixels',
                "args": [1]
            },
            {
                "identifier": 'EVENT_3729_non_embedded_action_queue_137_SUBSCRIPT_set_sprite_sequence_17',
                "command": 'set_sprite_sequence',
                "args": [21, 0, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3729_non_embedded_action_queue_137_SUBSCRIPT_shift_southwest_pixels_18',
                "command": 'shift_southwest_pixels',
                "args": [1]
            },
            {
                "identifier": 'EVENT_3729_non_embedded_action_queue_137_SUBSCRIPT_end_loop_19',
                "command": 'end_loop'
            },
            {
                "identifier": 'EVENT_3729_non_embedded_action_queue_137_SUBSCRIPT_start_loop_n_times_20',
                "command": 'start_loop_n_times',
                "args": [2]
            },
            {
                "identifier": 'EVENT_3729_non_embedded_action_queue_137_SUBSCRIPT_set_sprite_sequence_21',
                "command": 'set_sprite_sequence',
                "args": [22, 0, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3729_non_embedded_action_queue_137_SUBSCRIPT_pause_22',
                "command": 'pause',
                "args": [2]
            },
            {
                "identifier": 'EVENT_3729_non_embedded_action_queue_137_SUBSCRIPT_set_sprite_sequence_23',
                "command": 'set_sprite_sequence',
                "args": [23, 0, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3729_non_embedded_action_queue_137_SUBSCRIPT_pause_24',
                "command": 'pause',
                "args": [2]
            },
            {
                "identifier": 'EVENT_3729_non_embedded_action_queue_137_SUBSCRIPT_set_sprite_sequence_25',
                "command": 'set_sprite_sequence',
                "args": [24, 0, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3729_non_embedded_action_queue_137_SUBSCRIPT_pause_26',
                "command": 'pause',
                "args": [2]
            },
            {
                "identifier": 'EVENT_3729_non_embedded_action_queue_137_SUBSCRIPT_end_loop_27',
                "command": 'end_loop'
            },
            {
                "identifier": 'EVENT_3729_non_embedded_action_queue_137_SUBSCRIPT_pause_28',
                "command": 'pause',
                "args": [60]
            },
            {
                "identifier": 'EVENT_3729_non_embedded_action_queue_137_SUBSCRIPT_set_sprite_sequence_29',
                "command": 'set_sprite_sequence',
                "args": [0, 0, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3729_non_embedded_action_queue_137_SUBSCRIPT_pause_30',
                "command": 'pause',
                "args": [30]
            },
            {
                "identifier": 'EVENT_3729_non_embedded_action_queue_137_SUBSCRIPT_set_sprite_sequence_31',
                "command": 'set_sprite_sequence',
                "args": [1, 0, [_0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_3729_non_embedded_action_queue_137_SUBSCRIPT_set_animation_speed_32',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_3729_non_embedded_action_queue_137_SUBSCRIPT_shift_northwest_steps_33',
                "command": 'shift_northwest_steps',
                "args": [2]
            },
            {
                "identifier": 'EVENT_3729_non_embedded_action_queue_137_SUBSCRIPT_visibility_off_34',
                "command": 'visibility_off'
            },
            {
                "identifier": 'EVENT_3729_non_embedded_action_queue_137_SUBSCRIPT_ret_35',
                "command": 'ret'
            }
        ]
    },
    {
        "identifier": 'EVENT_3729_remove_from_current_level_138',
        "command": 'remove_from_current_level',
        "args": [AreaObjects.NPC_9]
    },
    {
        "identifier": 'EVENT_3729_remove_from_level_139',
        "command": 'remove_from_level',
        "args": [AreaObjects.NPC_9, Rooms._120_NIMBUS_CASTLE_AREA_13_THRONE_ROOM_DURING_VALENTINA]
    },
    {
        "identifier": 'EVENT_3729_pause_140',
        "command": 'pause',
        "args": [10]
    },
    {
        "identifier": 'EVENT_3729_action_queue_sync_141',
        "command": 'action_queue_sync',
        "args": [AreaObjects.SCREEN_FOCUS],
        "subscript": [
            {
                "identifier": 'EVENT_3729_action_queue_sync_141_SUBSCRIPT_shift_southwest_steps_0',
                "command": 'shift_southwest_steps',
                "args": [4]
            }
        ]
    },
    {
        "identifier": 'EVENT_3729_pause_142',
        "command": 'pause',
        "args": [30]
    },
    {
        "identifier": 'EVENT_3729_action_queue_sync_143',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_6],
        "subscript": [
            {
                "identifier": 'EVENT_3729_action_queue_sync_143_SUBSCRIPT_face_southeast_0',
                "command": 'face_southeast'
            }
        ]
    },
    {
        "identifier": 'EVENT_3729_action_queue_sync_144',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_3729_action_queue_sync_144_SUBSCRIPT_face_northwest_0',
                "command": 'face_northwest'
            }
        ]
    },
    {
        "identifier": 'EVENT_3729_pause_145',
        "command": 'pause',
        "args": [60]
    },
    {
        "identifier": 'EVENT_3729_run_dialog_146',
        "command": 'run_dialog',
        "args": [3637, AreaObjects.NPC_14, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_3729_pause_147',
        "command": 'pause',
        "args": [10]
    },
    {
        "identifier": 'EVENT_3729_remember_last_object_148',
        "command": 'remember_last_object'
    },
    {
        "identifier": 'EVENT_3729_action_queue_async_149',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_6],
        "subscript": [
            {
                "identifier": 'EVENT_3729_action_queue_async_149_SUBSCRIPT_set_sprite_sequence_0',
                "command": 'set_sprite_sequence',
                "args": [12, 0, [_0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_3729_run_dialog_150',
        "command": 'run_dialog',
        "args": [3638, AreaObjects.NPC_14, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_3729_pause_151',
        "command": 'pause',
        "args": [10]
    },
    {
        "identifier": 'EVENT_3729_action_queue_sync_152',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_3729_action_queue_sync_152_SUBSCRIPT_shift_northwest_pixels_0',
                "command": 'shift_northwest_pixels',
                "args": [4]
            },
            {
                "identifier": 'EVENT_3729_action_queue_sync_152_SUBSCRIPT_set_sprite_sequence_1',
                "command": 'set_sprite_sequence',
                "args": [7, 6, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_3729_action_queue_sync_152_SUBSCRIPT_pause_2',
                "command": 'pause',
                "args": [4]
            },
            {
                "identifier": 'EVENT_3729_action_queue_sync_152_SUBSCRIPT_set_sprite_sequence_3',
                "command": 'set_sprite_sequence',
                "args": [6, 6, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_3729_action_queue_sync_152_SUBSCRIPT_pause_4',
                "command": 'pause',
                "args": [2]
            },
            {
                "identifier": 'EVENT_3729_action_queue_sync_152_SUBSCRIPT_set_sprite_sequence_5',
                "command": 'set_sprite_sequence',
                "args": [5, 6, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_3729_action_queue_sync_152_SUBSCRIPT_pause_6',
                "command": 'pause',
                "args": [16]
            },
            {
                "identifier": 'EVENT_3729_action_queue_sync_152_SUBSCRIPT_set_sprite_sequence_7',
                "command": 'set_sprite_sequence',
                "args": [4, 6, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_3729_action_queue_sync_153',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_6],
        "subscript": [
            {
                "identifier": 'EVENT_3729_action_queue_sync_153_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [10]
            },
            {
                "identifier": 'EVENT_3729_action_queue_sync_153_SUBSCRIPT_set_animation_speed_1',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_3729_action_queue_sync_153_SUBSCRIPT_shift_southeast_pixels_2',
                "command": 'shift_southeast_pixels',
                "args": [2]
            },
            {
                "identifier": 'EVENT_3729_action_queue_sync_153_SUBSCRIPT_set_animation_speed_3',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.SLOW, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_3729_action_queue_sync_153_SUBSCRIPT_shift_southeast_pixels_4',
                "command": 'shift_southeast_pixels',
                "args": [2]
            },
            {
                "identifier": 'EVENT_3729_action_queue_sync_153_SUBSCRIPT_set_animation_speed_5',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_SLOW, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_3729_action_queue_sync_153_SUBSCRIPT_shift_southeast_pixels_6',
                "command": 'shift_southeast_pixels',
                "args": [2]
            },
            {
                "identifier": 'EVENT_3729_action_queue_sync_153_SUBSCRIPT_transfer_to_xyzf_7',
                "command": 'transfer_to_xyzf',
                "args": [26, 80, 0, RadialDirections.EAST]
            }
        ]
    },
    {
        "identifier": 'EVENT_3729_remember_last_object_154',
        "command": 'remember_last_object'
    },
    {
        "identifier": 'EVENT_3729_action_queue_async_155',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_3729_action_queue_async_155_SUBSCRIPT_reset_properties_0',
                "command": 'reset_properties'
            },
            {
                "identifier": 'EVENT_3729_action_queue_async_155_SUBSCRIPT_pause_1',
                "command": 'pause',
                "args": [30]
            },
            {
                "identifier": 'EVENT_3729_action_queue_async_155_SUBSCRIPT_face_south_2',
                "command": 'face_south'
            }
        ]
    },
    {
        "identifier": 'EVENT_3729_set_action_script_async_156',
        "command": 'set_action_script_async',
        "args": [AreaObjects.MARIO, 395]
    },
    {
        "identifier": 'EVENT_3729_unfreeze_camera_157',
        "command": 'unfreeze_camera'
    },
    {
        "identifier": 'EVENT_3729_set_bit_158',
        "command": 'set_bit',
        "args": [0x7090, 2]
    },
    {
        "identifier": 'EVENT_3729_ret_159',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_3729_fade_in_from_black_async_160',
        "command": 'fade_in_from_black_async'
    },
    {
        "identifier": 'EVENT_3729_ret_161',
        "command": 'ret'
    }
]
