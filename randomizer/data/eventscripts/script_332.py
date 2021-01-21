from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data import items
script = [
    {
        "identifier": 'EVENT_332_jmp_if_bit_clear_0',
        "command": 'jmp_if_bit_clear',
        "args": [0x7081, 6, 'EVENT_256_ret_0']
    },
    {
        "identifier": 'EVENT_332_jmp_if_bit_set_1',
        "command": 'jmp_if_bit_set',
        "args": [0x7082, 2, 'EVENT_256_ret_0']
    },
    {
        "identifier": 'EVENT_332_set_bit_2',
        "command": 'set_bit',
        "args": [0x7082, 2]
    },
    {
        "identifier": 'EVENT_332_remove_from_current_level_3',
        "command": 'remove_from_current_level',
        "args": [AreaObjects.NPC_5]
    },
    {
        "identifier": 'EVENT_332_pause_action_script_4',
        "command": 'pause_action_script',
        "args": [AreaObjects.NPC_8]
    },
    {
        "identifier": 'EVENT_332_action_queue_sync_5',
        "command": 'action_queue_sync',
        "args": [AreaObjects.SCREEN_FOCUS],
        "subscript": [
            {
                "identifier": 'EVENT_332_action_queue_sync_5_SUBSCRIPT_bounce_to_xy_with_height_0',
                "command": 'bounce_to_xy_with_height',
                "args": [16, 104, 4]
            }
        ]
    },
    {
        "identifier": 'EVENT_332_action_queue_async_6',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_8],
        "subscript": [
            {
                "identifier": 'EVENT_332_action_queue_async_6_SUBSCRIPT_set_solidity_bits_0',
                "command": 'set_solidity_bits',
                "args": [[_0x0AFlags.CANT_PASS_WALLS]]
            },
            {
                "identifier": 'EVENT_332_action_queue_async_6_SUBSCRIPT_fixed_f_coord_off_1',
                "command": 'fixed_f_coord_off'
            },
            {
                "identifier": 'EVENT_332_action_queue_async_6_SUBSCRIPT_floating_on_2',
                "command": 'floating_on'
            },
            {
                "identifier": 'EVENT_332_action_queue_async_6_SUBSCRIPT_jump_to_height_silent_3',
                "command": 'jump_to_height_silent',
                "args": [0]
            },
            {
                "identifier": 'EVENT_332_action_queue_async_6_SUBSCRIPT_pause_4',
                "command": 'pause',
                "args": [1]
            },
            {
                "identifier": 'EVENT_332_action_queue_async_6_SUBSCRIPT_db_5',
                "command": 'db',
                "args": [0xfd, 0x3d, 0x1c, 0xaf]
            }
        ]
    },
    {
        "identifier": 'EVENT_332_action_queue_async_7',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_332_action_queue_async_7_SUBSCRIPT_clear_solidity_bits_0',
                "command": 'clear_solidity_bits',
                "args": [[_0x0AFlags.BIT_4, _0x0AFlags.CANT_PASS_NPCS, _0x0AFlags.CANT_WALK_THROUGH, _0x0AFlags.BIT_7]]
            }
        ]
    },
    {
        "identifier": 'EVENT_332_summon_to_current_level_8',
        "command": 'summon_to_current_level',
        "args": [AreaObjects.NPC_10]
    },
    {
        "identifier": 'EVENT_332_summon_to_current_level_9',
        "command": 'summon_to_current_level',
        "args": [AreaObjects.NPC_9]
    },
    {
        "identifier": 'EVENT_332_action_queue_sync_10',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_10],
        "subscript": [
            {
                "identifier": 'EVENT_332_action_queue_sync_10_SUBSCRIPT_reset_properties_0',
                "command": 'reset_properties'
            },
            {
                "identifier": 'EVENT_332_action_queue_sync_10_SUBSCRIPT_visibility_off_1',
                "command": 'visibility_off'
            }
        ]
    },
    {
        "identifier": 'EVENT_332_action_queue_sync_11',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_9],
        "subscript": [
            {
                "identifier": 'EVENT_332_action_queue_sync_11_SUBSCRIPT_reset_properties_0',
                "command": 'reset_properties'
            },
            {
                "identifier": 'EVENT_332_action_queue_sync_11_SUBSCRIPT_face_southwest_1',
                "command": 'face_southwest'
            },
            {
                "identifier": 'EVENT_332_action_queue_sync_11_SUBSCRIPT_visibility_off_2',
                "command": 'visibility_off'
            },
            {
                "identifier": 'EVENT_332_action_queue_sync_11_SUBSCRIPT_transfer_to_xyzf_3',
                "command": 'transfer_to_xyzf',
                "args": [19, 119, 4, RadialDirections.EAST]
            }
        ]
    },
    {
        "identifier": 'EVENT_332_set_12',
        "command": 'set',
        "args": [0x70aa, 28]
    },
    {
        "identifier": 'EVENT_332_set_13',
        "command": 'set',
        "args": [0x70a9, 28]
    },
    {
        "identifier": 'EVENT_332_set_14',
        "command": 'set',
        "args": [0x70a8, 28]
    },
    {
        "identifier": 'EVENT_332_jmp_if_bit_set_15',
        "command": 'jmp_if_bit_set',
        "args": [0x7043, 3, 'EVENT_332_action_queue_async_20']
    },
    {
        "identifier": 'EVENT_332_run_event_as_subroutine_16',
        "command": 'run_event_as_subroutine',
        "args": [260]
    },
    {
        "identifier": 'EVENT_332_run_dialog_17',
        "command": 'run_dialog',
        "args": [599, AreaObjects.MEM_70A8, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]]
    },
    {
        "identifier": 'EVENT_332_remember_last_object_18',
        "command": 'remember_last_object'
    },
    {
        "identifier": 'EVENT_332_unsync_dialog_19',
        "command": 'unsync_dialog'
    },
    {
        "identifier": 'EVENT_332_action_queue_async_20',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_8],
        "subscript": [
            {
                "identifier": 'EVENT_332_action_queue_async_20_SUBSCRIPT_face_southwest_0',
                "command": 'face_southwest'
            }
        ]
    },
    {
        "identifier": 'EVENT_332_action_queue_async_21',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_332_action_queue_async_21_SUBSCRIPT_walk_to_xy_coords_0',
                "command": 'walk_to_xy_coords',
                "args": [19, 119]
            },
            {
                "identifier": 'EVENT_332_action_queue_async_21_SUBSCRIPT_face_northeast_1',
                "command": 'face_northeast'
            }
        ]
    },
    {
        "identifier": 'EVENT_332_action_queue_async_22',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_10],
        "subscript": [
            {
                "identifier": 'EVENT_332_action_queue_async_22_SUBSCRIPT_transfer_to_xyzf_0',
                "command": 'transfer_to_xyzf',
                "args": [19, 119, 4, RadialDirections.EAST]
            },
            {
                "identifier": 'EVENT_332_action_queue_async_22_SUBSCRIPT_shift_southeast_pixels_1',
                "command": 'shift_southeast_pixels',
                "args": [4]
            },
            {
                "identifier": 'EVENT_332_action_queue_async_22_SUBSCRIPT_visibility_on_2',
                "command": 'visibility_on'
            },
            {
                "identifier": 'EVENT_332_action_queue_async_22_SUBSCRIPT_shift_southeast_pixels_3',
                "command": 'shift_southeast_pixels',
                "args": [12]
            },
            {
                "identifier": 'EVENT_332_action_queue_async_22_SUBSCRIPT_face_northeast_4',
                "command": 'face_northeast'
            }
        ]
    },
    {
        "identifier": 'EVENT_332_set_action_script_sync_23',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_8, 99]
    },
    {
        "identifier": 'EVENT_332_pause_24',
        "command": 'pause',
        "args": [20]
    },
    {
        "identifier": 'EVENT_332_run_dialog_25',
        "command": 'run_dialog',
        "args": [600, AreaObjects.MEM_70A8, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]]
    },
    {
        "identifier": 'EVENT_332_pause_action_script_26',
        "command": 'pause_action_script',
        "args": [AreaObjects.NPC_8]
    },
    {
        "identifier": 'EVENT_332_action_queue_async_27',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_8],
        "subscript": [
            {
                "identifier": 'EVENT_332_action_queue_async_27_SUBSCRIPT_floating_on_0',
                "command": 'floating_on'
            },
            {
                "identifier": 'EVENT_332_action_queue_async_27_SUBSCRIPT_set_solidity_bits_1',
                "command": 'set_solidity_bits',
                "args": [[_0x0AFlags.CANT_PASS_WALLS]]
            },
            {
                "identifier": 'EVENT_332_action_queue_async_27_SUBSCRIPT_jump_to_height_silent_2',
                "command": 'jump_to_height_silent',
                "args": [0]
            },
            {
                "identifier": 'EVENT_332_action_queue_async_27_SUBSCRIPT_pause_3',
                "command": 'pause',
                "args": [1]
            },
            {
                "identifier": 'EVENT_332_action_queue_async_27_SUBSCRIPT_db_4',
                "command": 'db',
                "args": [0xfd, 0x3d, 0x1c, 0x0c]
            }
        ]
    },
    {
        "identifier": 'EVENT_332_run_dialog_28',
        "command": 'run_dialog',
        "args": [594, AreaObjects.NPC_10, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]]
    },
    {
        "identifier": 'EVENT_332_action_queue_sync_29',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_10],
        "subscript": [
            {
                "identifier": 'EVENT_332_action_queue_sync_29_SUBSCRIPT_face_northwest_0',
                "command": 'face_northwest'
            },
            {
                "identifier": 'EVENT_332_action_queue_sync_29_SUBSCRIPT_set_sprite_sequence_1',
                "command": 'set_sprite_sequence',
                "args": [7, 0, [_0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_332_action_queue_sync_29_SUBSCRIPT_pause_2',
                "command": 'pause',
                "args": [30]
            },
            {
                "identifier": 'EVENT_332_action_queue_sync_29_SUBSCRIPT_set_sprite_sequence_3',
                "command": 'set_sprite_sequence',
                "args": [4, 0, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_332_action_queue_sync_29_SUBSCRIPT_pause_4',
                "command": 'pause',
                "args": [4]
            },
            {
                "identifier": 'EVENT_332_action_queue_sync_29_SUBSCRIPT_set_sprite_sequence_5',
                "command": 'set_sprite_sequence',
                "args": [2, 2, [_0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_332_action_queue_sync_29_SUBSCRIPT_pause_6',
                "command": 'pause',
                "args": [40]
            },
            {
                "identifier": 'EVENT_332_action_queue_sync_29_SUBSCRIPT_reset_properties_7',
                "command": 'reset_properties'
            },
            {
                "identifier": 'EVENT_332_action_queue_sync_29_SUBSCRIPT_face_northeast_8',
                "command": 'face_northeast'
            }
        ]
    },
    {
        "identifier": 'EVENT_332_action_queue_sync_30',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_332_action_queue_sync_30_SUBSCRIPT_face_southeast_0',
                "command": 'face_southeast'
            },
            {
                "identifier": 'EVENT_332_action_queue_sync_30_SUBSCRIPT_pause_1',
                "command": 'pause',
                "args": [40]
            },
            {
                "identifier": 'EVENT_332_action_queue_sync_30_SUBSCRIPT_start_loop_n_times_2',
                "command": 'start_loop_n_times',
                "args": [1]
            },
            {
                "identifier": 'EVENT_332_action_queue_sync_30_SUBSCRIPT_set_sprite_sequence_3',
                "command": 'set_sprite_sequence',
                "args": [26, 2, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_332_action_queue_sync_30_SUBSCRIPT_pause_4',
                "command": 'pause',
                "args": [2]
            },
            {
                "identifier": 'EVENT_332_action_queue_sync_30_SUBSCRIPT_set_sprite_sequence_5',
                "command": 'set_sprite_sequence',
                "args": [2, 3, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_332_action_queue_sync_30_SUBSCRIPT_pause_6',
                "command": 'pause',
                "args": [2]
            },
            {
                "identifier": 'EVENT_332_action_queue_sync_30_SUBSCRIPT_set_sprite_sequence_7',
                "command": 'set_sprite_sequence',
                "args": [2, 3, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_332_action_queue_sync_30_SUBSCRIPT_pause_8',
                "command": 'pause',
                "args": [2]
            },
            {
                "identifier": 'EVENT_332_action_queue_sync_30_SUBSCRIPT_set_sprite_sequence_9',
                "command": 'set_sprite_sequence',
                "args": [26, 2, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_332_action_queue_sync_30_SUBSCRIPT_pause_10',
                "command": 'pause',
                "args": [2]
            },
            {
                "identifier": 'EVENT_332_action_queue_sync_30_SUBSCRIPT_end_loop_11',
                "command": 'end_loop'
            },
            {
                "identifier": 'EVENT_332_action_queue_sync_30_SUBSCRIPT_visibility_off_12',
                "command": 'visibility_off'
            }
        ]
    },
    {
        "identifier": 'EVENT_332_action_queue_async_31',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_9],
        "subscript": [
            {
                "identifier": 'EVENT_332_action_queue_async_31_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [56]
            },
            {
                "identifier": 'EVENT_332_action_queue_async_31_SUBSCRIPT_visibility_on_1',
                "command": 'visibility_on'
            },
            {
                "identifier": 'EVENT_332_action_queue_async_31_SUBSCRIPT_pause_2',
                "command": 'pause',
                "args": [2]
            },
            {
                "identifier": 'EVENT_332_action_queue_async_31_SUBSCRIPT_start_loop_n_times_3',
                "command": 'start_loop_n_times',
                "args": [5]
            },
            {
                "identifier": 'EVENT_332_action_queue_async_31_SUBSCRIPT_turn_clockwise_45_degrees_n_times_4',
                "command": 'turn_clockwise_45_degrees_n_times',
                "args": [2]
            },
            {
                "identifier": 'EVENT_332_action_queue_async_31_SUBSCRIPT_pause_5',
                "command": 'pause',
                "args": [2]
            },
            {
                "identifier": 'EVENT_332_action_queue_async_31_SUBSCRIPT_end_loop_6',
                "command": 'end_loop'
            },
            {
                "identifier": 'EVENT_332_action_queue_async_31_SUBSCRIPT_stop_sound_7',
                "command": 'stop_sound'
            }
        ]
    },
    {
        "identifier": 'EVENT_332_pause_32',
        "command": 'pause',
        "args": [30]
    },
    {
        "identifier": 'EVENT_332_set_action_script_sync_33',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_8, 99]
    },
    {
        "identifier": 'EVENT_332_pause_34',
        "command": 'pause',
        "args": [30]
    },
    {
        "identifier": 'EVENT_332_run_dialog_35',
        "command": 'run_dialog',
        "args": [595, AreaObjects.MEM_70A8, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]]
    },
    {
        "identifier": 'EVENT_332_action_queue_sync_36',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_9],
        "subscript": [
            {
                "identifier": 'EVENT_332_action_queue_sync_36_SUBSCRIPT_visibility_off_0',
                "command": 'visibility_off'
            },
            {
                "identifier": 'EVENT_332_action_queue_sync_36_SUBSCRIPT_transfer_to_xyzf_1',
                "command": 'transfer_to_xyzf',
                "args": [10, 98, 4, RadialDirections.EAST]
            }
        ]
    },
    {
        "identifier": 'EVENT_332_action_queue_sync_37',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_332_action_queue_sync_37_SUBSCRIPT_reset_properties_0',
                "command": 'reset_properties'
            },
            {
                "identifier": 'EVENT_332_action_queue_sync_37_SUBSCRIPT_face_northeast_1',
                "command": 'face_northeast'
            },
            {
                "identifier": 'EVENT_332_action_queue_sync_37_SUBSCRIPT_visibility_on_2',
                "command": 'visibility_on'
            }
        ]
    },
    {
        "identifier": 'EVENT_332_action_queue_async_38',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_10],
        "subscript": [
            {
                "identifier": 'EVENT_332_action_queue_async_38_SUBSCRIPT_set_sprite_sequence_0',
                "command": 'set_sprite_sequence',
                "args": [5, 0, [_0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_332_action_queue_async_38_SUBSCRIPT_pause_1',
                "command": 'pause',
                "args": [30]
            }
        ]
    },
    {
        "identifier": 'EVENT_332_run_dialog_39',
        "command": 'run_dialog',
        "args": [596, AreaObjects.NPC_10, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]]
    },
    {
        "identifier": 'EVENT_332_pause_40',
        "command": 'pause',
        "args": [20]
    },
    {
        "identifier": 'EVENT_332_pause_action_script_41',
        "command": 'pause_action_script',
        "args": [AreaObjects.NPC_8]
    },
    {
        "identifier": 'EVENT_332_run_event_as_subroutine_42',
        "command": 'run_event_as_subroutine',
        "args": [278]
    },
    {
        "identifier": 'EVENT_332_action_queue_async_43',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_10],
        "subscript": [
            {
                "identifier": 'EVENT_332_action_queue_async_43_SUBSCRIPT_reset_properties_0',
                "command": 'reset_properties'
            }
        ]
    },
    {
        "identifier": 'EVENT_332_pause_44',
        "command": 'pause',
        "args": [30]
    },
    {
        "identifier": 'EVENT_332_run_dialog_45',
        "command": 'run_dialog',
        "args": [597, AreaObjects.MEM_70A8, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]]
    },
    {
        "identifier": 'EVENT_332_action_queue_sync_46',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_10],
        "subscript": [
            {
                "identifier": 'EVENT_332_action_queue_sync_46_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_332_action_queue_sync_46_SUBSCRIPT_set_sprite_sequence_1',
                "command": 'set_sprite_sequence',
                "args": [7, 1, [_0x08Flags.LOOPING_OFF, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_332_action_queue_sync_46_SUBSCRIPT_pause_2',
                "command": 'pause',
                "args": [13]
            },
            {
                "identifier": 'EVENT_332_action_queue_sync_46_SUBSCRIPT_set_sprite_sequence_3',
                "command": 'set_sprite_sequence',
                "args": [8, 1, [_0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_332_action_queue_sync_46_SUBSCRIPT_play_sound_4',
                "command": 'play_sound',
                "args": [Sounds._022_CLOSE_DOOR, 6]
            },
            {
                "identifier": 'EVENT_332_action_queue_sync_46_SUBSCRIPT_pause_5',
                "command": 'pause',
                "args": [50]
            },
            {
                "identifier": 'EVENT_332_action_queue_sync_46_SUBSCRIPT_reset_properties_6',
                "command": 'reset_properties'
            }
        ]
    },
    {
        "identifier": 'EVENT_332_action_queue_async_47',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_332_action_queue_async_47_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_332_action_queue_async_47_SUBSCRIPT_set_sprite_sequence_1',
                "command": 'set_sprite_sequence',
                "args": [7, 2, [_0x08Flags.LOOPING_OFF, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_332_action_queue_async_47_SUBSCRIPT_pause_2',
                "command": 'pause',
                "args": [13]
            },
            {
                "identifier": 'EVENT_332_action_queue_async_47_SUBSCRIPT_set_sprite_sequence_3',
                "command": 'set_sprite_sequence',
                "args": [8, 2, [_0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_332_action_queue_async_47_SUBSCRIPT_pause_4',
                "command": 'pause',
                "args": [50]
            },
            {
                "identifier": 'EVENT_332_action_queue_async_47_SUBSCRIPT_reset_properties_5',
                "command": 'reset_properties'
            }
        ]
    },
    {
        "identifier": 'EVENT_332_pause_48',
        "command": 'pause',
        "args": [60]
    },
    {
        "identifier": 'EVENT_332_run_dialog_49',
        "command": 'run_dialog',
        "args": [567, AreaObjects.NPC_14, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_332_action_queue_sync_50',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_332_action_queue_sync_50_SUBSCRIPT_face_northwest_0',
                "command": 'face_northwest'
            },
            {
                "identifier": 'EVENT_332_action_queue_sync_50_SUBSCRIPT_pause_1',
                "command": 'pause',
                "args": [30]
            },
            {
                "identifier": 'EVENT_332_action_queue_sync_50_SUBSCRIPT_set_sprite_sequence_2',
                "command": 'set_sprite_sequence',
                "args": [7, 2, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_332_action_queue_sync_50_SUBSCRIPT_set_animation_speed_3',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_332_action_queue_sync_50_SUBSCRIPT_play_sound_4',
                "command": 'play_sound',
                "args": [Sounds._000_SILENCE, 6]
            },
            {
                "identifier": 'EVENT_332_action_queue_sync_50_SUBSCRIPT_add_z_coord_1_step_5',
                "command": 'add_z_coord_1_step'
            },
            {
                "identifier": 'EVENT_332_action_queue_sync_50_SUBSCRIPT_dec_z_coord_1_step_6',
                "command": 'dec_z_coord_1_step'
            },
            {
                "identifier": 'EVENT_332_action_queue_sync_50_SUBSCRIPT_set_animation_speed_7',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
            }
        ]
    },
    {
        "identifier": 'EVENT_332_action_queue_sync_51',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_10],
        "subscript": [
            {
                "identifier": 'EVENT_332_action_queue_sync_51_SUBSCRIPT_face_northwest_0',
                "command": 'face_northwest'
            },
            {
                "identifier": 'EVENT_332_action_queue_sync_51_SUBSCRIPT_pause_1',
                "command": 'pause',
                "args": [30]
            },
            {
                "identifier": 'EVENT_332_action_queue_sync_51_SUBSCRIPT_set_sprite_sequence_2',
                "command": 'set_sprite_sequence',
                "args": [9, 1, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_332_action_queue_sync_51_SUBSCRIPT_set_animation_speed_3',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_332_action_queue_sync_51_SUBSCRIPT_add_z_coord_1_step_4',
                "command": 'add_z_coord_1_step'
            },
            {
                "identifier": 'EVENT_332_action_queue_sync_51_SUBSCRIPT_dec_z_coord_1_step_5',
                "command": 'dec_z_coord_1_step'
            },
            {
                "identifier": 'EVENT_332_action_queue_sync_51_SUBSCRIPT_set_animation_speed_6',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
            }
        ]
    },
    {
        "identifier": 'EVENT_332_action_queue_sync_52',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_8],
        "subscript": [
            {
                "identifier": 'EVENT_332_action_queue_sync_52_SUBSCRIPT_fixed_f_coord_off_0',
                "command": 'fixed_f_coord_off'
            },
            {
                "identifier": 'EVENT_332_action_queue_sync_52_SUBSCRIPT_set_solidity_bits_1',
                "command": 'set_solidity_bits',
                "args": [[_0x0AFlags.CANT_PASS_WALLS]]
            },
            {
                "identifier": 'EVENT_332_action_queue_sync_52_SUBSCRIPT_floating_on_2',
                "command": 'floating_on'
            },
            {
                "identifier": 'EVENT_332_action_queue_sync_52_SUBSCRIPT_face_northwest_3',
                "command": 'face_northwest'
            },
            {
                "identifier": 'EVENT_332_action_queue_sync_52_SUBSCRIPT_pause_4',
                "command": 'pause',
                "args": [30]
            },
            {
                "identifier": 'EVENT_332_action_queue_sync_52_SUBSCRIPT_set_animation_speed_5',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_332_action_queue_sync_52_SUBSCRIPT_add_z_coord_1_step_6',
                "command": 'add_z_coord_1_step'
            },
            {
                "identifier": 'EVENT_332_action_queue_sync_52_SUBSCRIPT_dec_z_coord_1_step_7',
                "command": 'dec_z_coord_1_step'
            },
            {
                "identifier": 'EVENT_332_action_queue_sync_52_SUBSCRIPT_set_animation_speed_8',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
            }
        ]
    },
    {
        "identifier": 'EVENT_332_action_queue_async_53',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_9],
        "subscript": [
            {
                "identifier": 'EVENT_332_action_queue_async_53_SUBSCRIPT_visibility_on_0',
                "command": 'visibility_on'
            },
            {
                "identifier": 'EVENT_332_action_queue_async_53_SUBSCRIPT_set_animation_speed_1',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_332_action_queue_async_53_SUBSCRIPT_shift_southeast_steps_2',
                "command": 'shift_southeast_steps',
                "args": [14]
            },
            {
                "identifier": 'EVENT_332_action_queue_async_53_SUBSCRIPT_face_northwest_3',
                "command": 'face_northwest'
            },
            {
                "identifier": 'EVENT_332_action_queue_async_53_SUBSCRIPT_pause_4',
                "command": 'pause',
                "args": [20]
            }
        ]
    },
    {
        "identifier": 'EVENT_332_run_dialog_54',
        "command": 'run_dialog',
        "args": [598, AreaObjects.NPC_9, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]]
    },
    {
        "identifier": 'EVENT_332_action_queue_sync_55',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_9],
        "subscript": [
            {
                "identifier": 'EVENT_332_action_queue_sync_55_SUBSCRIPT_face_southeast_0',
                "command": 'face_southeast'
            },
            {
                "identifier": 'EVENT_332_action_queue_sync_55_SUBSCRIPT_set_animation_speed_1',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_332_action_queue_sync_55_SUBSCRIPT_sequence_looping_on_2',
                "command": 'sequence_looping_on'
            },
            {
                "identifier": 'EVENT_332_action_queue_sync_55_SUBSCRIPT_shift_z_up_pixels_3',
                "command": 'shift_z_up_pixels',
                "args": [8]
            },
            {
                "identifier": 'EVENT_332_action_queue_sync_55_SUBSCRIPT_set_animation_speed_4',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.SLOW, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_332_action_queue_sync_55_SUBSCRIPT_shift_z_up_pixels_5',
                "command": 'shift_z_up_pixels',
                "args": [4]
            },
            {
                "identifier": 'EVENT_332_action_queue_sync_55_SUBSCRIPT_set_animation_speed_6',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_SLOW, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_332_action_queue_sync_55_SUBSCRIPT_shift_z_up_pixels_7',
                "command": 'shift_z_up_pixels',
                "args": [2]
            },
            {
                "identifier": 'EVENT_332_action_queue_sync_55_SUBSCRIPT_pause_8',
                "command": 'pause',
                "args": [8]
            },
            {
                "identifier": 'EVENT_332_action_queue_sync_55_SUBSCRIPT_shift_z_down_pixels_9',
                "command": 'shift_z_down_pixels',
                "args": [2]
            },
            {
                "identifier": 'EVENT_332_action_queue_sync_55_SUBSCRIPT_set_animation_speed_10',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.SLOW, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_332_action_queue_sync_55_SUBSCRIPT_shift_z_down_pixels_11',
                "command": 'shift_z_down_pixels',
                "args": [4]
            },
            {
                "identifier": 'EVENT_332_action_queue_sync_55_SUBSCRIPT_set_animation_speed_12',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_332_action_queue_sync_55_SUBSCRIPT_shift_z_down_pixels_13',
                "command": 'shift_z_down_pixels',
                "args": [8]
            },
            {
                "identifier": 'EVENT_332_action_queue_sync_55_SUBSCRIPT_set_animation_speed_14',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FASTEST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_332_action_queue_sync_55_SUBSCRIPT_play_sound_15',
                "command": 'play_sound',
                "args": [Sounds._011_WHOOSH_AWAY, 6]
            },
            {
                "identifier": 'EVENT_332_action_queue_sync_55_SUBSCRIPT_shift_southeast_steps_16',
                "command": 'shift_southeast_steps',
                "args": [9]
            },
            {
                "identifier": 'EVENT_332_action_queue_sync_55_SUBSCRIPT_visibility_off_17',
                "command": 'visibility_off'
            }
        ]
    },
    {
        "identifier": 'EVENT_332_action_queue_sync_56',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_10],
        "subscript": [
            {
                "identifier": 'EVENT_332_action_queue_sync_56_SUBSCRIPT_reset_properties_0',
                "command": 'reset_properties'
            },
            {
                "identifier": 'EVENT_332_action_queue_sync_56_SUBSCRIPT_pause_1',
                "command": 'pause',
                "args": [56]
            },
            {
                "identifier": 'EVENT_332_action_queue_sync_56_SUBSCRIPT_start_loop_n_times_2',
                "command": 'start_loop_n_times',
                "args": [11]
            },
            {
                "identifier": 'EVENT_332_action_queue_sync_56_SUBSCRIPT_turn_clockwise_45_degrees_n_times_3',
                "command": 'turn_clockwise_45_degrees_n_times',
                "args": [2]
            },
            {
                "identifier": 'EVENT_332_action_queue_sync_56_SUBSCRIPT_pause_4',
                "command": 'pause',
                "args": [3]
            },
            {
                "identifier": 'EVENT_332_action_queue_sync_56_SUBSCRIPT_end_loop_5',
                "command": 'end_loop'
            },
            {
                "identifier": 'EVENT_332_action_queue_sync_56_SUBSCRIPT_start_loop_n_times_6',
                "command": 'start_loop_n_times',
                "args": [7]
            },
            {
                "identifier": 'EVENT_332_action_queue_sync_56_SUBSCRIPT_turn_clockwise_45_degrees_n_times_7',
                "command": 'turn_clockwise_45_degrees_n_times',
                "args": [2]
            },
            {
                "identifier": 'EVENT_332_action_queue_sync_56_SUBSCRIPT_pause_8',
                "command": 'pause',
                "args": [5]
            },
            {
                "identifier": 'EVENT_332_action_queue_sync_56_SUBSCRIPT_end_loop_9',
                "command": 'end_loop'
            },
            {
                "identifier": 'EVENT_332_action_queue_sync_56_SUBSCRIPT_start_loop_n_times_10',
                "command": 'start_loop_n_times',
                "args": [7]
            },
            {
                "identifier": 'EVENT_332_action_queue_sync_56_SUBSCRIPT_turn_clockwise_45_degrees_n_times_11',
                "command": 'turn_clockwise_45_degrees_n_times',
                "args": [2]
            },
            {
                "identifier": 'EVENT_332_action_queue_sync_56_SUBSCRIPT_pause_12',
                "command": 'pause',
                "args": [10]
            },
            {
                "identifier": 'EVENT_332_action_queue_sync_56_SUBSCRIPT_end_loop_13',
                "command": 'end_loop'
            },
            {
                "identifier": 'EVENT_332_action_queue_sync_56_SUBSCRIPT_face_northeast_14',
                "command": 'face_northeast'
            },
            {
                "identifier": 'EVENT_332_action_queue_sync_56_SUBSCRIPT_pause_15',
                "command": 'pause',
                "args": [30]
            },
            {
                "identifier": 'EVENT_332_action_queue_sync_56_SUBSCRIPT_face_northwest_16',
                "command": 'face_northwest'
            },
            {
                "identifier": 'EVENT_332_action_queue_sync_56_SUBSCRIPT_pause_17',
                "command": 'pause',
                "args": [80]
            },
            {
                "identifier": 'EVENT_332_action_queue_sync_56_SUBSCRIPT_set_animation_speed_18',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_332_action_queue_sync_56_SUBSCRIPT_set_sprite_sequence_19',
                "command": 'set_sprite_sequence',
                "args": [5, 0, [_0x08Flags.READ_AS_SEQUENCE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_332_action_queue_sync_57',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_8],
        "subscript": [
            {
                "identifier": 'EVENT_332_action_queue_sync_57_SUBSCRIPT_reset_properties_0',
                "command": 'reset_properties'
            },
            {
                "identifier": 'EVENT_332_action_queue_sync_57_SUBSCRIPT_pause_1',
                "command": 'pause',
                "args": [56]
            },
            {
                "identifier": 'EVENT_332_action_queue_sync_57_SUBSCRIPT_start_loop_n_times_2',
                "command": 'start_loop_n_times',
                "args": [11]
            },
            {
                "identifier": 'EVENT_332_action_queue_sync_57_SUBSCRIPT_turn_clockwise_45_degrees_n_times_3',
                "command": 'turn_clockwise_45_degrees_n_times',
                "args": [6]
            },
            {
                "identifier": 'EVENT_332_action_queue_sync_57_SUBSCRIPT_pause_4',
                "command": 'pause',
                "args": [3]
            },
            {
                "identifier": 'EVENT_332_action_queue_sync_57_SUBSCRIPT_end_loop_5',
                "command": 'end_loop'
            },
            {
                "identifier": 'EVENT_332_action_queue_sync_57_SUBSCRIPT_start_loop_n_times_6',
                "command": 'start_loop_n_times',
                "args": [7]
            },
            {
                "identifier": 'EVENT_332_action_queue_sync_57_SUBSCRIPT_turn_clockwise_45_degrees_n_times_7',
                "command": 'turn_clockwise_45_degrees_n_times',
                "args": [6]
            },
            {
                "identifier": 'EVENT_332_action_queue_sync_57_SUBSCRIPT_pause_8',
                "command": 'pause',
                "args": [5]
            },
            {
                "identifier": 'EVENT_332_action_queue_sync_57_SUBSCRIPT_end_loop_9',
                "command": 'end_loop'
            },
            {
                "identifier": 'EVENT_332_action_queue_sync_57_SUBSCRIPT_start_loop_n_times_10',
                "command": 'start_loop_n_times',
                "args": [7]
            },
            {
                "identifier": 'EVENT_332_action_queue_sync_57_SUBSCRIPT_turn_clockwise_45_degrees_n_times_11',
                "command": 'turn_clockwise_45_degrees_n_times',
                "args": [6]
            },
            {
                "identifier": 'EVENT_332_action_queue_sync_57_SUBSCRIPT_pause_12',
                "command": 'pause',
                "args": [10]
            },
            {
                "identifier": 'EVENT_332_action_queue_sync_57_SUBSCRIPT_end_loop_13',
                "command": 'end_loop'
            },
            {
                "identifier": 'EVENT_332_action_queue_sync_57_SUBSCRIPT_face_southwest_14',
                "command": 'face_southwest'
            }
        ]
    },
    {
        "identifier": 'EVENT_332_action_queue_sync_58',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_332_action_queue_sync_58_SUBSCRIPT_reset_properties_0',
                "command": 'reset_properties'
            },
            {
                "identifier": 'EVENT_332_action_queue_sync_58_SUBSCRIPT_pause_1',
                "command": 'pause',
                "args": [56]
            },
            {
                "identifier": 'EVENT_332_action_queue_sync_58_SUBSCRIPT_start_loop_n_times_2',
                "command": 'start_loop_n_times',
                "args": [11]
            },
            {
                "identifier": 'EVENT_332_action_queue_sync_58_SUBSCRIPT_turn_clockwise_45_degrees_n_times_3',
                "command": 'turn_clockwise_45_degrees_n_times',
                "args": [1]
            },
            {
                "identifier": 'EVENT_332_action_queue_sync_58_SUBSCRIPT_pause_4',
                "command": 'pause',
                "args": [3]
            },
            {
                "identifier": 'EVENT_332_action_queue_sync_58_SUBSCRIPT_end_loop_5',
                "command": 'end_loop'
            },
            {
                "identifier": 'EVENT_332_action_queue_sync_58_SUBSCRIPT_start_loop_n_times_6',
                "command": 'start_loop_n_times',
                "args": [7]
            },
            {
                "identifier": 'EVENT_332_action_queue_sync_58_SUBSCRIPT_turn_clockwise_45_degrees_n_times_7',
                "command": 'turn_clockwise_45_degrees_n_times',
                "args": [1]
            },
            {
                "identifier": 'EVENT_332_action_queue_sync_58_SUBSCRIPT_pause_8',
                "command": 'pause',
                "args": [5]
            },
            {
                "identifier": 'EVENT_332_action_queue_sync_58_SUBSCRIPT_end_loop_9',
                "command": 'end_loop'
            },
            {
                "identifier": 'EVENT_332_action_queue_sync_58_SUBSCRIPT_start_loop_n_times_10',
                "command": 'start_loop_n_times',
                "args": [13]
            },
            {
                "identifier": 'EVENT_332_action_queue_sync_58_SUBSCRIPT_turn_clockwise_45_degrees_n_times_11',
                "command": 'turn_clockwise_45_degrees_n_times',
                "args": [1]
            },
            {
                "identifier": 'EVENT_332_action_queue_sync_58_SUBSCRIPT_pause_12',
                "command": 'pause',
                "args": [10]
            },
            {
                "identifier": 'EVENT_332_action_queue_sync_58_SUBSCRIPT_end_loop_13',
                "command": 'end_loop'
            },
            {
                "identifier": 'EVENT_332_action_queue_sync_58_SUBSCRIPT_set_animation_speed_14',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_332_action_queue_sync_58_SUBSCRIPT_set_sprite_sequence_15',
                "command": 'set_sprite_sequence',
                "args": [7, 2, [_0x08Flags.READ_AS_SEQUENCE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_332_remember_last_object_59',
        "command": 'remember_last_object'
    },
    {
        "identifier": 'EVENT_332_run_dialog_60',
        "command": 'run_dialog',
        "args": [601, AreaObjects.NPC_10, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]]
    },
    {
        "identifier": 'EVENT_332_pause_61',
        "command": 'pause',
        "args": [30]
    },
    {
        "identifier": 'EVENT_332_action_queue_async_62',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_10],
        "subscript": [
            {
                "identifier": 'EVENT_332_action_queue_async_62_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_332_action_queue_async_62_SUBSCRIPT_set_sprite_sequence_1',
                "command": 'set_sprite_sequence',
                "args": [12, 0, [_0x08Flags.READ_AS_MOLD]]
            },
            {
                "identifier": 'EVENT_332_action_queue_async_62_SUBSCRIPT_shift_z_up_pixels_2',
                "command": 'shift_z_up_pixels',
                "args": [10]
            },
            {
                "identifier": 'EVENT_332_action_queue_async_62_SUBSCRIPT_set_animation_speed_3',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_332_action_queue_async_62_SUBSCRIPT_shift_z_up_pixels_4',
                "command": 'shift_z_up_pixels',
                "args": [6]
            },
            {
                "identifier": 'EVENT_332_action_queue_async_62_SUBSCRIPT_set_sprite_sequence_5',
                "command": 'set_sprite_sequence',
                "args": [13, 0, [_0x08Flags.READ_AS_MOLD]]
            },
            {
                "identifier": 'EVENT_332_action_queue_async_62_SUBSCRIPT_set_animation_speed_6',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_332_action_queue_async_62_SUBSCRIPT_dec_z_coord_1_step_7',
                "command": 'dec_z_coord_1_step'
            },
            {
                "identifier": 'EVENT_332_action_queue_async_62_SUBSCRIPT_play_sound_8',
                "command": 'play_sound',
                "args": [Sounds._022_CLOSE_DOOR, 6]
            },
            {
                "identifier": 'EVENT_332_action_queue_async_62_SUBSCRIPT_pause_9',
                "command": 'pause',
                "args": [20]
            },
            {
                "identifier": 'EVENT_332_action_queue_async_62_SUBSCRIPT_set_animation_speed_10',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
            }
        ]
    },
    {
        "identifier": 'EVENT_332_action_queue_async_63',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_332_action_queue_async_63_SUBSCRIPT_reset_properties_0',
                "command": 'reset_properties'
            },
            {
                "identifier": 'EVENT_332_action_queue_async_63_SUBSCRIPT_face_northeast_1',
                "command": 'face_northeast'
            }
        ]
    },
    {
        "identifier": 'EVENT_332_set_action_script_async_64',
        "command": 'set_action_script_async',
        "args": [AreaObjects.MARIO, 671]
    },
    {
        "identifier": 'EVENT_332_remember_last_object_65',
        "command": 'remember_last_object'
    },
    {
        "identifier": 'EVENT_332_action_queue_async_66',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_332_action_queue_async_66_SUBSCRIPT_face_southeast_0',
                "command": 'face_southeast'
            },
            {
                "identifier": 'EVENT_332_action_queue_async_66_SUBSCRIPT_pause_1',
                "command": 'pause',
                "args": [10]
            }
        ]
    },
    {
        "identifier": 'EVENT_332_action_queue_async_67',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_10],
        "subscript": [
            {
                "identifier": 'EVENT_332_action_queue_async_67_SUBSCRIPT_reset_properties_0',
                "command": 'reset_properties'
            },
            {
                "identifier": 'EVENT_332_action_queue_async_67_SUBSCRIPT_shift_northwest_pixels_1',
                "command": 'shift_northwest_pixels',
                "args": [12]
            },
            {
                "identifier": 'EVENT_332_action_queue_async_67_SUBSCRIPT_visibility_off_2',
                "command": 'visibility_off'
            }
        ]
    },
    {
        "identifier": 'EVENT_332_summon_to_current_level_68',
        "command": 'summon_to_current_level',
        "args": [AreaObjects.NPC_5]
    },
    {
        "identifier": 'EVENT_332_set_action_script_sync_69',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_5, 119]
    },
    {
        "identifier": 'EVENT_332_set_action_script_sync_70',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.MARIO, 395]
    },
    {
        "identifier": 'EVENT_332_apply_tile_mod_71',
        "command": 'apply_tile_mod',
        "args": [Rooms._190_MUSHROOM_KINGDOM_DURING_MACK_OUTSIDE, 0, [_0x6AFlags.USE_ALTERNATE]]
    },
    {
        "identifier": 'EVENT_332_apply_tile_mod_72',
        "command": 'apply_tile_mod',
        "args": [Rooms._325_MUSHROOM_KINGDOM_CASTLE_DURING_MACK_MAIN_HALL, 0, [_0x6AFlags.USE_ALTERNATE]]
    },
    {
        "identifier": 'EVENT_332_apply_solidity_mod_73',
        "command": 'apply_solidity_mod',
        "args": [Rooms._190_MUSHROOM_KINGDOM_DURING_MACK_OUTSIDE, 0, [_0x6BFlags.PERMANENT]]
    },
    {
        "identifier": 'EVENT_332_apply_solidity_mod_74',
        "command": 'apply_solidity_mod',
        "args": [Rooms._325_MUSHROOM_KINGDOM_CASTLE_DURING_MACK_MAIN_HALL, 0, [_0x6BFlags.PERMANENT]]
    },
    {
        "identifier": 'EVENT_332_set_bit_75',
        "command": 'set_bit',
        "args": [0x7065, 4]
    },
    {
        "identifier": 'EVENT_332_set_bit_76',
        "command": 'set_bit',
        "args": [0x706d, 4]
    },
    {
        "identifier": 'EVENT_332_clear_bit_77',
        "command": 'clear_bit',
        "args": [0x7043, 3]
    },
    {
        "identifier": 'EVENT_332_remove_from_level_78',
        "command": 'remove_from_level',
        "args": [AreaObjects.NPC_10, Rooms._023_MUSHROOM_KINGDOM_BEFORE_CROCO_OUTSIDE]
    },
    {
        "identifier": 'EVENT_332_remove_from_level_79',
        "command": 'remove_from_level',
        "args": [AreaObjects.NPC_9, Rooms._023_MUSHROOM_KINGDOM_BEFORE_CROCO_OUTSIDE]
    },
    {
        "identifier": 'EVENT_332_ret_80',
        "command": 'ret'
    }
]
